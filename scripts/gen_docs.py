#!/usr/bin/env python3
"""Regenerate the parts of the docs and the issue form that come from the taxonomy.

    python scripts/gen_docs.py           # rewrite the generated blocks
    python scripts/gen_docs.py --check   # fail if any block is stale (used by CI)

The vocabulary used to be copied by hand into README.md, CONTRIBUTING.md,
TAXONOMY.md and the issue form — four copies of the same tables, plus counts
like "58 topics" hardcoded in three places. They drift the moment anyone edits
taxonomy.yml, and a stale issue form is worse than stale prose: it offers an
option the validator will then reject.

Everything between a pair of markers is owned by this script:

    <!-- gen:areas-table -->  ...  <!-- /gen:areas-table -->   (markdown)
    # gen:areas  ...  # /gen:areas                             (yaml)

Text outside the markers is written by hand and never touched.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TAXONOMY = yaml.safe_load((ROOT / "src" / "data" / "taxonomy.yml").read_text(encoding="utf-8"))
SITE = "https://juliodosreis.github.io/awesome-agenticsystems"
PAPERS_DIR = ROOT / "src" / "content" / "papers"

# Markers on a listing entry. Everyone who browses these repos on GitHub scans
# for exactly this: what is a survey (where to start), what is a benchmark
# (how things are measured), and what the maintainers consider essential.
MARKERS = [
    ("featured", "🔥", "essential"),
    ("survey", "📖", "survey"),
    ("benchmark", "⚖️", "benchmark"),
]


def load_papers():
    """Every record on disk, sorted the way the listing shows them.

    `captured` papers are skipped for the same reason the site skips them:
    they have no area yet, so there is nowhere to list them.
    """
    papers = []
    for path in sorted(PAPERS_DIR.glob("*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if data.get("status") == "captured":
            continue
        papers.append(data)
    return papers


def rel(path):
    """Path for display, relative to the repo when it is inside it.

    Plain `relative_to` raises for anything outside ROOT, which meant the code
    building an error message could itself crash with a ValueError — losing the
    actual error. Falls back to the full path.
    """
    try:
        return str(Path(path).relative_to(ROOT))
    except ValueError:
        return str(path)


def first_sentence(text):
    """The opening claim of a blurb.

    Area blurbs carry the rule for picking that area and can run long; the
    issue form and the compact tables only have room for the first sentence.
    Every blurb in taxonomy.yml is written so that sentence stands alone.
    """
    text = " ".join(str(text).split())
    match = re.match(r"^(.+?\.)(?:\s|$)", text)
    return match.group(1) if match else text


# --- block builders --------------------------------------------------------
# Each returns the body that goes between the markers, without trailing
# newline. The key is the name used in the marker.


def block_counts():
    facet_values = sum(len(v) for v in TAXONOMY["facets"].values())
    return (
        f"{len(TAXONOMY['areas'])} areas in {len(TAXONOMY['groups'])} layers, "
        f"{len(TAXONOMY['topics'])} topics and {facet_values} facet values "
        f"across {len(TAXONOMY['facets'])} facets."
    )


def block_areas_table():
    """Layer -> areas. The table used to choose an area at a glance."""
    rows = ["| Layer | Areas |", "|---|---|"]
    for key, group in TAXONOMY["groups"].items():
        areas = [a for a, v in TAXONOMY["areas"].items() if v["group"] == key]
        rows.append(f"| {group['label']} | {', '.join(f'`{a}`' for a in areas)} |")
    return "\n".join(rows)


def block_areas_detail():
    """Every area with the rule for picking it. The full reference."""
    rows = ["| Area | Layer | Pick it when |", "|---|---|---|"]
    for key, area in TAXONOMY["areas"].items():
        group = TAXONOMY["groups"][area["group"]]["label"]
        blurb = " ".join(str(area["blurb"]).split())
        rows.append(f"| `{key}` | {group} | {blurb} |")
    return "\n".join(rows)


def block_facet_names():
    """Just the facet names, inline.

    This list was written by hand in three places, and when `capability` became
    `about` and `level` became `scale` two of them were missed — nothing was
    watching. Generating it is the same reason every other block here exists.
    """
    return ", ".join(f"`{f}`" for f in TAXONOMY["facets"])


def block_facets_table():
    rows = ["| Facet | Allowed values | Use |", "|---|---|---|"]
    for facet, values in TAXONOMY["facets"].items():
        blurb = " ".join(str(TAXONOMY["facet_blurbs"][facet]).split())
        listed = ", ".join(f"`{v}`" for v in values)
        rows.append(f"| `{facet}` | {listed} | {blurb} |")
    return "\n".join(rows)


def block_status_table():
    rows = ["| status | Requires | Effect |", "|---|---|---|"]
    requires = {
        "captured": "metadata only",
        "triaged": "`area`, `scale`, `type`",
        "read": "`tldr`, `topics`, `about`",
    }
    for state in TAXONOMY["status"]:
        blurb = " ".join(str(TAXONOMY["status_blurbs"][state]).split())
        rows.append(f"| `{state}` | {requires.get(state, '')} | {blurb} |")
    return "\n".join(rows)


def block_references_table():
    rows = ["| Reference | What it supports |", "|---|---|"]
    for ref in TAXONOMY["references"]:
        used = " ".join(str(ref["used_for"]).split())
        rows.append(f"| [{ref['cite']}]({ref['url']}) | {used} |")
    return "\n".join(rows)


def block_resource_kinds():
    """Every resource kind with its blurb, in the order of the /resources page."""
    rows = ["| Kind | Section on the site | Covers |", "|---|---|---|"]
    for key, kind in TAXONOMY["resource_kinds"].items():
        blurb = " ".join(str(kind["blurb"]).split())
        link = f"[{kind['label']}]({SITE}/resources#{key})"
        rows.append(f"| `{key}` | {link} | {blurb} |")
    return "\n".join(rows)


def _paper_line(paper):
    """One listing entry: markers, linked title, year, venue, one-line summary."""
    marks = ""
    for key, symbol, _ in MARKERS:
        hit = paper.get("featured") if key == "featured" else key in (paper.get("type") or [])
        if hit:
            marks += symbol + " "

    title = str(paper.get("title", "")).replace("|", "\\|")
    link = (paper.get("links") or {}).get("paper", "")
    year = paper.get("year", "")
    venue = paper.get("venue", "")

    where = f"`{venue}`" if venue else f"`{year}`"
    line = f"- {marks}[{title}]({link}) — {where}"
    if venue:
        line += f" · {year}"

    tldr = " ".join(str(paper.get("tldr", "")).split())
    if tldr:
        line += f"  \n  {tldr}"
    return line


def block_papers():
    """The collection itself, grouped by layer and area.

    Without this the README shows process documentation and zero content,
    which is the opposite of how anyone actually finds one of these repos.
    The data is already structured, so the listing costs nothing to keep
    current — it is regenerated from the same .yml files the site reads.
    """
    papers = load_papers()
    out = []

    legend = " · ".join(f"{symbol} {label}" for _, symbol, label in MARKERS)
    out.append(f"*{legend}. Surveys first within each area, then newest first.*")

    for group_key, group in TAXONOMY["groups"].items():
        area_keys = [a for a, v in TAXONOMY["areas"].items() if v["group"] == group_key]
        in_group = [p for p in papers if p.get("area") in area_keys]
        if not in_group:
            continue

        out.append(f"\n### {group['label']}\n")
        out.append(f"{group['blurb']}\n")

        for area_key in area_keys:
            in_area = [p for p in papers if p.get("area") == area_key]
            if not in_area:
                continue
            # Surveys are the way into an area, so they go first; after that,
            # newest first. Same order the site uses.
            in_area.sort(
                key=lambda p: (
                    0 if "survey" in (p.get("type") or []) else 1,
                    -(p.get("year") or 0),
                    str(p.get("title", "")),
                )
            )
            label = TAXONOMY["areas"][area_key]["label"]
            out.append(f"#### {label} ([`{area_key}`]({SITE}/areas/{area_key}))\n")
            out.extend(_paper_line(p) for p in in_area)
            out.append("")

    empty = [a for a in TAXONOMY["areas"] if not any(p.get("area") == a for p in papers)]
    if empty:
        out.append(
            "\n> **Gaps.** No papers yet in "
            + ", ".join(f"`{a}`" for a in empty)
            + ". The areas exist in the taxonomy before anything lives in them — "
            "the gap is a reading list, and a good place to make a first "
            "contribution."
        )

    return "\n".join(out).rstrip()


def block_paper_count():
    papers = load_papers()
    read = sum(1 for p in papers if p.get("status") == "read")
    return f"{len(papers)} papers listed, {read} of them with a written summary."


def _options(values, blurbs, indent="        ", multi=False):
    """Issue-form dropdown options: `value — one-line description`.

    process_issue.py splits on the em dash and keeps the value, so the
    description is free: the contributor reads what each option means without
    leaving the form, which is where they were guessing before.

    For a `multiple: true` dropdown GitHub joins the picked options with
    ", ", and there is no way to tell that separator apart from a comma inside
    a description. Rather than leave that as a trap for whoever next edits a
    blurb, we refuse to generate such an option at all: the failure lands here,
    with a clear message, instead of on a contributor whose valid submission
    gets rejected.
    """
    lines = []
    for value in values:
        blurb = first_sentence(blurbs.get(value, ""))
        if multi and "," in blurb:
            sys.exit(
                f"value_blurbs for '{value}' contains a comma: {blurb!r}\n"
                f"This facet is a multi-select dropdown, and GitHub joins the "
                f"chosen options with ', ' — a comma inside a description "
                f"cannot be told apart from that separator. Rewrite the "
                f"description without a comma."
            )
        option = f"{value} — {blurb}" if blurb else value
        # A ": " inside a plain scalar turns the option into a one-key
        # mapping, and the form then holds an object where GitHub expects a
        # string. JSON string syntax is valid YAML double-quoted syntax.
        if ": " in option or " #" in option:
            option = json.dumps(option, ensure_ascii=False)
        lines.append(f"{indent}- {option}")
    return "\n".join(lines)


def block_issue_areas():
    blurbs = {k: v["blurb"] for k, v in TAXONOMY["areas"].items()}
    return _options(list(TAXONOMY["areas"]), blurbs)


def block_issue_scale():
    return _options(
        TAXONOMY["facets"]["scale"], TAXONOMY["value_blurbs"]["scale"], multi=True
    )


def block_issue_type():
    return _options(
        TAXONOMY["facets"]["type"], TAXONOMY["value_blurbs"]["type"], multi=True
    )


def block_issue_resource_kinds():
    blurbs = {k: v["blurb"] for k, v in TAXONOMY["resource_kinds"].items()}
    return _options(list(TAXONOMY["resource_kinds"]), blurbs)


BLOCKS = {
    "papers": block_papers,
    "paper-count": block_paper_count,
    "counts": block_counts,
    "areas-table": block_areas_table,
    "areas-detail": block_areas_detail,
    "facet-names": block_facet_names,
    "facets-table": block_facets_table,
    "status-table": block_status_table,
    "references-table": block_references_table,
    "resource-kinds": block_resource_kinds,
    "issue-areas": block_issue_areas,
    "issue-scale": block_issue_scale,
    "issue-type": block_issue_type,
    "issue-resource-kinds": block_issue_resource_kinds,
}

TARGETS = [
    ROOT / "README.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "TAXONOMY.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "add_paper.yml",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "add_resource.yml",
]


def render(path, text):
    """Replace the body of every marked block in `text`."""
    yaml_style = path.suffix in (".yml", ".yaml")
    if yaml_style:
        pattern = re.compile(
            r"(?P<open>[ \t]*# gen:(?P<name>[a-z-]+)[ \t]*\n)"
            r".*?"
            r"(?P<close>[ \t]*# /gen:(?P=name)[ \t]*(?:\n|$))",
            re.DOTALL,
        )
    else:
        pattern = re.compile(
            r"(?P<open><!-- gen:(?P<name>[a-z-]+) -->\n?)"
            r".*?"
            r"(?P<close><!-- /gen:(?P=name) -->)",
            re.DOTALL,
        )

    unknown = []

    def replace(match):
        name = match.group("name")
        if name not in BLOCKS:
            unknown.append(name)
            return match.group(0)
        opened = match.group("open")
        # A block marker ends its line; an inline one does not, and adding a
        # newline there would break the sentence it sits in.
        tail = "\n" if opened.endswith("\n") else ""
        return opened + BLOCKS[name]() + tail + match.group("close")

    result = pattern.sub(replace, text)
    if unknown:
        sys.exit(
            f"{rel(path)}: unknown generated block(s): "
            f"{', '.join(sorted(set(unknown)))}. Known: {', '.join(sorted(BLOCKS))}"
        )
    return result


BADGES_PATH = ROOT / ".github" / "badges.json"


def badges_json():
    """Counts for the shields.io badges in the README.

    shields.io can read a value out of a JSON file in the repo, which keeps the
    badge honest without a service to run: the number updates in the same
    commit that adds the paper, because `npm run docs` writes both.
    """
    papers = load_papers()
    payload = {
        "papers": len(papers),
        "read": sum(1 for p in papers if p.get("status") == "read"),
        "areas": len(TAXONOMY["areas"]),
        "topics": len(TAXONOMY["topics"]),
    }
    return json.dumps(payload, indent=2) + "\n"


def main():
    check = "--check" in sys.argv[1:]
    stale = []

    current = BADGES_PATH.read_text(encoding="utf-8") if BADGES_PATH.exists() else ""
    updated = badges_json()
    if current != updated:
        if check:
            stale.append(rel(BADGES_PATH))
        else:
            BADGES_PATH.write_text(updated, encoding="utf-8")
            print(f"updated {rel(BADGES_PATH)}")

    for path in TARGETS:
        if not path.exists():
            continue
        current = path.read_text(encoding="utf-8")
        updated = render(path, current)
        if current == updated:
            continue
        if check:
            stale.append(rel(path))
        else:
            path.write_text(updated, encoding="utf-8")
            print(f"updated {rel(path)}")

    if check and stale:
        sys.exit(
            "These files are out of sync with src/data/taxonomy.yml:\n  - "
            + "\n  - ".join(stale)
            + "\n\nRun `npm run docs` and commit the result."
        )
    if check:
        print("docs are in sync with src/data/taxonomy.yml")
    elif not stale:
        print("done")


if __name__ == "__main__":
    main()
