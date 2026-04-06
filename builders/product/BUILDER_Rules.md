# Product Builder — Rules
**Applies to:** All docs generated via `builders/product/`.
**Authority:** `SYSTEM_Exit_Rules.md` > `SYSTEM_Content_Guide.md` > this file.

---

## Rule 1 — Dev Plan Is Always Generated Last

The DEV_Plan doc synthesizes every other doc in the bundle. It cannot be written until ARCH, DATA, API, and SETUP are complete and reviewed. Any doc generated before its dependencies = quality gate fail.

Generation order: Vision → Architecture → Data Schema → API Spec → Environment Setup → **Dev Plan** → CLAUDE.md → Starter Prompt.

Never deviate from this order.

---

## Rule 2 — Dev Plan Phases Must Reference Specific Files

Every task in every phase must name:
- The exact file to create or modify (e.g., `src/models/user.ts`, `migrations/001_users.sql`)
- The acceptance criterion — a testable statement (passes test / endpoint returns 200 / UI renders component)
- The phase dependency — what must be complete before this phase starts

Vague tasks like "build the authentication system" = Gate 3 fail. Rewrite as:
- "Create `src/lib/auth.ts` — implements `signIn()`, `signOut()`, `getSession()`. Acceptance: `auth.test.ts` passes all 3 cases."

---

## Rule 3 — Phase 0 Always Exists

Every dev plan starts with Phase 0: Project Setup. It covers:
- Repository initialization (commands copy-pasteable)
- Dependency installation (`package.json` or `requirements.txt` contents)
- Environment variable setup (`.env.example` with all keys, no values)
- Local dev server verification (command + expected output)

Phase 0 must be completable by a developer in under 30 minutes. If it's longer, split it.

---

## Rule 4 — Starter Prompt Is Self-Contained

The starter prompt must work when pasted verbatim into a fresh AI session with zero prior context. It includes:
- What is being built (one-liner)
- What files are provided (list every file in the bundle)
- Explicit instruction to read CLAUDE.md first
- The first concrete task (Phase 0, Task 1 from the dev plan)
- A constraint: "Follow the dev plan phases in order. Ask before deviating."

Test: if you removed every other doc and only gave the AI the starter prompt, could it at minimum set up the project? If not, the starter prompt is incomplete.

---

## Rule 5 — CLAUDE.md Is for the New Project, Not Docgen

The CLAUDE.md in the output bundle is written for the product being built, not for this documentation system. It follows the standard structure: What This Is / Commands / Architecture / Code Style / Important Notes. Under 300 lines. Version stamped.

Do not copy the docgen CLAUDE.md into the bundle.

---

## Rule 6 — Tech Stack Must Be Fully Specified

No doc in the bundle may say "use your preferred database" or "choose an appropriate framework." Every technology decision must be explicit:
- Frontend: framework + version
- Backend: runtime + framework + version
- Database: type + name + ORM/client
- Auth: provider + method
- Deployment: platform + config

If the user hasn't decided, recommend a stack per Q5 guidelines and confirm before generating.

---

## Rule 7 — File Structure Is Declared in Architecture Doc

The ARCH doc must contain the complete top-level folder structure for the project. Not a general diagram — the actual intended directory tree, with a one-line comment on every folder.

Example (not a template — adapt to actual stack):
```
my-app/
├── src/
│   ├── app/          ← Next.js App Router pages
│   ├── components/   ← Shared UI components
│   ├── lib/          ← Utilities, auth, db client
│   └── types/        ← TypeScript type definitions
├── prisma/           ← Schema and migrations
├── public/           ← Static assets
├── tests/            ← Jest unit + integration tests
├── .env.example      ← All required env vars (no values)
├── CLAUDE.md         ← AI coding context (read first)
└── package.json
```

The dev plan's task list must reference this exact structure. Discrepancies between ARCH and DEV_Plan = Gate 3 fail.

---

## Rule 8 — MVP Scope Is Frozen at Intake

Once the user confirms the MVP feature list, the entire bundle scopes to those features only. If the user asks to add features during generation, pause and ask: "Do you want to add this to the MVP scope? This will require updating the architecture, schema, API spec, and dev plan before I continue."

Never silently expand scope mid-generation.

---

## Rule 9 — Every Integration Gets an Environment Variable

Every external service mentioned in Q6 must appear in:
- `SETUP_Environment.md` → API Keys section
- `.env.example` → the scaffold file
- `ARCH_System.md` → Integrations section
- `DEV_Plan.md` → the phase that wires it up

A service mentioned in the architecture but missing from the environment setup = Gate 2 fail.

---

