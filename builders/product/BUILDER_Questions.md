# Product Builder — Intake Questions
**Use when:** User wants to build a product, app, SaaS, tool, or any software system.
**Output:** Implementation-ready bundle — docs + dev plan + starter prompt + project scaffold.

---

## Q0 — Context Gate (ask before anything else)

Before collecting detailed answers, ask:

> "Tell me what you want to build in 2–3 sentences. Who uses it, what does it do, and what's the main problem it solves?"

If the answer covers all three (who / what / why), proceed to Q1–Q8. If not, ask the missing piece specifically. Never proceed to generation without all three answered.

---

## Q1 — Product One-Liner

**Ask:** "Give me the one-liner: '[Product] helps [user] to [outcome] by [differentiator].' Fill in the blanks."

**Why:** Every doc in the bundle opens with this. If the one-liner is fuzzy, every doc is fuzzy.

**What to capture:** Product name + target user + core outcome + differentiator.

---

## Q2 — MVP Scope (max 5 features)

**Ask:** "List the features you want in the MVP — the smallest version that delivers real value. Maximum 5."

If the user lists more than 5, ask them to prioritize: "If you could only ship 3 of these, which 3?"

**Why:** The dev plan phases map directly to MVP features. Unbounded scope = unbounded dev plan = agent doesn't know where to stop.

**What to capture:** Ordered list of 3–5 features with brief descriptions.

---

## Q3 — Target Users and Core Flows

**Ask:** "Who are the 1–2 types of users? For each, describe the most important thing they do in the product — one complete flow from landing to value."

**Why:** Data schema and API design follow user flows. If the flows are unclear, the schema will have wrong entities.

**What to capture:** User types + 1 core flow per type (start → actions → outcome).

---

## Q4 — Data Entities

**Ask:** "What are the main 'things' your product stores and manages? Example: a task manager has Users, Tasks, Projects, Comments."

If the user isn't technical, rephrase: "What are the nouns in your product? What objects does a user create, manage, or interact with?"

**Why:** The data schema doc derives from this. Entities define the entire backend.

**What to capture:** 4–8 named entities + brief description of each + key relationships.

---

## Q5 — Tech Stack

**Ask:** "What tech stack do you want to use? If you're not sure, tell me your team's background and I'll recommend."

Provide a recommendation if they don't know:
- **Web app (non-technical founder, fast MVP):** Next.js + Supabase + Vercel
- **Web app (engineering team):** Next.js + PostgreSQL + Node API + Docker
- **Mobile:** React Native + Expo + Supabase
- **AI-native product:** Next.js + Python FastAPI + PostgreSQL + OpenAI/Claude SDK

**Why:** Architecture doc, CLAUDE.md, environment setup, and scaffold files all depend on stack. A vague stack = docs that don't work.

**What to capture:** Frontend framework + backend + database + auth solution + deployment target.

---

## Q6 — Key Integrations

**Ask:** "Are there any external services this product must connect to? Examples: Stripe (payments), Auth0 (auth), SendGrid (email), OpenAI (AI), Twilio (SMS), Slack (notifications)."

**Why:** Integrations appear in the architecture diagram, environment setup (API keys), and dev plan phases.

**What to capture:** List of services + what they're used for.

---

## Q7 — AI Coding Tool

**Ask:** "Which AI coding tool will you use to build this? Claude Projects, Cursor, Windsurf, Codex, or something else?"

**Why:** The CLAUDE.md format, starter prompt structure, and file bundle layout are optimized per tool. Cursor handles `.cursor/rules/` differently from Claude Projects.

**What to capture:** Primary AI tool + secondary if any.

---

## Q8 — Existing Code?

**Ask:** "Are you starting from scratch, or is there an existing codebase? If existing, describe what's already built."

**Why:** If existing code exists, the dev plan must not repeat what's done. Architecture doc references the existing structure.

**What to capture:** New project / existing project + what already exists.

---

## Context Confirmation (before generating)

Before generating any docs, present a summary and confirm:

> "Here's what I'm going to build:
> - **Product:** [one-liner]
> - **MVP features:** [list]
> - **Stack:** [stack]
> - **Output bundle:** [7 docs + CLAUDE.md + starter prompt + scaffold]
>
> Does this look right, or do you want to adjust anything before I generate?"

Only generate after explicit confirmation.

---

## Output Bundle (always deliver all of these)

**Generation order matters** — each doc informs the next.

| # | File | Purpose | Depends on |
|---|---|---|---|
| 1 | `PRD_{name}_v1.0.md` | Product requirements: features, acceptance criteria, out-of-scope | Q0–Q2 intake |
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

**PRD note:** The PRD is the AI's source of truth for *what* to build. Every feature must have: description, user story, acceptance criteria, and out-of-scope boundary. This prevents scope creep during AI-assisted development.

**UX note:** User journeys inform the API design and UI component list. If flows are missing from UX, the API will be missing endpoints and the UI will be missing screens.

**UI note:** Screen list and component spec is what the AI uses to generate frontend code. It must reference UX flows (which screen triggers which) and design system tokens if available.

---

## Post-Delivery: Evaluate and Rerun

After delivering the bundle, always ask:

> "Review the docs and let me know:
> - Which docs need more detail?
> - Anything missing or wrong in the dev plan?
> - Does the starter prompt give the AI everything it needs?
>
> You can say 'redo [doc name]' with specific feedback and I'll regenerate just that doc."

Rerun rules:
- Regenerate the specific doc only — don't regenerate the full bundle unless explicitly asked
- Incorporate feedback precisely — quote back what changed
- Re-run quality gates on the regenerated doc before delivering
- Update the zip after any rerun
