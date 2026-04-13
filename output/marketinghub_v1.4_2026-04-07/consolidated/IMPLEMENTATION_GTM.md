# Marketing Hub — Implementation & GTM Reference
**v1.4 · 2026-04-07 · Full setup + strategy reference**
---
# Marketing Hub — Setup Guide
**Version:** 1.3 | **Date:** 2026-04-07 | **Status:** Production
**Architecture:** Claude = Brain | ChatGPT = Execution Engine
**New in v1.3:** Full platform UI/UX — Artifacts, Styles, Memory, Code Interpreter, Image Gen, Scheduled Tasks

---

## Architecture Overview

```
DAILY WORKFLOW

Denis
  │
  ▼
Claude.ai — Marketing OS Project
  │  UI: Conversation Starters · Artifacts · Custom Style · Memory · Model Routing
  │
  ├─ generates 📋 BRIEF (in Artifact)
  │
  ▼
ChatGPT GPT
  │  UI: Conversation Starters · Canvas · Code Interpreter · Image Gen · Web Search
  │
  ├─ returns output in Canvas
  │
  ▼
Denis pastes back into Claude
  │
  ▼
Claude evaluates → 📊 EVALUATION (in Artifact) → SHIP or Revision Brief
```

**Token cost:** Claude ~8–15K/month | ChatGPT: flat ~$20/month Plus

---

## PART 1 — CLAUDE.AI SETUP

### Feature Map — Everything You'll Configure

| Feature | Where | What it does |
|---------|-------|-------------|
| Project | Projects → New | Persistent workspace, 200K context |
| Knowledge files | Project → Knowledge | ICP, product, strategy context always loaded |
| Custom Instructions | Project → Settings | Claude's role, brief format, evaluation format |
| Conversation Starters | Project → Settings | 4 clickable buttons to launch workflows |
| Custom Style | Profile → Styles | Response format baked in — no re-prompting |
| Memory | Automatic | ICP, campaigns, preferences across sessions |
| Artifacts | Automatic (instructed) | Every structured output opens in side panel |
| Extended Thinking | Automatic (criteria-based) | Activates for strategy sessions |
| Model Selection | Chat (manual override) | Opus/Sonnet/Haiku per task weight |

---

### Step 1: Create the Project

1. **claude.ai → Projects → New Project**
2. Name: `Marketing OS`
3. Description: `Marketing brain — strategy, briefs, evaluation`

---

### Step 2: Upload Project Knowledge Files

Upload all of these to **Project → Knowledge → Add content → Upload files**:

```
MARKETING_OS_CLAUDE_v1.4_2026-04-07.md   ← Claude's brain instructions (primary)
CONTEXT_Product.md                         ← Your product context (fill in first)
CONTEXT_Technical.md                       ← Stack + integrations
IMPLEMENTATION.md                          ← GTM strategy
```

How to fill in CONTEXT_Product.md before uploading:
- Product name and 2-sentence description
- Primary ICP (role, company size, pain)
- Current stage (pre-launch / traction / growth)
- Active channels
- Key proof points (stats, testimonials, case studies)

---

### Step 3: Set Custom Instructions

**Project → Settings → Custom Instructions** — paste:

```
You are Marketing OS — the strategic brain of Denis's dual-platform marketing system.

YOUR ROLE:
- Maintain full product/ICP/campaign context via memory and knowledge files
- Generate structured briefs for ChatGPT execution GPTs — always in Markdown artifact
- Evaluate ChatGPT output and score 1–10 — always in Markdown artifact
- Route requests to the correct GPT using the routing table
- Run strategy sessions using extended thinking when appropriate

ARTIFACT RULE: Open an artifact for ANY output 10+ lines. Never dump structure into chat.

MEMORY: Maintain across sessions — active product, ICP, campaigns, last evaluation.

DO NOT write final marketing copy. DO NOT do web research. Generate briefs for execution GPTs.

ROUTING:
ICP research → ICP Builder brief
Positioning / copy scoring → Messaging Builder brief
Funnel design → Funnel Builder brief
Emails / ads / blog / social → Content Builder brief
Feature specs / launch → Build Planner brief
Landing pages → Landing Builder brief
Strategy / GTM → Claude brain (artifact)
Evaluate output → Claude brain (evaluation artifact)
```

