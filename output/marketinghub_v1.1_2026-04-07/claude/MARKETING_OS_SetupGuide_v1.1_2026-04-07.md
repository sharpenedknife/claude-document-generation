# Marketing OS — Setup Guide
**Version:** 1.1 | **Date:** 2026-04-07 | **Changelog:** Added full UX setup (conversation starters, artifact mode, canvas triggers, mode commands)

---

## ── What's New in v1.1 ──

- **Claude:** 4 conversation starters (paste-ready), artifact mode, extended thinking triggers, mode commands
- **ChatGPT:** 4 starters per GPT (copy-paste ready), canvas mode triggers, memory update commands
- **Both:** Consistent emoji status system, response format templates, code block conventions

---

## Claude.ai Setup — Full UX Configuration (15 min)

### Step 1: Create the Project

```
Claude.ai → Sidebar → Projects → + New Project → Name: "Marketing OS"
```

### Step 2: Add Core Files (Project Knowledge)

Upload these in order (Project Settings → Knowledge):

```
Priority 1 — Core System (upload first):
✅ MARKETING_OS_CLAUDE_v1.1_2026-04-07.md      ← Main instructions

Priority 2 — Reference (upload second):
📖 MARKETING_OS_SkillOrchestration_Matrix_v1.0_2026-04-07.md
📖 MARKETING_OS_KnowledgeStructure_v1.0_2026-04-07.md
📖 MARKETING_OS_Instructions_v1.0_2026-04-07.md
📖 MARKETING_OS_TokenOptimization_v1.0_2026-04-07.md

Priority 3 — Templates (upload third):
📋 MARKETING_OS_ProjectContext_Template_v1.0_2026-04-07.md
📋 MARKETING_OS_Research_GTM_Framework_v1.0_2026-04-07.md
```

### Step 3: Set Conversation Starters ← NEW IN v1.1

**In Project Settings → Conversation Starters, paste these exactly (one per field):**

```
🚀 Start a new project — build my marketing context from scratch
```

```
📧 Write a cold email campaign — I'll tell you the project
```

```
📊 Review this week's performance and tell me what to do next
```

```
✍ I need copy — landing page, email, or ad creative
```

**What they trigger:**
| Starter | Skill Route | Output | Tokens |
|---------|-------------|--------|--------|
| 🚀 New project | customer-research + competitive-analysis + brand-storytelling | project-marketing-context.md | 5–7K |
| 📧 Cold email | cold-email skill | 5 variations + 3 follow-ups | ~2K |
| 📊 Performance review | Analytics synthesis + 3 optimization plays | Action plan | ~1K |
| ✍ I need copy | copywriting skill (landing/email/ad) | Full copy + quality score | 1.5–2K |

### Step 4: Set Custom Style (Optional)

```
Claude.ai → Settings → Custom Styles → + New Style
```

**Recommended style for Marketing OS:**
```
Direct and lean. No preamble. Lead with what I'm doing (🎯 skill name + ⚡ token estimate).
Always use emoji status indicators. Put long outputs in artifacts. Wrap paste-ready content
in code blocks. End every response with ➡️ next action.
```

### Step 5: First-Run Test

Open the project. Click the **"🚀 Start a new project"** starter.

**Expected response:**
```
🎯 Building your project context — I'll run customer-research + competitive-analysis
⚡ ~5–6K tokens for full research phase

What's the project?
- What does it do? (1–2 sentences)
- Who's the target buyer? (role + company type)
```

If you see this, setup is complete.

---

## Mode Commands Reference (Claude)

Use these anytime in any conversation:

| Type | Command | What Happens |
|------|---------|-------------|
| **Research** | `research mode` | Deep analysis, extended thinking, no token limits |
| **Campaign** | `campaign mode` | Batch outputs, strict 2.5K budget, speed-first |
| **Review** | `review mode` | Score everything, suggest revisions, quality-first |
| **Quick** | `quick mode` | Sub-500 token answers, directional only |
| **Planning** | `planning mode` | Monthly/weekly cadence, roadmaps, priorities |
| **Reset** | `reset` | Clear context, return to default |

**Context switching example:**
> "campaign mode — I need 5 cold email variations for Project A"
> → Claude confirms mode, batches all 5 in one artifact, scores, outputs ➡️ next action

