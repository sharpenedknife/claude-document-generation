# Marketing OS — Quick Reference
**Version:** 1.0 | **Date:** 2026-04-07 | **For:** Denis — solo marketing + outbound operator

---

## What Is This?

Marketing OS is a complete dual-platform marketing system running on **Claude.ai** (primary) and **ChatGPT** (supplementary). It covers full-funnel marketing from research to revenue:

```
Research & ICP → Positioning → Copy → Outbound → Content → Measurement
```

One system. Two platforms. 25+ specialized skills. All for solo use.

---

## Quick Start (5 Minutes)

### Claude (Primary)
1. Open **Marketing OS** project in Claude.ai
2. Click a conversation starter:
   - 🚀 **New project** → builds your ICP + messaging context
   - 📧 **Cold email** → writes campaign for your project
   - 📊 **Performance review** → analyzes metrics + recommends plays
   - ✍ **Copy** → landing page, email, or ad creative

### ChatGPT (Supplementary)
Open the right GPT for your task:
- **Research Architect** → market maps, ICP research, competitor analysis
- **Messaging Critic** → score and improve copy (1–10 rubric)
- **Funnel Builder** → design or audit your conversion funnel
- **Copy Rewriter** → 3-version rewrites with paste-ready code blocks
- **PRD Thinker** → feature specs and dev briefs (opens in canvas)

---

## How to Choose: Claude vs. ChatGPT

| What You're Doing | Use Claude | Use ChatGPT |
|------------------|-----------|------------|
| Deep research + ICP analysis | ✅ Extended thinking | ✓ Research Architect |
| Writing cold email campaigns | ✅ cold-email skill | ✓ Copy Rewriter |
| Editing existing copy inline | ✓ copy-editing | ✅ Copy Rewriter + Canvas |
| Landing page (write new) | ✅ copywriting skill (artifact) | ✓ |
| Scoring messaging (1–10) | ✓ | ✅ Messaging Critic |
| PRD / feature spec | ✓ | ✅ PRD Thinker + Canvas |
| Token budget control | ✅ Explicit | ✗ Not visible |
| Funnel design | ✓ | ✅ Funnel Builder + Canvas |

**Default rule:** Claude for strategy and orchestration. ChatGPT for specialized personas and canvas editing.

---

## Mode Commands (Claude Only)

Say these in any Claude conversation to switch context:

| Command | What It Does |
|---------|-------------|
| `research mode` | Deep analysis, extended thinking, no token limits |
| `campaign mode` | Batch outputs, strict 2.5K budget, speed-first |
| `review mode` | Score everything, suggest revisions |
| `quick mode` | Under 500 tokens, directional answers only |
| `planning mode` | Weekly/monthly cadence, roadmaps |
| `reset` | Clear context, return to default |

---

## Skill Map (Claude)

| Request | Skill | Tokens |
|---------|-------|--------|
| "research my market" | customer-research + competitive-analysis | 4–6K |
| "cold email campaign" | cold-email | 2–2.5K |
| "nurture sequence" | email-sequence | 1.5–2K |
| "landing page copy" | copywriting | 1.5–2K |
| "polish this copy" | copy-editing | 0.5–1K |
| "10 ad variations" | ad-creative | 1.5–2K |
| "content strategy" | content-strategy | 1–1.5K |
| "set up tracking" | analytics-tracking | 1–1.5K |
| "A/B test design" | ab-test-setup | 1–1.5K |
| "brand story" | brand-storytelling | 1–1.5K |

**Monthly budget:** 20–30K tokens

---

## Response Format (What You'll See in Claude)

```
🎯 [Skill being run]
⚡ [Token estimate]

[Output — in artifact if 10+ lines]

📊 Quality: [X]/10 — [one-line reason]
➡️ Next: [exact action you take]
```

**Emoji guide:**
- 🎯 What Claude is executing
- ⚡ Token cost estimate
- 📊 Quality score + reason
- ➡️ Your next action
- ⚠️ Warning (budget, missing context, assumption)
- ✅ Complete
- 🔄 Needs revision
- 📁 Open the artifact

