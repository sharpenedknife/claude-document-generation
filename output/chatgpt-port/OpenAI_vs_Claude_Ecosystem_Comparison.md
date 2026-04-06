# OpenAI vs Claude Ecosystem Comparison
## Documentation Generation System Equivalency Analysis

**Date:** April 2026
**Purpose:** Identify OpenAI/ChatGPT ecosystem equivalents for building a Documentation Generation System equivalent to the Claude version.

---

## Executive Summary

The Claude and OpenAI ecosystems have **functional equivalents for most components**, but with significant architectural and behavioral differences:

- **Claude Projects** ≈ **ChatGPT Projects** (both support knowledge bases, but Claude's context window is larger)
- **Claude Project Instructions** ≈ **GPT Custom Instructions + AGENTS.md in Codex**
- **Claude Skills** ≈ **Codex Skills** (directory-based, SKILL.md format, similar autodiscovery)
- **MCP Servers** ≈ **OpenAI Actions + MCP Support in Codex** (both now converging)
- **Cowork Mode** ≈ **Codex CLI/App** (local filesystem access, bash execution)
- **CLAUDE.md** ≈ **AGENTS.md in Codex** (project-level instructions)

**Key Difference:** Claude is a conversational system focused on iterative refinement within Projects. Codex is an **agentic, multi-step engineering automation tool** optimized for task execution in isolated worktrees.

---

## Component-by-Component Analysis

### A) Claude Projects vs ChatGPT Projects

#### Claude Version
- **What it does:** Persistent workspace that bundles conversations, uploaded knowledge base files, and custom project instructions (system prompt).
- **Knowledge base:** Upload files directly to project; Claude reads them via RAG to inform responses.
- **Scope:** Limited to conversations within that project; context persists across chat threads.
- **Context window:** Up to 200K tokens (Claude 3.5 Sonnet)

#### ChatGPT Equivalent
- **ChatGPT Projects** (released 2024-2026) provide similar functionality:
  - Group chats, reference files, and custom project instructions in one workspace
  - Upload up to 20 files per project (512 MB each)
  - Sources can come from apps (Slack, Google Drive), chat history, or ad-hoc text
  - Available on all plans (free through Enterprise)

- **Key limitation:** ChatGPT's context window is smaller; Projects do not extend it

#### Key Differences
| Aspect | Claude | ChatGPT |
|--------|--------|---------|
| **Context window** | 200K tokens | ~128K tokens |
| **File limit** | Depends on plan, typically higher | 20 files, 512 MB each |
| **Knowledge retrieval** | Better for long documents | Fast, good for web/integrated sources |
| **Cost** | Pro/Max tiers only | Available on Plus ($20/mo) |
| **Sharing** | With teammates (Pro/Max) | Teams can share (Business+) |

#### Porting Notes
- ChatGPT Projects are **sufficient** for a Documentation Generation System equivalent
- You may need to split large knowledge bases into multiple projects (20-file limit)
- Use **ChatGPT Plus tier minimum** for consistency with Claude Pro
- Custom instructions in ChatGPT Projects serve the same role as Claude project instructions

---

### B) Project Instructions (Claude) vs Custom Instructions (ChatGPT) vs AGENTS.md (Codex)

#### Claude Version
- **What it does:** System prompt set at the project level; Claude reads this file (CLAUDE.md) automatically and follows its rules.
- **Format:** Markdown file with clear sections (goals, rules, file map, quality gates, etc.)
- **Scope:** Applied to all conversations in that project
- **Function:** Acts as an operating manual for the AI's behavior within that project

#### ChatGPT Equivalent (UI)
- **Custom Instructions** (settable in project settings):
  - User-friendly form fields: "What would you like ChatGPT to know about you?" + "How would you like ChatGPT to respond?"
  - Applied to all conversations in that project
  - NOT automatically discovered from repo files (no equivalent to CLAUDE.md auto-detection)

#### Codex Equivalent (CLI/Agent)
- **AGENTS.md or AGENTS.override.md** in repository:
  - Placed at project root or nested in directories
  - Codex automatically discovers via directory walk: `~/.codex/AGENTS.md` (global) → project root → current working directory
  - Max 32 KiB per scope (global + project)
  - Stops at first non-empty file or when size limit reached
  - Function: instructs Codex how to navigate codebase, what tests to run, coding standards

#### Key Differences
| Aspect | Claude (CLAUDE.md) | ChatGPT (Custom Instructions) | Codex (AGENTS.md) |
|--------|-------------------|-------------------------------|-------------------|
| **Auto-discovery** | Yes (read from project folder) | No (manual configuration) | Yes (directory walk) |
| **Format** | Markdown (human-readable) | Form fields (semi-structured) | Markdown (plain text) |
| **Scope** | Project-level | Project-level | Global + Project (cascading) |
| **Size limit** | None documented | ~2000 chars per field | 32 KiB combined |
| **Updating** | Edit file, changes apply immediately | Edit in UI, changes apply to new chats | Edit file, Codex re-reads on next task |

#### Porting Notes
- **For ChatGPT Projects:** Manually paste CLAUDE.md content into Custom Instructions form
  - Split into two fields: "About you" (goals/rules) and "How to respond" (format/output standards)
- **For Codex:** Place AGENTS.md at repository root; structure it identically to CLAUDE.md
- **Key issue:** ChatGPT has no auto-discovery; you must manually copy instructions into each project
- **Recommendation:** Build a helper that converts CLAUDE.md → ChatGPT Custom Instructions format + Codex AGENTS.md

---

### C) GPTs (Custom GPTs) vs Claude Projects

#### GPT Version
- **What it does:** Customizable GPT-4o variant with bundled knowledge, instructions, and actions
- **Knowledge base:** Upload files as "knowledge" (RAG); GPT searches these when answering
- **Instructions:** Write custom system instructions that define behavior
- **Actions:** Connect to external APIs via OpenAPI schemas
- **Conversation starters:** Define 4 suggested prompts to kick off conversations
- **Scope:** Can be published publicly or shared with teams

#### Claude Projects Version
- **What it does:** Private workspace bundling conversations, knowledge files, project instructions
- **Knowledge:** Upload files; Claude references them
- **Instructions:** Project instructions (system prompt) define behavior
- **Tools:** Can call MCP servers for live external API access
- **Conversation starters:** Built-in feature in Claude Projects
- **Scope:** Private to workspace; can share with teammates (Pro/Max)

#### Key Differences
| Aspect | GPTs | Claude Projects |
|--------|------|-----------------|
| **Distribution** | Can be public or private | Always private/team |
| **Customization level** | Deep (instructions + actions) | Deep (instructions + MCP) |
| **Knowledge file limit** | 20 files, 512 MB each | Depends on tier (higher limits) |
| **Conversation starters** | Yes (4 suggested prompts) | Yes, built-in |
| **Tool integration** | OpenAPI actions | MCP servers |
| **Use case** | Publish specialized GPT versions | Internal team tool |

#### Porting Notes
- **GPTs are NOT a replacement for Claude Projects** in this system
- GPTs are better for **publishing a finished Documentation Builder tool** to others
- For **building the system itself**, use ChatGPT Projects + Codex
- If you want to publish a "Documentation Builder GPT": upload system/templates as knowledge, write instructions, deploy as public GPT

---

### D) OpenAI Actions (OpenAPI) vs MCP Servers

#### OpenAI Actions Version
- **What it does:** Connect GPTs/Codex to external APIs via OpenAPI schemas
- **Protocol:** REST over HTTPS (GET, POST, PUT, DELETE, PATCH)
- **Authentication:** OAuth 2.0 built-in, automatic token refresh
- **Tool discovery:** Static at configuration time (no runtime discovery)
- **Scope:** Server-side infrastructure maintained by OpenAI

#### MCP Servers Version
- **What it does:** Open protocol for AI applications to interact with external tools and data
- **Protocol:** JSON-RPC over stdio, WebSocket, or HTTP
- **Authentication:** Vendor-agnostic (OAuth, API keys, local auth patterns)
- **Tool discovery:** Dynamic at runtime (server announces available tools)
- **Scope:** Runs locally or as a standalone service; works with Claude, Cursor, Codex, others

#### Key Differences
| Aspect | OpenAI Actions | MCP Servers |
|--------|----------------|------------|
| **Protocol** | REST/OpenAPI | JSON-RPC (stdio/WebSocket/HTTP) |
| **Configuration** | Fixed at setup time | Dynamic discovery at runtime |
| **Vendor lock-in** | OpenAI only | Multi-vendor (Claude, Codex, others) |
| **Local access** | No | Yes (stdio mode for local files/DB) |
| **Auth patterns** | OAuth 2.0 | Flexible (OAuth, keys, local) |
| **Use case** | External SaaS APIs | Everything (APIs, databases, local tools) |

#### Porting Notes
- **Both are now converging:** Codex added native MCP support in March 2026
- **For Documentation Builder:** MCP is the better choice (future-proof, multi-vendor)
  - Define MCP servers for: Git operations, file I/O, AWS/cloud services
  - Both Claude and Codex can use the same MCP servers
- **If you need Codex only:** OpenAI Actions work, but MCP is recommended
- **Recommendation:** Build MCP servers for tool integration; they work everywhere

---

### E) Codex: What It Is Today (2026)

#### Current State
**Codex is an agentic engineering automation tool, not a standalone model or coding IDE.**

- **Core function:** Multi-agent orchestrator powered by GPT-5.4 (main) and GPT-5.4-mini (subagents)
- **Deployment:** Desktop app, CLI, GitHub integration, IDE plugins, web interface
- **Workspace:** Isolated worktrees (not your local git state)
- **Task execution:** Agents run in parallel across projects; tasks take 1-30 minutes typically

#### Key Capabilities (March 2026)
1. **Code generation & PR authoring:** Write features, fix bugs, propose pull requests
2. **Multi-agent orchestration:** Run parallel agents in isolated worktrees; inspect diffs before merging
3. **Skills-based workflows:** Codex Skills (SKILL.md) define repeatable tasks; agents follow them
4. **Tool integration:**
   - MCP servers (new in March 2026)
   - OpenAI Actions (REST APIs)
   - Plugins (Sentry, Datadog, GitHub native)
   - Triggers (auto-respond to GitHub events)
5. **Security review:** Codex Security in research preview for context-aware app security
6. **Custom instructions:** AGENTS.md in repository for codex-specific guidance

#### Codex vs o3/o4-mini vs Claude
- **o3/o4-mini:** Reasoning models; Codex uses them internally but is **not** these models
- **Codex:** Orchestrator layer on top of reasoning models + engineering tools
- **Claude:** Conversational LLM; Cowork mode adds file/bash access

#### How It Compares to Claude Code / Cowork Mode
| Aspect | Codex | Claude Cowork |
|--------|-------|---------------|
| **Focus** | Multi-agent automation, PR-ready code | Interactive assistant with file/bash access |
| **Execution** | Long-running tasks (1-30 min), isolated worktrees | Interactive steps, user-driven |
| **Primary output** | Pull requests, diffs, engineering artifacts | Conversation + edited files |
| **Git integration** | Deep (GitHub native, branch management) | Basic (read/write files) |
| **Model** | Codex-optimized GPT-5.4 | Claude 3.5 Sonnet |
| **Skill integration** | Codex Skills in ~/.codex/skills/ | Claude Skills (marketplace) |

#### Porting Notes
- **Codex is NOT a direct Cowork replacement**
- Codex excels at: "build this 10-file feature" → automated PR ready to merge
- Cowork excels at: iterative, conversational development with human in the loop
- **For Documentation Builder:**
  - Use Codex if you want **fully automated doc generation** (set up agents, they run, you review PR)
  - Use Claude Cowork if you want **conversational generation with refinement steps**

---

### F) Skill Equivalent in ChatGPT / Codex

#### Claude Skill Version
- **What it does:** Installed workflow playbooks (SKILL.md files) that Claude reads and follows
- **Format:** Directory containing:
  - `SKILL.md` (YAML frontmatter + markdown body describing the workflow)
  - Optional: `scripts/`, `references/`, `assets/` subdirectories
- **Autodiscovery:** Skills in `~/.claude/skills/` are automatically read by Claude
- **Invocation:** Via name/description; callable through Skill tool in Cowork mode

#### Codex Equivalent
- **Codex Skills:** Nearly identical to Claude Skills
  - Directory-based with SKILL.md (YAML frontmatter + body)
  - Autodiscovery from `~/.codex/skills/`
  - Agents read SKILL.md when working on tasks
  - Can invoke via `use-skill` command in Codex CLI

#### ChatGPT Equivalent (Partial)
- **No direct equivalent** in ChatGPT Projects or GPTs
- **Closest approach:** Write instructions inline in Custom Instructions, then reference them in conversation
- **Workaround:** Create GPT Actions that emulate skill behavior (call external APIs that mimic skill workflows)

#### Comparison Table
| Aspect | Claude Skills | Codex Skills | ChatGPT Workaround |
|--------|---------------|--------------|-------------------|
| **Format** | SKILL.md (directory) | SKILL.md (directory) | Inline instructions + GPT Actions |
| **Autodiscovery** | Yes (~/.claude/skills) | Yes (~/.codex/skills) | No (manual setup) |
| **Persistence** | Session-based | Task-based | Per-GPT configuration |
| **Tool access** | Skill tool in Cowork | use-skill in CLI | None (invoke via action) |
| **Reusability** | Across projects | Across Codex tasks | Only within that GPT |

#### Porting Notes
- **For Codex:** Directly copy Claude SKILL.md files to ~/.codex/skills/; minimal changes needed
  - Update tool references: `TodoWrite` → `update_plan`, `Skill` tool → `use-skill` command
- **For ChatGPT Projects:** Skills cannot be directly ported
  - Recommendation: Write skills as GPT Actions (call APIs that implement the workflow)
  - Or: Paste skill SKILL.md body into Custom Instructions as documentation

---

### G) File & Knowledge Base Management

#### Claude Projects
- **Upload mechanism:** Drag-and-drop or form upload in UI
- **Retrieval:** Automatic RAG; Claude searches files when relevant
- **Limits:** Plan-dependent (Pro/Max tiers allow more files)
- **File types:** PDFs, docs, spreadsheets, images, code, text
- **Visibility:** Files stay within project; not accessible outside

#### ChatGPT Projects
- **Upload mechanism:** Drag-and-drop in UI or link to apps (Slack, Google Drive)
- **Retrieval:** Automatic RAG; similar to Claude
- **Limits:** 20 files per project, 512 MB each
- **File types:** Similar to Claude (docs, spreadsheets, images, code, text)
- **Visibility:** Files within project; can share project with teams

#### Codex
- **Upload mechanism:** Repository files + AGENTS.md configuration
- **Retrieval:** Agents read files from worktree during task execution
- **Limits:** No hard file limit (entire repo is accessible)
- **File types:** Any (code, docs, configs, binaries)
- **Visibility:** Isolated to worktree; no persistent knowledge base

#### Key Differences
| Aspect | Claude | ChatGPT | Codex |
|--------|--------|---------|-------|
| **Knowledge persistence** | Yes (stays in project) | Yes (stays in project) | No (fresh worktree per task) |
| **Retrieval mechanism** | RAG at chat time | RAG at chat time | File system access at task time |
| **File limit** | Higher (plan-dependent) | 20 files, 512 MB | Unlimited (entire repo) |
| **Best for** | Reference docs, long-form content | Integrated web sources, external apps | Codebase context, full source access |

#### Porting Notes
- **For Documentation Builder system itself:**
  - Store system/templates, builders/, config/ as **project knowledge** in ChatGPT Projects
  - This replicates how Claude reads the folder
- **For Codex:** No knowledge base concept; agents read files directly from repo
  - Place all system files in repository root and AGENTS.md configuration
- **For ChatGPT Projects:** Upload system/guides, system/templates as files (may exceed 20-file limit; split into multiple projects)

---

### H) Auto-Discovery of Project Instructions (CLAUDE.md Equivalent)

#### Claude Version
- **Mechanism:** Claude automatically reads `CLAUDE.md` from the project folder
- **Behavior:** Loads on every conversation; acts as operating manual
- **No setup needed:** Drop file in project, Claude finds it automatically

#### ChatGPT Equivalent
- **No auto-discovery:** Must manually paste into Custom Instructions form
- **Workaround:**
  1. Create CLAUDE.md in repository
  2. Use a script to copy content → ChatGPT Custom Instructions via API or manual paste
  3. Or: Store CLAUDE.md in knowledge base and ask ChatGPT to read it first in conversation

#### Codex Equivalent
- **Mechanism:** Codex automatically discovers AGENTS.md (or AGENTS.override.md)
- **Directory walk:** Starts at `~/.codex/AGENTS.md` (global), then project root, then current directory
- **Behavior:** Loads before task execution; guides agent behavior
- **Size limit:** 32 KiB combined (global + project)

#### Comparison Table
| Aspect | Claude (CLAUDE.md) | ChatGPT | Codex (AGENTS.md) |
|--------|-------------------|---------|-------------------|
| **Auto-discovery** | Yes (automatic read) | No | Yes (directory walk) |
| **Manual setup** | None | Required (copy to form) | None |
| **Hierarchy** | Single file | Single form | Global + project cascade |
| **Size limit** | None documented | ~2000 chars per field | 32 KiB |
| **Frequency** | Every chat | Every new chat | Every task |

#### Porting Notes
- **For ChatGPT Projects:** Implement a helper script that:
  1. Reads CLAUDE.md
  2. Splits into "About you" and "How to respond" sections
  3. Stores in ChatGPT project config (via UI or API)
- **For Codex:** Create AGENTS.md at repo root (same content as CLAUDE.md, just renamed)
- **Best practice:** Maintain both CLAUDE.md + AGENTS.md in repo; have separate tools to sync them to ChatGPT Projects

---

### I) Instruction Following & Format Compliance

#### Claude's Strengths
- **Structured step-by-step execution:** Follows multi-step instructions reliably
- **Format precision:** Excellent at honoring output format requirements
- **Long-document analysis:** Can process and synthesize 200K token documents
- **Instruction depth:** Handles complex, nested instructions without drift

#### GPT-4o's Strengths
- **Format-exactness edge:** Slightly better at rigid "only X" constraints
- **Flexibility & improvisation:** More creative, less literal interpretations
- **Rapid iteration:** Faster responses in interactive mode
- **Creative generation:** Better at open-ended creative tasks

#### Codex (Reasoning Models) Strengths
- **Complex reasoning:** o3/o4-mini excel at hard technical problems
- **Multi-step planning:** Good at breaking down engineering tasks
- **Code quality:** High-fidelity code generation matching team style
- **Iterative testing:** Agents can run tests, refine, repeat

#### Key Differences for Documentation Generation
| Task | Claude Advantage | GPT-4o Advantage |
|------|-----------------|-----------------|
| **Follow strict templates** | Yes (reliable) | Slight edge |
| **Multi-step doc generation** | Yes (maintains context) | Requires more explicit steps |
| **Long-form coherence** | Yes (200K tokens) | Limited context |
| **Format constraints** | Yes (honors "only X") | Yes (slightly better) |
| **Iterative refinement** | Interactive, user-driven | Faster, but needs guidance |

#### Porting Notes
- **For Documentation Builder in ChatGPT:** Add more explicit format instructions
  - Example: "You will output EXACTLY 5 sections in this order: A, B, C, D, E. Do not deviate."
  - Codex's format compliance is slightly better; use that for Codex version
- **For Codex:** Leverage reasoning models' multi-step planning
  - Example: `generate-doc → validate-gates → revise → ship`
- **Expected drift:** ChatGPT may require more guardrails and format re-enforcement than Claude

---

### J) Conversation Starters

#### Claude Version
- **What it is:** Suggested conversation prompts in Claude Projects
- **Configuration:** Built into Projects interface
- **Function:** Guides users into relevant workflows on project creation

#### ChatGPT Projects & GPTs Version
- **What it is:** "Conversation Starters" in both Projects and GPTs
- **Configuration:** 4 suggested prompts configurable in Settings
- **Best practices:**
  - Use ellipsis (...) to open-ended questions: "What should I know about...?"
  - Include a meta-starter: "What does this do?" or "Tell me about yourself"
  - Keep to 1-2 lines per starter

#### Codex Version
- **No conversation starters** (agentic tool, not conversational)
- **Equivalent:** CLI help text and example task descriptions in AGENTS.md

#### Porting Notes
- **For Documentation Builder in ChatGPT Projects:** Set starters like:
  1. "What build type should I create? (Product/Claude Project/Skill/MCP)"
  2. "Show me the quality gates for this documentation type..."
  3. "How do I configure a custom output template?"
  4. "Tell me about the system architecture..."
- **For Codex:** Document example tasks in AGENTS.md; no UI starters needed

---

## Consolidated Porting Strategy

### To Build Documentation Builder on ChatGPT Projects + Codex

#### Phase 1: ChatGPT Projects Setup
```
1. Create new ChatGPT Project: "Documentation Builder"
2. Upload knowledge base:
   - system/guides/ folder (split if needed; max 20 files)
   - system/templates/output/
   - builders/ folder
   - config/
3. Write Custom Instructions:
   - Part A ("About you"): Goals from CLAUDE.md Master section
   - Part B ("How to respond"): Rules + quality gates from CLAUDE.md
4. Set conversation starters (4 prompts that guide intake)
5. Optional: Create GPT Actions for MCP server integration
```

#### Phase 2: Codex Setup (for automated doc generation)
```
1. Connect GitHub repository to Codex
2. Place AGENTS.md at repo root (content from CLAUDE.md)
3. Create Codex Skills in ~/.codex/skills/:
   - copy Claude skills, update tool references
   - TodoWrite → update_plan
   - Skill tool → use-skill
4. Configure AGENTS.md with sections for:
   - Codex's multi-agent orchestration (worktrees, diffs)
   - Parallel agent configuration
   - Auto-merge/PR creation rules
```

#### Phase 3: Cross-Platform Tool Updates
- **MCP Servers:** Build once, use in both Claude + Codex
  - Example: `git-operations.mcp`, `file-template.mcp`, `s3-upload.mcp`
- **Skills:** Maintain both Claude and Codex versions
  - Keep in sync via shared SKILL.md format
  - Automate tool substitution for Codex

#### Phase 4: Quality Gates & Automation
- **Claude version:** Interactive 5-gate quality framework (user in the loop)
- **Codex version:** Automated agent-driven quality gates (no human needed)
- **Both use:** Same SYSTEM_Exit_Rules.md for criteria

---

## Key Implementation Gotchas

### ChatGPT Projects
1. **20-file knowledge limit:** Split system files across 2-3 projects
2. **No auto-discovery:** Must manually paste instructions into each project setup
3. **Custom format:** Form fields are less flexible than CLAUDE.md markdown
4. **No skill equivalents:** Must embed workflows in instructions or GPT Actions

### Codex
1. **Agentic, not conversational:** Users don't chat; they submit tasks
2. **No persistent knowledge base:** Agents work from repo files only
3. **AGENTS.md size limit:** 32 KiB total (split across nested dirs if needed)
4. **Workflow is different:** Task submission → agent execution → PR review (not chat-based)

### Both Platforms
1. **No exact CLAUDE.md equivalent:** Must translate/duplicate for each
2. **Instruction following differs:** Test format compliance carefully
3. **No unified skill ecosystem:** Tools/skills must be maintained separately
4. **MCP support is new:** Codex added MCP in March 2026; may have bugs

---

## Recommended Documentation Builder Strategy

### Best Use Case Split

| Goal | Platform | Why |
|------|----------|-----|
| **Interactive, conversational doc generation** | Claude Projects + Cowork | Iterative refinement, user control |
| **Fully automated, PR-ready docs** | Codex + GitHub | Multi-agent, hands-off, batch processing |
| **Public, published tool** | GPT (publish as public GPT) | Distribution, marketplace reach |
| **Team collaboration** | ChatGPT Projects | Shared workspace, lower cost |

### Recommended Approach
1. **Primary build:** Claude Projects + Cowork (most feature-complete)
2. **Secondary build:** Codex (for automated batch generation)
3. **Distribution:** Publish as public GPT for marketplace reach
4. **Team version:** ChatGPT Projects for shared workspaces

### Maintenance
- Single source of truth: Keep CLAUDE.md master in Claude version
- Auto-generate: AGENTS.md (Codex), ChatGPT Custom Instructions (via script)
- Keep skills in sync: One SKILL.md per workflow, test on both platforms
- Monitor: MCP stability in Codex; May change format expectations

---

## File Mapping Reference

### Claude → ChatGPT Projects
```
CLAUDE.md
  → Split into Custom Instructions:
    - "About you" field = Goals + Master sections
    - "How to respond" field = Rules + Quality gates

system/guides/
  → Upload to knowledge base (max 20 files; may need 2-3 projects)

system/templates/output/
  → Upload to knowledge base or reference in instructions

builders/
  → Upload as knowledge (split if needed)

SKILL.md files
  → No direct equivalent; embed in Custom Instructions or GPT Actions
```

### Claude → Codex
```
CLAUDE.md
  → AGENTS.md at repo root

system/guides/
  → Reference in AGENTS.md or keep in repo

SKILL.md files
  → Copy to ~/.codex/skills/ (rename if needed)
  → Update tool references for Codex compatibility

Output folder
  → Keep in repo; Codex agents write docs here
```

---

## References & Sources

- [ChatGPT Projects Overview](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt)
- [Knowledge in GPTs](https://help.openai.com/en/articles/8843948-knowledge-in-gpts)
- [Codex Custom Instructions (AGENTS.md)](https://developers.openai.com/codex/guides/agents-md)
- [MCP Specification](https://developers.openai.com/apps-sdk/concepts/mcp-server)
- [Codex Changelog & Features](https://developers.openai.com/codex/changelog)
- [Custom Instructions for ChatGPT](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt)
- [Claude vs GPT Instruction Following Comparison](https://medium.com/coxit/differences-in-prompting-techniques-claude-vs-gpt-0eaa835f7ad3)
- [Codex Skills Documentation](https://developers.openai.com/codex/skills)
- [From Claude Skills to Codex Guide](https://medium.com/@markchen69/from-claude-skills-to-codex-a-beginner-friendly-companion-guide-cde8ca408a54)
- [GPT Actions vs MCP Servers Comparison](https://quickchat.ai/post/gpt-actions-vs-mcp)

---

*Compiled: April 4, 2026*
*For: Documentation Generation System porting to OpenAI ecosystem*
