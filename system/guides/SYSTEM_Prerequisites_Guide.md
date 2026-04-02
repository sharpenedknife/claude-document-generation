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