---

### Step 4: Set Conversation Starters

**Project → Settings → Conversation Starters** — add these 4 exactly:

```
🧠 Plan my next campaign
```
```
📊 Evaluate this output
```
```
🗺️ Build my GTM strategy
```
```
🔄 Update my project context
```

**What each button does:**
- **🧠 Plan** → Claude asks goal + ICP, produces campaign plan + first brief in artifact
- **📊 Evaluate** → Claude asks you to paste ChatGPT output, produces scored evaluation artifact
- **🗺️ GTM** → Engages extended thinking, produces full GTM strategy artifact
- **🔄 Update** → Claude asks what changed, updates memory, confirms

---

### Step 5: Create Custom Style

**Profile → Styles → Create Style**

Name: `Marketing OS`

Instructions to paste:
```
Response format:
- Direct, no preamble. Lead with the action or answer.
- Never start with "Great question", "Absolutely", "Certainly"
- Any output 10+ lines → open in artifact (Markdown)
- Briefs: use 📋 BRIEF FOR [GPT NAME] format with divider lines
- Evaluations: use 📊 EVALUATION format with 4-dimension scoring
- Strategy: section headers + "Next actions" numbered list at end
- Tone: confident, precise, marketing-literate
- Avoid: bullet points for things that should be prose, re-stating the question, hedging without resolution
```

**Activate the style:**
- After creating it, set it as active in the Marketing OS Project
- It applies to all conversations in the project automatically
- Switch to a different style for non-marketing projects

---

### Step 6: Memory — How It Works

Memory is automatic. After sessions where significant context changes:
- Claude updates memory with: current ICP, active campaigns, last evaluation outcome, Denis's focus
- Next session: Claude reads memory and picks up where you left off

**To manually seed memory** (first session):
```
Remember this context:
Product: [name + 2 sentences]
Primary ICP: [role, company, pain]
Current campaign: [what I'm running]
Preferred format: direct, use artifact for everything structured
```

**To check memory:**
```
What do you remember about my product and current campaigns?
```

---

### Step 7: Model Routing

Claude auto-selects model based on task. Override anytime:

| Task | Default Model | Override |
|------|-------------|---------|
| Brief generation | Sonnet | "Use Sonnet for this" |
| Evaluation | Sonnet | "Use Sonnet for this" |
| Full GTM strategy | Opus (via extended thinking) | "Use Haiku — just quick answer" |
| Quick routing question | Haiku | "Use Opus — go deep" |

Extended thinking activates automatically for: GTM strategy, ICP architecture, campaign system design.
It does NOT activate for: briefs, evaluations, routing, quick answers.

---

### Step 8: Artifacts — How They Work

Every structured Claude output opens in the artifact panel (right side).

You can:
- **Edit directly** in the artifact
- **Copy** with one click (copy button top right)
- **Publish** (share via link) — useful for sharing briefs with team
- **Open in new tab** for full-screen editing
- **Download** as markdown

To paste into ChatGPT: click Copy in artifact → paste into GPT chat.

---

## PART 2 — CHATGPT SETUP

### Feature Map — Everything Per GPT

| Feature | Which GPTs | What it does |
|---------|-----------|-------------|
| Conversation Starters | All 6 | 4 clickable entry points per GPT |
| Canvas | All 6 | Auto-opens for >10 line outputs, inline editing |
| Web Search | ICP Builder, Funnel Builder | Live data from G2, Reddit, forums |
| Code Interpreter | ICP, Content, Funnel, Landing, Build Planner | Tables, CSVs, scoring grids, projections |
| Image Generation | Landing Builder | Hero section mockups, section layouts |
| Knowledge Files | All 6 | ICP profiles, messaging frameworks per GPT |
| Canvas Suggest Edits | All 6 | GPT surfaces 2-3 specific edits Denis approves/rejects |
| Canvas Comments | Content, Landing, Messaging | GPT flags weak lines inline |
| Canvas Version History | All 6 | V1 → V2 iteration visible |

---

### GPT Setup — All 6

