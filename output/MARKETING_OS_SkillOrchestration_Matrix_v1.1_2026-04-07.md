# Marketing OS — Skill Orchestration Matrix
**Version:** 1.1 | **Date:** 2026-04-07
**Architecture:** 3-Tier — Claude Brain · Claude Skills · ChatGPT GPTs

---

## Three-Tier System

```
TIER 1 — CLAUDE BRAIN (always on)
  Strategy · Routing · Brief generation · HTML production · Evaluation
  Cost: ~300–8,000 tokens per task

TIER 2 — CLAUDE SKILLS (invoke on demand)
  Deep research · Specialized analysis · Growth design · Tracking setup
  Cost: ~1,000–3,000 tokens per skill
  Trigger: when Claude Skill quality > ChatGPT draft quality AND worth the tokens

TIER 3 — CHATGPT GPTs (default execution)
  ICP research · First drafts · Copy · Funnels · Specs · Landing page drafts
  Cost: flat ~$20/month regardless of usage
  Trigger: default for all execution tasks
```

**Decision rule:** If a task has a ChatGPT GPT — use it first. Use a Claude Skill only when the GPT output is insufficient after evaluation, or when the task requires Claude-level depth from the start (e.g., full competitive analysis for a new market).

---

## Tier 2 — Claude Skills: When to Invoke

| Claude Skill | Use When | Don't Use When | Cost |
|---|---|---|---|
| `customer-research` | Deep synthesis from interviews/transcripts Denis uploads; ICP Builder GPT returned thin data | Just need a quick ICP profile — use ICP Builder GPT | ~2–3K |
| `competitive-analysis` | Full market positioning analysis; entering new category | Quick competitor comparison — Messaging Builder handles | ~1.5–2K |
| `copywriting` | Upgrading ChatGPT draft to production quality in place | Starting from scratch — brief Content Builder first | ~1.5–2K |
| `copy-editing` | Final polish on production copy before publishing | Reviewing drafts — evaluate in Claude Brain first | ~0.5–1K |
| `cold-email` | Writing outbound sequences directly without a ChatGPT draft first | Denis has a Content Builder draft already | ~1.5–2K |
| `email-sequence` | Multi-touch lifecycle campaign design with timing logic | Single email — Content Builder handles | ~1.5–2K |
| `analytics-tracking` | Full tracking plan: GTM, events, dashboards | Already tracking and just need a review | ~1–1.5K |
| `ab-test-setup` | Structured test design: hypothesis, variants, sample size, timeline | Simple A/B where gut judgment is enough | ~1–1.5K |
| `content-strategy` | Full content calendar with topic clusters and keyword mapping | One-off content piece — brief Content Builder | ~1–1.5K |
| `ad-creative` | Batch of 10+ ad variations with multiple angles | 3 versions of one ad — Content Builder handles | ~1.5–2K |
| `churn-prevention` | Designing cancellation flow + save offers + win-back sequence | Single retention email — Content Builder | ~1.5K |
| `designing-growth-loops` | Designing referral mechanics or viral loops | Improving one conversion point — Funnel Builder | ~1.5K |
| `designing-surveys` | Customer survey design with analysis framework | Quick 3-question check-in | ~1K |
| `competitor-alternatives` | Full vs./alternative pages for SEO | Quick competitive comparison doc | ~1–1.5K |
| `content-marketing` | SEO content strategy + distribution plan | One blog post — Content Builder | ~1.5–2K |
| `ai-seo` | Optimizing content for AI search citation | Standard SEO — not AI-specific | ~1K |

---

## Routing Decision Tree

```
Denis requests something
        │
        ▼
Does a ChatGPT GPT handle this task?
        │
   YES ──────────────────────────────► Route to GPT (Tier 3)
        │                               ChatGPT executes → Denis evaluates with Claude
        │
   NO / GPT output was insufficient
        │
        ▼
Does a Claude Skill handle this better?
        │
   YES ──────────────────────────────► Invoke Claude Skill (Tier 2)
        │                               Claude runs skill directly
        │
   NO / needs strategy/HTML
        │
        ▼
Claude Brain handles it (Tier 1)
  Strategy artifact / HTML artifact / Evaluation
```

---

## Campaign Workflows — Which Tiers Run

### Workflow 1: Cold Outbound Campaign
**Goal:** Email sequence to a new ICP segment
**Timeline:** 1–2 days | **Token budget:** ~5–8K

```
1. [T1] Claude Brain → ICP Builder brief (Markdown artifact)
2. [T3] ICP Builder GPT → ICP profile + real quotes (canvas)
3. [T1] Claude Brain → evaluate ICP output
   └─ If thin: [T2] customer-research skill on uploaded transcripts
4. [T1] Claude Brain → Content Builder brief
5. [T3] Content Builder GPT → 3-version email sequence (canvas)
6. [T1] Claude Brain → evaluate sequence (score all 3 versions)
   └─ If <7: revision brief → back to Content Builder
7. [T2] ab-test-setup skill → test design for 2 subject lines
8. [T2] analytics-tracking skill → tracking plan
```

