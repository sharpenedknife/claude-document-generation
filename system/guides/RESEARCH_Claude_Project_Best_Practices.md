# Research: How People Actually Build AI Systems
**Compiled:** April 2026
**Sources:** Anthropic docs, modelcontextprotocol.io, Cursor community, practitioner guides, Claude Code docs, Skills Manager project instructions, skills_map.md (341 skills)
**Purpose:** Ground the Documentation Builder in what actually works in production — not invented rules.

---

## TL;DR — 7 Things That Matter Most

1. **Start single-agent.** One LLM + tools + system prompt handles 80% of real use cases. Add complexity only when forced.
2. **CLAUDE.md / project instructions under 300 lines, 5–7 rules max.** More rules = lower compliance per rule. The curse of instructions is real.
3. **Each doc must stand alone.** AI agents process pages without navigation context. If a page depends on reading others first, it fails in RAG.
4. **Complete runnable examples beat descriptions.** Partial snippets cause hallucination. If the code doesn't run, it shouldn't be in the doc.
5. **MCP tools, resources, and prompts are distinct.** Confusing them breaks the integration architecture.
6. **Self-checking agents are fundamentally more reliable.** Build the output check into the workflow, not as an afterthought.
7. **Living docs beat perfect docs.** Stale rules cause agent failure. Update on every meaningful change.
8. **The skill description is the entire trigger.** Claude decides whether to load a skill based on description alone. Under-triggers by default — descriptions must compensate with specific phrases and "always use when."
9. **341 skills already exist.** Check before building. The majority of use cases are covered.

---

## 1. How People Build AI Agents

**Source:** Anthropic 2024/2025, Hu et al. arXiv 2512.13564, ExpeL (AAAI 2024), Yao et al. ICLR 2023, Wang et al. ACL 2023, Microsoft Azure Architecture Center 2026, AWS Bedrock 2025
**Full reference:** `SYSTEM_Agent_Architecture.md`

### Start Single-Agent — Always

The dominant production pattern is a single LLM with tools. Multi-agent adds ~15× token overhead (Anthropic 2025) — that overhead must be justified by measured quality improvement, not architectural preference.

```
Single agent (default):
User → LLM + System Prompt + Tools → Output

Multi-agent (only when forced):
User → Orchestrator → [Subagent A | Subagent B] → Orchestrator → Output
```

Add subagents only when: task cannot fit in one context window, subtasks require distinct non-overlapping tool sets, or true parallel execution is needed.

### The Four-Part Framework

Every agent has exactly four components (Anthropic 2024; Hu et al. 2025):

| Component | Role |
|---|---|
| **LLM** | Reasoning engine — interprets input, generates plans |
| **Contextual Memory** | Persists facts, traces, and working state across steps |
| **External Functions / Sub-agents** | Tools or child agents the LLM invokes |
| **Routing** | Classifies input and dispatches to specialized handlers |

### Four Orchestration Patterns

| Pattern | When to Use |
|---|---|
| **Sequential** | Fixed, ordered stages (draft → review → polish). Use for docgen. |
| **Parallel (Fan-out/Fan-in)** | Independent subtasks that can run concurrently. Use for multi-section generation. |
| **Supervisor** | Dynamic delegation; subtasks unknown upfront. Use when routing complexity outgrows rules. |
| **Planning Agent** | Complex open-ended problems requiring iterative replanning. Use as last resort. |

### Memory Types — Three Layers

| Type | What it stores | In this system |
|---|---|---|
| **Factual** | Domain knowledge, templates, rules | Claude Project knowledge base, system guides |
| **Experiential (Decision Trace)** | Past decisions, quality outcomes, insights from failures | `metrics/LOG_Generation.md`, `backlog/SYSTEM_DEBT.md` |
| **Working** | Current task context, in-progress state | Active conversation window |

**Decision Trace is the self-improvement mechanism.** ExpeL (AAAI 2024) proved agents that store natural-language insights from prior runs improve consistently — without weight updates. Every quality gate failure logged to DEBT.md is experiential memory for the next run.

### Planning: ReAct vs Plan-and-Execute

**ReAct (Think → Act → Observe):** One LLM call per tool invocation. Best for exploratory, unknown-path tasks. Higher cost. Default in LangChain, AWS Bedrock Agents.