**For each GPT: chatgpt.com → Explore GPTs → Create a GPT → Configure**

#### GPT 1: ICP Builder

**Name:** `ICP Builder`
**Description:** `Deep customer research with live web data — ICPs, pain points, real quotes from G2, Reddit, forums`
**Instructions:** paste `GPT_01_ICP_Builder.md` contents
**Capabilities:**
- ✅ Web Search
- ✅ Code Interpreter & Data Analysis
- ✅ Canvas
- ❌ Image Generation
**Knowledge:** upload ICP hypothesis doc, any existing customer interviews
**Conversation Starters:**
```
Build my full ICP — I'll give you the product and target market
```
```
Find real customer pain points — search G2, Reddit, and forums now
```
```
Segment my audience — which ICP should I target first?
```
```
What does my ICP actually say about this problem? Pull real quotes.
```

---

#### GPT 2: Messaging Builder

**Name:** `Messaging Builder`
**Description:** `Sharp positioning and copy that lands — build from scratch or score what you have`
**Instructions:** paste `GPT_02_Messaging_Builder.md` contents
**Capabilities:**
- ❌ Web Search
- ✅ Code Interpreter & Data Analysis
- ✅ Canvas
- ❌ Image Generation
**Knowledge:** upload ICP profiles, current positioning doc, competitor messaging samples
**Conversation Starters:**
```
Build my positioning — here's my product and ICP
```
```
Score this copy — what's weak and how do I fix it?
```
```
Write 3 headline versions — sharper, bolder, more specific
```
```
Punch up this cold email — give me 3 rewritten versions
```

---

#### GPT 3: Funnel Builder

**Name:** `Funnel Builder`
**Description:** `Design funnels, find conversion leaks, benchmark against competitors`
**Instructions:** paste `GPT_03_Funnel_Builder.md` contents
**Capabilities:**
- ✅ Web Search (competitor funnel research)
- ✅ Code Interpreter & Data Analysis
- ✅ Canvas
- ❌ Image Generation
**Knowledge:** upload current funnel stages + known conversion rates, ICP profiles
**Conversation Starters:**
```
Design my full funnel — from first touchpoint to first dollar
```
```
Find my biggest conversion leak — where am I losing people?
```
```
Research competitor funnels in my market — what are they doing?
```
```
Build a nurture sequence plan — I'll tell you the product and ICP
```

---

#### GPT 4: Content Builder

**Name:** `Content Builder`
**Description:** `Primary execution engine — emails, ads, blog, LinkedIn, sequences, newsletters. Always 3 versions, paste-ready.`
**Instructions:** paste `GPT_04_Content_Builder.md` contents
**Capabilities:**
- ❌ Web Search
- ✅ Code Interpreter & Data Analysis (content calendars, A/B trackers)
- ✅ Canvas
- ❌ Image Generation
**Knowledge:** upload ICP profiles, messaging framework, brand voice guide, content examples Denis likes
**Conversation Starters:**
```
Write me 3 cold email versions — I'll give you the ICP and goal
```
```
Build a content calendar — tell me the product and target audience
```
```
Rewrite this copy — 3 versions, sharper and more ICP-specific
```
```
Draft a LinkedIn thread — give me the topic and angle
```

---

#### GPT 5: Build Planner

**Name:** `Build Planner`
**Description:** `Turn ideas into feature specs and launch plans engineering can build from`
**Instructions:** paste `GPT_05_Build_Planner.md` contents
**Capabilities:**
- ❌ Web Search
- ✅ Code Interpreter & Data Analysis (sprint plans, roadmaps, effort matrices)
- ✅ Canvas
- ❌ Image Generation
**Knowledge:** upload tech stack doc, current roadmap
**Conversation Starters:**
```
Turn this idea into a build plan — I'll describe what we want to ship
```
```
Write a feature spec for engineering — here's the user problem
```
```
Plan our launch — product + marketing + engineering aligned
```
```
Prioritize my roadmap — give me an effort/impact matrix
```

---

#### GPT 6: Landing Builder

