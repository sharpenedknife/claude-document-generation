# How to Use the Documentation Builder
**What this is:** A step-by-step guide for setting up and using the Documentation Builder to generate complete, AI-ready implementation documentation for anything you want to build.
**Last updated:** April 2026 · v2.0
**GitHub:** https://github.com/sharpenedknife/claude-document-generation

---

## What Docgen Does

You describe what you want to build. Docgen asks the right questions, then generates a complete bundle of implementation documents that an AI coding agent (Claude, Cursor, Windsurf, Codex) can use to build the thing correctly — without you needing to know how to write technical specs.

**What you get:** A zip file with everything the AI needs to start building. For products, that's 11 documents including a development plan and a starter prompt you paste directly into your AI tool.

---

## Choose Your Setup Path

There are two ways to use Docgen, depending on where you want to run it:

| Path | Best for | Setup time |
|------|----------|------------|
| **Path A — Claude.ai Chat** | Web users, no terminal needed | 5 minutes |
| **Path B — Cowork / Claude Code** | Power users, full file access | 2 minutes |

---

## Path A — Claude.ai Chat Project (4 files to upload)

This only needs to be done once.

**A.1 Create the project:**
- Go to [claude.ai](https://claude.ai) → Projects → New Project
- Name it: `Documentation Builder`
- Description: `Create & update product docs.`

**A.2 Paste the project instructions:**
- Click "Set project instructions"
- Open `system/templates/project_instructions/PROJECT_INSTRUCTIONS_Docgen_Production.md`
- Copy the full contents → paste → Save

**A.3 Upload the knowledge base (4 files only):**
- Click "+" in the "Project knowledge" panel
- Upload these 4 files from the `chat/` folder:
  1. `CLAUDE.md` (from the repo root)
  2. `chat/REFERENCE_System.md`
  3. `chat/REFERENCE_Builders.md`
  4. `chat/REFERENCE_Templates.md`
- Wait for processing (~1 minute)

**A.4 (Optional) Link the GitHub repo:**
- In the Project settings, add the repo URL: `https://github.com/sharpenedknife/claude-document-generation`
- This gives Claude access to the full source files when it needs deeper detail

**A.5 Verify it's working:**
Send: *"hi"*

A correctly configured project responds with the navigation menu showing all 4 build types. If it doesn't show the menu, re-paste the project instructions and save again.

---

## Path B — Cowork / Claude Code (clone and go)

```bash
git clone https://github.com/sharpenedknife/claude-document-generation.git
cd claude-document-generation
```

**For Claude Code:** Run `claude` in the project directory. CLAUDE.md is read automatically.

**For Cowork:** Select the `claude-document-generation/` folder as your working directory. CLAUDE.md is read automatically.

That's it. No uploading, no pasting instructions. Say "hi" and the menu appears.

---

## Step 1 — Set Up (see Path A or Path B above)

---

## Step 2 — Open a Chat: The Menu Appears Automatically

Open your Documentation Builder (whether chat project, Cowork, or Claude Code) and start a new chat. **Just say "hi" or anything at all** — Docgen's first response is always the navigation menu:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋  DOCUMENTATION BUILDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
What do you want to build?

🏗️  1 · Product / Startup
🤖  2 · Claude Project
⚡  3 · Skill
🔌  4 · MCP Integration
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

You can respond with a number ("1"), a keyword ("product"), or describe what you want directly. Type `/menu` at any point to bring the menu back.

**You can also skip the menu entirely** and just describe your idea:

> "I want to build a task management app for remote teams."

> "I need a Claude assistant that knows our brand guidelines."

> "Connect Claude to our Jira so it can create tickets from Slack messages."

> "Document the API for our checkout service."

Docgen identifies the build type automatically and starts asking the right questions.

---

## Step 3 — Provide Context (Your Way)

No question is mandatory. Provide context however works for you:

- **Answer questions** — Docgen asks conversationally, one at a time. Answer as many or as few as you want.
- **Paste freeform context** — Drop in existing specs, notes, braindumps, competitor analysis, design docs.
- **Upload files** — Screenshots, wireframes, existing code, spreadsheets.
- **Mix and match** — Answer some questions, paste some context, skip the rest.

Docgen dynamically figures out if it has enough to generate quality docs. If context is thin, it warns you and lists the assumptions it will make — you decide whether to add more detail or proceed with defaults. Every default gets marked as ASSUMED in the output so you can review and override later.

**Tips for better output:**
- Be specific about features. "User management" is vague. "Users can invite team members by email, set their role (Admin or Member), and remove them" is actionable.
- If you don't know the tech stack, say "we're a Node.js team" or "we're a Python team" and Docgen will recommend.
- The MVP feature list should be the smallest possible version that delivers real value.
- If you have existing specs, designs, or notes — paste them. Docgen extracts what it needs and skips questions you've already answered.

---

## Step 4 — Review and Confirm the Generation Plan

Before Docgen generates anything, it shows you a plan:

> "Here's what I'm going to generate for [Your Product]:
> - PRD — feature requirements + acceptance criteria
> - UX — user journeys + flows
> - UI — screen list + component specs
> - Architecture — tech stack + file structure
> - Data Schema — all entities + relationships
> - API Spec — all endpoints + request/response shapes
> - Environment Setup — dependencies + env vars + deployment
> - Development Plan — phases, tasks, files, acceptance criteria
> - CLAUDE.md — for your new project
> - Starter Prompt — paste into your AI tool to begin
>
> Delivered as: YourProduct_Implementation_Bundle_v1.0_2026-04-03.zip
>
> Does this look right?"

**This is your last chance to adjust scope before generation.** If you want to add or remove features, do it now. Once you confirm, Docgen generates all 11 documents.

---

## Step 5 — Receive Your Bundle

Docgen delivers a zip file: `{ProductName}_Implementation_Bundle_v1.0_{date}.zip`

**What's inside:**

```
YourProduct_Implementation_Bundle_v1.0_2026-04-03/
├── PRD_YourProduct_v1.0.md          ← Feature requirements + acceptance criteria
├── UX_YourProduct_v1.0.md           ← User journeys + flows
├── UI_YourProduct_v1.0.md           ← Screen list + component specs
├── PRODUCT_Vision_YourProduct_v1.0.md
├── ARCH_System_YourProduct_v1.0.md  ← Tech stack + folder structure
├── DATA_Schema_YourProduct_v1.0.md  ← Database entities + relationships
├── API_Spec_YourProduct_v1.0.md     ← All API endpoints
├── SETUP_Environment_YourProduct_v1.0.md ← Setup + deployment
├── DEV_Plan_YourProduct_v1.0.md     ← ★ The implementation plan
├── CLAUDE.md                         ← For your new project (read this first)
└── STARTER_PROMPT_YourProduct.md    ← ★ Paste this into your AI tool
```

The two most important files are marked ★:
- **DEV_Plan** is the execution graph — phases in order, each with specific files and acceptance criteria
- **STARTER_PROMPT** is what you paste to start building — see Step 6

---

## Step 6 — Hand Off to Your AI Coding Tool

### Using Claude Projects

1. Create a new Claude project for your product (not the Docgen project — a new one)
2. Upload all files from the bundle to the project knowledge base
3. Open a chat in the project
4. Open `STARTER_PROMPT_YourProduct.md` — copy everything inside the marked section
5. Paste it as your first message
6. Claude reads all context files and begins Phase 0 (project setup)

### Using Cursor

1. Open Cursor and create a new project folder
2. Copy all files from the bundle into the project root
3. Open a new AI chat (Cmd+L or Ctrl+L)
4. Open `STARTER_PROMPT_YourProduct.md` — copy and paste as first message
5. Cursor reads the project files automatically and begins Phase 0

### Using Windsurf

Same as Cursor — copy bundle files to project root, paste starter prompt in the AI panel.

### Using Codex / API

1. Use `CLAUDE.md` contents as your system prompt
2. Use the starter prompt as the first user message
3. Attach all doc files as context files

---

## Step 7 — Evaluate and Refine

After reviewing the generated docs, go back to the Docgen project and request improvements:

> "Redo the Dev Plan — Phase 3 needs more detail on the file structure."

> "The API spec is missing the search endpoint from the PRD."

> "The UX flows don't cover what happens when a user's invite expires."

Docgen regenerates only the specific doc you asked about, re-runs quality gates, and delivers an updated zip. You do not need to regenerate the full bundle.

**Evaluate each doc against these questions:**
- PRD: Is every MVP feature described with clear acceptance criteria? Is "out of scope" explicitly listed?
- UX: Does every user type have at least one complete flow from start to value?
- UI: Does every screen have a name, purpose, and list of components?
- Dev Plan: Does every phase have concrete file names and a testable acceptance criterion?
- Starter Prompt: Could an AI complete Phase 0 from this prompt alone, with no other context?

---

## Step 8 — During Development: Keep CLAUDE.md Updated

As your AI coding agent builds the product, it will discover things that aren't in the docs. Instruct it to update `CLAUDE.md` whenever:
- A new command or script is needed
- A gotcha or workaround is discovered
- A dependency version caused a problem
- The folder structure deviates from the architecture doc

A stale CLAUDE.md is the most common cause of AI coding failures mid-project.

---

## FAQ

**Q: How long does it take to generate the bundle?**
Typically 10–20 minutes total: ~5 minutes for Q&A, ~10–15 minutes for generation of all 11 docs. Complex products with many integrations take longer.

**Q: Can I reuse Docgen for the same product as it grows?**
Yes. Run a new session, paste the existing CLAUDE.md from your project for context, and say "generate a v2 dev plan covering [new features]." Docgen will version the output correctly.

**Q: What if I don't know the tech stack?**
Tell Docgen your team's background (e.g., "we're JavaScript developers" or "this is solo, I prefer Python"). It will recommend a stack and explain why before generating.

**Q: Can I use Docgen for something that isn't a product?**
Yes. Docgen handles four build types: products, Claude Projects (AI assistants), Skills (repeatable workflows), and MCP Servers (live tool integrations). The Q&A adapts to the build type.

**Q: What if the AI coding agent doesn't follow the dev plan?**
Add this line to your starter prompt: *"When I say 'check the plan', stop and reread `DEV_Plan.md` before continuing."* Use this phrase any time the agent drifts from the phase order.

**Q: Should I upload the Docgen system files to my product's Claude project?**
No. The Docgen bundle is self-contained — it has its own `CLAUDE.md` for the product. The Docgen system files belong only in the Documentation Builder project.

---

## Quick Reference: Build Types

| You want to build | Docgen routes to | Main output |
|---|---|---|
| A product / app / SaaS / tool | Product Builder | 11-doc implementation bundle |
| A Claude assistant for your team | Claude Project Builder | CLAUDE.md + project instructions + knowledge base structure |
| A repeatable workflow or `/command` | Skill Builder | SKILL.md + evals.json |
| Claude connected to an external tool | MCP Builder | Setup guide + API reference + auth guide |

---

*Documentation Builder v2.0 · April 2026*
*For issues with the system: update `backlog/SYSTEM_DEBT.md` and regenerate affected docs.*
