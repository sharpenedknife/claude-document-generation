# User Journey Guide: From Idea to Working AI System
**Version:** 1.0 · April 2026
**Purpose:** Guide users through every stage — from "I have an idea" to "it works in production." Never skip a stage. Never assume the user knows the next step.

---

## The Docgen Mission

**Our job:** Take the user's idea and produce complete, implementation-ready documentation that an AI can use to build the thing correctly.

**How we work:** We ask until we understand. We generate only when we have enough. We guide through activation. We verify it works.

**The rule on context:** Ask as many questions as needed before generating. One missing context item means the wrong docs. Wrong docs mean the AI builds the wrong thing. Incomplete is always worse than asking more.

---

## The Five Stages

```
Stage 1: Understand     → What are we building, exactly?
Stage 2: Collect        → Get all context before touching a file
Stage 3: Generate       → Produce the docs
Stage 4: Activate       → Deploy/install/configure the thing
Stage 5: Verify         → Confirm it works, log what's missing
```

Never jump stages. If Stage 1 is unclear, do not proceed to Stage 2.

---

## Stage 1: Understand — What Are We Building?

### The Q0 Gate

Before any intake questions, answer: **what type of thing is being built?**

Ask the user to describe their idea in 2-3 sentences. Then classify:

| What user describes | Build type | Go to |
|---|---|---|
| "A Claude assistant that knows about X" | Claude Project | `builders/claude-project/` |
| "A slash command / repeatable workflow" | Skill | `builders/skill/` |
| "Connect Claude to [tool]" | MCP Server | `builders/mcp/` |
| "Document this product/feature/API" | AI Doc | `builders/ai-docs/` |
| "Document this codebase" | Code Doc | `builders/code/` |
| All of the above combined | Start with Project, then Skills, then MCP | Sequential |

**If unclear:** Ask. Do not classify based on one ambiguous sentence.

### Questions to Clarify the Build Type

When the user's description is vague, ask exactly one of these:

- "Is this something people will chat with (like an assistant), or a specific task they'll trigger (like a command)?"
- "Will it need to connect to live tools like Slack, Jira, or a database — or just work with documents?"
- "Is this a one-time document, or something people will use repeatedly?"

### Check Before Building

**For Skills:** Check the 341-skill library first. "Before we build, let me check if this already exists. What would you type to trigger it?"

If a matching skill exists: "There's already a `[skill-name]` skill that [does X]. Should we use that, customize it, or build something distinct?"

**For MCP connectors:** Check available connectors (Slack, Notion, Jira, Figma, Google Calendar, Gmail, Ahrefs, etc.). Many integrations are already built.

---

## Stage 2: Collect — Get All Context

### The Context Gate

Run the appropriate builder's intake questions (`builders/{type}/BUILDER_Questions.md`). Do not skip questions. Do not generate with unknowns or placeholders.

**The most important questions to ask for each type:**

**Claude Project:**
- What will Claude specifically DO in this project? (list 3-5 tasks)
- Who is the user? (technical level + role)
- What files/knowledge should Claude always have access to?
- What should Claude never do or say in this project?

**Skill:**
- What exact phrase or command triggers this skill?
- What are 3-5 specific situations where it should trigger (even without explicit command)?
- What does the user provide as input?
- What does the user get back, in what format?

**MCP Server:**
- What external system? (name + URL)
- What should Claude READ from it?
- What should Claude DO in it? (create/update/send/query)
- How does it authenticate? (API key, OAuth, service account)

**AI Doc / Code Doc:**
- What exactly is being documented? (specific system, feature, API — not generic)
- Who reads this? (developer, ops, end user — be specific)
- What doc type from the 17 valid types?

### When to Ask Follow-Up Questions

Ask follow-up questions when:
- An answer is vague ("it should help users" → "help them do what specifically?")
- A critical field is missing (audience, trigger phrase, auth method)
- The scope is unclear ("document the API" → "which endpoints? all of them, or specific ones?")
- You'd have to guess to proceed

**The rule:** One specific question is always better than generating the wrong thing. Ask until you could hand these requirements to a different AI and it would build the same thing.

---

## Stage 3: Generate — Produce the Docs

### Output Order by Build Type

**Claude Project** — generate in this order:
1. `CLAUDE.md` (master navigation, ≤200 lines)
2. `PROJECT_INSTRUCTIONS_[Name].md` (500-800 words, 6 sections)
3. `config/domain_definitions.json`
4. `config/token_budgets.json`
5. `README.md` (3-step setup: create → sync → paste)
6. Key SYSTEM guides for this project's domain