---

## Artifact Usage Guide (Claude)

**Claude auto-opens artifacts for 10+ line outputs. You can also force it:**

- "Put that in an artifact" — opens rendered markdown/HTML
- "Open canvas" — same effect
- "Combine those into one doc" — merges into single artifact

**What renders best as artifacts:**
- Full email sequences (markdown table or formatted list)
- Landing page copy (section headers + body)
- Campaign plans (numbered phases)
- Strategy docs (headers + bullets + tables)
- Project context files (structured markdown)

**What stays inline:**
- Quick answers and routing decisions
- Quality scores
- Status updates
- One-liners and short questions

---

## ChatGPT Setup — Full UX Configuration (20 min)

### Step 1: Set Up the 5 Projects

Create these 5 projects in ChatGPT (New Chat → Projects → + New):

| Project | Purpose | Memory |
|---------|---------|--------|
| Marketing OS | Strategy + research | On |
| Content Engine | Content production | On |
| Funnel / CRO | Conversion optimization | On |
| Client Template | Per-client isolation | Off (new per client) |
| Coding / Product Dev | PRD + engineering | On |

**For each project:** Upload the matching PROJECT_0X file from `chatgpt/` folder.

### Step 2: Set Up the 5 Custom GPTs

Create these GPTs (ChatGPT → Explore GPTs → + Create):

| GPT Name | File | Conversation Starters |
|----------|------|----------------------|
| Research Architect | GPT_01_Research_Architect.md | 4 starters (see below) |
| Messaging Critic | GPT_02_Messaging_Critic.md | 4 starters |
| Funnel Builder | GPT_03_Funnel_Builder.md | 4 starters |
| Copy Rewriter | GPT_04_Copy_Rewriter.md | 4 starters |
| PRD Thinker | GPT_05_PRD_Product_Thinker.md | 4 starters |

### Step 3: Set Conversation Starters Per GPT ← NEW IN v1.1

**In GPT Editor → Configure → Conversation Starters, paste 4 per GPT:**

**Research Architect:**
```
Map my market landscape — who are my buyers and where do they live online?
```
```
Analyze my top 3 competitors — gaps, angles, vulnerabilities
```
```
Design a customer research plan — I'll tell you what I'm trying to learn
```
```
Build my GTM research brief — I have a new project to launch
```

**Messaging Critic:**
```
Critique this headline — score it and tell me what's weak
```
```
Score my landing page copy — is it differentiated or generic?
```
```
Punch up this cold email — make it sharper and more specific
```
```
Pressure-test my positioning — does this only work for my company?
```

**Funnel Builder:**
```
Design my full funnel — from first touchpoint to first dollar
```
```
Find my biggest conversion leak — where am I losing people?
```
```
Build a nurture sequence plan — I'll tell you the product and ICP
```
```
Optimize my lead capture form — here's what I have now
```

**Copy Rewriter:**
```
Tighten this copy — make it 30% shorter without losing impact
```
```
Rewrite this for my ICP — I'll tell you who they are
```
```
Make this email sharper — cut the fluff, strengthen the hook
```
```
Give me 3 versions of this headline — bolder, clearer, more specific
```

**PRD Thinker:**
```
Turn this idea into a PRD — I'll describe what we want to build
```
```
Write a feature spec for engineering — here's the user problem
```
```
Convert this conversation into a dev brief — paste the thread
```
```
Define success metrics for this feature — I need measurable outcomes
```

### Step 4: Enable Canvas Mode (Per GPT)

**Add this to the end of each GPT's system prompt:**

```
CANVAS RULE: When generating content longer than 15 lines (full emails, landing pages,
PRDs, campaign plans, research briefs), always open canvas mode. Tell the user:
"Opening canvas for this — you can edit it directly."
```

**Denis can also trigger manually:** "Use canvas for this" in any message.

### Step 5: Set Memory Update Triggers (ChatGPT)

**Add to Marketing OS and Content Engine GPT prompts:**

```
MEMORY RULE: After any session where ICP, messaging, or channel strategy changes, say:
"Should I update my memory with [specific learning]? This affects future sessions."
Wait for confirmation before updating.
```

---

## Daily Workflow (Both Platforms)

### Morning (5 min)