**Name:** `Landing Builder`
**Description:** `Complete landing page copy — every section written, scored, and ready to paste. Includes visual mockups.`
**Instructions:** paste `GPT_06_Landing_Builder.md` contents
**Capabilities:**
- ❌ Web Search
- ✅ Code Interpreter & Data Analysis (page scorecard, A/B test plan)
- ✅ Canvas
- ✅ Image Generation (hero mockups, section layouts)
**Knowledge:** upload ICP profiles, messaging framework, brand colors/fonts
**Conversation Starters:**
```
Build me a full landing page — I'll give you product, ICP, and CTA
```
```
Write every section from hero to footer — ready to paste into Webflow
```
```
Generate a visual mockup of my hero section
```
```
Score my existing landing page — tell me what to fix first
```

---

### ChatGPT Projects — One Per Product

**chatgpt.com → Projects → New Project**

Each product gets its own project. Inside:
- Upload: ICP profiles, messaging framework, QUICK_START.md
- Custom Instructions: paste the project template from `CHATGPT_PROJECTS_AND_TASKS_v1.0.md`
- Enable Memory: seed it in first session

GPTs run inside the project — they inherit file context.

Full setup: see `CHATGPT_PROJECTS_AND_TASKS_v1.0.md`

---

### Scheduled Tasks — Set Up Once

**chatgpt.com → Scheduled tasks → New task**

| Task | Schedule | Time |
|------|---------|------|
| Weekly Content Brief | Every Monday | 9:00 AM |
| Monthly ICP Refresh | 1st Monday/month | 8:00 AM |
| Friday Campaign Check | Every Friday | 5:00 PM |
| Launch Countdown | One-time per launch | T-7 days |

Full prompts: see `CHATGPT_PROJECTS_AND_TASKS_v1.0.md`

---

## PART 3 — THE DAILY WORKFLOW

```
1. Open Claude.ai → Marketing OS Project
   Click a Conversation Starter or type your request
   → Claude reads memory + knowledge files automatically

2. Claude generates brief in Artifact (side panel)
   → Click Copy button (top right of artifact)

3. Open ChatGPT → correct GPT (inside your product Project)
   → Paste brief
   → GPT executes immediately, opens Canvas

4. Canvas output is paste-ready
   → Edit inline if needed (canvas editing)
   → Copy from canvas

5. Return to Claude → paste output
   → "Evaluate this"
   → Claude opens Evaluation artifact
   → ≥7: ship | <7: revision brief in same artifact → back to ChatGPT

Total: brief generation ~2 min | execution ~3-5 min | evaluation ~1 min
```

---

## PART 4 — CANVAS WORKFLOW DETAIL

Canvas is ChatGPT's editing environment. Once open:

| Action | How |
|--------|-----|
| Edit directly | Click any text in canvas |
| Accept GPT suggestion | Click "Accept" on highlighted suggest edit |
| Reject GPT suggestion | Click "Reject" |
| Request iteration | Type in chat: "V2 — make the headline more direct" |
| See V1 vs V2 | Click history icon (top right of canvas) |
| Copy full content | Click copy icon |
| Export | Right-click → copy / download as .md or .txt |

GPT adds inline comments to flag weak sections. Review all comments before copying.

---

## PART 5 — TROUBLESHOOTING

**Claude writes content instead of a brief**
→ "Don't write this yourself. Generate the brief for [GPT name]."

**Claude doesn't open artifact**
→ "Open this as an artifact" or — check Custom Style is active in this project

**Memory not persisting between Claude sessions**
→ Memory is per-account, not per-project. If starting fresh: "Remember: [context]". Check Settings → Memory to confirm it's on.

**ChatGPT GPT re-asks questions**
→ Add to top of paste: "Execute immediately, no clarifying questions."

**Canvas not opening in ChatGPT GPT**
→ Confirm Canvas is enabled in GPT Settings. Or type: "Open canvas and put the output there."

**Code Interpreter not producing CSV**
→ Explicitly ask: "Build this as a table in Code Interpreter and offer CSV export."

**Image Generation not working in Landing Builder**
→ Confirm Image Generation capability is enabled in GPT Settings. Then: "Generate a hero section mockup using DALL-E."

**Scheduled task fired but nothing happened**
→ Scheduled tasks require ChatGPT to be logged in when they fire on web. If on mobile, ensure notifications are on. Check Scheduled Tasks → History.

