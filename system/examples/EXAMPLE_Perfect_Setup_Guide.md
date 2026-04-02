---
doc_type: setup_guide
domain: web_dev
builder_version: "v1.0"
generated_by: example_builder
generated_at: 2026-04-02T00:00:00Z
builder_session_id: example_session_001

audience: beginner
difficulty: easy
time_estimate: "15-minutes"
prerequisites: [terminal_basics]
related_docs: [Deploy_to_Production, Troubleshooting_Setup]
tags: [setup, nodejs, npm, quick_start]

status: production
version: "1.0"
updated: 2026-04-02

quality_score: 95
token_count: 2340
exit_gates_passed: [1,2,3,4,5]
exit_gates_failed: []
---

# How to Install Node.js and npm

Install Node.js and npm on your machine in 15 minutes.
This gets you ready to run JavaScript applications locally.

**Search keywords:** node.js installation, npm setup, nodejs download, javascript environment
**Audience:** beginner
**Time to complete:** 15 minutes

---

## Prerequisites

### Node.js (not yet installed)
Check: `node --version`
If you see: "command not found" → continue to setup
If you see: "v16.0.0+" → you already have it installed ✓

Install if needed: https://nodejs.org/en/download/ (download v16 LTS or newer)
Why: Node.js is the JavaScript runtime. npm comes with it.

---

## Setup

### Step 1: Download Node.js Installer
1. Go to: https://nodejs.org/en/download/
2. Click: Green button (LTS version - most stable)
3. Choose: Your operating system (Windows/Mac/Linux)
4. Click: Download

Expected: `.msi` (Windows), `.pkg` (Mac), or `.tar.xz` (Linux) file downloaded

**AI metadata:**
- Precondition: Internet access, admin rights to install
- Postcondition: Installer file on your computer
- Time: 1 minute
- Common error: See Troubleshooting → "Download fails"

---

### Step 2: Run the Installer
1. Open the downloaded file
2. Click: "Install" or "Next" through the steps
3. Accept: Default settings (click through)
4. Restart: Your computer (important!)

Expected: Installer completes, system restarts

**AI metadata:**
- Precondition: Installer downloaded, admin rights
- Postcondition: Node.js installed, terminal updated
- Time: 5 minutes
- Common error: See Troubleshooting → "Installation hangs"

---

### Step 3: Verify Installation
1. Open terminal (Mac/Linux) or Command Prompt (Windows)
2. Run: `node --version`
   Expected output: `v16.13.0` (or higher)

3. Run: `npm --version`
   Expected output: `8.1.0` (or higher)

Expected: Both commands show version numbers ✓

**AI metadata:**
- Precondition: Installer completed, computer restarted
- Postcondition: Node and npm in system PATH
- Time: 2 minutes
- Common error: See Troubleshooting → "Command not found"

---

## What Success Looks Like

After setup, you should:

| Check | Expected | Command |
|-------|----------|---------|
| Node installed | Version shows (v16+) | `node --version` |
| npm installed | Version shows (8+) | `npm --version` |
| Can create project | No errors | `npm init -y` |
| Can install packages | No errors | `npm install express` |

If all pass: ✅ Setup complete

---

## Troubleshooting

### Error: "command not found: node"
**Root cause:** Node.js not in system PATH (terminal wasn't restarted after install)

**Fix:**
1. Restart your computer (close and reopen terminal)
2. Try again: `node --version`
3. If still fails: Uninstall and reinstall Node.js

**AI metadata:**
- Error signature: "command not found: node"
- Precondition check: Installer completed? Restart done?
- Related: Installation hangs (see that error)

---

### Error: "v15.6.0 (node version too old)"
**Root cause:** Node.js installed but version too old (need v16+)

**Fix:**
1. Uninstall current Node.js
2. Download v16+ from nodejs.org
3. Install new version
4. Restart computer
5. Verify: `node --version` (should show v16+)

**AI metadata:**
- Error signature: "v15" or "v14" showing when you check
- Precondition check: Which version shows? `node --version`
- Related: Installation fails (wrong download link)

---

### Error: Permission denied (Mac/Linux)
**Root cause:** Missing admin rights or PATH not updated

**Fix:**
1. Restart terminal: Close and reopen
2. Try again: `npm --version`
3. If still fails: Try `sudo npm --version` (admin mode)

**AI metadata:**
- Error signature: "permission denied" or "EACCES"
- Precondition check: Is terminal open after restart?
- Related: Command not found

---

## Why This Approach

We use the official Node.js installer because:
- **Simplest:** No build steps, works for beginners
- **Official:** Directly from nodejs.org, always current
- **Reliable:** Handles PATH setup automatically
- **Tested:** Millions of users, no surprises

---

## After Setup

You now have Node.js and npm installed. Next steps:

1. **Create your first project** → See: "Create a Node.js Project"
   - Use if: You want to start building
   - Time: 10 minutes

2. **Learn npm basics** → See: "Understanding npm packages"
   - Use if: You want to understand how npm works
   - Time: 15 minutes

3. **Deploy to production** → See: "Deploy Node.js App"
   - Use if: You're ready to put your app online
   - Time: Varies

Choose based on your next goal.
