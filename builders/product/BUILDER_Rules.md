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