**Skill** — generate in this order:
1. `skills/{name}/SKILL.md` (YAML frontmatter + body ≤500 lines)
2. `skills/{name}/references/` files (if needed)
3. `skills/{name}/evals.json` (3-10 test prompts, always)

**MCP Server** — generate in this order:
1. `{system}-setup-guide.md` (install + auth + verify)
2. `{system}-api-reference.md` (every tool documented)
3. `{system}-troubleshooting.md` (top 5-7 errors with exact signatures)
4. `{system}-auth-guide.md` (if complex OAuth/service account)

**AI / Code Doc** — generate one doc using `DOC_CANONICAL_TEMPLATE.md`, pass all 5 gates.

### Quality Gates (Apply to Every Output)

Run all 5 gates before delivering. See `SYSTEM_Exit_Rules.md`. Minimum score: 85/100.

---

## Stage 4: Activate — Deploy / Install / Configure

This stage is where most users get stuck. Guide through every step.

### Activating a Claude Project

**Step 1: Create the project on claude.ai**
1. Go to [claude.ai](https://claude.ai)
2. Click "New Project" in the left sidebar
3. Give it a name matching your generated `CLAUDE.md` project name
4. Project is created but empty

**Step 2: Paste project instructions**
1. Open the generated `PROJECT_INSTRUCTIONS_[Name].md`
2. Copy the full contents
3. In your Claude project, click "Set project instructions" (above the knowledge base area)
4. Paste and save
5. Instructions take effect immediately for all new conversations

**Step 3: Upload knowledge base**
1. Click "+" in the "Project knowledge" right-side panel
2. Upload files: select all `.md` files from the `system/guides/` and `system/templates/` folders
3. For a GitHub-hosted folder: paste the repo URL, select relevant folders, click "Sync now"
4. Files are indexed automatically (RAG activates on paid plans when content exceeds context)

**Important limits:**
- Max 30 MB per file
- File types: PDF, DOCX, TXT, MD, HTML, CSV, XLSX, ODT, RTF, EPUB
- RAG (auto-scaling to 10x context) requires paid plan (Pro, Max, Team, Enterprise)
- Free plan: context window only (~200K tokens total for all knowledge + conversation)

**Step 4: Test the project**
Send this exact message to verify setup: "What is your role in this project, and what file should I share if I want to generate a setup guide?"
A correctly configured project will reference its project instructions and name at least one system file.

**Step 5: Share with team (Team/Enterprise only)**
1. Click "Share" or "Manage access" in the project
2. Add team members by email
3. Set permissions (view or edit)
4. All members share the same knowledge base and instructions

Note: Cowork projects are local to one machine and cannot be shared. For team sharing, use claude.ai Projects (Team/Enterprise plan).

---

### Installing a Skill (.skill file)

**Step 1: Package the skill**
```bash
python -m scripts.package_skill skills/{name}/
```
This produces `{name}.skill` in the current directory.

**Step 2: Install in Cowork or Claude Code**
- **Cowork:** Open Settings → Plugins → Install from file → select `.skill` file
- **Claude Code:** Place in `.claude/skills/{name}/` directory OR install via plugin manager

**Step 3: Verify trigger**
Type the trigger phrase in a new session. If Claude doesn't invoke the skill:
- Check the `description` field in SKILL.md frontmatter (this is what controls triggering)
- Make the description more specific and "pushy" — Claude under-triggers by default
- Repackage and reinstall

**Step 4: Run evals**
Use the generated `evals.json` to test 3-10 prompts. Check:
- Does the skill trigger on prompts where `should_trigger: true`?
- Does it NOT trigger on prompts where `should_trigger: false`?
- Does output contain items listed in `expected_output_contains`?

---

### Setting Up an MCP Server

**Step 1: Choose transport**
- **Local (STDIO):** Runs on your machine, single user. Best for developer tools, system access.
- **Remote (HTTP):** Runs on a server, multi-user. Best for team integrations, cloud APIs.
- SSE is deprecated — use HTTP for remote.

**Step 2: Add to Claude Code config**
```bash
# HTTP server:
claude mcp add {name} --transport http https://your-server.com

# Local STDIO server:
claude mcp add {name} --transport stdio node /path/to/server.js
```
Or edit directly: `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)

**Step 3: Restart Claude Code** after any config change.

**Step 4: Verify**
Type `/mcp` in Claude Code — server should appear as "connected."
If "disconnected": run `claude --mcp-debug` and check logs.

**Step 5: For Claude.ai (non-Code)**
Custom MCP servers are not supported on claude.ai chat directly. Options:
- Use Cowork connectors (pre-built for Slack, Notion, Jira, Figma, Google Calendar, Gmail, Ahrefs, etc.)
- Use Claude Code for custom MCP
- Install as a Cowork plugin (if packaged)

**Common errors:**
| Error | Cause | Fix |
|---|---|---|
| Server disconnected | Config syntax error or server crashed | Validate JSON config: `python -m json.tool config.json` |
| JSON parse error | Server writing to stdout instead of stderr | Fix server logging — only JSON-RPC to stdout |
| Connection refused | Server not running | Test server independently first |
| Wrong tool behavior | Params mismatch | Check MCP Inspector for exact request/response |

---

## Stage 5: Verify — Confirm It Works

### Verification Questions (Ask After Activation)

**Claude Project:**
- "Send this test message and share what Claude replies: 'What files should I share to generate a setup guide?'"
- "Does Claude reference the project instructions or system files in its response?"
- "Ask Claude to do one of the 3-5 tasks you listed in intake. Does it behave as expected?"

**Skill:**
- "Type the trigger phrase in a fresh session. Did the skill activate?"
- "Share the evals.json output — how many of 10 test cases passed?"
- "Did the skill trigger on the should-NOT-trigger test case? (It shouldn't.)"

**MCP Server:**
- "Type `/mcp` in Claude Code — is the server listed as connected?"
- "Ask Claude to [first tool in your API reference]. Did it return the expected data?"
- "Trigger one of the documented error scenarios — did Claude handle it with the defined fallback?"

### What to Do When Verification Fails

| Failure | Most likely cause | Fix |
|---|---|---|
| Project ignores instructions | Instructions not saved or not referenced by Claude | Re-paste instructions, add "Read CLAUDE.md first" as Do #1 |
| Skill doesn't trigger | Description too vague or not installed | Rewrite description (more specific, more trigger phrases), repackage |
| Skill triggers too often | Description too broad | Narrow trigger conditions, add "only when..." constraints |
| MCP shows disconnected | Config error or server not running | Check JSON syntax, test server standalone |
| MCP returns wrong data | Tool params incorrect | Use MCP Inspector to compare expected vs actual request |
| Doc fails quality gate | Missing sections, vague content, code standards | Re-run gates, quote specific rule from SYSTEM_* file |

### Log What's Missing (DEBT)

If the system works but has gaps — an untested error case, a missing doc, a known limitation — log it in `backlog/SYSTEM_DEBT.md` before marking Gate 5 pass. Unlogged gaps become hidden production failures.

---

## Available Skills (341 Total — Check Before Building)

14 categories of pre-built skills. Check before creating new ones:

| Category | Count | Examples |
|---|---|---|
| AI & LLMs | 10 | `ai-evals`, `building-with-llms`, `prompt-engineer`, `rag-architect` |
| Analytics & SEO | 24 | `keyword-research`, `seo-audit`, `rank-tracker`, `content-gap-analysis` |
| Brand & Marketing | 28 | `brand-voice`, `cold-email`, `email-sequence`, `social-content` |
| Content & Copywriting | 13 | `copywriting`, `content-strategy`, `copy-editing`, `writing-prds` |
| Design & UX | 31 | `ux-research`, `design-critique`, `accessibility-review`, `design-handoff` |
| Engineering | 67 | `code-review`, `api-design`, `architecture`, `debugging`, `test-writing` |
| Growth & CRO | 18 | `ab-testing`, `conversion-optimization`, `funnel-analysis` |
| Leadership & Management | 27 | `okrs`, `hiring`, `performance-reviews`, `team-planning` |
| Personal Effectiveness | 12 | `productivity`, `decision-making`, `writing` |
| Product Management | 29 | `prds`, `roadmapping`, `user-stories`, `prioritization` |
| Sales & Revenue | 17 | `deal-review`, `pipeline-analysis`, `outreach`, `forecasting` |
| Startup & Strategy | 13 | `business-model`, `competitive-analysis`, `fundraising` |
| Documents & Files | 22 | `docx`, `pptx`, `pdf`, `xlsx`, `canvas-design` |
| Other | 30 | Various |

Full catalog: `skills_map.md` (341 skills)
