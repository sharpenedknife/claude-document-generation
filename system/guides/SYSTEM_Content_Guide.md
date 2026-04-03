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