**Plan-and-Execute:** Single planning call upfront, cheaper execution. Best for predictable, fixed-stage workflows. This is what docgen uses and what Skills implement.

For docgen: Plan-and-Execute primary, ReAct as fallback within individual steps for unexpected input.

### Production Best Practices (cited)

1. Invest more time in tool descriptions than system prompts. Anthropic's SWE-bench team found rewriting tool descriptions cut task completion time 40%. (Anthropic 2025)
2. Persist a `progress.md` outside the context window for runs exceeding 50K tokens. Reload at each planning step. (Anthropic 2025)
3. Use programmatic schema validation (JSON Schema, YAML lint) between stages — not LLM checks. LLM-as-judge is for semantic quality only (0.0–1.0). (Anthropic 2025)
4. Cap ReAct at `max_iterations=5`, Plan-and-Execute at `max_replans=2`. Unbounded loops are the top cause of runaway cost. (AWS 2025, Microsoft Azure 2026)
5. Enable production tracing from day one. It was the prerequisite to systematic multi-agent debugging. (Anthropic 2025)

### Self-Correction Is the Highest-ROI Feature

Agents that check their own output before delivering are fundamentally more reliable:

```
Generate output → Validate (programmatic schema check) → Score (LLM-as-judge) → If fail: rewrite → Deliver
```

This is the 5-gate quality framework in practice.

### Common Failure Modes

| Failure | Fix |
|---|---|
| **Compounding errors** | Insert schema validation gates between stages; halt on violation |
| **Tool misuse** | Document every tool with explicit input format, edge cases, example call |
| **Memory drift** | Compact context at 80% window capacity; persist key facts externally |
| **Autonomy-oversight tension** | Define explicitly which actions require human confirmation |
| **Infinite delegation loops** | Set iteration caps; implement circuit-breaker; log every handoff |

---

## 2. How to Build MCP Servers

**Source:** modelcontextprotocol.io, FastMCP docs, Anthropic MCP guide

### The Three-Part Model

Every MCP server exposes exactly three types of capabilities:

| Type | Controlled by | Purpose |
|---|---|---|
| **Tools** | LLM (model decides when to call) | Actions and data retrieval — the most common type |
| **Resources** | Application (host controls access) | File contents, database records, persistent data |
| **Prompts** | User (explicit invocation) | Reusable prompt templates for specific tasks |

Most integrations only need Tools. Resources and Prompts are added when the use case requires app-controlled data or user-invoked templates.

### Language: TypeScript or Python — Both Work

Choose based on team comfort. The wire protocol is identical.

| | TypeScript | Python |
|---|---|---|
| Best for | Node/React teams, type safety | Data teams, fast iteration |
| Schema generation | Manual or Zod | Auto from docstrings (FastMCP) |
| Dev speed | Moderate | Fast with FastMCP |
| Production stability | High | High |

### Critical Rules

**Never write to stdout in STDIO servers.** The MCP protocol uses stdout for JSON-RPC. Any debug print to stdout corrupts the message stream and breaks the connection. Use stderr for logging.

**Test with a real client before documenting.** "No server instructions are better than poorly written instructions." A documented server that doesn't work as documented is worse than no docs.

**Tool names must be stable.** Renaming a tool breaks all clients using that name. Version-bump the server if you rename tools.

**Auth is not optional.** Even internal tools need auth. Use existing security libraries — never write homegrown token validation.

### Standard Folder Structure (TypeScript)

```
mcp-server-name/
├── src/
│   ├── index.ts        ← Server entry point, tool registrations
│   ├── tools/          ← One file per tool or tool group
│   └── types.ts        ← Shared type definitions
├── package.json
├── tsconfig.json
└── README.md           ← Setup, auth, tool list, example calls
```

### Documentation Requirements Per Tool

Every tool needs: purpose (one sentence), parameters table (name/type/required/description), return shape (JSON example), one complete example call, error table (message/cause/fix).

---

## 3. Writing Docs for AI to Consume

**Source:** llms.txt spec, Anthropic context engineering docs, RAG best practices

### The Core Insight

"LLM-powered assistants often process individual pages without broader navigation context. Each page must stand on its own."

Human documentation assumes a reader who navigates, clicks, reads prior pages. AI documentation assumes a reader who receives one page in isolation and must understand it completely from that page alone.

