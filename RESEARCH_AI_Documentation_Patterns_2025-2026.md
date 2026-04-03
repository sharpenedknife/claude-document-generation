# Research Findings: AI Documentation System Design Patterns
**Date:** April 3, 2026 | **Scope:** Topics 1-4 | **Sources:** 32+ authoritative references

---

## TOPIC 1: How People Build AI Agents Today

### Core Architectural Patterns

**Single vs. Multi-Agent Decision:**
- Start with **single-agent systems** unless you have clearly distinct tasks
- Single-agent: one LLM + defined tool set + system prompt = autonomous handler
- Multi-agent: specialized agents + orchestration + access controls (higher cost, higher risk)
- **Key principle:** "Find the simplest solution possible when building LLM applications, which might mean not building agentic systems at all" — Anthropic

**Essential Components (4-part framework):**
1. **LLMs** — the reasoning engine
2. **Contextual Memory** — persistence and state
3. **External Functions/Sub-agents** — tool integration
4. **Routing** — decision logic for tool selection

**Four Proven Multi-Agent Patterns:**

| Pattern | Use Case | Execution Model |
|---------|----------|-----------------|
| **Sequential Orchestration** | Step-by-step workflows with clear dependencies | Agent output → next agent input |
| **Multi-Agent Sequential** | Specialized agents in fixed order | Predefined logic (no AI orchestration) |
| **Supervisor Pattern** | Best starting point for multi-agent | LLM decides which agent to call |
| **Planning Agent** | Tasks requiring coordinated multi-step actions | Plan first, execute sequentially |

### Memory Architecture Patterns (2025)

**Three Memory Types:**
- **Factual Memory:** Fixed knowledge, domain data
- **Experiential Memory:** Past decisions and outcomes (Decision Trace Memory)
- **Working Memory:** Current conversation context

**Decision Trace Memory:**
Structured logs of every prompt, response, and decision create auditability and learning loops.

**Coordination Pattern for Multi-Agent:**
Topic subscription model — agents subscribe to topics (e.g., "global_plan", "state_update"), orchestrator broadcasts updates, workers refresh local view. This reduces stale-information risk.

### Planning vs. Reacting

**ReAct Framework (most widely adopted):**
- Iterative loop: Think → Act → Observe → Think
- Powerful synergy between cognition and action
- Best for exploratory tasks with uncertain paths

**Plan-and-Execute Approach:**
- Generate complete plan upfront
- Execute all tool calls at once
- Collect results, formulate response
- Better for well-defined workflows with known dependencies

### Common Failure Modes

- **Autonomy-oversight tension:** Agents must work autonomously BUT humans retain control over goals (especially before high-stakes decisions)
- **Compounding errors:** Small mistakes in early steps propagate
- **Tool misuse:** Agents calling wrong tools or with wrong parameters
- **Memory drift:** Stale information causes incorrect decisions

### Best Practices Summary

✓ Self-improving agents (check output, self-correct) are fundamentally more reliable
✓ Start simple, add multi-step agentic complexity only when simpler solutions fail
✓ Extensive testing in sandboxed environments before production
✓ Modular design + observability (not an afterthought) + feedback loops
✓ Use frameworks for speed, but reduce abstraction layers for production

