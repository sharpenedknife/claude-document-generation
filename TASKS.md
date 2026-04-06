# TASKS.md — Documentation Builder Improvement Backlog
**Created:** 2026-04-04
**Scope:** All improvements, fixes, and new work identified via full project audit.
**How to use:** Pick a task, mark it `[x]` when done, update SYSTEM_DEBT.md if relevant.

---

## STATUS KEY
- `[ ]` Not started
- `[~]` In progress
- `[x]` Done
- `[!]` Blocked

---

## P0 — CRITICAL: Research-First Workflow

**Problem:** The system currently collects Q0–Q8 and generates immediately. This produces docs for half-baked ideas with unvalidated assumptions. The fix: force a research/data-collection gate between Q0 and Q1 for every build type, so users come back with real data instead of speculation.

### T-01 — Add Research Gate to Product Builder
**File:** `builders/product/BUILDER_Questions.md`
**Where:** After Q0 Gate, before Q1.

Insert this section:

```
## RESEARCH GATE (mandatory after Q0, before Q1)

After Q0 is answered, STOP. Do not proceed to Q1.

Tell the user:

> "Good — I have the overview. Before I generate your docs, I need you to go collect
> real data. Docs built on guesses produce broken dev plans.
>
> Go do this and come back:
>
> **1. Lock your MVP features (Q2 input)**
>    - Write out each feature in 1 sentence. Max 5.
>    - If you haven't decided yet — decide now. Don't generate with 'TBD'.
>
> **2. Map your core user flow (Q3 input)**
>    - Describe what your primary user does from login to first value, step by step.
>    - Minimum: 5 steps with real screen names or actions.
>
> **3. List your data objects (Q4 input)**
>    - What 'things' does the product store? Name them: User, Project, Task, etc.
>    - Include the key relationships (User has many Projects, etc.)
>
> **4. Lock your tech stack (Q5 input)**
>    - Decide: frontend, backend, database, auth, deployment.
>    - If unsure, say who is on the team and I'll recommend specifically.
>
> **5. List external services (Q6 input)**
>    - Any payment, email, auth, AI, or notification services you'll integrate?
>
> Come back with these 5 answers and I'll generate a complete, agent-ready doc bundle."

Do not ask Q1–Q8 until the user returns with this data.
If the user pushes back and wants to proceed anyway — warn them:
> "I can generate with assumptions, but I'll mark every unconfirmed item as ASSUMED.
> Any ASSUMED item in the docs is a point where the AI coding agent will have to guess.
> Do you want to proceed with assumptions, or take 10 minutes to lock these down?"

If they explicitly confirm they want to proceed with assumptions → proceed, mark everything ASSUMED.
```

---

### T-02 — Add Research Gate to Claude Project Builder
**File:** `builders/claude-project/BUILDER_Questions.md`
**Where:** After Q0, before Q1.

Research gate content:
```
> "Before I design your Claude Project, go answer these:
>
> 1. What does the person using this assistant do manually today that's slow/painful?
>    (Write out the exact steps — this becomes the knowledge base structure.)
>
> 2. What files, docs, or reference material does Claude need to know?
>    (List them by name — these become knowledge base uploads.)
>
> 3. What are 3 real example requests users will send?
>    (These become the project instruction examples and test cases.)
>
> 4. What should Claude NEVER do in this project?
>    (Constraints drive the instruction quality more than capabilities.)
>
> Come back with these 4 answers."
```

---

### T-03 — Add Research Gate to Skill Builder
**File:** `builders/skill/BUILDER_Questions.md`
**Where:** After Q0, before Q1.

Research gate content:
```
> "Before I write your SKILL.md, do this:
>
> 1. Do the task manually once right now. Write out every step you took.
>    (The skill body is a playbook — it must match what actually works, not what you think works.)
>
> 2. Write 5 different ways a user might ask for this skill to be used.
>    (These become the trigger description — the most important field in SKILL.md.)
>
> 3. What does a bad output look like? Name one failure mode.
>    (This becomes the Error Handling section.)
>
> Come back with these 3 things."
```

---

### T-04 — Add Research Gate to MCP Builder
**File:** `builders/mcp/BUILDER_Questions.md`
**Where:** After Q0, before Q1.

Research gate content:
```
> "Before I document your MCP server, get this:
>
> 1. The API docs or endpoint list for the service you're connecting to.
>    (Paste the URL or the relevant endpoints — I cannot invent API shapes.)
>
> 2. The auth method: API key, OAuth2, Bearer token? Where does the token go?
>    (Auth docs or header format required before I can write the auth guide.)
>
> 3. List the 3–5 specific operations your MCP needs to support.
>    (Example: 'create task', 'list projects', 'update status' — not 'manage tasks'.)
>
> Come back with this data."
```

---