---

## Project Context Files

Every project needs a `[ProjectName]_marketing.md` file with:
- **ICP** (who you're selling to)
- **Messaging pillars** (5 pillars: problem, solution, proof, outcome, movement)
- **Competitive positioning** (how you're different)
- **Channels** (where you're going to market)

**Create one:** Click "🚀 Start a new project" in Claude → answer 5 questions → get the file.

**Use it:** Every skill automatically references your project context.

**Update it:** After every campaign — log learnings, update winning angles.

---

## Quality Score System

After every output, Claude scores it:

```
Q1 ICP Match:         X/10
Q2 Messaging:         X/10
Q3 Differentiation:   X/10
Q4 Objections:        X/10
─────────────────────────
Average:              X/10
```

**Thresholds:**
- ≥ 7/10 → Ship it
- 5–6/10 → Ask for revision
- < 5/10 → Don't publish, rewrite

---

## Weekly Rhythm

**Monday (5 min):**
> "📊 Weekly check-in — which projects are active, what metrics came in?"

**Thursday (15 min):**
> "📊 Mid-week review [Project] — what's working, what should I test?"

**Friday (30 min):**
> "📅 Planning mode — plan next week for [Project]"

**Monthly (1 hour, last Friday):**
> "📋 Monthly review — analyze all campaigns, update project context, plan next month"

---

## File Structure (Claude Project)

```
Claude Project: Marketing OS
├── MARKETING_OS_CLAUDE_v1.1.md           ← Primary instructions
├── MARKETING_OS_SkillOrchestration.md    ← Skill routing
├── MARKETING_OS_KnowledgeStructure.md    ← Templates
├── MARKETING_OS_Instructions.md          ← Behavioral rules
├── MARKETING_OS_TokenOptimization.md     ← Budget config
├── MARKETING_OS_ProjectContext_Template.md ← Template per project
├── MARKETING_OS_Research_GTM_Framework.md ← Research guide
└── [ProjectName]_marketing.md            ← Per-project context (you create)
```

---

## File Structure (ChatGPT Projects)

```
ChatGPT Projects (5):
├── Marketing OS          ← Strategy + research
├── Content Engine        ← Content production
├── Funnel / CRO          ← Conversion optimization
├── Client Template       ← Per-client isolation
└── Coding / Product Dev  ← PRD + engineering

ChatGPT GPTs (5):
├── Research Architect    ← Market maps, ICP, competitor analysis
├── Messaging Critic      ← Score + improve copy (1–10)
├── Funnel Builder        ← Journey design + friction analysis
├── Copy Rewriter         ← 3-version rewrites + canvas editing
└── PRD Thinker           ← Feature specs + dev briefs
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Claude doesn't know my project | Add `[ProjectName]_marketing.md` to Project Knowledge |
| Conversation starters don't appear | Check you're on Pro/Team plan; verify Project Settings |
| Artifact doesn't open | Say "put that in an artifact" or ensure output is 10+ lines |
| Canvas won't open in ChatGPT | Say "use canvas for this" or verify GPT has canvas rule |
| Quality score below 7/10 | ICP is probably too vague — update project context |
| Tokens running high | Batch tasks, reuse context, skip draft polishing |

---

## Support

- **Reference:** MARKETING_OS_Instructions_v1.0.md (detailed rules)
- **Skills:** MARKETING_OS_SkillOrchestration_Matrix_v1.0.md (which skill for what)
- **Templates:** MARKETING_OS_KnowledgeStructure_v1.0.md
- **Budget:** MARKETING_OS_TokenOptimization_v1.0.md
- **Issues:** MARKETING_OS_tasks_v1.0.md (log bugs + improvement ideas here)

---

*Marketing OS v1.0 · Quick Reference · 2026-04-07*
*Solo marketing system: research → positioning → execution → measurement*
