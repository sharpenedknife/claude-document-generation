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
