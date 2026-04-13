# Marketing Hub — Full Setup & Reference
**v1.6 · 2026-04-07**
---
# Marketing Hub — Setup Guide
**Version:** 1.4 | **Date:** 2026-04-07
**Architecture:** Claude = Brain + HTML Production | ChatGPT = Research + First Drafts

---

## How It Works

```
Denis → Claude (strategy + brief)
  → ChatGPT GPT (research or rough draft — cheap, fast)
  → Denis pastes back to Claude
  → Claude evaluates + upgrades + builds HTML artifact if needed
```

Claude holds all context. ChatGPT GPTs are stateless — every brief from Claude contains everything they need. **One ChatGPT Project: "Marketing OS" — used for all products.** Build the 6 GPTs once inside it, use them for any product forever. No new project per product, ever.

---

## PART 1 — CLAUDE.AI SETUP (one-time)

### Features being configured

| Feature | Where | What it does |
|---|---|---|
| Project | Projects → New | Persistent workspace, 200K context |
| Knowledge files | Project → Knowledge | Product + ICP context always loaded |
| Custom Instructions | Project → Settings | Brain role + HTML production rules |
| Conversation Starters | Project → Settings | 4 clickable buttons |
| Custom Style | Profile → Styles | Response format baked in permanently |
| Memory | Automatic | ICP, campaigns, preferences across sessions |
| Artifacts | Automatic | Structured output in side panel — HTML or Markdown |

---

### Step 1: Create the Project

**claude.ai → Projects → New Project**
- Name: `Marketing OS`
- Description: `Marketing brain — strategy, briefs, evaluation, HTML production`

---

### Step 2: Upload Knowledge Files

**Project → Knowledge → Add content → Upload files**

Upload at minimum:
```
MARKETING_OS_CLAUDE_v1.6_2026-04-07.md   ← Claude's instructions (required)
```

**Product context comes from Documentation Builder output.** When you document a product using Documentation Builder, it generates `CONTEXT_Product.md` and `CONTEXT_Technical.md` — upload those to this project's Knowledge. That's the only per-product step on Claude.

Until you have Documentation Builder output: tell Claude your product context in the first session ("Remember: product is X, ICP is Y") — it will hold it in memory.

---

### Step 3: Custom Instructions

**Project → Settings → Custom Instructions** — paste:

```
You are Marketing OS — the strategic brain and HTML production engine of Denis's marketing system.

ARTIFACT RULE: Open an artifact for ANY output ≥10 lines.
- Briefs → Markdown artifact
- HTML pages → HTML artifact
- Evaluations → Markdown artifact

DO NOT write raw text copy (emails, ads, posts) — generate briefs for ChatGPT.
EXCEPTION: If Denis pastes a ChatGPT draft and asks to upgrade it — rewrite it in a Markdown artifact.
HTML PAGES: When Denis says "build me a landing page" or "production page" — build a complete responsive HTML artifact, no external dependencies.

See uploaded MARKETING_OS_CLAUDE_v1.6 for full routing table, brief formats, and evaluation format.
```

---

### Step 4: Conversation Starters

**Project → Settings → Conversation Starters** — add exactly:

```
🧠 Plan my next campaign
```
```
📊 Evaluate this output
```
```
🏗️ Build me a landing page
```
```
🔄 Update my project context
```

---

### Step 5: Custom Style

**Profile → Styles → Create Style**
Name: `Marketing OS`

Paste into instructions:
```
Direct, no preamble. Lead with the action or answer.
Never: "Great question", "Absolutely", "Certainly".
Output ≥10 lines → open artifact (HTML or Markdown).
Briefs: use 📋 BRIEF format with dividers.
Evaluations: use 📊 EVALUATION format, quote failing lines.
HTML pages: inline CSS, responsive, self-contained, commented sections.
Tone: confident, precise, marketing-literate. No hedging without resolution.
```

Activate this style in the Marketing OS project. It applies to all sessions automatically.

---

### Step 6: Memory

Memory is automatic. Seed it in your first session:
```
Remember: Product = [name]. Primary ICP = [role, company, pain].
Current campaign = [what I'm running]. Format preference = artifact for everything structured.
```

Check anytime: "What do you remember about my current product and campaigns?"

---

## PART 2 — CHATGPT SETUP (one-time)

**One project. Six GPTs inside it. Done forever.**

Create one ChatGPT Project called "Marketing OS". Build all 6 GPTs inside it. Never create another project. Context comes from Claude's brief every time — GPTs need no product-specific configuration.

### Step 0: Create the single Marketing OS Project

**chatgpt.com → Projects → New Project**
- Name: `Marketing OS`
- Instructions: `Marketing execution workspace. I use Claude (Marketing OS project) as my brain — it sends structured briefs here. All 6 GPTs in this project execute those briefs.`
- Upload nothing yet — product context comes from Documentation Builder output when ready.

Now build all 6 GPTs inside this project.

---

### How to build each GPT

**chatgpt.com → [inside Marketing OS project] → Explore GPTs → Create → Configure**

For each:
1. Set Name and Description as shown
2. Instructions: paste the contents of the `.md` file exactly
3. Capabilities: enable only what's listed
4. Conversation Starters: add the 4 shown
5. Save → Only me (private)

---

### GPT 1: ICP Builder

**Name:** `ICP Builder`
**Description:** `Deep customer research — ICPs, pain points, real quotes from G2, Reddit, forums`
**Instructions file:** `GPT_01_ICP_Builder.md`
**Enable:** Web Search ✅ · Code Interpreter ✅ · Canvas ✅ · Image Generation ❌

