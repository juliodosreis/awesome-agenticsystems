"""scripts/gen_docs.py — the generated blocks and the drift check.

Two things matter here. The generator must never touch hand-written prose
outside its markers, and `--check` must actually fail when the taxonomy moves
without the docs — a check that silently passes is worse than no check, because
CI would then bless a stale issue form.
"""
import json

import pytest

import gen_docs as gd


# --- first_sentence --------------------------------------------------------
# Area blurbs carry the whole rule for picking an area and run long; the issue
# form only has room for the opening claim.

@pytest.mark.parametrize(
    "blurb, expected",
    [
        ("Short one.", "Short one."),
        ("First one. Second one.", "First one."),
        ("No trailing period", "No trailing period"),
        # Newlines from YAML folded scalars must collapse.
        ("Wrapped\n  across lines.", "Wrapped across lines."),
        # A colon inside the first sentence is not a boundary.
        ("A general view: surveys, taxonomies. And more.",
         "A general view: surveys, taxonomies."),
    ],
)
def test_first_sentence(blurb, expected):
    assert gd.first_sentence(blurb) == expected


# --- render ----------------------------------------------------------------

def test_render_replaces_markdown_block(tmp_path):
    path = tmp_path / "doc.md"
    text = "before\n<!-- gen:counts -->\nstale text\n<!-- /gen:counts -->\nafter\n"

    out = gd.render(path, text)

    assert "stale text" not in out
    assert gd.block_counts() in out
    # Hand-written prose on both sides is untouched.
    assert out.startswith("before\n")
    assert out.endswith("after\n")


def test_render_replaces_yaml_block_preserving_indentation(tmp_path):
    path = tmp_path / "form.yml"
    text = (
        "options:\n"
        "        # gen:issue-scale\n"
        "        - stale\n"
        "        # /gen:issue-scale\n"
        "validations:\n"
    )

    out = gd.render(path, text)

    assert "- stale" not in out
    # The options have to stay at list depth or the form stops parsing.
    assert "        - single-agent — One agent acting on its own." in out
    assert out.endswith("validations:\n")


def test_render_is_idempotent(tmp_path):
    path = tmp_path / "doc.md"
    text = "<!-- gen:counts -->\n\n<!-- /gen:counts -->\n"
    once = gd.render(path, text)
    assert gd.render(path, once) == once


def test_render_handles_several_blocks(tmp_path):
    path = tmp_path / "doc.md"
    text = (
        "<!-- gen:counts -->\n\n<!-- /gen:counts -->\n"
        "middle\n"
        "<!-- gen:areas-table -->\n\n<!-- /gen:areas-table -->\n"
    )
    out = gd.render(path, text)
    assert gd.block_counts() in out
    assert "| Layer | Areas |" in out
    assert "middle" in out


def test_render_leaves_unmarked_text_alone(tmp_path):
    path = tmp_path / "doc.md"
    text = "just prose, no markers at all\n"
    assert gd.render(path, text) == text


def test_render_rejects_unknown_block(tmp_path):
    """A typo in a marker would otherwise leave that section stale forever."""
    path = tmp_path / "doc.md"
    text = "<!-- gen:not-a-block -->\n\n<!-- /gen:not-a-block -->\n"
    with pytest.raises(SystemExit) as exc:
        gd.render(path, text)
    assert "unknown generated block" in str(exc.value)
    # The message lists what is available, so the typo is easy to fix.
    assert "areas-table" in str(exc.value)


# --- the blocks themselves -------------------------------------------------

def test_areas_table_covers_every_area():
    table = gd.block_areas_table()
    for area in gd.TAXONOMY["areas"]:
        assert f"`{area}`" in table


def test_facets_table_covers_every_facet_and_value():
    table = gd.block_facets_table()
    for facet, values in gd.TAXONOMY["facets"].items():
        assert f"`{facet}`" in table
        for value in values:
            assert f"`{value}`" in table


def test_issue_options_match_the_taxonomy_exactly():
    """The form must not offer an option the validator would reject."""
    options = gd.block_issue_areas().strip().split("\n")
    offered = [line.strip().lstrip("- ").strip('"').split(" — ")[0] for line in options]
    assert offered == list(gd.TAXONOMY["areas"])


def test_resource_kinds_table_covers_every_kind():
    table = gd.block_resource_kinds()
    for key in gd.TAXONOMY["resource_kinds"]:
        assert f"`{key}`" in table
        assert f"/resources#{key})" in table