## Rule 10 — Quality Score Target Is 90/100 for Product Bundles

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

---

## Rule 12 — Generated Docs Must Be Written Lean

Every doc in the product bundle is read by an AI coding agent, not a human. Dense, structured output parses better and costs fewer tokens to send as context. Apply these per-doc rules:

### PRD
- Features as user stories only: `As a [user], I want [action] so that [outcome].`
- Acceptance criteria: `GIVEN/WHEN/THEN` — one line each, no prose
- Out-of-scope: bulleted list, one phrase per item
- No narrative introduction — start with Problem Statement directly
- Bad: "The user registration feature will allow new users to create accounts..." → Good: `User registers | POST /auth/register | returns JWT`

### Architecture Doc
- Tech stack decisions: table format — `| Layer | Choice | Version | Reason (one clause) |`
- File structure: directory tree with ← comments, nothing else
- Data flow: numbered sequence `1. Client → 2. API → 3. DB → 4. Response`, not prose
- Integrations: one row per service — `| Service | Purpose | Auth method | Env var |`
- No "we chose X because it is a popular and well-supported..." — just `| DB | Postgres | mature, Prisma support |`

### Data Schema
- Table per entity: `| Field | Type | Required | Default | Notes |`
- Relationships: `User 1→N Projects` — not prose
- No field explanations inline — notes column only if non-obvious

### API Spec
- One table per endpoint group: `| Method | Path | Auth | Body | Response |`
- Request/response shapes: inline JSON schema, no prose description
- Error codes: `| Code | Meaning | When |` — three columns, one row per code

### Dev Plan
- Task format: `{N.M} — {verb} {filename}` / `Acceptance: {GIVEN/WHEN/THEN}`
- No "goal" paragraphs beyond one sentence per phase
- Phase header format: `Phase N — {Name} | Depends: Phase {N-1} | Est: {N}h`

### Starter Prompt
- Under 600 tokens total
- No "How to Use This File" section in the actual prompt — only in surrounding wrapper
- Rules section: 5 rules max, one sentence each
- Phase 0 tasks: copy from Dev Plan verbatim, no restatement

### CLAUDE.md (for the built product)
- Under 150 lines
- Commands section: copy-pasteable only — no explanation of what commands do
- Architecture section: one paragraph max, reference ARCH_System.md for detail

---

## Rule 11 — AI-Native Products Use prompt-building Skills (Callable)

When Q5 identifies an AI-native stack (LLM product, AI agent, RAG system, chatbot, prompt pipeline), the following `prompt-building` skills are callable via Skill tool — use them instead of or in addition to local SKILL.md reads:

| Stage | When | Call |
|-------|------|------|
| Stage 5 — Architecture | Always for AI-native stack | `Skill tool: prompt-building:prompt-engineering-patterns` → prompt architecture, system prompt design, token efficiency |
| Stage 5 — Architecture | If multi-step chains or agents | `Skill tool: prompt-building:langchain-architecture` → chain design, ReAct agent, memory architecture |
| Stage 7 — API Spec | If prompt API endpoints exist | `Skill tool: prompt-building:prompt-engineering-patterns` → structured output schemas for prompt inputs/outputs |
| Stage 9 — Dev Plan | If evaluation tasks in plan | `Skill tool: prompt-building:llm-evaluation` → quality metric tasks, LLM-as-Judge setup, A/B test phases |
| Stage 11 — Starter Prompt | Always for AI-native stack | `Skill tool: prompt-building:prompt-engineering-patterns` → apply few-shot, CoT, and structured output to the starter prompt itself |

**AI-native detection rule:** If Q0 mentions LLM, AI, GPT, Claude, agents, RAG, embeddings, chatbot, or prompt — treat as AI-native and apply this rule.

**Token budget:** Each Skill tool call counts as one of the two allowed skill activations per stage. If this rule adds a third, it replaces the secondary local read (not the primary architecture skill).

---

## Stage 3 (UI) — Missing Skill Workaround

The skills `ui-ux-pro-max` and `ui-styling` are not available locally. At UI generation:

1. Apply standard UX component patterns and accessibility principles directly.
2. Read the stack-specific framework skill from `skills/SKILL_MAP.md` stack table (e.g., `skills/nextjs-developer/SKILL.md`) — this covers component naming and structure for the target framework.
3. For React/Next.js: apply shadcn/ui + Tailwind class naming conventions to all component specs.
4. For mobile stacks: apply native component patterns (iOS HIG for Swift, Material Design for Flutter/Android).

This workaround is documented. Do not attempt to call `ui-ux-pro-max` — it does not exist locally.
