#!/usr/bin/env python3
"""Fetch paper metadata from the arXiv API.

Shared by add.py (local capture) and process_issue.py (the Issue form), so
that both resolve an arXiv link the same way.

Making this shared is what lets the Issue form treat BibTeX as optional: for
an arXiv link there is nothing a contributor needs to paste by hand.
"""
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

NS = {
    "a": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

API = "https://export.arxiv.org/api/query?id_list={}"


class ArxivError(Exception):
    """arXiv could not resolve the id. The caller decides how to report it."""


def extract_id(raw):
    """Pull the bare arXiv id out of an id, an /abs/ URL or a /pdf/ URL.

    Returns None when there is no arXiv id in the string — the caller uses
    that to decide whether BibTeX is required.
    """
    match = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", raw or "")
    return match.group(1) if match else None


def is_arxiv_link(link):
    return "arxiv.org" in (link or "").lower() and extract_id(link) is not None


def fetch(aid, timeout=30):
    """Return (title, authors, year, venue) for an arXiv id.

    `venue` comes from journal_ref when the paper has been published; it is an
    empty string for a plain preprint, and the caller omits the key entirely
    (the schema rejects an empty venue).
    """
    try:
        with urllib.request.urlopen(API.format(aid), timeout=timeout) as resp:
            root = ET.fromstring(resp.read())
    except (urllib.error.URLError, ET.ParseError) as exc:
        raise ArxivError(f"could not reach the arXiv API for {aid}: {exc}") from exc

    entry = root.find("a:entry", NS)
    # A bad id still returns 200 with an entry whose title is "Error".
    if entry is None or entry.findtext("a:title", "", NS).strip() == "Error":
        raise ArxivError(f"arXiv returned nothing for id {aid}")

    title = " ".join(entry.findtext("a:title", "", NS).split())
    authors = [
        " ".join(a.findtext("a:name", "", NS).split())
        for a in entry.findall("a:author", NS)
    ]
    authors = [a for a in authors if a]
    published = entry.findtext("a:published", "", NS)
    year = int(published[:4]) if published[:4].isdigit() else None
    venue = " ".join(entry.findtext("arxiv:journal_ref", "", NS).split())

    if not title:
        raise ArxivError(f"arXiv returned no title for {aid}")
    return title, authors, year, venue
