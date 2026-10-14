# Contributing

The repository holds two collections: papers, classified by the taxonomy, and
resources, listed by kind. The differences between them are in the
[README](./README.md#papers-and-resources). This guide covers papers first, and
[Resources](#resources) covers the other collection.

Software repositories do not get a paper record, including when they have an
associated paper. The rule governs what gets a record, and the subject matter
of a paper is unrestricted: a paper describing a framework is recorded with
`type: framework`. AutoGen and MetaGPT are in the collection as papers, and
their repositories can be listed as resources of kind `framework`. A benchmark
with a paper belongs to the `evaluation` area; a leaderboard or an evaluation
harness with no paper is a resource of kind `benchmark`.

## Classification model

A paper is classified on two axes:

- `area` — exactly one. Answers *"what is the contribution?"*.
- `topics` and the facets (<!-- gen:facet-names -->`about`, `scale`, `infra`, `type`, `domain`<!-- /gen:facet-names -->) —
  as many as apply. They answer *"what is it about?"* and cross areas freely.

## Two paths

The path depends on the intended contribution:

| | Who | How | Resulting status |
|---|---|---|---|
| Suggest a paper | Anyone | Issue with 3 fields → reviewed PR | `triaged` — visible on the site |
| Add and read | Anyone willing to clone | Edit the `.yml` and open a pull request | `read` — includes `tldr` and `notes` |

### Issue submission

1. Go to **Issues** → **New Issue** → **Add a Paper**.
2. Paste the link to the paper. An arXiv link supplies the rest: title,
   authors and year are fetched automatically. For
   any other source, paste the **BibTeX** too (most publisher pages have a
   "Cite" or "Export citation" button).
3. Pick **`area`** (see [below](#area-selection)), **`scale`** and
   **`type`**. Each option in the form carries a one-line description. When
   the classification is unclear, pick the closest option: a debatable area
   still records a paper that would otherwise be missing.
4. An automated process reads the metadata, generates the `.yml` file, checks
   that the site still builds and that the tests pass, and opens a **pull
   request** for a maintainer to review. The pull request holds only the new
   `.yml` file, and nothing is merged automatically.

The process stops before opening a pull request when the year is missing, the
link is invalid, a value falls outside the taxonomy, or the paper is already in
the collection, which is checked against the arXiv id and the title as well as
the filename. **The reason is posted as a comment on the issue** and the issue
is labeled `needs-fix`, so it is readable without opening CI logs. Fix the
issue and close/reopen it to retry.

`docs_sync.yml` regenerates the paper list of the README and the badge count on
`main` after the merge, so several pull requests from issues can be open and
merged in any order. GitHub holds `validate.yml` on these pull requests until a
maintainer approves it; approving it is optional, since the intake job ran the
same build and tests before opening the pull request.

### Direct edit

The issue path reaches `triaged`, with no `tldr`, `notes`, `topics` or
`about`, because those come from reading the paper. To add them, edit the
`.yml` file directly and open a pull request.

### Existing records

The same path covers a paper already in the collection: an `area` that fits the
contribution better, missing topics or facets, a `relates_to` link, a `tldr`
written after reading. Edit the file under `src/content/papers/`, commit it on a
branch and open a pull request. `validate.yml` runs the checks listed under
[build validation](./TAXONOMY.md#build-validation) on the pull request, and a
maintainer reviews it before the merge.

Two constraints apply to such an edit. Raising `status` to `read` requires
`tldr`, `topics` and `about` in the same commit, and the build names the missing
field. A `relates_to` link is declared in the newer paper alone; the site
computes the reverse direction, so adding it by hand duplicates the link.

Reporting a problem without editing the file goes through the *Fix a
classification* issue template, described under [questions and
issues](#questions-and-issues). That template records the disagreement on the
paper; the edit to the record is then made by whoever picks the issue up.

See the [local workflow](./TAXONOMY.md#local-workflow) and the
[fields of a record](./TAXONOMY.md#fields-of-a-record).

## Area selection

The criterion for picking an area is the **main contribution** of the paper,
and not its general topic. Each area with its layer and the rule for picking it:

<!-- gen:areas-detail -->
| Area | Layer | Pick it when |
|---|---|---|
| `foundations` | Overview | A general view of the field: surveys, taxonomies, position papers. |
| `reasoning-planning` | Agent capabilities | What happens between the input and the action: reasoning, planning, self-critique. |
| `memory` | Agent capabilities | What the agent stores and how it retrieves it. Vocabulary taken from CoALA. |
| `tools-context` | Agent capabilities | How the agent acts on the world and where it gets context from. |
| `learning-evolution` | Agent capabilities | Changes that persist between tasks: skills, experience, tuning. Learning discarded when the task ends is self-correction and belongs in reasoning-planning. |
| `architectures` | System structure | The complete loop of an agent. A contribution covering one component (memory, planning, tools) belongs to that component instead. |
| `coordination` | System structure | The mechanisms by which several agents divide work and communicate. A system with several agents is recorded as scale: multi-agent, which does not place the paper here. This area holds papers whose contribution is the coordination mechanism itself. |
| `interoperability` | System structure | Standards through which agents and tools locate and communicate with each other. |
| `engineering` | System structure | The runtime substrate around the model, and how it is operated. A harness acts on the reliability of the output, with the model unchanged. |
| `evaluation` | Measurement and control | How an agent or a multi-agent system is measured. |
| `safety` | Measurement and control | Risk, security, trust and control. |
<!-- /gen:areas-detail -->

Every area also has its description on
[`/areas`](https://juliodosreis.com/awesome-agenticsystems/areas).

The number of agents does not decide the area. A paper on memory shared between
agents goes to `memory` with `scale: [multi-agent]`.

## Record states

Recording a paper does not require reading it in full. The schema implements
three states:

<!-- gen:status-table -->
| status | Requires | Effect |
|---|---|---|
| `captured` | metadata only | Kept in git, not visible on the site. |
| `triaged` | `area`, `scale`, `type` | Visible in the index. |
| `read` | `tldr`, `topics`, `about` | Works as a summary on the site. |
<!-- /gen:status-table -->

An issue lands the paper in `triaged`, which is enough for it to appear on the
site, and a record may stay in that state without a time limit. The cost of
suggesting a paper is meant to stay close to zero.

## Resources

The kinds of resource, and what each one covers, are listed under
[Resources](./README.md#resources) in the README.

### Resource submission

1. Go to **Issues** → **New Issue** → **Add a Resource**.
2. Fill in the link, the name, the kind and a description of what the material
   contains. The related area is optional.
3. The intake builds the record with `scripts/process_resource_issue.py` and
   opens a pull request, as for papers. On an invalid link, a kind outside the
   taxonomy, or a resource already listed, it comments the reason on the issue
   and labels it `needs-fix`.

The form does not ask for authors, organization or year. The reviewer adds
`authors` or `org`, and `year`, to the pull request when they are known.

### Resource records

A resource can also arrive as a pull request that adds
`src/content/resources/<id>.yml`:

```yaml
id: langgraph                     # equal to the filename
title: "LangGraph"
kind: framework                   # a key of resource_kinds
url: https://github.com/langchain-ai/langgraph
org: "LangChain"                  # or authors: ["Name"] for a person
year: 2024                        # optional
area: engineering                 # optional
description: >-
  Library for building agents as graphs of nodes over a shared state, with
  checkpointing and interrupts for human review.
added: "2026-10-13"
```

The schema rejects a `kind` or an `area` outside `src/data/taxonomy.yml`, and
`npm run build` reports the valid values. A new kind is added under
`resource_kinds` in the same file, followed by `npm run docs`.

## Questions and issues

- **A misclassified paper.** Open an issue with the *Fix a classification*
  template. Disagreement about an area is recorded as signal on the taxonomy.
  The correction can also arrive as a pull request on the record itself: see
  [existing records](#existing-records).
- **Material that is not a paper.** See [Resources](#resources).
- **A term missing from the vocabulary.** Use the *Propose a taxonomy change*
  template. Adding topics is expected; the criteria are in
  [TAXONOMY.md](./TAXONOMY.md#changing-the-taxonomy).
- **Anything else.** Open a regular issue. Questions from people new to the
  field are welcome, and a guide that leaves a step unclear is a defect in the
  guide.

Participation is covered by the [Code of Conduct](./CODE_OF_CONDUCT.md).

## Further reading

- **[TAXONOMY.md](./TAXONOMY.md)** — The rest of the fields, the behavior of
  topics and facets, the criteria for changing the taxonomy, and the
  bibliography behind it. Read it before filling records in by hand or
  proposing changes to the vocabulary.
- **[`/taxonomy`](https://juliodosreis.com/awesome-agenticsystems/taxonomy)** — The complete vocabulary. Terms nobody
  uses yet are shown in gray and are still valid.
