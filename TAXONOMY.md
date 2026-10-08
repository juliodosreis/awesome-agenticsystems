# The taxonomy

How the vocabulary is structured, why, and what it takes to change it.

To add a paper quickly, see [CONTRIBUTING.md](./CONTRIBUTING.md). This guide is
for filling records in by hand and for proposing changes to the vocabulary.

Current size:

<!-- gen:counts -->
11 areas in 4 layers, 58 topics and 33 facet values across 5 facets.
<!-- /gen:counts -->

## Vocabulary surfaces

Three surfaces, all generated from the same YAML file:

| Surface | Location |
|---|---|
| The complete vocabulary, with usage counts | [`/taxonomy`](https://juliodosreis.github.io/awesome-agenticsystems/taxonomy) — terms nobody uses yet are shown in gray and are still valid. |
| The areas with their descriptions, grouped by layer | [`/areas`](https://juliodosreis.github.io/awesome-agenticsystems/areas) — empty areas have a dashed border. |
| The source of truth, with a comment explaining each decision | [`src/data/taxonomy.yml`](./src/data/taxonomy.yml) |

Terms outside this vocabulary are not accepted: the build rejects unknown
values and prints the list of valid ones.

## The four vocabularies

The word *layer* has one meaning throughout this project: one of the four
navigation groups (Overview, Agent capabilities, …). The table below covers a
different axis, the four kinds of vocabulary a record draws on.

| Vocabulary | Definition | Per paper |
|---|---|---|
| `groups` | The navigation layers. Derived from the area. | — |
| `areas` | Criterion: *"what is the contribution?"* | **Exactly 1** |
| `topics` | Flat, global list. | 0..n |
| `facets` | <!-- gen:facet-names -->`about`, `scale`, `infra`, `type`, `domain`<!-- /gen:facet-names -->. | 0..n |

## Fields of a record

| Field | Required | Meaning |
|---|---|---|
| `status` | All states | `captured`, `triaged` or `read`. Sets what else is required — see [Record states](./CONTRIBUTING.md#record-states). |
| `id` | All states | Paper identifier. **Must equal the filename** — the build enforces this. |
| `title`, `authors`, `year` | All states | Metadata. `year` must be a number. |
| `links.paper` | All states | Main URL. `links.code` is optional. |
| `venue`, `arxiv` | Optional | Shown on the record when present. An empty `venue` is rejected — omit the key instead. |
| `area` | From `triaged` | **Exactly one.** See [CONTRIBUTING](./CONTRIBUTING.md#area-selection). |
| `scale` | From `triaged` | The scale of the system studied. |
| `type` | From `triaged` | `survey` records are pinned to the top of their area. |
| `topics` | From `read` | Flat, global vocabulary. Not restricted by area. |
| `about` | From `read` | Transversal facet. Answers *"what is it about?"*, not *"what is the contribution?"*. |
| `tldr` | From `read` | One or two sentences. Shown on the listing cards. |
| `notes` | Optional | The reading of the paper. Shown only on the detail page. |
| `infra`, `domain` | Optional | Facets. `domain` generates the `/domains` pages. |
| `relates_to` | Optional | Ids of other papers. Builds the **reading path**. See below. |
| `evaluated_on` | Optional | Ids of benchmarks (which must exist as papers). |
| `featured` | Optional | Sorts the paper first in the listing. Draws no badge. |
| `added` | All states | Date the record was created, `YYYY-MM-DD`. |

## Topics: flat and transversal

`topics:` is a **flat, global list** inside `taxonomy.yml`. The file groups
them under comments so they stay readable, but that grouping **is not a
constraint**: a paper filed under `memory` may declare a coordination topic,
and the validator will accept it.

This is deliberate. Since `area` is single-valued, it cannot express that a
work belongs to several areas. Topics do that job. *Generative Agents*, for
example, is filed under `memory` (where its main contribution lies) and
declares `agent-organizations`, which records that it also addresses
multi-agent systems.

> Note: in earlier versions this list was nested under each area, which
> implied a constraint the validator did not enforce. It was flattened so that
> the YAML and the validation logic say the same thing.

## Available facets

The complete topic list lives on
[`/taxonomy`](https://juliodosreis.github.io/awesome-agenticsystems/taxonomy)
so this document cannot go stale. The facets available on every record are:

<!-- gen:facets-table -->
| Facet | Allowed values | Use |
|---|---|---|
| `about` | `reasoning`, `planning`, `memory`, `reflection`, `tool-use`, `learning`, `self-evolution` | What the paper is about. Crosses areas by design: a coordination paper may declare about: memory. |
| `scale` | `single-agent`, `multi-agent`, `human-agent` | The scale of the system studied. "multi-agent" is recorded here and not as an area. |
| `infra` | `rag`, `knowledge-graph`, `sandbox`, `api` | Infrastructure the system uses. A paper whose subject is the protocol itself (mcp, a2a) records that as a topic. |
| `type` | `survey`, `position`, `method`, `benchmark`, `framework`, `empirical`, `case-study` | What kind of contribution it is. |
| `domain` | `general`, `software-engineering`, `data`, `science`, `healthcare`, `education`, `business`, `finance`, `robotics`, `gui`, `web`, `deep-research` | Where it is applied. Generates the /domains pages. |
<!-- /gen:facets-table -->

The automated issue flow assigns `domain: [general]` by default. A record still
carrying `general` after somebody has read the paper is an oversight worth
revisiting.

### Deliberate overlaps

**`area` vs `about`:** the two answer different questions. `area` answers
*"what is the contribution?"* and is single-valued; `about` answers *"what is
it about?"* and is transversal. A `coordination` paper can declare
`about: [memory]`. It is then findable in a search about memory regardless of
where it is filed.

The facet carries the name `about` because of that overlap. `capability` read
as a synonym for the areas in the `capabilities` group, and the choice between
the two was the most frequent error among newcomers. The same reasoning renamed
`level` to `scale`, since `level` did not name what it measured.

**Topic or facet:** each term lives in exactly one vocabulary.

| Terms | Vocabulary | Meaning |
|---|---|---|
| `mcp`, `a2a` | `topics` | The paper is **about** the protocol. |
| `rag`, `knowledge-graph`, `sandbox`, `api` | `facets.infra` | The system **uses** that infrastructure. |

## `relates_to`: one-directional links

`A.relates_to: [B]` means: **"to understand A, read B first"**. In practice the
newer paper points at the older one.

**Declare it once only.** The reverse direction is computed automatically: on
A's page, B appears under *"read first"*; on B's page, A appears under *"then
read"*. Declaring it on both records duplicates the *"read first"* hint and
breaks the reading path.

```yaml
# reflexion-2023.yml (2023, referencing ReAct)
relates_to: [react-2022]

# react-2022.yml (2022, nothing earlier to point at)
relates_to: []
```

A reference to an id that does not exist breaks the build.

## Changing the taxonomy

**Adding topics** is expected and carries a low cost. The test is whether the
term would serve as a filter *today*. A topic that does not discriminate
between the papers already in the collection adds no retrieval value. Version 2
of the taxonomy had 105 topics with a 22% usage rate, which motivated the cut
to the current list in version 3.

**Adding areas** is a structural change. Do not create an area with no paper
to live in it (`rules` in `taxonomy.yml`).

An empty area records a gap in what has been read so far. These render with a
dashed border on `/areas`. The empty areas that already exist are accepted debt
and **set no precedent** for creating more.

The thresholds in `rules:` trigger a review and drive no automation. An area
that grows past `split_area_at` may need splitting, and a topic used by more
papers than `promote_topic_at` may deserve promotion to an area of its own. The
current values live in `taxonomy.yml`, so they are not repeated here.

To propose a change, open an issue with the *Propose a taxonomy change*
template. Structural proposals should be argued from the literature below.

## Bibliographic basis

The taxonomy is backed by technical literature. The `references:` section of
`taxonomy.yml` records where each classification axis comes from, and
`used_for` states which part of the vocabulary each reference supports:

<!-- gen:references-table -->
| Reference | What it supports |
|---|---|
| [Sumers et al. (2023). Cognitive Architectures for Language Agents.](https://arxiv.org/abs/2309.02427) | The vocabulary of the memory area (working / episodic / semantic / procedural, via Tulving's trichotomy) and the split of the action space into internal (retrieval, reasoning, learning) and external (grounding). |
| [Wang et al. (2024). A Survey on LLM-based Autonomous Agents. Frontiers of Computer Science 18:186345.](https://link.springer.com/article/10.1007/s11704-024-40231-1) | The profile / memory / planning / action framework, which the architectures topics (profile, persona) come from. |
| [Luo et al. (2025). Large Language Model Agent: A Survey on Methodology, Applications and Challenges.](https://arxiv.org/abs/2503.21460) | The construction / collaboration / evolution axis, which supports learning-evolution as an area of its own. |
| [From Question Answering to Task Completion: A Survey on Agent System and Harness Design (2026).](https://arxiv.org/abs/2606.20683) | The vocabulary of the engineering area. |
| [masamasa59/ai-agent-papers](https://github.com/masamasa59/ai-agent-papers) | The grouping of areas into the four navigation layers, and the decision to place multi-agent systems under architecture. |
<!-- /gen:references-table -->

This is rendered on `/taxonomy`.

## Automation and manual classification

Nothing analyzes the content of a paper automatically: **all classification is
manual**.

| Field | Source |
|---|---|
| `title`, `authors`, `year`, `venue`, `arxiv`, `links.paper`, `id`, `added` | Automatic: from arXiv (`add.py`, or the issue flow when the link is an arXiv one) or from the pasted BibTeX |
| `area`, `scale`, `type` | Manual: picked in the issue form. Scripts only check that the value exists. |
| `topics`, `about`, `infra`, `domain`, `tldr`, `notes`, `relates_to`, `evaluated_on` | Manual: requires editing the file. |

The system automates **validation**. Classification stays manual.

## Local workflow

Requires **Node.js 22.12 or newer** (the version in `.nvmrc`). The scripts —
`add.py`, and `npm run docs`, which wraps one — additionally need **Python
3.11+** with `pip install -r requirements-dev.txt`. Building and browsing the
site need only Node.

```bash
npm install
npm run dev

# Create a record from arXiv metadata:
python scripts/add.py 2210.03629

# After editing src/data/taxonomy.yml, propagate it to the docs and issue form:
npm run docs
```

`add.py` creates the record in the `captured` state with the classification
fields commented out. To get the paper onto the site, uncomment `area`, `scale`
and `type` and change `status` to `triaged`.

When the site does not reflect an edit after a reload, the cause is usually the
Astro 7 daemon: `npx astro dev stop && npm run dev`. See the
[README](./README.md#local-development).

## Build validation

Data is validated with **Zod** during `npm run dev` and `npm run build`. The
schema (`src/content.config.ts`) reads its vocabulary from `taxonomy.yml`. Any
unrecognized value stops the build and reports the valid options:

```
"multi-agent" is not part of areas (src/data/taxonomy.yml).
Valid values: foundations, reasoning-planning, memory, ...
```

Beyond the per-record schema, the build also checks:

| Check | Where | What it prevents |
|---|---|---|
| Every value belongs to the taxonomy | `src/content.config.ts` | Invented areas, topics and facet values |
| Each status has its required fields | `src/content.config.ts` | `status: read` with no `tldr` |
| `id` equals the filename | `src/lib/papers.ts` | A paper published at one URL and linked from another |
| `relates_to` / `evaluated_on` resolve | `src/pages/papers/[id].astro` | Reading paths broken with no build error |
| Areas, domain groups and descriptions resolve | `src/lib/taxonomy.ts` | A typo making an area vanish from the navigation |
| Docs and issue form match the taxonomy | `scripts/gen_docs.py --check` in CI | An issue form offering an option the validator rejects |

## Repository scope

This collection is for **papers** only. Software (a GitHub repository, a
released tool) does not get a record of its own.

The rule governs the record. The subject matter is unrestricted: a paper
describing a framework is welcome and is recorded as `type: framework`.

For mixed cases (AutoGen, MetaGPT), only the paper is included; the tool
itself is not. A separate `ecosystem/` collection with its own schema may
exist in the future. Until it does, software should not be added.

Benchmarks count as papers and belong to the `evaluation` area (see
`agentbench-2023`, `tau-bench-2024`). Their relationship to the methods they
evaluate is expressed through `evaluated_on`.