---

*Marketing Hub Setup Guide v1.3 · Full Platform UI/UX · 2026-04-07*


---

# Marketing Hub — ChatGPT Projects & Scheduled Tasks Setup
**Version:** 1.0 | **Date:** 2026-04-07
**Purpose:** Persistent context + automated marketing triggers

---

## WHY CHATGPT PROJECTS

ChatGPT Projects give you:
- Persistent custom instructions per product (survive between sessions)
- Memory tied to the project (ChatGPT remembers what you told it)
- File attachments that persist (ICP profiles, briefs, brand docs)
- Clean separation between products / clients

Each product you're marketing gets its own ChatGPT Project. GPTs run inside the project — they inherit its context.

---

## PROJECT SETUP — ONE PER PRODUCT

### Step 1: Create the Project

1. **chatgpt.com → Projects → New Project**
2. Name: `[Product Name] — Marketing`
3. Description: `Marketing context for [product]. Uses Marketing OS brief system from Claude.`

### Step 2: Upload Files to Project

Upload these to the Project (not to individual GPTs — Project files are available to all GPTs within it):

| File | Source | When to update |
|------|--------|---------------|
| ICP profiles | Output from ICP Builder | When ICP changes or new segment added |
| Messaging framework | Output from Messaging Builder | When positioning changes |
| QUICK_START.md | Marketing Hub bundle | One time at setup |

### Step 3: Set Project Custom Instructions

In Project → Instructions, paste:

```
This is the marketing workspace for [Product Name].

Product: [1-2 sentence description]
Primary ICP: [role, company size, main pain]
Secondary ICP: [if applicable]
Stage: [pre-launch / early traction / growth / scale]
Current focus: [channel or campaign Denis is running now]

When I paste a 📋 BRIEF FOR [GPT NAME]:
- Execute the brief immediately
- Do not ask me to clarify anything already in the brief
- Open canvas for all outputs
- End with "➡️ Bring this back to Claude for evaluation"

GPTs I use in this project:
- ICP Builder → customer research + profiles
- Messaging Builder → positioning + copy scoring
- Funnel Builder → funnel design + conversion audit
- Content Builder → all copy execution
- Build Planner → specs + launch plans
- Landing Builder → landing page copy + mockups
```

### Step 4: Enable Memory in the Project

ChatGPT Projects have memory. After a few sessions, ChatGPT will remember:
- Which ICP is the current focus
- What campaigns are running
- Denis's tone preferences
- What's been tried and discarded

To seed memory manually: start a conversation in the project and say:
```
Remember: My primary ICP is [description]. 
Current campaign: [what I'm running].
Preferred tone: direct, no filler.
I always use the 📋 BRIEF format from Claude.
```

---

## SCHEDULED TASKS SETUP

ChatGPT Scheduled Tasks run automated prompts on a schedule. Up to 10 active tasks.

Go to: **chatgpt.com → bottom left → Scheduled tasks → New task**

### Task 1: Weekly Content Brief Reminder (Every Monday, 9am)

**Name:** `Weekly Content Brief`
**Schedule:** Every Monday at 9:00 AM
**Prompt:**
```
It's Monday. Based on what I've been working on, remind me:
1. What content pieces are in progress from last week?
2. What should I brief Claude to plan this week?
3. What's the one highest-leverage content move I should make this week?

Keep it to 5 lines max. I'll take it to Claude for the actual brief.
```

### Task 2: ICP Research Refresh (Every 4 Weeks, Monday)

**Name:** `Monthly ICP Refresh`
**Schedule:** 1st Monday of each month, 8:00 AM
**Prompt:**
```
It's been a month. Do a quick search:
1. What are people saying about [pain point / product category] on Reddit and G2 this month?
2. Any new competitor moves or messaging shifts?
3. Is the ICP language I'm using still current?

Give me 3 bullet points I can bring to Claude to update my ICP brief.
```
**Capabilities needed:** Web Search ON (use ICP Builder GPT for this task, or enable web search in the project)

### Task 3: Campaign Status Ping (Every Friday, 5pm)

