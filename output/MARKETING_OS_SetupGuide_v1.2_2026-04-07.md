# Marketing Hub — Setup Guide
**Version:** 1.2 | **Date:** 2026-04-07 | **Status:** Production
**Architecture:** Claude = Brain | ChatGPT = Execution Engine

---

## What You're Building

A two-platform marketing system where Claude.ai handles strategy and coordination, and ChatGPT handles all content generation and research. You get the strategic intelligence of Claude at low token cost + the execution throughput of ChatGPT at a flat monthly rate.

```
DAILY WORKFLOW

Denis
  │
  ▼
Claude.ai Project (Marketing OS)
  │  Strategy · Context · Brief Generation · Quality Evaluation
  │
  ├─ generates "📋 BRIEF FOR [GPT]"
  │
  ▼
ChatGPT GPT (ICP Builder / Content Builder / etc.)
  │  Executes brief · Writes content · Pulls web data
  │
  ├─ returns output to Denis
  │
  ▼
Denis pastes output back into Claude
  │
  ▼
Claude evaluates · scores 1–10 · writes revision brief if <7
```

**Token cost:** Claude ~8–15K tokens/month (brain only) | ChatGPT: flat ~$20/month (execution)

---

## PART 1 — CLAUDE.AI SETUP

### Step 1: Create the Project

1. Go to **claude.ai → Projects → New Project**
2. Name: `Marketing OS`
3. Description: `Marketing brain — strategy, briefs, evaluation`

### Step 2: Upload Project Knowledge Files

Upload these files to **Project Knowledge** (drag & drop all at once):

```
CONTEXT_Product.md         ← Your product context
CONTEXT_Technical.md       ← Stack + integrations  
IMPLEMENTATION.md          ← GTM strategy
MARKETING_OS_CLAUDE_v1.3_2026-04-07.md   ← Claude's instructions
```

> **How to upload:** Project → Knowledge → Add content → Upload files

### Step 3: Set Custom Instructions

Go to **Project → Settings → Custom Instructions**. Paste:

```
You are Marketing OS — the strategic brain of Denis's marketing system.

YOUR ROLE:
- Maintain full product/ICP/campaign context
- Generate structured briefs for ChatGPT execution GPTs
- Evaluate returned outputs and score 1–10
- Route requests to the correct ChatGPT GPT
- Never write final marketing copy yourself — generate briefs for ChatGPT

ROUTING:
- ICP research → Brief for ICP Builder
- Positioning / copy scoring → Brief for Messaging Builder  
- Funnel design / conversion → Brief for Funnel Builder
- Emails / ads / blog / social → Brief for Content Builder
- Feature specs / launch plans → Brief for Build Planner
- Landing pages → Brief for Landing Builder

BRIEF FORMAT (always use this structure):
📋 BRIEF FOR [GPT NAME]
Project: [name] | ICP: [description] | Goal: [what to produce]
[GPT-specific fields]
Tone: [direct/warm/authoritative] | Versions: [number]

EVALUATION FORMAT (when Denis returns ChatGPT output):
📊 EVALUATION
Score: [X]/10
ICP Match: [X]/10 — [reason]
Messaging: [X]/10 — [reason]  
Differentiation: [X]/10 — [reason]
Objection Handling: [X]/10 — [reason]
Verdict: SHIP / REVISE
[If REVISE: write revision brief immediately]
```

### Step 4: Set Conversation Starters

Go to **Project → Settings → Conversation Starters**. Add these 4:

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

### Step 5: Configure Style

Go to **Profile → Settings → Custom Instructions → How should Claude respond?**

```
Direct and precise. No preamble. No "Great question!" 
Lead with action or the answer.
For briefs: use the standard 📋 BRIEF format.
For evaluations: use the standard 📊 EVALUATION format.
Open an artifact for any document > 10 lines.
```

### Step 6: Extended Thinking

Extended thinking is available but **expensive**. Claude will use it only when Denis explicitly requests it:

- Allowed uses: Full ICP research from scratch, complete GTM strategy
- Trigger phrase: "Use deep thinking for this"
- Limit: Max 2–3 times/month
- Default: OFF (standard mode for all briefs and evaluations)

---

## PART 2 — CHATGPT SETUP

### Overview: 6 Execution GPTs

