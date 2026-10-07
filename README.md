# Awesome Agentic Systems

[![Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjuliodosreis%2Fawesome-agenticsystems%2Fmain%2F.github%2Fbadges.json&query=%24.papers&label=papers&color=58a6ff)](#the-collection)
[![Deploy](https://github.com/juliodosreis/awesome-agenticsystems/actions/workflows/deploy.yml/badge.svg)](https://github.com/juliodosreis/awesome-agenticsystems/actions/workflows/deploy.yml)
[![Code: MIT](https://img.shields.io/badge/code-MIT-green.svg)](./LICENSE)
[![Papers: CC0](https://img.shields.io/badge/papers-CC0--1.0-lightgrey.svg)](./LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

A curated collection of papers on agentic AI systems, classified by the
contribution of each one.

Every paper is filed under a single area, its contribution, then cut across by
topics and facets: what it is about, at what scale, in which domain. The
vocabulary is validated at build time, so a term that stops resolving stops the
build.

**[Browse the site](https://juliodosreis.github.io/awesome-agenticsystems)** ·
[Suggest a paper](https://github.com/juliodosreis/awesome-agenticsystems/issues/new?template=add_paper.yml) ·
[Contributing guide](./CONTRIBUTING.md) ·
[RSS](https://juliodosreis.github.io/awesome-agenticsystems/rss.xml)

<!-- gen:counts -->
11 areas in 4 layers, 58 topics and 32 facet values across 5 facets.
<!-- /gen:counts -->

## Contents

- [The collection](#the-collection)
- [Design decisions](#design-decisions)
- [Adding a paper](#adding-a-paper)
- [The taxonomy](#the-taxonomy)
- [Local development](#local-development)
- [Tests](#tests)
- [Contributing](#contributing)
- [Citing this collection](#citing-this-collection)
- [License](#license)

## The collection

<!-- gen:paper-count -->
36 papers listed, 32 of them with a written summary.
<!-- /gen:paper-count -->

The site has filtering, search and the reading-path graph; this listing is the
same data, flattened for reading on GitHub.

<!-- gen:papers -->
*🔥 essential · 📖 survey · ⚖️ benchmark. Surveys first within each area, then newest first.*

### Overview

Where to enter the field.

#### Foundations & surveys ([`foundations`](https://juliodosreis.github.io/awesome-agenticsystems/areas/foundations))

- 🔥 📖 [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](https://arxiv.org/abs/2607.05775) — `2026`  
  Synthesizes 27 benchmark, taxonomy and audit papers across 19 benchmarks into six failure clusters, from tool invocation errors to measurement validity problems.


### Agent capabilities

What the agent reasons about, stores, executes and learns.

#### Reasoning, planning & reflection ([`reasoning-planning`](https://juliodosreis.github.io/awesome-agenticsystems/areas/reasoning-planning))

- 🔥 📖 [Metacognition in LLMs: Foundations, Progress, and Opportunities](https://arxiv.org/abs/2607.11881) — `2026`  
  A survey of metacognition in LLMs: how it is measured, how it can be elicited or improved, and where the evidence for it is limited.
- [CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems](https://arxiv.org/abs/2608.06871) — `2026`  
  Runs Monte Carlo Tree Search where an LLM Judge scores emergent behavior and an LLM Editor proposes variants, searching for complex systems that meet a stated behavioral goal.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — `NeurIPS 2023` · 2023  
  Turns the feedback from a failed attempt into text and stores it in episodic memory to condition the retry, without updating weights.
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) — `NeurIPS 2023` · 2023  
  Explores several reasoning paths in parallel and prunes them with self-evaluation.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — `ICLR 2023` · 2022  
  Interleaves reasoning traces with actions on the environment, so that each observation corrects the reasoning that follows.

#### Memory ([`memory`](https://juliodosreis.github.io/awesome-agenticsystems/areas/memory))

- 🔥 📖 [Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents](https://arxiv.org/abs/2606.30306) — `2026`  
  Surveys 435 works on agents whose behavior depends on durable state, along six axes (authority, scope, mutability, provenance, recoverability, actionability) and a write-to-rollback lifecycle.
- [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets](https://arxiv.org/abs/2607.02303) — `2026`  
  Gives linear attention a bounded exact KV cache alongside its compressive recurrent state, so associations that do not survive compression are still recallable.
- [Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale](https://arxiv.org/abs/2607.01538) — `2026`  
  Studies in-context retrieval at million-token corpus scale and traces its collapse to attention dilution, where irrelevant documents dominate the softmax denominator.
- [Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability](https://arxiv.org/abs/2607.26637) — `2026`  
  Studies the de facto default for agent memory, a directory of markdown files the agent maintains itself, across memory shape, stream scale and tool harness.
- [Zero-Mem: Zero-Token Memory Operations for LLM Agents](https://arxiv.org/abs/2607.29377) — `2026`  
  Runs memory operations with no LLM calls, using an entity-context graph and a temporal hierarchy over the original traces, and reserves generation for the final answer.
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — `UIST 2023` · 2023  
  A memory architecture with an observation stream, retrieval weighted by relevance-recency-importance, and periodic synthesis into reflections.

#### Tools, environment & context ([`tools-context`](https://juliodosreis.github.io/awesome-agenticsystems/areas/tools-context))

- [Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories](https://arxiv.org/abs/2607.27250) — `2026`  
  A controlled ablation of AGENTS.md and CLAUDE.md across two frontier agents and 288 evaluated runs finds no measurable effect on correctness, bounded to 10-15pp by equivalence testing.
- [Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents](https://arxiv.org/abs/2604.00555) — `2026`
- [ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509) — `2026`  
  A training-free inference method that builds a query-conditioned evidence pool from the model's own relevance signals and replays it before generation, without pruning the original context.
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — `NeurIPS 2023` · 2023  
  The model self-annotates where to insert API calls and keeps the ones that reduce perplexity, learning tool use without human supervision.

#### Learning, skills & self-evolution ([`learning-evolution`](https://juliodosreis.github.io/awesome-agenticsystems/areas/learning-evolution))

- [GitSkills: A Dataset of Agent Skills on GitHub](https://arxiv.org/abs/2608.10906) — `2026`  
  A dataset of 3.8M SKILL.md files mined from 282,200 public repositories, with front matter, folder contents and partial commit history.
- [Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories](https://arxiv.org/abs/2608.02276) — `2026`  
  Post-trains a separate 9B harness engineer with online RL to turn batches of agent failures into validated executable patches to the runtime harness, rewarded by the target agent's realized success.
- [Inducing Task Models from Computer-Use Traces](https://arxiv.org/abs/2608.20319) — `2026`  
  Recovers the latent tasks inside an unconstrained computer-use trace and induces, for each, a hierarchical objective model paired with a procedure model of the control flow.


### System structure

The inner loop of the system, its number of agents, and the substrate it runs on.

#### Coordination & organization ([`coordination`](https://juliodosreis.github.io/awesome-agenticsystems/areas/coordination))

- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — `COLM 2024` · 2023  
  Models the application as a conversation between configurable agents, with humans and code execution as first-class participants.
- [MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) — `ICLR 2024` · 2023  
  Encodes the standard operating procedures of a software company as agent roles chained by structured artifacts.

#### Harness, scaffolding & AgentOps ([`engineering`](https://juliodosreis.github.io/awesome-agenticsystems/areas/engineering))

- [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528) — `2026`  
  A framework for harnessed agentic RL, where the deploy-time harness runs the environment loop and the trainer receives only request-response pairs.
- [Coding-agents can replicate scientific machine learning papers](https://arxiv.org/abs/2607.02134) — `2026`  
  A replication workflow implemented as a coding-agent skill, where each paper claim becomes a recorded target and completion depends on workspace evidence passing validation checks.
- [Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs](https://arxiv.org/abs/2607.04371) — `2026`  
  A compressed hybrid-MoE variant tuned for interactive serving, roughly doubling server throughput at matched user throughput and raising 1M-token concurrency from one request to eight.
- [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557) — `2026`  
  Trains agents inside the real inference harness they are deployed with, by proxying the harness's model calls into a standard RL codebase and running each rollout in its own container.
- 🔥 [The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI](https://arxiv.org/abs/2607.06906) — `2026`  
  Holds six models constant and swaps only the orchestration layer, cutting cost per task 41% and tokens per task 38% at parity quality.


### Measurement and control

How a system is measured, and how its risk is governed.

#### Evaluation & benchmarks ([`evaluation`](https://juliodosreis.github.io/awesome-agenticsystems/areas/evaluation))

- ⚖️ [ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?](https://arxiv.org/abs/2608.03874) — `2026`  
  Five domains of 100 interconnected subtasks ordered by difficulty, built to separate skill consolidation from adaptation to recent context.
- 🔥 [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391) — `2026`  
  Scores candidate solutions by taking the expectation over scoring-token logits. Verification then scales with granularity, repetition and criteria decomposition.
- 🔥 ⚖️ [One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows](https://arxiv.org/abs/2608.19741) — `2026`  
  507 policy-conditioned workflows in an MCP-compatible sandbox, scored on the persistent backend state an agent leaves behind.
- ⚖️ [Protocol Agent: What If Agents Could Use Cryptography In Everyday Life?](https://arxiv.org/abs/2602.01304) — `2026`
- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227) — `2026`  
  Argues automatic harness evolution must be compared against test-time scaling under matched feedback and inference budgets, and finds it does not outperform that baseline or generalize to held-out tasks.
- 🔥 ⚖️ [tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — `ICLR 2025` · 2024  
  Evaluates the agent against a simulated user and domain policies, measuring consistency across runs on top of per-task success.
- 🔥 ⚖️ [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) — `ICLR 2024` · 2023  
  Gathers eight heterogeneous interactive environments to measure agents on multi-turn tasks under a common protocol.

#### Safety, trust & governance ([`safety`](https://juliodosreis.github.io/awesome-agenticsystems/areas/safety))

- 📖 [The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088) — `2026`
- [Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations](https://arxiv.org/abs/2607.01181) — `2026`  
  Augments RL with verifiable rewards with an adversarial discriminator trained on human demonstrations, so non-verifiable properties like style and structure are optimized alongside task accuracy.
- [Graph-Symbolic Policy Enforcement and Control (G-SPEC): A Neuro-Symbolic Framework for Safe Agentic AI in 5G Autonomous Networks](https://arxiv.org/abs/2512.20275) — `2025`


> **Gaps.** No papers yet in `architectures`, `interoperability`. The areas exist in the taxonomy before anything lives in them — the gap is a reading list, and a good place to make a first contribution.
<!-- /gen:papers -->

## Design decisions

- **A validated vocabulary.** The Zod schema reads the vocabulary from
  `taxonomy.yml`. A nonexistent area or topic breaks the build
  and prints the valid values. The taxonomy validates itself too: an area
  pointing at a missing layer, or an orphaned domain, stops compilation.
- **A taxonomy with a declared bibliographic basis** (CoALA, Wang et al. 2024,
  Luo et al. 2025, harness survey 2026), browsable at `/taxonomy`. Each
  reference states which part of the vocabulary it supports.
- **Three navigation axes**: by area (contribution), by domain (application),
  and by reading path (the `relates_to` graph between papers, navigable in
  both directions).
- **Two-level classification.** A single area defines the contribution; topics
  and facets (<!-- gen:facet-names -->`about`, `scale`, `infra`, `type`, `domain`<!-- /gen:facet-names -->) cut across areas
  and say what the paper is about.
- **Adding a paper is a GitHub issue**, with no local setup.
- **Site-wide search** (Pagefind), an [RSS feed](https://juliodosreis.github.io/awesome-agenticsystems/rss.xml)
  of new additions, and a sitemap.

## Adding a paper

| | Who | How | Resulting status |
|---|---|---|---|
| Suggest a paper | Anyone | Issue with 3 fields → reviewed PR | `triaged` — visible on the site |
| Add and read | Anyone willing to clone | Edit the `.yml` and open a pull request | `read` — includes `tldr` and `notes` |

### Issue submission

No cloning, no local scripts.

1. Go to the **Issues** tab.
2. Pick **New Issue** → **Add a Paper**.
3. Paste the link to the paper. An arXiv link supplies the rest: the title,
   authors and year are fetched automatically. For any other source, paste the
   **BibTeX** as well.
4. Pick **area**, **scale** and **type**. Each option in the form carries a
   one-line description. The `triaged` state requires these three fields, and
   reaching it makes the paper visible once the PR is merged. When the choice
   is unclear, pick the closest option; the PR is reviewed before merging.
5. A GitHub Action (`issue_ops.yml`) validates the data, builds the site with
   the new record, and opens a pull request. On a missing year, an invalid
   link, a duplicate paper, or a value outside the taxonomy, the Action
   **comments the reason on the issue** and labels it `needs-fix` in place of
   opening a broken PR. Close and reopen the issue to retry.

### Direct edit

The issue flow reaches `triaged`: no `tldr`, `notes`, `topics` or
`about`, since those require reading the paper. To add them, edit the
`.yml` directly. `python scripts/add.py <arxiv-id>` fetches the metadata and
creates the record in the `captured` state with the classification fields
commented out.

Editing a record already in the collection follows the same path: change the
file under `src/content/papers/` and open a pull request. `validate.yml` runs
the build and the test suite on it.

Incomplete classification does not block a paper. The schema enforces three
states:

<!-- gen:status-table -->
| status | Requires | Effect |
|---|---|---|
| `captured` | metadata only | Kept in git, not visible on the site. |
| `triaged` | `area`, `scale`, `type` | Visible in the index. |
| `read` | `tldr`, `topics`, `about` | Works as a summary on the site. |
<!-- /gen:status-table -->

See [CONTRIBUTING.md](./CONTRIBUTING.md) for picking an area, and
[TAXONOMY.md](./TAXONOMY.md) for filling a record in by hand or proposing
changes to the vocabulary.

## The taxonomy

It lives in `src/data/taxonomy.yml` (v3) and is the single source of truth: the
validator, the site, the guides and the issue form all read from that one file.

<!-- gen:areas-table -->
| Layer | Areas |
|---|---|
| Overview | `foundations` |
| Agent capabilities | `reasoning-planning`, `memory`, `tools-context`, `learning-evolution` |
| System structure | `architectures`, `coordination`, `interoperability`, `engineering` |
| Measurement and control | `evaluation`, `safety` |
<!-- /gen:areas-table -->

The complete vocabulary, with usage counts, is at
[`/taxonomy`](https://juliodosreis.github.io/awesome-agenticsystems/taxonomy).
The design and the criterion behind each field are documented in
[TAXONOMY.md](./TAXONOMY.md).

Two decisions that resolve most ambiguous cases:

- **Scale does not determine the area.** Having multiple agents is expressed
  with `scale: [multi-agent]`. The `coordination` area is reserved for papers
  whose central contribution is the coordination mechanism itself.
- **A term belongs to exactly one vocabulary.** `mcp` and `a2a` are topics (the
  paper is about the protocol); `rag`, `knowledge-graph`, `sandbox` and `api`
  are `infra` values (the system uses them).

## Local development

Requires Node.js 22.12 or newer (an Astro 7 requirement). The exact version is
in `.nvmrc`, which is also what CI uses: `nvm use` picks it up.

```bash
npm install
npm run dev
```

Python 3.11+ is needed only for the scripts: `npm run docs`, `npm test` and
`scripts/add.py`. Browsing and building the site need nothing but Node.

```bash
pip install -r requirements-dev.txt
```

The dev server starts at `http://localhost:4321`.

> The search box in the header is powered by Pagefind, which indexes the
> **built** HTML. Under `astro dev` it returns nothing, which is expected. To
> exercise search, run `npm run build && npm run preview`.

> Note: as of Astro 7 the dev server runs as a background daemon. Ctrl+C does
> not stop it, and a later `npm run dev` attaches to the existing instance,
> which can serve a stale version of the site. To stop it:
>
> ```bash
> npx astro dev stop      # stop the server
> npx astro dev status    # check the process
> npx astro dev logs      # view server logs
> ```

### Commands

| Command | What it does |
|---|---|
| `npm run dev` | Dev server on `localhost:4321` |
| `npm run build` | Runs `astro check` (types + paper validation) and builds to `dist/` |
| `npm run preview` | Serves `dist/` to review the final build |
| `npm run docs` | Regenerates the doc sections and issue form from `taxonomy.yml` |
| `npm run docs:check` | Fails if those are stale. CI runs this. |
| `npm test` | Runs the full test suite (~20s) |
| `npm run test:fast` | Skips the tests that shell out to a real build (<1s) |
| `python scripts/add.py <arxiv-id>` | Creates a record from arXiv metadata |

`npm run docs` also rewrites the paper listing in this README and the counts in
`.github/badges.json`, so both stay true without anyone updating them by hand.

`npm run build` gates deployment: a type error, or a paper that fails
taxonomy validation, stops publication.

### Layout

| Path | Contents |
|---|---|
| `src/content/papers/` | One `.yml` per paper. The data. |
| `src/data/taxonomy.yml` | Single source of truth: layers, areas, topics, facets, domains and references. |
| `src/content.config.ts` | Zod schema, built from the taxonomy vocabulary. Enforces the three paper states. |
| `src/lib/taxonomy.ts` | Shared loader for `taxonomy.yml` plus integrity guards (`assertGroupsResolve`). |
| `src/lib/papers.ts` | Collection helpers: publication logic, author formatting, id/filename check. |
| `src/lib/url.ts` | `url()` helper for internal links. The site lives under a subpath, so hardcoding routes breaks every fork. |
| `src/layouts/Layout.astro` | Shared shell: header, area sidebar, client scripts. |
| `src/pages/` | Routes: `/`, `/areas`, `/domains`, `/taxonomy`, `/papers/[id]`, `/rss.xml`. |
| `public/` | Static files (favicon). |
| `scripts/` | `arxiv.py` (shared metadata fetch), `add.py` (local capture), `process_issue.py` (used by the Action), `gen_docs.py` (README listing, doc blocks, issue form, badges). |
| `tests/` | pytest suite. `test_schema.py` is the important one: it falsifies records on purpose to prove the build rejects them. |
| `.github/workflows/` | `issue_ops.yml` (issue intake), `validate.yml` (build on every PR), `deploy.yml` (GitHub Pages). |

## Tests

```bash
pip install -r requirements-dev.txt
npm test
```

The suite covers the issue parser, the one script that runs unsupervised,
along with the doc generator and the build-time guards. The assertions cover
the error messages as well as the exit codes, since a rejection a contributor
cannot act on leaves the submission stuck.

`tests/test_schema.py` is deliberately slow. It falsifies a record or the
taxonomy and runs a real `npm run build` per case. A passing `npm run build`
proves only that valid data compiles, and leaves the behavior of the guards
unmeasured. Skip it locally with `npm run test:fast`.

## Contributing

Read [CONTRIBUTING.md](./CONTRIBUTING.md). Suggestions, corrections to a
classification, and proposals for new vocabulary are all welcome, and each has
its own issue template. Participation is covered by the
[Code of Conduct](./CODE_OF_CONDUCT.md).

## Citing this collection

For citing the taxonomy or the collection, the repository carries a
[CITATION.cff](./CITATION.cff), which GitHub's "Cite this repository" button
reads. It covers the classification work only. The papers themselves are cited
directly.

## License

Two licenses, because the repository holds two different things:

- **Code** (`src/`, `scripts/`, `.github/`): [MIT](./LICENSE).
- **The paper collection** (`src/content/papers/`) and the taxonomy
  (`src/data/taxonomy.yml`): [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
  Bibliographic metadata is reusable without conditions.

The papers themselves carry no license from this repository. They stay under
the terms their publishers set. See [LICENSE](LICENSE).