**Sources:**
- [Building Effective AI Agents — Anthropic](https://www.anthropic.com/research/building-effective-agents)
- [AI Agent Orchestration Patterns — Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- [Agentic AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Memory in the Age of AI Agents — arXiv](https://arxiv.org/abs/2512.13564)

---

## TOPIC 2: How to Build MCP Servers

### Language Choice: TypeScript vs Python (Equivalence Model)

**Official guidance:** "Both paths produce equivalent results, so pick whichever language you are more comfortable writing in."

**TypeScript:**
- Strengths: static typing, superior IntelliSense, unified Node/React stack
- Schema validation: Zod with explicit `.describe()` calls
- Best for: web-centric projects, teams already on Node

**Python:**
- Strengths: fast iteration, cleaner syntax for simple servers
- Schema validation: type hints + docstring inference (FastMCP)
- FastMCP auto-generates schemas from annotations and docstring Args: section
- Best for: data scripts, quick prototypes, teams already on Python

**Folder Structure Standard:**

TypeScript:
```
my-mcp-server/
├── src/
│   └── server.ts
├── dist/              (compiled output)
├── package.json
├── tsconfig.json      (outDir: dist, rootDir: src)
├── .gitignore
└── README.md
```

Python:
```
my-mcp-server/
├── server.py
├── pyproject.toml
├── .venv/
└── README.md
```

### Core Primitives (3-part model)

| Primitive | Control | Use |
|-----------|---------|-----|
| **Tools** | Model-controlled | Functions the AI can call |
| **Resources** | Application-controlled | Data the AI can read |
| **Prompts** | User-controlled | Reusable prompt templates |

### Key Implementation Rules

**Tool Design:**
- Each tool performs **single operation** with clearly defined inputs/outputs
- May require user consent before execution (maintains user control)
- Tools are model-directed, not orchestrated by the app

**Logging Best Practices:**
- **STDIO servers:** Never write to stdout (corrupts JSON-RPC messages). Use stderr or files.
- **HTTP servers:** stdout is safe (doesn't interfere with HTTP responses), but use logging libraries to stderr/files.

**Server Instructions:**
"Server instructions give the server a way to inject information that the LLM should always read in order to understand how to use the server — independent of individual prompts, tools, or messages."

⚠️ **Critical:** "No instructions are better than poorly written instructions." Evaluate client behavior with your server before relying on server instructions.

**Security & Authorization:**
- Do NOT implement token validation yourself
- Use off-the-shelf, well-tested libraries (OAuth, JWT validators)
- Use short-lived tokens (reduces attack surface if stolen)
- Avoid long-lived tokens

### Recommended Implementation Path

1. **Define your three primitives** — What tools? What resources? What prompts?
2. **Choose language** — TypeScript for web, Python for scripts
3. **Set up folder structure** — Follow standard above
4. **Implement transport** — STDIO (simple) or HTTP (remote)
5. **Write server instructions** — Concise, tested user manual for the server
6. **Test with clients** — Validate behavior before production

**Sources:**
- [Build an MCP Server — Model Context Protocol](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
- [Server Instructions: Giving LLMs a user manual](http://blog.modelcontextprotocol.io/posts/2025-11-03-using-server-instructions/)
- [MCP SDK Comparison: Python vs TypeScript](https://www.stainless.com/mcp/mcp-sdk-comparison-python-vs-typescript-vs-go-implementations)

---

## TOPIC 3: AI Documentation / Writing Docs for AI to Consume

### Fundamental Difference from Human Docs

**Human documentation:** sequential reading, navigation context, can infer relationships
**AI documentation:** stateless (each page/section isolated), must be self-contained, needs explicit structure

"LLM-powered assistants often process individual pages or sections without the broader navigation context. Each page must stand on its own."

### Three-Part Documentation Stack

**1. llms.txt (the sitemap)**
- Machine-readable registry of all documentation
- Markdown file listing links to raw markdown files
- Easier for LLMs to discover and parse
- Current adoption: 844,000+ websites (Anthropic, Stripe, Cloudflare)
- Format: brief background + links to detailed markdown files

**2. CLAUDE.md (agent instructions)**
- Project instructions file in repository root
- Claude Code reads this at session start
- Persistent context that doesn't clutter conversation history
- Focus: build commands, architecture, code style, gotchas

**3. AI-specific sections in code/docs**
- Complete, runnable code examples (imports + config + file paths)
- Partial snippets force LLMs to assume/hallucinate
- Error examples showing what NOT to do
- Cross-references with explicit links

### Content Structure Rules

**Each page must include:**
- Clear purpose statement (what problem does this solve?)
- Prerequisites/dependencies upfront
- Complete, copy-paste-able code examples
- Common mistakes and how to avoid them
- Links to related pages (not relying on nav context)

**Avoid:**
- Vague language ("sometimes", "might", "usually")
- Incomplete code examples
- Narrative prose without structure
- Navigation-dependent context

### Practical Implementation Rules

✓ Start with `.ai/guidelines.md` for core coding standards
✓ Document top 10 most-used tools comprehensively
✓ Set up llms.txt pointing to raw markdown files
✓ Expose an MCP server for documentation search/fetch
✓ Keep focused, relevant information (insufficient context causes hallucination)
✓ Use clear markdown structure (headings, code blocks, lists)

### What Works vs. What Fails

| Works | Fails |
|-------|-------|
| Complete runnable examples | Partial snippets |
| Explicit step-by-step procedures | Narrative explanation |
| Structured data (tables, lists, code) | Free-form prose |
| Page self-containment | Navigation-dependent context |
| Recent, version-specific docs | Generic, undated guidance |

**Sources:**
- [Why Your AI Agents Need Contextual Documentation](https://hyperdev.matsuoka.com/p/why-your-ai-agents-need-contextual)
- [Optimizing docs for AI agents — Biel.ai](https://biel.ai/blog/optimizing-docs-for-ai-agents-complete-guide)
- [How to expose any documentation to any LLM agent](https://ericmjl.github.io/blog/2025/10/19/how-to-expose-any-documentation-to-any-llm-agent/)
- [llms.txt standard](https://llmstxt.org/)
- [Writing effective tools for AI agents — Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents)

---

## TOPIC 4: Vibe Coding Rules / CLAUDE.md / Cursor Rules Patterns

### The Three Formats (2026 Landscape)

| Format | Tool | Use | Scope | Priority |
|--------|------|-----|-------|----------|
| **.cursorrules** | Cursor | IDE-tight editing workflows | File/directory | Fast iteration |
| **CLAUDE.md** | Claude Code | Deep context, repo reasoning | Session-level | Planning, architecture |
| **AGENTS.md** | Multi-agent (Sourcegraph standard) | Universal agent rules | Cross-tool | Future standard |

**How they layer:**
1. Workspace rules (universal preferences, coding standards)
2. Project rules (build commands, architecture, tech stack specific)
3. Directory rules (scope to specific subdirs)
4. Session context (Claude reads CLAUDE.md at start, always available)

### CLAUDE.md: The Standard Format

**Filename:** Exactly `CLAUDE.md` (case-sensitive)
**Location:** Repository root (shareable), parent directory (monorepo), or home folder (universal)

**WHY/WHAT/HOW Structure:**

```markdown
# [Project Name]

## What This Is
One-liner: what is this project—a brief orientation for new team members.

## Code Style
- TypeScript strict mode, no `any` types
- Named exports only
- Functional patterns preferred over class-based
- Early returns for error handling (avoid nesting)

## Commands
- `npm run dev` — start dev server
- `npm run test` — unit tests
- `npm run test:e2e` — end-to-end tests
- `npm run build` — production build

## Architecture
- `/app` — application shell
- `/components/ui` — reusable UI components
- `/lib` — utilities and helpers
- `/prisma` — database schema

## Important Notes (Gotchas)
- Never commit .env files
- Stripe webhook validation required on production
- Database migrations must be reversible
- All API responses must include error handling
```

**Length:** <300 lines is standard (shorter is better)
**Tone:** Brief, imperative, actionable

### .cursorrules: The IDE Pattern

**Filename:** `.cursorrules` (at project root)
**When to use:** Specific Cursor IDE workflows, deterministic output in editing tasks

**Best structure:**
- Group rules by category (Code Style, Testing, Architecture, etc.)
- Use markdown headings for navigation
- Include real-world examples (full task implementations)
- Focus on patterns you see Cursor misunderstanding repeatedly

**Key principle:** "Start simple, add rules only when you notice the agent making the same mistake repeatedly"

### Effective System Prompt Composition (2025 Research)

**The "Curse of Instructions":**
As you pile on more instructions, the model's performance in adhering to each one drops significantly — even GPT-4 and Claude struggle with many simultaneous requirements.

**Counter-strategy:**
- Prioritize the 5-7 most important rules
- Use structured format (headings, sections, code examples)
- Remove rules that are working (they're redundant)
- Update the file as you learn (it's a living document, not static)

### Agent-Specific Best Practices

**For Agent Mode (reasoning + tool use):**
- Specific instructions > vague guidance
- ✓ "Write a test case for auth.ts covering the logout edge case, using patterns in __tests__/ and avoiding mocks"
- ✗ "Add tests for auth.ts"

**What agents need to succeed:**
- Typed languages (catch errors early)
- Configured linters (clear signal of what's wrong)
- Tests (executable ground truth)
- Clear error signals (agents can't fix what they don't know about)

**Command Pattern (Repeatable Workflows):**
```
/test-focused — write tests for the last change
/refactor — extract common patterns
/docs — generate API documentation
```
Add commands AFTER figuring out workflows you actually repeat.

### Practical Checklist for Setup

✓ Create CLAUDE.md with 5 core sections (What, Code Style, Commands, Architecture, Gotchas)
✓ Keep < 300 lines
✓ Include real command invocations
✓ Document code style with code examples, not descriptions
✓ Use `/init` command in Claude Code to generate starter CLAUDE.md
✓ Create .cursorrules if you use Cursor IDE
✓ Group rules by category with markdown headings
✓ Update rules as you learn what actually helps
✓ Don't add rules for things that are working

### Examples from Production

**FastAPI Backend Pattern:**
```
- Python 3.11+ features
- Type hints everywhere
- Pydantic v2 for validation
- PEP 8 guidelines
- RESTful conventions
- SQLAlchemy 2.0 with async
```

**Key difference between contexts:**
- Cursor rules are tight/local (file/directory scope)
- CLAUDE.md is deep (repo-level reasoning, planning, architecture)
- AGENTS.md will be the unified standard (coming 2026)

**Sources:**
- [Best practices for coding with agents — Cursor](https://cursor.com/blog/agent-best-practices)
- [Rules | Cursor Docs](https://cursor.com/docs/context/rules)
- [How to write a good CLAUDE.md — Builder.io](https://www.builder.io/blog/claude-md-guide)
- [My Vibe Coding Setup — Medium](https://medium.com/@chace.medeiros/my-vibe-coding-setup-using-cursor-claude-to-manage-8-projects-7dd9a1216597)
- [How to write a good spec for AI agents — Addy Osmani](https://addyosmani.com/blog/good-spec/)
- [Comparing MCP Server Frameworks — Medium](https://medium.com/@divyanshbhatiajm19/comparing-mcp-server-frameworks-which-one-should-you-choose-cbadab4ddc80)

---

## Cross-Topic Synthesis: Key Patterns for Documentation Systems

### Pattern 1: Self-Containment
Whether MCP, docs, or agent instructions, each unit must stand alone. No hidden dependencies on external context.

### Pattern 2: Explicit Structure
AI parsing succeeds with markdown headings, code blocks, tables, and lists. Narrative prose requires more reasoning.

### Pattern 3: Example-Driven
Complete, runnable code beats description. Real examples beat abstract guidance.

### Pattern 4: Layered Context
Workspace rules (universal) → Project rules (tech-specific) → Directory rules (scope-specific) → Session context (active memory)

### Pattern 4: Versioning & Drift Prevention
SPEC.md, CLAUDE.md, and .cursorrules are living documents. Update them as you discover new information. Stale rules cause agent failure.

### Pattern 5: Memory Architecture
Decision traces (what was tried, why, what worked) matter more than implicit knowledge. Explicit logging > emergent understanding.

---

## Recommendations for Your Documentation System

### Immediate (Incorporate into CLAUDE.md template)
1. **Memory/context model:** Define Decision Trace Memory as required pattern
2. **MCP server rules:** Standardize tool definition, resource control, prompt patterns
3. **Documentation format:** Define llms.txt structure + AI-readable guidelines
4. **CLAUDE.md sections:** Codify WHY/WHAT/HOW + core sections list

### Short-term (Enhance builders)
1. Create MCP builder that outputs both TypeScript + Python templates
2. Add "write docs for AI" builder (distinct from code docs)
3. Create CLAUDE.md generator (analyze codebase, suggest structure)
4. Add "spec for agents" builder (6 core areas: Commands, Testing, Structure, Style, Git, Boundaries)

### Long-term (Ecosystem)
1. Track adoption of AGENTS.md standard (Sourcegraph + OpenAI + Google)
2. Monitor cursor.ai, claude.ai, windsurf for ruling/instruction patterns
3. Build ecosystem guide (how projects choose: single-agent vs multi-agent vs workflow)
4. Create fallback patterns for agents (what to do when tools fail, memory limits hit, etc.)

