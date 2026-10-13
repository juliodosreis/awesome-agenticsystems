#!/usr/bin/env python3
"""Build a resource record from the body of an "Add a Resource" issue.

    python scripts/process_resource_issue.py issue_body.md

The resource counterpart of process_issue.py. A resource has no metadata
source to fetch from, so every field comes from the form: link, name, kind,
description and an optional area. The record carries no `authors`, `org` or
`year`; the reviewer adds them in the pull request when they are known.

issue_ops.yml posts whatever this prints back to the issue, so the messages
are written for the contributor, as in process_issue.py.
"""
import datetime
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from process_issue import check_vocab, field, normalize_title, strip_description  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# The labels of the issue form, .github/ISSUE_TEMPLATE/add_resource.yml.
LINK, NAME, KIND, DESCRIPTION, AREA = (
    "Link", "Name", "Kind", "Description", "Related area (optional)",
)


def slugify(name):
    """`Model Context Protocol (MCP)` -> `model-context-protocol-mcp`."""
    words = re.findall(r"[a-z0-9]+", name.lower())
    return "-".join(words[:6] or ["resource"])


def normalize_url(url):
    """Comparable URL: no scheme, no `www.`, no trailing slash, host lowercased."""
    parsed = urlparse(url.strip())
    host = parsed.netloc.lower().removeprefix("www.")
    return host + parsed.path.rstrip("/") + (f"?{parsed.query}" if parsed.query else "")


def find_duplicate(resources_dir, slug, name, url):
    """The same resource under another name, or the same id for another resource."""
    if (resources_dir / f"{slug}.yml").exists():
        return f"{slug}.yml", "same id"

    target_name, target_url = normalize_title(name), normalize_url(url)
    for path in sorted(resources_dir.glob("*.yml")):
        try:
            existing = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue  # the Astro build reports this file on its own
        if normalize_url(str(existing.get("url", ""))) == target_url:
            return path.name, "same link"
        if normalize_title(str(existing.get("title", ""))) == target_name:
            return path.name, "same name"
    return None


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python process_resource_issue.py <issue_body_file>")

    body = Path(sys.argv[1]).read_text(encoding="utf-8")

    link = field(body, LINK)
    parsed = urlparse(link)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        sys.exit(f"'{LINK}' is not a valid URL: {link!r}")

    name = " ".join(field(body, NAME).split())
    if not name:
        sys.exit(f"'{NAME}' is empty. Add the name of the resource and reopen the issue.")

    description = " ".join(field(body, DESCRIPTION).split())
    if not description:
        sys.exit(
            f"'{DESCRIPTION}' is empty. Add one or two sentences on what the "
            f"resource contains and reopen the issue."
        )

    kind = strip_description(field(body, KIND))
    if not kind:
        sys.exit(f"'{KIND}' is empty. Pick the section of the Resources page and reopen the issue.")
    check_vocab([kind], "resource_kinds", KIND)

    area = strip_description(field(body, AREA))
    if area:
        check_vocab([area], "areas", AREA)

    slug = slugify(name)
    resources_dir = ROOT / "src" / "content" / "resources"
    resources_dir.mkdir(parents=True, exist_ok=True)

    duplicate = find_duplicate(resources_dir, slug, name, link)
    if duplicate:
        existing, reason = duplicate
        sys.exit(
            f"This resource is already listed: src/content/resources/{existing} "
            f"({reason}). If it is missing information, edit that file instead "
            f"of adding a second copy."
        )

    record = {
        "id": slug,
        "title": name,
        "kind": kind,
        "url": link,
        **({"area": area} if area else {}),
        "description": description,
        "added": datetime.date.today().isoformat(),
    }

    path = resources_dir / f"{slug}.yml"
    path.write_text(
        yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Created {path.relative_to(ROOT)}")

    Path("output_slug.txt").write_text(slug)


if __name__ == "__main__":
    main()