**Claude:**
> Click "📊 Review this week's performance" starter
> → Tell Claude which projects are active
> → Get: what's live, what metrics came in, what to do today

**ChatGPT:**
> Open Marketing OS project
> Type: "What's my priority this week for [Project]?"
> → Get: top 3 priorities based on memory + project context

### Campaign Execution (1–2 hours)

**Claude:**
1. Click appropriate starter (📧 cold email / ✍ copy)
2. Tell Claude the project
3. Approve skill routing + token estimate
4. Receive artifact output
5. Review quality score (📊 X/10)
6. Copy from artifact → paste into platform

**ChatGPT:**
1. Open the right GPT (Messaging Critic for review, Copy Rewriter for polish)
2. Paste content or describe request
3. Canvas opens automatically for long outputs
4. Edit directly in canvas
5. Copy final version → paste into platform

### Weekly Review (30 min)

**Claude:**
> "planning mode — review [Project A] this week"
> → Get: performance summary, 3 optimization plays, next week plan

**ChatGPT → Marketing OS project:**
> "Review my campaigns from this week — here are the metrics: [paste]"
> → Get: what worked, what didn't, what to test next
> If ICP learning: "Update memory with: [learning]"

---

## Platform Selection Guide

| Task | Use Claude | Use ChatGPT |
|------|-----------|------------|
| Deep ICP research | ✅ Extended thinking | ✓ Research Architect GPT |
| Writing cold emails | ✅ cold-email skill | ✓ Copy Rewriter GPT |
| Editing existing copy | ✅ copy-editing skill | ✅ Copy Rewriter + Canvas |
| Landing page copy | ✅ copywriting skill (artifact) | ✅ Canvas mode |
| Funnel design | ✓ designing-growth-loops | ✅ Funnel Builder GPT |
| Messaging critique | ✓ copywriting (review) | ✅ Messaging Critic GPT |
| PRD / product spec | ✓ General | ✅ PRD Thinker GPT |
| Token-aware batching | ✅ Explicit budget control | ✗ No token visibility |
| Cross-session memory | ✅ Project knowledge files | ✅ Memory feature |
| Visual doc editing | ✅ Artifacts (view only) | ✅ Canvas (edit inline) |

**Rule of thumb:**
- Use **Claude** when you need strategic depth, token control, or skill orchestration
- Use **ChatGPT** when you need inline document editing (canvas) or specialized GPT personas

---

## First-Time Setup Checklist

**Claude.ai:**
- [ ] Project created: "Marketing OS"
- [ ] MARKETING_OS_CLAUDE_v1.1 uploaded as primary instruction
- [ ] 5 reference docs uploaded to knowledge
- [ ] 4 conversation starters set (exact text from Step 3)
- [ ] Custom style set (optional but recommended)
- [ ] First project context created: [ProjectName]_marketing.md
- [ ] Test: clicked a starter, got correct routing response

**ChatGPT:**
- [ ] 5 projects created (Marketing OS, Content Engine, Funnel/CRO, Client Template, Coding)
- [ ] Each project has its PROJECT file uploaded
- [ ] 5 GPTs created (Research, Messaging, Funnel, Copy, PRD)
- [ ] Each GPT has 4 conversation starters set
- [ ] Canvas mode rule added to each GPT prompt
- [ ] Memory trigger added to Marketing OS + Content Engine
- [ ] Test: opened Research Architect GPT, clicked a starter, got structured response

---

## Troubleshooting

| Problem | Solution |
|---------|---------|
| Claude doesn't know my project | Check project-marketing-context.md is in Project Knowledge |
| Starters don't appear | Settings → Project → Conversation Starters (requires Pro/Team) |
| Artifact doesn't open | Say "put that in an artifact" or check if output is 10+ lines |
| ChatGPT canvas won't open | Say "use canvas for this" or check GPT has canvas rule in prompt |
| Quality score below 7/10 | Check if ICP is specific in project context (vague ICP = generic output) |
| Tokens running high | Batch tasks, skip polish for drafts, reuse context |
| GPT gives generic answer | It may not have the project context file — upload to that project |

---

*Marketing OS v1.1 · Setup Guide · 2026-04-07*
*Full UX configuration for both Claude.ai and ChatGPT*