---

### Workflow 2: Landing Page (Full Production)
**Goal:** Production-ready page with copy and live HTML
**Timeline:** 1 session | **Token budget:** ~8–15K

```
1. [T1] Claude Brain → ICP Builder brief
2. [T3] ICP Builder GPT → ICP profile (canvas)
3. [T1] Claude Brain → Messaging Builder brief (with ICP data)
4. [T3] Messaging Builder GPT → positioning + messaging pillars (canvas)
5. [T1] Claude Brain → Landing Builder brief (with messaging)
6. [T3] Landing Builder GPT → full page copy draft, scored per section (canvas)
7. [T1] Claude Brain → evaluate copy draft
   └─ If ≥7: build HTML artifact
   └─ If <7: revision brief → back to Landing Builder
8. [T1] Claude Brain → builds production HTML artifact
   → Shareable link. Hand to developer or publish directly.
```

---

### Workflow 3: Content Engine (Ongoing)
**Goal:** Weekly content across channels
**Timeline:** Per week | **Token budget:** ~3–5K/week

```
PLANNING (monthly):
1. [T2] content-strategy skill → topic clusters + calendar (30-day)

WEEKLY EXECUTION:
2. [T1] Claude Brain → Content Builder brief (this week's pieces)
3. [T3] Content Builder GPT → first drafts (canvas)
4. [T1] Claude Brain → evaluate + upgrade if needed
5. [T2] copy-editing skill → final polish before publishing (optional)
```

---

### Workflow 4: New Market Entry
**Goal:** Full ICP, positioning, and GTM for new segment
**Timeline:** 3–5 days | **Token budget:** ~15–25K**

```
RESEARCH:
1. [T2] customer-research skill → deep synthesis (if transcripts available)
2. [T3] ICP Builder GPT → web research + quotes
3. [T2] competitive-analysis skill → full market positioning map

STRATEGY:
4. [T1] Claude Brain → GTM strategy artifact (extended thinking)
5. [T3] Messaging Builder GPT → positioning framework

EXECUTION:
6. [T1] Claude Brain → campaign brief bundle (all GPTs, sequenced)
7. [T3] Run each GPT in sequence
8. [T1] Claude Brain → evaluate each output

MEASUREMENT:
9. [T2] analytics-tracking skill → full tracking plan
10. [T2] ab-test-setup skill → test first 2 campaign variables
```

---

## Token Allocation by Tier

| Tier | Monthly typical | Spike (launch month) |
|---|---|---|
| T1 — Claude Brain (briefs + eval + HTML) | 8–15K | 20–30K |
| T2 — Claude Skills (on demand) | 2–6K | 8–15K |
| T3 — ChatGPT GPTs | flat ~$20 | flat ~$20 |
| **Total Claude tokens** | **10–21K** | **28–45K** |

**Token efficiency rules:**
- Default to T3 (ChatGPT) — it costs nothing extra
- Use T2 Claude Skills only when GPT output fails evaluation
- Use T1 HTML production only for pages Denis wants as production artifacts
- Extended thinking (T1 Opus): max 2–3x/month, only for new market GTM or full ICP architecture

---

## Skill Loading Protocol (Claude.ai)

Claude Skills are not preloaded. They activate when Denis invokes them or Claude routes to them.

**How Denis invokes a skill:**
- "Use the cold-email skill to write this sequence"
- "Run customer-research on these transcripts"
- "Set up analytics tracking for this campaign"

**How Claude routes to a skill automatically:**
- GPT output evaluated as <5/10 after revision brief → Claude escalates to corresponding skill
- Denis uploads primary research (interviews, survey data) → Claude uses customer-research skill
- Denis asks for ab-test design → Claude uses ab-test-setup skill

**Skill ↔ GPT equivalents:**

| Task | Default (T3 GPT) | Escalate to (T2 Skill) |
|---|---|---|
| ICP research | ICP Builder GPT | `customer-research` |
| Positioning | Messaging Builder GPT | `competitive-analysis` |
| Copy | Content Builder GPT | `copywriting` / `cold-email` |
| Funnel | Funnel Builder GPT | `designing-growth-loops` |
| Tracking | (Claude Brain routing) | `analytics-tracking` |
| A/B test | (Claude Brain routing) | `ab-test-setup` |

---

## Quality Escalation Path

If ChatGPT GPT output scores below threshold after one revision:

```
Score <5 after revision → escalate to Claude Skill
Score 5–6 after revision → one more ChatGPT revision brief
Score 7+ → ship

Escalation example:
Content Builder returns email scoring 4/10
→ Claude writes revision brief → Content Builder returns 5/10
→ Claude escalates: "Use the cold-email skill directly"
→ cold-email skill produces output scoring 8/10 → ship
```

Cost of escalation: ~1.5–2K extra tokens. Worth it for campaigns where quality matters.

---

*Marketing OS Skill Orchestration Matrix v1.1 · 3-Tier Architecture · 2026-04-07*
