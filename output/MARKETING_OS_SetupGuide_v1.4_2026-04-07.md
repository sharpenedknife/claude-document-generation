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
