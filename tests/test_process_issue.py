"""scripts/process_issue.py — the unsupervised path.

This is the script that runs with no human watching: it turns an issue into a
record and its failure messages are posted back to the contributor verbatim.
So the tests assert on the messages too, not only on the exit status — a
correct rejection with an unusable explanation is still a bad outcome for
somebody new to the project.
"""
import yaml
import pytest

import process_issue as pi
from conftest import BIBTEX


@pytest.fixture(autouse=True)
def isolate(monkeypatch, repo, tmp_path):
    """Write into the temporary tree, never into the repository."""
    monkeypatch.setattr(pi, "ROOT", repo)
    # main() drops output_slug.txt in the working directory for the workflow.
    monkeypatch.chdir(tmp_path)


def run(body, tmp_path):
    path = tmp_path / "issue_body.md"
    path.write_text(body, encoding="utf-8")
    monkey_argv = ["process_issue.py", str(path)]
    import sys
    sys.argv = monkey_argv
    pi.main()


def record(papers_dir, slug):
    return yaml.safe_load((papers_dir / f"{slug}.yml").read_text(encoding="utf-8"))


def fails_with(body, tmp_path):
    with pytest.raises(SystemExit) as exc:
        run(body, tmp_path)
    return str(exc.value)


# --- helpers ---------------------------------------------------------------

def test_strip_description_keeps_only_the_value():
    # The issue form shows "value — description"; only the part before the em
    # dash is taxonomy vocabulary.
    assert pi.strip_description("memory — What the agent remembers.") == "memory"
    assert pi.strip_description("memory") == "memory"
    assert pi.strip_description("  memory  ") == "memory"
    # A hyphen inside the value is not the separator.
    assert pi.strip_description("single-agent — One agent.") == "single-agent"


def test_field_treats_no_response_as_empty():
    body = "### BibTeX\n\n_No response_\n\n### Area\n\nmemory\n"
    assert pi.field(body, "BibTeX") == ""
    assert pi.field(body, "Area") == "memory"
    assert pi.field(body, "Missing Field") == ""


def test_normalize_title_ignores_punctuation_and_case():
    assert pi.normalize_title("Some Brand-New Paper!") == \
           pi.normalize_title("some brand new paper")


# --- metadata: the arXiv path ---------------------------------------------

def test_arxiv_link_needs_no_bibtex(issue_body, papers_dir, fake_arxiv, tmp_path):
    """The whole point of 2.1: an arXiv link is enough on its own."""
    run(issue_body(), tmp_path)

    data = record(papers_dir, "voyager-2023")
    assert data["title"].startswith("Voyager")
    assert data["authors"] == ["Guanzhi Wang", "Yuqi Xie"]
    assert data["year"] == 2023
    assert data["arxiv"] == "2305.16291"
    assert fake_arxiv.calls == ["2305.16291"]