## P1 — HIGH: Token Optimization — Lazy Skill Loading

**Problem:** The current SKILL_MAP and project instructions don't explicitly enforce lazy loading. The risk is that a session reads multiple SKILL.md files upfront or loads SKILL_MAP before it's needed, consuming tokens on skills that won't be used in that run.

**Principle:** Read ONE skill at a time, ONLY when at that generation stage. Never preload.

### T-05 — Add Lazy Loading Rules to SKILL_MAP.md
**File:** `skills/SKILL_MAP.md`
**Where:** Add as a new top section before "How Skills Are Called".

Add:
```markdown
## Token Budget Rules — Read Before Using This Map

1. **Read SKILL_MAP.md ONCE per session** — at Step 3 (generation plan), not before.
   Do not re-read it at each stage. Keep it in context after the first read.

2. **Read each SKILL.md ONLY at its stage** — do not preload skills.
   At Stage 1 (PRD): read writing-prds/SKILL.md. At Stage 5: read architecture-designer/SKILL.md.
   Never read Stage 5 skills during Stage 1.

3. **Read at most 2 SKILL.md files per generation stage.**
   If a stage calls a primary skill + a secondary skill, read both. Stop there.
   Stack-specific skill = one of the two allowed reads.

4. **Stack skills: read ONE that matches Q5.**
   The stack table has 31 entries. Read only the one that matches the user's stack.
   Never scan the stack table and read multiple to compare.

5. **Skip skills for stages you're not generating.**
   If the user only wants a PRD, do not read architecture-designer/SKILL.md.
   Load skills on demand for the docs being generated, nothing more.
```

---

### T-06 — Add Lazy Loading Instruction to Project Instructions
**File:** `system/templates/project_instructions/PROJECT_INSTRUCTIONS_Docgen_Production.md`
**Where:** After "How to Use Project Context" section.

Add:
```
## Skill Loading — Token Conservation Rule

NEVER load skills upfront. Load each skill ONLY when you reach that generation stage.

- SKILL_MAP.md: read once, at Step 3 (generation plan), never before.
- Each SKILL.md: read at the start of that specific generation stage.
- Stack skills: read ONE (the one that matches Q5). Skip the rest.
- If only generating 1–2 docs: only read the skills for those docs.

This prevents wasting context window on skills that won't be used in this session.
```

---

### T-07 — Add Stage-Gated Skill Call Pattern to CLAUDE.md
**File:** `CLAUDE.md` (project root)
**Where:** Add a note in the Skills section or Rules section.

Add to Rule 2 (or add a Rule 10):
```
10. **Load skills on demand, not upfront.** Read SKILL_MAP.md once at Step 3.
    Read each SKILL.md only when at that stage. Never preload. Max 2 skills active per stage.
```

---

## P2 — HIGH: Missing Example Library

**Problem:** `output/examples/` has only 1 example (mhub skill). Logged as DEBT item 2.1. The system needs at least 1 working example per doc type so the exit gates can be tested and users can see what "good" looks like.

### T-08 — Create Example PRD
**File:** `output/examples/example-product/PRD_ExampleProduct_v1.0_2026-04-04.md`
Use a simple product (e.g., a task manager) that covers all PRD required sections.
Must score 85+/100 against exit gates. Mark every section with ✓ to show gate compliance.

### T-09 — Create Example Architecture Doc
**File:** `output/examples/example-product/ARCH_System_ExampleProduct_v1.0_2026-04-04.md`
Cover: tech stack decision record, file/folder structure, component diagram (text), key flows.
Use Next.js + PostgreSQL stack (most common recommendation).

### T-10 — Create Example Dev Plan
**File:** `output/examples/example-product/DEV_Plan_ExampleProduct_v1.0_2026-04-04.md`
Must follow DEV_PLAN_TEMPLATE.md exactly. Show Phase 0 (setup) through Phase 3 (MVP launch).
Every task must include: file path + acceptance criterion + dependency.

### T-11 — Create Example Starter Prompt
**File:** `output/examples/example-product/STARTER_PROMPT_ExampleProduct.md`
Must be self-contained: works when pasted into a fresh session with no prior context.
Test: read only this file — can an AI start Phase 0 without any other doc?

### T-12 — Create Example Claude Project Output
**File:** `output/examples/example-claude-project/CLAUDE.md`
Use Documentation Builder itself as the example (already built). Show a condensed version.

---

## P3 — MEDIUM: Workflow Polish

### T-13 — Add Context Tier Warning to All Builders
**Files:** All 6 `BUILDER_Questions.md` files
**Problem:** Tier 1/2/3 context system is described in project instructions but not enforced in builder files.

In each builder, before "Context Confirmation", add:

