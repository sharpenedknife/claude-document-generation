# Documentation Builder — System Reference
> Consolidated reference: all system guides.
> For individual source files: https://github.com/sharpenedknife/claude-document-generation

========================================================================
RESEARCH Claude Project Best Practices
========================================================================

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


========================================================================
SYSTEM AI First Format
========================================================================

# AI-First Documentation Format Guide

## Core Principle

Documentation is read by both humans AND AI systems (Claude Projects, vector search, RAG pipelines, agents). Optimize for both simultaneously through structured metadata and intelligent chunking.

---

## YAML Frontmatter (Required for all docs)

Every doc must start with metadata block:

```yaml
---
doc_type: project-setup|claude-md|project-instructions|system-guide|how-to|reference|feature|process|update|setup-guide|api-guide|architecture|adr|troubleshooting|config-reference|schema-reference|command-reference
audience: beginner|intermediate|advanced|all
difficulty: easy|medium|hard
time_estimate: "5-minutes|15-minutes|30-minutes|1-hour|varies"
prerequisites: [tool_name_version, access_type, knowledge_area]
related_docs: [doc_title_1, doc_title_2]
tags: [keyword1, keyword2, keyword3]
updated: YYYY-MM-DD
status: production|draft|deprecated
---
```

**Why it matters:**
- Claude can filter docs by audience/difficulty instantly
- Projects know prerequisites before reading content
- Related docs are discoverable programmatically
- Search systems rank by recency (updated field)
- Deprecated docs don't confuse AI

**Example:**
```yaml
---
doc_type: setup-guide
audience: beginner
difficulty: easy
time_estimate: "15-minutes"
prerequisites: [nodejs_16+, npm_8+, git_2.30+]
related_docs: [How to Install Dependencies, Troubleshooting Node Issues]
tags: [installation, nodejs, npm, setup]
updated: 2026-04-02
status: production
---
```

---

## Section Structure for AI Extraction

### 1. Overview (1-2 sentences, MUST have)
**Machine reason:** Claude extracts this for search results, project summaries.
**Human reason:** Reader knows immediately what this is.

```markdown
# [Action Verb + Noun]

One sentence: what you'll accomplish.
One sentence: why you need this.

**Search keywords:** keyword1, keyword2
```

The `**Search keywords:**` line helps vector embeddings understand doc intent.

---

### 2. Prerequisites (Structured for parsing)

**For AI:** Use consistent structure that's easy to parse.
**For humans:** Clear verification commands.

```markdown
## Prerequisites

### Level 1: Tools & Software
- **Node.js 16+** (required)
  - Check: `node --version`
  - Install: https://nodejs.org/en/download/ (LTS v16+)
  - Why: Native Promise/async support needed

- **npm 8+** (required)
  - Check: `npm --version`
  - Install: `npm install -g npm@latest`
  - Why: Workspace feature requires npm 8+

### Level 2: Access & Keys
- **GitHub account with repo access** (required)
  - Check: `git clone <repo>` works without password
  - Get: Ask @team in Slack
  - Why: Need to pull code

### Level 3: Knowledge
- **Basic terminal commands** (optional, can learn)
  - Guide: https://... (5 min read)
  - Why: Makes troubleshooting easier

### Level 4: Current State
- **Project cloned locally**
  - Check: `ls -la` shows project files
  - Setup: `git clone <repo> && cd <repo>`
  - Why: All commands assume you're in project dir
```

**Why structured this way for AI:**
- Level numbering is parseable
- Boolean flags (required/optional) are extractable
- Check/Install/Why are labeled sections
- Claude can build prerequisite chains automatically

---

### 3. Step-by-Step Instructions (Chunked for RAG)

Break into logical chunks, each identifiable by Claude:

```markdown
## Setup

### Step 1: Initialize Project
1. Run: `npm init -y`
   Expected: `package.json` created with default values
   
   **AI metadata:** 
   - Precondition: npm 8+
   - Postcondition: package.json exists
   - Common error: "Command not found"

### Step 2: Install Dependencies
1. Run: `npm install express`
   Expected: `node_modules/` folder created, `package-lock.json` updated
   
   **AI metadata:**
   - Precondition: package.json exists
   - Postcondition: Dependencies installed
   - Related section: "Troubleshoot: npm install failures"

### Step 3: Verify Setup
1. Run: `npm list`
   Expected: Show installed packages tree
   
   **AI metadata:**
   - Verification step
   - Postcondition: Setup confirmed
   - If fails: Jump to "Troubleshooting" section
```

**Why this structure:**
- Claude can chunk at step level for RAG
- Preconditions/postconditions show dependencies
- Cross-references help Claude navigate
- "Common error" links anticipate questions

---

### 4. Expected Output / Success Indicator (Exact matches)

```markdown
## What Success Looks Like

After completing setup:

| Check | Expected Result | Command |
|-------|-----------------|---------|
| **Files exist** | `package.json`, `package-lock.json` present | `ls -la \| grep package` |
| **Packages installed** | `node_modules/` folder with 100+ packages | `npm list \| head -20` |
| **Module loadable** | Can require module in Node REPL | `node -e "require('express')"` |
| **No errors** | Zero error messages in output | `npm list 2>&1 \| grep error` |

**If any check fails:** Jump to relevant troubleshooting section
```

**Why table format for AI:**
- Easily parseable structure
- Each row is independent (embeds well)
- Links to troubleshooting are discoverable
- Claude can run checks programmatically

---

### 5. Troubleshooting (Indexed by error)

```markdown
## Troubleshooting

### Error: "command not found: npm"
**Root cause:** npm not installed or not in PATH
**Fix steps:**
1. Check: `npm --version`
2. If error: Install Node from https://nodejs.org/
3. Restart terminal: Close and reopen terminal window
4. Verify: `npm --version` (should show v8+)

**AI metadata:**
- Error signature: "command not found: npm"
- Precondition check: nodejs_16+
- Related section: Prerequisites → Level 1: Tools

---

### Error: "npm ERR! code ERESOLVE"
**Root cause:** Dependency conflict (npm 7+ strict mode)
**Fix steps:**
1. Try: `npm install --legacy-peer-deps`
2. If fails: `npm cache clean --force && npm install`
3. Check: `npm list` (verify clean output)

**AI metadata:**
- Error signature: "ERESOLVE"
- Precondition: npm 7+
- Solution type: dependency resolution
- Related section: "Common npm issues"
```

**Why metadata in troubleshooting:**
- Claude can match error messages to solutions
- "Error signature" field enables exact pattern matching
- Precondition checks prevent bad advice
- Related sections create knowledge graph

---

## Chunking Strategy for RAG (Important for Projects)

Documents should be chunked at **logical boundaries**, not token limits:

```
Chunk 1: Frontmatter + Overview + Prerequisites
Chunk 2: Step 1 + Step 2 (related pair)
Chunk 3: Step 3 + Expected Output
Chunk 4: Troubleshooting section (split by error type if >5 errors)
```

**Why not token-based chunking:**
- Breaks mid-step (confusing)
- Separates prereq from step that needs it
- Splits error from solution

**Use logical chunks:**
- Each chunk is complete and self-contained
- Claude can answer questions from single chunk
- Prerequisites flow naturally to steps

---

## Writing Rules for AI-First Docs

1. **Exact commands, not descriptions** — `npm install stripe` not "Install the payment library"
2. **Verifiable output after each step** — Show what terminal displays
3. **Labeled sections for AI parsing** — Use `**AI metadata:**` blocks
4. **Preconditions/postconditions** — Define what must be true before/after
5. **Error signatures, not descriptions** — "command not found: npm" not "npm error occurred"
6. **Cross-references by doc title** — "See: How to Install Dependencies" (not "see above")
7. **Links in metadata** — Keep doc links in prerequisites/related_docs, not inline
8. **Structured tables for options** — Don't paragraph out alternatives
9. **No ambiguous pronouns** — "This file" → "{filename}"
10. **Timestamps in frontmatter** — Not "recently" or "this quarter"

---

## Template: AI-First Setup Guide

```markdown
---
doc_type: setup-guide
audience: beginner
difficulty: easy
time_estimate: "20-minutes"
prerequisites: [nodejs_16+, npm_8+, git]
related_docs: [How to Configure Environment, Troubleshooting Node Issues]
tags: [setup, installation, nodejs, npm]
updated: 2026-04-02
status: production
---

# How to Set Up [Project Name]

Install and verify [project] on your machine in 20 minutes.
You'll have a working development environment ready for the next step.

**Search keywords:** installation, initial setup, first run, bootstrap

---

## Prerequisites

### Level 1: Tools & Software
- **Node.js 16+** (required)
  - Check: `node --version`
  - Install: https://nodejs.org/en/download/
  - Why: Project requires native async/await

- **npm 8+** (required)
  - Check: `npm --version`
  - Install: `npm install -g npm@latest`
  - Why: We use workspaces (npm 8 feature)

- **Git 2.30+** (required)
  - Check: `git --version`
  - Install: https://git-scm.com/download
  - Why: Clone repository and manage versions

### Level 2: Access & Keys
- **GitHub account** (required)
  - Check: `git clone <repo>` succeeds without password
  - Get: Create account at https://github.com/signup
  - Why: Repository access

### Level 3: Knowledge
- **Basic terminal commands** (optional)
  - Guide: https://ubuntu.com/tutorials/command-line-for-beginners (5 min)
  - Why: Easier troubleshooting

### Level 4: Current State
- **Project folder ready**
  - Check: You have an empty folder for the project
  - Setup: `mkdir my-project && cd my-project`
  - Why: Clone will populate this folder

**Ready?** Run this:
```bash
node --version && npm --version && git --version
```
All three should show versions. If any say "command not found," install it.

---

## Setup

### Step 1: Clone Repository
1. Run: `git clone https://github.com/yourorg/project.git && cd project`
   Expected: Folder populated with code files
   
   **AI metadata:**
   - Precondition: Git installed, GitHub access
   - Postcondition: Project folder contains code
   - Files created: All files in repository

### Step 2: Install Dependencies
1. Run: `npm install`
   Expected: `node_modules/` folder created, progress shows package count
   
   **AI metadata:**
   - Precondition: package.json exists
   - Postcondition: node_modules/ exists
   - Time: Usually 1-3 minutes
   - Common error: See "Troubleshooting → npm install failures"

### Step 3: Verify Installation
1. Run: `npm run verify`
   Expected: Output shows "✓ All checks passed"
   
   **AI metadata:**
   - Verification step
   - Postcondition: Setup confirmed working
   - If fails: Go to "Troubleshooting" section

---

## What Success Looks Like

| Item | Check | Expected | Command |
|------|-------|----------|---------|
| **Node** | Version 16+ | `v16.0.0` or higher | `node --version` |
| **npm** | Version 8+ | `8.0.0` or higher | `npm --version` |
| **Code** | Files present | `src/`, `package.json` visible | `ls -la` |
| **Dependencies** | Installed | `node_modules/` folder exists | `test -d node_modules && echo "yes"` |
| **Verification** | Passes | Output says "All checks passed" | `npm run verify` |

If any check fails, go to troubleshooting section below.

---

## Troubleshooting

### Error: "command not found: node"
**Root cause:** Node.js not installed or not in PATH
**Fix:**
1. Install: https://nodejs.org/en/download/
2. Restart terminal (close and reopen)
3. Verify: `node --version`

**AI metadata:**
- Error signature: "command not found: node"
- Precondition needed: nodejs_16+
- Related: Prerequisites → Level 1

### Error: "npm ERR! code ERESOLVE"
**Root cause:** Dependency version conflict
**Fix:**
1. Try: `npm install --legacy-peer-deps`
2. If fails: `npm cache clean --force && npm install`

**AI metadata:**
- Error signature: "ERESOLVE"
- Solution type: dependency conflict
- Related: "How to Manage npm Dependencies"

---

## What's Next

✓ Setup complete. Now:

1. **Configure environment** → See: "How to Configure Environment"
2. **Run first command** → See: "How to Run Your First Script"
3. **Troubleshoot issues** → See: "Common Setup Issues"
```

---

## AI-First Checklist (Before Publishing)

- [ ] Frontmatter present with all 8 fields filled
- [ ] Prerequisites use Level 1-4 structure
- [ ] Each step has precondition/postcondition metadata
- [ ] Error signatures are exact (not descriptions)
- [ ] Verification table uses exact commands
- [ ] All cross-references use doc titles (not "see above")
- [ ] No inline links except in frontmatter/metadata
- [ ] Timestamps in frontmatter, not prose ("recently", "last quarter")
- [ ] Search keywords defined in Overview
- [ ] Related docs listed in frontmatter
- [ ] Can Claude extract every prerequisite programmatically?
- [ ] Can Claude match error messages to troubleshooting sections?

---

## Before → After: Common Conversions

The fastest way to understand AI-first format is to see the transformation.

**Prerequisites — Before (human prose):**
```markdown
You'll need Node.js 16 or higher and npm 8 or higher. Some familiarity with the terminal helps.
```
**After (AI-first):**
```markdown
### Level 1: Tools & Software
- **Node.js 16+** (required) · Check: `node --version` · Install: nodejs.org · Why: native async support
- **npm 8+** (required) · Check: `npm --version` · Install: `npm install -g npm@latest` · Why: workspaces feature
### Level 3: Knowledge
- **Basic terminal** (optional) · Guide: ubuntu.com/tutorials/command-line-for-beginners
**Ready?** `node --version && npm --version`
```

**Steps — Before:**
```markdown
1. Clone the repo   2. Install dependencies   3. Run the setup script
```
**After:**
```markdown
### Step 1: Clone Repository
1. Run: `git clone https://github.com/org/repo.git && cd repo`
   Expected: folder populated with `src/`, `package.json`
   **AI metadata:** Precondition: git + GitHub access · Postcondition: project folder exists