def test_arxiv_record_is_triaged_with_the_three_fields(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    run(issue_body(), tmp_path)
    data = record(papers_dir, "voyager-2023")

    # area + level + type is exactly what the schema requires for `triaged`,
    # which is what makes the paper visible once the PR merges.
    assert data["status"] == "triaged"
    assert data["area"] == "learning-evolution"
    assert data["scale"] == ["single-agent"]
    assert data["type"] == ["method"]
    # Filled in later, by whoever reads the paper.
    assert data["topics"] == []
    assert data["about"] == []


def test_multi_select_values_are_split_and_stripped(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    """GitHub joins chosen options with ', ' and each carries a description."""
    run(issue_body(
        scale="single-agent — One agent acting on its own., "
              "human-agent — A human is part of the loop.",
        type_="benchmark — Introduces a dataset or an evaluation suite., "
              "empirical — Measures or compares existing approaches.",
    ), tmp_path)

    data = record(papers_dir, "voyager-2023")
    assert data["scale"] == ["single-agent", "human-agent"]
    assert data["type"] == ["benchmark", "empirical"]


def test_options_without_descriptions_still_work(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    """Old issues predate the generated descriptions; they must not break."""
    run(issue_body(area="memory", scale="single-agent", type_="method"), tmp_path)
    assert record(papers_dir, "voyager-2023")["area"] == "memory"


def test_empty_venue_key_is_omitted(issue_body, papers_dir, fake_arxiv, tmp_path):
    # The schema rejects venue: "", and it rendered a stray separator on cards.
    fake_arxiv.result = ("A Preprint", ["Someone"], 2026, "")
    run(issue_body(), tmp_path)
    assert "venue" not in record(papers_dir, "preprint-2026")


def test_venue_is_kept_when_arxiv_has_one(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    fake_arxiv.result = ("A Published Paper", ["Someone"], 2026, "ICLR 2026")
    run(issue_body(), tmp_path)
    assert record(papers_dir, "published-paper-2026")["venue"] == "ICLR 2026"


# --- metadata: the BibTeX path --------------------------------------------

def test_non_arxiv_link_uses_bibtex(issue_body, papers_dir, tmp_path):
    run(issue_body(
        link="https://aclanthology.org/2024.emnlp-main.1/",
        bibtex=BIBTEX,
        area="memory — What the agent remembers.",
    ), tmp_path)

    data = record(papers_dir, "some-paper-about-agent-2024")
    assert data["title"] == "Some Paper About Agent Memory"
    assert data["authors"] == ["Jane Doe", "John Roe"]
    assert data["year"] == 2024
    assert data["venue"] == "NeurIPS 2024"
    # No arXiv id to record for a non-arXiv link.
    assert "arxiv" not in data


def test_bibtex_wins_over_arxiv(issue_body, papers_dir, fake_arxiv, tmp_path):
    """Somebody who pasted BibTeX usually meant the published version."""
    run(issue_body(bibtex=BIBTEX), tmp_path)

    data = record(papers_dir, "some-paper-about-agent-2024")
    assert data["title"] == "Some Paper About Agent Memory"
    # The arXiv id still comes from the link, so the record keeps both.
    assert data["arxiv"] == "2305.16291"
    assert fake_arxiv.calls == []


def test_bibtex_without_fences_is_accepted(issue_body, papers_dir, tmp_path):
    """Contributors paste BibTeX with and without a code fence."""
    raw = ("@article{x, title={Fenceless Entry}, "
           "author={Ann Author}, year={2025}}")
    run(issue_body(link="https://example.org/paper", bibtex=raw), tmp_path)
    assert record(papers_dir, "fenceless-entry-2025")["year"] == 2025


def test_bibtex_last_first_names_are_reordered(issue_body, papers_dir, tmp_path):
    """BibTeX writes "Last, First"; the records use "First Last"."""
    raw = ("@article{x, title={Name Order}, "
           "author={Li, Hao and Ann Author and {van der Laan}, Vincent}, year={2025}}")
    run(issue_body(link="https://example.org/paper", bibtex=raw), tmp_path)
    assert record(papers_dir, "name-order-2025")["authors"] == [
        "Hao Li", "Ann Author", "Vincent van der Laan"]


# --- rejections: each one is posted back to the contributor ---------------

def test_rejects_link_that_is_not_a_url(issue_body, tmp_path):
    message = fails_with(issue_body(link="just some text"), tmp_path)
    assert "not a valid URL" in message


def test_rejects_neither_arxiv_nor_bibtex(issue_body, tmp_path):
    message = fails_with(
        issue_body(link="https://aclanthology.org/2024.emnlp-main.1/"), tmp_path)
    # The message has to say what to do next, not just what went wrong.
    assert "arXiv link or a BibTeX" in message
    assert "Export citation" in message


def test_rejects_unresolvable_arxiv_id(issue_body, fake_arxiv, tmp_path):
    fake_arxiv.missing = {"2305.16291"}
    message = fails_with(issue_body(), tmp_path)
    assert "returned nothing" in message
    assert "paste the BibTeX" in message


def test_rejects_unparseable_bibtex(issue_body, tmp_path):
    message = fails_with(
        issue_body(bibtex="```\nthis is not bibtex\n```"), tmp_path)
    assert "could not parse the BibTeX" in message


def test_rejects_bibtex_without_year(issue_body, tmp_path):
    # The schema requires year as a number; there is no valid record without one.
    raw = "@article{x, title={No Year Here}, author={Ann Author}}"
    message = fails_with(
        issue_body(link="https://example.org/p", bibtex=raw), tmp_path)
    assert "numeric 'year'" in message


def test_rejects_area_outside_the_taxonomy(issue_body, fake_arxiv, tmp_path):
    # The classic mistake the area/level split exists to prevent.
    message = fails_with(issue_body(area="multi-agent"), tmp_path)
    assert "not part of areas" in message
    # Listing the valid values is what makes the rejection actionable.
    assert "learning-evolution" in message


def test_rejects_scale_outside_the_taxonomy(issue_body, fake_arxiv, tmp_path):
    message = fails_with(issue_body(scale="two-agent"), tmp_path)
    assert "not part of facets.scale" in message
    assert "single-agent" in message


def test_nothing_is_written_when_validation_fails(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    """A rejected submission must not leave a half-record behind."""
    fails_with(issue_body(area="multi-agent"), tmp_path)
    assert list(papers_dir.glob("*.yml")) == []


# --- duplicates ------------------------------------------------------------

def existing(papers_dir, **fields):
    data = {"id": "existing-2023", "title": "An Existing Paper",
            "arxiv": "1111.11111", "status": "triaged"}
    data.update(fields)
    path = papers_dir / f"{data['id']}.yml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


def test_rejects_duplicate_by_slug(issue_body, papers_dir, fake_arxiv, tmp_path):
    existing(papers_dir, id="voyager-2023", title="Voyager: Something Else")
    message = fails_with(issue_body(), tmp_path)
    assert "already in the collection" in message
    assert "same slug" in message


def test_rejects_duplicate_by_arxiv_id(issue_body, papers_dir, fake_arxiv, tmp_path):
    """Same paper, different title — the slug check alone would miss it."""
    existing(papers_dir, title="A Completely Different Title",
             arxiv="2305.16291")
    message = fails_with(issue_body(), tmp_path)
    assert "same arXiv id (2305.16291)" in message


def test_rejects_duplicate_by_normalized_title(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    """A BibTeX carrying the subtitle produces a different slug."""
    existing(papers_dir, id="voyager-open-ended-2023",
             title="Voyager: An Open-Ended Embodied Agent with Large Language Models!",
             arxiv="9999.99999")
    message = fails_with(issue_body(), tmp_path)
    assert "same title" in message


def test_unreadable_yml_does_not_block_a_submission(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    """A broken file is the Astro build's problem, not this script's."""
    (papers_dir / "broken.yml").write_text("{{ not: valid: yaml", encoding="utf-8")
    run(issue_body(), tmp_path)
    assert (papers_dir / "voyager-2023.yml").exists()


# --- the workflow contract -------------------------------------------------

def test_slug_is_written_for_the_workflow(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    run(issue_body(), tmp_path)
    assert (tmp_path / "output_slug.txt").read_text() == "voyager-2023"


def test_title_with_a_colon_is_quoted(
        issue_body, papers_dir, fake_arxiv, tmp_path):
    """Titles with colons broke the file when it was written by hand."""
    run(issue_body(), tmp_path)
    # Round-tripping through the YAML parser is the actual check.
    assert record(papers_dir, "voyager-2023")["title"] == \
        "Voyager: An Open-Ended Embodied Agent with Large Language Models"