```
## Context Assessment (before confirming plan)

Assess intake completeness:
- **Tier 1 (minimal — proceed with caution):** User answered Q0 only, or gave < 3 sentences total.
  → WARN: "I have minimal context. I'll be making significant assumptions. Want to add more before I generate?"
- **Tier 2 (solid):** Q0–Q5 answered with specific (non-vague) content.
  → NOTE remaining defaults. Confirm and proceed.
- **Tier 3 (full):** All Q0–Q8 answered with concrete, specific details.
  → Best output. Confirm and proceed.
```

---

### T-14 — Fix SKILL_MAP Precedence Orphan
**File:** `skills/SKILL_MAP.md`
**Problem:** Last line says "This file takes precedence over the SKILL MAP in REFERENCE_Builders.md" — but REFERENCE_Builders.md is a knowledge base file, not a project file. The precedence claim is confusing.

**Fix:** Change the footer to:
```
*In Cowork mode: this file is the authoritative skill routing table.
The SKILL MAP in the Claude.ai knowledge base applies only in Claude.ai Chat sessions.*
```

---

### T-15 — Fix Version Inconsistency
**Files:** `CLAUDE.md` line 140, `config/token_budgets.json` line 3, `config/domain_definitions.json` line 2
**Problem:** CLAUDE.md says v1.5, config files say v1.1.

Decide: if system is v1.5, update configs. If configs are right at v1.1, update CLAUDE.md.
Document the decision in metrics/LOG_Generation.md.

---

### T-16 — Add "Clarify Build Type" Step for Ambiguous Requests
**File:** `system/guides/SYSTEM_Build_Decision_Framework.md` + project instructions
**Problem:** Users often describe something that could be Type 1, 2, or 3. The current Q0 doesn't explicitly route them.

Add a disambiguation question pattern:
```
If Q0 response is ambiguous (could be product OR Claude Project), ask:
> "Quick check — are you building:
>    A) Software that runs for your users (app, SaaS, tool) → I'll generate code docs
>    B) A Claude assistant for yourself or your team → I'll generate project instructions
>    C) A reusable workflow/command → I'll build a Skill
>    D) A connection to an external tool → I'll document an MCP server"
```

---

## P4 — MEDIUM: DEBT.md Updates

### T-17 — Log Research Gate to DEBT.md
**File:** `backlog/SYSTEM_DEBT.md`
Add item for "Research Gate implementation" status once T-01 through T-04 are complete.
Mark Decision 2 (Manual Questionnaires) update: research gates are now part of questionnaire design.

### T-18 — Log Token Lazy-Loading to DEBT.md
Once T-05 through T-07 are done, add to DEBT.md:
"Token lazy-loading pattern documented in SKILL_MAP.md, project instructions, and CLAUDE.md. Monitoring needed to confirm average tokens/session stays under budget."

### T-19 — Log Verification 1 (Token Budgets Realistic)
After 5 real sessions: measure actual tokens used per stage vs. budget in `config/token_budgets.json`.
Update the budget file if values are wrong.

---

## P5 — LOW: Housekeeping

### T-20 — Populate metrics/LOG_Generation.md
**File:** `metrics/LOG_Generation.md`
After each real doc generation session, log it. Format:
`| 2026-04-04 | product | ExampleProduct | PRD | 85/100 | Pass | All 5 gates |`

### T-21 — Add ui-ux-pro-max Workaround to Builder Rules
**File:** `builders/product/BUILDER_Rules.md`
Document the Stage 3 (UI) fallback since `ui-ux-pro-max` and `ui-styling` are missing:
"At UI generation: use standard UX component patterns + read the stack's framework skill for component naming."

### T-22 — Add ai-docs and code Builder Research Gates
**Files:** `builders/ai-docs/BUILDER_Questions.md`, `builders/code/BUILDER_Questions.md`
Apply same research-gate pattern as T-01 through T-04 — adapted for those builder types.

---

## P6 — HIGH: Token-Efficient Generation

**Problem:** `SYSTEM_Token_Optimization.md` defines measurement budgets and post-hoc checks, but gives no behavioral rules for *during* generation. The product bundle has no per-doc token budgets for its specific doc types (PRD, UX, UI, Vision, Dev Plan, Starter Prompt). Result: docs grow to fill available space rather than being written lean by design.

**Goal:** High-quality docs at minimum token cost. Every word must earn its place.

### T-23 — Add Product Bundle Doc Types to token_budgets.json
**File:** `config/token_budgets.json`
**What:** Add budget entries for: `prd`, `ux-research`, `ui-spec`, `product-vision`, `data-schema`, `dev-plan`, `starter-prompt`. Also add a `bundle-total` field capping the full 11-doc product bundle.
**Target budgets:** PRD 2500, UX 1800, UI 1800, Vision 1000, Data Schema 2000, Dev Plan 3500, Starter Prompt 800. Bundle total: 22000 tokens.

