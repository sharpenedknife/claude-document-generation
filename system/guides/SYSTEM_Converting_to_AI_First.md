# Converting Docs to AI-First Format

Migration guide for existing documentation to become AI-readable while staying human-friendly.

---

## Before & After Examples

### Example 1: Prerequisites Section

**BEFORE (Human-only):**
```markdown
## Prerequisites

You'll need Node.js 16 or higher and npm 8 or higher installed on your machine. 
We also recommend having some familiarity with the terminal, though it's not strictly necessary.
You should have a GitHub account to access the repository.
```

**AFTER (AI-first + Human-friendly):**
```markdown
## Prerequisites

### Level 1: Tools & Software
- **Node.js 16+** (required)
  - Check: `node --version`
  - Install: https://nodejs.org/en/download/ (select LTS v16+)
  - Why: Project requires native Promise/async support (added in v16)

- **npm 8+** (required)
  - Check: `npm --version`
  - Install: `npm install -g npm@latest`
  - Why: We use npm workspaces (feature added in npm 8)

### Level 2: Access & Keys
- **GitHub account** (required)
  - Check: `git clone <repo>` works without password prompt
  - Get: Create at https://github.com/signup
  - Why: Need to pull repository code

### Level 3: Knowledge
- **Comfortable with terminal** (optional)
  - Guide: https://ubuntu.com/tutorials/command-line-for-beginners (5 min)
  - Why: Easier to troubleshoot if something goes wrong

**Ready?** Run this:
```bash
node --version && npm --version && git --version
```
All three should show version numbers. If any say "command not found," install it.
```

**What changed:**
- Vague → Specific versions
- Descriptions → Check commands
- Generic → Level-based structure (parseable)
- "Somewhat helpful to know" → Clearly optional
- Verification test at end

---

### Example 2: Step-by-Step Instructions

**BEFORE (Human-only):**
```markdown
## Installation

1. Clone the repository from GitHub
2. Navigate to the project directory
3. Install dependencies using npm
4. Run the setup script to verify everything works
```

**AFTER (AI-first + Human-friendly):**
```markdown
## Installation

### Step 1: Clone Repository
1. Run: `git clone https://github.com/yourorg/project.git && cd project`
   Expected: Folder now contains project files (you see `src/`, `package.json`, etc.)
   
   **AI metadata:**
   - Precondition: Git installed, GitHub access
   - Postcondition: Project code in current directory
   - Time: ~10 seconds
   - Related: See Prerequisites → Level 2: Access

### Step 2: Install Dependencies
1. Run: `npm install`
   Expected: Terminal shows progress, completes with "added X packages"
   
   **AI metadata:**
   - Precondition: Node 16+, npm 8+, package.json exists
   - Postcondition: node_modules/ folder created
   - Time: Usually 1-3 minutes
   - Common error: See Troubleshooting → "npm ERR!"

### Step 3: Verify Setup
1. Run: `npm run verify`
   Expected: Output shows "✓ All checks passed"
   
   **AI metadata:**
   - Precondition: node_modules/ exists
   - Postcondition: Setup verified working
   - If fails: See Troubleshooting section below
```

**What changed:**
- Descriptions → Exact commands
- Vague flow → Numbered steps
- No expected output → Shows what terminal displays
- No relationships → Metadata shows preconditions/postconditions
- No links → Related docs referenced in metadata

---

### Example 3: Troubleshooting

**BEFORE (Human-only):**
```markdown
## Troubleshooting

If you get an error installing dependencies, try clearing the npm cache 
and installing again. If you get permission errors, you might need to fix 
npm permissions. For more information, see the npm documentation.
```

**AFTER (AI-first + Human-friendly):**
```markdown
## Troubleshooting

### Error: "npm ERR! code ERESOLVE"
**Root cause:** Dependency version conflict (npm 7+ is strict about versions)
**Fix:**
1. Try: `npm install --legacy-peer-deps`
2. If fails: `npm cache clean --force && npm install`
3. Check: `npm list` (should show clean output)

**AI metadata:**
- Error signature: "npm ERR! code ERESOLVE"
- Precondition check: npm 7+
- Solution type: dependency conflict resolution
- Related: Prerequisites → Level 1: npm version check

---

### Error: "npm ERR! code EACCES"
**Root cause:** Permission issue (npm trying to write to protected directory)
**Fix:**
1. Try: `sudo npm install` (use system sudo)
2. Better: `npm config set prefix ~/.npm-global` then add to PATH
3. Verify: `npm config get prefix` (should show ~/.npm-global)

**AI metadata:**
- Error signature: "npm ERR! code EACCES"
- Precondition check: File system permissions
- Solution type: permission configuration
- Alternative: Use Node version manager (nvm) instead

---

### Error: "command not found: npm"
**Root cause:** npm not installed or not in PATH
**Fix:**
1. Install Node: https://nodejs.org/en/download/
2. Restart terminal (close and reopen)
3. Check: `npm --version` (should be 8+)

