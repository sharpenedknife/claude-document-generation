# Research Context Primer
**Copy-paste this into any Claude chat to get research help for the Documentation Builder.**
Last updated: April 2026

---

## About This Project

I'm building a **Documentation Generation System** ("Documentation Builder") — a Claude Project that takes any software product idea and generates a complete, implementation-ready documentation bundle that an AI coding agent (Cursor, Windsurf, Codex, Claude) can use to build the product.

**What it generates (Product Bundle — 11 docs):**
PRD → UX Research → UI Spec → Product Vision → Architecture → Data Schema → API Spec → Environment Setup → Dev Plan → CLAUDE.md → Starter Prompt

**How it works:**
1. User describes what they want to build
2. System runs a Research Gate — stops and asks user to collect real data before generating
3. User answers 8 intake questions (features, user flows, tech stack, integrations)
4. System generates all 11 docs in order, applying quality gates at each stage
5. Docs are delivered as a zip bundle ready for an AI coding agent to consume

**Tech approach:** Claude Project with a `skills/` folder of SKILL.md files (playbooks per doc type), lazy-loaded per stage. Token budget enforced per doc type. All docs pass 5 quality gates before delivery.

**Current version:** v1.7 (April 2026)

---

## What I Need From You

Pick the research task below that matches what I need, copy the filled-in version, and paste it after this primer. Return your findings in the format specified — I'll bring them back to the Documentation Builder to feed into the generation process.

---

## Research Task Templates

### TASK A — Competitive / Market Research

```
RESEARCH TASK: Competitive Analysis

Product idea: [FILL IN — 1-2 sentences: what it does, who it's for]

Research needed:
1. Who are the top 3-5 direct competitors? (same problem, same user)
2. What features does each competitor's MVP include?
3. What do users complain about in reviews? (G2, Trustpilot, Reddit, App Store)
4. What's the pricing model pattern? (freemium / per-seat / usage-based / flat)
5. What's the differentiation gap — what are none of them doing that users want?

Return format:
## Competitors
| Name | Core features | Main complaints | Pricing |
|------|--------------|----------------|---------|

## Differentiation Gap
- [insight 1]
- [insight 2]

## Recommended positioning
[1-2 sentences]
```

---

### TASK B — Tech Stack Research

```
RESEARCH TASK: Stack Decision

Product type: [FILL IN — e.g. "SaaS web app with real-time features", "mobile app", "AI chatbot"]
Team: [FILL IN — e.g. "solo developer, JavaScript background", "2 engineers, Python backend experience"]
Scale target: [FILL IN — e.g. "MVP for 100 users", "scale to 10K users in 6 months"]
Budget: [FILL IN — e.g. "bootstrap / free tier only", "up to $200/month infra"]

Research needed:
1. What's the best frontend framework for this? Why?
2. What's the best backend/API approach? Why?
3. What database fits the data model? (relational vs. document vs. vector)
4. Best auth solution for this stack?
5. Best deployment platform? (considering team skill + budget)
6. Any gotchas or known issues with this stack combination?

Return format:
## Recommended Stack
| Layer | Choice | Version | Why |
|-------|--------|---------|-----|
| Frontend | | | |
| Backend | | | |
| Database | | | |
| Auth | | | |
| Hosting | | | |

## Gotchas
- [anything to watch out for during build]

## Alternatives considered
| Option | Why rejected |
|--------|-------------|
```

---

### TASK C — User Research

```
RESEARCH TASK: User Flows & Pain Points

Product: [FILL IN — what it does]
Target user: [FILL IN — their role, context, technical level]

Research needed:
1. What does this user currently do to solve this problem (without my product)?
2. What are the exact steps in their current workflow? (step-by-step, as specific as possible)
3. Where does the current workflow break down or frustrate them?
4. What's their "first value moment" — the first thing that makes them feel the product is worth it?
5. What would make them NOT use this product?

Return format:
## Current Workflow (without product)
1. [step]
2. [step]
...

## Pain Points
| Step | Pain | Severity (1-3) |
|------|------|---------------|

## First Value Moment
[The specific action/outcome that makes them say "yes, this works"]

## Likely objections
- [objection] → [how product addresses it]
```

---

### TASK D — Feature Validation

```
RESEARCH TASK: MVP Feature Set Validation

Product: [FILL IN]
Proposed MVP features:
1. [feature]
2. [feature]
3. [feature]

Research needed:
1. Are these the right 3-5 features for MVP? What evidence supports/contradicts each?
2. Which feature is most critical to delivering first value?
3. Is anything missing that would make users not adopt the product?
4. What can safely be cut to v2 without losing core value?
5. What's the minimum viable version of each feature? (not full feature — what's the smallest useful slice)

Return format:
## Feature Assessment
| Feature | Keep/Cut/Shrink | Reason | Minimum viable slice |
|---------|----------------|--------|---------------------|

## Recommended MVP (re-ordered by build priority)
1. [highest priority]
2. [second]
3. [third]

## Cut to v2
- [feature] — [why it can wait]
```

---

### TASK E — Integration Research

```
RESEARCH TASK: External Service Selection

Product: [FILL IN]
Integrations needed: [FILL IN — e.g. "payments, email, auth, AI/LLM"]

For each integration, research:
1. What are the top 2-3 options?
2. What's the pricing model? Free tier limits?
3. How good is the developer experience? (SDK quality, docs, community)
4. Any known gotchas or outages?
5. What's the recommended choice for an MVP with [team/budget context]?

Return format:
## Integration Decisions
| Integration | Recommended | Why | Free tier | Env var name |
|-------------|-------------|-----|-----------|-------------|
| Payments | | | | |
| Email | | | | |
| Auth | | | | |
| AI/LLM | | | | |

## Env vars to add to .env.example
[list all var names]
```

---

### TASK F — AI / LLM Architecture Research

```
RESEARCH TASK: LLM Product Architecture

Product: [FILL IN — what the AI does in the product]
AI task type: [FILL IN — e.g. "classify user input", "generate structured output", "multi-step reasoning agent", "RAG over documents"]
Latency requirement: [FILL IN — e.g. "real-time <2s", "async batch OK"]
Volume: [FILL IN — e.g. "100 calls/day MVP", "high volume production"]

Research needed:
1. Which LLM / model family fits this task? (GPT-4o, Claude 3.5, Gemini, Mistral, local?)
2. What prompt pattern works best? (zero-shot, few-shot, CoT, structured output, tool use?)
3. If RAG — what's the right chunking strategy and vector DB for this use case?
4. How should the system prompt be structured for this task type?
5. What evals should be set up to measure quality?

Return format:
## LLM Architecture Decision
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Model | | |
| Prompt pattern | | |
| Context window needed | | |
| Vector DB (if RAG) | | |
| Embedding model (if RAG) | | |

## System Prompt Structure
[Recommended role + context + constraints + output format]

## Eval Dimensions
| Dimension | How to measure | Pass threshold |
|-----------|---------------|---------------|
```

---

## How to Return Research

Paste your findings at the end of this doc and return the whole thing to the Documentation Builder session. It will be fed directly into the Research Gate — no reformatting needed.

**Label your findings clearly:**
```
## RESEARCH FINDINGS — [Task letter + title]
Date: [today]
Source: [which chats / searches were used]

[your findings in the return format above]
```

---

*Documentation Builder v1.7 · April 2026*
