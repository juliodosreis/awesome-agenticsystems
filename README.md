# Awesome Agentic Systems

[![Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjuliodosreis%2Fawesome-agenticsystems%2Fmain%2F.github%2Fbadges.json&query=%24.papers&label=papers&color=58a6ff)](#papers)
[![Resources](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjuliodosreis%2Fawesome-agenticsystems%2Fmain%2F.github%2Fbadges.json&query=%24.resources&label=resources&color=a371f7)](#resources)
[![Deploy](https://github.com/juliodosreis/awesome-agenticsystems/actions/workflows/deploy.yml/badge.svg)](https://github.com/juliodosreis/awesome-agenticsystems/actions/workflows/deploy.yml)
[![Code: MIT](https://img.shields.io/badge/code-MIT-green.svg)](./LICENSE)
[![Papers: CC0](https://img.shields.io/badge/papers-CC0--1.0-lightgrey.svg)](./LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

A curated collection of material on agentic AI systems, in two parts:

- **[Papers](#papers)**: research papers, each filed under the area of its contribution and described by topics and facets (what it is about, at what scale, in which domain).
- **[Resources](#resources)**: material that is not a paper, such as protocols, orchestration frameworks, skills, benchmarks, books, courses, guides and tools. Each resource is filed under one kind.

<p align="center">
  <a href="https://juliodosreis.com/awesome-agenticsystems"><img alt="Browse the site" src="https://img.shields.io/badge/Browse_the_site-0969da?style=for-the-badge"></a>
  <a href="https://github.com/juliodosreis/awesome-agenticsystems/issues/new?template=add_paper.yml"><img alt="Suggest a paper" src="https://img.shields.io/badge/Suggest_a_paper-2da44e?style=for-the-badge&logo=github"></a>
  <a href="https://github.com/juliodosreis/awesome-agenticsystems/issues/new?template=add_resource.yml"><img alt="Suggest a resource" src="https://img.shields.io/badge/Suggest_a_resource-8250df?style=for-the-badge&logo=github"></a>
  <a href="./CONTRIBUTING.md"><img alt="Contributing guide" src="https://img.shields.io/badge/Contributing_guide-57606a?style=for-the-badge"></a>
</p>

<p align="center">
  <a href="https://juliodosreis.com/awesome-agenticsystems/rss.xml">RSS feed of new additions</a>
</p>

## Collection overview

| | Papers | Resources |
|---|---|---|
| Holds | Papers on agentic systems: surveys, methods, benchmarks, frameworks, empirical studies | Links to protocols, frameworks, skills, benchmarks, books, courses, guides and tools |
| Entries | <!-- gen:paper-total -->222<!-- /gen:paper-total --> | <!-- gen:resource-total -->35<!-- /gen:resource-total --> |
| Classified by | One `area`, plus topics and facets | One `kind`, plus an optional `area` |
| On the site | [Index](https://juliodosreis.com/awesome-agenticsystems), [areas](https://juliodosreis.com/awesome-agenticsystems/areas), [domains](https://juliodosreis.com/awesome-agenticsystems/domains) | [Resources](https://juliodosreis.com/awesome-agenticsystems/resources), and the page of its area when one is set |
| In this README | [Papers](#papers), grouped by area | [Resources](#resources), grouped by kind |
| Suggest one | [*Add a Paper* form](https://github.com/juliodosreis/awesome-agenticsystems/issues/new?template=add_paper.yml) | [*Add a Resource* form](https://github.com/juliodosreis/awesome-agenticsystems/issues/new?template=add_resource.yml) |

A framework or a benchmark published with a paper has an entry in each part. The paper goes to the paper collection, with `type: framework` or `type: benchmark`, and its repository, documentation or leaderboard goes to the resources. AutoGen and MetaGPT, for example, are papers in the collection, and their repositories can be listed as resources of kind `framework`.

## Contents

- [Collection overview](#collection-overview)
- [Papers](#papers)
- [Resources](#resources)
- [Design decisions](#design-decisions)
- [The taxonomy](#the-taxonomy)
- [Local development](#local-development)
- [Tests](#tests)
- [Contributing](#contributing)
- [Citing this collection](#citing-this-collection)
- [License](#license)

## Papers

<!-- gen:paper-count -->
222 papers listed, 42 of them with a written summary.
<!-- /gen:paper-count -->

Each paper is filed under one area, the one its main contribution belongs to. The areas are grouped in layers, listed below in order. The site adds filtering, search and the reading-path graph over the same data.

<!-- gen:papers -->
*🔥 essential · 📖 survey · ⚖️ benchmark. Surveys first within each area, then newest first.*

### Overview

Where to enter the field.

#### Foundations & surveys ([`foundations`](https://juliodosreis.com/awesome-agenticsystems/areas/foundations))

- 🔥 📖 [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](https://arxiv.org/abs/2607.05775) — `2026`  
  Synthesizes 27 benchmark, taxonomy and audit papers across 19 benchmarks into six failure clusters, from tool invocation errors to measurement validity problems.
- 📖 [The Hitchhiker's Guide to Agentic AI: From Foundations to Systems](https://arxiv.org/abs/2606.24937) — `2026`
- 📖 [Agentic AI in Education: State of the Art and Future Directions](https://ieeexplore.ieee.org/abstract/document/11201263) — `IEEE Access` · 2025
- 📖 [Agentic AI: A Comprehensive Survey of Architectures, Applications, and Future Directions](https://arxiv.org/abs/2510.25445) — `2025`
- 📖 [Evolution of AI in Education: Agentic Workflows](https://arxiv.org/abs/2504.20082v2) — `2025`
- 📖 [From Multi-Agent Systems and the Semantic Web to Agentic AI: A Unified Narrative of the Web of Agents](https://arxiv.org/abs/2507.10644) — `arXiv preprint arXiv:2507.10644` · 2025
- 📖 [LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead](https://dl.acm.org/doi/10.1145/3712003) — `ACM Transactions on Software Engineering and Methodology` · 2025
- 📖 [A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges](https://doi.org/10.1007/s44336-024-00009-2) — `Vicinagearth` · 2024
- 📖 [Exploring Autonomous Agents through the Lens of Large Language Models: A Review](https://arxiv.org/abs/2404.04442) — `2024`
- 📖 [Exploring Large Language Model based Intelligent Agents: Definitions, Methods, and Prospects](https://arxiv.org/abs/2401.03428) — `2024`
- 📖 [LLM-based Multi-Agent Reinforcement Learning: Current and Future Directions](https://arxiv.org/abs/2405.11106) — `2024`
- 📖 [Large Language Model based Multi-Agents: A Survey of Progress and Challenges](https://arxiv.org/abs/2402.01680) — `2024`
- 📖 [Large Model Based Agents: State-of-the-Art, Cooperation Paradigms, Security and Privacy, and Future Trends](https://arxiv.org/abs/2409.14457) — `2024`
- 📖 [Large language models empowered agent-based modeling and simulation: a survey and perspectives](https://doi.org/10.1057/s41599-024-03611-3) — `Humanities and Social Sciences Communications` · 2024
- 📖 [The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey](https://arxiv.org/abs/2404.11584) — `2024`
- 📖 [Towards Rationality in Language and Multimodal Agents: A Survey](https://arxiv.org/abs/2406.00252) — `2024`
- 📖 [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) — `2023`
- 📖 [Balancing Autonomy and Alignment: A Multi-Dimensional Taxonomy for Autonomous LLM-powered Multi-Agent Architectures](https://arxiv.org/abs/2310.03659) — `2023`
- 📖 [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) — `2023`
- [Large Language Models Miss the Multi-Agent Mark](https://arxiv.org/abs/2505.21298) — `2025`
- [Enhancing AI Systems with Agentic Workflows Patterns in Large Language Model](https://doi.org/10.36227/techrxiv.173092393.30216600/v1) — `TechRxiv` · 2024
- [GenAI-powered Multi-Agent Paradigm for Smart Urban Mobility: Opportunities and Challenges for Integrating Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) with Intelligent Transportation Systems](https://arxiv.org/abs/2409.00494) — `2024`
- [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/abs/2402.03578) — `2024`
- [LLM-based agentic systems in medicine and healthcare](https://www.nature.com/articles/s42256-024-00944-1) — `Nature Machine Intelligence` · 2024
- [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) — `2023`


### Agent capabilities

What the agent reasons about, stores, executes and learns.

#### Reasoning, planning & reflection ([`reasoning-planning`](https://juliodosreis.com/awesome-agenticsystems/areas/reasoning-planning))

- 🔥 📖 [Metacognition in LLMs: Foundations, Progress, and Opportunities](https://arxiv.org/abs/2607.11881) — `2026`  
  A survey of metacognition in LLMs: how it is measured, how it can be elicited or improved, and where the evidence for it is limited.
- 📖 [Understanding the Planning of LLM Agents: A Survey](https://arxiv.org/abs/2402.02716) — `2024`
- [CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems](https://arxiv.org/abs/2608.06871) — `2026`  
  Runs Monte Carlo Tree Search where an LLM Judge scores emergent behavior and an LLM Editor proposes variants, searching for complex systems that meet a stated behavioral goal.
- [ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory](https://dl.acm.org/doi/10.1145/3770855.3818931) — `Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26)` · 2026
- [L-MARS: Legal Multi-Agent System with Agentic Search and Citation-Faithfulness Audit](https://arxiv.org/abs/2509.00761) — `2026`
- [Why Reasoning Fails to Plan: A Planning-Centric Analysis of Long-Horizon Decision Making in LLM Agents](https://arxiv.org/abs/2601.22311) — `2026`
- [CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging](https://arxiv.org/abs/2502.05664) — `2025`
- [ADaPT: As-Needed Decomposition and Planning with Language Models](https://aclanthology.org/2024.findings-naacl.264/) — `Findings of the Association for Computational Linguistics: NAACL 2024` · 2024
- [Devil's Advocate: Anticipatory Reflection for LLM Agents](https://arxiv.org/abs/2405.16334) — `2024`
- [Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://proceedings.mlr.press/v235/zhou24r.html) — `Proceedings of the 41st International Conference on Machine Learning` · 2024
- [Positive Experience Reflection for Agents in Interactive Text Environments](https://arxiv.org/abs/2411.02223) — `2024`
- [Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560) — `2023`
- [ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models](https://arxiv.org/abs/2305.18323) — `2023`
- [Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992) — `2023`
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — `NeurIPS 2023` · 2023  
  Turns the feedback from a failed attempt into text and stores it in episodic memory to condition the retry, without updating weights.
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) — `2023`
- [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://arxiv.org/abs/2309.17452) — `ICLR 2024` · 2023  
  An agent that solves complex mathematical problems by interleaving natural language reasoning with programmatic code execution.
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) — `NeurIPS 2023` · 2023  
  Explores several reasoning paths in parallel and prunes them with self-evaluation.
- [LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models](https://arxiv.org/abs/2212.04088) — `2022`
- [Measuring and Narrowing the Compositionality Gap in Language Models](https://arxiv.org/abs/2210.03350) — `2022`
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — `ICLR 2023` · 2022  
  Interleaves reasoning traces with actions on the environment, so that each observation corrects the reasoning that follows.

#### Memory ([`memory`](https://juliodosreis.com/awesome-agenticsystems/areas/memory))

- 🔥 📖 [Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents](https://arxiv.org/abs/2606.30306) — `2026`  
  Surveys 435 works on agents whose behavior depends on durable state, along six axes (authority, scope, mutability, provenance, recoverability, actionability) and a write-to-rollback lifecycle.
- 📖 [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716) — `2026`
- 📖 [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) — `2024`
- [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets](https://arxiv.org/abs/2607.02303) — `2026`  
  Gives linear attention a bounded exact KV cache alongside its compressive recurrent state, so associations that do not survive compression are still recallable.
- [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190) — `2026`  
  An autonomous memory management approach where the agent actively decides which parts of its context window to compress, summarize, or discard.
- [Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale](https://arxiv.org/abs/2607.01538) — `2026`  
  Studies in-context retrieval at million-token corpus scale and traces its collapse to attention dilution, where irrelevant documents dominate the softmax denominator.
- [Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability](https://arxiv.org/abs/2607.26637) — `2026`  
  Studies the de facto default for agent memory, a directory of markdown files the agent maintains itself, across memory shape, stream scale and tool harness.
- [Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering](https://arxiv.org/abs/2606.10921) — `2026`  
  A memory architecture that maps long documents into a structure-aware hypergraph, tracing and retrieving only the necessary context nodes on-demand for complex multi-hop question answering.
- [Zero-Mem: Zero-Token Memory Operations for LLM Agents](https://arxiv.org/abs/2607.29377) — `2026`  
  Runs memory operations with no LLM calls, using an entity-context graph and a temporal hierarchy over the original traces, and reserves generation for the final answer.
- ["My agent understands me better": Integrating Dynamic Human-like Memory Recall and Consolidation in LLM-Based Agents](https://arxiv.org/abs/2404.00573) — `2024`
- [INMS: Memory Sharing for Large Language Model based Agents](https://arxiv.org/abs/2404.09982) — `2024`
- [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://arxiv.org/abs/2408.03615) — `2024`
- [RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents](https://arxiv.org/abs/2402.03610) — `2024`
- [Self-evolving Agents with reflective and memory-augmented abilities](https://arxiv.org/abs/2409.00872) — `2024`
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — `UIST 2023` · 2023  
  A memory architecture with an observation stream, retrieval weighted by relevance-recency-importance, and periodic synthesis into reflections.
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — `ICLR 2024` · 2023  
  Introduces a virtual memory hierarchy that allows LLMs to explicitly page information between their limited context window and external storage using function calls.

#### Tools, environment & context ([`tools-context`](https://juliodosreis.com/awesome-agenticsystems/areas/tools-context))

- [A11y-Compressor: A Framework for Enhancing the Efficiency of GUI Agent Observations through Visual Context Reconstruction and Redundancy Reduction](https://aclanthology.org/2026.acl-srw.50/) — `Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop)` · 2026
- [Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories](https://arxiv.org/abs/2607.27250) — `2026`  
  A controlled ablation of AGENTS.md and CLAUDE.md across two frontier agents and 288 evaluated runs finds no measurable effect on correctness, bounded to 10-15pp by equivalence testing.
- [Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents](https://arxiv.org/abs/2604.00555) — `2026`
- [ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509) — `2026`  
  A training-free inference method that builds a query-conditioned evidence pool from the model's own relevance signals and replays it before generation, without pruning the original context.
- [Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI Education](https://arxiv.org/abs/2605.12988) — `2026`  
  A retrieval-augmented agentic tutoring system designed to assist students with algorithm tracing and problem-solving in computer science education.
- [Construção de Agente Inteligente para a Resolução de Questões de Vestibular com LLM](https://hdl.handle.net/11449/315755) — `Undergraduate thesis, Universidade Estadual Paulista (UNESP)` · 2025
- [RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection via Retrieval-Augmented Generation](https://arxiv.org/abs/2505.03275) — `2025`
- [AutoCodeRover: Autonomous Program Improvement](https://dl.acm.org/doi/10.1145/3650212.3680384) — `Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis` · 2024
- [DRAGIN: Dynamic Retrieval Augmented Generation based on the Real-time Information Needs of Large Language Models](https://aclanthology.org/2024.acl-long.702.pdf) — `Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)` · 2024
- [Re-Invoke: Tool Invocation Rewriting for Zero-Shot Tool Retrieval](https://arxiv.org/abs/2408.01875) — `2024`
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a7c947568c1b1328ccc5230172e1e7c-Paper-Conference.pdf) — `Advances in Neural Information Processing Systems` · 2024
- [Tool Documentation Enables Zero-Shot Tool-Usage with Large Language Models](https://arxiv.org/abs/2308.00675) — `2023`
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — `NeurIPS 2023` · 2023  
  The model self-annotates where to insert API calls and keeps the ones that reduce perplexity, learning tool use without human supervision.

#### Learning, skills & self-evolution ([`learning-evolution`](https://juliodosreis.com/awesome-agenticsystems/areas/learning-evolution))

- 📖 [A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications](https://arxiv.org/abs/2605.07358) — `2026`
- [EvoMAS: Evolutionary Generation of Multi-Agent Systems](https://arxiv.org/abs/2602.06511) — `ICML 2026` · 2026
- [GitSkills: A Dataset of Agent Skills on GitHub](https://arxiv.org/abs/2608.10906) — `2026`  
  A dataset of 3.8M SKILL.md files mined from 282,200 public repositories, with front matter, folder contents and partial commit history.
- [Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories](https://arxiv.org/abs/2608.02276) — `2026`  
  Post-trains a separate 9B harness engineer with online RL to turn batches of agent failures into validated executable patches to the runtime harness, rewarded by the target agent's realized success.
- [Inducing Task Models from Computer-Use Traces](https://arxiv.org/abs/2608.20319) — `2026`  
  Recovers the latent tasks inside an unconstrained computer-use trace and induces, for each, a hierarchical objective model paired with a procedure model of the control flow.
- [Towards conversational diagnostic artificial intelligence](https://www.nature.com/articles/s41586-025-08866-7) — `Nature` · 2025
- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) — `2024`
- [ExpeL: LLM Agents Are Experiential Learners](https://dl.acm.org/doi/10.1609/aaai.v38i17.29936) — `Proceedings of the AAAI Conference on Artificial Intelligence` · 2024
- [MetaReflection: Learning Instructions for Language Agents using Past Reflections](https://arxiv.org/abs/2405.13009) — `2024`
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — `2023`  
  An embodied agent that continuously explores a 3D environment by writing, refining, and retrieving executable code from a procedural skill library.


### System structure

The inner loop of the system, its number of agents, and the substrate it runs on.

#### Agent architectures ([`architectures`](https://juliodosreis.com/awesome-agenticsystems/areas/architectures))

- [A Multi-Agent System for Feedback Quality Assurance: Evaluate, Revise, and Validate at Scale](https://proceedings.mlr.press/v339/bulut26a.html) — `Impactful and Responsible AI Systems for Education Workshop (IRAISE), PMLR 339` · 2026
- [AgentSchool: An LLM-Powered Multi-Agent Simulation for Education](https://arxiv.org/abs/2605.30144) — `2026`
- [Agentic Learning Ecosystem for Open, Negotiated, and Accountable Education](https://panosd.eu/asi2026/Papers/ASI2026_paper_12.pdf) — `Workshop on Agents for Societal Impact (ASI) at AAMAS 2026` · 2026
- [An Agentic AI Control Plane for 6G Network Slice Orchestration, Monitoring, and Trading](https://arxiv.org/abs/2602.13227) — `2026`
- [An Artificial Intelligence-Enhanced Assessment Framework for Analyzing Middle School Science Students' Written Responses](https://onlinelibrary.wiley.com/doi/10.1111/jedm.70044) — `Journal of Educational Measurement` · 2026
- [ITAS: A Multi-Agent Architecture for LLM-Based Intelligent Tutoring](https://arxiv.org/abs/2604.24808) — `arXiv preprint arXiv:2604.24808` · 2026
- [LLM-Driven Multi-Agent Framework for Autonomous Network Slice Management: Architecture and Proof-of-Concept Experiments](https://ieeexplore.ieee.org/document/11573048) — `IEEE Open Journal of the Communications Society` · 2026
- [PenExpert: A Multi-Agent Hybrid LLM–Expert System Framework for Autonomous Penetration Testing](https://www.sciencedirect.com/science/article/pii/S0957417426021937?via%3Dihub) — `Expert Systems with Applications` · 2026
- [Towards conversational artificial intelligence for disease management](https://www.nature.com/articles/s41586-026-10764-5) — `Nature` · 2026
- [A Multi-agent LLM System for Automated Requirements Analysis: A Study on User Story Generation and Prioritization](https://link.springer.com/chapter/10.1007/978-3-032-04200-2_12) — `Euromicro Conference on Software Engineering and Advanced Applications (SEAA 2025)` · 2025
- [Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227) — `2025`
- [Agentic AI in Network Slicing](https://ieeexplore.ieee.org/document/11450023) — `2025 9th International Conference on Computer, Software and Modeling (ICCSM)` · 2025
- [Cradle: Empowering Foundation Agents towards General Computer Control](https://proceedings.mlr.press/v267/tan25h.html) — `Proceedings of the 42nd International Conference on Machine Learning` · 2025
- [Designing an LLM-based Multiagent System for Generating Activities and Their Rubrics: A Study on Data Mining](https://doi.org/10.5753/sbie.2025.12723) — `Simpósio Brasileiro de Informática na Educação (SBIE)` · 2025
- ⚖️ [Goal2Story: A Multi-Agent Fleet based on Privately Enabled sLLMs for Impacting Mapping on Requirements Elicitation](https://arxiv.org/abs/2503.13279) — `2025`
- [LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents](https://arxiv.org/abs/2512.04105) — `2025`
- [Leveraging Multi-Agent System (MAS) and Fine-Tuned Small Language Models (SLMs) for Automated Telecom Network Troubleshooting](https://arxiv.org/abs/2511.00651) — `2025`
- [MedScrubCrew: A Medical Multi-Agent Framework for Automating Appointment Scheduling Based on Patient-Provider Profile Resource Matching](https://www.mdpi.com/2227-9032/13/14/1649) — `Healthcare` · 2025
- [PentestAgent: Incorporating LLM Agents to Automated Penetration Testing](https://dl.acm.org/doi/10.1145/3708821.3733882) — `Proceedings of the 20th ACM Asia Conference on Computer and Communications Security` · 2025
- [Scaling Equitable Reflection Assessment in Education via Large Language Models and Role-Based Feedback Agents](https://arxiv.org/abs/2511.11772) — `2025`
- [Structuring the Unstructured: A Multi-Agent System for Extracting and Querying Financial KPIs and Guidance](https://arxiv.org/abs/2505.19197) — `2025`
- [TASER: Table Agents for Schema-guided Extraction and Recommendation](https://arxiv.org/abs/2508.13404) — `2025`
- [Towards AI-Powered Real-Time Negotiation Agent](https://ceur-ws.org/Vol-3977/SemGenAge-5.pdf) — `SemGenAge Workshop (CEUR-WS Vol-3977)` · 2025
- [UFO2: The Desktop AgentOS](https://arxiv.org/abs/2504.14603) — `2025`
- [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26/) — `Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)` · 2025
- [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164) — `2024`
- ⚖️ [AutoDCWorkflow: LLM-based Data Cleaning Workflow Auto-Generation and Benchmark](https://arxiv.org/abs/2412.06724) — `2024`
- [CleanAgent: Automating Data Standardization with LLM-based Agents](https://arxiv.org/abs/2403.08291) — `2024`
- [LLM Based Multi-Agent Generation of Semi-structured Documents from Semantic Templates in the Public Administration Domain](https://arxiv.org/abs/2402.14871) — `2024`
- [LLM-based agents for automating the enhancement of user story quality: An early report](https://arxiv.org/abs/2403.09442) — `2024`
- [MALADE: Orchestration of LLM-powered Agents with Retrieval Augmented Generation for Pharmacovigilance](https://arxiv.org/abs/2408.01869) — `2024`
- [MoA is All You Need: Building LLM Research Team using Mixture of Agents](https://arxiv.org/abs/2409.07487) — `2024`
- [PENTEST-AI: An LLM-Powered Multi-Agents Framework for Penetration Testing Automation Leveraging MITRE ATT&CK](https://ieeexplore.ieee.org/document/10679480) — `2024 IEEE International Conference on Cyber Security and Resilience (CSR)` · 2024
- ⚖️ [PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing](https://www.usenix.org/conference/usenixsecurity24/presentation/deng) — `33rd USENIX Security Symposium (USENIX Security 24)` · 2024
- [Perceive, Reflect, and Plan: Designing LLM Agent for Goal-Directed City Navigation without Instructions](https://arxiv.org/abs/2408.04168) — `2024`
- [StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows](https://arxiv.org/abs/2403.11322) — `2024`
- [SynthAI: A Multi Agent Generative AI Framework for Automated Modular HLS Design Generation](https://arxiv.org/abs/2405.16072) — `2024`
- ⚖️ [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://aclanthology.org/2024.acl-long.371/) — `Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)` · 2024
- [Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485) — `2023`
- [Large Language Model Enhanced Multi-Agent Systems for 6G Communications](https://arxiv.org/abs/2312.07850) — `2023`
- [Self-Adaptive Large Language Model (LLM)-Based Multiagent Systems](https://arxiv.org/abs/2307.06187) — `2023`

#### Coordination & organization ([`coordination`](https://juliodosreis.com/awesome-agenticsystems/areas/coordination))

- [A Diagnostic-Driven Multi-Agent Socratic Teaching System](https://doi.org/10.1145/3796114.3796119) — `Proceedings of the 2026 Asia-Pacific Intelligent Educational Technologies Conference (APIET 2026)` · 2026
- [A Multi-Agent AI System for Automated High School Transcript Processing: Collaborative Document Analysis at Scale](https://arxiv.org/abs/2606.13916) — `2026`
- [Artifact validity under varying agent configurations in LLM-assisted software development: A comparative analysis](https://www.sciencedirect.com/science/article/abs/pii/S095058492600011X) — `Information and Software Technology` · 2026
- [From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration](https://arxiv.org/abs/2603.04474) — `2026`
- [Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.17148) — `2026`
- [Hetero-Designer: Automated Design of Multi-Agent Systems with Heterogeneous LLMs](https://aclanthology.org/2026.acl-long.1272/) — `Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)` · 2026
- [IntelliCode: A Multi-Agent LLM Tutoring System with Centralized Learner Modeling](https://aclanthology.org/2026.eacl-demo.10/) — `Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) -- System Demonstrations` · 2026
- [Multi-Agent Teams Hold Experts Back](https://arxiv.org/abs/2602.01011) — `2026`
- [PentestLLM: A Cyber Kill Chain-driven Multi-Agent Large Language Model Framework Enabling Automatic Penetration Testing](https://ieeexplore.ieee.org/document/11645571) — `2026 IEEE 50th Annual Computers, Software, and Applications Conference (COMPSAC)` · 2026
- [QUARE: Quality-Aware Requirements Analysis through Multi-Agent Dialectical Negotiation](https://arxiv.org/abs/2603.11890) — `2026`
- [UFO3: Weaving the Digital Agent Galaxy](https://arxiv.org/abs/2511.11332) — `2026`
- [A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making](https://aclanthology.org/2025.emnlp-main.1699/) — `Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing` · 2025
- [AdaCoder: An Adaptive Planning and Multi-Agent Framework for Function-Level Code Generation](https://arxiv.org/abs/2504.04220) — `2025`
- [AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology](https://ieeexplore.ieee.org/document/11052788) — `2025 IEEE/ACM Second International Conference on AI Foundation Models and Software Engineering (Forge)` · 2025
- [Controller Makes Pentesting Better: An Improved Multi-Agent Automated Penetration Testing Framework](https://ieeexplore.ieee.org/document/11354714) — `2025 IEEE 24th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom)` · 2025
- [LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring](https://arxiv.org/abs/2509.14834) — `2025`
- [Mixture-of-Agents Enhances Large Language Model Capabilities](https://openreview.net/forum?id=h0ZfDIrj7T) — `The Thirteenth International Conference on Learning Representations` · 2025
- [MultiTutor: Collaborative LLM Agents for Multimodal Student Support](https://proceedings.mlr.press/v273/sun25a.html) — `PMLR 2025` · 2025  
  A multi-agent tutoring framework that coordinates specialized expert agents to provide personalized, multimodal educational support using internet search and code generation.
- [A Multi-Agent Conversational Recommender System](https://arxiv.org/abs/2402.01135) — `2024`
- [Challenges Faced by Large Language Models in Solving Multi-Agent Flocking](https://arxiv.org/abs/2404.04752) — `2024`
- [ChatDev: Communicative Agents for Software Development](https://aclanthology.org/2024.acl-long.810/) — `Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)` · 2024
- [Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2410.02506) — `2024`
- [LawLuo: A Multi-Agent Collaborative Framework for Multi-Round Chinese Legal Consultation](https://arxiv.org/abs/2407.16252) — `2024`
- [Leveraging Multi-AI Agents for Cross-Domain Knowledge Discovery](https://arxiv.org/abs/2404.08511) — `2024`
- [Mdagents: An adaptive collaboration of llms for medical decision-making](https://proceedings.neurips.cc/paper_files/paper/2024/hash/90d1fc07f46e31387978b88e7e057a31-Abstract-Conference.html) — `Advances in Neural Information Processing Systems` · 2024
- [Multi-Agent Large Language Models for Conversational Task-Solving](https://arxiv.org/abs/2410.22932) — `2024`
- [SimAC: Simulating Agile Collaboration to Generate Acceptance Criteria in User Story Elaboration](https://link.springer.com/article/10.1007/s10515-024-00448-7) — `Automated Software Engineering` · 2024
- [Simulating Classroom Education with LLM-Empowered Agents](https://arxiv.org/abs/2406.19226) — `2024`
- [Simulating Human Strategic Behavior: Comparing Single and Multi-agent LLMs](https://arxiv.org/abs/2402.08189) — `2024`
- [Towards Efficient LLM Grounding for Embodied Multi-Agent Collaboration](https://arxiv.org/abs/2405.14314) — `2024`
- [AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation](https://arxiv.org/abs/2312.13010) — `2023`
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — `COLM 2024` · 2023  
  Models the application as a conversation between configurable agents, with humans and code execution as first-class participants.
- [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://proceedings.neurips.cc/paper/2023/hash/a3621ee907def47c1b952ade25c67698-Abstract-Conference.html) — `Advances in Neural Information Processing Systems` · 2023
- [Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication](https://doi.org/10.18653/v1/2023.emnlp-main.936) — `Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing` · 2023
- [MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning](https://arxiv.org/abs/2311.10537) — `2023`
- [MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) — `ICLR 2024` · 2023  
  Encodes the standard operating procedures of a software company as agent roles chained by structured artifacts.

#### Interoperability & protocols ([`interoperability`](https://juliodosreis.com/awesome-agenticsystems/areas/interoperability))

- 📖 [A survey of agent interoperability protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)](https://arxiv.org/abs/2505.02279) — `arXiv preprint arXiv:2505.02279` · 2025
- [Beyond DNS: Unlocking the Internet of AI Agents via the NANDA Index and Verified AgentFacts](https://arxiv.org/abs/2507.14263) — `2025`
- [Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence](https://arxiv.org/abs/2407.07061) — `2024`

#### Harness, scaffolding & AgentOps ([`engineering`](https://juliodosreis.com/awesome-agenticsystems/areas/engineering))

- [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528) — `2026`  
  A framework for harnessed agentic RL, where the deploy-time harness runs the environment loop and the trainer receives only request-response pairs.
- [Breaking the 1.58-bit Barrier for Ternary LLMs](https://arxiv.org/abs/2609.16338) — `2026`  
  Explores extreme quantization for LLMs, pushing ternary weight representations below the 1.58-bit barrier to dramatically improve inference efficiency.
- [Coding-agents can replicate scientific machine learning papers](https://arxiv.org/abs/2607.02134) — `2026`  
  A replication workflow implemented as a coding-agent skill, where each paper claim becomes a recorded target and completion depends on workspace evidence passing validation checks.
- [Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs](https://arxiv.org/abs/2607.04371) — `2026`  
  A compressed hybrid-MoE variant tuned for interactive serving, roughly doubling server throughput at matched user throughput and raising 1M-token concurrency from one request to eight.
- [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557) — `2026`  
  Trains agents inside the real inference harness they are deployed with, by proxying the harness's model calls into a standard RL codebase and running each rollout in its own container.
- [Quantization Degradation in Large Language Models: A Signal-Noise Perspective](https://arxiv.org/abs/2608.08188) — `2026`  
  Analyzes the performance degradation of Large Language Models after quantization through a signal-to-noise ratio framework.
- 🔥 [The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI](https://arxiv.org/abs/2607.06906) — `2026`  
  Holds six models constant and swaps only the orchestration layer, cutting cost per task 41% and tokens per task 38% at parity quality.
- [An Empirical Study of Agent Developer Practices in AI Agent Frameworks](https://arxiv.org/abs/2512.01939) — `2025`
- [Edge-First Language Model Inference: Models, Metrics, and Tradeoffs](https://arxiv.org/abs/2505.16508) — `2025`  
  An empirical benchmarking study of edge-first Small Language Model (SLM) inference, exploring the tradeoffs between on-device performance, energy consumption, and cloud fallback.
- [Let It Flow: Agentic Crafting on Rock and Roll, Building the ROME Model within an Open Agentic Learning Ecosystem](https://arxiv.org/abs/2512.24873) — `2025`
- [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a4b6ad6b48850c0c331d1259fc66a69c-Abstract-Conference.html) — `International Conference on Learning Representations` · 2025
- [AgentLite: A Lightweight Library for Building and Advancing Task-Oriented LLM Agent System](https://arxiv.org/abs/2402.15538) — `2024`
- [AgentScope: A Flexible yet Robust Multi-Agent Platform](https://arxiv.org/abs/2402.14034) — `2024`
- [Gentopia: A Collaborative Platform for Tool-Augmented LLMs](https://arxiv.org/abs/2308.04030) — `2023`


### Measurement and control

How a system is measured, and how its risk is governed.

#### Evaluation & benchmarks ([`evaluation`](https://juliodosreis.com/awesome-agenticsystems/areas/evaluation))

- [Benchmarking large language model-based agent systems for clinical decision tasks](https://www.nature.com/articles/s41746-026-02443-6) — `npj Digital Medicine` · 2026
- ⚖️ [ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?](https://arxiv.org/abs/2608.03874) — `2026`  
  Five domains of 100 interconnected subtasks ordered by difficulty, built to separate skill consolidation from adaptation to recent context.
- ⚖️ [Diagon: A Programmable Testbed for AI-Agent Cognitive Labor Markets](https://arxiv.org/abs/2604.06688) — `arXiv preprint arXiv:2604.06688` · 2026
- 🔥 [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391) — `2026`  
  Scores candidate solutions by taking the expectation over scoring-token logits. Verification then scales with granularity, repetition and criteria decomposition.
- ⚖️ [MarketBench: Evaluating AI Agents as Market Participants](https://arxiv.org/abs/2604.23897) — `arXiv preprint arXiv:2604.23897` · 2026
- 🔥 ⚖️ [One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows](https://arxiv.org/abs/2608.19741) — `2026`  
  507 policy-conditioned workflows in an MCP-compatible sandbox, scored on the persistent backend state an agent leaves behind.
- ⚖️ [Protocol Agent: What If Agents Could Use Cryptography In Everyday Life?](https://arxiv.org/abs/2602.01304) — `2026`
- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227) — `2026`  
  Argues automatic harness evolution must be compared against test-time scaling under matched feedback and inference budgets, and finds it does not outperform that baseline or generalize to held-out tasks.
- ⚖️ [AI Hospital: Benchmarking Large Language Models in a Multi-agent Medical Interaction Simulator](https://aclanthology.org/2025.coling-main.680.pdf) — `Proceedings of the 31st International Conference on Computational Linguistics` · 2025
- ⚖️ [AutoPenBench: A Vulnerability Testing Benchmark for Generative Agents](https://aclanthology.org/2025.emnlp-industry.114/) — `Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track` · 2025
- [Exploring LLM Agents for Cleaning Tabular Machine Learning Datasets](https://arxiv.org/abs/2503.06664) — `2025`
- [How Do LLMs Fail In Agentic Scenarios? A Qualitative Analysis of Success and Failure Scenarios of Various LLMs in Agentic Simulations](https://arxiv.org/abs/2512.07497) — `2025`
- ⚖️ [MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents](https://arxiv.org/abs/2501.14654) — `2025`
- ⚖️ [Sequential Diagnosis with Language Models](https://arxiv.org/abs/2506.22405) — `2025`
- ⚖️ [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) — `2025`
- ⚖️ [Evaluating Language Model Agency through Negotiations](https://arxiv.org/abs/2401.04536) — `International Conference on Learning Representations` · 2024
- ⚖️ [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — `2024`
- ⚖️ [SWE-bench: Can Language Models Resolve Real-world Github Issues?](https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html) — `International Conference on Learning Representations` · 2024
- ⚖️ [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4410c0711e9154a7a2d26f9b3816d1ef-Abstract-Conference.html) — `International Conference on Learning Representations` · 2024
- ⚖️ [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://arxiv.org/abs/2409.08264) — `2024`
- 🔥 ⚖️ [tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — `ICLR 2025` · 2024  
  Evaluates the agent against a simulated user and domain policies, measuring consistency across runs on top of per-task success.
- 🔥 ⚖️ [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) — `ICLR 2024` · 2023  
  Gathers eight heterogeneous interactive environments to measure agents on multi-turn tasks under a common protocol.

#### Safety, trust & governance ([`safety`](https://juliodosreis.com/awesome-agenticsystems/areas/safety))

- 📖 [The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088) — `2026`
- 📖 [Toward Safe LLM Agents: A Survey of Specification, Verification, and Enforcement](https://arxiv.org/abs/2608.14590) — `2026`
- [Auditable Agents](https://arxiv.org/abs/2604.05485) — `2026`
- [Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks](https://arxiv.org/abs/2606.28679) — `2026`
- [Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice](https://arxiv.org/abs/2603.07191) — `2026`
- [Governance-Aware Agent Telemetry for Closed-Loop Enforcement in Multi-Agent AI Systems](https://arxiv.org/abs/2604.05119) — `2026`
- [Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations](https://arxiv.org/abs/2607.01181) — `2026`  
  Augments RL with verifiable rewards with an adversarial discriminator trained on human demonstrations, so non-verifiable properties like style and structure are optimized alongside task accuracy.
- [Runtime Policy Enforcement for MCP-Based LLM Agents](https://www.mdpi.com/2079-9292/15/13/2829) — `Electronics` · 2026
- [The Verifier Tax: Horizon Dependent Safety Success Tradeoffs in Tool Using LLM Agents](https://arxiv.org/abs/2603.19328) — `2026`
- [Toward Trustworthy Large Language Model Agents in Healthcare](https://arxiv.org/abs/2607.05055) — `2026`
- [AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents](https://arxiv.org/abs/2503.18666) — `Proc. ICSE'26, pages 2938-2950. ACM, 2026` · 2025
- [Authenticated Delegation and Authorized AI Agents](https://arxiv.org/abs/2501.09674) — `2025`
- [DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/77f3b26c7907aa27b207df9b9d43f29a-Abstract-Conference.html) — `Advances in Neural Information Processing Systems` · 2025
- [Enforcing Temporal Constraints for LLM Agents](https://arxiv.org/abs/2512.23738) — `2025`
- [Governance-as-a-Service: A Multi-Agent Framework for AI System Compliance and Policy Enforcement](https://arxiv.org/abs/2508.18765) — `2025`
- [Graph-Symbolic Policy Enforcement and Control (G-SPEC): A Neuro-Symbolic Framework for Safe Agentic AI in 5G Autonomous Networks](https://arxiv.org/abs/2512.20275) — `2025`
- [MiniScope: Authorizing Agents with Least-Privilege Permissions](https://arxiv.org/abs/2512.11147) — `2025`
- [SHIELDA: Structured Handling of Exceptions in LLM-Driven Agentic Workflows](https://arxiv.org/abs/2508.07935) — `2025`
- [VeriGuard: Enhancing LLM Agent Safety via Verified Code Generation](https://arxiv.org/abs/2510.05156) — `2025`
- [BlockAgents: Towards Byzantine-Robust LLM-Based Multi-Agent Coordination via Blockchain](https://doi.org/10.1145/3674399.3674445) — `ACM Turing Award Celebration Conference 2024` · 2024
- [RedAgent: Red Teaming Large Language Models with Context-aware Autonomous Language Agent](https://arxiv.org/abs/2407.16667) — `2024`
<!-- /gen:papers -->

## Resources

<!-- gen:resource-count -->
35 resources listed, in 8 of the 8 kinds.
<!-- /gen:resource-count -->

Each entry is a link with a one or two sentence description, filed under one kind. An entry with an `area` also appears on that area's page of the site, below the papers. The kinds and the rule for each one are listed under [resource kinds](./CONTRIBUTING.md#resource-kinds) in CONTRIBUTING.md.

<!-- gen:resources -->
### Protocols ([`protocol`](https://juliodosreis.com/awesome-agenticsystems/resources#protocol))

Specifications for connecting agents to tools, to clients or to other agents.

- [Agent Client Protocol (ACP)](https://agentclientprotocol.com/) — Zed Industries, 2025  
  Protocol for communication between code editors and coding agents, for local and remote agents. An editor that implements it connects to any agent that implements it, with no integration specific to each agent.
- [Agent Payments Protocol (AP2)](https://ap2-protocol.org/) — Google, 2025  
  Protocol for payments started by agents, available as an extension of A2A. Signed mandates record the intent of the user and the approval of the cart, so the merchant and the payment provider can check what the user authorized.
- [Agent2Agent Protocol (A2A)](https://a2a-protocol.org/) — Linux Foundation, 2025  
  Protocol for communication between agents built on different frameworks. An agent publishes an Agent Card that describes its skills, and a client agent sends it tasks over JSON-RPC on HTTP, with streaming and push notifications for long-running tasks.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — Agentic AI Foundation, 2024  
  Client-server protocol over JSON-RPC. A server exposes tools, resources and prompts, and an LLM application connects to it as a client.

### Orchestration Frameworks ([`framework`](https://juliodosreis.com/awesome-agenticsystems/resources#framework))

Code frameworks for orchestrating agents: control flow, state, tool calls and multi-agent workflows.

- [Agent Development Kit (ADK)](https://github.com/google/adk-python) — Google, 2025  
  Python toolkit for defining agents in code, composing them into multi-agent systems, and evaluating and deploying them.
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) — Anthropic, 2025  
  Python SDK that runs the Claude Code agent loop from a program, with its built-in tools, custom tools defined as in-process MCP servers, and hooks on tool calls. The package bundles the Claude Code CLI.
- [CrewAI](https://github.com/crewAIInc/crewAI)  
  Python framework for running groups of role-based agents that share tasks, with sequential and hierarchical processes.
- [LangGraph](https://github.com/langchain-ai/langgraph) — LangChain, 2024  
  Library for building agents as graphs of nodes over a shared state, with checkpointing and interrupts for human review.
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — Microsoft, 2025  
  Framework for building agents and multi-agent workflows in Python and .NET, with a Go SDK in a separate repository. The archived AutoGen repository points to it as its successor.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) — OpenAI, 2025  
  Python framework for multi-agent workflows built from agents with instructions and tools, handoffs between agents, guardrails and tracing. Supports the OpenAI APIs and other model providers.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) — Pydantic, 2024  
  Python agent framework with typed tool definitions and structured outputs validated by Pydantic models, for several model providers.
- [smolagents](https://github.com/huggingface/smolagents) — Hugging Face, 2024  
  Python library for agents that write their actions as Python code snippets, executed locally or in a sandbox.

### Skills ([`skill`](https://juliodosreis.com/awesome-agenticsystems/resources#skill))

Packaged instructions, scripts and reference files that an agent loads when a task requires them.

- [Agent Skills specification](https://agentskills.io/) — 2025  
  Open format for agent skills. A skill is a folder with a SKILL.md file that holds a name, a description and instructions, and can bundle scripts, reference files and templates that the agent loads when a task requires them.
- [Anthropic Skills repository](https://github.com/anthropics/skills) — Anthropic, 2025  
  Repository of skills for Claude, each one a folder with a SKILL.md file. Includes skills for creative tasks, web application testing and MCP server generation, and the document skills for Word, PowerPoint, Excel and PDF files.

### Benchmarks ([`benchmark`](https://juliodosreis.com/awesome-agenticsystems/resources#benchmark))

Benchmarks, leaderboards and evaluation harnesses released as a website, dataset or repository. A benchmark published as a paper also gets a record in the paper collection, under the evaluation area.

- [Berkeley Function Calling Leaderboard (BFCL)](https://gorilla.cs.berkeley.edu/leaderboard.html) — UC Berkeley, 2024  
  Leaderboard that measures how accurately language models call functions, over single-turn and multi-turn tests. Version 4 adds agentic evaluation categories.
- [Holistic Agent Leaderboard (HAL)](https://hal.cs.princeton.edu/) — Princeton University, 2025  
  Third-party leaderboard that runs agents on nine benchmarks and reports accuracy together with cost. A separate dashboard reports reliability measures such as consistency and robustness.
- [SWE-bench leaderboards](https://www.swebench.com/) — 2023  
  Leaderboards for SWE-bench and its variants (Verified, Lite, Multimodal, Multilingual, Bash Only). Each entry reports the percentage of GitHub issues an agent resolved, checked by the tests of the repository.
- [Terminal-Bench](https://www.tbench.ai/) — Stanford University and Laude Institute, 2025  
  Benchmark of tasks that an agent completes in a terminal environment. The leaderboard reports the resolution rate, cost and tokens of each model and agent pair.

### Books ([`book`](https://juliodosreis.com/awesome-agenticsystems/resources#book))

Books covering agents, or the methods agents are built from.

- [AI Engineering](https://huyenchip.com/books/) — Chip Huyen, 2025  
  Book on building applications on top of foundation models. Covers evaluation, prompt engineering, retrieval-augmented generation, agents, finetuning and inference optimization.
- [Artificial Intelligence: A Modern Approach (4th edition)](https://aima.cs.berkeley.edu/) — Stuart Russell, Peter Norvig, 2020  
  Textbook on artificial intelligence. Chapter 2 defines intelligent agents and their environments, and later chapters cover search, planning, knowledge representation and learning.
- [Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations](http://www.masfoundations.org/) — Yoav Shoham, Kevin Leyton-Brown, 2008  
  Textbook on multiagent systems covering distributed problem solving, game theory, social choice, mechanism design and logics of knowledge and belief. The site offers the eBook as a free download.
- [Reinforcement Learning: An Introduction (2nd edition)](http://incompleteideas.net/book/the-book-2nd.html) — Richard S. Sutton, Andrew G. Barto, 2018  
  Textbook on reinforcement learning: Markov decision processes, dynamic programming, Monte Carlo and temporal-difference methods, function approximation and policy gradient methods. The authors publish the full text on the site.

### Courses ([`course`](https://juliodosreis.com/awesome-agenticsystems/resources#course))

Courses and lecture series with recorded or written material.

- [Advanced Large Language Model Agents (MOOC, Spring 2025)](https://llmagents-learning.org/sp25) — Dawn Song, Xinyun Chen, Kaiyu Yang · UC Berkeley, 2025  
  Lecture series that follows the Fall 2024 LLM Agents MOOC, with recorded lectures on reasoning and planning, agents for coding and web tasks, mathematics and theorem proving, and agent safety.
- [Agentic AI](https://www.deeplearning.ai/courses/agentic-ai/) — Andrew Ng · DeepLearning.AI, 2025  
  Course of 31 video lessons with code examples and graded assignments on reflection, tool use, planning and multi-agent workflows, and on the evaluation and error analysis of agentic systems.
- [AI Agents Course](https://huggingface.co/learn/agents-course) — Hugging Face, 2025  
  Course with written units and exercises on agent fundamentals and on building agents with smolagents, LlamaIndex and LangGraph. The final assignment evaluates the agent of each student on questions from the GAIA benchmark.
- [Large Language Model Agents (MOOC, Fall 2024)](https://llmagents-learning.org/f24) — Dawn Song, Xinyun Chen · UC Berkeley, 2024  
  Lecture series with recordings and slides, given by guest speakers, on LLM reasoning, the history of LLM agents, agent frameworks such as AutoGen, agents for software development and robotics.

### Guides & Posts ([`guide`](https://juliodosreis.com/awesome-agenticsystems/resources#guide))

Articles and engineering posts on building and running agents.

- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) — Dex Horthy · HumanLayer, 2025  
  Twelve principles for building LLM applications, among them owning the prompts and the context window, treating tools as structured outputs, unifying execution state with business state and contacting humans through tool calls.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic, 2024  
  Article that separates workflows, where LLMs and tools follow predefined code paths, from agents, where the LLM directs its own tool use. Describes prompt chaining, routing, parallelization, orchestrator-workers and evaluator-optimizer.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic, 2025  
  Article on the tokens an agent holds in its context window: system prompts, tool definitions, examples, retrieval at the time of use, compaction, structured note-taking and sub-agents for long-horizon tasks.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — Anthropic, 2025  
  Engineering post on the Research feature of Claude, in which a lead agent plans the research and starts subagents that search in parallel. Covers prompt design, evaluation and the operation of the system in production.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — Lilian Weng, 2023  
  Blog post that describes an agent as an LLM with three components: planning (task decomposition and self-reflection), memory (short-term and long-term) and tool use. Reviews the papers behind each component and several case studies.

### Tools & SDKs ([`tool`](https://juliodosreis.com/awesome-agenticsystems/resources#tool))

Libraries, SDKs and developer tools for building, running or observing agents.

- [Browser Use](https://github.com/browser-use/browser-use) — Browser Use, 2024  
  Python library through which an LLM agent controls a web browser. The agent reads the state of the page and clicks, types and navigates.
- [E2B](https://github.com/e2b-dev/E2B) — E2B, 2023  
  Open-source infrastructure that runs code generated by AI models in isolated cloud sandboxes, with Python and JavaScript SDKs.
- [Inspect](https://inspect.aisi.org.uk/) — UK AI Security Institute, 2024  
  Python framework for evaluations of language models and agents, built from datasets, solvers, tools and scorers. Includes sandboxed tool execution, a log viewer and a collection of pre-built evaluations.
- [Langfuse](https://github.com/langfuse/langfuse) — Langfuse  
  Open-source platform for tracing LLM applications and agents, with evaluations, prompt management and datasets.
<!-- /gen:resources -->

## Design decisions

- **A validated vocabulary.** The Zod schema reads the vocabulary from `taxonomy.yml`. A nonexistent area or topic breaks the build and prints the valid values. The taxonomy validates itself too: an area pointing at a missing layer, or an orphaned domain, stops compilation.
- **A taxonomy with a declared bibliographic basis** (CoALA, Wang et al. 2024, Luo et al. 2025, harness survey 2026), browsable at `/taxonomy`. Each reference states which part of the vocabulary it supports.
- **Three navigation axes for papers**: by area (contribution), by domain (application), and by reading path (the `relates_to` graph between papers, navigable in both directions). Resources are grouped by kind on `/resources`, and a resource with an `area` is also listed on that area's page.
- **Adding a paper or a resource is a GitHub issue.** A workflow turns the issue into a pull request that holds one file, with no local setup.
- **Site-wide search** (Pagefind), an [RSS feed](https://juliodosreis.com/awesome-agenticsystems/rss.xml) of new additions, and a sitemap.

## The taxonomy

<!-- gen:counts -->
11 areas in 4 layers, 58 topics and 33 facet values across 5 facets.
<!-- /gen:counts -->

It lives in `src/data/taxonomy.yml` (v3) and is the single source of truth: the validator, the site, the guides and the issue forms all read from that one file. Besides the paper vocabulary below, the file defines the resource kinds, listed under [resource kinds](./CONTRIBUTING.md#resource-kinds).

<!-- gen:areas-table -->
| Layer | Areas |
|---|---|
| Overview | `foundations` |
| Agent capabilities | `reasoning-planning`, `memory`, `tools-context`, `learning-evolution` |
| System structure | `architectures`, `coordination`, `interoperability`, `engineering` |
| Measurement and control | `evaluation`, `safety` |
<!-- /gen:areas-table -->

The complete vocabulary, with usage counts, is at [`/taxonomy`](https://juliodosreis.com/awesome-agenticsystems/taxonomy). The design and the criterion behind each field are documented in [TAXONOMY.md](./TAXONOMY.md), and the rule for picking an area under [area selection](./CONTRIBUTING.md#area-selection).

## Local development

Requires Node.js 22.12 or newer (an Astro 7 requirement). The exact version is in `.nvmrc`, which is also what CI uses: `nvm use` picks it up.

```bash
npm install
npm run dev
```

Python 3.11+ is needed only for the scripts: `npm run docs`, `npm test` and `scripts/add.py`. Browsing and building the site need nothing but Node.

```bash
pip install -r requirements-dev.txt
```

The dev server starts at `http://localhost:4321`.

> The search box in the header is powered by Pagefind, which indexes the **built** HTML. Under `astro dev` it returns nothing, which is expected. To exercise search, run `npm run build && npm run preview`.

> Note: as of Astro 7 the dev server runs as a background daemon. Ctrl+C does not stop it, and a later `npm run dev` attaches to the existing instance, which can serve a stale version of the site. To stop it:
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
| `npm run build` | Runs `astro check` (types + paper and resource validation) and builds to `dist/` |
| `npm run preview` | Serves `dist/` to review the final build |
| `npm run docs` | Regenerates the doc sections and issue form from `taxonomy.yml` |
| `npm run docs:check` | Fails if those are stale |
| `npm test` | Runs the full test suite (~20s) |
| `npm run test:fast` | Skips the tests that shell out to a real build (<1s) |
| `python scripts/add.py <arxiv-id>` | Creates a record from arXiv metadata |

`npm run docs` also rewrites the paper and resource listings in this README and the counts in `.github/badges.json`. On `main`, `docs_sync.yml` runs it after each merge that touches a paper, a resource or the taxonomy, and commits the result.

`npm run build` gates deployment: a type error, or a paper or resource that fails taxonomy validation, stops publication.

### Layout

| Path | Contents |
|---|---|
| `src/content/papers/` | One `.yml` per paper. |
| `src/content/resources/` | One `.yml` per resource. |
| `src/data/taxonomy.yml` | Single source of truth: layers, areas, topics, facets, domains and references. |
| `src/content.config.ts` | Zod schemas of both collections, built from the taxonomy vocabulary. Enforces the three paper states. |
| `src/lib/taxonomy.ts` | Shared loader for `taxonomy.yml` plus integrity guards (`assertGroupsResolve`). |
| `src/lib/papers.ts` | Collection helpers: publication logic, author formatting, id/filename check. |
| `src/lib/resources.ts` | Resource helpers: grouping by kind, the "by" line, id/filename check. |
| `src/lib/url.ts` | `url()` helper for internal links. The site lives under a subpath, so hardcoding routes breaks every fork. |
| `src/layouts/Layout.astro` | Shared shell: header, sidebar with the areas and the resource kinds, client scripts. |
| `src/pages/` | Routes: `/`, `/areas`, `/domains`, `/taxonomy`, `/papers/[id]`, `/resources`, `/rss.xml`. |
| `public/` | Static files (favicon). |
| `scripts/` | `arxiv.py` (shared metadata fetch), `add.py` (local capture), `process_issue.py` and `process_resource_issue.py` (used by the Action), `gen_docs.py` (README listings, doc blocks, issue form, badges). |
| `tests/` | pytest suite. `test_schema.py` is the important one: it falsifies records on purpose to prove the build rejects them. |
| `.github/workflows/` | `issue_ops.yml` (issue intake), `docs_sync.yml` (regenerates the docs on `main`), `validate.yml` (build on every PR), `deploy.yml` (GitHub Pages). |

## Tests

```bash
npm test
```

The suite covers the two issue parsers, for papers and for resources, which run unsupervised, along with the doc generator and the build-time guards. The assertions cover the error messages as well as the exit codes, since a rejection a contributor cannot act on leaves the submission stuck.

`tests/test_schema.py` is deliberately slow. It falsifies a record or the taxonomy and runs a real `npm run build` per case. A passing `npm run build` proves only that valid data compiles, and leaves the behavior of the guards unmeasured. Skip it locally with `npm run test:fast`.

## Contributing

| Contribution | Path |
|---|---|
| Suggest a paper | *Add a Paper* issue form. See [issue submission](./CONTRIBUTING.md#issue-submission). |
| Suggest a resource | *Add a Resource* issue form. See [resource submission](./CONTRIBUTING.md#resource-submission). |
| Summarize a paper, or edit a paper or resource record | Pull request on the `.yml` file. See [direct edit](./CONTRIBUTING.md#direct-edit) and [resource records](./CONTRIBUTING.md#resource-records). |
| Report a misclassified paper | *Fix a classification* issue form. See [questions and issues](./CONTRIBUTING.md#questions-and-issues). |
| Propose a term for the vocabulary | *Propose a taxonomy change* issue form. See [changing the taxonomy](./TAXONOMY.md#changing-the-taxonomy). |

Participation is covered by the [Code of Conduct](./CODE_OF_CONDUCT.md).

## Citing this collection

For citing the taxonomy or the collection, the repository carries a [CITATION.cff](./CITATION.cff), which GitHub's "Cite this repository" button reads. It covers the classification work only. The papers themselves are cited directly.

## License

Two licenses, because the repository holds two different things:

- **Code** (`src/`, `scripts/`, `.github/`): [MIT](./LICENSE).
- **The paper collection** (`src/content/papers/`) and the taxonomy (`src/data/taxonomy.yml`): [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Bibliographic metadata is reusable without conditions.

The papers themselves carry no license from this repository. They stay under the terms their publishers set. See [LICENSE](LICENSE).
