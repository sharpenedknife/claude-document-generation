---
doc_type: architecture
domain: SYSTEM
builder_version: "v1.0"
generated_by: research_builder
generated_at: 2026-04-03T00:00:00Z
audience: intermediate
difficulty: medium
time_estimate: "30-minutes"
prerequisites: []
tags: [ai-agents, multi-agent, orchestration, memory, react, plan-and-execute]
status: active
version: "1.0"
last_updated: 2026-04-03
---

# SYSTEM: AI Agent Architectural Patterns

**Purpose:** Ground the docgen pipeline architecture in production-validated patterns. Covers single vs multi-agent decisions, the four-part framework, orchestration topology, memory types, and planning approaches.
**Search keywords:** ai agent architecture, multi-agent orchestration, ReAct framework, agent memory types, supervisor pattern, plan-and-execute, sequential orchestration

---

## 1. Single vs Multi-Agent Decision

Default to a single agent. Add agents only when tasks require distinct tool sets, parallel execution, or exceed a single context window.

| Factor | Single Agent | Multi-Agent | Source |
|---|---|---|---|
| Task decomposability | Subtasks share context and tools | Subtasks are independent with distinct tools | Anthropic 2024 |
| Context window pressure | Total tokens fit within one window | Information exceeds single context window | Anthropic 2025 |
| Latency tolerance | Low-latency required | Higher latency acceptable (multi-agent uses ~15× more tokens than chat) | Anthropic 2025 |
| Error isolation | Acceptable to retry entire chain | Need per-stage rollback and independent failure domains | Microsoft Azure Architecture Center 2026 |

> **Rule:** Start single-agent. The 15× token overhead of multi-agent systems must be justified by a measured quality improvement.

---

## 2. Core Components: The Four-Part Framework

Every agent consists of four primitives (Anthropic 2024; Hu et al., arXiv 2512.13564, 2025):

| Component | Role | Docgen Example |
|---|---|---|
| **LLM** | Reasoning engine — interprets input, generates plans | Selecting doc template based on `doc_type` |
| **Contextual Memory** | Persists facts, traces, and working state across steps | Storing extracted research facts between pipeline stages |
| **External Functions / Sub-agents** | Tools or child agents the LLM invokes to act on environment | `web_search`, `fetch_template`, `validate_yaml` tool calls |
| **Routing** | Classifies input and dispatches to specialized handlers | Directing `architecture` docs to structure-focused agent vs. `tutorial` to step-focused agent |

> Postcondition: you can identify and label the four primitives in any agent system.

---

## 3. Multi-Agent Orchestration Patterns

Four patterns ranked by complexity (Anthropic 2024; Microsoft Azure Architecture Center 2026; AWS Multi-Agent Guidance 2025):

| Pattern | Use Case | Execution Model | When to Choose |
|---|---|---|---|
| **Sequential Orchestration** | Linear pipelines with clear stage dependencies (draft → review → polish) | Agent A output feeds Agent B; deterministic order | Tasks decompose into fixed, ordered subtasks with no parallelism needed |
| **Parallel (Fan-out/Fan-in)** | Independent analyses on same input (multi-section doc generation) | N agents run concurrently; results aggregated by merger | Subtasks are independent and latency reduction matters |
| **Supervisor Pattern** | Dynamic delegation where a coordinator assigns work to specialist agents | Supervisor LLM breaks task → delegates to workers → synthesizes results | Subtasks cannot be predetermined; require runtime planning |
| **Planning Agent** | Complex open-ended problems requiring iterative replanning | Manager maintains task ledger; backtracks and re-delegates as needed | No predetermined solution path; requires human-reviewable plan |

**For docgen:** Sequential Orchestration is the primary pattern (parse → template → generate → validate → assemble). Supervisor is the upgrade path when docgen complexity grows.

---

## 4. Memory Architecture: Three Functional Types

Taxonomy from Hu et al. (arXiv 2512.13564, Dec 2025), corroborated by ACM TOIS survey (2025):

| Memory Type | What It Stores | Retrieval Trigger | Docgen Application |
|---|---|---|---|
| **Factual Memory** | Domain knowledge, schema definitions, template rules | Semantic similarity search at planning time | `DOC_CANONICAL_TEMPLATE` specs and domain vocabulary |
| **Experiential Memory (Decision Trace)** | Past agent decisions, outcomes, extracted insights from completed episodes | Task-type match; analogical recall of prior runs | "Architecture docs with >5 tables scored higher on review" — recalled on future runs |
| **Working Memory** | Active context: current plan, intermediate outputs, tool results | Always loaded; compacted when approaching token limit | Current YAML frontmatter, partially generated sections, validation errors in progress |

### Decision Trace Memory — the self-improvement mechanism

The ExpeL framework (Zhao et al., AAAI 2024) demonstrated that agents storing natural-language insights extracted from trial-and-error trajectories improve consistently as experiences accumulate — without weight updates. In docgen: an agent that failed a quality gate on a prior run can recall *why* it failed and adjust its generation strategy.

**In this system:** The `metrics/LOG_Generation.md` and `backlog/SYSTEM_DEBT.md` files serve as lightweight experiential memory — recording what failed and why so future generation runs avoid the same mistakes.

---

## 5. Planning Approaches: ReAct vs Plan-and-Execute