### The Three-Layer Stack

```
llms.txt          ← Machine-readable sitemap (which pages exist, what they're for)
    ↓
CLAUDE.md         ← Session-level context (what this project is, commands, gotchas)
    ↓
Individual docs   ← Self-contained pages with frontmatter + complete examples
```

**llms.txt** is a plain-text file at the root of a project listing all AI-relevant files with one-line descriptions. It tells AI systems where to look without requiring them to crawl.

**CLAUDE.md** is the session-initialization file. In Claude Code it loads automatically. In Claude.ai Projects it loads if project instructions reference it. It answers: what is this project, where do things live, what commands exist, what are the gotchas.

**Individual docs** carry their own context via YAML frontmatter. An AI reading a single doc should be able to answer: what is this, who is it for, what prerequisites are needed, what does success look like.

### What Works vs What Fails

| Format | Works for AI | Fails for AI |
|---|---|---|
| Tables | ✅ Parseable structure | |
| Code blocks with language tags | ✅ Runnable, extractable | |
| Numbered steps with expected output | ✅ Precondition/postcondition chain | |
| YAML frontmatter | ✅ Filterable metadata | |
| Narrative prose paragraphs | | ❌ Hard to chunk, no structure |
| Partial code snippets | | ❌ Causes hallucination to fill gaps |
| Navigation-dependent content ("see above") | | ❌ Breaks when page is read in isolation |
| Inline links everywhere | | ❌ Noise; use frontmatter links instead |

### Complete Examples Are Non-Negotiable

If a code example is partial, Claude will complete it — and may complete it incorrectly. Every code block must either be complete and runnable, or explicitly marked as a snippet with a link to the full version.

---

## 4. Vibe Coding Rules / CLAUDE.md / Project Instructions

**Source:** Cursor community guides, Claude Code docs, practitioner posts (2025–2026)

### The Three Formats

| Format | Tool | Scope | When to use |
|---|---|---|---|
| **CLAUDE.md** | Claude Code | Session/project | Architecture, commands, code style, gotchas |
| **Project Instructions** | Claude.ai Projects | Project-wide | Persona, workflow rules, what to do/not do |
| **.cursorrules** | Cursor | File/directory | Cursor-specific AI behavior in IDE |
| **AGENTS.md** | Multi-agent | Cross-tool | Emerging standard for agent meshes |

### The Curse of Instructions

Research finding: more rules = lower compliance per rule. A system prompt with 50 rules follows each rule ~60% of the time. With 7 rules, compliance per rule rises to ~90%.

**Implication:** Project instructions must stay lean. Include only rules Claude won't follow by default. Every added rule pushes out compliance on all existing rules.

### CLAUDE.md Standard Structure (WHY/WHAT/HOW)

```markdown
# [Project Name]

## What This Is
[One sentence. What is this project and why does it exist?]

## Commands
[Exact commands Claude needs to run. Copy-pasteable.]
- Build: `npm run build`
- Test: `npm test`

## Architecture
[File map. Where things live. Why.]

## Code Style
[3-5 rules with examples. Not prose — rules.]

## Important Notes
[2-3 gotchas that trip up anyone new. Non-obvious things only.]
```

**Length:** Under 300 lines. Shorter is better. If you're writing paragraphs, rewrite as rules.

### Project Instructions Standard Structure (6 sections)

1. **Role** — who Claude is in this project (one paragraph max)
2. **First action** — what to read before responding (always: CLAUDE.md + primary rules file)
3. **Truth sources** — which files Claude quotes from (list, not prose)
4. **Response format** — length, structure, tone
5. **Do's** — 3–5 explicit positive behaviors
6. **Don'ts** — 3–5 explicit prohibitions (with WHY — agents follow rules they understand)

**Word count:** 500–800 words total. Under 500 is fine. Over 800 degrades compliance.

### Update Continuously — Stale Rules Cause Failures

"The most common cause of agent failure in production is stale system prompts." Rules that were true when written become false as the project evolves.

**Rule:** Update CLAUDE.md every time: folder structure changes, a command changes, a new gotcha is discovered, a builder or rule is deprecated. Include `Last updated: YYYY-MM-DD` in every instruction file.

---

## 5. Skills Ecosystem — How the 341-Skill Library Works