def test_issue_resource_kinds_match_the_taxonomy_exactly():
    options = gd.block_issue_resource_kinds().strip().split("\n")
    offered = [line.strip().lstrip("- ").strip('"').split(" — ")[0] for line in options]
    assert offered == list(gd.TAXONOMY["resource_kinds"])


def test_option_with_a_colon_is_quoted_so_it_parses_as_a_string():
    """`- a — b: c` is a one-key mapping in YAML, not a string."""
    import yaml
    block = gd._options(["x"], {"x": "Covers this: and that."})
    assert yaml.safe_load(block) == ["x — Covers this: and that."]


def test_issue_option_descriptions_come_from_the_blurbs():
    line = next(l for l in gd.block_issue_areas().split("\n") if "memory —" in l)
    assert gd.first_sentence(gd.TAXONOMY["areas"]["memory"]["blurb"]) in line


def test_multi_select_descriptions_may_not_contain_a_comma():
    """GitHub joins chosen options with ', ' — a comma inside a description is
    indistinguishable from the separator, so the generator must refuse."""
    with pytest.raises(SystemExit) as exc:
        gd._options(
            ["single-agent"],
            {"single-agent": "One agent, acting alone."},
            multi=True,
        )
    assert "contains a comma" in str(exc.value)


def test_single_select_descriptions_may_contain_a_comma():
    """Area is not multi-select, and its blurbs legitimately use commas."""
    out = gd._options(
        ["foundations"],
        {"foundations": "Surveys, taxonomies, position papers."},
    )
    assert "Surveys, taxonomies, position papers." in out


def test_shipped_taxonomy_passes_the_comma_guard():
    """Guards against someone editing a blurb and breaking the live form."""
    gd.block_issue_scale()
    gd.block_issue_type()


def test_papers_block_skips_captured(tmp_path, monkeypatch):
    import yaml
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "shown-2026.yml").write_text(yaml.safe_dump({
        "id": "shown-2026", "title": "Visible Paper", "year": 2026,
        "area": "memory", "type": ["method"], "status": "triaged",
        "links": {"paper": "https://example.org/a"},
    }), encoding="utf-8")
    (papers / "hidden-2026.yml").write_text(yaml.safe_dump({
        "id": "hidden-2026", "title": "Captured Paper", "year": 2026,
        "status": "captured", "links": {"paper": "https://example.org/b"},
    }), encoding="utf-8")
    monkeypatch.setattr(gd, "PAPERS_DIR", papers)

    block = gd.block_papers()
    # A captured paper has no area, so there is nowhere to list it.
    assert "Visible Paper" in block
    assert "Captured Paper" not in block


def test_papers_block_marks_featured_surveys_and_benchmarks(tmp_path, monkeypatch):
    import yaml
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "marked-2026.yml").write_text(yaml.safe_dump({
        "id": "marked-2026", "title": "Marked Paper", "year": 2026,
        "area": "evaluation", "type": ["survey", "benchmark"],
        "featured": True, "status": "triaged",
        "links": {"paper": "https://example.org/a"},
    }), encoding="utf-8")
    monkeypatch.setattr(gd, "PAPERS_DIR", papers)

    line = next(l for l in gd.block_papers().split("\n") if "Marked Paper" in l)
    for _, symbol, _ in gd.MARKERS:
        assert symbol in line


def test_papers_block_escapes_pipes_in_titles(tmp_path, monkeypatch):
    """A pipe would otherwise break the surrounding markdown."""
    import yaml
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "piped-2026.yml").write_text(yaml.safe_dump({
        "id": "piped-2026", "title": "A | B", "year": 2026,
        "area": "memory", "type": ["method"], "status": "triaged",
        "links": {"paper": "https://example.org/a"},
    }), encoding="utf-8")
    monkeypatch.setattr(gd, "PAPERS_DIR", papers)
    assert r"A \| B" in gd.block_papers()


def test_value_tables_cover_every_type_and_scale():
    for facet, block in (("type", gd.block_type_values), ("scale", gd.block_scale_values)):
        table = block()
        for value in gd.TAXONOMY["facets"][facet]:
            assert f"| `{value}` |" in table


def _write_resource(directory, **fields):
    import yaml
    (directory / f"{fields['id']}.yml").write_text(yaml.safe_dump(fields), encoding="utf-8")


