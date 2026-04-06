# Skill Map — AI Routing Table for Doc Generation
**What this is:** Operational instructions for Docgen in Cowork mode. At each generation stage this map tells you exactly how to apply the skill.
**When to read:** Step 3 of Interactive Operating Mode (before showing the plan). Re-read at each generation stage (Step 4).
**Last updated:** April 2026

## Write Lean — Pre-Generation Rules (Apply to Every Stage)

Read these before writing any doc. They override any verbose instinct.

| Rule | Do | Don't |
|------|----|-------|
| BLUF | Lead every section with the conclusion | Warm up to the point |
| Structure | Use tables for all structured data | Explain tables in prose |
| Scope | Reference other docs by filename | Repeat their content |
| Length | Stop when content is complete | Fill to the budget ceiling |
| Criteria | GIVEN/WHEN/THEN, one line each | Prose acceptance criteria |
| Code | Minimal runnable example | Full boilerplate with logging |
| Sections | ≤ 120 words per prose body | Multi-paragraph explanations |

**Bundle rule:** Track running token total against 22,000-token bundle cap. If nearing 22K, cut Vision doc first, then UX — never cut Dev Plan or Architecture.

**Check before moving to next stage:** estimated tokens so far ÷ stages remaining ≤ remaining budget ÷ remaining stages.

---

## Token Budget Rules — Read Before Using This Map

1. **Read SKILL_MAP.md ONCE per session** — at Step 3 (generation plan), not before. Do not re-read at each stage. Keep it in context after the first read.

2. **Read each SKILL.md ONLY at its stage** — do not preload skills. At Stage 1 (PRD): read `skills/writing-prds/SKILL.md`. At Stage 5: read `skills/architecture-designer/SKILL.md`. Never read Stage 5 skills during Stage 1.

3. **Read at most 2 SKILL.md files per generation stage.** If a stage calls a primary skill + secondary skill, read both. Stop there. The stack-specific skill counts as one of the two allowed reads.

4. **Stack skills: read ONE that matches Q5.** The stack table has 31 entries. Read only the one matching the user's stack. Never scan multiple stack skills to compare.

5. **Skip skills for stages you're not generating.** If the user only wants a PRD, do not read `architecture-designer/SKILL.md`. Load skills on demand for the docs being generated, nothing more.

---

## How Skills Are Called in Cowork

Two modes — use the right one per stage:

| Mode | When | How |
|------|------|-----|
| **Skill tool** | Skill is installed and callable | `Skill tool: skill-name` |
| **Read + apply** | Skill SKILL.md is in `skills/` folder | `Read: skills/{name}/SKILL.md` → follow its instructions as the generation playbook |

**Rule:** Skill output = raw draft. Always format via DOC_CANONICAL_TEMPLATE and run all 5 quality gates after.

---

## Product Builder (Type 1) — Generation Order

### Stage 1: PRD
**Read:** `skills/writing-prds/SKILL.md` → apply as generation playbook
**Input:** Q0 context, Q1 one-liner, Q2 MVP features, Q3 user flows

### Stage 2: UX Research
**Read:** `skills/user-research/SKILL.md` → apply if user hasn't validated flows
**Skill tool:** `conducting-user-interviews` (if conducting live research sessions)
**Input:** PRD output + Q3 user types and flows

### Stage 3: UI Design
**No local skill for ui-ux-pro-max or ui-styling.** Apply expertise directly:
- Use standard UX component patterns, accessibility principles, flow diagrams
- If React/Next.js stack: apply shadcn/ui + Tailwind component naming conventions
- Read `skills/nextjs-developer/SKILL.md` (or relevant stack skill) for component structure
**Input:** UX output + Q3 flows

### Stage 4: Vision
**Skill tool:** `defining-product-vision`
**Input:** Q0–Q3 context
**Fallback:** Generate from DOC_CANONICAL_TEMPLATE directly — no skill required

### Stage 5: Architecture
**Read:** `skills/architecture-designer/SKILL.md` → apply as generation playbook
**Also read:** `skills/api-designer/SKILL.md` → apply for API layer decisions
**Stack-specific (mandatory):** Read the framework skill from the Stack Table below
**AI-native stack (LLM product, agent, RAG, chatbot):** Additionally call:
- `Skill tool: prompt-building:prompt-engineering-patterns` → apply for prompt architecture, system prompt design, and token efficiency decisions
- `Skill tool: prompt-building:langchain-architecture` → apply for chain design, agent patterns, and memory architecture
**Input:** PRD + Data entities (Q4) + Tech stack (Q5) + Integrations (Q6)

