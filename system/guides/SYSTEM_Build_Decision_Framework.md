# Build Decision Framework: Projects vs Skills vs MCPs vs Products
**Version:** 1.1 · April 2026
**Purpose:** Determine what to build before generating any documentation.

---

## The Core Question

When a user asks for help building something with Claude/AI, the first decision is: **what type of artifact is being built?** Get this wrong and every doc generated will be structurally incorrect. Get it right and the builder, templates, and output format all lock in automatically.

---

## Disambiguation Script (use when Q0 response is ambiguous)

If the user's Q0 answer could match more than one build type, ask:

> "Quick check — are you building:
>    **A)** Software that runs for your users (app, SaaS, tool) → code docs + dev plan
>    **B)** A Claude assistant for yourself or your team → project instructions + knowledge base
>    **C)** A reusable workflow or slash command → SKILL.md + evals
>    **D)** A connection to an external tool or API → MCP server docs
>
> Which one fits?"

Then route to the correct builder based on the answer. No answer = re-ask Q0 more specifically. Do not guess the build type.

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
