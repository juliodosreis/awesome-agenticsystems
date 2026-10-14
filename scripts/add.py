#!/usr/bin/env python3
"""Create a paper record from an arXiv id or URL.

    python scripts/add.py 2210.03629
    python scripts/add.py https://arxiv.org/abs/2303.11366
    python scripts/add.py 2210.03629 custom-slug

Downloads title, authors and year from the arXiv API and leaves the
classification fields commented out, with status: captured. You pick area,
scale and type.

A `captured` paper is valid but does not show up on the site: it is a saved
link. To get it into the index, uncomment area/scale/type and switch status
to `triaged`.
"""
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import arxiv  # noqa: E402  (same directory, must follow the path insert)

ROOT = Path(__file__).resolve().parent.parent
STOP = {"a", "an", "the", "of", "for", "and", "with", "in", "on", "to", "via"}


def slugify(title, year):
    head = re.split(r"[:\-–]", title)[0].lower()
    words = [w for w in re.findall(r"[a-z0-9]+", head) if w not in STOP]
    return "-".join(words[:4] or ["paper"]) + (f"-{year}" if year else "")


def yaml_list(values):
    return "[" + ", ".join(values) + "]"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    aid = arxiv.extract_id(sys.argv[1])
    if not aid:
        sys.exit(f"Could not extract an arXiv id from '{sys.argv[1]}'")

    try:
        title, authors, year, venue = arxiv.fetch(aid)
    except arxiv.ArxivError as exc:
        sys.exit(str(exc))
    if not year:
        sys.exit(f"arXiv returned no year for {aid}, and the schema requires one")

    slug = sys.argv[2] if len(sys.argv) > 2 else slugify(title, year)
    path = ROOT / "src" / "content" / "papers" / f"{slug}.yml"
    if path.exists():
        sys.exit(f"{path.relative_to(ROOT)} already exists")

    quoted = [json.dumps(a) for a in authors]
    # journal_ref is only set once the paper is published; for a preprint the
    # key is omitted, because the schema rejects an empty venue.
    venue_line = f"venue: {json.dumps(venue)}\n" if venue else "# venue: \"\"   # fill in once published\n"

    # Classification fields stay commented out: an empty `area:` is null and the
    # schema rejects it. Commented, the stub is always valid as `captured`.
    path.write_text(
        f"id: {slug}\n"
        f"title: {json.dumps(title)}\n"
        f"authors: {yaml_list(quoted)}\n"
        f"year: {year}\n"
        f"{venue_line}"
        f'arxiv: "{aid}"\n'
        f"links:\n"
        f"  paper: https://arxiv.org/abs/{aid}\n\n"
        f"# --- triage: uncomment these three and set status: triaged ---\n"
        f"# area:            # see src/data/taxonomy.yml\n"
        f"# scale: []        # single-agent | multi-agent | human-agent\n"
        f"# type: []         # survey | method | benchmark | framework | ...\n\n"
        f"# --- once you have read it: fill these in and set status: read ---\n"
        f"# topics: []\n# about: []\n# infra: []\n# domain: [general]\n"
        f'# tldr: ""\n# notes: ""\n# relates_to: []\n# evaluated_on: []\n\n'
        f"status: captured\n"
        f"added: {datetime.date.today().isoformat()}\n",
        encoding="utf-8",
    )
    print(f"created {path.relative_to(ROOT)} — now fill in area, scale and type")


if __name__ == "__main__":
    main()
