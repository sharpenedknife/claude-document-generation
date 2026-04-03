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
