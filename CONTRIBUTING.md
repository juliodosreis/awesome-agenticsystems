# Contributing

This guide covers papers. Resources (orchestration frameworks, skills,
benchmarks without a paper, protocols, books, courses and guides) have their
own path, described under [Resources](./README.md#resources) in the README,
together with a table of the differences between the two collections.

This is a collection of **papers**. Software repositories do not get a paper
record, including when they have an associated paper. They go to the
[Resources page](./README.md#resources), together with skills, benchmarks
without a paper, protocols, books, courses and guides.

The rule governs what gets a record. The subject matter of a paper is
unrestricted: a paper describing a framework belongs here, recorded as
`type: framework`. AutoGen and MetaGPT are both in the collection as papers;
their repositories are not. A benchmark with a paper counts as a paper and
belongs to the `evaluation` area; a leaderboard or an evaluation harness with no
paper is a resource of kind `benchmark`.

[Issue submission](#issue-submission) takes one minute and needs no setup. The
sections after it cover filling records in by hand.

## Classification model

A paper is classified on two axes:

- `area` — exactly one. Answers *"what is the contribution?"*.
- `topics` and the facets (<!-- gen:facet-names -->`about`, `scale`, `infra`, `type`, `domain`<!-- /gen:facet-names -->) —
  as many as apply. They answer *"what is it about?"* and cross areas freely.

An issue submission requires three fields: `area`, `scale` and `type`. The rest
are optional and get filled in later, while reading the paper.

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
   **`type`**. Each option in the form carries a one-line description.
4. An automated process reads the metadata, generates the `.yml` file, checks
   that the site still builds and that the tests pass, and opens a **pull
   request** for a maintainer to review. The pull request holds only the new
   `.yml` file, and nothing is merged automatically.

This path requires no clone and no local setup.

When the classification is unclear, pick the closest option. The pull request
is reviewed before it is merged, and a debatable area still records a paper
that would otherwise be missing.

The submission is validated before any pull request is opened. The process
stops when the year is missing, the link is invalid, a value falls outside the
taxonomy, or the paper is already in the collection, which is checked against
the arXiv id and the title as well as the filename. The site is then built with
the new record and the test suite is run. The pull request is opened only when
both succeed.

**A failure is posted as a comment on the issue** and the issue is labeled
`needs-fix`, so the reason is readable without opening CI logs. Fix the issue
and close/reopen it to retry.

### Direct edit

The issue path reaches `triaged`, with no `tldr`, `notes`, `topics` or
`about`, because those come from reading the paper. To add them, edit the
`.yml` file directly and open a pull request. This path is open to anyone with
a clone and requires no maintainer status. The issue form omits those fields
deliberately, since they can only be filled in after reading.

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

The areas are grouped into layers. The criterion for picking one is the
**main contribution** of the paper, and not its general topic.

<!-- gen:areas-table -->
| Layer | Areas |
|---|---|
| Overview | `foundations` |
| Agent capabilities | `reasoning-planning`, `memory`, `tools-context`, `learning-evolution` |
| System structure | `architectures`, `coordination`, `interoperability`, `engineering` |
| Measurement and control | `evaluation`, `safety` |
<!-- /gen:areas-table -->

Each area with the rule for picking it:

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
[`/areas`](https://juliodosreis.github.io/awesome-agenticsystems/areas).

Two rules that resolve most ambiguous cases:

- **Scale does not define the area.** A multi-agent system does not
  automatically belong to `coordination`; the count of agents is recorded by
  `scale: [multi-agent]`. `coordination` holds work whose central contribution
  is the coordination mechanism itself. A paper on shared memory, for example, goes
  to `memory` with `scale: [multi-agent]`.
- **`architectures` means the whole loop.** If the contribution is one
  component (memory, planning, tool use), it belongs to that component.

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

The schema enforces the states. Declaring `status: read` without a `tldr`
breaks the build, with a message naming the missing field and offering
`triaged` as the state that does not require it.

## Questions and issues

- **A misclassified paper.** Open an issue with the *Fix a classification*
  template. Disagreement about an area is recorded as signal on the taxonomy.
  The correction can also arrive as a pull request on the record itself: see
  [existing records](#existing-records).
- **Material that is not a paper.** Use the *Add a Resource* template, or
  open a pull request that adds a file to `src/content/resources/`. The kinds
  and the record format are in the [README](./README.md#resources).
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
- **[`/taxonomy`](https://juliodosreis.github.io/awesome-agenticsystems/taxonomy)** — The complete vocabulary. Terms nobody
  uses yet are shown in gray and are still valid.