| Dimension | ReAct (Yao et al., ICLR 2023) | Plan-and-Execute (Wang et al., ACL 2023) |
|---|---|---|
| **Loop** | Think → Act → Observe → repeat | Plan all steps → Execute sequentially → Replan on failure |
| **LLM calls** | One per tool invocation (higher cost) | Single planning call + cheaper per-step execution |
| **Planning horizon** | One step at a time (myopic, adaptive) | Full task decomposition upfront (global, less adaptive) |
| **Failure handling** | Self-corrects at each observation | Must detect failure explicitly and trigger replanning |
| **Best fit** | Exploratory tasks, dynamic environments, unknown tool needs | Well-defined workflows with predictable steps |
| **Adoption** | Default in AWS Bedrock Agents, LangChain, CrewAI | LangGraph Plan-and-Execute, BabyAGI derivatives |

**For docgen:** Plan-and-Execute is primary — document generation follows a predictable structure. ReAct serves as fallback *within* individual steps when an executor encounters unexpected input.

---

## 6. Common Failure Modes

| Failure | Cause | Mitigation |
|---|---|---|
| **Compounding errors** | Early-stage mistakes propagate through sequential pipelines unchecked | Insert programmatic validation gates between stages; halt on schema violation |
| **Tool misuse** | Ambiguous tool descriptions lead agent to select wrong function or pass wrong parameters | Write tool descriptions with explicit input formats, edge cases, and example invocations |
| **Memory drift** | Working memory accumulates stale or contradictory context over long runs | Compact at 80% window capacity; clear tool-result tokens after extraction; persist key facts externally |
| **Autonomy-oversight tension** | Agent acts beyond intended scope; hallucinates actions without grounding | Require confirmation for destructive actions; validate every output against ground-truth |
| **Infinite delegation loops** | Supervisor and workers hand tasks back and forth without resolution | Set max iteration caps (3–5 rounds); implement circuit-breaker patterns; log each handoff |

---

## 7. Production Best Practices

1. **Start with a single agent and one tool.** Add orchestration complexity only after measuring that single-agent fails a defined quality threshold. (Anthropic 2024)
2. **Invest more in tool descriptions than system prompts.** Anthropic's SWE-bench team found a tool-testing agent that rewrote tool descriptions cut task completion time by 40%. (Anthropic 2025)
3. **Implement structured note-taking for runs exceeding 50K tokens.** Persist a `progress.md` outside the context window; reload via retrieval at each planning step. (Anthropic "Context Engineering" 2025)
4. **Validate output between every pipeline stage.** Use programmatic schema checks (JSON Schema, YAML lint) for structure; use LLM-as-judge (0.0–1.0 scale) for semantic quality only. (Anthropic 2025)
5. **Enable production tracing from day one.** Log every tool call, token count, and planning decision. Adding tracing was the prerequisite to systematic debugging of multi-agent failures. (Anthropic 2025)
6. **Cap agent iterations explicitly.** Set `max_iterations=5` for ReAct loops and `max_replans=2` for Plan-and-Execute. Unbounded loops are the top cause of runaway cost. (AWS Bedrock Docs 2025, Microsoft Azure 2026)
7. **Use experiential memory to close the feedback loop.** After each run, extract one natural-language insight from the quality evaluation and persist it to the experiential memory store. (ExpeL, AAAI 2024)

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Agent repeats same tool call 3+ times with identical parameters | Tool returned an error the agent cannot parse | Add structured error responses: `{"error": "INVALID_PATH", "suggestion": "use absolute path"}` |
| Token count exceeds context window mid-pipeline | Working memory not compacted; accumulated tool results fill the window | Trigger compaction at 80% window capacity; summarize completed stages; persist key facts externally |
| Supervisor generates plan but no sub-agent executes | Sub-agent tool definitions missing from supervisor's tool list | Register each sub-agent as an explicit tool with typed input/output schemas; test tool discovery in isolation |
| Quality score drops after adding second agent | New agent duplicates work of first; token overhead exceeds value | Verify agents have non-overlapping tool sets and distinct system prompts |
| `429 ThrottlingException` during parallel fan-out | Concurrent agents exceed model API rate limits | Implement exponential backoff with random jitter; use request queuing with concurrency cap |

---

## Applied to Docgen

The docgen system maps directly to **Sequential Orchestration + Plan-and-Execute**: input parsing → template selection → section generation → validation → assembly. Within individual stages, ReAct provides adaptive fallback for ambiguous inputs. The three-type memory architecture ensures the system retains template rules (factual), learns from past quality scores (experiential via LOG_Generation.md + SYSTEM_DEBT.md), and maintains coherent state across sections (working) without overflow.

**Upgrade path:** When docgen adds parallel section generation, use Fan-out/Fan-in. When routing becomes too complex for rule-based decisions, introduce a Supervisor.

---

## Sources

- Anthropic, "Building Effective Agents," 2024
- Anthropic, "Multi-Agent Research System," 2025
- Anthropic, "Context Engineering," 2025
- Hu et al., arXiv 2512.13564, Dec 2025
- Zhao et al., ExpeL framework, AAAI 2024
- Yao et al., ReAct, ICLR 2023
- Wang et al., Plan-and-Execute, ACL 2023
- Microsoft Azure Architecture Center, Multi-Agent Design Patterns, 2026
- AWS Bedrock Multi-Agent Collaboration Docs, 2025
- ACM TOIS Agent Memory Survey, 2025
