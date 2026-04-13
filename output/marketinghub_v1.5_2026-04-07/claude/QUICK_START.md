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