| # | GPT Name | Role | Web Browsing |
|---|----------|------|--------------|
| 1 | ICP Builder | Customer research · profiles · pain points | ✅ ON |
| 2 | Messaging Builder | Positioning · copy scoring · rewrites | ❌ OFF |
| 3 | Funnel Builder | Funnel design · friction mapping | ❌ OFF |
| 4 | Content Builder | Emails · ads · blog · social · sequences | ❌ OFF |
| 5 | Build Planner | Feature specs · launch plans | ❌ OFF |
| 6 | Landing Builder | Full landing page generation + scoring | ❌ OFF |

### Step 1: Access GPT Builder

Go to **chatgpt.com → Explore GPTs → Create a GPT** (requires ChatGPT Plus)

### Step 2: Build Each GPT

For each of the 6 GPTs below:

1. Click **Create a GPT → Configure**
2. Set **Name** and **Description** as shown
3. Set **Instructions**: paste the full contents of the corresponding `.md` file from the ChatGPT folder
4. Set **Conversation Starters**: copy the 4 starters from that file
5. Set **Capabilities**: enable/disable Web Browsing per the table above
6. Set **Canvas**: leave on (all GPTs auto-open canvas for 15+ line outputs)
7. Click **Save → Only me** (private GPTs)

---

### GPT 1: ICP Builder

**Name:** `ICP Builder`
**Description:** `Deep customer research — ICPs, pain points, buying triggers, real quotes from web`
**Instructions file:** `GPT_01_ICP_Builder.md`
**Web Browsing:** ON
**Conversation starters:**
```
Build my full ICP — I'll tell you the product and market
```
```
Find real customer pain points — pull from G2, Reddit, forums
```
```
Segment my audience — which ICP should I target first?
```
```
What does my ICP actually say about this problem?
```

---

### GPT 2: Messaging Builder

**Name:** `Messaging Builder`
**Description:** `Sharp positioning from scratch — or score and rebuild existing copy`
**Instructions file:** `GPT_02_Messaging_Builder.md`
**Web Browsing:** OFF
**Conversation starters:**
```
Build my positioning — here's what my product does and who it's for
```
```
Score this copy — what's weak and how do I fix it?
```
```
Write 3 versions of this headline — sharper, bolder, more specific
```
```
Punch up this cold email — give me 3 rewritten versions
```

---

### GPT 3: Funnel Builder

**Name:** `Funnel Builder`
**Description:** `Design full funnels, find conversion leaks, map friction at every stage`
**Instructions file:** `GPT_03_Funnel_Builder.md`
**Web Browsing:** OFF
**Conversation starters:**
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

---

### GPT 4: Content Builder

**Name:** `Content Builder`
**Description:** `Primary execution engine — emails, ads, blog posts, LinkedIn, sequences, newsletters`
**Instructions file:** `GPT_04_Content_Builder.md`
**Web Browsing:** OFF
**Conversation starters:**
```
Tighten this copy — make it 30% shorter without losing impact
```
```
Rewrite this for my ICP — I'll tell you who they are
```
```
Write me a content piece — blog post, email, LinkedIn thread, or ad
```
```
Give me 3 headline versions — bolder, clearer, more specific
```

---

### GPT 5: Build Planner

**Name:** `Build Planner`
**Description:** `Turn ideas into build plans — feature specs, launch plans, product-marketing alignment`
**Instructions file:** `GPT_05_Build_Planner.md`
**Web Browsing:** OFF
**Conversation starters:**
```
Turn this idea into a build plan — I'll describe what we want to ship
```
```
Write a feature spec for engineering — here's the user problem
```
```
Plan our launch — product + marketing + engineering, aligned
```
```
What should we build first? Help me prioritize the roadmap
```

---

### GPT 6: Landing Builder

**Name:** `Landing Builder`
**Description:** `Full landing page generation — every section written, scored, and ready to paste`
**Instructions file:** `GPT_06_Landing_Builder.md`
**Web Browsing:** OFF
**Conversation starters:**
```
Build me a landing page — I'll tell you the product and ICP
```
```
Write every section of my page — hero to footer, ready to paste
```
```
Critique my existing landing page — score it and rewrite the weak sections
```
```
Give me 3 hero headline options — then build out the strongest one
```

---

### Step 3: Set Up ChatGPT Projects (Optional but Recommended)

Projects in ChatGPT persist context across conversations. Create one per product/campaign.

1. **chatgpt.com → Projects → New Project**
2. Name: `[Product Name] Marketing`
3. Upload relevant context files from your Documentation Builder output
4. Use the GPTs above within this project for persistent context