```

**Troubleshooting — Before:**
```markdown
If you get errors installing dependencies, try clearing the npm cache and installing again.
```
**After:**
```markdown
### Error: "npm ERR! code ERESOLVE"
**Root cause:** Dependency version conflict (npm 7+ strict mode)
**Fix:** 1. `npm install --legacy-peer-deps` 2. `npm cache clean --force && npm install`
**AI metadata:** Error signature: "ERESOLVE" · Solution type: dependency conflict
```

**What changed in every case:** vague → specific versions, descriptions → exact commands, prose → labeled structure, no output → expected output shown, generic errors → exact error signatures.

---

## For Claude Projects Users

**When uploading AI-first docs:**

1. Upload all docs to project knowledge base
2. Claude reads frontmatter automatically
3. In project instructions, tell Claude:
   ```
   Use doc frontmatter (doc_type, prerequisites, audience) to:
   - Filter docs by audience level
   - Suggest related docs automatically
   - Check prerequisites before suggesting steps
   - Match user errors to troubleshooting sections
   ```

4. Claude now:
   - Knows which docs are for beginners vs. advanced
   - Can see prerequisite chains
   - Can route users to related docs
   - Can match error messages exactly

**Example:** User asks "I get error 'command not found: npm'" → Claude finds error signature in troubleshooting, suggests fix, links to Prerequisites check.


========================================================================
SYSTEM Agent Architecture
========================================================================

---
doc_type: architecture
domain: SYSTEM
builder_version: "v1.0"
generated_by: research_builder
generated_at: 2026-04-03T00:00:00Z
audience: intermediate
difficulty: medium
time_estimate: "30-minutes"
prerequisites: []
tags: [ai-agents, multi-agent, orchestration, memory, react, plan-and-execute]
status: active
version: "1.0"
last_updated: 2026-04-03
---

# SYSTEM: AI Agent Architectural Patterns

**Purpose:** Ground the docgen pipeline architecture in production-validated patterns. Covers single vs multi-agent decisions, the four-part framework, orchestration topology, memory types, and planning approaches.
**Search keywords:** ai agent architecture, multi-agent orchestration, ReAct framework, agent memory types, supervisor pattern, plan-and-execute, sequential orchestration

---

## 1. Single vs Multi-Agent Decision

Default to a single agent. Add agents only when tasks require distinct tool sets, parallel execution, or exceed a single context window.

| Factor | Single Agent | Multi-Agent | Source |
|---|---|---|---|
| Task decomposability | Subtasks share context and tools | Subtasks are independent with distinct tools | Anthropic 2024 |
| Context window pressure | Total tokens fit within one window | Information exceeds single context window | Anthropic 2025 |
| Latency tolerance | Low-latency required | Higher latency acceptable (multi-agent uses ~15× more tokens than chat) | Anthropic 2025 |
| Error isolation | Acceptable to retry entire chain | Need per-stage rollback and independent failure domains | Microsoft Azure Architecture Center 2026 |

> **Rule:** Start single-agent. The 15× token overhead of multi-agent systems must be justified by a measured quality improvement.

---

## 2. Core Components: The Four-Part Framework

Every agent consists of four primitives (Anthropic 2024; Hu et al., arXiv 2512.13564, 2025):

| Component | Role | Docgen Example |
|---|---|---|
| **LLM** | Reasoning engine — interprets input, generates plans | Selecting doc template based on `doc_type` |
| **Contextual Memory** | Persists facts, traces, and working state across steps | Storing extracted research facts between pipeline stages |
| **External Functions / Sub-agents** | Tools or child agents the LLM invokes to act on environment | `web_search`, `fetch_template`, `validate_yaml` tool calls |
| **Routing** | Classifies input and dispatches to specialized handlers | Directing `architecture` docs to structure-focused agent vs. `tutorial` to step-focused agent |

> Postcondition: you can identify and label the four primitives in any agent system.

---

## 3. Multi-Agent Orchestration Patterns

Four patterns ranked by complexity (Anthropic 2024; Microsoft Azure Architecture Center 2026; AWS Multi-Agent Guidance 2025):

| Pattern | Use Case | Execution Model | When to Choose |
|---|---|---|---|
| **Sequential Orchestration** | Linear pipelines with clear stage dependencies (draft → review → polish) | Agent A output feeds Agent B; deterministic order | Tasks decompose into fixed, ordered subtasks with no parallelism needed |
| **Parallel (Fan-out/Fan-in)** | Independent analyses on same input (multi-section doc generation) | N agents run concurrently; results aggregated by merger | Subtasks are independent and latency reduction matters |
| **Supervisor Pattern** | Dynamic delegation where a coordinator assigns work to specialist agents | Supervisor LLM breaks task → delegates to workers → synthesizes results | Subtasks cannot be predetermined; require runtime planning |
| **Planning Agent** | Complex open-ended problems requiring iterative replanning | Manager maintains task ledger; backtracks and re-delegates as needed | No predetermined solution path; requires human-reviewable plan |

**For docgen:** Sequential Orchestration is the primary pattern (parse → template → generate → validate → assemble). Supervisor is the upgrade path when docgen complexity grows.

---

## 4. Memory Architecture: Three Functional Types

Taxonomy from Hu et al. (arXiv 2512.13564, Dec 2025), corroborated by ACM TOIS survey (2025):

| Memory Type | What It Stores | Retrieval Trigger | Docgen Application |
|---|---|---|---|
| **Factual Memory** | Domain knowledge, schema definitions, template rules | Semantic similarity search at planning time | `DOC_CANONICAL_TEMPLATE` specs and domain vocabulary |
| **Experiential Memory (Decision Trace)** | Past agent decisions, outcomes, extracted insights from completed episodes | Task-type match; analogical recall of prior runs | "Architecture docs with >5 tables scored higher on review" — recalled on future runs |
| **Working Memory** | Active context: current plan, intermediate outputs, tool results | Always loaded; compacted when approaching token limit | Current YAML frontmatter, partially generated sections, validation errors in progress |

### Decision Trace Memory — the self-improvement mechanism

The ExpeL framework (Zhao et al., AAAI 2024) demonstrated that agents storing natural-language insights extracted from trial-and-error trajectories improve consistently as experiences accumulate — without weight updates. In docgen: an agent that failed a quality gate on a prior run can recall *why* it failed and adjust its generation strategy.

**In this system:** The `metrics/LOG_Generation.md` and `backlog/SYSTEM_DEBT.md` files serve as lightweight experiential memory — recording what failed and why so future generation runs avoid the same mistakes.

---

## 5. Planning Approaches: ReAct vs Plan-and-Execute

| Dimension | ReAct (Yao et al., ICLR 2023) | Plan-and-Execute (Wang et al., ACL 2023) |
|---|---|---|
| **Loop** | Think → Act → Observe → repeat | Plan all steps → Execute sequentially → Replan on failure |
| **LLM calls** | One per tool invocation (higher cost) | Single planning call + cheaper per-step execution |
| **Planning horizon** | One step at a time (myopic, adaptive) | Full task decomposition upfront (global, less adaptive) |
| **Failure handling** | Self-corrects at each observation | Must detect failure explicitly and trigger replanning |
| **Best fit** | Exploratory tasks, dynamic environments, unknown tool needs | Well-defined workflows with predictable steps |
| **Adoption** | Default in AWS Bedrock Agents, LangChain, CrewAI | LangGraph Plan-and-Execute, BabyAGI derivatives |

**For docgen:** Plan-and-Execute is primary — document generation follows a predictable structure. ReAct serves as fallback *within* individual steps when an executor encounters unexpected input.

---

## 6. Common Failure Modes

| Failure | Cause | Mitigation |
|---|---|---|
| **Compounding errors** | Early-stage mistakes propagate through sequential pipelines unchecked | Insert programmatic validation gates between stages; halt on schema violation |
| **Tool misuse** | Ambiguous tool descriptions lead agent to select wrong function or pass wrong parameters | Write tool descriptions with explicit input formats, edge cases, and example invocations |
| **Memory drift** | Working memory accumulates stale or contradictory context over long runs | Compact at 80% window capacity; clear tool-result tokens after extraction; persist key facts externally |
| **Autonomy-oversight tension** | Agent acts beyond intended scope; hallucinates actions without grounding | Require confirmation for destructive actions; validate every output against ground-truth |
| **Infinite delegation loops** | Supervisor and workers hand tasks back and forth without resolution | Set max iteration caps (3–5 rounds); implement circuit-breaker patterns; log each handoff |

---

## 7. Production Best Practices

1. **Start with a single agent and one tool.** Add orchestration complexity only after measuring that single-agent fails a defined quality threshold. (Anthropic 2024)
2. **Invest more in tool descriptions than system prompts.** Anthropic's SWE-bench team found a tool-testing agent that rewrote tool descriptions cut task completion time by 40%. (Anthropic 2025)
3. **Implement structured note-taking for runs exceeding 50K tokens.** Persist a `progress.md` outside the context window; reload via retrieval at each planning step. (Anthropic "Context Engineering" 2025)
4. **Validate output between every pipeline stage.** Use programmatic schema checks (JSON Schema, YAML lint) for structure; use LLM-as-judge (0.0–1.0 scale) for semantic quality only. (Anthropic 2025)
5. **Enable production tracing from day one.** Log every tool call, token count, and planning decision. Adding tracing was the prerequisite to systematic debugging of multi-agent failures. (Anthropic 2025)
6. **Cap agent iterations explicitly.** Set `max_iterations=5` for ReAct loops and `max_replans=2` for Plan-and-Execute. Unbounded loops are the top cause of runaway cost. (AWS Bedrock Docs 2025, Microsoft Azure 2026)
7. **Use experiential memory to close the feedback loop.** After each run, extract one natural-language insight from the quality evaluation and persist it to the experiential memory store. (ExpeL, AAAI 2024)

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Agent repeats same tool call 3+ times with identical parameters | Tool returned an error the agent cannot parse | Add structured error responses: `{"error": "INVALID_PATH", "suggestion": "use absolute path"}` |
| Token count exceeds context window mid-pipeline | Working memory not compacted; accumulated tool results fill the window | Trigger compaction at 80% window capacity; summarize completed stages; persist key facts externally |
| Supervisor generates plan but no sub-agent executes | Sub-agent tool definitions missing from supervisor's tool list | Register each sub-agent as an explicit tool with typed input/output schemas; test tool discovery in isolation |
| Quality score drops after adding second agent | New agent duplicates work of first; token overhead exceeds value | Verify agents have non-overlapping tool sets and distinct system prompts |
| `429 ThrottlingException` during parallel fan-out | Concurrent agents exceed model API rate limits | Implement exponential backoff with random jitter; use request queuing with concurrency cap |

---

## Applied to Docgen

The docgen system maps directly to **Sequential Orchestration + Plan-and-Execute**: input parsing → template selection → section generation → validation → assembly. Within individual stages, ReAct provides adaptive fallback for ambiguous inputs. The three-type memory architecture ensures the system retains template rules (factual), learns from past quality scores (experiential via LOG_Generation.md + SYSTEM_DEBT.md), and maintains coherent state across sections (working) without overflow.

**Upgrade path:** When docgen adds parallel section generation, use Fan-out/Fan-in. When routing becomes too complex for rule-based decisions, introduce a Supervisor.

---

## Sources

- Anthropic, "Building Effective Agents," 2024
- Anthropic, "Multi-Agent Research System," 2025
- Anthropic, "Context Engineering," 2025
- Hu et al., arXiv 2512.13564, Dec 2025
- Zhao et al., ExpeL framework, AAAI 2024
- Yao et al., ReAct, ICLR 2023
- Wang et al., Plan-and-Execute, ACL 2023
- Microsoft Azure Architecture Center, Multi-Agent Design Patterns, 2026
- AWS Bedrock Multi-Agent Collaboration Docs, 2025
- ACM TOIS Agent Memory Survey, 2025


========================================================================
SYSTEM Architecture
========================================================================

# docgen System Architecture

How the documentation generation system works.

---

## Core Components

### 1. Framework (system/)

**Purpose:** Authoritative reference for all standards

**Contents:**
- `guides/` — 10 production standards (Content Guide, Exit Rules, Token Optimization, etc.)
- `templates/` — Output templates (canonical doc structure, DEBT template, project instructions)
- `checklists/` — Quality verification (human pass, AI pass, token efficiency)
- `examples/` — Perfect example docs showing all standards applied

**Usage:** Everything else references these guides. They are read-only truth sources.

### 2. Builders (builders/)

**Purpose:** Domain-specific documentation generators

**Structure per domain (e.g., GTM):**
```
builders/gtm/
├── builder.md          — Questionnaire logic (what to ask users)
├── rules.md            — Output rules (GTM-specific standards)
├── token_budget.md     — Token limit (4000 for GTM strategy)
└── examples/           — Sample GTM docs
```

**Flow:**
1. User answers questionnaire in `builder.md`
2. Builder generates doc using `DOC_CANONICAL_TEMPLATE.md`
3. Output runs through rules in `rules.md`
4. Token count checked against `token_budget.md`
5. Doc stored in `output/gtm/v1.0/`

### 3. Output (output/)

**Purpose:** Store generated documentation with versioning

**Structure per domain:**
```
output/gtm/
├── v1.0/               — Initial release
│   ├── GTM_Strategy_2026.md
│   ├── GTM_Strategy_2026.DEBT.md
│   └── metadata.json
├── v1.1/               — Patch update
├── v2.0/               — Major revision
└── archive/            — Deprecated versions ([DEPRECATED] prefix)
```

**Versioning:**
- v1.0 = initial
- v1.1 = patch (typo, clarification)
- v2.0 = major (new approach)
- Deprecated versions moved to archive/

### 4. Skills (skills/)

**Purpose:** Track reusable workflows

**Folders:**
- `published/` — Production skills (auto-added to projects)
- `suggested/` — Skills under review (from doc generation patterns)
- `archived/` — Deprecated skills

### 5. Config (config/)

**Purpose:** System-wide rules and budgets

**Contents:**
- `token_budgets.json` — Token limits per doc type (2500 for setup, 4000 for GTM, etc.)
- `domain_definitions.json` — What each domain covers (GTM, Design, Branding, etc.)
- Additional config as system grows

### 6. Metrics (metrics/)

**Purpose:** Track all generated docs

**Contents:**
- `generation_log.md` — Append-only log of every doc created
- Monthly summaries (count, avg quality, avg tokens, etc.)

### 7. Backlog (backlog/)

**Purpose:** System-wide technical debt

**Contents:**
- `SYSTEM_DEBT.md` — Framework improvements (P0-P3 items)

### 8. Projects (projects/)

**Purpose:** Claude Projects configurations

**Folders per domain:**
```
projects/docgen_base/              — Base system
projects/gtm_docs/                 — GTM builder
projects/design_docs/              — Design builder
etc.
```

Each contains:
- `instructions.md` — Custom instructions for Claude
- `knowledge_base/` — Reference documents

---

## Production Flow

```
User → Ask for GTM doc
  ↓
Builder/Questionnaire
  (what needs to be in GTM doc?)
  ↓
Output Generated
  (using DOC_CANONICAL_TEMPLATE.md)
  ↓
Exit Gate 1: Validation
  ✓ Metadata valid?
  ↓
Exit Gate 2: Structure
  ✓ All sections present?
  ↓
Exit Gate 3: Content Quality
  ✓ Clear & accurate?
  ↓
Exit Gate 4: Quality Check
  ✓ Human pass + AI pass + Token pass?
  ↓
Create DEBT.md
  (known limitations, backlog)
  ↓
Name File
  (GTM_Strategy_2026.md per SYSTEM_File_Naming.md)
  ↓
Exit Gate 5: Shipping
  ✓ All gates pass + DEBT exists + metadata complete?
  ↓
Store in output/gtm/v1.0/
  └─ GTM_Strategy_2026.md
  └─ GTM_Strategy_2026.DEBT.md
  └─ metadata.json
  ↓
Add to Claude Projects
  (docgen_base + gtm_docs)
  ↓
✅ PRODUCTION
```

---

## Quality Gates

### Gate 1: Validation (Input Check)
- **What:** Does metadata exist and is it valid?
- **Fail:** Fix frontmatter, re-run
- **Owner:** Automated

### Gate 2: Structure (Template Compliance)
- **What:** Does doc follow DOC_CANONICAL_TEMPLATE.md?
- **Fail:** Add missing sections
- **Owner:** Automated or manual

### Gate 3: Content Quality (Clarity/Accuracy)
- **What:** Is it clear, accurate, complete?
- **Fail:** Rewrite for clarity
- **Owner:** Manual (human review)

### Gate 4: Quality (Human + AI + Token)
- **What:** Human checklist + AI checklist + token budget OK?
- **Fail:** Optimize or cut content
- **Owner:** Automated + manual

### Gate 5: Shipping (Final Approval)
- **What:** All 4 gates + DEBT.md + metadata complete?
- **Fail:** Return to earlier gate
- **Owner:** Manual (project owner)

---

## Templates

### DOC_CANONICAL_TEMPLATE.md

Every doc must follow this structure:

```
1. YAML Frontmatter (8 required fields)
2. Title + Overview (exactly 2 sentences)
3. Prerequisites (Level 1-4 if applicable)
4. Content (type-appropriate)
5. Expected Output (table with commands)
6. Troubleshooting (errors with signatures)
7. Why This Matters (optional)
8. What's Next (related docs)
```

Plus:
- AI metadata blocks (preconditions/postconditions)
- metadata.json (quality score, tokens, gates)
- DEBT.md (known limitations, backlog)

### DEBT Template

Every doc includes DEBT.md listing:
- P0 items (critical, none if shipped)
- P1 items (high priority)
- P2 items (medium priority)
- P3 items (low priority)

Plus:
- Known limitations
- Content decisions (why things cut)
- Dependencies
- Verification needs
- Skills to create

---

## Token Optimization

**Budgets per type:**
- Setup guide: 2500 tokens
- GTM strategy: 4000 tokens
- API guide: 3000 tokens
- (See config/token_budgets.json)

**Quality per token:** 0.03+ (quality score ÷ token count)

**Optimization rules:**
- No fluff or theory
- Examples concise but complete
- Prose ≤ 4 paragraphs per section
- Only top 3-5 errors (rest in DEBT.md)
- Every section must serve purpose

---

## File Naming

Pattern: `{CATEGORY}_{TOPIC}_{VERSION}_{DATE}.md`

Examples:
- `GTM_Strategy_2026.md` (evergreen)
- `GTM_Competitive_Analysis_v1.0.md` (versioned)
- `[DEPRECATED]_Old_Strategy_v1.0.md` (archived)

---

## Version Control

**v1.0** = Initial release (in v1.0/ folder)
**v1.1** = Patch (same folder, new version file)
**v2.0** = Major revision (new v2.0/ folder, v1.x moved to archive/)

**Deprecation:**
1. Create v2.0 (new folder)
2. Mark v1.x deprecated (status field)
3. Move v1.x to archive/ with [DEPRECATED] prefix
4. Set EOL date (6-12 months)

---

## Claude Projects Integration

Each Claude Project has:

1. **Custom Instructions** (from PROJECT_INSTRUCTIONS_Docgen_Production.md)
   - Role definition
   - How to use uploaded framework
   - Response format
   - Do's and Don'ts

2. **Knowledge Base** (from system/)
   - All guides (SYSTEM_*.md)
   - All templates (DOC_CANONICAL_TEMPLATE.md, TEMPLATE_DEBT.md, etc.)
   - Examples

3. **Domain-Specific Projects**
   - docgen_base — Core system
   - gtm_docs — GTM builder
   - design_docs — Design builder
   - etc.

---

## Automation Opportunities (see backlog/)

**P1 (High Priority):**
- Builder automation framework (questionnaire → output → gates)
- Skill suggestion engine (detect patterns → suggest skills)
- Token validation script (check budgets automatically)
- Monthly metrics dashboard (quality trends)

**P2 (Medium Priority):**
- Domain-specific checklists
- Deprecation automation
- Cross-doc link validation
- Skill auto-integration

---

## Extensibility

### Adding a New Domain

1. Create `builders/{new_domain}/`
2. Create `builder.md`, `rules.md`, `token_budget.md`
3. Add to `config/domain_definitions.json`
4. Create `output/{new_domain}/{v1.0,v1.1,v2.0,archive}/`
5. Create `projects/{new_domain}_docs/`

### Adding a New Doc Type

1. Add to `DOC_CANONICAL_TEMPLATE.md` (section for type-specific examples)
2. Update `config/token_budgets.json` (add budget)
3. Create type-specific checklist in `system/checklists/`
4. Document in appropriate guide

### Adding Automation

1. Create script in `automation/` (not yet created)
2. Reference from relevant gate or process
3. Document in `docs/`
4. Add to CONTRIBUTING.md

---

## Directory Tree

```
docgen/
├── README.md                   # Start here
├── CONTRIBUTING.md             # How to contribute
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore patterns
│
├── system/                     # Framework (read-only reference)
│   ├── guides/                 # 10 production standards
│   ├── templates/              # Output templates
│   ├── checklists/             # Quality verification
│   └── examples/               # Perfect example docs
│
├── builders/                   # Domain builders
│   ├── gtm/                    # Go-to-market
│   ├── design/                 # Design & UX
│   ├── branding/               # Branding & voice
│   ├── content/                # Content strategy
│   ├── icp/                    # Ideal customer profile
│   └── web_dev/                # Web development
│
├── output/                     # Generated docs (versioned)
│   ├── gtm/{v1.0,v1.1,v2.0,archive}
│   ├── design/
│   ├── branding/
│   ├── content/
│   ├── icp/
│   └── web_dev/
│
├── skills/                     # Reusable workflows
│   ├── published/              # Production skills
│   ├── suggested/              # Under review
│   └── archived/               # Deprecated
│
├── projects/                   # Claude Projects configs
│   ├── docgen_base/            # Core system
│   ├── gtm_docs/               # GTM builder
│   └── [other domains]
│
├── config/                     # System configuration
│   ├── token_budgets.json      # Token limits
│   └── domain_definitions.json # Domain specs
│
├── metrics/                    # Tracking & logs
│   └── generation_log.md       # All docs created
│
├── backlog/                    # Technical debt
│   └── SYSTEM_DEBT.md          # Framework improvements
│
└── docs/                       # System documentation
    └── ARCHITECTURE.md         # This file
