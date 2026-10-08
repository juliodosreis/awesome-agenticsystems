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


# -> se a API do arXiv retornar erro 406, a função abaixo pode funcionar
# 1- comente a função fetch original e descomente essa
# 2- salve o arquivo 
# 3- dê o comando no terminal: pip install requests
# 4- feche o terminal e abra novamente
# 5- use normalmente

# import requests
# def fetch(aid, timeout=30):
#     """Return (title, authors, year, venue) by parsing the arXiv HTML directly."""
#     url = f"https://arxiv.org/abs/{aid}"
    
#     try:
#         # Acessa a página principal de visualização do paper, que não bloqueia requisições 
#         # comuns da mesma forma que o endpoint export.arxiv.org/api
#         resp = requests.get(
#             url, 
#             timeout=timeout,
#             headers={
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#                 'Accept-Language': 'en-US,en;q=0.5',
#             }
#         )
#         resp.raise_for_status()
#         html = resp.text
#     except requests.exceptions.RequestException as exc:
#         raise ArxivError(f"could not reach arxiv.org for {aid}: {exc}") from exc

#     # Extração de Título via metadados embutidos na página
#     title_match = re.search(r'<meta\s+name="citation_title"\s+content="([^"]+)"', html)
#     if not title_match:
#         raise ArxivError(f"arXiv returned no title for id {aid}")
#     title = " ".join(title_match.group(1).replace('\n', ' ').split())

#     # Extração de Autores
#     authors_raw = re.findall(r'<meta\s+name="citation_author"\s+content="([^"]+)"', html)
#     authors = []
#     for a in authors_raw:
#         # O arXiv formata a tag como "Sobrenome, Nome", vamos inverter para "Nome Sobrenome"
#         if "," in a:
#             parts = a.split(",", 1)
#             authors.append(f"{parts[1].strip()} {parts[0].strip()}")
#         else:
#             authors.append(a.strip())

#     # Extração de Ano
#     date_match = re.search(r'<meta\s+name="citation_date"\s+content="(\d{4})[^"]*"', html)
#     year = int(date_match.group(1)) if date_match else None

#     # Extração de Venue (Referência de publicação, se existir)
#     venue_match = re.search(r'<td class="tablecell jref">([^<]+)</td>', html)
#     venue = " ".join(venue_match.group(1).split()) if venue_match else ""

#     if not title:
#         raise ArxivError(f"arXiv returned no title for {aid}")
        
#     return title, authors, year, venue