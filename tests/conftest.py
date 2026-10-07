"""Shared fixtures.

The scripts under test read and write inside the repository: process_issue.py
writes a record into src/content/papers, gen_docs.py rewrites the guides. None
of the tests are allowed to touch the real files, so the fixtures here point
each script at a temporary tree instead.

What they deliberately do NOT fake is src/data/taxonomy.yml. Both scripts load
it at import time from the real path, so the tests validate against the project's
actual vocabulary — a test suite that passed against a toy taxonomy would not
tell us the issue form still matches the validator.
"""
import shutil
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"

# The scripts import each other by bare name (process_issue does `import arxiv`),
# so scripts/ has to be importable as a directory.
sys.path.insert(0, str(SCRIPTS))


@pytest.fixture
def repo(tmp_path):
    """A throwaway repo root with an empty papers directory.

    Returns the path. Point a script's ROOT at this and it will write here.
    """
    (tmp_path / "src" / "content" / "papers").mkdir(parents=True)
    (tmp_path / "src" / "data").mkdir(parents=True)
    shutil.copy(
        REPO_ROOT / "src" / "data" / "taxonomy.yml",
        tmp_path / "src" / "data" / "taxonomy.yml",
    )
    return tmp_path


@pytest.fixture
def papers_dir(repo):
    return repo / "src" / "content" / "papers"


@pytest.fixture
def issue_body():
    """Build an issue body the way GitHub renders the Add a Paper form.

    Fields default to a valid submission; pass None to drop a field entirely,
    which is how GitHub represents one the user left blank on a required-false
    input.
    """
    def build(
        link="https://arxiv.org/abs/2305.16291",
        bibtex="_No response_",
        area="learning-evolution — Changes that persist BETWEEN tasks.",
        scale="single-agent — One agent acting on its own.",
        type_="method — Proposes a new technique.",
    ):
        sections = [
            ("Link to the paper", link),
            ("BibTeX (optional)", bibtex),
            ("Area", area),
            ("Scale", scale),
            ("Type", type_),
        ]
        return "\n".join(
            f"### {name}\n\n{value}\n"
            for name, value in sections
            if value is not None
        )

    return build


@pytest.fixture
def fake_arxiv(monkeypatch):
    """Replace arxiv.fetch so no test depends on the network.

    Worth doing beyond the usual reasons: the real API rate-limits with a 429
    when called repeatedly, which a test suite absolutely would.
    """
    import arxiv

    calls = []

    def fetch(aid, timeout=30):
        calls.append(aid)
        if aid in fetch.missing:
            raise arxiv.ArxivError(f"arXiv returned nothing for id {aid}")
        return fetch.result

    fetch.result = (
        "Voyager: An Open-Ended Embodied Agent with Large Language Models",
        ["Guanzhi Wang", "Yuqi Xie"],
        2023,
        "",
    )
    fetch.missing = set()
    fetch.calls = calls
    monkeypatch.setattr(arxiv, "fetch", fetch)
    return fetch


BIBTEX = """```bibtex
@inproceedings{doe2024something,
  title={Some Paper About Agent Memory},
  author={Jane Doe and John Roe},
  booktitle={NeurIPS 2024},
  year={2024}
}
```"""
