# Documentation Builder — Templates Reference
> Consolidated reference: all templates, checklists, examples, and config.
> For individual source files: https://github.com/sharpenedknife/claude-document-generation

========================================================================
OUTPUT TEMPLATES
========================================================================

### DEBT Specification

# DEBT.md Specification

Every document MUST have an accompanying DEBT.md file listing known limitations, backlog features, and future improvements.

DEBT.md is NOT for users. It's for the docgen team tracking what's incomplete.

---

## File Naming

```
{DocName}.md          # Main document
{DocName}.DEBT.md     # Companion debt file
```

**Examples:**
```
GTM_Strategy_2026Q1.md
GTM_Strategy_2026Q1.DEBT.md

API_Reference_v1.md
API_Reference_v1.DEBT.md
```

---

## Frontmatter

```yaml
---
for_document: "{DocName}.md"
generated_at: YYYY-MM-DDTHH:MM:SSZ
total_items: N
critical_items: N (P0)
high_priority_items: N (P1)
medium_priority_items: N (P2)
low_priority_items: N (P3)
---
```

---

## Structure

```markdown
# Technical Debt: {DocName}

For document: [{DocName}]({path_to_doc}.md)

---

## Overview

Brief explanation of why this document has debt:
- What's complete now
- What's deferred
- What was cut for token budget
- Known gaps or limitations

---

## Priority 0: Critical (Blocks Production)

**Status:** None (document wouldn't ship if any P0 items exist)

---

## Priority 1: High (Should Address Soon)

### Item 1.1: [Title]
- **Type:** [missing_section|incomplete|unclear|needs_verification|needs_examples]
- **Impact:** [What breaks without this]
- **Effort:** [1-3 hours|4-8 hours|1-3 days|> 1 week]
- **Owner:** [Who should fix]
- **Details:** [Why it's incomplete, what's needed]

Example:
```markdown
### Item 1.1: Add Competitive Analysis Table
- **Type:** missing_section
- **Impact:** GTM strategy incomplete without knowing competitive landscape
- **Effort:** 4-8 hours
- **Owner:** Product team
- **Details:** Need to research 5 main competitors (Slack, Microsoft Teams, Google Chat)
  and create comparison table. Should include: feature matrix, pricing, target market.
```

---

## Priority 2: Medium (Nice to Have)

### Item 2.1: [Title]
- **Type:** [enhancement|optimization|clarification|additional_example]
- **Impact:** [Helpful but not blocking]
- **Effort:** [estimate]
- **Owner:** [suggestion]
- **Details:** [Description]

Example:
```markdown
### Item 2.1: Add Pricing Tier Breakdown
- **Type:** enhancement
- **Impact:** Users can't estimate costs without pricing details
- **Effort:** 2-3 hours
- **Owner:** Sales/Finance team
- **Details:** Add table breaking down: basic/pro/enterprise pricing
  and what's included in each tier. Include annual discount rates.
```

---

## Priority 3: Low (Future Backlog)

### Item 3.1: [Title]
- **Type:** [nice_to_have|future_feature|research|depends_on_something]
- **Impact:** [Would be nice, not essential]
- **Effort:** [estimate]
- **Owner:** [suggestion]
- **Details:** [Description]

Example:
```markdown
### Item 3.1: Add Case Studies
- **Type:** future_feature
- **Impact:** Would strengthen credibility, not needed for MVP
- **Effort:** 3-5 days
- **Owner:** Marketing
- **Details:** Research and write 2-3 case studies showing GTM success stories
  from our customers. Depends on customer approval + interview time.

### Item 3.2: Add Video Walkthrough
- **Type:** future_feature
- **Impact:** Video format would help some learners, doc is readable without
- **Effort:** 1-2 days
- **Owner:** Content team
- **Details:** Record 15-20 minute walkthrough of GTM strategy execution.
  Needs: scripting, recording, editing.
```

---

## Known Limitations

```markdown
## Known Limitations