### Stage 6: Data Schema
**Read:** `skills/postgres-pro/SKILL.md` (PostgreSQL) or `skills/sql-pro/SKILL.md` (other SQL)
**If GraphQL:** Read `skills/graphql-architect/SKILL.md` instead
**Input:** Architecture output + Q4 data entities + user flows from UX

### Stage 7: API Spec
**Read:** `skills/api-designer/SKILL.md` → apply as generation playbook
**If GraphQL:** Read `skills/graphql-architect/SKILL.md` instead
**Input:** Architecture output + Data Schema + PRD features

### Stage 8: Environment Setup
**Read:** `skills/devops-engineer/SKILL.md` (Docker/CI/CD) or `skills/cloud-architect/SKILL.md` (cloud)
**Stack-specific:** Also read framework skill for setup commands and config
**Input:** Architecture + Tech stack + Integrations (Q6)

### Stage 9: Dev Plan
**Read:** `skills/feature-forge/SKILL.md` → apply for requirements → task breakdown
**Also read:** Stack-specific framework skill → validate phase tasks and file paths
**Input:** ALL previous docs (PRD through Setup)

### Stage 10: CLAUDE.md
**No skill.** Generate from DOC_CANONICAL_TEMPLATE — this is Docgen's core output.

### Stage 11: Starter Prompt
**Read:** `skills/vibe-coding/SKILL.md` → apply for AI coding best practices
**Also read:** `skills/prompt-engineer/SKILL.md` → apply to optimize the prompt
**AI-native stack:** Additionally call `Skill tool: prompt-building:prompt-engineering-patterns` → apply chain-of-thought, few-shot, and structured output patterns to the starter prompt itself
**Input:** Dev Plan + CLAUDE.md + tool choice (Q7)

---

## Claude Project Builder (Type 2) — Generation Order

### Project Instructions
**Read:** `skills/prompt-engineer/SKILL.md` → apply for writing effective project instructions
**Always call:** `Skill tool: prompt-building:prompt-engineering-patterns` → apply for role-based system prompt design, structured output format, and progressive disclosure patterns
**Input:** Q0 context, purpose, target users

### Knowledge Base Structure
**Read:** `skills/rag-architect/SKILL.md` (if project needs retrieval over large docs)
**Input:** What knowledge the project needs access to

### Custom Skills (if project needs them)
**Skill tool:** `skill-creator` — always, no exceptions
**Input:** Identified workflow patterns from intake

### MCP Integrations (if project needs live tools)
**Read:** `skills/mcp-developer/SKILL.md` → apply for implementation details
**Input:** Q6 integrations list

### Starter Prompt
**Read:** `skills/prompt-engineer/SKILL.md` + `skills/vibe-coding/SKILL.md`

---

## Skill Builder (Type 3) — Generation Order

### SKILL.md
**Skill tool:** `skill-creator` — always, no exceptions
**Input:** All intake answers (Q0–Q8)
**This skill handles the entire lifecycle:** create, structure, validate

### evals.json
**Skill tool:** `ai-evals`
**Input:** SKILL.md output + expected behaviors

---

## MCP Server Builder (Type 4) — Generation Order

### Setup Guide + API Reference
**Read:** `skills/mcp-developer/SKILL.md` — always, no exceptions
**Also read:** `skills/api-designer/SKILL.md` for tool schema design
**Input:** All intake answers

### Auth Guide
Follow auth patterns in `skills/mcp-developer/SKILL.md`

### Testing
**Skill tool:** `ai-evals` for eval design

---

## Stack-Specific Skill Table (Mandatory at Stages 5, 8, 9, 11)

When the user answers Q5 (tech stack), look up the skill below. Read the SKILL.md and apply it during Architecture, Setup, Dev Plan, and Starter Prompt generation.

