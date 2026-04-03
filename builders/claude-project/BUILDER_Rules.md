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

## User Onboarding Rules — First-Response Menu + Project Description

Claude.ai Projects does NOT have built-in conversation starters or customizable placeholder text. The equivalent is a **first-response menu** in the custom instructions (Claude always shows it as its first message) combined with a well-written **project description** (the subtitle under the project name).

Every generated Claude Project MUST include both:

### 1. Project Description (subtitle)

The short text under the project name in the Claude.ai sidebar. Keep it under 60 characters. It should tell the user what the project does in one phrase.

**Format:** `[Action verb] + [what] + [for whom/what context]`

**Examples:**
- "Create & update product docs." (Docgen)
- "Review PRs and suggest improvements." (Code Reviewer)
- "Draft and optimize cold emails." (Sales Outreach)

Generate this from Q2 (Core Purpose) during intake. Include it in the README setup steps.

### 2. First-Response Menu

Every generated CLAUDE.md and PROJECT_INSTRUCTIONS must include a first-response menu that acts as conversation starters. The menu appears as Claude's very first message in every new conversation — before the user types anything meaningful.

**Design principles (from AI onboarding research):**

- **3-5 options maximum** — more causes decision paralysis
- **Each option starts with an emoji + number** — visual scanning
- **Each option has a one-line description** — the user knows what they'll get
- **Include a catch-all option** — "or just describe what you need" at the bottom
- **Options map to the project's core tasks** — derived from Q4 (Key Tasks)
- **Use action-oriented language** — "Draft a cold email" not "Email assistance"
- **One option should be exploratory** — "What can you do?" or "Show me examples" helps new users

**Template:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[emoji]  [PROJECT NAME]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
What do you want to do?

[emoji]  1 · [Core Task 1]
     [One-line description of what the user gets]

[emoji]  2 · [Core Task 2]
     [One-line description of what the user gets]

[emoji]  3 · [Core Task 3]
     [One-line description of what the user gets]

[emoji]  4 · [Core Task 4 — exploratory/help]
     [One-line description]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pick a number, or just tell me what you need.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**The first-response instruction in CLAUDE.md must say:**
"Your very first response in every new conversation must be this menu. No exceptions. Even if the user says 'hi' or asks a direct question — show the menu first, then respond."

### 3. No Hallucination in Onboarding

The menu options must match the project's ACTUAL capabilities. Do not add options for features the project doesn't support. Every menu item must map to a documented task or workflow in the project's knowledge base.