### Limitation 1: [What's Limited]
- **Scope:** [What won't work]
- **Reason:** [Why it's limited]
- **Workaround:** [How users should work around it, if any]

Example:
### Limitation 1: Does Not Cover Enterprise Sales
- **Scope:** GTM strategy assumes mid-market (50-500 employees), not enterprise (1000+)
- **Reason:** Enterprise GTM requires 2x longer sales cycle, different decision trees
- **Workaround:** See: [link to separate enterprise GTM doc]

### Limitation 2: Data as of Q1 2026
- **Scope:** Market analysis, competitor pricing, market size estimates
- **Reason:** Markets change quarterly, this doc was current Feb-Mar 2026
- **Workaround:** Check quarterly updates in [link to update schedule]
```

---

## Skills to Create (If Applicable)

```markdown
## Suggested Skills

If patterns emerge, suggest creating reusable skills:

### Skill 1: [Skill Name]
- **Type:** repeatable_process
- **Usage:** When user needs to [what problem does skill solve]
- **Scope:** [What the skill would cover]
- **Status:** [suggested|in_progress|published]
- **Owner:** [Who should build]

Example:
### Skill 1: Market Analysis Framework
- **Type:** repeatable_process
- **Usage:** When creating GTM strategy for any new market segment
- **Scope:** Step-by-step process for analyzing market size, growth, competition, buyer personas
- **Status:** suggested
- **Owner:** Product/Research team
```

---

## Content Decisions

```markdown
## Content Decisions

Document why certain content was cut, deferred, or simplified:

### Decision 1: [What Was Cut/Deferred]
- **Original Plan:** [What was supposed to be included]
- **Actual:** [What's in the doc]
- **Reason:** [Token budget|Quality over quantity|Out of scope|Dependency not ready]
- **Impact:** [What users can't do without this]
- **When to Revisit:** [Condition for adding it back]

Example:
### Decision 1: Simplified Pricing Analysis
- **Original Plan:** Detailed price elasticity analysis, customer lifetime value calcs
- **Actual:** Simple pricing tier comparison table
- **Reason:** Token budget (would have added 800+ tokens)
- **Impact:** Users can't optimize pricing strategy without elasticity data
- **When to Revisit:** After GTM v1.0 ships, create separate "Advanced Pricing Strategy" doc
```

---

## Dependencies

```markdown
## Dependencies

Items that depend on other work being done first:

### Dependency 1: [What's Blocked]
- **Blocks:** [What item(s) depend on this]
- **Waiting For:** [What needs to happen first]
- **Owner:** [Who controls the dependency]
- **Expected Date:** [When will it be ready]

Example:
### Dependency 1: Customer Interview Data
- **Blocks:** Item 1.1 (Add Competitive Analysis - need ICP validation)
- **Waiting For:** Sales team to complete 10 customer discovery interviews
- **Owner:** Sales team
- **Expected Date:** End of Q2 2026
```

---

## Verification Needed

```markdown
## Items Needing Verification

Content that should be verified before finalizing:

### Verification 1: [What Needs Verification]
- **Current Status:** [What's in the doc now]
- **Who Should Verify:** [Department/person]
- **How to Verify:** [Process or test]
- **Blocker?:** [Yes|No]

Example:
### Verification 1: Competitive Pricing Data
- **Current Status:** Pricing from public websites + Q1 2026 reports
- **Who Should Verify:** Sales team (they talk to prospects)
- **How to Verify:** 5-customer feedback survey on pricing accuracy
- **Blocker?:** No (can ship with caveat "verify with your sales team")

### Verification 2: Market Size Numbers
- **Current Status:** From Gartner report Q1 2026
- **Who Should Verify:** Research/Analytics team
- **How to Verify:** Cross-check against 2-3 other research firms
- **Blocker?:** Yes (market size is foundational)
```

---

## Changelog

Track why this DEBT.md exists and how it's evolving:

```markdown
## Changelog

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-02 | Created initial DEBT.md | Document shipped, P1 items deferred for v1.1 |
| 2026-04-10 | Moved Item 1.2 from P2→P1 | Sales team flagged competitive analysis as urgent |
| 2026-05-01 | Closed Item 2.1 | Pricing breakdown added in v1.1 update |
| 2026-05-15 | Added Dependency 1 | Waiting for customer data from interviews |
```

---

## DEBT.md Quality Checklist

Every DEBT.md must have:

- [ ] Frontmatter with total_items count
- [ ] Overview explaining why doc has debt
- [ ] P0 section (should be empty if doc shipped)
- [ ] P1+ items with Type, Impact, Effort, Owner, Details
- [ ] Known Limitations section
- [ ] Content Decisions explaining what was cut and why
- [ ] Dependencies listed with owners + expected dates
- [ ] Verification items with process for checking
- [ ] Changelog showing evolution
- [ ] Total items counts match (frontmatter = actual items)

---

## Template to Copy

```markdown
---
for_document: "{DocName}.md"
generated_at: YYYY-MM-DDTHH:MM:SSZ
total_items: 8
critical_items: 0
high_priority_items: 3
medium_priority_items: 3
low_priority_items: 2
---

# Technical Debt: {DocName}

For document: [{DocName}]({path}).md

---

## Overview

[Why this document has debt - what's done, what's deferred]

---

## Priority 0: Critical (Blocks Production)

None. Document is production-ready.

---

## Priority 1: High (Should Address Soon)

### Item 1.1: [Title]
- **Type:** [type]
- **Impact:** [impact]
- **Effort:** [estimate]
- **Owner:** [owner]
- **Details:** [description]

---

## Priority 2: Medium (Nice to Have)

### Item 2.1: [Title]
- **Type:** [type]
- **Impact:** [impact]
- **Effort:** [estimate]
- **Owner:** [owner]
- **Details:** [description]

---

## Priority 3: Low (Future Backlog)

### Item 3.1: [Title]
- **Type:** [type]
- **Impact:** [impact]
- **Effort:** [estimate]
- **Owner:** [owner]
- **Details:** [description]

---

## Known Limitations

### Limitation 1: [What's Limited]
- **Scope:** [What won't work]
- **Reason:** [Why]
- **Workaround:** [If any]

---

## Content Decisions

### Decision 1: [What Was Cut]
- **Original Plan:** [Plan]
- **Actual:** [What's in doc]
- **Reason:** [Why deferred]
- **Impact:** [What users lose]
- **When to Revisit:** [Condition]

---

## Dependencies

### Dependency 1: [What's Blocked]
- **Blocks:** [Items affected]
- **Waiting For:** [What's needed]
- **Owner:** [Who controls it]
- **Expected Date:** [When ready]

---

## Verification Needed

### Verification 1: [What Needs Check]
- **Current Status:** [What's there now]
- **Who Should Verify:** [Department]
- **How to Verify:** [Process]
- **Blocker?:** [Yes|No]

---

## Changelog

| Date | Change | Reason |
|------|--------|--------|
| YYYY-MM-DD | [Initial creation] | Document shipped |

---

**This DEBT.md is living. Update as items are closed or new debt discovered.**
```

---

## Automation: Auto-Generate DEBT.md

Builder should auto-create DEBT.md with:

1. **P0 items:** None (if doc ships)
2. **P1-P3 items:** Items user mentioned during builder questionnaire
3. **Known Limitations:** From builder's domain knowledge
4. **Content Decisions:** Cuts made for token budget
5. **Dependencies:** Flagged from prerequisites or cross-doc links

**Then human adds:**
- Specific effort estimates
- Owner assignments
- Verification processes
- Detailed descriptions

Final DEBT.md is human-reviewed before doc ships.


### DEV PLAN TEMPLATE

---
doc_type: dev-plan
domain: product
version: "1.0"
status: draft
product_name: "{ProductName}"
ai_tool: "{claude-projects | cursor | windsurf | codex}"
stack: "{frontend} + {backend} + {database}"
deployment: "{platform}"
generated_at: "{YYYY-MM-DD}"
quality_score: 0
exit_gates_passed: []
---

# Development Plan: {ProductName}
**Generated by:** Documentation Builder · {YYYY-MM-DD}
**AI Tool:** {tool} — this plan is formatted for direct use in {tool}
**Stack:** {stack}
**Deployment:** {deployment}

> **How to use this plan:**
> 1. Read CLAUDE.md first — it contains project context and commands
> 2. Complete phases in order — each phase is a prerequisite for the next
> 3. Check off tasks as you complete them
> 4. Run the acceptance test before marking a phase done
> 5. If you get stuck, refer to the relevant doc (linked per phase)

---

## Build Context

| Item | Value |
|---|---|
| Product | {one-liner description} |
| MVP Features | {feature 1}, {feature 2}, {feature 3} |
| Estimated phases | {N} |
| Estimated total tasks | {N} |

---

## Phase 0 — Project Setup
**Goal:** Working local dev environment. Nothing built yet — just everything needed to start building.
**Reference docs:** `SETUP_Environment.md`
**Time estimate:** 20–30 minutes

### Tasks

**0.1 — Initialize repository**
```bash
# Run these commands exactly:
{init command for stack — e.g. npx create-next-app@latest {app-name} --typescript --tailwind --app}
cd {app-name}
git init
git add .
git commit -m "chore: initial project scaffold"
```
Acceptance: `{dev server command}` runs without errors. Browser shows default app page.

**0.2 — Install dependencies**
```bash
{install command for all project dependencies}
```
List all packages being installed + one-line reason for each:
- `{package}` — {why}

Acceptance: `node_modules/` present, no install errors.

**0.3 — Configure environment**
Copy `.env.example` to `.env.local` and fill in:
```
{ENV_VAR_1}=    # {what this is and where to get it}
{ENV_VAR_2}=    # {what this is and where to get it}
```
Acceptance: Application loads without "missing environment variable" errors.

**0.4 — Set up database**
```bash
{database setup commands — e.g. npx prisma migrate dev --name init}
```
Acceptance: Database created. `{verify command}` returns success.

**Phase 0 complete when:** Dev server runs, database connected, no console errors.

---

## Phase 1 — Data Layer
**Goal:** All data models and migrations created and tested.
**Reference docs:** `DATA_Schema.md`
**Depends on:** Phase 0 complete
**Time estimate:** {N} hours

### Tasks

**1.1 — {Entity 1} model**
File: `{path/to/model}`
```
{schema definition for entity 1}
```
Acceptance: Migration runs. `{test query}` returns expected shape.

**1.2 — {Entity 2} model**
File: `{path/to/model}`
Acceptance: {testable statement}

**1.3 — Seed data (dev only)**
File: `{path/to/seed}`
Acceptance: `{seed command}` populates database with {N} test records per entity.

**Phase 1 complete when:** All entities migrated. Seed data loads. Schema matches `DATA_Schema.md` exactly.

---

## Phase 2 — Authentication
**Goal:** Users can sign up, log in, and log out. Session persists.
**Reference docs:** `API_Spec.md` → Auth section
**Depends on:** Phase 1 complete
**Time estimate:** {N} hours

### Tasks

**2.1 — Auth provider setup**
File: `{path/to/auth-config}`
Follow: `SETUP_Environment.md` → Auth section for API keys
Acceptance: `{auth provider dashboard}` shows app registered.

**2.2 — Sign up flow**
Files: `{route file}`, `{component file}`
Acceptance: New user created in database. Redirect to {destination page}.

**2.3 — Sign in / Sign out**
Files: `{route file}`, `{component file}`
Acceptance: Existing user can sign in. Session cookie set. Sign out clears session.

**2.4 — Route protection**
File: `{middleware file}`
Acceptance: Unauthenticated user redirected to /login. Authenticated user can access /dashboard.

**Phase 2 complete when:** Full auth flow works end-to-end in browser. Session persists on page reload.

---

## Phase 3 — Core Feature: {Feature 1 Name}
**Goal:** {What this feature does and why it's the most important MVP feature}
**Reference docs:** `API_Spec.md` → {section}, `ARCH_System.md` → {section}
**Depends on:** Phase 2 complete
**Time estimate:** {N} hours

### Tasks

**3.1 — API: {endpoint}**
File: `{route file}`
Method: `{HTTP method} {path}`
Request: `{shape}`
Response: `{shape}`
Acceptance: `curl {example call}` returns `{expected response}`.

**3.2 — UI: {component/page name}**
File: `{component file}`
Acceptance: {describe what the user sees and can do}

**3.3 — {Additional task}**
File: `{file}`
Acceptance: {testable statement}

**Phase 3 complete when:** User can complete the {feature 1} flow end-to-end without errors.

---

## Phase {N} — {Feature N Name}
*(Repeat Phase 3 structure for each MVP feature)*

---

## Phase {N+1} — Error Handling and Edge Cases
**Goal:** All known edge cases handled gracefully. No unhandled errors.
**Depends on:** All feature phases complete
**Time estimate:** {N} hours

### Tasks

**{N+1}.1 — Form validation**
All user inputs validated client-side and server-side. Error messages follow UX copy in `API_Spec.md`.

**{N+1}.2 — API error responses**
All API routes return structured errors per `API_Spec.md` → Error Responses section.

**{N+1}.3 — Empty states**
All list views handle 0 items. Loading states for async operations.

---

## Phase {N+2} — Testing
**Goal:** Core flows covered by automated tests. Regressions detectable.
**Depends on:** All feature phases complete
**Time estimate:** {N} hours

**{N+2}.1 — Unit tests:** {test command} — covers {what}
**{N+2}.2 — Integration tests:** covers {critical flows}
**{N+2}.3 — End-to-end (optional):** Playwright — covers {happy path scenarios}

Acceptance: `{test command}` exits 0. Coverage ≥ 70% on business logic.

---

## Phase {N+3} — Deployment
**Goal:** Live on {deployment platform}. Accessible via {domain/URL}.
**Reference docs:** `SETUP_Environment.md` → Deployment section
**Depends on:** Testing phase complete
**Time estimate:** {N} hours

**{N+3}.1 — Production environment config:** Set all env vars on {platform}
**{N+3}.2 — Deploy:** `{deploy command}` — expected output: {success message}
**{N+3}.3 — Verify:** {test these specific URLs/flows in production}

---

## Implementation Order Summary

```
Phase 0: Setup          ← No dependencies
    ↓
Phase 1: Data Layer     ← Needs: Phase 0
    ↓
Phase 2: Auth           ← Needs: Phase 1
    ↓
Phase 3: {Feature 1}    ← Needs: Phase 2
    ↓
Phase 4: {Feature 2}    ← Needs: Phase 2 (parallel with Phase 3 if independent)
    ↓
Phase N: Errors         ← Needs: All features
    ↓
Phase N+1: Tests        ← Needs: All features
    ↓
Phase N+2: Deploy       ← Needs: Tests passing
```

---

## Definition of Done

The product is ready to ship when:
- [ ] All phases complete and acceptance criteria met
- [ ] `{test command}` passes with 0 failures
- [ ] Application deployed and accessible
- [ ] All env vars documented in `.env.example`
- [ ] CLAUDE.md updated with any new commands or gotchas discovered during build
- [ ] No `console.error` or unhandled promise rejections in production logs


### DOC CANONICAL TEMPLATE

# DOC_CANONICAL_TEMPLATE.md — Output Standard

Every document generated by any builder MUST follow this structure. This template is optimized for AI readability — docs generated from it should be parseable and actionable by LLMs building the described product.

---

## YAML Frontmatter (Required)

```yaml
---
doc_type: prd|ux|ui|vision|architecture|data-schema|api-spec|setup|dev-plan|claude-md|starter-prompt|project-setup|project-instructions|system-guide|how-to|reference|feature|process|update|api-guide|adr|troubleshooting|config-reference|schema-reference|command-reference
domain: product|claude-project|skill|mcp|ai-docs|code|reference
builder_version: "v2.6"
generated_by: [builder_name]
generated_at: YYYY-MM-DDTHH:MM:SSZ

audience: beginner|intermediate|advanced|all
status: production|draft|review|deprecated
version: "1.0"
updated: YYYY-MM-DD

quality_score: 0-100
exit_gates_passed: [1,2,3,4,5]
context_tier: 1|2|3
assumptions_count: [number]
---
```

**Required fields:** doc_type, domain, builder_version, generated_by, generated_at, audience, status, version, quality_score, exit_gates_passed, context_tier, assumptions_count

---

## 0. Constraints & Non-Negotiables (Required for Product docs)

**This section goes FIRST — before the overview.** It contains the hard rules the building LLM must never deviate from.

```markdown
## Constraints & Non-Negotiables

> These constraints override any other instruction in this document. If a constraint conflicts with a recommendation elsewhere, the constraint wins.

| # | Constraint | Reason | Violation Impact |
|---|-----------|--------|-----------------|
| C1 | [Hard requirement] | [Why this is non-negotiable] | [What breaks if violated] |
| C2 | [Hard requirement] | [Why this is non-negotiable] | [What breaks if violated] |
| C3 | [Hard requirement] | [Why this is non-negotiable] | [What breaks if violated] |

**ASSUMED constraints** (from smart defaults — verify with stakeholder):
| # | Constraint | Default Reasoning | Override by |
|---|-----------|-------------------|-------------|
| A1 | [Assumed constraint] *(ASSUMED)* | [Why this default] | [What user should say to change it] |
```

**Rules:**
- Constraints derived from user input = confirmed, no marker needed
- Constraints from smart defaults = marked *(ASSUMED)* with override instructions
- Maximum 10 constraints — if more, the scope is too big
- Every constraint must state what breaks if violated — this prevents the LLM from treating it as a suggestion

---

## 1. Title + Overview (Required)

```markdown
# [Clear Action Verb + Noun]

[One sentence: what you'll accomplish]
[One sentence: why you need this / business context]

**Builds:** [Product name — one-liner]
**Audience:** [beginner|intermediate|advanced]
**Context tier:** [1|2|3] — [Full context | Solid context, N assumptions | Minimal context, N assumptions]
```

**Rules:**
- Title must start with action verb
- Overview ALWAYS exactly 2 sentences
- Context tier disclosure is mandatory — the building LLM needs to know how much to trust the details

---

## 2. Decision Records (Required for Architecture, Data Schema, API Spec)

Every technology choice, design pattern, or structural decision must be recorded with reasoning.

```markdown
## Decisions

### D1: [Decision title]
**Choice:** [What was chosen]
**Why:** [Reasoning — tied to user requirements or constraints]
**Alternatives rejected:** [What else was considered and why not]
**Status:** CONFIRMED | ASSUMED
**Affects:** [Which other docs/sections depend on this decision]

### D2: [Decision title]
[...]
```

**Rules:**
- CONFIRMED = user explicitly stated or approved this
- ASSUMED = defaulted by Docgen, marked for user review
- "Affects" field is critical — when a user changes a decision, the LLM knows what else to update
- Every decision in ARCH must be referenced by the DEV_Plan
- Never present an ASSUMED decision without the ASSUMED marker — this is a hallucination (Rule 1 violation)

---

## 3. Content Section (Variable by doc_type)

### For Product docs (PRD, UX, UI, Vision):

```markdown
## [Feature/Section Name]

### Intent
[One sentence: what this feature/section achieves for the user]

### Requirements
| ID | Requirement | Source | Priority | Status |
|----|------------|--------|----------|--------|
| R1 | [Specific requirement] | User input / INFERRED | Must | Confirmed / Assumed |
| R2 | [Specific requirement] | User input / INFERRED | Should | Confirmed / Assumed |

### Acceptance Criteria (as testable checks)
```
GIVEN: [precondition]
WHEN: [action]
THEN: [expected result]
VERIFY: [how to test — command, UI check, or API call]
```

### Out of Scope
[Explicitly list what this feature does NOT include — prevents LLM scope creep]

### When-in-Doubt Defaults
[For areas where requirements are vague, specify what the LLM should do:]
- If [ambiguous situation]: do [specific default behavior]
- If [unclear requirement]: implement [specific approach]
- If [missing detail]: use [specific fallback]
```

**Rules:**
- Every requirement has a Source (User input = confirmed, INFERRED = Docgen derived it)
- Acceptance criteria use GIVEN/WHEN/THEN + VERIFY format — directly translatable to tests
- Out of Scope is mandatory — prevents the LLM from adding features
- When-in-Doubt Defaults fill the gaps for the LLM when requirements are loose

### For Setup/Installation/How-To Guides:

```markdown
## [Section Title]

### Step 1: [Specific Action]
1. Run: `[exact command]`
   Expected: [what appears in terminal]

   **AI metadata:**
   - Precondition: [what must be true before this step]
   - Postcondition: [what's true after this step]
   - Time: X minutes
   - Common error: See Troubleshooting → [error section]

### Step 2: [Specific Action]
[repeat pattern]
```

**Rules:**
- One action per step
- Number steps (1, 2, 3) not bullets
- Always include "Expected:" after each command
- Always include **AI metadata:** block with precondition/postcondition

### For API/Reference Docs:

```markdown
## Endpoint: [HTTP METHOD] /[path]

**Description:** [One sentence what this does]
**Authentication:** [Required|Optional] - [type]

**Parameters:**
| Name | Type | Required | Description | Example |
|------|------|----------|-------------|---------|
| param1 | string | Yes | What it does | "value" |

**Request Example:**
```bash
curl -X GET https://api.example.com/endpoint \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"param1": "value"}'
```

**Response Example:**
```json
{
  "status": "success",
  "data": { ... }
}
```

**Error Codes:**
| Code | Meaning | Fix | Related Constraint |
|------|---------|-----|--------------------|
| 401 | Unauthorized | Check API key | C2 (auth required) |
| 404 | Not found | Verify endpoint exists | — |
```

### For Dev Plans:

```markdown
## Phase N: [Phase Name]
**Depends on:** Phase [N-1] complete
**Delivers:** [What's usable at end of this phase]
**Estimated tasks:** [count]

### Task N.1: [Exact file to create/modify]
<!-- PURPOSE: [What this file does in the system. Depends on: file1.ts, file2.ts] -->
- **File:** `[exact path from ARCH doc]`
- **Action:** Create | Modify | Configure
- **Implements:** [Which requirement ID from PRD — e.g., R1, R3]
- **Acceptance criteria:**
  ```
  GIVEN: [precondition]
  WHEN: [action]
  THEN: [expected result]
  VERIFY: [exact test command or check]
  ```
- **Blocked by:** [Task IDs that must complete first, or "none"]
- **When-in-doubt:** [If the LLM is unsure about implementation detail, do THIS]

### Task N.2: [...]
```

**Rules:**
- Every task references the exact file path from ARCH doc (discrepancy = Gate 3 fail)
- Every task links to requirement IDs from the PRD
- Blocked-by creates an explicit dependency graph
- When-in-doubt gives the LLM a safe fallback for ambiguous implementation details
- Phase-level "Delivers" tells the LLM what should be working after this phase

---

## 4. Anti-Patterns (Required for Architecture and Dev Plan docs)

```markdown
## Anti-Patterns — What NOT to Do

| Pattern | Why It's Wrong | Do This Instead |
|---------|---------------|-----------------|
| [Bad approach] | [What breaks] | [Correct approach with file reference] |
| [Bad approach] | [What breaks] | [Correct approach with file reference] |
```

**Rules:**
- Minimum 3 anti-patterns for Architecture docs
- Minimum 2 anti-patterns per phase in Dev Plan
- Each anti-pattern must reference the correct approach with a specific file or pattern
- Focus on mistakes the LLM is likely to make (e.g., "Don't create a separate auth service — use the Supabase auth client in `src/lib/auth.ts`")

---

## 5. Expected Output / Success Indicator (Required)

```markdown
## What Success Looks Like

After completing [action], you should:

| Check | Expected | Command/Evidence |
|-------|----------|-----------------|
| [What to verify] | [What should happen] | `[Exact command]` |
| [What to verify] | [What should happen] | `[Exact command]` |

**If any check fails:** Go to Troubleshooting section below.
```

---

## 6. Troubleshooting (Required if steps exist)

```markdown
## Troubleshooting

### Error: "[Exact error message]"
**Root cause:** [Why this happens]
**Fix:**
1. [Specific step 1]
2. [Specific step 2]
3. [Verification step]

**AI metadata:**
- Error signature: "[Exact error from logs]"
- Precondition check: [What must be true]
- Related: [Link to related doc by title]
```

---

## 7. Assumption Register (Required when context_tier < 3)

```markdown
## Assumptions Register

All items marked ASSUMED or INFERRED in this document:

| ID | Item | Default Value | Reasoning | Impact if Wrong | Override |
|----|------|--------------|-----------|-----------------|----------|
| A1 | Tech stack | Next.js + Supabase | Solo founder, web SaaS | Requires full regeneration of ARCH + DATA + API + DEV | Tell Docgen "change stack to [X]" |
| A2 | Auth method | Supabase Auth | Matches default DB | Affects auth flows in UX + API endpoints | Tell Docgen "use [auth provider] instead" |

**To override any assumption:** Say "change [assumption] to [your preference]" and the affected docs will be regenerated.
```

**Rules:**
- Every ASSUMED/INFERRED item from all sections consolidated here
- Impact column tells the user what breaks if they change it
- Override column tells them exactly what to say
- This register is the user's checklist for reviewing generated docs

---

## 8. What's Next (Required)

```markdown
## After Completing This

You now have [what they accomplished]. Next steps:

1. **[Related task 1]** → See: "[Related doc title]"
   - Use if: [condition]
   - Time: X minutes

2. **[Related task 2]** → See: "[Related doc title]"
   - Use if: [condition]
   - Time: X minutes
```

---

## NEVER Include These

- "Best practices" without listing specific practices
- "Learn more" links without context
- "It's important to remember" (make it a constraint or prerequisite)
- Vague instructions ("Configure properly", "Handle edge cases appropriately")
- Fabricated facts, statistics, or decisions not grounded in user input
- Technical decisions without CONFIRMED/ASSUMED status
- Requirements without source attribution (user input vs inferred)
- Theory without examples
- Generic disclaimers

---

## Quality Requirements

### Human Pass
- [ ] Constraints section present and complete (for product docs)
- [ ] Every decision has CONFIRMED/ASSUMED status
- [ ] Every requirement has source attribution
- [ ] Acceptance criteria use GIVEN/WHEN/THEN/VERIFY format
- [ ] No vague language anywhere
- [ ] Anti-patterns included (for ARCH and DEV_Plan)
- [ ] Assumption Register matches inline markers

### AI Pass
- [ ] Frontmatter complete with context_tier and assumptions_count
- [ ] Steps have **AI metadata:** blocks
- [ ] Dev plan tasks have blocked-by dependencies
- [ ] Dev plan tasks reference exact file paths from ARCH
- [ ] When-in-doubt defaults present for ambiguous areas
- [ ] Every ASSUMED item has override instructions
- [ ] No hallucinated content (Rule 1 compliance)

### Token Efficiency
- [ ] Doc size within domain budget (see config/token_budgets.json)
- [ ] No unnecessary explanation (rules explain, examples show)
- [ ] Prose sections ≤ 4 paragraphs
- [ ] Every section serves clear purpose
- [ ] No redundancy between sections


### STARTER PROMPT TEMPLATE

# Starter Prompt Template
**Purpose:** This file is the FIRST MESSAGE you send to your AI coding tool. It bootstraps the entire project in one message. Copy everything between the horizontal rules and paste it verbatim.
**Do not edit it** — the exact wording is optimized for AI compliance. If something is wrong, fix the source docs and regenerate this file.

---

*(Everything below this line is the starter prompt — copy and paste into your AI tool)*

---

You are building **{ProductName}**.

## What You're Building

{one-liner: "[ProductName] helps [target user] to [core outcome] by [differentiator]"}

**MVP scope:** {feature 1}, {feature 2}, {feature 3}
**Stack:** {frontend} + {backend} + {database}
**Deployment target:** {platform}

---

## Context Files in This Bundle

Read these files in this order before writing any code:

1. `CLAUDE.md` — project rules, commands, architecture overview (read first, always)
2. `docs/ARCH_System.md` — full system architecture and file structure
3. `docs/DATA_Schema.md` — all data entities, fields, and relationships
4. `docs/API_Spec.md` — all endpoints with request/response shapes
5. `docs/SETUP_Environment.md` — environment variables, dependencies, deployment
6. `docs/DEV_Plan.md` — your implementation plan (phases → tasks → acceptance criteria)

After reading all files, confirm back: "I've read all context files. I understand [X]. My first task is [Y from Phase 0]."

---

## Your First Task

Complete **Phase 0** from `docs/DEV_Plan.md`:

{copy Phase 0 task list here verbatim from the dev plan}

---

## Rules for This Build

1. **Follow the dev plan phases in order.** Do not skip ahead. Phase N must pass its acceptance criteria before Phase N+1 starts.
2. **Read before writing.** Before creating any file, confirm it's in the architecture (`docs/ARCH_System.md`). If a file isn't in the architecture, ask before creating it.
3. **Ask before deviating.** If you encounter a situation not covered by the docs, stop and ask. Do not invent solutions to undocumented problems.
4. **Update CLAUDE.md as you go.** When you discover a gotcha, a useful command, or a workaround — add it to CLAUDE.md under "Important Notes."
5. **One phase at a time.** When a phase is complete, say "Phase {N} complete — acceptance criteria met: [list]" before starting the next.

---

## Verification Checklist After Phase 0

Before moving to Phase 1, confirm all of these are true:
- [ ] `{dev server command}` runs without errors
- [ ] Browser shows app running at `localhost:{port}`
- [ ] Database connected (no connection errors)
- [ ] `.env.local` populated from `.env.example`
- [ ] `{test command}` exits 0

---

Start now. Read `CLAUDE.md` first.

---
*(End of starter prompt)*

---

## How to Use This File

**For Claude Projects:**
1. Upload all files from this bundle to the project knowledge base
2. Paste the starter prompt above as your first message in the project

**For Cursor / Windsurf:**
1. Open the project folder in Cursor/Windsurf (the scaffold folder from this bundle)
2. Open a new AI chat
3. Paste the starter prompt as your first message
4. Cursor will read the project files automatically

**For Codex / API:**
1. Include `CLAUDE.md` contents as the system prompt
2. Use the starter prompt as the first user message
3. Attach all doc files as context

**If the AI doesn't follow the dev plan:**
Add to the starter prompt: "I will ask you to stop and reread `docs/DEV_Plan.md` if you deviate from the phase order. When I say 'check the plan', stop what you're doing and reread the current phase."



========================================================================
PROJECT INSTRUCTIONS TEMPLATES
========================================================================

### PROJECT INSTRUCTIONS Docgen AI First

# Documentation Generation System — AI-First Project Instructions

## Role

You are a documentation standards enforcer and AI-optimization architect for the docgen framework. You guide users through creating production-grade documentation that works for both humans AND AI systems (Claude Projects, RAG pipelines, agents). You apply rigid standards, catch anti-patterns early, and evolve the framework based on real-world friction.

---

## How to Use Project Context

Treat all .md files in this project as authoritative standards:

**Human-first rules:**
- **Documentation_Content_Guide.md** is the gold standard for human-readable structure. Quote it when evaluating any doc.
- **Prerequisites_Guide.md** defines what good prerequisites look like for humans. Reference it whenever someone writes a prereq section.

**AI-first rules:**
- **AI_First_Documentation_Format.md** is the standard for machine-readable docs. Check for YAML frontmatter, metadata blocks, parseable structure.
- **Project_Chat_Instructions_Rules.md** is the rulebook for custom instructions. Use it when creating or auditing project instructions.

**System planning:**
- **documentation_ecosystem.md** maps priorities. Reference it when someone asks what to build next.

If a user's doc violates a rule, point to the specific section in these files. Don't rewrite from memory.

---

## Response Format

**Length:** Keep answers under 200 words unless user asks for depth or is writing a doc section.

**Structure:** Problem → Specific Rule → Example (good) → Example (bad) → Next Action.

**Tone:** Direct, no fluff. "This violates X" beats "You might want to consider."

**When to ask vs. answer:** If a doc requirement is ambiguous, stop and ask for specifics. Don't guess. If user says "my docs aren't working," ask: "Are people confused at a specific step? Are they skipping sections? Are Claude Projects having trouble parsing it?"

**Examples:** Always show before/after or good/bad paired. One sentence explaining the difference. Include both human and AI impact.

---

## Do's

- **Quote the rules files** whenever discussing what good looks like. Reference by filename + section. Distinguish human-first from AI-first.
- **Run dual quality checklists** from both Documentation_Content_Guide.md (human) and AI_First_Documentation_Format.md (machine). Report separately.
- **Check frontmatter first.** Before reading content, verify YAML exists with all 8 fields: doc_type, audience, difficulty, time_estimate, prerequisites, related_docs, tags, updated, status.
- **Catch anti-patterns early.** When you see vague language, missing metadata, or non-parseable structure, flag it immediately with specific bad example from guides.
- **Suggest doc evolution triggers.** When user reports real failure (people get stuck, Claude can't parse prereqs, errors aren't discoverable), propose what needs changing. Track as patterns.

---

## Don'ts

- **Never accept docs without frontmatter.** If YAML is missing, stop and ask user to add it before reviewing content.
- **Don't rewrite without showing violations first.** If doc is bad, quote rule it breaks (human or AI), show example from guide, then offer to rewrite.
- **Never skip either checklist.** Docs must pass BOTH human quality checklist (from Content Guide) AND AI checklist (from AI-First Format).
- **Don't suggest building without system thinking.** If user wants templates, point to documentation_ecosystem.md AND explain how to make them AI-first.
- **Never auto-assume the doc is done.** Final sign-off requires: (1) Human quality checklist passed, (2) AI quality checklist passed, (3) Reader Claude test suggested, (4) Evolution triggers noted.

---

## Examples

**GOOD:**

User: "I wrote a setup guide. Can you review it?"

Claude: 
First, checking frontmatter:
```yaml
---
doc_type: setup_guide
audience: beginner
difficulty: easy
time_estimate: "20-minutes"
prerequisites: [nodejs_16+, npm_8+]
related_docs: [How to Configure, Troubleshooting]
tags: [setup, installation]
updated: 2026-04-02
status: production
---
```

✅ Frontmatter complete.

Human quality check (Documentation_Content_Guide.md):
- ✅ Overview answers "what/why" in 2 sentences
- ❌ Expected Output section missing verification table
- ✅ Steps are numbered with expected output

AI quality check (AI_First_Documentation_Format.md):
- ✅ Prerequisites use Level 1-4 structure
- ❌ Troubleshooting errors lack "Error signature:" labels
- ❌ Steps missing **AI metadata:** blocks with preconditions

**Next:** Add verification table to Expected Output. Add error signatures. Add metadata blocks to steps. Then run Reader Claude test.

**BAD:**

User: "I wrote a setup guide. Can you review it?"

Claude: Looks good! Setup guides are important. Make sure steps are clear and prerequisites are listed.

Why: Good answer checks frontmatter first, runs both checklists, identifies specific failures with references; bad answer is generic and misses machine-readability entirely.

---

## AI-First Enforcement

### Frontmatter (Required - Non-negotiable)

Every doc must have:
```yaml
---
doc_type: [8 types only]
audience: beginner|intermediate|advanced|all
difficulty: easy|medium|hard
time_estimate: [specific duration]
prerequisites: [list with exact versions]
related_docs: [doc titles]
tags: [keywords]
updated: YYYY-MM-DD
status: production|draft|deprecated
---
```

**Why:** Claude extracts this automatically to:
- Filter docs by skill level
- Build prerequisite chains
- Find related knowledge
- Route to correct doc type
- Know recency

### Prerequisites Must Be Parseable

```markdown
### Level 1: Tools & Software
- **Name Version** (required|optional)
  - Check: [exact command]
  - Install: [link or command]
  - Why: [one sentence]
```

**Why:** Claude can:
- Extract prerequisites programmatically
- Run checks for users
- Build prerequisite dependency graphs
- Suggest alternative paths

### Steps Need Metadata

```markdown
### Step 1: [Action]
1. Run: [exact command]
   Expected: [what appears]
   
   **AI metadata:**
   - Precondition: [what must be true]
   - Postcondition: [what's true after]
   - Common error: [error signature if applicable]
```

**Why:** Claude can:
- Verify each step's dependencies
- Suggest troubleshooting proactively
- Build workflow diagrams automatically
- Chain steps intelligently

### Errors Must Have Signatures

```markdown
### Error: "command not found: npm"
**Root cause:** npm not installed
**Fix:** [steps]

**AI metadata:**
- Error signature: "command not found: npm"
- Precondition: nodejs_16+
```

**Why:** Claude can:
- Match user's exact error to solutions
- Prevent bad advice (e.g., suggesting npm config when npm isn't installed)
- Build error→solution knowledge graph
- Help users faster

---

## Auto-Evolution for AI Docs

**New signals to track:**

1. **Claude can't parse prerequisites** → Structure isn't consistent
2. **Error signatures don't match user errors** → Collecting wrong error patterns
3. **Claude suggests wrong related doc** → Links in metadata are wrong
4. **Frontmatter fields missing** → Users don't understand why each field matters
5. **Steps fail in wrong preconditions** → Precondition blocks are inaccurate

**When user reports Claude-related failure:**

Ask:
1. "What did Claude suggest?" (shows parsing issue)
2. "What were prerequisites Claude saw?" (shows frontmatter parsing)
3. "Did Claude find related docs?" (shows link discovery)

Then propose:
- Fix metadata structure
- Add error signature
- Correct precondition
- Update frontmatter field

**Quarterly evolution:** Review docs AI tried to parse. Which ones did it struggle with? Those are candidates for restructuring.

---

## Quality Checklist: Dual Pass

### Human Pass (Documentation_Content_Guide.md)
- [ ] Overview: 2 sentences answering what/why
- [ ] Prerequisites: Specific, testable, realistic
- [ ] Steps: Exact commands, expected output shown
- [ ] Success: Clear indicator of "it worked"
- [ ] Errors: Organized by symptom
- [ ] Next: Clear forward path

### AI Pass (AI_First_Documentation_Format.md)
- [ ] Frontmatter: All 8 fields present
- [ ] Prerequisites: Use Level 1-4 structure
- [ ] Steps: Have **AI metadata:** blocks with preconditions
- [ ] Errors: Have "Error signature:" field
- [ ] Tables: Verification uses commands, not prose
- [ ] Links: In metadata, not inline
- [ ] Timestamps: In frontmatter, not prose

**Both must pass. Not either/or.**

---

## Final Approval Gate

Doc cannot ship until:

1. ✅ Human quality checklist: 0 failures
2. ✅ AI quality checklist: 0 failures
3. ✅ Frontmatter: Complete with accurate fields
4. ✅ Metadata blocks: In all steps and errors
5. ✅ Evolution trigger: "If Claude can't parse this, it's because..."
6. ✅ Reader Claude test: Suggested (can they follow it?)

All 6 clear → "Ready for production (both human and AI)."
Any missing → "Hold, fix X first."

---

## For Claude Projects Setup

When uploading AI-first docs to a Claude Project:

```markdown
# Custom Instructions Addition

These docs use AI-first format. When reading them:

1. **Read frontmatter first:** Extract doc_type, audience, prerequisites, related_docs
2. **Filter by user level:** If user is beginner, prioritize "audience: beginner" docs
3. **Check prerequisites:** Before suggesting a step, verify preconditions are met
4. **Match errors exactly:** Use "Error signature:" field to match user problems
5. **Suggest related docs:** From related_docs field in frontmatter
6. **Respect status:** Ignore docs marked "deprecated" unless user explicitly asks
```

This turns docs into structured knowledge that Claude Projects can navigate intelligently.


### PROJECT INSTRUCTIONS Docgen Production

# Documentation Builder — Project Instructions
> Paste this into Claude.ai → Project → Custom Instructions.
> Length: ~1000 words (within compliance per SYSTEM_Project_Instructions_Rules.md).
> Last updated: April 2026 · v1.3

---

## Role

You are the Documentation Generation System. Your mission: take any idea — a product, an AI assistant, a workflow, an integration — understand it fully, and generate complete implementation-ready documentation so that an AI coding agent or Claude can build the thing correctly.

Your docs must enable LLMs to build QUALITY products that BOTH WORK and FOLLOW user requirements — even when those requirements are loose or not concise.

You operate interactively: collect context flexibly → assess sufficiency → confirm plan → generate → deliver → offer to refine. No question is mandatory. The user decides how much context to provide.

**Critical rule: Never hallucinate.** Never fabricate facts, invent requirements, or present assumptions as confirmed. If something is missing: ask the user, use a marked default, or add a NEEDS INPUT placeholder.

---

## Conversation Starters

Set these in Claude.ai Project settings → Conversation Starters:
1. "I want to build a product — an app, SaaS tool, or platform"
2. "I want to build a Claude Project — an AI assistant for my team"
3. "I want to build a Skill — a repeatable workflow or /command"
4. "I want to connect Claude to an external tool via MCP"

These appear as clickable buttons before the user types anything. When clicked, they send the text as the first message, triggering the menu + routing to the correct builder.

---

## First Response — Always Show the Menu

At the start of **every new conversation**, your very first response must be the navigation menu from CLAUDE.md — regardless of what the user says. Even if they clicked a conversation starter, show the menu first, then acknowledge their selection and begin intake. Show the menu first, then respond to their message.

If the user picks a number or describes a build, immediately identify the type and begin intake. Do not show the menu again unless the user asks or types `/menu`.

---

## Interactive Operating Mode

**Step 1 — Identify the build type.** Read the SYSTEM_Build_Decision_Framework section (in REFERENCE_System.md). Four types: Product, Claude Project, Skill, MCP Server. Classify before anything else.

**Step 2 — Collect context flexibly.** No question is mandatory. The user can answer questions, paste freeform context (specs, notes, braindumps), upload files, or mix all three. Use the builder questions (in REFERENCE_Builders.md) as a guide — ask only what's missing. Dynamically assess context sufficiency:
- **Tier 1 (minimal):** Warn the user. List all assumptions. Get explicit permission before generating.
- **Tier 2 (solid):** Note remaining defaults. Proceed after confirmation.
- **Tier 3 (full):** Best output. Proceed after confirmation.

If something is critical and can't be defaulted — **ask the user.** Never guess.

**Step 3 — Map skills to the generation plan.** Before generating, read the SKILL MAP (in REFERENCE_Builders.md). Build the plan showing which skill handles each doc, confirmed vs. assumed items, and ask for confirmation.

**How to call skills:**
- **In Cowork / Claude Code:** Use the Skill tool directly with intake context as input. Use skill output as draft.
- **In Claude.ai Chat:** Skills aren't callable. Apply the domain expertise the skill represents. The SKILL_MAP tells you WHAT expertise to apply.

**Stack-specific skills are mandatory** at Architecture, Setup, Dev Plan, and Starter Prompt.

**Step 4 — Generate in the correct order.** For products: PRD → UX → UI → Vision → Architecture → Data Schema → API Spec → Setup → Dev Plan → CLAUDE.md → Starter Prompt. Apply mapped skill at each stage. Run quality gates. Mark all ASSUMED/INFERRED items.

**Step 5 — Deliver and recommend next skills.** After delivering:
> "Bundle delivered. Review all docs — especially items marked ASSUMED or INFERRED.
> For your next phase, these skills can help: [relevant skills]"

**Step 6 — Rerun on request.** Regenerate only the specific doc. Re-apply skill + quality gates. Update the zip.

---

## How to Use Project Context

**Your knowledge base has 3 consolidated reference files + CLAUDE.md:**
- `REFERENCE_System.md` — all system guides (quality gates, naming, content standards, AI readability standards)
- `REFERENCE_Builders.md` — all builder questions + rules + **SKILL MAP routing table**
- `REFERENCE_Templates.md` — all templates, checklists, examples, config

For complete source files: https://github.com/sharpenedknife/claude-document-generation

**Truth sources (in REFERENCE_System.md) — quote directly, never paraphrase:**
- `SYSTEM_Exit_Rules` — 5 gates. Wins all conflicts.
- `SYSTEM_Build_Decision_Framework` — build type identification + routing
- `SYSTEM_Content_Guide` — required sections per doc type + AI readability standards
- `SYSTEM_Token_Optimization` — hard token budgets
- `SYSTEM_Coding_Standards` — code quality rules

---

## Response Format

**Guidance:** Under 200 words. Direct. No preamble.
**Reviews:** Gate number → exact rule quoted → bad example → good example → next action.
**Generation:** Follow `DOC_CANONICAL_TEMPLATE.md` exactly. Constraints section first. Decision records with CONFIRMED/ASSUMED status. GIVEN/WHEN/THEN/VERIFY acceptance criteria. When-in-Doubt defaults for ambiguous areas. Assumption Register at end.

---

## Do's

1. **Show the navigation menu first** in every new conversation. No exceptions.
2. **Collect context flexibly** — let the user provide input however they want.
3. **Warn before generating with thin context** — list all assumptions, get permission.
4. **Mark every assumption** — ASSUMED, INFERRED, or NEEDS INPUT. Never present defaults as confirmed.
5. **Ask the user when in doubt** — it's always better to ask than to guess wrong.
6. **Show the generation plan** and get confirmation before generating.
7. **Offer to rerun individual docs** after every delivery.

---

## Don'ts

1. **Do not hallucinate.** Never fabricate facts, invent features, or present assumptions as confirmed.
2. **Do not require all questions answered.** Assess dynamically, warn if thin, but never block.
3. **Do not generate without confirming the plan first.**
4. **Do not accept vague language in generated docs.** Flag with exact anti-pattern.
5. **Do not skip DEBT logging.** Known gaps go in `backlog/SYSTEM_DEBT.md`.
6. **Do not regenerate the full bundle when only one doc needs work.**

---

*This project enforces production quality. No bad docs ship. No hallucinated content ships.*



========================================================================
QUALITY CHECKLISTS
========================================================================

### CHECKLIST AI Quality

# AI Quality Checklist (Gate 4 - AI Pass)

Use before submitting doc for Gate 4 AI portion.

- [ ] Frontmatter extracts correctly (8 required fields)
- [ ] YAML is valid (no syntax errors)
- [ ] Prerequisites parseable (Levels 1-4 consistent)
- [ ] Each step has preconditions/postconditions
- [ ] Error signatures are exact (from actual errors)
- [ ] All links in metadata, not prose
- [ ] Success table has runnable commands
- [ ] Related docs discoverable from frontmatter
- [ ] No inline links (move to metadata)
- [ ] Error sections use "Error: [exact signature]"

**GATE 4 AI PASS:** All checked ✓


### CHECKLIST Human Quality

# Human Quality Checklist (Gate 3)

Use before submitting doc for Gate 3 review.

- [ ] Overview explains what AND why (not just what)
- [ ] All commands are exact and testable (not "install X")
- [ ] Expected output shown after each step
- [ ] Every error has Root cause + Fix steps
- [ ] Prerequisites are realistic
- [ ] All external links go to download page (not homepage)
- [ ] All cross-references use doc titles (not URLs)
- [ ] No acronyms without first definition
- [ ] No ambiguous pronouns without clear referent
- [ ] Tone consistent throughout
- [ ] No contradictions between sections
- [ ] No vague language ("configure properly", "make sure")
- [ ] Steps use numbers (not bullets)
- [ ] One action per step
- [ ] Success indicator is clear and testable
- [ ] Errors organized by symptom, not cause

**GATE 3 PASS:** All checked ✓


### CHECKLIST Token Efficiency

# Token Efficiency Checklist (Gate 4 - Token Pass)

Use before submitting doc for Gate 4 token portion.

- [ ] Token count ≤ domain budget (config/token_budgets.json)
- [ ] Prose sections ≤ 4 paragraphs
- [ ] Every section serves purpose (no fluff)
- [ ] Examples concise but complete
- [ ] Errors: Only top 3-5 (rest in DEBT.md)
- [ ] No repeated content between sections
- [ ] No theoretical explanation (link instead)
- [ ] No "nice to know" (move to DEBT.md P3)
- [ ] No generic disclaimers
- [ ] Quality score ≥ 85 at this token count

**GATE 4 TOKEN PASS:** All checked ✓



========================================================================
REFERENCE EXAMPLES
========================================================================

### EXAMPLE Perfect Setup Guide

---
doc_type: setup_guide
domain: web_dev
builder_version: "v1.0"
generated_by: example_builder
generated_at: 2026-04-02T00:00:00Z
builder_session_id: example_session_001

audience: beginner
difficulty: easy
time_estimate: "15-minutes"
prerequisites: [terminal_basics]
related_docs: [Deploy_to_Production, Troubleshooting_Setup]
tags: [setup, nodejs, npm, quick_start]

status: production
version: "1.0"
updated: 2026-04-02

quality_score: 95
token_count: 2340
exit_gates_passed: [1,2,3,4,5]
exit_gates_failed: []
---

# How to Install Node.js and npm

Install Node.js and npm on your machine in 15 minutes.
This gets you ready to run JavaScript applications locally.

**Search keywords:** node.js installation, npm setup, nodejs download, javascript environment
**Audience:** beginner
**Time to complete:** 15 minutes

---

## Prerequisites

### Node.js (not yet installed)
Check: `node --version`
If you see: "command not found" → continue to setup
If you see: "v16.0.0+" → you already have it installed ✓

Install if needed: https://nodejs.org/en/download/ (download v16 LTS or newer)
Why: Node.js is the JavaScript runtime. npm comes with it.

---

## Setup

### Step 1: Download Node.js Installer
1. Go to: https://nodejs.org/en/download/
2. Click: Green button (LTS version - most stable)
3. Choose: Your operating system (Windows/Mac/Linux)
4. Click: Download

Expected: `.msi` (Windows), `.pkg` (Mac), or `.tar.xz` (Linux) file downloaded

**AI metadata:**
- Precondition: Internet access, admin rights to install
- Postcondition: Installer file on your computer
- Time: 1 minute
- Common error: See Troubleshooting → "Download fails"

---

### Step 2: Run the Installer
1. Open the downloaded file
2. Click: "Install" or "Next" through the steps
3. Accept: Default settings (click through)
4. Restart: Your computer (important!)

Expected: Installer completes, system restarts

**AI metadata:**
- Precondition: Installer downloaded, admin rights
- Postcondition: Node.js installed, terminal updated
- Time: 5 minutes
- Common error: See Troubleshooting → "Installation hangs"

---

### Step 3: Verify Installation
1. Open terminal (Mac/Linux) or Command Prompt (Windows)
2. Run: `node --version`
   Expected output: `v16.13.0` (or higher)

3. Run: `npm --version`
   Expected output: `8.1.0` (or higher)

Expected: Both commands show version numbers ✓

**AI metadata:**
- Precondition: Installer completed, computer restarted
- Postcondition: Node and npm in system PATH
- Time: 2 minutes
- Common error: See Troubleshooting → "Command not found"

---

## What Success Looks Like

After setup, you should:

| Check | Expected | Command |
|-------|----------|---------|
| Node installed | Version shows (v16+) | `node --version` |
| npm installed | Version shows (8+) | `npm --version` |
| Can create project | No errors | `npm init -y` |
| Can install packages | No errors | `npm install express` |

If all pass: ✅ Setup complete

---

## Troubleshooting

### Error: "command not found: node"
**Root cause:** Node.js not in system PATH (terminal wasn't restarted after install)

**Fix:**
1. Restart your computer (close and reopen terminal)
2. Try again: `node --version`
3. If still fails: Uninstall and reinstall Node.js

**AI metadata:**
- Error signature: "command not found: node"
- Precondition check: Installer completed? Restart done?
- Related: Installation hangs (see that error)

---

### Error: "v15.6.0 (node version too old)"
**Root cause:** Node.js installed but version too old (need v16+)

**Fix:**
1. Uninstall current Node.js
2. Download v16+ from nodejs.org
3. Install new version
4. Restart computer
5. Verify: `node --version` (should show v16+)

**AI metadata:**
- Error signature: "v15" or "v14" showing when you check
- Precondition check: Which version shows? `node --version`
- Related: Installation fails (wrong download link)

---

### Error: Permission denied (Mac/Linux)
**Root cause:** Missing admin rights or PATH not updated

**Fix:**
1. Restart terminal: Close and reopen
2. Try again: `npm --version`
3. If still fails: Try `sudo npm --version` (admin mode)

**AI metadata:**
- Error signature: "permission denied" or "EACCES"
- Precondition check: Is terminal open after restart?
- Related: Command not found

---

## Why This Approach

We use the official Node.js installer because:
- **Simplest:** No build steps, works for beginners
- **Official:** Directly from nodejs.org, always current
- **Reliable:** Handles PATH setup automatically
- **Tested:** Millions of users, no surprises

---

## After Setup

You now have Node.js and npm installed. Next steps:

1. **Create your first project** → See: "Create a Node.js Project"
   - Use if: You want to start building
   - Time: 10 minutes

2. **Learn npm basics** → See: "Understanding npm packages"
   - Use if: You want to understand how npm works
   - Time: 15 minutes

3. **Deploy to production** → See: "Deploy Node.js App"
   - Use if: You're ready to put your app online
   - Time: Varies

Choose based on your next goal.



========================================================================
CONFIGURATION
========================================================================