---

## PART 3 — THE DAILY WORKFLOW

### Standard Operation (5 steps)

```
1. Open Claude.ai → Marketing OS project
   Tell Claude what you need ("Plan a cold email campaign for [ICP]")

2. Claude generates a structured brief:
   📋 BRIEF FOR CONTENT BUILDER
   Project: [name] | ICP: [description] | Goal: cold email sequence
   Format: 5-email sequence | Tone: direct | Versions: 3

3. Copy the brief → Open ChatGPT → Open Content Builder GPT
   Paste the brief. ChatGPT executes immediately (no re-clarifying).

4. ChatGPT returns scored output in canvas (paste-ready)
   Copy the output.

5. Return to Claude → Paste output
   "Evaluate this"
   Claude scores 1–10. If <7: revision brief generated immediately.
   If ≥7: ship it.
```

### What Goes to Claude (Brain Tasks)
- "What campaign should I run next?"
- "Evaluate this email sequence"
- "Build my ICP brief for the ICP Builder"
- "Score this positioning"
- "Plan the GTM for [feature]"

### What Goes to ChatGPT (Execution Tasks)
- Writing emails, ads, blog posts, LinkedIn threads
- Building landing page copy
- Deep ICP research from web (G2, Reddit, forums)
- Funnel mapping and friction analysis
- Feature specs and launch plans

---

## PART 4 — QUICK REFERENCE

### Brief Formats by GPT

**ICP Builder:**
```
📋 BRIEF FOR ICP BUILDER
Project: [name] | Market: [description] | Goal: [profile / pain points / segmentation]
Depth: [1 persona / full segmentation] | Web sources: [G2, Reddit, LinkedIn, forums]
```

**Messaging Builder:**
```
📋 BRIEF FOR MESSAGING BUILDER
Project: [name] | ICP: [description] | Goal: [build or score positioning]
Messaging pillars: [list] | Proof points: [list] | Competitors: [list]
```

**Funnel Builder:**
```
📋 BRIEF FOR FUNNEL BUILDER
Project: [name] | ICP: [description] | Goal: [design or audit]
Current funnel: [stages + known drop-offs] | Primary conversion: [action]
```

**Content Builder:**
```
📋 BRIEF FOR CONTENT BUILDER
Project: [name] | ICP: [description] | Goal: [what to produce]
Format: [email / sequence / ad / blog / thread / newsletter + length]
Messaging: [key messages] | Objections: [list] | Proof: [available]
Tone: [direct/warm/authoritative] | Versions: [number]
```

**Build Planner:**
```
📋 BRIEF FOR BUILD PLANNER
Project: [name] | Feature: [what we're building]
User: [who benefits + their context] | Goal: [success metric]
Scope: [MVP / full feature] | Ship target: [date or sprint]
```

**Landing Builder:**
```
📋 BRIEF FOR LANDING BUILDER
Project: [name] | ICP: [description] | Primary CTA: [action]
Sections: [which sections / full page] | Proof: [quote/stat/case study]
Messaging: [key messages] | Tone: [direct/warm/authoritative]
```

### Evaluation Rubric

| Score | Action |
|-------|--------|
| 9–10 | Ship immediately |
| 7–8 | Ship with minor edits |
| 5–6 | Revise — Claude writes revision brief |
| 1–4 | Rewrite — Claude writes new brief from scratch |

---

## PART 5 — TROUBLESHOOTING

**ChatGPT re-asks questions instead of executing the brief**
→ Add to the top of your paste: "Execute this brief immediately without asking clarifying questions."

**Claude writes content instead of generating a brief**
→ Say: "Don't write this yourself. Generate the brief for [GPT name]."

**Extended thinking turns on unexpectedly (high token use)**
→ Don't use phrases like "think deeply" or "analyze thoroughly" — these trigger thinking mode. Use "Use deep thinking" only when you explicitly want it.

**ICP Builder not finding web data**
→ Confirm Web Browsing is ON in GPT settings. Check with: "Search G2 reviews for [product category] — what do users complain about?"

**Canvas not opening in ChatGPT**
→ All GPTs auto-open canvas for outputs >15 lines. If it doesn't: type "Open canvas and rewrite this" in the same conversation.

---

*Marketing Hub Setup Guide v1.2 · Brain/Execution Architecture · 2026-04-07*
