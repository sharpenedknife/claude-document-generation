# Documentation Builder — Builders Reference
> Consolidated reference: all builder questions + rules + SKILL MAP.
> For individual source files: https://github.com/sharpenedknife/claude-document-generation

========================================================================
PRODUCT — QUESTIONS
========================================================================

# Product Builder — Intake Questions
**Use when:** User wants to build a product, app, SaaS, tool, or any software system.
**Output:** Implementation-ready bundle — docs + dev plan + starter prompt + project scaffold.

---

## How Intake Works — Flexible Context Collection

This builder does NOT require rigid Q1–Q8 answers. Users can provide context however they want:

- **Answer questions** one at a time when prompted
- **Paste freeform context** — existing specs, PRDs, design docs, competitor analysis, notes, braindumps
- **Upload files** — screenshots, wireframes, existing code, spreadsheets
- **Mix and match** — answer some questions, paste some context, skip the rest

Claude dynamically assesses whether it has enough context to generate quality docs. No question is mandatory — but more context = better docs.

---

## Context Assessment — Dynamic Sufficiency Check

Before generating, Claude evaluates the available context against these tiers:

### Tier 1 — Minimum Viable Context (can generate, with heavy defaults)
- [ ] **What it is** — at least a sentence describing the product
- [ ] **Who it's for** — some indication of the target user

If only Tier 1 is met: warn the user.

> "I have a basic idea of what you want to build, but I'm missing a lot of context. I'll fill gaps with smart defaults and assumptions — but the docs will be more generic. Specifically, I'll need to assume:
> - [list each assumption: stack, features, user flows, etc.]
>
> Want me to proceed with these defaults, or would you like to add more detail first?"

### Tier 2 — Solid Context (good generation, some defaults)
Everything in Tier 1, plus:
- [ ] **Core features** — at least 2-3 things the product does
- [ ] **Tech stack** — specified or enough info to recommend one

If Tier 2 is met: note any remaining defaults but proceed with confidence.

> "I have a solid picture. I'll assume [list 2-3 defaults] unless you tell me otherwise. Generating now."

### Tier 3 — Full Context (best possible output)
Everything in Tier 2, plus:
- [ ] **User flows** — how users move through the product
- [ ] **Data entities** — what the product stores
- [ ] **Integrations** — external services
- [ ] **Existing code** — if any
- [ ] **AI tool preference** — what they'll build with

Tier 3 = maximum doc quality, fewest assumptions.

---

## Conversational Question Guide

Use these questions to fill gaps — but only ask what's missing. If the user already provided the info (in freeform context, uploaded files, or earlier answers), don't re-ask.

### Opening — Context Gate

Start every product intake with:

> "Tell me what you want to build. You can describe it in a few sentences, paste existing notes or specs, or just braindump — I'll figure out what I need."

If the user provides rich context upfront, skip to whatever questions remain unanswered. If they give a brief description, use the questions below to fill gaps.

---

### Q1 — Product One-Liner
**Ask when:** You can't summarize what it is in one sentence.
**Ask:** "Give me the one-liner: '[Product] helps [user] to [outcome] by [differentiator].' Fill in the blanks."
**Why:** Every doc opens with this. Fuzzy one-liner = fuzzy docs.
**Default if skipped:** Synthesize from whatever context exists. State the synthesis back to the user.

---

### Q2 — MVP Scope
**Ask when:** You don't know the core features.
**Ask:** "List the features you want in the MVP — the smallest version that delivers real value. Maximum 5."
**Why:** Dev plan phases map to features. Unbounded scope = docs that don't end.
**Default if skipped:** Infer 3-5 features from the description. Flag them as inferred.

---

### Q3 — Target Users and Core Flows
**Ask when:** You don't know who uses it or how they use it.
**Ask:** "Who are the 1–2 types of users? For each, describe the most important thing they do — one complete flow from landing to value."
**Why:** Data schema and API design follow user flows. Wrong flows = wrong schema.
**Default if skipped:** Infer a single user type from the product description. Generate a basic happy-path flow. Mark as "INFERRED — verify with stakeholder."

---

### Q4 — Data Entities
**Ask when:** You can't list what the product stores.
**Ask:** "What are the main 'things' your product stores and manages? Example: a task manager has Users, Tasks, Projects, Comments."
**Why:** Entities define the entire backend.
**Default if skipped:** Derive entities from features and flows. Always include Users. Mark derived entities as "INFERRED."

---

### Q5 — Tech Stack
**Ask when:** No stack mentioned and can't be inferred from existing code.
**Ask:** "What tech stack do you want to use? If you're not sure, tell me your team's background and I'll recommend."
**Recommendations if unknown:**
- Web app (non-technical founder, fast MVP): Next.js + Supabase + Vercel
- Web app (engineering team): Next.js + PostgreSQL + Node API + Docker
- Mobile: React Native + Expo + Supabase
- AI-native product: Next.js + Python FastAPI + PostgreSQL + OpenAI/Claude SDK
**Default if skipped:** Recommend based on product type + user signals. State the recommendation clearly.

---

### Q6 — Key Integrations
**Ask when:** Product clearly needs external services but none mentioned.
**Ask:** "Are there any external services this product must connect to? Examples: Stripe (payments), Auth0 (auth), SendGrid (email), OpenAI (AI)."
**Default if skipped:** Assume no integrations unless features imply them (e.g., "payments" implies Stripe or equivalent — flag assumption).

---

### Q7 — AI Coding Tool
**Ask when:** User hasn't mentioned what they'll build with.
**Ask:** "Which AI coding tool will you use to build this? Claude Projects, Cursor, Windsurf, Codex, or something else?"
**Default if skipped:** Assume Cursor. Note assumption in CLAUDE.md and Starter Prompt.

---

### Q8 — Existing Code
**Ask when:** Unclear if starting from scratch.
**Ask:** "Are you starting from scratch, or is there an existing codebase?"
**Default if skipped:** Assume new project (start from scratch).

---

## Custom Context Intake

When the user pastes freeform context (specs, notes, braindumps, competitor analysis, design docs), extract and map to the question fields:

1. **Parse** the pasted context for relevant information
2. **Map** extracted info to Q1–Q8 fields
3. **Show** what you extracted: "From your notes, I got: [product name], [features], [stack hint]. Still missing: [gaps]."
4. **Ask** only the remaining gaps — or offer to proceed with defaults

For uploaded files:
- **Screenshots/wireframes** → extract implied features, user flows, UI patterns
- **Existing code** → extract stack, file structure, entities, existing features
- **Spreadsheets/docs** → extract requirements, feature lists, priorities

---

## Context Confirmation (before generating)

Before generating, present the full context map — showing what's confirmed vs. assumed:

> "Here's what I'm working with:
>
> **Confirmed (from your input):**
> - Product: [one-liner]
> - Features: [list]
> - Stack: [if provided]
>
> **Assumed (I'll use these defaults):**
> - Stack: [recommended] — ASSUMED
> - User flows: [inferred] — INFERRED
> - Data entities: [derived] — INFERRED
> - AI tool: Cursor — DEFAULT
>
> **Output bundle:** 11 docs (PRD → UX → UI → Vision → Architecture → Data Schema → API Spec → Setup → Dev Plan → CLAUDE.md → Starter Prompt)
>
> Every ASSUMED/INFERRED item will be marked in the generated docs so you can verify and adjust.
>
> Proceed, or want to fill in more detail first?"

Generate only after explicit confirmation.

---

## Output Bundle (always deliver all of these)

**Generation order matters** — each doc informs the next.

| # | File | Purpose | Depends on |
|---|---|---|---|
| 1 | `PRD_{name}_v1.0.md` | Product requirements: features, acceptance criteria, out-of-scope | Intake context |
| 2 | `UX_{name}_v1.0.md` | User journeys: personas, flows, edge cases | PRD |
| 3 | `UI_{name}_v1.0.md` | Interface requirements: screen list, components, states | UX |
| 4 | `PRODUCT_Vision_{name}_v1.0.md` | One-liner, success metrics, constraints | PRD |
| 5 | `ARCH_System_{name}_v1.0.md` | Tech stack, file/folder structure, component diagram | PRD + UX |
| 6 | `DATA_Schema_{name}_v1.0.md` | All entities, fields, types, relationships | ARCH |
| 7 | `API_Spec_{name}_v1.0.md` | All endpoints, request/response shapes, auth | DATA + ARCH |
| 8 | `SETUP_Environment_{name}_v1.0.md` | Dependencies, env vars, local dev setup, deployment | ARCH |
| 9 | `DEV_Plan_{name}_v1.0.md` | **Always last.** Phases → tasks → files → acceptance criteria | All above |
| 10 | `CLAUDE.md` | For the **new project** (not docgen) — under 300 lines | DEV_Plan |
| 11 | `STARTER_PROMPT_{name}.md` | Paste verbatim into AI tool to begin building | All above |

Delivered as: `{ProductName}_Implementation_Bundle_v1.0_{YYYY-MM-DD}.zip`

---

## Assumption Marking Standard

Every inferred or defaulted value in generated docs MUST be visually marked:

```markdown
<!-- ASSUMED: No tech stack specified. Defaulting to Next.js + Supabase + Vercel based on product type (web SaaS, solo founder). Change this if you have a different stack preference. -->
```

And inline:
```markdown
**Tech Stack** *(ASSUMED)*: Next.js 14 (App Router) + Supabase (auth + DB) + Vercel (deploy)
```

This lets the user scan all assumptions quickly and decide what to override.

---

## Post-Delivery: Evaluate and Rerun

After delivering the bundle, always ask:

> "Review the docs and let me know:
> - Which docs need more detail?
> - Anything missing or wrong in the dev plan?
> - Does the starter prompt give the AI everything it needs?
> - Any **ASSUMED** or **INFERRED** items you want to change?
>
> You can say 'redo [doc name]' with specific feedback and I'll regenerate just that doc."

Rerun rules:
- Regenerate the specific doc only — don't regenerate the full bundle unless explicitly asked
- Incorporate feedback precisely — quote back what changed
- Re-run quality gates on the regenerated doc before delivering
- Update the zip after any rerun


========================================================================
PRODUCT — RULES
========================================================================

# Product Builder — Rules
**Applies to:** All docs generated via `builders/product/`.
**Authority:** `SYSTEM_Exit_Rules.md` > `SYSTEM_Content_Guide.md` > this file.

---

## Rule 0 — Skill-First Generation

Every doc in the bundle follows this 3-step process:

**Step A — Check the SKILL MAP.** Find the current generation stage in the SKILL MAP (in REFERENCE_Builders.md, or `skills/SKILL_MAP.md` in Cowork). It tells you which skill to use.

**Step B — Apply the skill.**
- *Cowork / Claude Code:* Call the skill using the Skill tool. Pass the intake context as input. Use the skill's output as the raw draft.
- *Claude.ai Chat:* Skills aren't callable. Apply the domain expertise the skill represents. Example: SKILL_MAP says "call `skills-library:architecture-designer`" → generate the architecture doc using system design patterns, scalability tradeoffs, and file structure conventions appropriate to the tech stack. The skill name tells you WHAT expertise to bring.
- *No matching skill:* Generate from DOC_CANONICAL_TEMPLATE directly.

**Step C — Quality gates.** Format the draft per DOC_CANONICAL_TEMPLATE. Run all 5 gates. The skill output is a starting point, not a finished doc.

**Stack-specific skills are mandatory** at Architecture, Setup, Dev Plan, and Starter Prompt stages. When the user picks a tech stack (Q5), look up the corresponding framework skill in the SKILL MAP stack table. Apply it alongside the stage skill. Skipping the stack skill = the generated docs will have generic file paths and config instead of framework-correct ones.

---

## Rule 1 — Never Hallucinate Facts or Decisions

**This is the highest-priority content rule.** Generated docs must NEVER contain fabricated facts, invented requirements, or assumed decisions presented as confirmed.

**What counts as hallucination:**
- Inventing features the user didn't mention and presenting them as requirements
- Making technical decisions (database choice, API design, auth method) without either user input or explicit default-marking
- Adding user flows, personas, or use cases not grounded in the user's context
- Citing specific performance numbers, market data, or statistics without source
- Writing acceptance criteria for features that don't exist in the confirmed scope

**What to do instead:**
- If a fact is missing and required for the doc: **stop and ask the user**
- If a decision can be reasonably defaulted: **mark it as ASSUMED** and explain the reasoning
- If a section can't be written without information the user hasn't provided: **write a placeholder** that says exactly what's needed:

```markdown
<!-- NEEDS INPUT: This section requires [specific information].
     Ask the user: "[exact question to ask]"
     Cannot be defaulted because: [why this needs real input] -->
```

- If you're unsure whether something is confirmed or inferred: **treat it as inferred** and mark it

**The test:** Could the user read every statement in the generated docs and say "yes, that's what I said or approved"? If not, it's either hallucinated or needs an ASSUMED/INFERRED marker.

---

## Rule 2 — Context Sufficiency Warning

Before generating any docs, assess context completeness using the tier system in BUILDER_Questions.md.

**If Tier 1 only (minimal context):**
- MUST warn the user before proceeding
- MUST list every assumption that will be made
- MUST get explicit permission: "proceed with defaults" or "let me add more context"
- Generated docs will have frequent ASSUMED/INFERRED markers

**If Tier 2 (solid context):**
- Note remaining defaults briefly
- Can proceed after showing the generation plan

**If Tier 3 (full context):**
- Proceed with generation plan confirmation

**At any tier:** If the user says "proceed" or "go ahead" — generate. Never block a user who wants to move forward. But the warnings ensure informed consent.

---

## Rule 3 — Smart Defaults with Transparency

When the user skips a question or provides incomplete context, apply these defaults:

| Missing Info | Default | Reasoning |
|---|---|---|
| Tech stack | Next.js + Supabase + Vercel | Most common for solo/small team web SaaS |
| AI tool | Cursor | Most popular AI coding tool |
| Auth | Supabase Auth (email + OAuth) | Integrated with default DB recommendation |
| Deployment | Vercel | Zero-config for Next.js |
| User types | Single user type, derived from product description | Simplest valid assumption |
| Data entities | Inferred from features + always includes Users | Users entity is universal |
| Integrations | None unless features imply them | Conservative — don't add complexity |
| Existing code | New project | Start fresh is the common case |

**Every default MUST be:**
1. Stated in the Context Confirmation before generation
2. Marked inline in the generated doc with `*(ASSUMED)*` or `*(INFERRED)*`
3. Accompanied by a brief reasoning comment
4. Overridable — if the user says "change X to Y", regenerate affected docs

---

## Rule 4 — Dev Plan Is Always Generated Last

The DEV_Plan doc synthesizes every other doc in the bundle. It cannot be written until ARCH, DATA, API, and SETUP are complete and reviewed. Any doc generated before its dependencies = quality gate fail.

Generation order: PRD → UX → UI → Vision → Architecture → Data Schema → API Spec → Environment Setup → **Dev Plan** → CLAUDE.md → Starter Prompt.

Never deviate from this order.

---

## Rule 5 — Dev Plan Phases Must Reference Specific Files

Every task in every phase must name:
- The exact file to create or modify (e.g., `src/models/user.ts`, `migrations/001_users.sql`)
- The acceptance criterion — a testable statement (passes test / endpoint returns 200 / UI renders component)
- The phase dependency — what must be complete before this phase starts

Vague tasks like "build the authentication system" = Gate 3 fail. Rewrite as:
- "Create `src/lib/auth.ts` — implements `signIn()`, `signOut()`, `getSession()`. Acceptance: `auth.test.ts` passes all 3 cases."

---

## Rule 6 — Phase 0 Always Exists

Every dev plan starts with Phase 0: Project Setup. It covers:
- Repository initialization (commands copy-pasteable)
- Dependency installation (`package.json` or `requirements.txt` contents)
- Environment variable setup (`.env.example` with all keys, no values)
- Local dev server verification (command + expected output)

Phase 0 must be completable by a developer in under 30 minutes. If it's longer, split it.

---

## Rule 7 — Starter Prompt Is Self-Contained

The starter prompt must work when pasted verbatim into a fresh AI session with zero prior context. It includes:
- What is being built (one-liner)
- What files are provided (list every file in the bundle)
- Explicit instruction to read CLAUDE.md first
- The first concrete task (Phase 0, Task 1 from the dev plan)
- A constraint: "Follow the dev plan phases in order. Ask before deviating."

Test: if you removed every other doc and only gave the AI the starter prompt, could it at minimum set up the project? If not, the starter prompt is incomplete.

---

## Rule 8 — CLAUDE.md Is for the New Project, Not Docgen

The CLAUDE.md in the output bundle is written for the product being built, not for this documentation system. It follows the standard structure: What This Is / Commands / Architecture / Code Style / Important Notes. Under 300 lines. Version stamped.

Do not copy the docgen CLAUDE.md into the bundle.

---

## Rule 9 — Tech Stack Must Be Fully Specified

No doc in the bundle may say "use your preferred database" or "choose an appropriate framework." Every technology decision must be explicit:
- Frontend: framework + version
- Backend: runtime + framework + version
- Database: type + name + ORM/client
- Auth: provider + method
- Deployment: platform + config

If the user hasn't decided, apply smart defaults (Rule 3) and mark as ASSUMED.

---

## Rule 10 — File Structure Is Declared in Architecture Doc

The ARCH doc must contain the complete top-level folder structure for the project. Not a general diagram — the actual intended directory tree, with a one-line comment on every folder.

The dev plan's task list must reference this exact structure. Discrepancies between ARCH and DEV_Plan = Gate 3 fail.

---

## Rule 11 — MVP Scope Is Frozen at Intake

Once the user confirms the MVP feature list, the entire bundle scopes to those features only. If the user asks to add features during generation, pause and ask: "Do you want to add this to the MVP scope? This will require updating the architecture, schema, API spec, and dev plan before I continue."

Never silently expand scope mid-generation.

---

## Rule 12 — Every Integration Gets an Environment Variable

Every external service mentioned in intake must appear in:
- `SETUP_Environment.md` → API Keys section
- `.env.example` → the scaffold file
- `ARCH_System.md` → Integrations section
- `DEV_Plan.md` → the phase that wires it up

A service mentioned in the architecture but missing from the environment setup = Gate 2 fail.

---

## Rule 13 — Quality Score Target Is 90/100 for Product Bundles

Product bundles are directly used by AI agents for code generation. The standard 85/100 minimum is insufficient. The higher bar applies because:
- Partial or ambiguous docs cause the AI coding agent to hallucinate implementation details
- A wrong architecture decision early compounds through every subsequent file
- Missing acceptance criteria means the agent doesn't know when a phase is done

Gate 4 checklist additions for product bundles:
- [ ] Dev plan covers 100% of MVP features (nothing left undocumented)
- [ ] Every phase has ≥1 testable acceptance criterion
- [ ] Starter prompt tested mentally: can AI complete Phase 0 from prompt alone?
- [ ] CLAUDE.md is ≤300 lines and correctly describes the new project (not docgen)
- [ ] `.env.example` contains all keys referenced in all docs
- [ ] No hallucinated features, decisions, or facts (Rule 1 compliance)
- [ ] All ASSUMED/INFERRED items are marked (Rule 3 compliance)

---

## Rule 14 — Deliver Two Bundle Formats

The output bundle must be usable in both Claude.ai chat (flat file upload) and Claude Code / Cowork (folder structure). Generate two delivery options:

**Option A — Full bundle (Cowork / Claude Code / Cursor):**
Individual files in a folder: `PRD.md`, `UX.md`, `UI.md`, `ARCH_System.md`, `DATA_Schema.md`, `API_Spec.md`, `SETUP_Environment.md`, `DEV_Plan.md`, `CLAUDE.md`, `STARTER_PROMPT.md`. Each file standalone.

**Option B — Chat bundle (Claude.ai Projects):**
Consolidate into 3 files for easy upload with no naming conflicts:
- `CONTEXT_Product.md` — merges PRD + UX + UI + Vision (what to build)
- `CONTEXT_Technical.md` — merges Architecture + Data Schema + API Spec + Setup (how to build it)
- `IMPLEMENTATION.md` — merges Dev Plan + CLAUDE.md + Starter Prompt (execute the build)

Both options go in the zip. Chat users upload 3 files. Code users use the full folder.


========================================================================
CLAUDE PROJECT — QUESTIONS
========================================================================

# Builder: Claude Project Setup

**Domain:** `claude-project`
**Use when:** Someone has an idea and needs a full Claude project generated from scratch — CLAUDE.md, project instructions, system guides, folder structure, knowledge base file list.

---

## How Intake Works — Flexible Context Collection

No question is mandatory. Users can provide context however they want — answer questions, paste existing notes, describe the idea freeform, or upload reference materials. Claude dynamically assesses whether enough context exists to generate quality output.

---

## Context Assessment

### Tier 1 — Minimum (can generate, heavy defaults)
- [ ] **What Claude does** — at least a sentence describing the project purpose

Warn: "I have the basic idea but will need to assume the user type, key tasks, output formats, and quality standards. Want me to proceed with defaults, or add more detail?"

### Tier 2 — Solid (good generation)
Everything in Tier 1, plus:
- [ ] **Who uses it** — primary user type
- [ ] **Key tasks** — at least 2-3 things Claude will do

### Tier 3 — Full (best output)
Everything in Tier 2, plus: domains, connected tools, output types, quality requirements.

---

## Conversational Question Guide

Use these to fill gaps — only ask what's missing from the user's input.

### Opening
> "Tell me about the Claude project you want to build. What should Claude do, and who will use it? You can describe it however you like — freeform, bullet points, or paste existing notes."

---

**Q1: Project Name**
**Ask when:** User hasn't named the project.
**Ask:** "What's the name of this Claude project?"
**Default if skipped:** Derive from the purpose description.

**Q2: Core Purpose**
**Ask when:** You can't summarize what Claude does in this project.
**Ask:** "Describe the project in 1–3 sentences. What will Claude do? What problem does it solve?"
**Default if skipped:** Cannot default — this is the minimum Tier 1 context. Ask again.

**Q3: Primary User**
**Ask when:** You don't know who uses this.
**Ask:** "Who will use this project day-to-day? Are they technical?"
**Default if skipped:** Infer from purpose. Mark as INFERRED.

**Q4: Key Tasks**
**Ask when:** You can't list what Claude will do.
**Ask:** "List the top 3–5 tasks Claude will perform. Be specific."
**Default if skipped:** Infer from purpose. Mark as INFERRED.

**Q5: Domains / Topics**
**Ask when:** Subject areas are unclear.
**Ask:** "What subject areas does this project touch?"
**Default if skipped:** Infer from tasks.

**Q6: Connected Tools**
**Ask when:** Project likely needs external connections.
**Ask:** "Will this project connect to external tools via MCP?"
**Default if skipped:** Assume none.

**Q7: Output Types**
**Ask when:** Output format matters for the project.
**Ask:** "What types of outputs should Claude produce?"
**Default if skipped:** Assume markdown docs + inline chat responses.

**Q8: Quality Requirements**
**Ask when:** User hasn't mentioned standards.
**Ask:** "Any specific quality gates, review processes, or standards Claude must follow?"
**Default if skipped:** Assume general quality guidelines, no special gates.

---

## Context Confirmation

Before generating, show confirmed vs. assumed:

> "Here's what I'm working with:
> **Confirmed:** [items from user input]
> **Assumed:** [defaults with reasoning]
>
> Generating: CLAUDE.md, Project Instructions, System Guide, Domain Config, Token Budgets, README
> Proceed?"

---

## Outputs to Generate

Based on answers, generate in this order:

1. **`CLAUDE.md`** — Master navigation
2. **`system/guides/SYSTEM_Master_Index.md`** — Quick reference for the domain
3. **`system/templates/project_instructions/PROJECT_INSTRUCTIONS_[Name].md`** — Project instructions
4. **`config/domain_definitions.json`** — Domain registry
5. **`config/token_budgets.json`** — Token budgets per doc type
6. **`README.md`** — Setup guide (3 steps: create project → sync folder → paste instructions)

---

## Generation Checklist

- [ ] Context assessed — tier identified, assumptions listed
- [ ] User confirmed generation plan (or said "proceed" with defaults)
- [ ] CLAUDE.md is ≤ 200 lines
- [ ] Project instructions are 500–800 words
- [ ] Project instructions follow 6-section structure from `SYSTEM_Project_Instructions_Rules.md`
- [ ] All ASSUMED items marked in output
- [ ] No hallucinated content — everything traceable to user input or marked ASSUMED
- [ ] All outputs pass Gate 1 before delivery


========================================================================
CLAUDE PROJECT — RULES
========================================================================

# Rules: Claude Project Builder

**These rules govern all output from the claude-project builder.**

---

## CLAUDE.md Rules

1. **Max 200 lines.** Beyond this, compliance degrades. Prune ruthlessly.
2. **No content from SYSTEM_* files inline.** Tell Claude WHERE to find information — don't paste the content. Progressive disclosure.
3. **Required sections in order:**
   - What This Is (2 sentences)
   - Rules (max 5, numbered, action-verb each)
   - File Map (folder tree with ← annotations)
   - Quality Gate Cheat Sheet (table)
   - Authoritative File Priority (when files conflict)
   - How to Set Up the Claude Project (3 steps)
4. **File map annotations must be accurate.** Every folder and file in the map must actually exist in the workspace.
5. **No prose paragraphs.** Bullets, tables, code blocks only. This is a navigation document.

## Project Instructions Rules

Follow `SYSTEM_Project_Instructions_Rules.md` exactly. Key constraints:
- 500–800 words total
- 6 sections: Role → Context Interpretation → Response Format → Do's (5) → Don'ts (5) → Examples
- "Read CLAUDE.md first" must be Do #1
- 2–3 labeled examples (at least 1 GOOD, 1 BAD)
- Timestamp: `Last updated: [Month Year]`

## Domain Definitions Rules

- Only define domains that are ACTUALLY used in this project
- Do not carry over domains from other projects
- Each domain needs: name, description, doc_types[], primary_audience, priority, status

## Token Budget Rules

- Every doc type that could be generated in this project must have a budget
- Use `config/token_budgets.json` from this system as reference for reasonable ranges
- Do not set budgets higher than the reference unless justified in rationale field

## README Rules

- Exactly 3 steps: (1) Create project on claude.ai, (2) Sync folder, (3) Paste project instructions
- Link to exact file paths for steps 2 and 3
- Include what the project will do in 2 sentences at the top

## Chat Bundle Rules

When the generated Claude Project has 4+ knowledge base files, also generate a consolidated `chat/` folder:
- `PROJECT_REFERENCE.md` — all knowledge base docs merged into one file with clear section headers
- `CLAUDE.md` — standalone (already a single file, no merge needed)
- `PROJECT_INSTRUCTIONS.md` — standalone (paste into instructions field)

This gives the user two setup paths:
- **Full folder:** Upload all individual files to the knowledge base
- **Chat bundle:** Upload just `CLAUDE.md` + `PROJECT_REFERENCE.md`, paste `PROJECT_INSTRUCTIONS.md`

Include both paths in the README.


========================================================================
SKILL — QUESTIONS
========================================================================

# Builder: Skill / Slash Command

**Domain:** `claude-project`
**Use when:** Someone needs a repeatable, structured workflow — a `/command`, a trigger phrase, or an autonomous invocation pattern. Output is a `SKILL.md` file (with optional supporting directories) packaged as a `.skill` file.

---

## Before You Ask Anything

Read `system/guides/SYSTEM_Build_Decision_Framework.md` → "Skill signals" to confirm this is the right builder.

Check existing skills first. With 341+ skills available across 14 categories, the skill the user needs may already exist. Ask: "Have you checked the skills library? What skill name or category might cover this?" Don't build what's already built.

**Skill vs Claude Project vs MCP:**
- Skill = structured playbook Claude follows for a specific recurring task (output: SKILL.md + `.skill` file)
- Claude Project = persistent knowledge base + persona (broader scope, many sessions)
- MCP = live connection to an external system (actions/data in real tools)

---

## The Most Important Thing to Get Right: The Description

The `description` field in SKILL.md frontmatter is the **primary triggering mechanism**. Claude sees all installed skill names and descriptions in its system prompt and decides whether to read the full skill body based on these alone.

**Critical finding:** Claude under-triggers by default — it tends not to consult skills for tasks it thinks it can handle alone. Descriptions must be slightly "pushy" and enumerate specific trigger contexts.

Spend as much time on the description as on the rest of the skill body combined.

---

## How Intake Works — Flexible Context Collection

No question is mandatory. Users can describe their skill idea however they want — freeform, with examples, by uploading an existing workflow, or by answering structured questions. Claude assesses what's needed and asks only for the gaps.

---

## Context Assessment

### Tier 1 — Minimum (can generate basic skill)
- [ ] **What the skill does** — at least a clear description of the task it automates

Warn: "I can build a basic skill from this, but I'll need to assume the trigger description, input/output format, and process steps. The skill may not trigger correctly without a refined description. Want me to proceed, or add more detail?"

### Tier 2 — Solid (good skill)
Everything in Tier 1, plus:
- [ ] **Trigger contexts** — when/how Claude should invoke this
- [ ] **Input/Output** — what goes in, what comes out

### Tier 3 — Full (production-quality skill)
Everything in Tier 2, plus: detailed process steps, error handling, edge cases, happy-path example.

---

## Conversational Question Guide

Use these to fill gaps — only ask what's missing.

### Opening
> "Tell me about the skill you want to build. What recurring task should it automate? You can describe it freeform, show me an example of the task being done manually, or paste an existing workflow."

---

**Q0: Does this skill already exist?**
**Ask when:** Always — before building anything.
**Ask:** "Describe the task in 1-2 sentences. I'll check whether an existing skill covers this."
**Default if skipped:** Check anyway based on the description provided.

**Q1: Skill Name & Trigger**
**Ask when:** User hasn't named it or specified invocation.
**Ask:** "What will this skill be called? Slash command (`/name`), keyword trigger, or autonomous?"
**Default if skipped:** Derive name from the task description.

**Q2: What Problem Does It Solve?**
**Ask when:** The "why" isn't clear.
**Ask:** "What specific, recurring task does this skill handle?"
**Default if skipped:** Infer from context.

**Q3: Trigger Description (The Critical One)**
**Ask when:** You don't have enough for a strong description field.
**Ask:** "How should Claude know to use this skill? Give me the primary action + 3-5 specific phrases that should trigger it."
**Default if skipped:** Generate a description from the task description. Warn: "I've generated a trigger description but it may under-trigger. Review and refine it."

**Q4: Input**
**Ask when:** What the user provides is unclear.
**Ask:** "What information does the user give when invoking this skill? Required vs optional?"
**Default if skipped:** Infer from the task. Mark as INFERRED.

**Q5: The Process**
**Ask when:** You can't write the step-by-step procedure.
**Ask:** "What should Claude do, in order, after receiving the input?"
**Default if skipped:** Infer a basic process. Mark as INFERRED. Warn: "I've inferred the process steps — review carefully."

**Q6: Output**
**Ask when:** Deliverable format is unclear.
**Ask:** "What does the user get? Format, structure, length, saved to file or inline?"
**Default if skipped:** Assume inline markdown response. Mark as ASSUMED.

**Q7: Supporting Resources**
**Ask when:** Skill likely needs reference files, scripts, or MCP tools.
**Ask:** "Does this skill need reference files, scripts, or MCP connections?"
**Default if skipped:** Assume no supporting resources.

**Q8: Happy Path Example**
**Ask when:** No example provided.
**Ask:** "Show me one complete example: User says [X] → Claude does [Y] → User gets [Z]."
**Default if skipped:** Generate an example from the context. Mark as INFERRED.

---

## Outputs to Generate

1. **`skills/{name}/SKILL.md`** — YAML frontmatter + skill body (required)
2. **`skills/{name}/references/{topic}.md`** — reference files loaded on demand (if needed)
3. **`skills/{name}/scripts/`** — executable scripts for deterministic tasks (if needed)
4. **`skills/{name}/evals.json`** — 3-10 test prompts for trigger and output testing (always generate)

Packaging into `.skill` file: `python -m scripts.package_skill skills/{name}/`

---

## SKILL.md Required Structure

```markdown
---
name: skill-identifier
description: >
  [Primary action verb] + [what it does] + [when to use it].
  Include specific trigger contexts, file types, user phrases.
  Be slightly pushy — err toward triggering more than less.
  50-120 words. This field alone controls whether Claude reads this skill.
---

# Skill Name

One-sentence summary.

## When to Use This Skill
[Only if description couldn't cover everything]

## Prerequisites / Dependencies
[Tools, MCP connections, or context required. Define fallbacks if MCP unavailable.]

## Procedure

### Step 1 — [Name]
[Exact instructions. What Claude does. What it produces by end of step.]

### Step 2 — [Name]
[...]

## Output Format
[Exact structure, format, length of the deliverable.]

## Error Handling
[What Claude does when input is missing, malformed, or tools are unavailable.]

## Edge Cases
[Specific known edge cases and how to handle them.]

## Examples
<example>
[One complete happy-path: input → steps → exact output]
</example>

## See Also
- `references/topic.md` — [when to read this]
```

---

## Generation Checklist

- [ ] Existing skill library checked — not duplicating existing skill
- [ ] Context assessed — tier identified, assumptions listed
- [ ] User confirmed generation plan
- [ ] Description field: 50-120 words, starts with action verb, lists 3-5 trigger contexts, slightly pushy
- [ ] Body: under 500 lines — large reference material moved to `references/` subdirectory
- [ ] Every procedure step states what it produces
- [ ] Output format specific enough that two AIs produce identical structure
- [ ] Error handling covers: missing input, unavailable MCP, malformed data
- [ ] Happy-path example is complete and specific
- [ ] No hallucinated content — process steps traceable to user input or marked INFERRED
- [ ] `evals.json` created with 3-10 test prompts
- [ ] Passes Gate 2 (structure complete) and Gate 3 (no vague steps)


========================================================================
SKILL — RULES
========================================================================

# Builder Rules: Skill / Slash Command

**Applies to:** All SKILL.md files and supporting skill assets
**Authority:** After `SYSTEM_Exit_Rules.md` and `SYSTEM_Content_Guide.md`.
**Source:** Skills Manager project instructions + community skill authoring best practices

---

## Rule 1: The Description Is the Skill

The `description` YAML frontmatter field is the **only thing Claude reads** before deciding whether to load the full skill. Everything else — the body, procedures, examples — is irrelevant if the description fails to trigger.

**Description requirements:**
- 50–120 words (hard limits — too short doesn't trigger, too long wastes context)
- Starts with a primary action verb: "Creates", "Analyzes", "Drafts", "Converts", "Builds"
- States WHAT the skill does AND WHEN to use it
- Lists 3–5 specific trigger phrases or contexts
- Uses "whenever" or "always use when" at least once
- Is slightly pushy — Claude under-triggers by default, so descriptions must compensate

```yaml
# BAD — only says what, not when:
description: Creates charts from data.

# BAD — too vague:
description: Helps with documents.

# BAD — too narrow:
description: Only for .docx files with tracked changes when the user says "review".

# GOOD — what + when + slightly pushy:
description: >
  Creates charts and data visualizations from spreadsheets, CSVs, or raw numbers.
  Use this whenever the user mentions charts, graphs, plotting, visualizing data,
  or asks to "show" numerical data — even if they don't say "chart" explicitly.
  Always use this skill when the user shares tabular data and wants to understand
  trends, comparisons, or distributions.
```

---

## Rule 2: SKILL.md Body Is a Playbook, Not a Description

Every sentence in the body must be an instruction Claude can follow — not a description of what Claude might do.

**Bad:** "Claude will help the user with their campaign planning needs."
**Good:** "Ask: What is the campaign goal? (brand awareness / lead gen / product launch). Wait for answer before proceeding to Step 2."

Body must be **under 500 lines**. If you're approaching the limit, move reference material to `references/` files and link them with guidance on when to read them.

---

## Rule 3: Directory Structure

```
skill-name/
├── SKILL.md              ← required
├── scripts/              ← optional; Python/bash for deterministic tasks
├── references/           ← optional; docs loaded into context on demand
├── assets/               ← optional; templates, fonts, icons
└── evals.json            ← always generate; 3-10 test prompts
```

Reference files in `references/` should be linked from SKILL.md with a "See Also" section that says WHEN to read each one — not just that it exists.

---

## Rule 4: Intake Must Be Gated

The skill must not produce output until minimum required inputs are collected. Mark optionals clearly.

```markdown
## Procedure

### Step 1 — Collect Inputs
Required before proceeding:
- [ ] [Input 1] (required) — ask: "[exact question to user]"
- [ ] [Input 2] (required) — ask: "[exact question]"
- [ ] [Input 3] (optional) — ask only if [condition]; default: [value]

If any required input is missing, ask for it. Do not proceed with placeholders.
```

---

## Rule 5: Every Procedure Step Has an Expected Output

```markdown
# BAD:
### Step 2 — Research the company.

# GOOD:
### Step 2 — Research Company Context
Search web for "[company] recent news" and "[company] product focus".
Output: 3-5 bullet points covering funding, product direction, and recent launches.
If no results found: note "no recent news found" and proceed to Step 3 with available info.
```

---

## Rule 6: Error Handling Is Mandatory

Every skill must define what Claude does when things go wrong. No skill ships without an Error Handling section.

Required error scenarios to cover:
- Required input is missing or malformed
- MCP tool is unavailable or returns an error (define the fallback)
- External search returns no results
- Generated output doesn't match expected format

```markdown
## Error Handling

**Missing required input:** Ask once. If still not provided after second ask, tell user what
you need and stop: "I need [X] to proceed. Please provide it and I'll continue."

**MCP unavailable:** If [tool] is not connected, fall back to: [specific alternative behavior].
Never silently fail — always tell the user what you're doing instead.

**No search results:** Note it explicitly: "Found no recent information on [X]."
Continue with available context rather than inventing data.
```

---

## Rule 7: The Example Is the Most Valuable Part

The `<example>` block in the skill body is what makes the skill immediately usable and testable. It must be:
- A specific, realistic scenario (not "user asks for X and Claude helps")
- Complete: trigger → every step → exact output shown
- Wrapped in `<example>` XML tags

If you can't write a complete example, the skill is underspecified — go back and clarify the procedure.

---

## Rule 8: Always Generate evals.json

Every skill output must include an `evals.json` with test prompts. Minimum 3, target 5-10.

```json
{
  "skill": "skill-name",
  "test_prompts": [
    {
      "id": "core-use-case",
      "prompt": "[Realistic user input for the main use case]",
      "should_trigger": true,
      "expected_output_contains": ["[key element 1]", "[key element 2]"]
    },
    {
      "id": "edge-case-1",
      "prompt": "[Input that tests an edge case]",
      "should_trigger": true,
      "expected_output_contains": ["[what should appear]"]
    },
    {
      "id": "should-not-trigger",
      "prompt": "[Input that looks similar but shouldn't use this skill]",
      "should_trigger": false
    }
  ]
}
```

Test prompts must be: substantive (not trivially simple), realistic user language (casual, messy, ambiguous), and cover core use case + at least 2 edge cases + 1 should-NOT-trigger case.

---

## Rule 9: Packaging

After generation and testing, package the skill:
```bash
python -m scripts.package_skill skills/{name}/
```

Present the resulting `.skill` file to the user for installation. Skills are installed by the user — do not attempt to install them directly.

---

## Rule 10: MCP Dependencies Must Be Declared and Fallback-Defined

```markdown
## Prerequisites / Dependencies

| Tool | MCP connector | Required for | Fallback if unavailable |
|---|---|---|---|
| Slack | slack-by-salesforce | Read channel messages | Draft message for user to send manually |
| Jira | atlassian | Create follow-up tickets | List action items for user to log manually |

If [MCP] is unavailable, Claude must [specific fallback behavior] and inform the user.
```

---

## Gate Applicability

| Gate | Applies? | Notes |
|---|---|---|
| Gate 1 (naming) | Yes | `skills/{name}/SKILL.md` |
| Gate 2 (structure) | Yes | YAML frontmatter + all required sections present |
| Gate 3 (content) | Yes | Description 50-120w, no vague steps, error handling present |
| Gate 4 (token budget) | Partial | Body under 500 lines; description under 120 words |
| Gate 5 (shipping) | Yes | evals.json present, version stamp in frontmatter |


========================================================================
MCP — QUESTIONS
========================================================================

# Builder: MCP Server

**Domain:** `reference` (MCP docs are operational reference, not AI-project docs)
**Use when:** Someone needs to document, set up, or help Claude connect to an external system via Model Context Protocol.

---

## Before You Ask Anything

Read `system/guides/SYSTEM_Build_Decision_Framework.md` → "MCP Server signals" to confirm this is the right builder.

**MCP vs Skill vs Claude Project:**
- MCP = live data + actions in external systems (Slack, Jira, databases, APIs)
- Skill = structured Claude workflow (no live external connection)
- Claude Project = persistent knowledge + persona

If the user wants Claude to both know things AND connect to tools: build the Project first, then document the MCPs.

---

## How Intake Works — Flexible Context Collection

No question is mandatory. Users can provide context however they want — paste API docs, describe the integration freeform, share existing MCP configs, or answer structured questions. Claude assesses what's needed and asks only for the gaps.

---

## Context Assessment

### Tier 1 — Minimum (can generate basic setup guide)
- [ ] **What system to connect to** — name and type of external system

Warn: "I know the system but not the specifics of what Claude needs to read or do. I'll generate a setup guide but the API reference and auth sections will be generic. Want me to proceed, or add more detail about the specific operations?"

### Tier 2 — Solid (good documentation)
Everything in Tier 1, plus:
- [ ] **Read operations** — what data Claude needs
- [ ] **Write operations** — what actions Claude takes
- [ ] **Auth method** — how to authenticate

### Tier 3 — Full (production-ready docs)
Everything in Tier 2, plus: operator persona, environment, error scenarios, happy-path example.

---

## Conversational Question Guide

Use these to fill gaps — only ask what's missing.

### Opening
> "Tell me about the MCP integration you need. What external system should Claude connect to, and what should it read or do? You can paste API docs, describe it freeform, or share an existing config."

---

**Q1: System Name & Type**
**Ask when:** System isn't clear.
**Ask:** "What external system does this MCP connect to? Name, type, and docs URL if available."
**Default if skipped:** Cannot default — this is minimum Tier 1 context.

**Q2: What Claude Needs to Read**
**Ask when:** Read operations aren't specified.
**Ask:** "What data does Claude need to read from this system? Be specific."
**Default if skipped:** Infer from system type (e.g., Slack → messages, channels, users). Mark as INFERRED.

**Q3: What Claude Needs to Do (Actions)**
**Ask when:** Write operations aren't specified.
**Ask:** "What actions must Claude take in this system?"
**Default if skipped:** Assume read-only. Mark as ASSUMED.

**Q4: Authentication**
**Ask when:** Auth method unknown.
**Ask:** "How does the MCP authenticate? API key, OAuth, service account?"
**Default if skipped:** Infer from system type. Mark as ASSUMED.

**Q5: Who Operates It**
**Ask when:** Operator persona unclear.
**Ask:** "Who installs and runs this MCP server? Developer, ops, or end user?"
**Default if skipped:** Assume developer. Mark as ASSUMED.

**Q6: Environment**
**Ask when:** Deployment context unclear.
**Ask:** "Where does this MCP run? Local, cloud, or inside Cowork/Claude Code?"
**Default if skipped:** Assume local developer machine. Mark as ASSUMED.

**Q7: Error Scenarios**
**Ask when:** User hasn't mentioned failure modes.
**Ask:** "What are the most common failure modes?"
**Default if skipped:** Generate generic error scenarios (auth failure, rate limit, not found). Mark as INFERRED.

**Q8: Happy Path Example**
**Ask when:** No example provided.
**Ask:** "Describe a complete example: user says → MCP calls → Claude returns."
**Default if skipped:** Generate from context. Mark as INFERRED.

---

## Outputs to Generate

Based on answers, generate in this order:

1. **`{system}-setup-guide.md`** — Installation, authentication, environment setup, verification
2. **`{system}-api-reference.md`** — Every available tool/command with params, returns, errors
3. **`{system}-schema-reference.md`** *(if applicable)* — Data models, field definitions, types
4. **`{system}-auth-guide.md`** *(if complex auth)* — Separate auth doc for OAuth, service accounts, etc.
5. **`{system}-troubleshooting.md`** — Top 5–7 error signatures with root causes and fixes

---

## Generation Checklist

- [ ] Context assessed — tier identified, assumptions listed
- [ ] User confirmed generation plan
- [ ] System name and API/tool type identified
- [ ] Every read operation listed with field-level specifics (or marked INFERRED)
- [ ] Every write action listed with required inputs and confirmation behavior (or marked ASSUMED read-only)
- [ ] Auth method documented (or marked ASSUMED with best guess)
- [ ] Operator persona confirmed or defaulted
- [ ] At least one complete end-to-end example
- [ ] Error signatures are exact strings (not "some kind of auth error")
- [ ] No hallucinated content — all items traceable to user input or marked ASSUMED/INFERRED
- [ ] All outputs pass Gates 1–5 before delivery


========================================================================
MCP — RULES
========================================================================

# Builder Rules: MCP Server Documentation

**Applies to:** All MCP server documentation (setup guides, API references, schema docs, auth guides, troubleshooting)
**Authority:** These rules apply after `SYSTEM_Exit_Rules.md` and `SYSTEM_Content_Guide.md`.

---

## Rule 1: Every Tool/Command Must Be Fully Documented

The API reference must cover every available MCP tool. For each tool:

```markdown
### tool_name

**Purpose:** One sentence — what this tool does and why you'd call it.

**Parameters:**
| Parameter | Type | Required | Description |
|---|---|---|---|
| param_name | string | Yes | What it is, valid values, constraints |

**Returns:**
```json
{
  "field": "value",
  "description": "what this field contains"
}
```

**Example call:**
```json
{
  "tool": "tool_name",
  "params": { "param_name": "example_value" }
}
```

**Errors:**
| Error code / message | Root cause | Fix |
|---|---|---|
| "Not found" | Resource doesn't exist | Verify ID, check permissions |
```

No tool is documented with less than: purpose, params table, return shape, one example, error table.

---

## Rule 2: Auth Steps Must Be Runnable

Authentication documentation must include exact, runnable steps — not conceptual descriptions.

**Bad:**
> Obtain an API key from the provider and add it to your environment.

**Good:**
```markdown
### Step 1: Obtain API Key
1. Go to https://app.example.com/settings/api
2. Click "Generate new key"
3. Copy the key (shown once — store it now)
   Expected: key format is `sk-xxxxxxxxxxxxxxxxxxxx` (32 chars after `sk-`)

### Step 2: Configure Environment
1. Add to `.env`:
   ```
   EXAMPLE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
   ```
2. Verify: `echo $EXAMPLE_API_KEY` (should print your key, not blank)
```

---

## Rule 3: Error Signatures Must Be Exact Strings

Troubleshooting docs must use the actual error text that appears in logs or Claude's response — not paraphrases.

**Bad:** "If there's a permission error..."
**Good:** `"Error: Forbidden (403) — Missing scope: channels:read"`

To obtain exact strings: test the MCP, trigger the error, copy the output verbatim. If untested, mark as: `[DEBT: verify exact error signature — not yet tested]`.

---

## Rule 4: Rate Limits and Quotas Must Be Documented

Every API has limits. Document them explicitly:

```markdown
## Rate Limits

| Endpoint / Action | Limit | Reset period | Claude behavior when hit |
|---|---|---|---|
| Search messages | 50 req/min | Per minute | Wait 60s, retry once, then inform user |
| Create ticket | 100 req/hour | Per hour | Inform user, queue action for manual follow-up |
```

If rate limits are unknown: note this as DEBT. Do not omit the section.

---

## Rule 5: Actions Must Document Reversibility

For every write action, state whether it is reversible and what the revert process is.

```markdown
### createJiraIssue

**Reversibility:** Reversible
**How to undo:** Call `deleteJiraIssue` with the returned `issue_id`, or delete manually at [Jira issue URL].

**Caution:** Issues are visible to all project members immediately on creation. Notify relevant stakeholders if creating on their behalf.
```

Irreversible actions (deletes, sends) must include a confirmation step in the process docs:

```markdown
Before executing: confirm with user — "This will send a Slack message to #general. Proceed? (yes/no)"
```

---

## Rule 6: Fallback Behavior Must Be Defined

When an MCP is unavailable or returns an error, Claude must have explicit fallback instructions — not just error handling.

```markdown
## Fallback Behavior

If the Slack MCP is not connected or returns an error:
1. Inform user: "I can't reach Slack right now. I'll draft the message for you to send manually."
2. Generate the message in Slack mrkdwn format
3. Provide the channel name and suggested send time
```

"Try again later" is not a fallback. A fallback always delivers value to the user.

---

## Rule 7: Setup Guide Must End With a Verification Test

Every setup guide ends with a verification step that confirms the MCP is working:

```markdown
## Verify Setup

Run this command (or ask Claude to run it):
```
[exact verification command or Claude prompt]
```
Expected output:
```
[exact success output]
```

If you see this instead:
```
[exact failure output]
```
→ See Troubleshooting → [relevant error section].
```

---

## Rule 8: Operator Persona Drives Depth

The technical depth of every section must match the operator persona identified in Q5:

| Operator | Depth level |
|---|---|
| Developer | Full CLI commands, env var names, JSON configs, exact API call syntax |
| Ops/DevOps | Deployment configs, environment management, monitoring, log locations |
| End user | No terminal. Step-by-step GUI instructions, screenshots described, no raw JSON |

Do not mix depths within a single doc. If two operators need different docs, generate two docs.

---

## Gate Applicability

| Gate | Applies? | Notes |
|---|---|---|
| Gate 1 (naming) | Yes | `reference_{system}-{doctype}_v{X.Y}_{YYYY-MM-DD}.md` |
| Gate 2 (structure) | Yes | All required sections must be present per doc type |
| Gate 3 (content) | Yes | Error signatures exact, auth steps runnable, no vague fallbacks |
| Gate 4 (token budget) | Yes | `api-guide`: 3000 tokens · `setup-guide`: 2500 · `troubleshooting`: 2200 |
| Gate 5 (shipping) | Yes | Version stamp + all DEBTs logged before marking pass |


========================================================================
AI DOCS — QUESTIONS
========================================================================

# Builder: AI Documentation

**Domain:** `ai-docs`
**Use when:** Generating or updating a single document for an AI workflow, Claude project, or AI implementation. Also covers process docs, how-to guides, and feature docs.

Three modes:

1. **New doc from scratch** — Generate a complete doc for a new topic
2. **Update existing doc** — Improve, extend, or correct an existing document
3. **Gap-fill** — Add a missing section to an existing doc

---

## Mode 1: New Doc from Scratch

**Q1: Doc type?**
> Choose: `how-to` | `reference` | `feature` | `process` | `system-guide`

**Q2: What is this doc about?**
> Describe the topic in 1 sentence. What does the reader do or learn?

**Q3: Who reads this?**
> Audience: `beginner` | `intermediate` | `advanced` | `all`
> Are they human, AI system, or both?

**Q4: What must the reader already know or have?**
> List prerequisites. If none, say "none."

**Q5: What are the 3–5 main things this doc covers?**
> These become the main sections.

**Q6: Are there code examples?**
> If yes: What language? What does the code do? (Applies `SYSTEM_Coding_Standards.md`)

**Q7: What does success look like?**
> What can the reader do or verify after completing this doc?

---

## Mode 2: Update Existing Doc

**Q1: What is the file name of the existing doc?**
> Provide exact file path.

**Q2: What specifically needs to change?**
> Be precise: "Add error handling to Step 3", "Update model string to claude-sonnet-4-6", "Add prerequisites section"

**Q3: What gate(s) did this doc fail?**
> If you know — helps target the fix.

**Q4: Are there sections to preserve exactly?**
> List sections that must not change.

---

## Mode 3: Gap-Fill

**Q1: What doc is being extended?**
> Provide exact file path.

**Q2: What section is missing?**
> Describe the gap.

**Q3: What's the token budget remaining?**
> Check `config/token_budgets.json` for the doc type. New section must fit within remaining budget.

---

## Outputs to Generate

For new docs:
1. **`[CATEGORY]_[TOPIC]_v1.0_[DATE].md`** — The document itself
2. **`[DOCNAME]_DEBT.md`** — Known gaps (even if empty, template must exist)

For updates:
1. **Updated version of existing doc** — Increment version in frontmatter (v1.0 → v1.1)
2. **Updated DEBT.md** — Add/remove debt items as appropriate

---

## Generation Checklist

- [ ] Doc type confirmed before generating
- [ ] DOC_CANONICAL_TEMPLATE.md structure followed exactly
- [ ] Code blocks pass SYSTEM_Coding_Standards.md
- [ ] File named using pattern `{CATEGORY}_{TOPIC}_{VERSION}_{DATE}.md`
- [ ] Token count checked against `config/token_budgets.json`
- [ ] Gate 1 checked before delivery


========================================================================
AI DOCS — RULES
========================================================================

# Rules: AI Docs Builder

---

## Content Rules (All AI Docs)

1. **Write for both human and AI readers simultaneously.** Every section must be machine-parseable (structured metadata) AND human-readable (clear prose).

2. **Audience-appropriate depth.** `beginner` = zero assumed knowledge, full commands, every step. `advanced` = skip boilerplate, focus on non-obvious parts. `all` = layered: basics first, advanced details in subsections.

3. **No vague language.** Flag these immediately as Gate 3 violations:
   - "Configure properly" → specify the exact config
   - "Make sure it works" → specify the exact verification command
   - "Follow best practices" → cite the specific practice
   - "As appropriate" → specify the condition

4. **Every claim needs specifics.** No unsourced assertions. "Claude performs better" → "Claude Sonnet 4.6 achieves X% on Y benchmark (source: Anthropic docs, [date])."

5. **AI metadata blocks are required in all steps.** See DOC_CANONICAL_TEMPLATE.md § Section 3.

## How-To Specific Rules

- Steps are numbered 1, 2, 3 — not bullets
- Each step has one action only
- Every executable command shows Expected output
- Prerequisite verification command at the end of Prerequisites section

## Reference Doc Specific Rules

- Tables preferred over prose for structured data
- Every option has: type, required/optional, default, example
- Alphabetical ordering within tables
- No how-to content in reference docs — link to how-to instead

## System Guide Specific Rules

- These are rules files — write as laws, not suggestions
- Use positive + negative examples (GOOD/BAD patterns) for every rule
- Rules must be falsifiable (you can check if they're violated)
- Max 5 rules per section — more than 5 = restructure into subsections

## Update Doc Rules

- Increment version in frontmatter (1.0 → 1.1 for minor, 1.1 → 2.0 for major rewrite)
- Log what changed in a `## Changelog` section at the bottom
- Never delete sections — deprecate with `[DEPRECATED]` marker and reason
- Update DEBT.md to remove resolved items and add new ones


========================================================================
CODE — QUESTIONS
========================================================================

# Builder: Code Documentation

**Domain:** `code`
**Use when:** Generating technical documentation for code — setup guides, API docs, architecture docs, ADRs, troubleshooting guides. All code in output is subject to `SYSTEM_Coding_Standards.md`.

---

## Intake Questions

**Q1: Doc type?**
> Choose: `setup-guide` | `api-guide` | `architecture` | `adr` | `troubleshooting`

**Q2: What system or codebase is this for?**
> Name, language/stack, version, brief description.

**Q3: Who is the reader?**
> `beginner` | `intermediate` | `advanced` | `all`
> Are they using this to BUILD, RUN, or MAINTAIN the system?

**Q4: What prerequisites are required?**
> List tools (with versions), access requirements, knowledge needed.

**Q5: What are the exact commands/endpoints/patterns to document?**
> Be specific. For setup guides: the full installation sequence.
> For API docs: the endpoint method + path + parameters.
> For architecture: the components and their relationships.

**Q6: What does a successful run look like?**
> What exact output confirms success? (Terminal output, HTTP response, file created, etc.)

**Q7: What are the top 3–5 errors or failure modes?**
> Provide exact error messages if known. These become the Troubleshooting section.

**Q8 (ADR only): What alternatives were considered?**
> List alternatives and why each was rejected.

---

## Outputs to Generate

1. **`CODE_[TOPIC]_v1.0_[DATE].md`** — The documentation
2. **`CODE_[TOPIC]_DEBT.md`** — Known gaps (missing error signatures, untested commands, etc.)

---

## Code Quality Enforcement

Before delivering any code documentation:

1. Run SYSTEM_Coding_Standards.md checklist against every code block
2. Verify all commands were actually tested (or flag as "untested — verify before shipping")
3. Confirm model strings use current versions from RESEARCH_Claude_Project_Best_Practices.md
4. Mark AI-generated code blocks with the required marker comment

---

## Generation Checklist

- [ ] Language/stack confirmed
- [ ] All code blocks have language tags
- [ ] All commands show Expected output
- [ ] No hardcoded secrets
- [ ] Dependencies version-pinned
- [ ] Code within line-count limits
- [ ] Error signatures are exact strings (not descriptions)
- [ ] Token count within budget (`config/token_budgets.json`)
- [ ] Gate 1 verified before delivery


========================================================================
CODE — RULES
========================================================================

# Rules: Code Builder

---

## Code Documentation Rules (All Types)

1. **SYSTEM_Coding_Standards.md applies to every code block.** No exceptions. Any code block violating those standards = Gate 3 fail.

2. **Commands must be tested or explicitly flagged.** If a command hasn't been verified: prefix with `# ⚠️ Untested — verify before shipping`.

3. **Error signatures must be exact strings.** Copy from actual error output. "Something goes wrong with the connection" is not an error signature. `"ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"` is.

4. **One concept per doc.** Don't document the setup AND the architecture AND the API in one file. Split into separate docs. Each gets its own token budget.

5. **Version all external dependencies.** If the doc says "use library X" — it must say which version of X.

## Setup Guide Rules

- Prerequisites section is mandatory (Level 1–4 structure)
- Every step has exactly one action
- Verification step at the end
- "Uninstall / clean up" steps included if setup can be reversed

## API Guide Rules

- One endpoint per section
- Request example: full curl command with all required headers
- Response example: complete JSON, not truncated
- Error codes table: every known code with fix
- Rate limits documented if they exist

## Architecture Doc Rules

- Start with a system diagram (ASCII or Mermaid)
- One section per component
- Data flow described explicitly
- Decision rationale included
- "Not included" section: what's explicitly out of scope

## ADR Rules

- Context: what problem triggered this decision
- Decision: the exact choice made (one sentence)
- Consequences: what becomes easier, what becomes harder
- Alternatives considered: list with rejection reason
- Status: `Accepted` | `Deprecated` | `Superseded by [ADR title]`
- ADRs are immutable once status = Accepted — create a new ADR to supersede

## Troubleshooting Rules

- Error signature first (exact string), then root cause, then fix
- Fix steps must be commands, not descriptions
- "Verification" step at the end of each fix
- Max 5-7 errors per doc — move the rest to DEBT.md


========================================================================
SKILL MAP — AI ROUTING TABLE
========================================================================

# Skill Map — AI Routing Table for Doc Generation
**What this is:** Operational instructions for Docgen. At each generation stage, this map tells you which skill to apply. Skills encode domain expertise — using them produces better docs than generating from scratch.
**When to read:** At Step 3 of the Interactive Operating Mode, before showing the generation plan. Re-read at each generation stage (Step 4).
**Last updated:** April 2026

---

## Routing Rules

1. **Before generating any doc**, find the current stage in this map.
2. **Apply the skill:**
   - **Cowork / Claude Code:** Call the skill using the `Skill` tool. Pass intake context (Q0–Q8 answers + previously generated docs) as input. Use the skill's output as the raw draft.
   - **Claude.ai Chat:** Skills aren't callable. Instead, apply the specific domain expertise each skill represents. The skill name tells you WHAT expertise to bring — e.g., `skills-library:architecture-designer` means: apply system design patterns, scalability tradeoffs, and framework-correct file structures.
3. **Format and gate the draft.** Apply DOC_CANONICAL_TEMPLATE formatting. Run all 5 quality gates. Skill output is a starting point, not a finished doc.
4. **If no skill matches**, generate from the template directly.
5. **Stack-specific skills are mandatory** — when the user picks a tech stack in Q5, the corresponding framework skill must be applied during Architecture, Setup, Dev Plan, and Starter Prompt generation. Skipping = generic file paths and config instead of framework-correct ones.

---

## Product Builder (Type 1) — Generation Order

### Stage 1: PRD Generation
**Call:** `skills-library:writing-prds`
**Input:** Q0 context, Q1 one-liner, Q2 MVP features, Q3 user flows
**Fallback if not available:** `product-management:write-spec`
**Then:** Run through DOC_CANONICAL_TEMPLATE + quality gates

### Stage 2: UX Generation
**Call:** `design:user-research` (if user hasn't validated flows) → then `skills-library:ui-ux-pro-max`
**Input:** PRD output + Q3 user types and flows
**Also call:** `design:ux-copy` for microcopy in the flows
**Then:** Quality gates

### Stage 3: UI Generation
**Call:** `skills-library:ui-ux-pro-max`
**Input:** UX output + Q3 flows
**Also call:** `design:accessibility-review` on the generated screen specs
**Also call:** `design:design-handoff` to generate component specs
**Stack-specific:** If React/Next.js → also call `skills-library:ui-styling` for shadcn/Tailwind component mapping
**Then:** Quality gates

### Stage 4: Vision
**No skill available.** Generate from template using Q0–Q3 context.

### Stage 5: Architecture
**Call:** `skills-library:architecture-designer`
**Input:** PRD + Data entities (Q4) + Tech stack (Q5) + Integrations (Q6)
**Also call:** `skills-library:api-designer` for API layer decisions
**Stack-specific (mandatory):** Call the framework skill from the stack table below. Feed it the architecture context and ask it to validate/enhance the file structure and technology choices.
**Then:** Quality gates

### Stage 6: Data Schema
**Call:** `skills-library:sql-pro` or `skills-library:postgres-pro` (based on Q5 database choice)
**Input:** Architecture output + Q4 data entities + user flows from UX
**Then:** Quality gates

### Stage 7: API Spec
**Call:** `skills-library:api-designer`
**Input:** Architecture output + Data Schema + PRD features
**If GraphQL:** Call `skills-library:graphql-architect` instead
**Then:** Quality gates

### Stage 8: Environment Setup
**Call:** `skills-library:devops-engineer` (for Docker/CI/CD) or `skills-library:cloud-architect` (for cloud deployment)
**Input:** Architecture + Tech stack + Integrations (Q6)
**Stack-specific:** Call framework skill for setup commands and configuration
**Then:** Quality gates

### Stage 9: Dev Plan
**Call:** `skills-library:feature-forge` for requirements → task breakdown
**Also call:** Stack-specific framework skill to validate phase tasks and file paths
**Also call:** `engineering:testing-strategy` for the testing phase
**Also call:** `engineering:deploy-checklist` for the deployment phase
**Input:** ALL previous docs (PRD through Setup)
**Then:** Quality gates (90/100 target)

### Stage 10: CLAUDE.md
**No skill needed.** Generate from template — this is Docgen's core output.

### Stage 11: Starter Prompt
**Call:** `skills-library:vibe-coding` for AI coding best practices
**Also call:** `skills-library:prompt-engineer` to optimize the prompt
**Input:** Dev Plan + CLAUDE.md + tool choice (Q7)
**Then:** Quality gates

---

## Claude Project Builder (Type 2) — Generation Order

### Project Instructions
**Call:** `skills-library:prompt-engineer`
**Input:** Q0 context, purpose, target users

### Knowledge Base Structure
**Call:** `skills-library:rag-architect` (if project needs retrieval over large docs)
**Input:** What knowledge the project needs access to

### Custom Skills (if project needs them)
**Call:** `skill-creator`
**Input:** Identified workflow patterns from intake

### MCP Integrations (if project needs live tools)
**Call:** `skills-library:mcp-developer` or `mcp-builder`
**Input:** Q6 integrations list

### Dev Plan + Starter Prompt
**Call:** `skills-library:prompt-engineer` for the starter prompt
**Call:** `skills-library:vibe-coding` for coding best practices

---

## Skill Builder (Type 3) — Generation Order

### SKILL.md
**Call:** `skill-creator` — **always, no exceptions**
**Input:** All intake answers (Q0–Q8)
**This skill handles the entire lifecycle:** create, structure, validate

### evals.json
**Call:** `ai-evals`
**Input:** SKILL.md output + expected behaviors

### Before Building — Duplicate Check
**Call:** Search the 341-skill catalog. If a matching skill exists, recommend customizing it instead of building from scratch. Categories to search:
- Check skill name/description against user's stated purpose
- Check `skills-library:*` variants first (these are installable)

---

## MCP Server Builder (Type 4) — Generation Order

### Setup Guide + API Reference
**Call:** `mcp-builder` — **always, no exceptions**
**Also call:** `skills-library:mcp-developer` for implementation details
**Input:** All intake answers

### Tool Schema Design
**Call:** `skills-library:api-designer`
**Input:** What the MCP server needs to read/write

### Auth Guide
**Call:** `mcp-builder` (handles auth patterns)

### Testing
**Call:** `engineering:testing-strategy`

---

## Stack-Specific Skill Table (Mandatory at Stages 5, 8, 9, 11)

When the user answers Q5 (tech stack), look up the framework skill below. Call it during Architecture, Setup, Dev Plan, and Starter Prompt generation to validate technology-specific decisions.

| Stack component | Skill to call |
|----------------|---------------|
| Next.js | `skills-library:nextjs-developer` |
| React | `skills-library:react-expert` |
| Vue 3 | `skills-library:vue-expert` |
| Angular | `skills-library:angular-architect` |
| React Native / Expo | `skills-library:react-native-expert` |
| Flutter | `skills-library:flutter-expert` |
| Swift / iOS | `skills-library:swift-expert` |
| NestJS | `skills-library:nestjs-expert` |
| Express / Node.js | `skills-library:javascript-pro` |
| FastAPI | `skills-library:fastapi-expert` |
| Django | `skills-library:django-expert` |
| Rails | `skills-library:rails-expert` |
| Laravel | `skills-library:laravel-specialist` |
| Spring Boot | `skills-library:spring-boot-engineer` |
| .NET / ASP.NET Core | `skills-library:dotnet-core-expert` |
| Go | `skills-library:golang-pro` |
| Rust | `skills-library:rust-engineer` |
| PHP | `skills-library:php-pro` |
| Python | `skills-library:python-pro` |
| TypeScript | `skills-library:typescript-pro` |
| PostgreSQL | `skills-library:postgres-pro` |
| SQL (general) | `skills-library:sql-pro` |
| GraphQL | `skills-library:graphql-architect` |
| WebSockets | `skills-library:websocket-engineer` |
| Kubernetes | `skills-library:kubernetes-specialist` |
| Terraform / IaC | `skills-library:terraform-engineer` |
| Docker / CI/CD | `skills-library:devops-engineer` |
| Playwright / E2E | `skills-library:playwright-expert` |
| WordPress | `skills-library:wordpress-pro` |
| Shopify | `skills-library:shopify-expert` |
| Salesforce | `skills-library:salesforce-developer` |

---

## Post-Bundle Skills (recommend to user after delivery)

After delivering the bundle, tell the user about these skills for their next phase:

### Go-to-Market
`marketing:campaign-plan`, `marketing:content-creation`, `marketing:email-sequence`, `marketing:seo-audit`, `skills-library:launch-marketing`, `skills-library:positioning-messaging`, `skills-library:copywriting`, `sales:competitive-intelligence`, `sales:draft-outreach`

### Growth & Optimization
`skills-library:page-cro`, `skills-library:signup-flow-cro`, `skills-library:onboarding-cro`, `skills-library:ab-test-setup`, `skills-library:churn-prevention`

### Pre-Build Validation (recommend if user hasn't validated)
`discovery:start-discovery`, `discovery:make-research`, `discovery:make-solution`, `discovery:make-decomposition`, `design:research-synthesis`, `skills-library:customer-research`, `skills-library:measuring-product-market-fit`

---

*This file is read by Docgen at generation time. It is not a user-facing document.*