| Stack component | Read this file |
|----------------|----------------|
| Next.js | `skills/nextjs-developer/SKILL.md` |
| React | `skills/react-expert/SKILL.md` |
| Vue 3 | `skills/vue-expert/SKILL.md` |
| Angular | `skills/angular-architect/SKILL.md` |
| React Native / Expo | `skills/react-native-expert/SKILL.md` |
| Flutter | `skills/flutter-expert/SKILL.md` |
| Swift / iOS | `skills/swift-expert/SKILL.md` |
| NestJS | `skills/nestjs-expert/SKILL.md` |
| Express / Node.js | `skills/javascript-pro/SKILL.md` |
| FastAPI | `skills/fastapi-expert/SKILL.md` |
| Django | `skills/django-expert/SKILL.md` |
| Rails | `skills/rails-expert/SKILL.md` |
| Laravel | `skills/laravel-specialist/SKILL.md` |
| Spring Boot | `skills/spring-boot-engineer/SKILL.md` |
| .NET / ASP.NET Core | `skills/dotnet-core-expert/SKILL.md` |
| Go | `skills/golang-pro/SKILL.md` |
| Rust | `skills/rust-engineer/SKILL.md` |
| PHP | `skills/php-pro/SKILL.md` |
| Python | `skills/python-pro/SKILL.md` |
| TypeScript | `skills/typescript-pro/SKILL.md` |
| PostgreSQL | `skills/postgres-pro/SKILL.md` |
| SQL (general) | `skills/sql-pro/SKILL.md` |
| GraphQL | `skills/graphql-architect/SKILL.md` |
| WebSockets | `skills/websocket-engineer/SKILL.md` |
| Kubernetes | `skills/kubernetes-specialist/SKILL.md` |
| Terraform / IaC | `skills/terraform-engineer/SKILL.md` |
| Docker / CI/CD | `skills/devops-engineer/SKILL.md` |
| Playwright / E2E | `skills/playwright-expert/SKILL.md` |
| WordPress | `skills/wordpress-pro/SKILL.md` |
| Shopify | `skills/shopify-expert/SKILL.md` |
| Salesforce | `skills/salesforce-developer/SKILL.md` |

---

## Missing Skills (not found locally)

These skills were referenced in the original SKILL MAP but are not available locally. Apply domain expertise directly when these stages are reached:

| Missing skill | Stage | Apply instead |
|--------------|-------|---------------|
| `ui-ux-pro-max` | UI Design (Stage 3) | Standard UX patterns + stack component library conventions |
| `ui-styling` | UI Design React/Next.js | Read `skills/nextjs-developer/SKILL.md` for component structure |

---

## Skill Tool Reference (Callable in Cowork)

These skills are installed and callable directly via the Skill tool:

| Task | Skill tool name |
|------|----------------|
| Define product vision | `defining-product-vision` |
| User interviews / research | `conducting-user-interviews` |
| Build a new skill | `skill-creator` |
| Evaluate LLM outputs | `ai-evals` |
| Build with LLMs | `building-with-llms` |
| Competitive analysis | `competitive-analysis` |
| Customer research | `customer-research` |
| Co-author documentation | `doc-coauthoring` |
| Evaluate tech options | `evaluating-new-technology` |
| **Write / optimize any prompt or system instruction** | `prompt-building:prompt-engineering-patterns` |
| **Score / evaluate prompt output quality** | `prompt-building:llm-evaluation` |
| **Build multi-step prompt chains or agent loops** | `prompt-building:langchain-architecture` |
| **Semantic few-shot example retrieval** | `prompt-building:similarity-search-patterns` |

---

---

## Research Hub Skills (load for research-type builds)

| Stage | Read this file |
|-------|---------------|
| Document / RAG research | `skills/rag-implementation/SKILL.md` |
| Search across large corpus | `skills/hybrid-search-implementation/SKILL.md` |
| Embedding / chunking decisions | `skills/embedding-strategies/SKILL.md` |
| Competitive research | `skills/competitive-landscape/SKILL.md` |
| Market sizing | `skills/market-sizing-analysis/SKILL.md` |
| Presenting findings | `skills/data-storytelling/SKILL.md` |
| Cross-session context | `skills/context-driven-development/SKILL.md` |
| Multi-agent research team (Cowork) | `skills/team-composition-patterns/SKILL.md` |
| Parallel task planning (Cowork) | `skills/task-coordination-strategies/SKILL.md` |

## Prompt Building Skills (load when writing or evaluating prompts)

| Task | Read this file |
|------|---------------|
| Write / optimize any prompt | `skills/prompt-engineering-patterns/SKILL.md` |
| Score / evaluate prompt output | `skills/llm-evaluation/SKILL.md` |
| Build multi-step prompt chains | `skills/langchain-architecture/SKILL.md` |
| Semantic few-shot example retrieval | `skills/similarity-search-patterns/SKILL.md` |

---

*In Cowork mode: this file is the authoritative skill routing table. The SKILL MAP in the Claude.ai knowledge base applies only in Claude.ai Chat sessions.*
