#!/usr/bin/env python3
"""Build a paper record from the body of an "Add a Paper" issue.

    python scripts/process_issue.py issue_body.md

Metadata comes from arXiv when the link points there, and from the pasted
BibTeX otherwise. BibTeX is optional on purpose: asking a newcomer to produce
one was the highest barrier in the whole flow, and for an arXiv link there is
nothing to paste.

Fails loudly on anything that would break the Astro build (missing year,
invalid link, area/level/type outside the taxonomy, duplicate paper). A failed
Action beats a pull request that does not compile — and issue_ops.yml posts
whatever this prints back to the issue, so the messages are written for the
contributor, not for a log.
"""
import datetime
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import arxiv  # noqa: E402  (same directory, must follow the path insert)

ROOT = Path(__file__).resolve().parent.parent
TAXONOMY = yaml.safe_load((ROOT / "src" / "data" / "taxonomy.yml").read_text(encoding="utf-8"))
STOP = {"a", "an", "the", "of", "for", "and", "with", "in", "on", "to", "via"}


def slugify(title, year):
    head = re.split(r"[:\-–]", title)[0].lower()
    words = [w for w in re.findall(r"[a-z0-9]+", head) if w not in STOP]
    return "-".join(words[:4] or ["paper"]) + (f"-{year}" if year else "")


def field(body, label):
    """Read one field of the issue form (`### Label` followed by the value)."""
    match = re.search(rf"### {re.escape(label)}\s*\n+(.*?)(?=\n### |\Z)", body, re.DOTALL)
    value = match.group(1).strip() if match else ""
    # GitHub writes this placeholder for every optional field left blank.
    return "" if value.startswith("_No response_") else value


def strip_description(option):
    """Drop the description from a dropdown option.

    The issue form shows `memory — what the agent remembers...` so that the
    contributor can tell the options apart without leaving the page, but only
    the part before the em dash is the taxonomy value. gen_docs.py writes
    these options, so the separator is fixed on both sides.
    """
    return option.split(" — ", 1)[0].strip()


def multi(body, label):
    """Same, for dropdowns with `multiple: true`.

    Values are comma-separated, and each may carry an em-dash description.
    Descriptions themselves never contain a comma followed by a space plus
    another option, so splitting on "," and then stripping is safe — but we
    split on the em dash first to be sure a description with a comma in it
    cannot leak into the value.
    """
    raw = field(body, label)
    return [strip_description(v) for v in raw.split(",") if strip_description(v)]


def normalize_title(title):
    """Comparable title: no punctuation, no case, no repeated whitespace."""
    return " ".join(re.findall(r"[a-z0-9]+", title.lower()))


def find_duplicate(papers_dir, slug, title, arxiv_id):
    """Catch the same paper submitted twice under slightly different titles.

    Comparing slugs alone is not enough: a BibTeX that includes the subtitle
    produces a different slug and the duplicate sails through the build. We
    also compare the arXiv id and the normalized title.
    """
    if (papers_dir / f"{slug}.yml").exists():
        return f"{slug}.yml", "same slug"

    target = normalize_title(title)
    for path in sorted(papers_dir.glob("*.yml")):
        try:
            existing = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue  # the Astro build will complain about this file anyway
        if arxiv_id and str(existing.get("arxiv", "")).strip() == arxiv_id:
            return path.name, f"same arXiv id ({arxiv_id})"
        if normalize_title(str(existing.get("title", ""))) == target:
            return path.name, "same title"
    return None


def check_vocab(values, vocab_path, label):
    """A value outside the taxonomy breaks the Astro build; stop before that."""
    allowed = TAXONOMY
    for part in vocab_path.split("."):
        allowed = allowed[part]
    allowed = list(allowed.keys()) if isinstance(allowed, dict) else allowed
    bad = [v for v in values if v not in allowed]
    if bad:
        sys.exit(
            f"{label}: {', '.join(bad)} is not part of {vocab_path} "
            f"(src/data/taxonomy.yml). Valid values: {', '.join(allowed)}"
        )


def parse_bibtex(body):
    """Return the first BibTeX entry in the issue, or None if there is none."""
    # The form labels the field "BibTeX (optional)", so the heading can carry
    # text after the word. Matching only "### BibTeX\n" dropped every pasted
    # entry and sent non-arXiv submissions to the "paste the BibTeX" error.
    raw = re.search(r"### BibTeX[^\n]*\n+```[a-z]*\n(.*?)\n```", body, re.DOTALL)
    if not raw:
        raw = re.search(r"### BibTeX[^\n]*\n+(.*?)(?=\n### |\Z)", body, re.DOTALL)
    if not raw:
        return None
    text = raw.group(1).strip()
    if not text or text.startswith("_No response_"):
        return None

    import bibtexparser  # imported late: not needed on the arXiv path

    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    database = bibtexparser.loads(text, parser=parser)
    if not database.entries:
        sys.exit(
            "I could not parse the BibTeX block. Check that it is a complete "
            "entry, from @article{ to the closing brace."
        )
    return database.entries[0]