```

---

That's the system. Scalable, production-grade, extensible.


========================================================================
SYSTEM Build Decision Framework
========================================================================

# Build Decision Framework: Projects vs Skills vs MCPs vs Products
**Version:** 1.1 · April 2026
**Purpose:** Determine what to build before generating any documentation.

---

## The Core Question

When a user asks for help building something with Claude/AI, the first decision is: **what type of artifact is being built?** Get this wrong and every doc generated will be structurally incorrect. Get it right and the builder, templates, and output format all lock in automatically.

---

## The Four Build Types

There are four distinct types of artifacts the system generates. Identify the correct type at Q0 — every subsequent doc, template, and output bundle depends on it.

### Type 1: Product / Startup (The Thing Being Built)
**What it is:** A software product, app, SaaS, or tool. The AI is the builder, not the artifact. The output is an implementation-ready bundle that an AI coding agent uses to build the product.

**Use when:**
- "I want to build [app / tool / product / system]"
- User describes what their software does, not what their Claude assistant does
- The end result is deployed software, not a configured AI workspace
- A developer or AI coding agent will receive the docs and start writing code

**What it produces:** Product vision, system architecture, data schema, API spec, environment setup, **development plan** (always), `CLAUDE.md` for the new project, starter prompt for AI coding tool — delivered as a complete implementation bundle zip.

**Signature phrases:** *"I want to build...", "Help me create an app that...", "I'm building a SaaS for...", "We need a tool that..."*

**Example:** Task management app, SaaS analytics dashboard, AI-powered chrome extension, marketplace platform

**Builder:** `builders/product/`
**Quality target:** 90/100 (higher bar — AI coding agents use these docs directly)

---

### Type 2: Claude Project (The Mind)
**What it is:** A persistent, configured Claude workspace with a knowledge base, project instructions, and a defined persona.

**Use when:**
- You need Claude to "know" a domain across multiple conversations (guidelines, templates, standards, brand voice)
- Multiple people need the same specialized Claude behavior in a shared interface
- The deliverable is advice, generated content, or document creation — not automation
- Context must survive between sessions (the knowledge base is always loaded)

**What it produces:** CLAUDE.md, PROJECT_INSTRUCTIONS, SYSTEM guides, config files, folder structure, README.

**Signature phrase:** *"I want a Claude assistant that knows about X and always behaves like Y."*

**Example:** Documentation Builder, Code Reviewer, Sales Enablement Assistant, Brand Voice Assistant

---

### Type 3: Skill (The Playbook)
**What it is:** A structured, repeatable workflow invoked by a slash command or trigger phrase. Defines exactly how Claude should handle a specific, recurring task type.

**Use when:**
- The task type is predictable and recurring (same inputs → same process → same output format)
- You want `/command` shortcuts that route to the right workflow
- Claude needs to follow a multi-step intake → process → output pattern reliably
- The skill is used from Cowork or Claude Code, not just a Claude Project chat

**What it produces:** `SKILL.md` (routing logic, intake questions, step-by-step process, output format, example), optionally supporting templates and reference files.

**Signature phrase:** *"Whenever someone asks for X, I want Claude to always follow this exact process."*

**Example:** `/docgen` (documentation generator), `/campaign-plan`, `/review-pr`, `/call-summary`

---

### Type 4: MCP Server (The Hands)
**What it is:** A Model Context Protocol server that gives Claude live, bidirectional access to an external system — read data from it, write actions back to it.

**Use when:**
- Claude needs **live data** that changes frequently (Slack messages, Jira tickets, calendar events, SEO metrics, analytics)
- Claude needs to **take actions** in external systems (create a ticket, send a message, update a record)
- Static knowledge base docs are insufficient because the data is dynamic
- You need bidirectional integration (read + write), not just summarization

**What it produces:** Setup guide, API reference, schema reference, command reference, troubleshooting guide, authentication guide.

**Signature phrase:** *"I want Claude to connect to [tool] and actually do things there — not just talk about it."*

**Example:** Slack MCP (read/send messages), Jira MCP (create/update tickets), Ahrefs MCP (live keyword data), Google Calendar MCP (schedule events)

---

## Decision Matrix

| What the user wants | Build | Builder |
|---|---|---|
| "I want to build an app / product / SaaS" | Product Bundle | `builders/product/` |
| "A Claude assistant for [domain]" | Claude Project | `builders/claude-project/` |
| "A repeatable workflow / slash command" | Skill | `builders/skill/` |
| "Claude connected to [external tool]" | MCP Server | `builders/mcp/` |
| "Docs for a product or feature" | AI Docs | `builders/ai-docs/` |
| "Code documentation" | Code Docs | `builders/code/` |
| Product + AI assistant + integrations | All types | Product Bundle first, then Project + Skills + MCPs |

---

## How They Layer Together

A real production system typically uses all three:

```
┌─────────────────────────────────────────────┐
│  Claude Project  ←  The Mind                │
│  (knowledge base, instructions, persona)    │
│                                             │
│  Routing: "What do you need today?"         │
│              ↓                              │
│  Skills  ←  The Playbooks                   │
│  (structured workflows, /commands)          │
│  /campaign-plan  /brand-review  /docgen     │
│              ↓                              │
│  MCPs  ←  The Hands                         │
│  (live data + actions in real tools)        │
│  Slack · Jira · Notion · Ahrefs · GCal      │
└─────────────────────────────────────────────┘
```

**The rule:** Add each layer only when needed. Start with the Project (knowledge + instructions). Add Skills when workflows become repeatable. Add MCPs when live data or external actions are required.

---

## Identifying What to Build: The Q0 Gate

Before any intake questions, ask **Q0: What type of thing are we building?**

Read the user's description and classify it:

**Product / Startup signals (check this first):**
- "I want to build...", "We're building a...", "Help me create an app/tool/platform"
- User describes software features, users, and problems — not Claude's behavior
- The word "users", "customers", "dashboard", "backend", "database" appear
- There's a problem to solve, not a knowledge base to populate
→ Route to `builders/product/`

**Claude Project signals:**
- "A Claude assistant / bot / workspace for [role or domain]"
- "Something my team can use in Claude.ai"
- "A project that knows about our [guidelines / brand / process]"
- Needs: knowledge base, persistent context, team-shared config

**Skill signals:**
- "A slash command / shortcut / workflow"
- "Whenever someone asks for X, Claude should always do Y"
- "Something for Cowork or Claude Code"
- "A repeatable process with consistent outputs"
- Needs: SKILL.md, intake questions, routing logic

**MCP Server signals:**
- "Connect Claude to [Slack / Jira / Salesforce / database / API]"
- "Read live data from [tool]"
- "Let Claude create/update/send in [tool]"
- "Integration with [external system]"
- Needs: server setup, API reference, auth guide, schema reference

**AI / Code Docs signals:**
- "Document this product / feature / API"
- "Write setup/architecture/troubleshooting docs for [thing]"
- "Document this codebase / function / module"
- Needs: single or multi-doc output using doc type templates

**If unclear:** Ask. Do not assume. Building the wrong artifact type wastes all subsequent documentation.

---

## Context Gate — What Must Be Known Before Generating

Each build type has a minimum context threshold. Below this threshold: ask, don't generate.

### Claude Project — minimum context required
- [ ] Project name
- [ ] Core purpose (1–3 sentences, specific problem being solved)
- [ ] Primary user (role + technical level)
- [ ] Top 3–5 tasks Claude will perform
- [ ] Any connected MCPs or external tools

### Skill — minimum context required
- [ ] Skill name / slash command trigger
- [ ] What triggers it (command, keyword, or pattern)
- [ ] What the user provides as input
- [ ] Step-by-step process Claude should follow
- [ ] What the output looks like (format, length, structure)

### MCP Server — minimum context required
- [ ] Which external system (name + URL / platform)
- [ ] What data Claude needs to read
- [ ] What actions Claude needs to take
- [ ] Authentication method (API key, OAuth, etc.)
- [ ] Who operates it (developer, ops, end user)

### Product / Startup — minimum context required
- [ ] What is being built (one-liner: who / what / why)
- [ ] Target user(s) + their core problem
- [ ] MVP feature list (3–5 features, prioritized)
- [ ] Tech stack preference (or background for recommendation)
- [ ] Deployment target

### AI Docs / Code Docs — minimum context required
- [ ] What is being documented (specific system, feature, API)
- [ ] Target audience (role + technical level)
- [ ] Doc type (from the 17 valid types in `SYSTEM_Exit_Rules.md`)
- [ ] Domain (`claude-project` | `ai-docs` | `code` | `reference`)

---

## Output Routing by Build Type

Once the build type is identified and context is confirmed, use this routing:

| Build type | Primary outputs | Gate sequence |
|---|---|---|
| **Product** | PRD, UX, UI, Vision, Architecture, Data Schema, API Spec, Setup, Dev Plan, CLAUDE.md, Starter Prompt | Gates 1–5 per doc (90/100 target) |
| Claude Project | CLAUDE.md, PROJECT_INSTRUCTIONS, SYSTEM guides, config | Gates 1–5 per doc |
| Skill | SKILL.md, supporting templates | Gate 2 (structure) + Gate 3 (content) |
| MCP Server | Setup guide, API reference, schema reference, auth guide | Gates 1–5 per doc |
| AI Docs | Single doc per selected doc type | Gates 1–5 |
| Code Docs | Setup, API, architecture, ADR, troubleshooting | Gates 1–5 per doc |

---

## What "Top-Tier Implementation Documentation" Means

For every build type, documentation is complete when a skilled AI reading only these docs could build the thing correctly without asking questions. That means:

- **Claude Project:** An AI can recreate the CLAUDE.md, project instructions, and folder structure from scratch
- **Skill:** An AI can implement the SKILL.md and know exactly what intake to collect and what output to produce
- **MCP Server:** An AI can set up, authenticate, and operate the server using only the generated docs
- **AI / Code Docs:** A human or AI can set up, use, troubleshoot, and extend the system using only the generated docs

If a gap remains — a step with no expected output, an API call with no auth example, a workflow with no error handling — it is logged in `backlog/SYSTEM_DEBT.md` and is not a Gate 5 pass.


========================================================================
SYSTEM Coding Standards
========================================================================

# SYSTEM_Coding_Standards.md — Code Quality Rules

**Applies to:** All code blocks in any document generated by this system.
**Gate:** Gate 3 (Content Quality). Code that violates these standards = Gate 3 fail.

---

## Core Principle

Code in documentation must be runnable, complete, and safe. If someone copies it and runs it, it must work without modification (other than substituting their own credentials/values).

---

## Rule 1: Every Code Block Must Have a Language Tag

```markdown
✅ GOOD
```python
import anthropic
```

❌ BAD
```
import anthropic
```
```

**Why:** Language tags enable syntax highlighting, AI parsing, and copy-paste safety. Untagged blocks are ambiguous.

**Required language tags:** `python`, `javascript`, `typescript`, `bash`, `json`, `yaml`, `markdown`, `sql`, `text`

---

## Rule 2: Commands Must Show Expected Output

```markdown
✅ GOOD
```bash
claude --version
```
Expected: `claude/1.x.x`

❌ BAD
```bash
claude --version
```
(no expected output shown)
```

**Why:** Without expected output, the user cannot tell if the command worked. Every executable command needs an Expected line.

---

## Rule 3: No Hardcoded Secrets

```markdown
✅ GOOD
```python
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)
```

❌ BAD
```python
client = anthropic.Anthropic(api_key="sk-ant-api03-xxxx")
```
```

**Required pattern for credentials:**
- API keys → `os.environ.get("KEY_NAME")`
- Tokens → env vars or config files
- Passwords → never inline

**Placeholder format when a value must be shown:** `YOUR_API_KEY_HERE`, `<your-api-key>`, `$ANTHROPIC_API_KEY`

---

## Rule 4: Code Must Be Complete and Runnable

```markdown
✅ GOOD — imports included, error handling present, complete function
```python
import anthropic
import os

def generate_response(prompt: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

if __name__ == "__main__":
    result = generate_response("Hello, Claude!")
    print(result)
```

❌ BAD — partial snippet, no imports, no context
```python
message = client.messages.create(
    model="claude-sonnet-4-6",
    messages=[...]
)
```
```

**Exception:** Short illustrative snippets (showing one concept only) may omit boilerplate IF preceded by a note: `# Snippet — see full example in [doc title]`

---

## Rule 5: Version Pin All Dependencies

```markdown
✅ GOOD
```bash
pip install anthropic==0.39.0
```
or with minimum version bound:
```bash
pip install "anthropic>=0.39.0,<1.0.0"
```

❌ BAD
```bash
pip install anthropic
```
```

**Why:** Unpinned installs break when APIs change. Documentation must be reproducible.

---

## Rule 6: Code Length Limits

| Code Type | Max Lines | Rationale |
|-----------|-----------|-----------|
| Illustrative snippet | 15 lines | Token budget; shows concept only |
| Working example | 50 lines | Complete but focused |
| Full implementation | 100 lines | Split into multiple docs if longer |
| Config file | 40 lines | Reference the real file for longer configs |

**If code exceeds limits:** Split into a separate file reference or link to a companion code file. Don't inflate docs with code walls.

---

## Rule 7: AI-Generated Code Markers

Any code generated by an AI assistant and included in documentation must include a comment:

```python
# Generated with Claude claude-sonnet-4-6 · Reviewed: YYYY-MM-DD
```

```javascript
// Generated with Claude claude-sonnet-4-6 · Reviewed: YYYY-MM-DD
```

**Why:** Tracks provenance. Enables future audits when model versions change.

**Required fields in marker:** model used, date reviewed by human.

---

## Rule 8: Error Handling Must Be Explicit

```markdown
✅ GOOD
```python
try:
    response = client.messages.create(...)
except anthropic.APIConnectionError as e:
    print(f"Connection failed: {e}")
    raise
except anthropic.RateLimitError as e:
    print(f"Rate limit hit — wait and retry: {e}")
    raise
```

❌ BAD
```python
response = client.messages.create(...)
# (no error handling)
```
```

**Exception:** Illustrative snippets under 15 lines may omit error handling if prefaced with `# Example only — add error handling in production`

---

## Rule 9: Shell Commands Must Be Safe to Run

Before including a shell command, verify:
- [ ] It does not delete files without confirmation (`rm`, `rmdir`)
- [ ] It does not install system packages without noting required permissions
- [ ] It does not modify global configs without a backup step
- [ ] Destructive commands are marked `# ⚠️ Destructive — run only if [condition]`

---

## Rule 10: Model Strings Must Be Current

Always use exact model strings from the current release:
- `claude-opus-4-6` (most capable, highest cost)
- `claude-sonnet-4-6` (balanced — recommended default)
- `claude-haiku-4-5-20251001` (fastest, lowest cost)

**Never use:** `claude-3-opus`, `claude-3-sonnet`, or any model string without checking `RESEARCH_Claude_Project_Best_Practices.md` for current strings.

---

## Code Review Checklist (Gate 3)

For every code block in a document, verify:

- [ ] Language tag present
- [ ] Expected output shown (for executable commands)
- [ ] No hardcoded secrets — env vars or placeholders only
- [ ] Imports present (or snippet marker explaining they're omitted)
- [ ] Dependencies are version-pinned
- [ ] Within line-count limits
- [ ] AI-generated marker present (if applicable)
- [ ] Error handling present or snippet disclaimer added
- [ ] Shell commands are safe
- [ ] Model strings are current

**Any failed check = Gate 3 fail.** Fix before proceeding to Gate 4.

---

*Documentation Builder · Coding Standards v1.0 · April 2026*


========================================================================
SYSTEM Content Guide
========================================================================

# Documentation Content Structure Guide

## Core Principle
Write documentation that enables LLMs to build QUALITY products that BOTH WORK and FOLLOW user requirements — even when those requirements are loose or not concise. Every sentence must pass two tests: "Will this help the building LLM implement correctly?" and "Is this grounded in the user's actual input?"

---

## CRITICAL SECTIONS (Must Always Include)

### 1. Overview (1-2 sentences)
**Purpose:** Answer immediately: what is this and why use it?

**Format:**
```markdown
# [Action Verb + Noun]
[One sentence: what you'll accomplish]
[One sentence: why you need this]

GOOD: "How to set up Stripe payments
Integrate credit card processing to accept payments from customers."

BAD: "Payment Integration Overview
The payment integration system provides..."
```

**Rule:** If someone can't explain it in 2 sentences, they don't understand it yet.

---

### 2. Prerequisites (✅ Detailed below)

---

### 3. Step-by-Step Instructions

**Format:**
```markdown
## Setup

1. [Exact command or action]
   Expected: [what you see after]

2. [Exact command or action]
   Expected: [what you see after]
```

**Rules:**
- Use exact commands, not descriptions
- Show what success looks like after each step
- Number steps (1, 2, 3) not bullets
- One action per step
- Include output/screenshot

**GOOD:**
```
1. Run: npm install stripe
   Expected: you see "added 47 packages"

2. Create file: .env with content:
   STRIPE_KEY=sk_test_123...
   Expected: file exists in project root
```

**BAD:**
```
1. Install dependencies
2. Configure Stripe
3. Test the setup
```

---

### 4. Expected Output / Success Indicator

**Format:**
```markdown
## What Success Looks Like

After completing setup, you should:
- See message: "Setup complete ✓"
- Have file: /config/payments.js (check: ls -la config/)
- Be able to: npm run test:payments (should pass all tests)
```

**Why:** Prevents confusion about whether it worked or not.

---

## IMPORTANT SECTIONS (Should Have)

### 5. Why This Matters (Context)

**Format:**
```markdown
## Why This Approach

We use Stripe because:
- [Business reason]: Lowest fees for our use case
- [Technical reason]: Webhook system matches our async flow
- [Integration reason]: Direct Node.js library available

We DON'T use Paypal because:
- [Constraint]: Requires separate authorization flow
- [Cost]: 2x more expensive per transaction
```

**Rule:** Hide nothing. Team needs to understand decisions.

---

### 6. Common Errors & Solutions

**Format:**
```markdown
## Troubleshooting

### Error: "Cannot find module 'stripe'"
- Cause: npm install was skipped
- Fix: Run `npm install stripe`
- Verify: Run `npm list stripe` (should show version)

### Error: "Invalid API key"
- Cause: STRIPE_KEY in .env is wrong or missing
- Fix: Check .env file exists: `cat .env | grep STRIPE`
- Verify: Key should start with "sk_test_" (test) or "sk_live_" (prod)

### Setup passes but payments fail
- Cause: Webhook URL not registered with Stripe
- Fix: Go to Stripe Dashboard → Webhooks → add https://yoursite.com/webhooks
- Verify: Run `npm run test:webhooks` (should pass)
```

**Rule:** Organize by: Error message → Why it happens → Exact fix → How to verify

---

### 7. What's Next (Forward Link)

**Format:**
```markdown
## After Setup

You now have Stripe connected. Next steps:

1. **Testing** → See "Test payments in sandbox mode" [link]
2. **Production** → See "Switch to live keys" [link]
3. **Security** → See "Secure webhook endpoints" [link]

Choose based on your needs:
- If you're testing: Start with #1
- If ready to launch: Follow #1 then #2
- If already live: Focus on #3
```

**Rule:** Give options, don't force one path.

---

## ❌ DON'T WRITE (Waste of Space)

| Avoid | Why | Solution |
|-------|-----|----------|
| "Follow best practices" | Which ones? | List specific practices |
| "Configure properly" | How? | Show exact config |
| "Make sure everything is installed" | How do I verify? | Show verification command |
| Long explanation of theory | How do I use this? | Show real example first, explain after |
| Same content in two places | Outdated in one place | Link to single source |
| "It's important to remember" | Then why bury it? | Make it a Gotcha or prerequisite |

---

---

## 🎯 PREREQUISITES - DETAILED GUIDE

### The Problem with Bad Prerequisites

❌ **Common mistakes:**
```markdown
## Prerequisites
- Node.js installed
- Understanding of JavaScript
- Stripe account
```

**Problems:**
- "Installed" what version? How do I check?
- "Understanding" what level? Junior? Senior?
- "Stripe account" - test or production? Do I need a card?

---

### ✅ How to Write Good Prerequisites

**Structure:**
```
[Requirement] → [How to check] → [If missing: how to fix] → [Why needed]
```

**Template:**

```markdown
## Prerequisites

You need [specific thing]. 

Check if you have it:
[command to verify]

If not installed:
[command to install]

Why you need this:
[one sentence explaining dependency]
```

---

### Real Examples

#### Example 1: Technical Setup

```markdown
## Prerequisites

### Node.js v18+ 
**Check:** 
```bash
node --version
```
Should show: v18.0.0 or higher

**If missing:**
Install from: https://nodejs.org/
Or use: `brew install node@18` (Mac) / `choco install nodejs` (Windows)

**Why:** Stripe client requires native Promise/async support (added in v18)

---

### npm 8+
**Check:**
```bash
npm --version
```
Should show: 8.0.0 or higher

**If missing:**
Run: `npm install -g npm@latest`

**Why:** We use workspaces feature (requires npm 8+)

---

### Git (any version)
**Check:**
```bash
git --version
```

**If missing:**
Install from: https://git-scm.com/

**Why:** We clone from GitHub during setup

---

### Stripe Account
**Check:**
Go to: https://dashboard.stripe.com (if you can log in, you have account)

**If missing:**
Sign up here: https://dashboard.stripe.com/register
Takes 2 minutes. You can start in test mode (no card needed)

**Why:** We need API keys from your Stripe account

---

### Your Stripe Test API Key (from account)
**Check:**
```bash
cat .env | grep STRIPE_KEY
```
Should show something like: `sk_test_abc123...`

**If missing:**
1. Go to: Stripe Dashboard → Developers → API Keys
2. Copy: Secret Key (starts with sk_test_)
3. Add to file: `.env` with line: `STRIPE_KEY=sk_test_...`

**Why:** Authentication - without this Stripe API calls fail
```

**Why this format works:**
- ✅ Easy to scan (bold headers)
- ✅ Checkable (exact command to verify)
- ✅ Actionable (exact install command)
- ✅ Understandable (one sentence why)

---

#### Example 2: Knowledge/Skills Prerequisites

```markdown
## Prerequisites

### Understand: How Stripe webhooks work
**Check your knowledge:** Can you answer "What happens when a payment succeeds?"

**If not:** 
Read first: "Stripe Webhooks Explained" [link to internal doc]
Time: 5 minutes

**Why:** This setup relies on webhook handlers. If you don't understand webhooks, 
debugging will be 10x harder.

---

### Know your Stripe account type
**Check:** 
Go to Stripe Dashboard. Is it labeled "Test" or "Live"?

**For this guide, you need:** Test mode (labeled "Viewing test data")

**If you only have Live:** 
Click toggle at top right → switch to "Viewing test data"

**Why:** We'll create test payments. You don't want real charges while learning.
```

---

### Example 3: Team/Context Prerequisites

```markdown
## Prerequisites

### You're in the #payments-team Slack channel
**Check:** Search Slack for #payments-team

**If not:**
Ask @alice to add you to the channel

**Why:** That's where we discuss issues and share test cases

---

### You have deploy access to staging
**Check:**
Run: `npm run deploy:staging`
If it works without error → you have access

**If denied:**
Contact: @devops-team in Slack

**Why:** You'll need to test on staging before production
```

---

## Prerequisites Checklists

### For Code/Technical Prerequisites
- [ ] Each tech has exact version number (not just "Node.js")
- [ ] Check command is shown
- [ ] Install command is shown (if easy; else link)
- [ ] One sentence explaining why it's needed
- [ ] Indication of what breaks if missing

### For Knowledge Prerequisites
- [ ] What concept must you understand
- [ ] How to check if you understand
- [ ] Where to learn it (link or doc)
- [ ] Time estimate
- [ ] Why it matters

### For Access/Permissions Prerequisites
- [ ] What access is needed (exact name/level)
- [ ] How to check if you have it
- [ ] Who to ask if you don't
- [ ] Why you need it

---

## Common Prerequisites Patterns

### Pattern 1: Tools Required
```markdown
## Prerequisites

You need: [Tool Name]

Current version: [X.Y.Z] (or later)

Check:
```bash
[check command]
```

Install:
```bash
[install command]
```

If using [alternative]: [alt install command]
```

---

### Pattern 2: Files/Configuration
```markdown
## Prerequisites

File: .env in project root
Contents:
```
DATABASE_URL=postgresql://...
API_KEY=sk_test_...
```

Check: `test -f .env && echo "exists"` or `cat .env`

Create: Copy from `.env.example`: `cp .env.example .env` then edit values
```

---

### Pattern 3: Access/Credentials
```markdown
## Prerequisites

You need: Admin access to [Service/Database/Server]

Check: [How to verify you have access]

If denied: Contact [person/team] in [channel]

Why: [One sentence: what will fail without it]
```

---

### Pattern 4: Knowledge
```markdown
## Prerequisites

You should understand: [Concept]

Assess yourself:
- [ ] Can I explain [concept] in one sentence?
- [ ] Have I used [tool/tech] before?
- [ ] Do I know what [term] means?

If you said "no" to any: Read [link] first (takes [time])
```

---

## What NOT to Put in Prerequisites

❌ "Understanding of coding" → Too vague. What language?
✅ "Python 3.8+ and pip installed. Check: python --version"

❌ "Basic knowledge of APIs" → Do they need REST? GraphQL? HTTP basics?
✅ "Know what HTTP headers are (optional, helps with debugging). Intro: [link]"

❌ "Stripe account configured" → What does "configured" mean?
✅ "Stripe account in Test mode. Check: Stripe Dashboard shows 'Viewing test data'"

---

## Order of Prerequisites

1. **Hard requirements first** (must have or it breaks)
   - Tools/software versions
   - Required credentials
   - Mandatory knowledge

2. **Soft requirements next** (needed but can learn on the way)
   - Nice-to-have background
   - Optional knowledge
   - Alternative options

**Example order:**
```markdown
## Prerequisites

### Required
- Node.js v18+ (hard requirement - will break without)
- .env file with API_KEY (hard requirement)
- Stripe Test account (hard requirement)

### Recommended  
- Understand webhooks (makes debugging easier, can learn as you go)
- Know your way around npm (nice to have, not critical)
```

---

## Prerequisites for Different Document Types

### For CLAUDE.md (code project):
```markdown
## Prerequisites

Run this first:
```bash
npm install
npm run setup
```

Expected: "Setup complete ✓" message

Requirements to use this project:
- Node.js 18+: Check `node --version`
- npm 8+: Check `npm --version`
- Environment: Copy `.env.example` to `.env` and fill in values
```

---

### For SKILL.md (repeating task):
```markdown
## Prerequisites

Before you can use this skill:

✓ [Previous skill] completed
  (If not: See "How to [previous skill]" [link])

✓ You have: [specific thing]
  Check: [command]

✓ You understand: [concept]
  If not: Read [internal doc] (5 min)
```

---

### For Claude Projects (knowledge hub):
```markdown
## Prerequisites for reading this

You should already know:
- What [concept] means (if not: see our glossary)
- Basic [domain knowledge] (if not: we have intro guide)

You'll need:
- Access to [system] (check: can you log in?)
- [Specific credential/permission] (if you don't have: ask #channel)
```

---

## Testing Your Prerequisites

Ask yourself:
1. **Can someone complete this list in 5 minutes?** (If not, break it down more)
2. **Is every requirement checkable?** (Can they verify themselves?)
3. **Is every requirement necessary?** (Remove nice-to-haves from required)
4. **Did I explain WHY?** (Not just WHAT)
5. **Is it in the right order?** (Hard requirements first)

If you can't answer yes to all 5 → rewrite it.

---

## Real-World Example: Complete Doc

```markdown
# How to Set Up Stripe Payments

## Overview
Add credit card payment processing to your application using Stripe.
Takes 15 minutes to set up, allows you to accept customer payments within the hour.

---

## Prerequisites

### Required - Check These First

**1. Node.js 18 or higher**
```bash
# Check
node --version
# Should show: v18.0.0 or higher

# Install if missing
# Option A: https://nodejs.org/
# Option B (Mac): brew install node@18
# Option C (Windows): choco install nodejs
```
Why: Stripe library requires modern JavaScript async/await (added in v18)

---

**2. npm 8 or higher**
```bash
# Check
npm --version
# Should show: 8.0.0 or higher

# Update if lower
npm install -g npm@latest
```
Why: We use npm workspaces (requires npm 8+)

---

**3. Stripe Account (Test Mode)**
- Go to: https://dashboard.stripe.com
- If you see "Viewing test data" toggle at top → you're ready
- If missing: Sign up at https://dashboard.stripe.com/register (free, 2 min)

Why: Need API keys from Stripe to authenticate requests

---

**4. Your Stripe Test Secret Key**
```bash
# Check
cat .env | grep STRIPE_SECRET_KEY
# Should show: STRIPE_SECRET_KEY=sk_test_...

# Get key if missing
# 1. Go to: Stripe Dashboard → Developers → API Keys
# 2. Copy the "Secret Key" (starts with sk_test_)
# 3. Add to .env file: STRIPE_SECRET_KEY=sk_test_your_key_here
```
Why: This authenticates every payment API call

---

### Recommended - Nice to Have

**Understanding how Stripe webhooks work** (5 min read)
- See: "How Stripe Webhooks Work" [link]
- Why: Helps with debugging if payments fail mysteriously

---

## Setup Steps

1. Run: `npm install stripe`
   Expected: Message "added 47 packages"

2. Create/edit `.env` file with:
   ```
   STRIPE_SECRET_KEY=sk_test_your_key_here
   STRIPE_PUBLISHABLE_KEY=pk_test_your_key_here
   ```
   Expected: File exists at project root

3. Test the connection:
   ```bash
   npm run test:stripe:connection
   ```
   Expected: Output shows "✓ Connected to Stripe"

---

## What Success Looks Like

After setup:
- ✓ No errors in npm install
- ✓ .env file has both keys
- ✓ Test passes: `npm run test:stripe:connection`
- ✓ You can see demo charges in Stripe Dashboard → Payments

---

## Common Errors

**Error: "Cannot find module 'stripe'"**
- Cause: Step 1 was skipped
- Fix: Run `npm install stripe`

**Error: "Invalid API key"**
- Cause: STRIPE_SECRET_KEY in .env is wrong/missing
- Fix: Double-check key in Stripe Dashboard, paste exact value to .env

**Setup passes but test fails**
- Cause: Publishable key missing or wrong
- Fix: Add STRIPE_PUBLISHABLE_KEY to .env (starts with pk_test_)

---

## What's Next

✓ Setup complete. Now:

1. **Test payments:** See "Make a test charge" [link]
2. **Add webhook:** See "Handle payment events" [link]
3. **Go live:** See "Switch to production keys" [link]
```

---

---

## AI READABILITY STANDARDS

These standards ensure generated docs are optimally parseable and actionable by LLMs building the described product.

### Standard 1 — Constraints First

Every product doc opens with a Constraints & Non-Negotiables section. Hard rules go at the top of the document, not buried in prose. Format: table with Constraint | Reason | Violation Impact columns. The building LLM reads top-down — if constraints are at the bottom, it may have already hallucinated a conflicting approach.

### Standard 2 — Decision Records with Status

Every technology choice gets a decision record: Choice | Why | Alternatives Rejected | Status (CONFIRMED/ASSUMED). Without this, the building LLM treats every decision as arbitrary and may substitute alternatives. A CONFIRMED decision came from the user. An ASSUMED decision was defaulted by Docgen and must be marked as such.

### Standard 3 — Acceptance Criteria as Executable Checks

Write acceptance criteria in GIVEN/WHEN/THEN/VERIFY format. The VERIFY line is critical — it's the exact command or check the building LLM should run to confirm the implementation works.

**BAD:** "Endpoint returns 200"
**GOOD:**
```
GIVEN: User exists with email "test@test.com"
WHEN: POST /api/auth/login {"email": "test@test.com", "password": "test123"}
THEN: Response status 200, body contains {token: string, user: {id, email}}
VERIFY: curl -X POST localhost:3000/api/auth/login -d '{"email":"test@test.com","password":"test123"}' | jq '.token'
```

### Standard 4 — Dependency Graphs as Blocked-By

Dev plan tasks include `Blocked by: [Task IDs]` to create explicit dependency chains. This prevents the building LLM from starting work that depends on unfinished pieces.

**BAD:** "Phase 3: Build Dashboard (after auth is done)"
**GOOD:** "Task 3.1: Create `src/app/dashboard/page.tsx` — Blocked by: [2.1, 2.3]. Implements: R4."

### Standard 5 — When-in-Doubt Defaults

For every area where the user's requirements are vague, specify what the building LLM should do. This is the most important standard for handling loose requirements.

**Format:**
```markdown
### When-in-Doubt Defaults
- Error handling → toast notifications for user-facing errors, structured JSON logging for server errors, retry with exponential backoff for external API calls
- Empty states → show descriptive empty state component with CTA to the relevant creation action
- Loading states → skeleton screens for content areas, spinner for actions
- Form validation → client-side validation on blur, server-side on submit, show inline error messages
- Mobile responsiveness → mobile-first, breakpoints at 640px (sm), 768px (md), 1024px (lg)
```

Without these, the building LLM either asks (slowing down) or guesses (risking wrong implementation).

### Standard 6 — File-Level Intent Headers

Every file mentioned in the dev plan gets a one-line PURPOSE comment showing what it does and what it depends on:

```
<!-- PURPOSE: Handles user authentication via magic link. Depends on: lib/email.ts, lib/db.ts -->
```

This gives the building LLM local context without re-reading the full architecture doc.

### Standard 7 — Anti-Pattern Examples

Show what NOT to do alongside what to do. The building LLM is prone to common patterns that may conflict with the project's constraints.

**BAD:** "Use the auth library correctly"
**GOOD:**
```markdown
| Anti-Pattern | Why It's Wrong | Do This Instead |
|---|---|---|
| Creating a custom JWT implementation | Supabase handles auth — custom JWT duplicates logic and creates security gaps | Use `supabase.auth.signInWithOtp()` in `src/lib/auth.ts` |
| Storing user profile in a separate `profiles` table | Supabase auth already has `auth.users` with metadata | Use `auth.users` + `raw_user_meta_data` JSONB column |
```

### Standard 8 — No Hallucinated Content

Generated docs must never contain fabricated facts, invented requirements, or assumed decisions presented as confirmed. If information is missing:

1. If the missing info is critical for the current section: add a NEEDS INPUT placeholder
2. If a reasonable default exists: use it and mark as ASSUMED
3. If the info can be inferred from other context: infer it and mark as INFERRED
4. Never present inferred or defaulted content as if the user confirmed it

```markdown
<!-- NEEDS INPUT: This section requires [specific information].
     Ask the user: "[exact question to ask]"
     Cannot be defaulted because: [why this needs real input] -->
```

### Standard 9 — Assumption Traceability

Every ASSUMED and INFERRED item gets three things: the reasoning (why this default), the impact (what changes if the user overrides it), and the override instruction (what to say to change it). Consolidated in the Assumption Register at the end of each doc.

---

## Summary Checklist

Before you publish any doc:

### Prerequisites section:
- [ ] Hard requirements are listed first
- [ ] Every requirement has a check command
- [ ] Every requirement has an install/fix instruction
- [ ] Every requirement has "Why" explanation
- [ ] No requirement is vaguer than "Check: [exact command]"
- [ ] Can someone complete this list in 5-10 minutes?
- [ ] Soft requirements clearly marked as optional

### Content section:
- [ ] Overview: answerable in 1-2 sentences
- [ ] Steps: numbered, with expected output
- [ ] Success: clear indicator of "it worked"
- [ ] Errors: organized by symptom, not by cause
- [ ] Next steps: linked forward options

### AI Readability:
- [ ] Constraints section at top of product docs
- [ ] All decisions have CONFIRMED/ASSUMED status
- [ ] Acceptance criteria use GIVEN/WHEN/THEN/VERIFY
- [ ] Dev plan tasks have Blocked-by dependencies
- [ ] When-in-Doubt Defaults present for ambiguous areas
- [ ] Anti-patterns included for Architecture and Dev Plan
- [ ] No hallucinated content — all items traceable to user input or marked ASSUMED/INFERRED
- [ ] Assumption Register consolidates all assumptions with override instructions


========================================================================
SYSTEM Exit Rules
========================================================================

# Exit Rules: 5-Level Gate System

No document ships without passing ALL 5 gates. Each gate is a hard stop.

---

## Gate Architecture

```
Level 1: Validation (Input Check)
    ↓ (PASS → continue, FAIL → return to builder)
Level 2: Structure (Template Compliance)
    ↓ (PASS → continue, FAIL → fix structure)
Level 3: Content (Quality Standards)
    ↓ (PASS → continue, FAIL → rewrite)
Level 4: Quality (Human + AI + Token Check)
    ↓ (PASS → continue, FAIL → optimize)
Level 5: Shipping (Final Approval)
    ↓
📦 PRODUCTION
```

Each gate has:
- Exit criteria (what must be true)
- Failure reason (why it failed)
- Recovery action (how to fix)
- Owner (who approves)

---

## Gate Level 1: Validation (Input Check)

**Purpose:** Verify builder collected necessary information before generating.

**Exit Criteria (ALL must be true):**
- [ ] Frontmatter has all 8 required fields
- [ ] YAML is valid (no syntax errors)
- [ ] doc_type is valid — one of: `project-setup`, `claude-md`, `project-instructions`, `system-guide`, `how-to`, `reference`, `feature`, `process`, `update`, `setup-guide`, `api-guide`, `architecture`, `adr`, `troubleshooting`, `config-reference`, `schema-reference`, `command-reference`
- [ ] domain is valid — one of: `claude-project`, `ai-docs`, `code`, `reference` (see `config/domain_definitions.json`)
- [ ] audience is valid (beginner, intermediate, advanced, or all)
- [ ] difficulty is valid (easy, medium, or hard)
- [ ] status is valid (production, draft, or review)
- [ ] title exists and starts with action verb
- [ ] overview is provided and exactly 2 sentences
- [ ] builder_session_id is unique (no duplicate generation)

**What Fails This Gate:**
- Missing frontmatter
- Invalid YAML syntax
- Unknown doc_type
- Unclear audience level
- Title doesn't answer "what/why"
- No overview provided

**Recovery Action:**
1. Return to builder questionnaire
2. Re-run builder questions
3. Generate new doc
4. Re-run Gate 1

**Owner:** Automated validation (Claude or system script)

**Example Pass:**
```yaml
---
doc_type: project-setup
domain: claude-project
builder_version: v1.1
generated_by: claude-project_builder
generated_at: 2026-04-03T10:00:00Z
builder_session_id: sess_abc123def456
audience: intermediate
difficulty: medium
time_estimate: "1-hour"
prerequisites: [claude-account, idea-description]
status: production
version: 1.0
quality_score: 0
exit_gates_passed: []
---

# How to Set Up a Claude Project from an Idea

Generate all required Claude project files (CLAUDE.md, project instructions, system guides) from a single idea description.
This ensures your Claude project has production-quality instructions, knowledge base structure, and quality gates from day one.
```

**Example Fail:**
```yaml
---
doc_type: unknown_type          # ❌ INVALID — not in approved list
audience: all skill levels      # ❌ INVALID — not in enum
---

# Claude Project                # ❌ No action verb
This document is about Claude projects in general.
It covers how to use Claude.
```

---

## Gate Level 2: Structure (Template Compliance)

**Purpose:** Verify doc follows DOC_CANONICAL_TEMPLATE structure.

**Exit Criteria (ALL must be true):**
- [ ] Section 1: Title + Overview (exists, 2 sentences, keywords defined)
- [ ] Section 2: Prerequisites (if applicable, uses Level 1-4, no vague items)
- [ ] Section 3: Content (appropriate for doc_type, organized logically)
- [ ] Section 4: Expected Output (table with commands, not prose)
- [ ] Section 5: Troubleshooting (if errors mentioned, each has signature)
- [ ] Section 6: Why This Matters (if relevant, explains rationale)
- [ ] Section 7: What's Next (references other docs by title, includes conditions)
- [ ] No forbidden sections (no "Best Practices", no generic disclaimers)
- [ ] AI metadata blocks in all steps/errors
- [ ] Preconditions/postconditions defined for all steps

**What Fails This Gate:**
- Missing required sections
- Expected Output in prose instead of table
- Troubleshooting errors without signatures
- "See above" instead of doc title references
- Missing AI metadata blocks
- Vague prerequisites ("be comfortable with...")
- No success indicator

**Recovery Action:**
1. Identify failed sections
2. Rewrite using DOC_CANONICAL_TEMPLATE
3. Add missing AI metadata blocks
4. Convert prose Expected Output to table
5. Re-run Gate 2

**Owner:** Automated structure check (can be done via regex or Claude)

**Example Pass:**
```markdown
## What Success Looks Like

| Check | Expected | Command |
|-------|----------|---------|
| Files created | 5 new files in project root | `ls -la \| grep -E "\.md$" \| wc -l` |
| Config valid | No errors when parsed | `yaml -c ./.docgen.yaml` |
```

**Example Fail:**
```markdown
## Expected Outcome

After completing the setup, you should see files in your project.
Everything should be working correctly without errors.
Try running the validation script to make sure.

## Common Issues

If you get an error, check the logs.
Make sure all prerequisites are installed.
```

---

## Gate Level 3: Content (Quality Standards)

**Purpose:** Verify content quality, accuracy, completeness.

**Exit Criteria (ALL must be true):**
- [ ] Overview explains what AND why (not just what)
- [ ] All commands are exact and testable (not "install X")
- [ ] Expected output shown after each step
- [ ] Every error has Root cause + Fix steps
- [ ] Prerequisites are realistic (don't ask for unreasonable knowledge)
- [ ] All external links go directly to download/resource (not homepage)
- [ ] All cross-references use doc titles (not URLs)
- [ ] No acronyms without first definition
- [ ] No ambiguous pronouns ("it", "this", "that" without clear referent)
- [ ] Tone consistent throughout
- [ ] No contradictions between sections
- [ ] **All code blocks pass SYSTEM_Coding_Standards.md checklist:** language tag present, expected output shown, no hardcoded secrets, imports present, dependencies version-pinned, within line-count limits, model strings are current

**What Fails This Gate:**
- Steps are descriptions not commands ("Install the library" vs. `npm install x`)
- No expected output shown
- Errors listed without root causes
- Prerequisites too demanding ("Expert knowledge of Kubernetes")
- Broken external links
- Vague references ("See above")
- Unexplained acronyms
- Inconsistent advice

**Recovery Action:**
1. For each failure, rewrite that section
2. Make commands exact and testable
3. Add expected output
4. Explain error causes
5. Make prerequisites realistic
6. Fix all links and references
7. Define all acronyms
8. Re-run Gate 3

**Owner:** Human review or Claude quality check

**Example Pass:**
```markdown
### Step 1: Install Node.js 16

1. Go to: https://nodejs.org/en/download/ (select LTS v16+)
2. Download the installer for your OS
3. Run the installer, accept defaults
4. Restart terminal (close and reopen)
5. Verify: `node --version` (should show v16.0.0+)

Expected: Terminal shows version number like "v16.13.0"

**AI metadata:**
- Precondition: Administrative access to computer
- Postcondition: Node.js 16+ installed and in PATH
```

**Example Fail:**
```markdown
### Step 1: Set up Node

Install Node.js on your computer. Make sure you get the right version.
Then configure it properly so it works with your project.

**AI metadata:**
- Precondition: You have a computer
- Postcondition: Node is installed
```

---

## Gate Level 4: Quality (Human + AI + Token Check)

**Purpose:** Verify doc passes human quality, AI parsing, and token efficiency.

**Exit Criteria (ALL must be true):**

### Human Quality Check (from Documentation_Content_Guide.md)
- [ ] Content serves clear purpose (passes "why this section?" test)
- [ ] Beginner can follow without external help
- [ ] All steps are actionable (not theoretical)
- [ ] Expected output is specific (not vague)
- [ ] Troubleshooting is organized by symptom, not cause

### AI Quality Check (from AI_First_Documentation_Format.md)
- [ ] Frontmatter extracts correctly (test: Can Claude read it?)
- [ ] Prerequisites are parseable (Levels 1-4 consistent)
- [ ] Steps have preconditions/postconditions (machine readable)
- [ ] Error signatures are exact (copy-paste from actual error output)
- [ ] All links in metadata, not prose
- [ ] Success table has runnable commands
- [ ] Related docs are discoverable from frontmatter

### Token Efficiency Check (see token_budgets.json)
- [ ] Doc token count ≤ domain budget
- [ ] Prose sections are ≤ 4 paragraphs
- [ ] Every section serves purpose (no fluff)
- [ ] Examples are concise but complete
- [ ] Errors: Only top 3-5 included (rest in DEBT.md)

**What Fails This Gate:**
- Human: Beginner can't follow steps
- AI: Claude can't extract prerequisites from metadata
- Token: Setup guide is 8K tokens (budget is 3K)
- Quality score < 85
- Any exit gate criteria unchecked

**Recovery Action:**
1. **Human issues:** Rewrite for clarity, test with user
2. **AI issues:** Fix metadata blocks, ensure parseable structure
3. **Token issues:** Remove non-essential sections, move to DEBT.md
4. **Quality score:** Address low-scoring sections
5. Run all three checks again

**Owner:** Automated checks + human review (if quality_score < 85)

**Token Check Example:**

```json
{
  "doc_type": "how-to",
  "domain": "ai-docs",
  "budget_tokens": 2200,
  "actual_tokens": 2050,
  "token_ratio": 0.93,
  "status": "PASS"
}
```

```json
{
  "doc_type": "project-setup",
  "domain": "claude-project",
  "budget_tokens": 5000,
  "actual_tokens": 8400,
  "token_ratio": 1.68,
  "status": "FAIL - exceeds budget by 68%. Reduce by 3400 tokens or split into 2 docs."
}
```

---

## Gate Level 5: Shipping (Final Approval)

**Purpose:** Final sign-off before doc goes to production.

**Exit Criteria (ALL must be true):**
- [ ] Gate 1 PASSED: Validation
- [ ] Gate 2 PASSED: Structure
- [ ] Gate 3 PASSED: Content Quality
- [ ] Gate 4 PASSED: Human + AI + Token Quality
- [ ] DEBT.md created with known limitations
- [ ] metadata.json complete with quality_score, exit_gates_passed
- [ ] Version number assigned (v1.0, v1.1, etc.)
- [ ] Status set to "production" (not draft/review)
- [ ] Related docs checked (exist and correct)
- [ ] Skill suggestion reviewed (published, suggested, or declined)
- [ ] Doc added to appropriate project knowledge base
- [ ] Generation logged in metrics/generation_log.md

**What Fails This Gate:**
- Any earlier gate failed
- DEBT.md missing or incomplete
- metadata.json incomplete
- Status still "draft" or "review"
- Related docs don't exist
- No entry in generation log

**Recovery Action:**
1. Return to failing gate
2. Fix all issues
3. Re-run Gates 1-4
4. Create DEBT.md
5. Generate metadata.json
6. Update status to "production"
7. Add to metrics log
8. Re-run Gate 5

**Owner:** Project owner or team lead (not automated)

**Final Checklist:**
```markdown
## Shipping Checklist

### Gate Status
- [✅] Gate 1: Validation PASSED
- [✅] Gate 2: Structure PASSED
- [✅] Gate 3: Content Quality PASSED
- [✅] Gate 4: Human + AI + Token Quality PASSED

### Production Readiness
- [✅] DEBT.md exists with all known issues
- [✅] metadata.json has quality_score >= 85
- [✅] All exit_gates_passed: [1,2,3,4,5]
- [✅] Status: production
- [✅] Version: v1.0

### Documentation
- [✅] Related docs exist and are current
- [✅] Skill suggestion reviewed (status: published/suggested/declined)
- [✅] Doc added to project knowledge base
- [✅] Generation logged in metrics/generation_log.md

### Sign-Off
- Reviewed by: [name]
- Date: YYYY-MM-DD
- Approved for shipping: YES ✅
```

---

## Gate Failure Recovery Matrix

| Gate | Failure | Time to Fix | Recovery | Escalation |
|------|---------|------------|----------|------------|
| 1 | Invalid frontmatter | 5 min | Re-run builder | Builder has bug |
| 2 | Missing sections | 15 min | Add sections manually | Template unclear |
| 3 | Vague instructions | 30 min | Rewrite with examples | Builder needs improvement |
| 4 | Token bloat | 20 min | Remove non-essentials, move to DEBT | Domain budget too tight |
| 5 | Missing DEBT.md | 10 min | Generate from builder feedback | Builder output incomplete |

---

## Gate Performance Metrics

Track for continuous improvement:

```json
{
  "gates_performance": {
    "gate_1_validation": {
      "total_documents": 450,
      "pass_rate": 0.98,
      "common_failures": ["invalid_doc_type", "missing_audience"],
      "avg_time_to_fix_minutes": 3
    },
    "gate_2_structure": {
      "total_documents": 441,
      "pass_rate": 0.94,
      "common_failures": ["missing_metadata_blocks", "prose_expected_output"],
      "avg_time_to_fix_minutes": 12
    },
    "gate_3_content": {
      "total_documents": 415,
      "pass_rate": 0.88,
      "common_failures": ["vague_steps", "no_expected_output", "broken_links"],
      "avg_time_to_fix_minutes": 28
    },
    "gate_4_quality": {
      "total_documents": 366,
      "pass_rate": 0.92,
      "common_failures": ["token_budget_exceeded", "quality_score_low"],
      "avg_time_to_fix_minutes": 22
    },
    "gate_5_shipping": {
      "total_documents": 336,
      "pass_rate": 0.99,
      "common_failures": ["missing_debt_md", "related_docs_broken"],
      "avg_time_to_fix_minutes": 8
    }
  }
}
```

---

## No Doc Ships Without All 5 Gates Passing

This is non-negotiable. A doc that:
- Passes Gates 1-4 but fails Gate 5 → stays in draft
- Passes Gate 4 but fails Gate 3 → goes back to rewriting
- Fails ANY gate → cannot be marked "production"

**Status meanings:**
- **draft:** Failed at least one gate, still being fixed
- **review:** Passed all gates, awaiting final approval (Gate 5)
- **production:** All 5 gates PASSED, shipping to users
- **deprecated:** Was production, now archived

Only "production" docs are visible to users in projects/output.


========================================================================
SYSTEM File Naming
========================================================================

# SYSTEM_File_Naming.md — LLM-Optimized Naming Convention

**Why naming matters for AI:** Claude reads filenames before reading content. A file named `SYSTEM_Exit_Rules.md` tells Claude "this is a system framework file about exit rules" before it processes a single word. A file named `rules.md` tells it nothing. Research confirms: descriptive filenames improve AI retrieval accuracy significantly in RAG contexts.

---

## Core Principle

**The filename is the first question it answers.** Every filename should complete the sentence: "This file contains [FILENAME]."

- `SYSTEM_Exit_Rules.md` → "This file contains system exit rules." ✅
- `BUILDER_Questions.md` → "This file contains builder questions." ✅
- `rules.md` → "This file contains... rules? For what?" ❌
- `doc1.md` → No signal at all. ❌

---

## Two Naming Patterns

### Pattern A: Framework Files (system infrastructure)

Files that ARE the documentation system — guides, templates, checklists, builders, research.

```
{TYPE}_{Topic}.md
```

Examples:
```
SYSTEM_Exit_Rules.md
CHECKLIST_Human_Quality.md
BUILDER_Questions.md
RESEARCH_Claude_Best_Practices.md
PROJECT_INSTRUCTIONS_Docgen_Production.md
```

### Pattern B: Generated Output Documents (docs the system produces)

Files that are produced BY the system — the deliverables for users.

```
{DOMAIN}_{Topic}_v{X.Y}_{YYYY-MM-DD}.md
```

Examples:
```
CODE_Stripe_Setup_v1.0_2026-04-03.md
AI-DOCS_Welcome_Guide_v1.0_2026-04-03.md
CLAUDE-PROJECT_Marketing_Hub_v1.0_2026-04-03.md
REFERENCE_API_Config_v2.1_2026-04-03.md
```

---

## TYPE Prefixes — Framework Files

Every framework file MUST start with one of these TYPE prefixes. Type prefix = ALL_CAPS + underscore.

| TYPE Prefix | What It Signals | Examples |
|---|---|---|
| `SYSTEM_` | Authoritative framework rule — read-only, never edit | `SYSTEM_Exit_Rules.md`, `SYSTEM_Coding_Standards.md` |
| `TEMPLATE_` | Document template — blank structure to fill in | `TEMPLATE_Debt_Standard.md` |
| `DOC_` | THE canonical output template | `DOC_CANONICAL_TEMPLATE.md` |
| `CHECKLIST_` | Quality gate checklist | `CHECKLIST_Human_Quality.md`, `CHECKLIST_AI_Quality.md` |
| `EXAMPLE_` | Complete example showing target quality | `EXAMPLE_Perfect_Setup_Guide.md` |
| `BUILDER_` | Builder intake questionnaire or rules file | `BUILDER_Questions.md`, `BUILDER_Rules.md` |
| `RESEARCH_` | Research findings and external source synthesis | `RESEARCH_Claude_Project_Best_Practices.md` |
| `PROJECT_INSTRUCTIONS_` | Claude.ai project instructions — paste-ready | `PROJECT_INSTRUCTIONS_Docgen_Production.md` |
| `LOG_` | Logs, metrics, generation tracking | `LOG_Generation.md` |
| `DEBT_` | Technical debt specification or tracker | `DEBT_Specification.md`, `SYSTEM_DEBT.md` |

### Special auto-detected files (no TYPE prefix)

These file names are auto-detected by tools and must be EXACT — no prefix:

| File | Why exact | Detected by |
|---|---|---|
| `CLAUDE.md` | Auto-loaded by Claude Code, Claude Projects | Claude |
| `README.md` | Auto-displayed by GitHub, file browsers | GitHub, many tools |
| `CONTRIBUTING.md` | Standard open-source convention | GitHub |
| `LICENSE` | Standard convention — no extension | GitHub, npm, pip |

---

## DOMAIN Categories — Output Documents

Must match `config/domain_definitions.json`. Used as the CATEGORY prefix in output file names.

| Domain prefix | Domain | Description |
|---|---|---|
| `CLAUDE-PROJECT_` | claude-project | Full Claude project setup from an idea |
| `AI-DOCS_` | ai-docs | Individual AI docs (how-tos, references, features) |
| `CODE_` | code | Code documentation (setup, API, architecture, ADR) |
| `REFERENCE_` | reference | Reference material (configs, schemas, commands) |

---

## Separator Rules

This is critical for LLM parsing. Different separators communicate different relationships:

| Separator | Role | Where |
|---|---|---|
| `_` (underscore) | Separates **elements** from each other | Between TYPE and Topic; between Topic and Version; between Version and Date |
| `_` or PascalCase | Separates **words within** an element | `Exit_Rules` or `ExitRules` — both valid within a topic |
| `-` (hyphen) | Separates words in **folder names only** | `claude-project/`, `ai-docs/` — never in file names |
| Never use spaces | N/A | Spaces break paths and LLM file tools |

```
SYSTEM_Exit_Rules.md
^      ^ ^         ^
TYPE   _ Topic     .ext

CODE_Stripe_Setup_v1.0_2026-04-03.md
^    ^      ^     ^    ^
DOM  _Topic_      _Ver _Date
```

---

## Topic Naming Rules

Topics in framework files use `PascalCase` or `Title_Case`:

```
✅ GOOD  SYSTEM_Exit_Rules.md       (Title_Case — first letter each word)
✅ GOOD  SYSTEM_ExitRules.md        (PascalCase — also valid)
❌ BAD   SYSTEM_exit_rules.md       (all lowercase — no visual separation from prefix)
❌ BAD   SYSTEM_EXITRULES.md        (all caps — looks like another prefix)
❌ BAD   SYSTEM_Exit-Rules.md       (hyphen in filename — reserved for folders)
```

Topics in output documents use `Title_Case` (matches the document's title):

```
✅ GOOD  CODE_Stripe_Payment_Setup_v1.0_2026-04-03.md
❌ BAD   CODE_stripe-payment-setup_v1.0_2026-04-03.md
❌ BAD   CODE_StripePaymentSetup_v1.0_2026-04-03.md  (PascalCase harder to read at speed)
```

---

## Version Rules

```
v1.0    Initial release
v1.1    Minor update (backwards compatible)
v2.0    Major revision (breaking changes or full rewrite)
```

**Include VERSION when:** Multiple versions in active use, or backwards compatibility tracking needed.

**Omit VERSION when:** Only one version exists, or version tracked in folder structure.

---

## Date Rules

Use ISO 8601 format: `YYYY-MM-DD`. Always. No exceptions.

```
✅ 2026-04-03   (ISO 8601 — sorts correctly, machine-readable)
❌ April 2026   (not sortable)
❌ 04-03-2026   (ambiguous locale format)
❌ 2026-Q1      (acceptable for quarterly docs only)
```

**Include DATE when:** Content has a shelf life, quarterly/annual updates, or distinguishing "old" from "current" matters.

**Omit DATE when:** Evergreen content, or using version numbers instead.

---

## Companion Files

Every generated output document ships with two companions:

```
CODE_Stripe_Setup_v1.0_2026-04-03.md          ← Main doc
CODE_Stripe_Setup_v1.0_2026-04-03.DEBT.md     ← Known gaps
CODE_Stripe_Setup_v1.0_2026-04-03.metadata.json ← Generation metadata
```

All three always together. Missing a companion = Gate 5 fail.

---

## Folder + Filename Combined Context

The folder provides the domain context. The filename provides the type + topic context. Together they create unambiguous meaning for an AI agent navigating the workspace.

```
✅ GOOD — full context from path alone:
system/guides/SYSTEM_Exit_Rules.md
  └── "system framework guide: exit rules"

builders/claude-project/BUILDER_Questions.md
  └── "builder for claude-project domain: intake questions"

output/claude-project/v1.0/CLAUDE-PROJECT_Code_Reviewer_v1.0_2026-04-03.md
  └── "output: claude-project domain, Code Reviewer assistant, version 1.0, April 2026"

❌ BAD — ambiguous path:
builders/claude-project/rules.md
  └── "rules? for what? for whom? which version?"

output/doc1.md
  └── completely opaque to AI and humans
```

---

## Forbidden Patterns

❌ Never use in file names:
- Spaces → `Exit Rules.md` (use `Exit_Rules.md`)
- Hyphens → `Exit-Rules.md` (use `Exit_Rules.md` — hyphens for folders only)
- Special chars → `(final)`, `#`, `@`, `$`, `%`
- Emojis → `🚀_Launch.md`
- Double underscores → `SYSTEM__Exit.md`
- Consecutive version + date without underscore → `v1.02026-04-03`
- Abbreviations in topic → `Sys_Ex_Rl.md` (spell it out)
- `[ARCHIVED]` or `[DEPRECATED]` brackets → use `ARCHIVED_` or `DEPRECATED_` prefix instead

---

## Naming Checklist

Before saving any file, verify:

**Framework files:**
- [ ] Starts with a valid TYPE prefix (`SYSTEM_`, `CHECKLIST_`, `BUILDER_`, etc.)
- [ ] Topic is PascalCase or Title_Case (not all-lowercase, not all-caps)
- [ ] No hyphens in filename (hyphens only in folder names)
- [ ] No spaces or special characters

**Output documents:**
- [ ] Starts with valid DOMAIN prefix (`CLAUDE-PROJECT_`, `AI-DOCS_`, `CODE_`, `REFERENCE_`)
- [ ] Topic is Title_Case, underscore-separated words
- [ ] Version included if needed (`v1.0` format)
- [ ] Date in ISO 8601 if time-sensitive (`YYYY-MM-DD`)
- [ ] Both companion files created (`DEBT.md`, `metadata.json`)

**Both:**
- [ ] Full path makes unambiguous sense (folder + filename together)
- [ ] Filename answers "What does this file contain?" without reading it

---

## Migration Reference

Current violations → corrected names:

| Was | Should be | Reason |
|---|---|---|
| `builder.md` | `BUILDER_Questions.md` | No type prefix |
| `rules.md` | `BUILDER_Rules.md` | No type prefix |
| `generation_log.md` | `LOG_Generation.md` | No type prefix |
| `Project_Instructions_X.md` | `PROJECT_INSTRUCTIONS_X.md` | Inconsistent case |
| `[ARCHIVED]_doc.md` | `ARCHIVED_doc.md` | Brackets break many systems |
| `doc-topic.md` | `DOC_Topic.md` | Hyphens in filenames reserved for folders |

---

*Documentation Builder · File Naming Standard v1.1 · April 2026*
*Research basis: Anthropic context engineering docs, RAG knowledge base best practices, Claude Code community conventions*


========================================================================
SYSTEM Master Index
========================================================================

# Documentation Generation System — Master Index

**Complete system for creating, structuring, and validating production-grade documentation.**

---

## File Overview & Reading Order

### 1. **START HERE: This Index**
- Orientation: What files exist, what they do, how they fit together
- Reading time: 5 minutes
- Use: First time only

### 2. **Documentation Content Guide** (16K)
- Comprehensive standards for doc content structure
- What sections every doc needs (critical, important, optional)
- When to include each section based on doc type
- Reading time: 20 minutes, reference later
- Use: Before writing any documentation

### 3. **Prerequisites Guide** (12K)
- Deep dive into prerequisite sections
- 4 levels of prerequisites (tools, access, knowledge, state)
- Examples for each documentation type
- Reading time: 20 minutes
- Use: When writing setup/install/configuration docs

### 4. **Documentation Ecosystem Strategy** (9K)
- High-level overview of what documentation types exist
- Priority 1 vs Priority 2 vs Optional files
- Decision matrix for what to build first
- Reading time: 15 minutes
- Use: Planning your documentation system

### 5. **Project Chat Instructions Rules** (8K)
- Rules for creating Claude Projects custom instructions
- 500–800 word limit, 6-section structure
- Anti-patterns to avoid
- Quality checklist
- Reading time: 15 minutes
- Use: When setting up a Claude Project

---

## How These Files Connect

```
Documentation_Content_Guide.md
  ├── Defines all sections every doc needs
  └── References: Prerequisites_Guide.md (for prereq section)

Prerequisites_Guide.md
  ├── Detailed coverage of ONE section
  ├── Examples for different doc types
  └── Integrates: Setup, API, Config, Troubleshooting docs

Documentation_Ecosystem_Strategy.md
  ├── Shows what files/docs to create
  ├── Priority ranking
  └── Recommends starting with these Templates:
      - CLAUDE.md
      - Project Instructions
      - SKILL.md
      - 8 Doc Type Templates

Project_Chat_Instructions_Rules.md
  ├── Rules for ONE specific file type
  └── Used in: Claude Projects setup
```

---

## Quick Decision Tree: Which File Do I Need?

**I'm writing documentation from scratch**
→ Start: Documentation_Content_Guide.md → Prerequisites_Guide.md

**I'm writing a setup/installation guide**
→ Use: Documentation_Content_Guide.md + Prerequisites_Guide.md

**I'm writing API documentation**
→ Use: Documentation_Content_Guide.md (check API doc type section)

**I'm setting up a Claude Project with custom instructions**
→ Use: Project_Chat_Instructions_Rules.md

**I want to build a complete documentation system**
→ Read in order: Documentation_Ecosystem_Strategy → then each template file

**My docs aren't working — readers are confused**
→ Use: Documentation_Content_Guide.md Quality Checklist (section: "When Docs Fail")

---

## Implementation Paths

### Path A: Single Document (1–2 hours)
Use case: Write one good doc quickly

1. Open Documentation_Content_Guide.md
2. Find your doc type section (Setup, API, Config, etc.)
3. Follow the structure
4. Check your prerequisites section against Prerequisites_Guide.md
5. Run through "Quality Checklist" before publishing

### Path B: Documentation System (6–8 hours)
Use case: Build reusable system for a project/team

1. Read Documentation_Ecosystem_Strategy.md
2. Create templates from Priority 1 section:
   - CLAUDE.md template
   - Project Instructions template
   - SKILL.md template
   - 8 Doc Type templates
3. Run each template through "Quality Checklist"
4. Test templates with 1–2 real docs
5. Add to your project/team wiki

### Path C: Document Audit (2–3 hours)
Use case: Fix existing documentation

1. For each doc, check Documentation_Content_Guide.md
2. Go through "Quality Checklist" for that doc type
3. Note what's missing or wrong
4. Use Prerequisites_Guide.md if prereqs need work
5. Rewrite problem sections

---

## File Purposes at a Glance

| File | What It Teaches | Use When | Length |
|------|-----------------|----------|--------|
| Documentation_Content_Guide | All doc sections, every type, examples | Writing any doc | 16K |
| Prerequisites_Guide | 4 levels of prerequisites, anti-patterns | Setting up prerequisites | 12K |
| Documentation_Ecosystem | Overall strategy, priorities, roadmap | Planning doc system | 9K |
| Project_Chat_Instructions_Rules | How to write custom instructions | Setting up Claude Project | 8K |

---

## Production Checklist: Before Sharing Any Documentation

**Content Quality:**
- [ ] Each section serves a purpose (passes "Why this section?" test)
- [ ] No vague language (see: Documentation_Content_Guide anti-patterns)
- [ ] All steps are exact commands/actions, not descriptions
- [ ] Prerequisites are specific, testable, realistic
- [ ] Expected output provided for each step

**Completeness:**
- [ ] All critical sections present (see: Documentation_Content_Guide critical sections)
- [ ] Links work (test each one)
- [ ] Code examples run without modification
- [ ] Screenshots/diagrams have alt text

**Clarity:**
- [ ] A beginner can complete the task using this doc alone
- [ ] No acronyms without definition (first use: define it)
- [ ] No references to "section X above" without location
- [ ] Tone is consistent throughout

**Usability:**
- [ ] Table of contents for docs >500 words
- [ ] Search-friendly (keywords in headers)
- [ ] No walls of text (break into sections, use lists)
- [ ] "Next steps" section points to related docs

**Testing:**
- [ ] Walk through it yourself (catch obvious errors)
- [ ] Give to someone unfamiliar, watch them try it
- [ ] Note where they get stuck or confused
- [ ] Fix those sections

---

## Common Scenarios

### Scenario 1: "My docs look complete but people still get stuck"
**Root cause:** Missing expected output or unclear success indicators

**Fix:**
1. Check Documentation_Content_Guide: "Expected Output" section
2. Add what success looks like after each step
3. Add verification commands

### Scenario 2: "Prerequisites are too long and people skip them"
**Root cause:** Asking for too much or not being specific enough

**Fix:**
1. Check Prerequisites_Guide: "Level 3: Knowledge/Understanding"
2. Remove anything not absolutely necessary
3. Add check commands so people verify quickly
4. Add "Ready? Run this test" command

### Scenario 3: "I don't know what to write next"
**Root cause:** Missing "Next Steps" or unclear section ordering

**Fix:**
1. Check Documentation_Content_Guide: "Next Steps" section
2. Add what people should do after completing this doc
3. Link to related docs (if applicable)

### Scenario 4: "My documentation system is a mess"
**Root cause:** No consistent structure across documents

**Fix:**
1. Read Documentation_Ecosystem_Strategy.md
2. Pick ONE doc type to standardize first
3. Create template from Documentation_Content_Guide.md
4. Update all existing docs to match template
5. New docs automatically follow template

---

## Updates & Maintenance

**These files are living documents.** Update them when:
- You discover patterns that don't work
- Your team evolves or changes
- You find anti-patterns not covered

**How to update:**
1. Note what failed or what worked better
2. Add to relevant file (section: "Common Mistakes" or "Lessons Learned")
3. Share update with team
4. Update any templates based on learnings

---

## Next Steps

1. **Choose your path:** Single doc, full system, or audit?
2. **Start with relevant file:** See "Quick Decision Tree" above
3. **Apply template:** Use the structure, follow examples
4. **Check quality:** Run through the appropriate checklist
5. **Test:** Have someone unfamiliar try following your doc

---

**Questions about these files?** Each file has its own quality checklist and anti-patterns section.


========================================================================
SYSTEM Prerequisites Guide
========================================================================

# Prerequisites in Technical Documentation: Complete Guide

## WHAT ARE PREREQUISITES

Prerequisites are the section that answers:
**"What do I need BEFORE I start this instruction?"**

❌ Wrong: "Make sure everything is ready"
✅ Right: "Need SSH access and Node.js 16+"

---

## PREREQUISITES STRUCTURE

### Level 1: Tools/Software
```markdown
## Prerequisites

### Required software
- Node.js 16 or higher (`node --version` to check)
- npm 8+ (`npm --version` to check)
- Git installed (`git --version` to check)
```

**What matters:**
- Exact version, not "latest"
- Command to check if already installed
- Link to install if missing

**Example ❌ BAD:**
```
You need Node.js
```

**Example ✅ GOOD:**
```
Node.js 16 or higher
- Check: `node --version`
- If you don't have it: https://nodejs.org/en/download/ (select v16 LTS or newer)
```

---

### Level 2: Access/Permissions
```markdown
### Required access
- SSH access to server: `ssh user@server.com`
- Admin rights in database (ask your database admin)
- Stripe API key from your dashboard (Settings → API Keys)
```

**What matters:**
- How to verify you have access
- Where to get it
- Who can grant it

**Example ❌ BAD:**
```
You need API key access
```

**Example ✅ GOOD:**
```
Stripe API key
- Where to find: Stripe Dashboard → Settings → API Keys
- Copy: Secret key (starts with sk_live_ or sk_test_)
- Check: `echo $STRIPE_SECRET_KEY` (should not be empty)
- If you don't have: Ask your manager for Stripe account access
```

---

### Level 3: Knowledge/Understanding
```markdown
### Required knowledge
- Basic command line (how to open terminal, run commands)
- Basic Git workflow (clone, commit, push)
- JSON format (what it is, not how to write from scratch)
```

**What matters:**
- Be honest about what's needed
- Don't overestimate (don't require a PhD)
- Provide links to 5-10 min guides

**Example ❌ BAD:**
```
Understanding of Docker and Kubernetes
```

**Example ✅ GOOD:**
```
Basic Docker knowledge
- What you need: Know what `docker run` does
- Don't need: Kubernetes, advanced networking
- Quick intro: https://docker-curriculum.com/ (5-10 min read)
```

---

### Level 4: Current State/Setup
```markdown
### What should be ready before starting
- Your project already cloned: `git clone <repo>`
- You're in project directory: `cd my-project`
- Dependencies installed: `npm install` (already ran)
```

**What matters:**
- Exact command or action needed
- How to verify it was completed

**Example ❌ BAD:**
```
Make sure everything is set up
```

**Example ✅ GOOD:**
```
Project is ready
- If not done yet: `git clone <repo> && cd <repo> && npm install`
- Check: `npm list` (should show your packages)
```

---

## WHEN TO WRITE EACH SECTION

| What | When to write | When to skip |
|-----|-------------|-------------|
| **Tools** | Always if software is needed | If using built-in tools only |
| **Access** | Always if API keys/passwords needed | If data is public |
| **Knowledge** | If topic is specialized | If basic knowledge (link to guide instead) |
| **State** | If pre-setup needed | If nothing required |

---

## EXAMPLES BY DOCUMENTATION TYPE

### 1️⃣ For "How to Install" Guide (Setup Guide)

```markdown
## Prerequisites

Before you start, make sure you have:

### Software
- macOS 10.15+ or Windows 10+ (we don't test on Linux)
  - Check your version: Click Apple icon → About This Mac
  
### Knowledge
- Comfortable with terminal (5 min tutorial: https://bit.ly/terminal-basics)

### Time
- ~15 minutes for installation

## How to check if you're ready
Run this command in terminal:
```
which node && node --version
```
If you see: `v16.0.0` or higher, you're good.
If you see: `not found`, go to next section (Install Node.js).
```

---

### 2️⃣ For "How to Use API" Guide (API Guide)

```markdown
## Prerequisites

### Software
- cURL or Postman (any API testing tool)
- Node.js 14+ (optional, for testing with code)

### Access & Keys
- Stripe API key (you'll need this)
  - Where: https://dashboard.stripe.com/apikeys
  - Which one: Copy the "Secret key" (sk_live_... or sk_test_...)
  - Set it: `export STRIPE_SECRET_KEY="sk_test_..."`

### Knowledge
- What HTTPS requests are (basic idea)
- What JSON is (basic idea)
- ✓ Don't need: Stripe internals or webhooks yet

### Ready? Test this command:
```bash
curl -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  https://api.stripe.com/v1/customers
```
You should get: `{"object":"list","data":[],...}`
If you get error: Check your API key in .env file
```

---

### 3️⃣ For "How to Configure" Guide (Configuration)

```markdown
## Prerequisites

### Current state
- Code already cloned: `git clone <repo> && cd my-project`
- Node.js installed: `node --version` (should be v16+)
- Dependencies installed: `npm install` (takes ~2 min)

### Verify you're ready
Run this:
```bash
npm run verify-setup
```

You should see: ✅ All checks passed

If you see error: Tell us the exact error message (we'll help)
```

---

### 4️⃣ For "How to Troubleshoot" Guide (Troubleshooting)

```markdown
## Prerequisites

You should have:
- The error message from your logs
- Knowledge of where to find logs:
  - macOS/Linux: `~/.app/logs/`
  - Windows: `C:\Users\YourName\AppData\Local\app\logs\`

## Verify before continuing
Run: `tail -50 ~/.app/logs/latest.log`
This shows the last 50 lines of your logs.
If you see errors → continue to "Common Issues" section
If you see no errors → problem might be different (ask in #support)
```

---

## ANTI-PATTERNS (DON'T DO THIS)

### ❌ Too vague
```markdown
### Prerequisites
- Be comfortable with the command line
- Have basic knowledge of programming
- Make sure everything is installed
```

### ✅ Specific
```markdown
### Prerequisites

**Software you need:**
- Node.js 16+: Check with `node --version`
- npm 8+: Check with `npm --version`

**Knowledge level:**
- Know how to open terminal and run commands
- Understand what `npm install` does
- Don't need: React, TypeScript, anything advanced

**Your project setup:**
1. Clone: `git clone <repo>`
2. Install: `npm install`
3. Verify: `npm run test` (should show 0 errors)

**Time needed:** 20 minutes
```

---

### ❌ Asking for too much
```markdown
Prerequisites:
- Degree in Computer Science
- 5 years of backend development experience
- Expert knowledge of Docker and Kubernetes
```

### ✅ Realistic
```markdown
Prerequisites:
- Basic command line skills
- Familiarity with JSON format (just what it is, not writing)
- 30 minutes of free time
```

---

### ❌ No way to verify
```markdown
Make sure you have Git installed
Make sure your database is running
Make sure you have the right permissions
```

### ✅ Provide verification
```markdown
**Git installed?**
Run: `git --version`
Expected: `git version 2.x.x`

**Database running?**
Run: `psql -l` (PostgreSQL) or `mysql -u root` (MySQL)
Expected: You see a list of databases

**Permissions OK?**
Run: `ls -l ~/.ssh/config`
Expected: File exists and you see it
```

---

## TEMPLATE TO COPY

```markdown
## Prerequisites

### Tools & Software
- [Tool name] [version]: [check command]
  - Where to get: [link]

### Access & Keys
- [What access]: [where to find/how to get]
  - Check: [command]

### Knowledge you need
- [Topic 1]: [quick 5-min resource]
- [Topic 2]: [quick 5-min resource]
- NOT needed: [what you don't need]

### Your current setup
- [Thing 1]: [verify with this command]
- [Thing 2]: [verify with this command]

### Ready?
Run this to check everything is good:
```
[command that verifies all prerequisites]
```

Expected result: [what should happen]
If error: [what to do]
```

---

## WRITING RULES

1. **Specificity** — use exact versions and commands, not generic phrases
2. **Verifiability** — for each prerequisite provide a check command
3. **Direct links** — link to downloads, not homepage
4. **Realism** — ask for what's actually needed, not more
5. **Time** — if > 5 min prep time, state how long it takes
6. **Honesty** — "This is more complex than I said" is better than surprises

---

## INTEGRATION INTO DOCUMENTATION

### In Claude Projects (Knowledge Base)
```markdown
# Setup Prerequisites

## For Node.js projects
- Required: Node 16+, npm 8+
- Check: [create template doc with all checks]

## For Python projects  
- Required: Python 3.9+, pip 21+
- Check: [create template doc with all checks]
```

### In CLAUDE.md (for Claude Code)
```markdown
## Prerequisites for this project

### Before running any code:
- Node 16+: `node --version`
- npm 8+: `npm --version`
- .env file exists: `cat .env | head -5`

### To run tests:
- Jest 27+: `npm list jest`
- 5 GB disk space: `df -h | grep /`
```

### In SKILL.md (for repeatable task)
```markdown
---
name: payment-setup
description: Set up Stripe payments
---

## Prerequisites
- Stripe account with API keys ready
  - Get keys: https://dashboard.stripe.com/apikeys
- .env file in project root with:
  - STRIPE_SECRET_KEY
  - STRIPE_PUBLISH_KEY

## Check you're ready
Run: `echo $STRIPE_SECRET_KEY` (should not be empty)
```

---

## COMMON MISTAKES

| Mistake | Why it's bad | Correct way |
|---------|-------------|------------|
| "Install Node.js" | Which version? Where from? | "Node.js 16+ from nodejs.org/download" |
| "Know basics" | Which exactly? | "Know how `npm install` works (5-min intro: link)" |
| "Have SSH access" | How to verify? | "SSH access (`ssh user@server.com` works)" |
| "15 minutes" | For which skill level? | "15 min for experienced devs, 30 min for beginners" |
| "Requirements list" | With no check | "Each requirement includes: verify command" |

---

## PRE-PUBLICATION CHECKLIST

- [ ] Each software has a version (not just "Git", but "Git 2.30+")
- [ ] Each software requirement has a check command
- [ ] All links go directly to download (not homepage)
- [ ] Knowledge requirements are realistic (not asking for PhD for simple task)
- [ ] Time stated if > 5 minutes
- [ ] Command provided to verify everything is ready
- [ ] No vague phrases ("make sure everything", "be ready")
- [ ] A beginner can complete all prerequisites without help

---

## GOOD PREREQUISITES EXAMPLES

### Example 1: Simple task (2 min)
```markdown
## Prerequisites

Run this:
```bash
node --version    # Should be 16+
npm --version     # Should be 8+
```

If you see errors: Install Node from https://nodejs.org/en/download/
```

### Example 2: Medium complexity (15 min)
```markdown
## Prerequisites

1. Clone the repo:
   ```bash
   git clone <repo-url>
   cd my-project
   ```
2. Check Node:
   ```bash
   node --version  # Should be 16.0.0+
   ```
3. Install deps:
   ```bash
   npm install
   ```
4. Create .env:
   ```bash
   cp .env.example .env
   nano .env  # Edit with your values
   ```
5. Run setup:
   ```bash
   npm run setup
   ```
   
Expected: ✅ Setup complete message appears
```

### Example 3: Complex task (30+ min)
```markdown
## Prerequisites

### Skills needed (20 min to learn)
- Terminal basics: https://ubuntu.com/tutorials/command-line-for-beginners
- Git workflow: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository

### Software (15 min to install)
- Node.js 16+
  - Download: https://nodejs.org/en/download/ (choose LTS)
  - Verify: `node --version`
  
- Docker (20 min)
  - Download: https://www.docker.com/products/docker-desktop
  - Verify: `docker --version`
  - Start app: Open Docker Desktop

### Access (5 min)
- GitHub account with access to this repo
- Verify: `git clone <repo>` works without asking for password

### Verification (2 min)
Run this, everything should ✅:
```bash
node --version &&
docker --version &&
git clone <test-repo> &&
echo "All prerequisites OK"
```
```

---

## WHEN PREREQUISITES ARE WRONG

Signs that prerequisites are poorly written:
- People say "I got error on step 2 but prerequisites are done"
- Many questions like "Do I really need this?"
- People skip prerequisites and get stuck later
- "I didn't know this version was required"

**How to fix:**
1. Check error logs
2. Add something to prerequisites
3. Add check command for what broke
4. Verify a beginner can complete all prerequisites


========================================================================
SYSTEM Project Instructions Rules
========================================================================

# Project Chat Instructions — Generation Rules

## What They Are

Custom instructions Claude receives when operating in a specific Claude Project. Define role, constraints, response format, and how Claude interprets context from the project's knowledge base.

**Scope:** Project-level behavior, not global Claude behavior.

---

## The Curse of Instructions (Research Finding)

More rules = lower compliance per rule. A system prompt with 50 rules follows each one ~60% of the time. With 7 rules, compliance per rule rises to ~90%.

**Implication:** Every rule you add pushes out compliance on all existing rules. Include only instructions Claude won't follow correctly by default. Delete anything obvious.

**Hard limit:** 5 Do's maximum + 5 Don'ts maximum = 10 total behavioral rules. No exceptions.

---

## Core Rules

### 1. Length Constraint: 500–800 words max
- Longer = more tokens burned, less context for actual work
- Too short (< 300 words) = vague, contradictory behavior
- Target: Dense, no filler. Under 500 words is fine if rules are specific.

### 2. Structure (recommended order)
1. **Role** — Who Claude becomes in this project (2-3 sentences)
2. **Context Interpretation** — How to read uploaded docs (2-3 sentences)
3. **Response Format** — What users should expect (style, structure, length)
4. **Do's** — 3–5 specific behaviors (bullet points)
5. **Don'ts** — 3–5 things never to do (bullet points)
6. **Examples** — 1–2 good responses, 1–2 bad responses (short snippets)

### 3. Role Definition
**Format:** One sentence for what you are, one for what you provide.

**Good:**
- "You are a technical documentation reviewer. You evaluate docs for clarity, completeness, and usability, then provide specific fixes."

**Bad:**
- "Help users with documentation." (vague, could mean anything)
- "You are an expert in all areas of documentation." (overpromise, no specificity)

### 4. Context Interpretation
**Critical rule:** Tell Claude how to use uploaded files, not what files exist.

**Good:**
- "Treat all .md files in this project as authoritative reference material. If a question relates to a topic covered in the files, quote relevant sections before answering."
- "Use prerequisites_guide.md as the gold standard for what good prerequisites look like."

**Bad:**
- "This project contains a prerequisites guide, documentation ecosystem plan, and templates." (listing, not instruction)
- "Read all the files." (too vague—which files? how should they inform behavior?)

### 5. Response Format Rules
**Be specific about:**
- Length (e.g., "Keep answers under 200 words unless user asks for depth")
- Structure (e.g., "Organize as: Problem → Root Cause → Fix → Why")
- Tone (e.g., "Direct, no preamble, no corporate jargon")
- Examples (e.g., "Always show before/after code or before/after copy")
- When to ask vs. answer (e.g., "If requirements are ambiguous, stop and ask. Don't guess.")

**Bad format examples:**
- "Be helpful and accurate." (meaningless)
- "Provide comprehensive responses." (how comprehensive? what does that look like?)
- "Use best practices." (which practices?)

### 6. Do's — Specific Behaviors
Each do must be:
- One action (not "do X and Y")
- Observable (someone could verify you're doing it)
- Tied to project purpose

**Good:**
- "Quote the prerequisites template whenever discussing what good prerequisites look like."
- "When evaluating docs, always reference the quality checklist."
- "If user asks for a doc type not in the templates, suggest the closest match + explain why."

**Bad:**
- "Always be thorough." (unmeasurable)
- "Help the user succeed." (too broad)

### 7. Don'ts — Hard Constraints
Things Claude must never do in this project, even if user asks. **Max 5. Each must include WHY — agents follow rules they understand.**

**Good:**
- "Do not generate documentation without referencing the Documentation_Content_Guide first. Without this, output will lack required sections and fail Gate 2."
- "Do not suggest docs are finished without running the quality checklist. Unverified docs fail silently in production."

**Bad:**
- "Don't be unhelpful." (not a constraint, it's obvious)
- "Don't make mistakes." (unmeasurable, implies you won't)
- "NEVER do X." (aggressive language overtriggers in Claude Sonnet — use "Do not" instead)

### 8. Examples — Show, Don't Tell
**Include:**
- 1 good response (full, or key excerpt)
- 1 bad response (the mistake you want to avoid)
- 2–3 sentences explaining why one is better

**Length:** Keep examples short (3–5 lines each).

**Example structure:**
```
GOOD:
User: "How should prerequisites be organized?"
Claude: [Answer that quotes template and gives specific structure]

BAD:
User: "How should prerequisites be organized?"
Claude: [Generic answer with no reference to project docs]

Why: Good answer anchors to the project's standard; bad answer ignores project context.
```

### 9. Negative Space Matters
**Don't include:**
- Links to files (Claude can't click them; you're relying on filenames)
- Assumptions about what Claude knows (you've already uploaded the docs)
- "You are an AI language model..." preamble (assume Claude knows what it is)
- Detailed file descriptions (save that for CLAUDE.md)
- Instructions on how to use Claude (focus on project-specific behavior)

---

## Anti-Patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| "Answer all questions accurately" | Unmeasurable, vague | "Quote the prerequisites template before answering questions about structure" |
| "Be professional and clear" | Describe what that looks like? | "Use short sentences. No jargon. Show examples." |
| "Help with documentation tasks" | What tasks? How? | "When user asks for a doc, suggest the matching template + explain why it fits" |
| "Use best practices" | Whose practices? | "Reference the quality checklist for every doc review" |
| "Think step by step" | Already built into Claude | Focus on project-specific logic instead |
| Listing files | "This project has A, B, C files" | "Use file A to validate B" (instruction, not listing) |

---

## Generation Process

### Step 1: Define Role Clearly
Answer:
- What singular perspective does Claude have in this project?
- What does Claude produce / provide?
- What's the success metric?

### Step 2: Extract "How to Use Context"
From CLAUDE.md or project overview:
- What files are most important?
- Which docs are reference (truth source) vs. examples vs. tools?
- How should conflicting info be resolved?

### Step 3: Write Response Format
Complete this sentence:
- "When a user asks me something, I should respond by: [structure], in [tone], at [length]"

### Step 4: List Specific Do's & Don'ts
For each:
- Is it observable?
- Is it project-specific (not general Claude behavior)?
- Can someone verify compliance?

### Step 5: Add Examples
Show:
- What good looks like in this project
- What bad looks like (common mistake)
- Why the difference matters

### Step 6: Test with Reader Claude
New conversation, paste instructions + ask:
- "In this project, how should I respond to [realistic question]?"
- "What should I never do in this project?"

Fix any ambiguity Reader Claude surfaces.

---

## Template

```markdown
# [Project Name] — Custom Instructions

## Role
[1 sentence: what you are] [1 sentence: what you provide]

## How to Use Project Context
[2–3 sentences: how to read/reference uploaded docs. Which are authoritative? How should they inform responses?]

## Response Format
[2–3 rules about length, structure, tone, examples. Be specific.]

## Do's
- [Specific action #1]
- [Specific action #2]
- [Specific action #3]

## Don'ts
- [Never do X]
- [Never do Y]
- [Never do Z]

## Examples

GOOD:
[Example response that follows the rules]

BAD:
[Example that violates the rules]

Why: [Explanation of the difference]
```

---

## Version Stamp Requirement

Every generated project instructions file must include `Last updated: YYYY-MM-DD` in the header. Stale instructions cause agent failure. If the stamp is more than 30 days old, review before trusting.

Update instructions whenever: a builder is added/removed, a key file is renamed, a workflow changes, a rule is proved wrong in practice.

---

## Quality Checklist for Project Instructions

- [ ] Role statement is one sentence, specific, tied to project purpose
- [ ] Context interpretation tells Claude *how* to use docs, not just that they exist
- [ ] Response format rules are specific (length, structure, tone, when to ask vs. answer)
- [ ] Each do/don't is observable and project-specific
- [ ] Examples show good + bad with explanation
- [ ] No links to files (assume file names are known)
- [ ] No general Claude behavior rules (focus on project uniqueness)
- [ ] Total length 500–800 words
- [ ] Do's: 5 max, each observable and project-specific
- [ ] Don'ts: 5 max, each includes WHY, uses "Do not" not "NEVER"
- [ ] No vague words: "helpful," "professional," "thorough," "best practices," "comprehensive"
- [ ] Version stamp present: `Last updated: YYYY-MM-DD`
- [ ] Reader Claude test passed (fresh instance answers questions correctly)


========================================================================
SYSTEM Token Optimization
========================================================================

# Token Optimization: Quality Per Token

Docs must be high-quality AND efficient. This defines token budgets and optimization rules.

---

## Core Principle

**Quality per token** = quality_score ÷ token_count

A 100-point doc in 2K tokens is better than the same 100-point doc in 4K tokens.

**Target:** 0.03+ quality points per token (85 quality score ÷ 2500 tokens = 0.034)

---

## Token Budgets by Doc Type

All budgets are HARD LIMITS. Exceeding by >10% = Gate 4 FAIL.

**Source of truth:** `config/token_budgets.json` — always check that file for current budgets and rationale. Do not duplicate budget values here.

**Quick reference:** Budgets range from 1,200 tokens (project-instructions) to 3,500 tokens (architecture). The `note` field in each budget entry explains the rationale. When in doubt, open `config/token_budgets.json`.

---

## How to Stay Within Budget

### 1. Prerequisites: Max 800 tokens

```markdown
## Prerequisites

### Level 1: Tools & Software
- **Tool Name** (required)
  - Check: [command]
  - Install: [link]
  - Why: [one sentence]

### Level 2-4
[Continue as needed]

**Ready?** [verification command]
```

**Optimization:**
- Don't repeat install links (reference once, then "see link above")
- Combine similar items ("Node + npm" not "Node (600 tokens) then npm (400 tokens)")
- Level 3 (Knowledge) = one line each
- Level 4 (State) = one line each

**Token counts:**
- Simple setup: 150-250 tokens
- Medium setup: 300-500 tokens
- Complex setup: 600-800 tokens (near limit)

### 2. Steps: Max 50 tokens per step

Each step should be:
```markdown
### Step N: [Action]

1. Run: [command]
   Expected: [output]
   
   **AI metadata:** [2-3 lines max]
```

**Token estimate per step:**
- Simple (command + expected): 30-40 tokens
- Medium (command + expected + error reference): 40-60 tokens
- Complex (command + expected + metadata + reference): 60-80 tokens

**If step exceeds 80 tokens:** Split into two steps.

### 3. Troubleshooting: Max 60 tokens per error

```markdown
### Error: "[signature]"

**Root cause:** [one sentence]

**Fix:**
1. [Step 1]
2. [Step 2]
3. [Verify]

**AI metadata:** [one line max]
```

**Token estimate:**
- Simple error: 30-40 tokens
- Medium error: 40-60 tokens (limit)
- Complex error: 70-100 tokens (move to DEBT.md)

**Rules:**
- Max 5 errors per doc
- If more needed: Add to DEBT.md as "Add X, Y, Z error handling"

### 4. Content Sections: Max 4 paragraphs = ~400 tokens

Each section (Why This Matters, Overview subsection, etc.):
```markdown
## Section Title

[Paragraph 1: Main point - ~80 tokens]
[Paragraph 2: Detail/support - ~80 tokens]
[Paragraph 3: Application - ~80 tokens]
[Paragraph 4: Context - ~80 tokens MAX]
```

**If content exceeds 400 tokens:** Break into multiple sections or move to separate doc.

### 5. Examples: Max 30% of doc tokens

If doc is 2500 tokens:
- Code examples: max 750 tokens total
- Reference tables: max 500 tokens total
- Illustrations (described): max 300 tokens total

**Example optimization:**
```markdown
❌ BAD (500 tokens):
"Here's a complete example with full error handling,
logging, edge cases, authentication flow..."

✅ GOOD (150 tokens):
```bash
curl -X GET https://api.example.com/users
```

Response: `{"users": [...]}`

[Link to: Complete example with error handling in appendix]
```

---

## Token Optimization Checklist

Before Gate 4, run this:

### Prose Sections
- [ ] Overview: 2 sentences, no filler
- [ ] Why This Matters: 3-5 bullets, not paragraphs
- [ ] What's Next: 3 options max, 1-2 sentences each
- [ ] Sections: ≤ 4 paragraphs each
- [ ] Examples: Simplified, reference full example in doc

### Step-by-Step
- [ ] Prerequisites: 200-800 tokens (not 1500)
- [ ] Each step: 30-60 tokens (not 100+)
- [ ] Errors: 5 max, 60 tokens each (move rest to DEBT)
- [ ] Metadata blocks: 3-5 lines, not 10+

### Structure
- [ ] No redundancy (same info in two places = remove one)
- [ ] No theoretical explanation (link to why instead)
- [ ] No "nice to know" (move to DEBT.md as "P3: Add X")
- [ ] No generic disclaimers ("Please note...", "It's important...")

### Cuts to Make
- [ ] "For more information, see..." → Replace with specific link
- [ ] "There are many ways..." → Show the one best way
- [ ] "You might want to consider..." → "Do X because Y"
- [ ] Generic intro/conclusion → Remove entirely
- [ ] Duplicate concepts → Consolidate into one section

---

## Quality Score Calculation

**Quality Score = (factors) → 0-100**

```
Base score: 50

+ 10: Passes human quality checklist (all items true)
+ 10: Passes AI quality checklist (all items true)
+ 10: Passes token efficiency (within budget, no fluff)
+ 10: Clear expected output (testable, specific)
+ 10: All steps/errors have AI metadata
+ 5:  All cross-references use doc titles
+ 5:  All external links verified working
+ 5:  Error signatures verified exact
+ 5:  Related docs exist and relevant
+ 5:  No vague language detected

Minus points:
- 5: Each vague phrase ("proper", "configure", "ensure")
- 3: Each broken link
- 5: Each unclear error signature
- 10: Exceeds token budget
- 10: Missing critical section (Expected Output, etc.)

Final: (Base + additions - subtractions) / 100 = Quality Score
```

**Example:**
```
Setup guide:
Base:                        50
+ Human quality:             10
+ AI quality:                10
+ Token efficiency:          10
+ Clear expected output:     10
+ AI metadata blocks:        10
+ Doc title references:      5
+ Working links:             5
+ Verified error signatures: 5
+ Related docs exist:        5
+ No vague language:         5

Subtractions:
- 1 broken link:             -3
- 1 missing error signature: -5

Total: 117 / 100 = 1.00 = 100 (capped at 100)
Quality Score: 92 (after manual adjustments for edge cases)
```

---

## Token Budget Exceptions

**When can you exceed budget?**

Only if:
1. Quality score would drop below 80 if you cut more
2. Exceeding is < 10% over budget (2500 budget + 250 overage = OK)
3. Overage justified in DEBT.md under "Content Decisions"

**Example:**
```markdown
## DEBT.md - Content Decisions

### Budget Overage (Item P0)
- Token budget: 2500
- Actual: 2680
- Overage: 180 tokens (7%)
- Reason: 3 error signatures essential for user success (not optional)
- Future: Refactor examples to reduce by 150 tokens
```

**If exceeding > 10%:** NOT APPROVED. Cut content, move to DEBT.md, or split into two docs.

---

## Token Tracking Template

Every doc must include this in metadata.json:

```json
{
  "token_budget": 2500,
  "token_count": 2347,
  "token_ratio": 0.94,
  "budget_status": "PASS",
  
  "token_breakdown": {
    "frontmatter": 45,
    "overview_section": 120,
    "prerequisites": 420,
    "content_sections": 980,
    "steps": 420,
    "troubleshooting": 240,
    "ai_metadata_blocks": 60,
    "examples": 200,
    "other": 42
  },
  
  "optimization_notes": [
    "Removed 300-token theoretical explanation section",
    "Consolidated 3 similar prerequisites into 1",
    "Moved advanced examples to separate doc (DEBT.md item)"
  ],
  
  "quality_score": 92,
  "quality_calculation": {
    "base": 50,
    "human_checklist": 10,
    "ai_checklist": 10,
    "token_efficiency": 10,
    "expected_output": 10,
    "metadata_blocks": 10,
    "doc_title_refs": 5,
    "working_links": 5,
    "error_signatures": 5,
    "related_docs": 5,
    "no_vague_language": 5,
    "penalties": -8,
    "final": 92
  }
}
```

---

## Benchmarks: Quality Per Token

**Excellent (0.035+):**
- 87 quality score ÷ 2500 tokens = 0.0348 ✅

**Good (0.030-0.035):**
- 85 quality score ÷ 2800 tokens = 0.0304 ✅

**Acceptable (0.025-0.030):**
- 80 quality score ÷ 3200 tokens = 0.0250 ⚠️

**Poor (< 0.025):**
- 82 quality score ÷ 3500 tokens = 0.0234 ❌
- Action: Cut tokens or improve quality

---

## Monthly Token Audit

Every month, analyze:

```markdown
## Monthly Token Report

### Metrics
- Total docs generated: X
- Avg tokens per doc: Y
- Avg quality score: Z
- Quality/token ratio: Q/T

### Trends
- Docs exceeding budget: N (%) [target: < 5%]
- Quality scores below 85: N (%) [target: < 10%]
- Token bloat areas: [section types averaging above budget]
- Quality issues: [recurring Gate 3-4 failures]

### Adjustments for Next Month
- Reduce budget for [domain]? (avg: 3200, budget: 2500)
- Improve quality for [domain]? (avg score: 78)
- Split [doc_type] into two? (avg tokens: 4100)
```

This tracking prevents budget creep and quality drift.


========================================================================
SYSTEM User Journey
========================================================================

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


========================================================================
SYSTEM Version Control
========================================================================

# Version Control Strategy

How to version documents, manage updates, deprecate, and archive.

---

## Core Principle

**One version is current. All others are archival.**

A doc can have v1.0, v1.1, v2.0 but only ONE is "production" (users see it).

---

## Version Numbering

```
v1.0  = Initial release (production)
v1.1  = Patch update (bug fix, clarification) (production)
v1.2  = Patch update (production)
v2.0  = Major revision (new content, structure, approach) (production)
```

**When to increment:**

| Change | Version | Example |
|--------|---------|---------|
| Typo fix | Patch (v1.0 → v1.1) | "Fix: 'environemnt' → 'environment'" |
| Clarification | Patch (v1.0 → v1.1) | "Add example to Step 3 for clarity" |
| 1-2 new sections | Patch (v1.0 → v1.1) | "Add 2 troubleshooting errors" |
| Structural changes | Minor (v1.0 → v2.0) | "Reorganize prerequisites, add validation section" |
| New approach/context | Minor (v1.0 → v2.0) | "GTM Strategy completely rewritten for new market segment" |
| Content outdated (>1 year) | Deprecate v1.x, create v2.0 | Market shifted, new numbers, new approach |

---

## File Structure

```
output/{domain}/
├── v1.0/                    # Original release
│   ├── {DOC_NAME}.md        # Live version (what users see)
│   ├── {DOC_NAME}.DEBT.md   # Known limitations
│   └── metadata.json        # Generation metadata
│
├── v1.1/                    # Patch update
│   ├── {DOC_NAME}.md        # Updated version
│   ├── {DOC_NAME}.DEBT.md   # Remaining debt
│   └── metadata.json        # New generation metadata
│
├── v2.0/                    # Major revision
│   ├── {DOC_NAME}.md        # Rewritten version
│   ├── {DOC_NAME}.DEBT.md   # New debt list
│   └── metadata.json        # New metadata
│
└── archive/                 # Old versions (< 1 year old)
    ├── [DEPRECATED]_{DOC_NAME}_v1.0_2025.md
    └── [DEPRECATED]_{DOC_NAME}_v1.1_2025.md
```

**Rules:**
- Only ONE version folder is "current" (others are historical)
- `archive/` contains deprecated versions (marked with [DEPRECATED])
- Each version folder is self-contained (can access any version anytime)

---

## Status Field (In Frontmatter)

Every doc frontmatter includes:

```yaml
status: production|draft|review|deprecated
version: 1.0|1.1|2.0|etc
deprecated_date: YYYY-MM-DD (if deprecated)
```

### Status Definitions

**production:** Current, live version. Users see this.

**draft:** Being written, not complete. Not shipped.

**review:** Completed but awaiting approval. All gates passed, waiting final sign-off.

**deprecated:** Old version, no longer recommended. Archived but accessible.

---

## Deprecation Process

### Step 1: Create Newer Version

User creates v2.0 (major update) or v1.1 (patch).

```yaml
version: 2.0
status: production  # ← This becomes the new current
```

### Step 2: Mark Old Version Deprecated

Old v1.0 file renamed and moved:

```
Before: output/gtm/v1.0/GTM_Strategy_2026.md
After:  output/gtm/archive/[DEPRECATED]_GTM_Strategy_2026_v1.0_2025.md
```

Old v1.0 frontmatter updated:

```yaml
version: 1.0
status: deprecated
deprecated_date: 2026-04-02
replacement_version: 2.0
migration_guide: "See: GTM_Strategy_v2.0_Migration_Guide.md"
```

### Step 3: Create Migration Guide (If Major Change)

For v1.0 → v2.0, create optional migration doc:

```
SYSTEM_GTM_Strategy_v2.0_Migration_Guide.md

Contents:
- What changed in v2.0
- Why it changed
- How to migrate from v1.0 approach
- New features
- Removed features
```

### Step 4: Update Related Docs

If other docs reference deprecated v1.0:

```markdown
# Old doc reference
See: GTM_Strategy_2026_v1.0  ← Users might have bookmarks
```

Update to:

```markdown
# New doc reference (with deprecation notice)
See: GTM_Strategy_2026_v2.0 (v1.0 is deprecated)
```

### Step 5: Announce Deprecation

Add entry to DEPRECATION_LOG.md:

```markdown
## Deprecation Log

### GTM_Strategy_2026 (v1.0 → v2.0)
- **Deprecated:** 2026-04-02
- **Version:** v1.0
- **Reason:** New market segment requires different GTM approach
- **Replacement:** GTM_Strategy_2026_v2.0
- **Migration Guide:** See SYSTEM_GTM_Strategy_v2.0_Migration_Guide.md
- **EOL Date:** 2026-07-02 (3 months from deprecation)
- **Users affected:** Sales team, Product marketing
- **Archive location:** output/gtm/archive/[DEPRECATED]_GTM_Strategy_2026_v1.0_2025.md
```

---

## Version Lifespan

```
v1.0 Published        Today: 2026-04-02
    ↓
v1.1 Small update     2026-04-15 (13 days later, same version folder)
    ↓
v2.0 Major revision   2026-05-01 (new folder: v2.0/)
    ↓
v1.1 deprecated       2026-05-01 (marked deprecated, moved to archive/)
    ↓
v1.1 EOL              2026-08-01 (90 days after deprecation)
    ↓
v1.1 deleted          2026-08-01 (or kept in archive forever)
```

**Default lifespan:**
- v1.x: 6 months as current, then deprecated, then EOL at 9 months
- v2.x: Current until v3.0, then 6-month deprecation period

---

## What Users See

```
Current (Production):
✅ v2.0 ← Direct link in Projects
   "This is the current version"

Older (Archived):
📦 v1.1 ← Accessible but marked deprecated
   "This version is deprecated. See: v2.0"

   v1.0 ← Accessible but marked deprecated
   "This version is deprecated. See: v2.0"
```

---

## Update Types & Process

### Type 1: Patch Update (v1.0 → v1.1)

**When:** Typo, clarification, 1-2 new errors, example fix

**Process:**
1. Clone v1.0 folder to v1.1
2. Make edits in v1.1 files
3. Update version in frontmatter: `version: 1.1`
4. Update metadata.json (new date, unchanged doc_type)
5. Run Exit Gates 3-5 only (skip structure check, we know it's good)
6. Mark v1.0 as no-longer-current (optional, depends on storage)
7. Users see v1.1 in Projects

**Example:** Fix 3 broken links, clarify Step 2, add new troubleshooting error

### Type 2: Major Revision (v1.x → v2.0)

**When:** New approach, new structure, updated context, different audience

**Process:**
1. Create NEW doc: v2.0 (not edit v1.x)
2. Rewrite or significantly restructure
3. Use same doc_type, new version: `version: 2.0`
4. Run ALL Exit Gates (1-5)
5. Create DEBT.md for v2.0 (fresh list)
6. Create migration guide if major (optional)
7. Mark v1.x as `deprecated: true` in frontmatter
8. Move v1.x files to `archive/` folder
9. Rename: `{NAME}.md` → `[DEPRECATED]_{NAME}_v1.x_YYYY.md`
10. Update metadata.json with deprecation notice
11. Users see v2.0 in Projects, can access v1.x in archive

**Example:** GTM strategy changes for new market segment, new structure, new metrics

---

## In Claude Projects

### Current Version Only

Users see only ONE version in project knowledge base:

```
Projects/docgen/knowledge_base/
├── GTM_Strategy_2026_v2.0.md       ← CURRENT
├── DESIGN_Button_System_v1.0.md    ← CURRENT
├── BRANDING_Voice_Guidelines.md    ← CURRENT (no version)
└── [Archived docs not shown here]
```

Project instructions:

```markdown
## Document Versions

If you're looking for an older version of a doc:

1. **Check project knowledge base** (current versions only)
2. **For archived versions**, see output/archive/ in the docgen repo
3. **For migration guides**, see SYSTEM_Migration guides
```

### Update Process

When v1.0 → v2.0:

1. New v2.0 created and tested
2. v1.0 marked deprecated in docgen folder
3. Project knowledge base updated:
   - Remove v1.0 file
   - Add v2.0 file
   - Update related_docs references
4. v1.0 accessible via docgen repo archive for historical reference

---

## Deprecation Timeline

```
Month 1: v2.0 published, v1.0 deprecated
  - v1.0 marked [DEPRECATED] in archive
  - Users notified: "v2.0 available, see migration guide"
  - Both versions visible (v2.0 current)

Month 2-3: v1.0 in deprecation period
  - Active notification: "v1.0 deprecated, use v2.0"
  - Support: Questions about v1.0 → redirect to v2.0
  - v1.0 still accessible in archive

Month 4: v1.0 EOL
  - v1.0 removed from archive searches
  - Still accessible if linked directly
  - Support: v1.0 questions → "No longer supported"

Month 6-12: v1.0 in cold storage
  - Deleted from project access
  - Still in git history if needed
  - Special request only
```

---

## Version Tracking

Every doc has metadata.json tracking all versions:

```json
{
  "document": "GTM_Strategy_2026",
  "current_version": "2.0",
  "status": "production",
  
  "version_history": [
    {
      "version": "1.0",
      "released": "2026-01-15",
      "status": "deprecated",
      "reason": "New market segment GTM requires v2.0",
      "replacement": "2.0",
      "eol_date": "2026-08-15",
      "location": "output/gtm/archive/"
    },
    {
      "version": "1.1",
      "released": "2026-02-01",
      "status": "deprecated",
      "reason": "Superseded by v2.0",
      "replacement": "2.0",
      "eol_date": "2026-08-01",
      "location": "output/gtm/archive/"
    },
    {
      "version": "2.0",
      "released": "2026-05-01",
      "status": "production",
      "reason": "Current version",
      "replacement": null,
      "eol_date": null,
      "location": "output/gtm/v2.0/"
    }
  ]
}
```

---

## Automation: Version Management

Builder should support:

```
User actions:
1. "Update existing doc" → Increment version (1.0→1.1 or 1.x→2.0)
2. Select update type:
   - "Patch (typo/clarification)" → v1.1
   - "Minor (add sections)" → v1.2
   - "Major (new approach)" → v2.0
3. Clone current version
4. Edit in new version folder
5. Run appropriate exit gates
6. Deprecate old version (automated)
7. Update Projects knowledge base (automated)
8. Log in version history (automated)
```

---

## Version Cleanup

Every 6 months, audit versions:

```bash
#!/bin/bash
# Find deprecated docs >1 year old

find output/ -name "[DEPRECATED]*.md" -mtime +365 | while read file; do
  echo "Can delete (>1 year old): $file"
done
```

Decision: Keep in archive 1-2 years, then delete (keep in git history).

---

## Version Control Checklist

Before shipping v2.0:

- [ ] v1.x is marked `status: deprecated`
- [ ] v1.x moved to `archive/` folder
- [ ] v1.x renamed with [DEPRECATED] prefix
- [ ] v2.0 frontmatter: `version: 2.0`, `status: production`
- [ ] v2.0 metadata.json created
- [ ] Migration guide created (if major change)
- [ ] DEPRECATION_LOG.md updated
- [ ] Related docs updated to reference v2.0
- [ ] Projects knowledge base updated (v1.x removed, v2.0 added)
- [ ] Users notified if applicable (email, chat, etc.)
- [ ] v1.x EOL date set (6-12 months out)

---

## Real-World Example: GTM Strategy Versioning

```
Timeline:
Q1 2026: v1.0 published (mid-market focus)
↓
Q2 2026: v1.1 patch (add competitive analysis)
↓
Q3 2026: v2.0 major revision (enterprise focus, new market)
         v1.0 & v1.1 deprecated

Folder structure Q3:
output/gtm/
├── v1.0/
│   ├── GTM_Strategy_2026.md (OLD, don't use)
│   └── ...
├── v1.1/
│   ├── GTM_Strategy_2026.md (OLD, don't use)
│   └── ...
├── v2.0/
│   ├── GTM_Strategy_2026.md (CURRENT)
│   └── ...
├── archive/
│   ├── [DEPRECATED]_GTM_Strategy_2026_v1.0_Q1_2026.md
│   ├── [DEPRECATED]_GTM_Strategy_2026_v1.1_Q2_2026.md
│   └── SYSTEM_GTM_Strategy_v2.0_Migration_Guide.md
```

Users see: GTM_Strategy_2026_v2.0 (current)
Can access: Old versions in archive if needed
Know: v1.x is deprecated, should migrate


