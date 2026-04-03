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