### T-24 — Add Generation-Time Behavioral Rules to SYSTEM_Token_Optimization.md
**File:** `system/guides/SYSTEM_Token_Optimization.md`
**What:** New section "Generation Behavioral Rules" with anti-patterns and constraints that apply *while writing* docs, not just when reviewing them. Key rules:
- BLUF: conclusion first, explanation second
- Tables over paragraphs for any structured comparison
- Never restate context from another doc in the bundle — reference by filename
- Section body max 120 words; expand only if acceptance criteria require
- Decision records: 3 lines max each (CONFIRMED/ASSUMED status + rationale)
- Code blocks: minimal but runnable; no defensive boilerplate unless it's the point
- Acceptance criteria: GIVEN/WHEN/THEN only, 1 sentence each, no prose explanation

### T-25 — Add Token Constraint Header to DOC_CANONICAL_TEMPLATE.md
**File:** `system/templates/output/DOC_CANONICAL_TEMPLATE.md`
**What:** Add a CONSTRAINTS block at the top (before any content sections) that every generated doc must fill in: token budget, doc type, hard limits. This makes the constraint visible to both the generator and the reviewer.

### T-26 — Add "Write Lean" Pre-Generation Checklist to SKILL_MAP.md
**File:** `skills/SKILL_MAP.md`
**What:** Before Stage 1, add a token constraint reminder that applies to all stages. Short rules for the generator to internalize before writing the first word.

---

## DONE

| Task | Completed | Notes |
|------|-----------|-------|
| Copy 42→56 SKILL.md files to `skills/` | 2026-04-04/06 | All SKILL MAP skills + prompt-building skills copied |
| Create `skills/SKILL_MAP.md` | 2026-04-04 | Cowork-native routing, replaces knowledge base version |
| T-01 Research Gate — Product Builder | 2026-04-04 | `builders/product/BUILDER_Questions.md` |
| T-02 Research Gate — Claude Project Builder | 2026-04-04 | `builders/claude-project/BUILDER_Questions.md` |
| T-03 Research Gate — Skill Builder | 2026-04-04 | `builders/skill/BUILDER_Questions.md` |
| T-04 Research Gate — MCP Builder | 2026-04-04 | `builders/mcp/BUILDER_Questions.md` |
| T-05 Lazy loading rules — SKILL_MAP.md | 2026-04-04 | Token Budget Rules section added |
| T-06 Lazy loading — Project Instructions | 2026-04-04 | Skill Loading section added |
| T-07 Lazy loading — CLAUDE.md Rule 10 | 2026-04-04 | Rule 10 added |
| T-13 Context Tier Assessment — all 6 builders | 2026-04-04 | Tier 1/2/3 warning in every BUILDER_Questions.md |
| T-14 SKILL_MAP footer fix | 2026-04-04 | "Cowork mode authoritative" footer |
| T-15 Version sync → v1.5 | 2026-04-04 | CLAUDE.md + config files aligned |
| T-16 Disambiguation script — Build Decision Framework | 2026-04-04 | A/B/C/D question added |
| T-17 Research Gate logged in DEBT.md | 2026-04-04 | Changelog updated |
| T-18 Lazy loading logged in DEBT.md | 2026-04-04 | Changelog updated |
| T-21 ui-ux-pro-max workaround | 2026-04-04 | Stage 3 workaround in product BUILDER_Rules.md |
| T-22 ai-docs + code research gates | 2026-04-05 | Both builders updated |
| Wire prompt-building skills → SKILL_MAP, BUILDER_Rules | 2026-04-06 | Stages 5 + 11; AI-native Rule 11 |
| ChatGPT port v1.6 | 2026-04-06 | AGENTS.md, CHATGPT_CUSTOM_INSTRUCTIONS, chatgpt-project builder |
| Zip `Documentation_Builder_v1.6_2026-04-06.zip` | 2026-04-06 | Full Claude version |
| Zip `DocumentationBuilder_ChatGPT_Port_v1.6_2026-04-06.zip` | 2026-04-06 | ChatGPT/Codex version |

---

## SUMMARY

| Priority | Count | Status |
|----------|-------|--------|
| P0 — Critical (Research gates) | 4 tasks | ✅ All done |
| P1 — High (Lazy loading) | 3 tasks | ✅ All done |
| P2 — High (Example library) | 5 tasks | ⏭ Skipped per user |
| P3 — Medium (Workflow polish) | 4 tasks | ✅ All done |
| P4 — Medium (DEBT updates) | 3 tasks | 🔄 T-19, T-20 pending |
| P5 — Low (Housekeeping) | 3 tasks | 🔄 T-20 pending |
| P6 — High (Token optimization) | 4 tasks | 🔄 T-23–T-26 new |
| **Total** | **26 tasks** | |