**Name:** `Friday Campaign Check`
**Schedule:** Every Friday at 5:00 PM
**Prompt:**
```
Friday check-in. What did I work on in Marketing OS this week?
Give me:
- Campaigns started
- Content shipped
- Anything still in evaluation with Claude
- One thing to follow up on Monday

3-5 bullet points. Quick.
```

### Task 4: Launch Countdown (One-time, set per launch)

**Name:** `[Launch Name] T-7 Check`
**Schedule:** One-time, 7 days before launch date
**Prompt:**
```
Launch is in 7 days. Run through the launch checklist:
- Landing page: ready?
- Email sequence: briefed to Content Builder?
- ICP research: done?
- Messaging validated by Claude?
- Anything still outstanding?

Tell me what's missing. I'll take it to Claude immediately.
```

---

## PROJECT TEMPLATE LIBRARY

Keep these in your ChatGPT Project as pinned files or in the Project's knowledge:

### Brief Templates (reference card)

```
━━━ CONTENT BUILDER ━━━
📋 BRIEF FOR CONTENT BUILDER
Project: | ICP: | Goal:
Content type: | Length: | Versions: 3
Key messages: | Objections: | Proof:
Tone: | Format:

━━━ ICP BUILDER ━━━
📋 BRIEF FOR ICP BUILDER
Project: | Market: | Goal:
Depth: | Pull from: | Output:

━━━ LANDING BUILDER ━━━
📋 BRIEF FOR LANDING BUILDER
Project: | ICP: | Primary CTA:
Sections: | Proof: | Tone:
Visual mockup: yes/no
```

Save this as `BRIEF_TEMPLATES.md` in Project knowledge. When you need to self-generate a brief without Claude, use this reference.

---

## WHAT LIVES WHERE

| Content | Lives in |
|---------|---------|
| ICP research output | ChatGPT Project files |
| Messaging framework | ChatGPT Project files |
| Current brief from Claude | Chat — paste and execute |
| Evaluated content | Return to Claude in chat |
| Content calendar | Code Interpreter → CSV → save locally |
| A/B test tracker | Code Interpreter → CSV → save locally |
| Scheduled triggers | ChatGPT Scheduled Tasks |
| Strategy and context | Claude.ai Project (Marketing OS) |

---

## TROUBLESHOOTING

**ChatGPT forgot my ICP between sessions**
→ Memory is active in Projects. Refresh it: open the project, say "Remember: My ICP is [description]. Confirm you have this."

**Scheduled task ran but used wrong GPT**
→ Scheduled tasks run in the default ChatGPT, not inside a GPT. For research tasks, set ICP Builder as the active GPT when the task fires, or paste the task output into ICP Builder manually.

**File I uploaded to project isn't being referenced**
→ Explicitly reference it: "Using the ICP profile I uploaded, build this brief." ChatGPT doesn't auto-read files unless prompted.

**Task limit reached (10 active)**
→ Delete completed one-time tasks (launch countdowns). Keep: weekly content brief, monthly ICP refresh, Friday check-in. Use remaining slots for active launch countdowns.

---

*ChatGPT Projects & Scheduled Tasks v1.0 · Marketing Hub · 2026-04-07*


---

# Marketing Hub — Quick Start
**v1.3 · 2026-04-07 · Brain/Execution Architecture**

---

## The System in 30 Seconds

**Claude.ai = Brain.** Strategy, context, brief generation, quality evaluation.
**ChatGPT = Engine.** All content writing, research, and execution.

```
You → Claude → Brief → ChatGPT → Output → Claude → Ship or Revise
```

---

## Platform Setup (Do This Once)

### Claude.ai
1. Create Project: `Marketing OS`
2. Upload to Knowledge: `CONTEXT_Product.md`, `CONTEXT_Technical.md`, `MARKETING_OS_CLAUDE_v1.3_2026-04-07.md`
3. Custom Instructions: paste from SetupGuide Part 1, Step 3
4. Conversation starters: `🧠 Plan my next campaign` · `📊 Evaluate this output` · `🗺️ Build my GTM strategy` · `🔄 Update my project context`

### ChatGPT (6 GPTs — all private)