**Conversation Starters:**
```
Build my full ICP — I'll give you the product and target market
```
```
Find real customer pain points — search G2, Reddit, forums now
```
```
Segment my audience — which ICP should I target first?
```
```
What does my ICP say about this problem? Pull real quotes.
```

---

### GPT 2: Messaging Builder

**Name:** `Messaging Builder`
**Description:** `Sharp positioning and copy scoring — build from scratch or critique what you have`
**Instructions file:** `GPT_02_Messaging_Builder.md`
**Enable:** Web Search ❌ · Code Interpreter ✅ · Canvas ✅ · Image Generation ❌

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
Rewrite this cold email — 3 versions with different angles
```

---

### GPT 3: Funnel Builder

**Name:** `Funnel Builder`
**Description:** `Design funnels, find conversion leaks, benchmark against competitors`
**Instructions file:** `GPT_03_Funnel_Builder.md`
**Enable:** Web Search ✅ · Code Interpreter ✅ · Canvas ✅ · Image Generation ❌

**Conversation Starters:**
```
Design my full funnel — from first touchpoint to first dollar
```
```
Find my biggest conversion leak — where am I losing people?
```
```
Research what competitors do at this funnel stage
```
```
Model the revenue impact of fixing my drop-off
```

---

### GPT 4: Content Builder

**Name:** `Content Builder`
**Description:** `Fast first drafts — emails, ads, LinkedIn, blog, social. 3 versions, paste-ready.`
**Instructions file:** `GPT_04_Content_Builder.md`
**Enable:** Web Search ❌ · Code Interpreter ✅ · Canvas ✅ · Image Generation ❌

**Conversation Starters:**
```
Write me 3 cold email drafts — I'll give you the ICP and goal
```
```
Draft a LinkedIn thread — give me the topic and angle
```
```
Build a content calendar — I'll tell you the product and audience
```
```
Write 3 ad headline options for this campaign
```

---

### GPT 5: Build Planner

**Name:** `Build Planner`
**Description:** `Feature specs and launch plans engineering can build from`
**Instructions file:** `GPT_05_Build_Planner.md`
**Enable:** Web Search ❌ · Code Interpreter ✅ · Canvas ✅ · Image Generation ❌

**Conversation Starters:**
```
Turn this idea into a build plan — describe what we want to ship
```
```
Write a feature spec — here's the user problem
```
```
Plan our launch — product + marketing + engineering aligned
```
```
Prioritize my roadmap — effort/impact matrix
```

---

### GPT 6: Landing Builder

**Name:** `Landing Builder`
**Description:** `Fast landing page drafts — copy for every section, scored, ready for Claude to build`
**Instructions file:** `GPT_06_Landing_Builder.md`
**Enable:** Web Search ❌ · Code Interpreter ✅ · Canvas ✅ · Image Generation ✅

**Conversation Starters:**
```
Draft a landing page — I'll give you product, ICP, and CTA
```
```
Write every section from hero to footer
```
```
Generate a hero section mockup
```
```
Score my existing landing page and rewrite the weak sections
```

---

## PART 3 — DAILY WORKFLOW

### Standard: Brief → Draft → Evaluate → Ship

```
1. Open Claude → Marketing OS project
   Click a starter or type your request
   
2. Claude generates brief → Markdown artifact → copy it

3. Paste into the right ChatGPT GPT
   GPT drafts fast in canvas

4. Copy from canvas → paste back into Claude
   "Evaluate this"

5. Claude scores it:
   ≥7 → ship
   <7 → revision brief → back to ChatGPT
```

### Production: Brief → Draft → Claude builds HTML

```
1. Claude generates Landing Builder brief
2. Landing Builder GPT drafts copy fast in canvas
3. Denis pastes copy back into Claude
4. Claude: "Build me a landing page from this draft"
   → Full responsive HTML artifact
   → Shareable link Denis can preview and hand to developer
```

### Express (skip ChatGPT): Claude builds page directly

```
Denis: "🏗️ Build me a landing page" + pastes product context
Claude: builds HTML artifact directly
(higher token cost, but fastest path to a shareable production page)
```

---

## PART 4 — WHAT LIVES WHERE

| Content | Platform |
|---|---|
| Product/ICP context | Claude Project Knowledge |
| Campaign strategy | Claude memory + artifact |
| Briefs | Claude → Markdown artifact |
| First-draft copy | ChatGPT canvas |
| ICP research output | ChatGPT canvas |
| Evaluations | Claude → Markdown artifact |
| Production HTML pages | Claude → HTML artifact (shareable link) |
| Content calendars / A/B trackers | ChatGPT Code Interpreter → CSV |

---

## PART 5 — TROUBLESHOOTING

**Claude writes copy instead of a brief**
→ "Don't write it — generate the brief for [GPT]."

**Claude doesn't open artifact**
→ "Open this as an artifact." Or check that your custom style is active in the project.

**ChatGPT GPT re-asks questions**
→ Add at top of paste: "Execute immediately, no clarifying questions."

**Canvas doesn't open**
→ "Open canvas and put the output there."

**HTML artifact doesn't render**
→ It renders in the artifact side panel. Click the artifact tab if collapsed. Click "Preview" if showing code view.

**Want to switch products**
→ On Claude: upload the new product's CONTEXT_Product.md from Documentation Builder output. On ChatGPT: nothing — context comes from Claude's brief every time.

---

*Marketing Hub Setup Guide v1.4 · Claude Brain + HTML Production · No Per-Product ChatGPT Config · 2026-04-07*

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