**Source:** Skills Manager project instructions, skills_map.md, real SKILL.md format from production plugins

### What Skills Are (the Real Format)

A Skill is a `SKILL.md` file with YAML frontmatter packaged as a `.skill` file. It is **not** a markdown document — it is a playbook Claude follows when the description triggers.

```
skill-name/
├── SKILL.md              ← Required: YAML frontmatter + playbook body
├── references/           ← Optional: docs/templates loaded on demand
├── scripts/              ← Optional: Python/bash for deterministic ops
├── assets/               ← Optional: fonts, icons, templates
└── evals.json            ← Always generate: 3–10 test prompts
```

Packaged with: `python -m scripts.package_skill skills/{name}/`

### The Description Field Is the Entire Triggering Mechanism

Claude sees only skill names + descriptions before deciding whether to load a skill. The full body is invisible until the skill is loaded.

**Description must be 50–120 words.** Too short → won't trigger. Too long → wastes context budget.

**Claude under-triggers by default.** Descriptions must be slightly "pushy" — enumerating specific contexts, using "always use when", "whenever", listing 3–5 exact trigger phrases. A vague description means the skill never runs.

```yaml
# BAD — vague, will not trigger reliably:
description: Helps with campaign planning.

# GOOD — specific, pushy, 3+ trigger phrases:
description: >
  Generates full campaign briefs with objectives, audience segments, messaging,
  channel strategy, content calendar, and success metrics. Use whenever the user
  mentions campaign, launch, go-to-market, GTM, or asks to plan marketing activity.
  Always use this skill when the user has a deadline or product to promote. Routes
  to channel-specific content generation after brief is approved.
```

### The 341-Skill Library — Categories

| Category | Count | Key skills |
|---|---|---|
| Engineering | 67 | `code-review`, `api-design`, `debugging`, `architecture`, `test-writing` |
| Product Management | 29 | `prds`, `roadmapping`, `user-stories`, `prioritization` |
| Design & UX | 31 | `ux-research`, `design-critique`, `accessibility-review`, `design-handoff` |
| Brand & Marketing | 28 | `brand-voice`, `cold-email`, `email-sequence`, `social-content` |
| Analytics & SEO | 24 | `keyword-research`, `seo-audit`, `rank-tracker`, `content-gap-analysis` |
| Leadership | 27 | `okrs`, `hiring`, `performance-reviews`, `team-planning` |
| Documents & Files | 22 | `docx`, `pptx`, `pdf`, `xlsx`, `canvas-design` |
| Sales & Revenue | 17 | `deal-review`, `pipeline-analysis`, `outreach`, `forecasting` |
| Growth & CRO | 18 | `ab-testing`, `conversion-optimization`, `funnel-analysis` |
| AI & LLMs | 10 | `ai-evals`, `prompt-engineer`, `rag-architect`, `building-with-llms` |
| Content & Copywriting | 13 | `copywriting`, `content-strategy`, `copy-editing` |
| Startup & Strategy | 13 | `business-model`, `competitive-analysis`, `fundraising` |
| Personal Effectiveness | 12 | `productivity`, `decision-making`, `writing` |
| Other | 30 | Various |

**Rule:** Check the library before building. Many skills already exist. Build only what's missing or distinct.

### Evals.json — Always Required

Every skill must ship with test prompts. These are the acceptance tests.

```json
{
  "skill": "skill-name",
  "test_prompts": [
    {
      "id": "core-use-case",
      "prompt": "realistic user input for main use case",
      "should_trigger": true,
      "expected_output_contains": ["key element 1", "key element 2"]
    },
    {
      "id": "edge-case",
      "prompt": "input testing an edge case",
      "should_trigger": true,
      "expected_output_contains": ["what should appear"]
    },
    {
      "id": "should-not-trigger",
      "prompt": "similar-looking input that should NOT use this skill",
      "should_trigger": false
    }
  ]
}
```

Prompts must be: realistic (messy user language, not perfect), substantive, and include at least 1 should-NOT-trigger case.

---

## 6. Deployment Patterns — How to Get Things Running

**Source:** Anthropic docs, Claude Code CLI docs, SYSTEM_User_Journey.md

### Claude Projects (claude.ai) — Full Setup Flow