def test_resources_block_groups_by_kind_in_taxonomy_order(tmp_path, monkeypatch):
    resources = tmp_path / "resources"
    resources.mkdir()
    _write_resource(resources, id="zeta", title="Zeta Tool", kind="tool",
                    url="https://example.org/z", org="Org", year=2025,
                    description="Does a thing.")
    _write_resource(resources, id="alpha", title="Alpha Protocol", kind="protocol",
                    url="https://example.org/a", authors=["A. Person"],
                    description="Specifies a thing.")
    monkeypatch.setattr(gd, "RESOURCES_DIR", resources)

    block = gd.block_resources()
    kinds = list(gd.TAXONOMY["resource_kinds"])
    assert kinds.index("protocol") < kinds.index("tool")
    assert block.index("Alpha Protocol") < block.index("Zeta Tool")
    assert "- [Zeta Tool](https://example.org/z) — Org, 2025  \n  Does a thing." in block
    assert "- [Alpha Protocol](https://example.org/a) — A. Person  \n" in block
    # Kinds with nothing in them are named once, as gaps, with no empty heading.
    assert "`framework`" in block.split("**Gaps.**")[1]
    assert "/resources#framework)" not in block


def test_resource_count_names_the_kinds_in_use(tmp_path, monkeypatch):
    resources = tmp_path / "resources"
    resources.mkdir()
    for i in range(2):
        _write_resource(resources, id=f"r{i}", title=f"R{i}", kind="book",
                        url=f"https://example.org/{i}", description="x")
    monkeypatch.setattr(gd, "RESOURCES_DIR", resources)
    total = len(gd.TAXONOMY["resource_kinds"])
    assert gd.block_resource_count() == f"2 resources listed, in 1 of the {total} kinds."


def test_badges_json_is_valid_and_counts_papers():
    payload = json.loads(gd.badges_json())
    assert payload["papers"] == len(gd.load_papers())
    assert payload["resources"] == len(gd.load_resources())
    assert gd.block_paper_total() == str(payload["papers"])
    assert gd.block_resource_total() == str(payload["resources"])
    assert payload["areas"] == len(gd.TAXONOMY["areas"])
    assert payload["topics"] == len(gd.TAXONOMY["topics"])


# --- the drift check -------------------------------------------------------

def test_check_passes_on_the_committed_docs(monkeypatch, capsys):
    """The repository must ship with its generated blocks up to date."""
    monkeypatch.setattr(gd.sys, "argv", ["gen_docs.py", "--check"])
    gd.main()
    assert "in sync" in capsys.readouterr().out


def test_check_fails_when_a_block_is_stale(tmp_path, monkeypatch):
    doc = tmp_path / "doc.md"
    doc.write_text(
        "<!-- gen:counts -->\nsomething stale\n<!-- /gen:counts -->\n",
        encoding="utf-8")
    monkeypatch.setattr(gd, "TARGETS", [doc])
    monkeypatch.setattr(gd, "BADGES_PATH", tmp_path / "badges.json")
    (tmp_path / "badges.json").write_text(gd.badges_json(), encoding="utf-8")
    monkeypatch.setattr(gd.sys, "argv", ["gen_docs.py", "--check"])

    with pytest.raises(SystemExit) as exc:
        gd.main()
    assert "out of sync" in str(exc.value)
    assert "npm run docs" in str(exc.value)
    # --check must not fix anything, or CI would hide the drift.
    assert "something stale" in doc.read_text(encoding="utf-8")


def test_check_fails_when_badges_are_stale(tmp_path, monkeypatch):
    badges = tmp_path / "badges.json"
    badges.write_text('{"papers": 0}\n', encoding="utf-8")
    monkeypatch.setattr(gd, "TARGETS", [])
    monkeypatch.setattr(gd, "BADGES_PATH", badges)
    monkeypatch.setattr(gd.sys, "argv", ["gen_docs.py", "--check"])

    with pytest.raises(SystemExit) as exc:
        gd.main()
    assert "badges.json" in str(exc.value)


def test_write_mode_updates_a_stale_block(tmp_path, monkeypatch):
    doc = tmp_path / "doc.md"
    doc.write_text(
        "keep me\n<!-- gen:counts -->\nstale\n<!-- /gen:counts -->\n",
        encoding="utf-8")
    monkeypatch.setattr(gd, "TARGETS", [doc])
    monkeypatch.setattr(gd, "BADGES_PATH", tmp_path / "badges.json")
    monkeypatch.setattr(gd.sys, "argv", ["gen_docs.py"])

    gd.main()

    written = doc.read_text(encoding="utf-8")
    assert "stale" not in written
    assert "keep me" in written
    assert gd.block_counts() in written
