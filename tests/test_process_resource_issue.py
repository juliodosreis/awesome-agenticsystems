"""scripts/process_resource_issue.py — the intake path for resources.

Same contract as process_issue.py: the failure messages are posted back to the
contributor verbatim, so the tests assert on them as well as on the record.
"""
import sys

import pytest
import yaml

import process_resource_issue as pr


BODY = """### Link

https://github.com/langchain-ai/langgraph

### Name

LangGraph

### Kind

framework — Code frameworks for orchestrating agents: control flow, state, tool calls and multi-agent workflows.

### Description

Library for building agents as graphs of nodes over a shared state,
with checkpointing.

### Related area (optional)

engineering — The runtime substrate around the model, and how it is operated.
"""


@pytest.fixture
def resources_dir(repo):
    path = repo / "src" / "content" / "resources"
    path.mkdir(parents=True)
    return path


@pytest.fixture(autouse=True)
def isolate(monkeypatch, repo, tmp_path):
    """Write into the temporary tree, never into the repository."""
    monkeypatch.setattr(pr, "ROOT", repo)
    monkeypatch.chdir(tmp_path)


def run(body, tmp_path):
    path = tmp_path / "issue_body.md"
    path.write_text(body, encoding="utf-8")
    sys.argv = ["process_resource_issue.py", str(path)]
    pr.main()


def fails_with(body, tmp_path):
    with pytest.raises(SystemExit) as exc:
        run(body, tmp_path)
    return str(exc.value)


def record(resources_dir, slug):
    return yaml.safe_load((resources_dir / f"{slug}.yml").read_text(encoding="utf-8"))


def test_slugify_keeps_words_and_drops_punctuation():
    assert pr.slugify("Model Context Protocol (MCP)") == "model-context-protocol-mcp"
    assert pr.slugify("LangGraph") == "langgraph"
    assert pr.slugify("!!!") == "resource"


def test_normalize_url_ignores_scheme_www_and_trailing_slash():
    assert pr.normalize_url("https://www.Example.com/a/") == pr.normalize_url("http://example.com/a")


def test_record_has_the_form_fields(resources_dir, tmp_path):
    run(BODY, tmp_path)
    data = record(resources_dir, "langgraph")
    assert data["id"] == "langgraph"
    assert data["title"] == "LangGraph"
    assert data["kind"] == "framework"
    assert data["url"] == "https://github.com/langchain-ai/langgraph"
    assert data["area"] == "engineering"
    # The textarea wraps lines; the description is stored as one line.
    assert data["description"] == (
        "Library for building agents as graphs of nodes over a shared state, with checkpointing."
    )
    assert "added" in data
    assert (tmp_path / "output_slug.txt").read_text() == "langgraph"


def test_area_left_blank_is_omitted(resources_dir, tmp_path):
    body = BODY.split("### Related area")[0] + "### Related area (optional)\n\n_No response_\n"
    run(body, tmp_path)
    assert "area" not in record(resources_dir, "langgraph")


def test_rejects_link_that_is_not_a_url(resources_dir, tmp_path):
    body = BODY.replace("https://github.com/langchain-ai/langgraph", "langgraph")
    assert "not a valid URL" in fails_with(body, tmp_path)


def test_rejects_kind_outside_the_taxonomy(resources_dir, tmp_path):
    body = BODY.replace("framework — Code", "frameworks — Code")
    message = fails_with(body, tmp_path)
    assert "frameworks is not part of resource_kinds" in message
    assert "Valid values: protocol, framework" in message


def test_rejects_empty_description(resources_dir, tmp_path):
    body = BODY.split("### Description")[0] + (
        "### Description\n\n_No response_\n\n### Related area (optional)\n\n_No response_\n"
    )
    assert "'Description' is empty" in fails_with(body, tmp_path)


def test_rejects_duplicate_by_link(resources_dir, tmp_path):
    (resources_dir / "lang-graph.yml").write_text(
        "id: lang-graph\ntitle: Something else\nurl: https://www.github.com/langchain-ai/langgraph/\n"
    )
    message = fails_with(BODY, tmp_path)
    assert "lang-graph.yml" in message and "same link" in message


def test_rejects_duplicate_by_name(resources_dir, tmp_path):
    (resources_dir / "lg.yml").write_text("id: lg\ntitle: LANGGRAPH\nurl: https://example.com/\n")
    message = fails_with(BODY, tmp_path)
    assert "lg.yml" in message and "same name" in message


def test_nothing_is_written_when_validation_fails(resources_dir, tmp_path):
    fails_with(BODY.replace("framework — Code", "frameworks — Code"), tmp_path)
    assert list(resources_dir.glob("*.yml")) == []


def test_form_labels_match_the_issue_template():
    """A renamed form field would make every submission fail as 'empty'."""
    from conftest import REPO_ROOT

    form = yaml.safe_load(
        (REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "add_resource.yml").read_text(encoding="utf-8")
    )
    labels = {b["attributes"]["label"] for b in form["body"] if b["type"] != "markdown"}
    assert {pr.LINK, pr.NAME, pr.KIND, pr.DESCRIPTION, pr.AREA} == labels