```
1. Create project on claude.ai → New Project → name it
2. Paste project instructions → "Set project instructions" field (above knowledge panel)
3. Upload knowledge base → "+" in Project knowledge panel
   - File types: PDF, DOCX, TXT, MD, HTML, CSV, XLSX, ODT, RTF, EPUB
   - Max 30 MB per file
   - GitHub: paste repo URL → select folders → "Sync now"
4. RAG activates automatically on paid plans (Pro, Max, Team, Enterprise)
   when content exceeds context window → scales to 10x context
5. Test: send "What is your role and what file should I share to generate a setup guide?"
   → correctly configured project references instructions and names a system file
6. Team sharing (Team/Enterprise only): Share → Add by email → Set permissions
```

**Free plan limitation:** Context window only (~200K tokens total). No auto-RAG.

**Cowork limitation:** Projects are local — not sharable. For team sharing, use claude.ai Projects.

### Skills (.skill files) — Install and Verify

```
Package:   python -m scripts.package_skill skills/{name}/
Install:   Cowork → Settings → Plugins → Install from file → .skill file
           Claude Code → .claude/skills/{name}/ directory OR plugin manager
Verify:    Type trigger phrase in new session
           → skill doesn't trigger? Rewrite description (more specific, more trigger phrases), repackage
           → skill triggers too often? Add "only when..." constraints to description
Test:      Run evals.json prompts manually — check should_trigger cases both ways
```

### MCP Servers — Setup and Debug

```
# Add HTTP server (remote, multi-user):
claude mcp add {name} --transport http https://your-server.com

# Add STDIO server (local, single-user):
claude mcp add {name} --transport stdio node /path/to/server.js

# Or edit directly:
~/Library/Application Support/Claude/claude_desktop_config.json   (macOS)
%APPDATA%\Claude\claude_desktop_config.json                        (Windows)

# Verify:
/mcp    → server should show as "connected"
→ disconnected? Run: claude --mcp-debug

# Debug tool behavior:
MCP Inspector (npx @modelcontextprotocol/inspector) → see exact request/response
```

**Transport choice:** STDIO for developer tools, local file access, single-user. HTTP for team integrations, cloud APIs, multi-user. SSE is deprecated — use HTTP for all remote servers.

### Common Deployment Failures

| Failure | Most likely cause | Fix |
|---|---|---|
| Project ignores instructions | Not pasted or not saved | Re-paste, confirm "Instructions saved" message |
| Skill never triggers | Description too vague | Rewrite: more specific, add trigger phrases, use "always use when" |
| Skill triggers on everything | Description too broad | Add "only when..." and negative constraints |
| MCP disconnected | Config JSON syntax error | Validate: `python -m json.tool config.json` |
| MCP wrong behavior | Tool params mismatch | Use MCP Inspector to compare expected vs actual |
| Doc fails quality gate | Missing sections, vague content | Re-run all 5 gates, quote specific rule from SYSTEM_* file |

---

## 7. Applied to This System

| Research finding | Where it's applied |
|---|---|
| 5–7 rules max per instruction file | Project instructions capped: 5 Do's + 5 Don'ts |
| Each page stands alone | Every output doc requires self-contained frontmatter |
| Complete examples only | Gate 3: partial code snippets = fail |
| CLAUDE.md < 300 lines | Enforced in `builders/claude-project/BUILDER_Rules.md` |
| ReAct for exploration, Plan-Execute for workflows | Skills use Plan-Execute; open-ended generation uses ReAct |
| MCP Tools vs Resources vs Prompts | `builders/mcp/BUILDER_Questions.md` Q2/Q3 separate these |
| Self-correction built in | 5-gate quality framework is the self-correction loop |
| Update continuously | Version stamp required in all CLAUDE.md and project instructions |
| Queries at end of long-context prompts improves quality ~30% | System guides referenced, not embedded inline in project instructions |
| Description field = trigger mechanism | `builders/skill/BUILDER_Rules.md` Rule 1; check before building |
| 341 skills exist — check first | Q0 gate in `builders/skill/BUILDER_Questions.md` |
| Evals.json always required | `builders/skill/BUILDER_Rules.md` Rule 8; Gate 5 prerequisite |
| Deployment is a stage, not an afterthought | `SYSTEM_User_Journey.md` Stage 4 (Activate) + Stage 5 (Verify) |