**AI metadata:**
- Error signature: "command not found: npm"
- Precondition needed: nodejs_16+ installed
- Related: Prerequisites → Level 1: Node.js
```

**What changed:**
- Vague guidance → Exact error signatures
- Generic advice → Specific solutions
- No context → Metadata explains when error occurs
- No links → Related sections referenced
- Causes explained → Users understand why

---

## Conversion Checklist

For each section, convert in this order:

### 1. Add Frontmatter (First!)
```yaml
---
doc_type: [setup|api|config|troubleshooting|feature|architecture|adr|process]
audience: [beginner|intermediate|advanced|all]
difficulty: [easy|medium|hard]
time_estimate: "X-minutes|1-hour|varies"
prerequisites: [tool_version, access, knowledge]
related_docs: [doc_title_1, doc_title_2]
tags: [keyword1, keyword2]
updated: YYYY-MM-DD
status: production
---
```

### 2. Convert Prerequisites
- Separate into Levels 1-4
- Add check commands
- Add install links
- Add "Why" explanations
- Add verification test at end

### 3. Convert Steps
- Use exact commands (not descriptions)
- Show expected output after each
- Add **AI metadata:** block with:
  - Precondition
  - Postcondition
  - Time estimate
  - Common errors (link to troubleshooting)

### 4. Upgrade Troubleshooting
- Add "Error signature:" field (exact error text)
- Explain root cause
- Provide numbered fix steps
- Add **AI metadata:** with error signature and preconditions

### 5. Add Verification Table
Create Expected Output section:
```markdown
| Check | Expected | Command |
|-------|----------|---------|
| [what to verify] | [what should happen] | [exact command] |
```

### 6. Update Navigation
- Review "Related docs" field in frontmatter
- Update "Next steps" to link by doc title
- Ensure all references use actual doc titles

---

## Migration Impact

### What Stays the Same
- Overall structure (Overview → Prerequisites → Steps → Troubleshooting)
- Tone and voice
- Examples and explanations
- Human readability

### What Changes
- Added frontmatter (8 fields)
- Prerequisites structured as Levels 1-4
- Steps include metadata blocks
- Errors include signatures
- More specific commands and output
- Links centralized in frontmatter

### Benefits

**For Humans:**
- ✅ Easier to scan (structured prerequisites)
- ✅ Clearer prerequisites (specific vs. vague)
- ✅ Better troubleshooting (exact error matching)
- ✅ Better navigation (related docs visible)

**For AI (Claude Projects, RAG, Agents):**
- ✅ Parseable metadata
- ✅ Prerequisite chains discoverable
- ✅ Error signatures matchable
- ✅ Related docs linkable
- ✅ Preconditions verifiable
- ✅ Can chunk intelligently

**Combined:**
- ✅ Claude Projects understand skill levels automatically
- ✅ Can suggest docs users are ready for
- ✅ Can build prerequisite chains
- ✅ Can match user errors instantly
- ✅ Humans still read naturally

---

## Tool: Auto-Conversion Template

Use this template to convert docs systematically:

```markdown
# [Original Title] — [Conversion Status]

## Step 1: Analyze
- [ ] Current frontmatter status: [exists|missing]
- [ ] Prerequisites structured: [levels 1-4|prose]
- [ ] Steps have metadata: [yes|no]
- [ ] Errors have signatures: [yes|no]
- [ ] Verification present: [table|prose|missing]

## Step 2: Add/Update Frontmatter
```yaml
---
doc_type: 
audience: 
difficulty: 
time_estimate: 
prerequisites: 
related_docs: 
tags: 
updated: 
status: 
---
```

## Step 3: Structure Prerequisites
- [ ] Level 1 (Tools): [done|in progress]
- [ ] Level 2 (Access): [done|in progress]
- [ ] Level 3 (Knowledge): [done|in progress]
- [ ] Level 4 (State): [done|in progress]
- [ ] Verification test: [done|missing]

## Step 4: Add Step Metadata
- [ ] Step 1: Add AI metadata block
- [ ] Step 2: Add AI metadata block
- [ ] [continue for all steps]

## Step 5: Fix Troubleshooting
- [ ] Error 1: Add signature + metadata
- [ ] Error 2: Add signature + metadata
- [ ] [continue for all errors]

## Step 6: Add Verification Table
- [ ] Create Expected Output section
- [ ] Add verification table with commands

## Conversion Complete
- [ ] Frontmatter filled
- [ ] All prerequisites structured
- [ ] All steps have metadata
- [ ] All errors have signatures
- [ ] Verification table present
- [ ] Related docs updated
- [ ] Status set to: [production|draft]
```

---

## Common Conversion Mistakes (Avoid These)

❌ **Adding frontmatter but keeping old prose structure**
✅ Do: Restructure prerequisites as Levels 1-4

❌ **Keeping vague error descriptions**
✅ Do: Use exact error signatures from user reports

❌ **Forgetting metadata blocks in steps**
✅ Do: Every step gets **AI metadata:** with preconditions

❌ **Inline links everywhere**
✅ Do: Move links to frontmatter, use doc titles in prose

❌ **Converting without testing with Claude**
✅ Do: Paste converted doc into Claude Projects, verify it parses frontmatter

---

## Quick Start: 30-Minute Conversion

1. **5 min:** Add frontmatter template
2. **10 min:** Restructure prerequisites as Levels 1-4
3. **10 min:** Add error signatures to troubleshooting
4. **5 min:** Test with Claude (paste doc, ask "What are prerequisites?")

Verify Claude extracts frontmatter correctly. If yes, you're ready for production.