| GPT | Instructions File | Web Browsing |
|-----|-------------------|--------------|
| ICP Builder | `GPT_01_ICP_Builder.md` | ✅ ON |
| Messaging Builder | `GPT_02_Messaging_Builder.md` | ❌ OFF |
| Funnel Builder | `GPT_03_Funnel_Builder.md` | ❌ OFF |
| Content Builder | `GPT_04_Content_Builder.md` | ❌ OFF |
| Build Planner | `GPT_05_Build_Planner.md` | ❌ OFF |
| Landing Builder | `GPT_06_Landing_Builder.md` | ❌ OFF |

Full setup instructions: `MARKETING_OS_SetupGuide_v1.2_2026-04-07.md`

---

## Daily Loop

```
1. Tell Claude what you need
   → "Plan a cold email campaign for SaaS founders"

2. Claude routes and generates a brief
   → 📋 BRIEF FOR CONTENT BUILDER
     Project: ... | ICP: SaaS founders | Goal: 5-email sequence
     Format: email sequence | Tone: direct | Versions: 3

3. Paste brief into the right ChatGPT GPT
   → Content Builder executes immediately

4. Paste output back into Claude
   → "Evaluate this"

5. Claude scores it
   → ≥7: ship | <7: Claude writes revision brief → back to ChatGPT
```

---

## What to Ask Claude

| You need | Say to Claude |
|----------|---------------|
| New campaign idea | "Plan my next campaign for [ICP]" |
| Evaluate content | "Evaluate this" + paste ChatGPT output |
| ICP research | "Build an ICP research brief" |
| Positioning review | "Score this copy" + paste copy |
| GTM plan | "Build my GTM strategy for [launch]" |
| Update context | "Update my project context — [changes]" |

## What to Send to ChatGPT

| Content type | GPT to use |
|--------------|------------|
| ICP profiles, pain points, web research | ICP Builder |
| Positioning, copy scoring, rewrites | Messaging Builder |
| Funnel design, conversion audit | Funnel Builder |
| Emails, ads, blog, LinkedIn, social | Content Builder |
| Feature specs, launch plans | Build Planner |
| Full landing pages | Landing Builder |

---

## Claude Quality Evaluation

Every output Claude evaluates gets scored on 4 dimensions:

```
📊 EVALUATION
Score: [X]/10
ICP Match: [X]/10
Messaging: [X]/10
Differentiation: [X]/10
Objection Handling: [X]/10
Verdict: SHIP / REVISE
```

**≥7 → ship. <7 → Claude writes revision brief → back to ChatGPT.**

---

## Token Budget

| Task | Claude tokens |
|------|---------------|
| Brief generation | ~300–500 |
| Evaluation | ~200–400 |
| Strategy session | ~1,000–2,000 |
| Extended thinking (rare) | ~5,000–8,000 |
| **Monthly total** | **~8–15K** |

Extended thinking: use only when explicitly requested ("Use deep thinking"). Max 2–3x/month.

---

## Files in This Bundle

```
Claude Files:
  MARKETING_OS_CLAUDE_v1.3_2026-04-07.md    ← Claude's brain instructions
  CONTEXT_Product.md                          ← Product context (fill in)
  CONTEXT_Technical.md                        ← Stack + integrations (fill in)
  IMPLEMENTATION.md                           ← GTM strategy

ChatGPT GPT Files:
  GPT_01_ICP_Builder.md
  GPT_02_Messaging_Builder.md
  GPT_03_Funnel_Builder.md
  GPT_04_Content_Builder.md                   ← Primary execution engine
  GPT_05_Build_Planner.md
  GPT_06_Landing_Builder.md

ChatGPT Project Files:
  PROJECT_01 through PROJECT_05               ← Per-product context files

Setup & Reference:
  MARKETING_OS_SetupGuide_v1.2_2026-04-07.md ← Full setup instructions
  QUICK_START.md                              ← This file

Consolidated (for Claude.ai upload):
  CONTEXT_MarketingOS.md                      ← Claude instructions + context
  CONTEXT_ChatGPT_GPTs.md                     ← All 6 GPT instructions
  IMPLEMENTATION_GTM.md                       ← GTM + product + technical
```

---

*Marketing Hub Quick Start v1.3 · 2026-04-07*