def clean(value):
    return " ".join(str(value).replace("{", "").replace("}", "").split())


def display_name(author):
    """BibTeX "Last, First" to the "First Last" every other record uses."""
    author = clean(author)
    if author.count(",") == 1:
        last, first = (part.strip() for part in author.split(","))
        return f"{first} {last}" if first else last
    return author


def metadata_from_bibtex(entry):
    title = clean(entry.get("title", ""))
    if not title:
        sys.exit("The BibTeX entry has no 'title'.")

    # The schema requires year as a number. No year, no valid record.
    year_raw = entry.get("year", "").strip()
    if not year_raw.isdigit():
        sys.exit(
            f"The BibTeX entry has no numeric 'year' (found: {year_raw!r}). "
            f"Add it and reopen the issue."
        )

    authors_raw = " ".join(entry.get("author", "").split())
    authors = [display_name(a) for a in authors_raw.split(" and ") if a.strip()]
    venue = clean(
        entry.get("journal") or entry.get("booktitle") or entry.get("publisher") or ""
    )
    return title, authors, int(year_raw), venue


def metadata_from_arxiv(aid):
    try:
        title, authors, year, venue = arxiv.fetch(aid)
    except arxiv.ArxivError as exc:
        sys.exit(
            f"{exc}. Check the link, or paste the BibTeX in the issue so the "
            f"metadata can be read from there instead."
        )
    if not year:
        sys.exit(f"arXiv returned no year for {aid}, and the schema requires one.")
    return title, authors, year, venue


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python process_issue.py <issue_body_file>")

    body = Path(sys.argv[1]).read_text(encoding="utf-8")

    link = field(body, "Link to the paper")
    parsed = urlparse(link)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        sys.exit(f"'Link to the paper' is not a valid URL: {link!r}")

    arxiv_id = arxiv.extract_id(link) if arxiv.is_arxiv_link(link) else None
    entry = parse_bibtex(body)

    # BibTeX wins when both are present: a contributor who bothered to paste it
    # usually did so because the arXiv version is not the one to cite.
    if entry:
        title, authors, year, venue = metadata_from_bibtex(entry)
    elif arxiv_id:
        title, authors, year, venue = metadata_from_arxiv(arxiv_id)
    else:
        sys.exit(
            "I need either an arXiv link or a BibTeX block. The link you gave "
            f"({link}) is not an arXiv one, so paste the paper's BibTeX in the "
            "issue and reopen it. Most publisher pages have a 'Cite' or "
            "'Export citation' button that gives you one."
        )

    authors = authors or ["Unknown Author"]

    area = strip_description(field(body, "Area"))
    scale = multi(body, "Scale")
    type_ = multi(body, "Type")
    check_vocab([area], "areas", "Area")
    check_vocab(scale, "facets.scale", "Scale")
    check_vocab(type_, "facets.type", "Type")

    slug = slugify(title, year)
    papers_dir = ROOT / "src" / "content" / "papers"
    path = papers_dir / f"{slug}.yml"

    duplicate = find_duplicate(papers_dir, slug, title, arxiv_id)
    if duplicate:
        name, reason = duplicate
        sys.exit(
            f"This paper is already in the collection: src/content/papers/{name} "
            f"({reason}). If it is missing information, edit that file instead "
            f"of adding a second copy."
        )

    # area + level + type is exactly what the schema asks for `triaged`, so the
    # paper shows up in the index as soon as the pull request is merged.
    record = {
        "id": slug,
        "title": title,
        "authors": authors,
        "year": year,
        # venue and arxiv only when present: the schema rejects an empty venue,
        # which also rendered a stray separator on the card.
        **({"venue": venue} if venue else {}),
        **({"arxiv": arxiv_id} if arxiv_id else {}),
        "links": {"paper": link},
        "area": area,
        "scale": scale,
        "type": type_,
        "topics": [],
        "about": [],
        "infra": [],
        "domain": ["general"],
        "status": "triaged",
        "added": datetime.date.today().isoformat(),
    }

    # yaml.safe_dump quotes titles containing colons or quotes, which broke the
    # file when it was written by hand.
    path.write_text(
        yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Created {path.relative_to(ROOT)}")

    Path("output_slug.txt").write_text(slug)


if __name__ == "__main__":
    main()
