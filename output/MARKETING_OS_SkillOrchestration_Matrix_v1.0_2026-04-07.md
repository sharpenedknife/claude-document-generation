# Marketing OS — Skill Orchestration Matrix
**Version:** 1.0
**Date:** 2026-04-07
**Purpose:** Map how all 25+ marketing skills coordinate, hand off work, and reference shared project context.

---

## Overview

The Marketing OS uses **25+ Claude skills** working simultaneously. They're not isolated tools—they orchestrate around a single **project-marketing-context.md** that defines ICP, messaging, positioning, and channels.

**Architecture:**
```
┌─────────────────────────────────────────────────────┐
│   Project-Marketing-Context.md (Shared Nerve Center) │
│   (ICP, Messaging, Positioning, Channels, GTM)       │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
   ┌────▼────┐ ┌──▼──────┐ ┌─▼──────────┐
   │RESEARCH │ │EXECUTION│ │OPTIMIZATION│
   └────┬────┘ └──┬──────┘ └─┬──────────┘
        │         │          │
    [7 Skills]  [15 Skills] [3+ Skills]
```

Each skill reads the project context, pulls relevant data, executes its specialty, outputs work, and feeds into downstream skills.

---

## Phase 1: Research & Strategy (Foundation)

**These skills run FIRST. They create the project-marketing-context.md that all other skills reference.**

| Skill | Input | Output | Token Cost | When to Use |
|-------|-------|--------|------------|-----------|
| **customer-research** | Problem statement, target audience | Customer insights, pain points, quotes, behavior patterns | 2–3K | Starting new project or validating ICP assumptions |
| **conducting-user-interviews** | Interview questions, target participants | Transcripts, themes, quotes, behaviors | 1.5–2K | Primary research (1:1 customer calls) |
| **designing-surveys** | Survey questions, audience | Survey design, analysis framework | 1K | Quantify patterns from interviews |
| **competitive-analysis** | Competitor list, your positioning | Competitive matrix, gaps, opportunities | 1.5–2K | Understanding landscape and positioning |
| **customer-research** (secondary) | Topic (market reports, reviews, forums) | Market trends, competitor intel, customer language | 2K | G2 analysis, Reddit mining, market reports |
| **brand-storytelling** | Your origin, values, mission | Brand story, voice guide, narrative arc | 1–1.5K | Define brand identity |
| **defining-product-vision** | Long-term goals, market opportunity | Vision statement, product direction | 1K | Strategic alignment |

**Output:** **project-marketing-context.md** (feeds all downstream skills)

**Quality Gate:** Context doc is complete, ICP data-driven, messaging tested, channels prioritized.

---

## Phase 2: Execution (All Skills Simultaneously)

**These skills pull from project-marketing-context.md and execute campaigns, content, and outreach.**

### Messaging & Content Foundation
| Skill | Input | Output | Token Cost | Downstream |
|-------|-------|--------|------------|-----------|
| **copywriting** | Messaging pillars, ICP, context | Website copy, landing pages, long-form content | 1.5–2K | All paid/owned channels |
| **brand-storytelling** (applied) | Brand narrative, voice | Positioning pages, about pages, case studies | 1–1.5K | Content, social, brand assets |

### Cold Outbound (Highest ROI)
| Skill | Input | Output | Token Cost | Downstream |
|-------|-------|--------|------------|-----------|
| **cold-email** | ICP, messaging, list | Email sequences (initial + 3–5 follow-ups), templates | 1.5–2.5K | Analytics-tracking (measure opens/clicks) |
| **founder-sales** | ICP, messaging, objection handling | Sales call framework, demo deck, pitch guide | 1–1.5K | Sales team, live meetings |
| **email-sequence** | Cold email output, nurture sequence | Full automated sequence (5–10 emails), timing, CTAs | 1.5–2K | Analytics-tracking, conversion measurement |

### Content & Owned Channels
| Skill | Input | Output | Token Cost | Downstream |
|-------|-------|--------|------------|-----------|
| **content-strategy** | ICP, messaging pillars, channels | Content calendar, topic clusters, keywords | 1–1.5K | copywriting, content-marketing |
| **content-marketing** | Topics, target audience | Blog post outlines, SEO strategy, distribution plan | 1.5–2K | copywriting, ai-seo (for AI visibility) |
| **ai-seo** | Blog content, positioning | AI search optimization, LLM citation opportunities | 1K | Publishing, promotion |

### Paid & Creative Channels
| Skill | Input | Output | Token Cost | Downstream |
|-------|-------|--------|------------|-----------|
| **ad-creative** | Messaging pillars, ICP, brand voice | Ad copy variations (5–20), headlines, CTAs | 1.5–2K | Analytics-tracking (CTR, conversion) |
| **copywriting** (landing pages) | Messaging, ICP, offer | High-converting landing page copy | 1.5–2K | form-cro (optimize form fields) |
| **form-cro** | Landing page, lead magnet | Optimized form fields, field order, copy | 1K | Analytics-tracking (form completion rate) |

### Website & Sales Enablement
| Skill | Input | Output | Token Cost | Downstream |
|-------|-------|--------|------------|-----------|
| **competitor-alternatives** | Your positioning, competitors | Alternative/vs. pages for SEO + sales | 1–1.5K | Publishing, sales deck |
| **copywriting** (sales pages) | Positioning, objections, proof | Pricing page, feature pages, case studies | 1–1.5K | Sales, conversion measurement |

### Social & Community
| Skill | Input | Output | Token Cost | Downstream |
|-------|-------|--------|------------|-----------|
| **community-building** | ICP, messaging, channels | Community strategy, Discord/Slack setup, engagement plan | 1.5K | Organic growth, word-of-mouth |
| **content-strategy** (social angle) | Brand voice, platforms | Social content calendar, thread templates | 1K | Publishing, engagement |

### Copy Polish
| Skill | Input | Output | Token Cost | Downstream |
|-------|-------|--------|------------|-----------|
| **copy-editing** | Draft copy from any source | Polished, tight copy (removes 20–30% of words) | 0.5–1K | Publishing, performance |

---

## Phase 3: Measurement & Optimization (Continuous)

**These skills measure performance, run tests, and feed learnings back into strategy.**

| Skill | Input | Output | Token Cost | Loop Back To |
|-------|-------|--------|------------|-------------|
| **analytics-tracking** | Campaigns, conversion points, goals | Tracking plan, GTM implementation, dashboard | 1–1.5K | All campaigns (measures performance) |
| **ab-test-setup** | Hypotheses (copy, creative, offer) | Test framework, variants, sample size, timeline | 1–1.5K | copywriting, ad-creative, form-cro |
| **designing-surveys** | Post-purchase or churn questions | Survey design, analysis framework | 1K | customer-research (feedback loop) |
| **churn-prevention** | ICP, objections, retention metrics | Exit survey, save offers, win-back sequence | 1.5K | email-sequence, copywriting (adjust messaging) |
| **designing-growth-loops** | Current metrics, virality potential | Referral mechanics, network effects, expansion strategy | 1.5K | Marketing strategy, customer-research (feedback) |

---

## Orchestration Workflows

### Workflow 1: Cold Outbound Campaign (Fastest ROI)
**Timeline:** 2–3 weeks
**Skills Used:** 5 (research → outbound → measure)

```
1. product-marketing-context.md exists ✓
   ↓
2. cold-email (writes sequence)
   ↓
3. founder-sales (sales call framework if warm)
   ↓
4. analytics-tracking (sets up opens/clicks/reply tracking)
   ↓
5. ab-test-setup (test 2 subject lines, 2 opening hooks)
   ↓
6. MEASURE: Reply rate, conversion rate
   ↓
7. LEARN: Update messaging if needed, iterate
```

**Token Budget:** ~6–8K total (one-time per campaign)

---

### Workflow 2: Content & SEO Funnel (Long-term)
**Timeline:** 4–8 weeks
**Skills Used:** 6 (strategy → content → SEO → measure)

```
1. product-marketing-context.md exists ✓
   ↓
2. content-strategy (topic clusters, keywords)
   ↓
3. copywriting (blog post outlines, copy)
   ↓
4. ai-seo (optimize for AI search engines)
   ↓
5. analytics-tracking (organic traffic, lead gen)
   ↓
6. ab-test-setup (test headlines, CTAs, offers)
   ↓
7. MEASURE: Traffic, leads, conversion rate
   ↓
8. LEARN: Double down on winning topics, kill underperformers
```

**Token Budget:** ~8–12K total (amortized across multiple posts)

---

### Workflow 3: Paid Ads Campaign
**Timeline:** 1–2 weeks
**Skills Used:** 5 (creative → execution → optimize)

```
1. product-marketing-context.md exists ✓
   ↓
2. ad-creative (write 10+ variations)
   ↓
3. copywriting (landing pages for each ad)
   ↓
4. form-cro (optimize lead capture form)
   ↓
5. analytics-tracking (impressions, clicks, conversions)
   ↓
6. ab-test-setup (test 3 creatives, 2 audiences)
   ↓
7. MEASURE: CTR, conversion rate, cost per lead
   ↓
8. LEARN: Pause losers, scale winners, iterate
```

**Token Budget:** ~6–8K total (per campaign)

---

### Workflow 4: Full-Funnel Launch (All Phases)
**Timeline:** 6–12 weeks
**Skills Used:** 15+ (research → awareness → consideration → decision → measure)

```
RESEARCH PHASE (Weeks 1–2):
├─ customer-research
├─ competitive-analysis
├─ brand-storytelling
└─ Output: project-marketing-context.md

AWARENESS PHASE (Weeks 3–4):
├─ content-strategy
├─ copywriting
├─ ad-creative
└─ cold-email (warm outreach)

CONSIDERATION PHASE (Weeks 5–6):
├─ email-sequence (nurture)
├─ copywriting (case studies, comparison pages)
├─ competitor-alternatives (vs. pages)
└─ form-cro (lead capture)

DECISION PHASE (Weeks 7+):
├─ founder-sales (sales calls)
├─ copywriting (pricing, objection handling)
└─ churn-prevention (retention)

OPTIMIZATION (Ongoing):
├─ analytics-tracking (all phases)
├─ ab-test-setup (test winning angles)
├─ designing-surveys (customer feedback)
└─ designing-growth-loops (expansion)
```

**Token Budget:** ~25–35K total (amortized across 6+ months)

---

## Token Allocation by Phase

| Phase | Skills | % of Budget | Typical Spend |
|-------|--------|------------|---------------|
| Research & Strategy | 7 skills | 15% | 4–6K (one-time) |
| Execution | 15 skills | 55% | 12–18K (per month) |
| Measurement & Optimization | 3+ skills | 20% | 4–6K (per month) |
| Iteration & Learning | All | 10% | 2–3K (per month) |

**Total Monthly Budget:** ~20–30K tokens (varies by campaign intensity)

---

## Skill Dependencies & Sequencing

```
Must Run Before Others:
├─ product-marketing-context.md (all others depend on this)
├─ customer-research (informs positioning)
├─ competitive-analysis (informs positioning)
└─ brand-storytelling (informs all messaging)

Then Can Run Simultaneously:
├─ Execution Group: cold-email, copywriting, ad-creative, content-strategy
└─ Support Group: form-cro, analytics-tracking, ab-test-setup

Finally:
└─ Optimization: churn-prevention, designing-surveys, designing-growth-loops
```

---

## Skill Routing Rules (Token Efficiency)

**Rule 1: Reuse Project Context**
- product-marketing-context.md is loaded ONCE per project
- All 15+ execution skills reference the same context
- Don't re-run research unless ICP changes
- **Token Savings:** ~10K per project

**Rule 2: Batch Similar Tasks**
- Instead of: "Write one cold email" (costs 1.5K)
- Do: "Write 5 cold email variations + 3 follow-ups" (costs 2.5K for all)
- **Token Savings:** ~30–40% per task type

**Rule 3: Skip Polish for Drafts**
- Use copywriting for first drafts
- Skip copy-editing for internal iterations
- Only polish for publication
- **Token Savings:** ~0.5K per draft cycle

**Rule 4: Conditional Skill Triggers**
- If cold email reply rate is good: skip ab-test-setup
- If landing page converting: don't run form-cro
- If no churn signal: skip churn-prevention
- **Token Savings:** ~2–3K per campaign

**Rule 5: Async Skill Execution**
- Run research skills first (4–6K)
- Then execution skills in parallel (not sequential)
- Measure continuously
- **Token Efficiency:** Linear token growth, not exponential

---

## Quality Gates at Each Stage

### After Research Phase (Gate 1)
- [ ] project-marketing-context.md created and current
- [ ] ICP data-driven (from customer research, not guesses)
- [ ] Positioning tested against competitive landscape
- [ ] Messaging tied to customer language
- [ ] Channels prioritized by audience + cost

### After Each Execution Skill (Gate 2)
- [ ] Output quality: Does it match messaging pillars?
- [ ] Does it speak to ICP in their language?
- [ ] Does it address stated objections?
- [ ] Is it differentiated from competitors?

### After Campaign Launch (Gate 3)
- [ ] Tracking is live (analytics-tracking confirmed)
- [ ] Test variants are distinct (ab-test-setup confirmed)
- [ ] Baseline metrics captured
- [ ] Success thresholds defined

### During Optimization (Gate 4)
- [ ] Learnings from each campaign logged
- [ ] Successful angles fed back to copywriting, ad-creative
- [ ] Failed approaches documented (prevent re-iteration)
- [ ] project-marketing-context.md updated with learnings

---

## Evaluation Framework (Manual Review Loop)

**Question 1: Does it match the ICP?**
- Read the output
- Check against project-marketing-context.md
- Ask: "Would THIS ICP person respond to this?"
- Score 1–10

**Question 2: Does it use customer language?**
- Are your actual customer quotes/phrases in the copy?
- Or is it generic marketing speak?
- Score 1–10

**Question 3: Is it differentiated?**
- Read competitor copy
- Compare your copy
- Ask: "Could this ONLY come from our company?"
- Score 1–10

**Question 4: Does it address objections?**
- List common objections for this ICP
- Check if copy proactively addresses them
- Score 1–10

**Quality Threshold:** Average score ≥7/10. Below 7 = revise before publishing.

---

## Skill Selection Matrix (Which Skill for This Task?)

| Task | Skill | Why | Token Cost | When NOT to Use |
|------|-------|-----|------------|-----------------|
| "Write landing page copy" | copywriting | Comprehensive, ICP-focused | 1.5–2K | If just need minor tweaks (use copy-editing) |
| "Polish existing copy" | copy-editing | Fast, efficient, tightens | 0.5–1K | If starting from scratch (use copywriting) |
| "Write 5 cold email versions" | cold-email | Specialized in outbound, personalization | 1.5–2K | If not B2B outbound (use copywriting) |
| "Create email drip sequence" | email-sequence | Lifecycle, timing, automation | 1.5–2K | If just one email (use copywriting) |
| "Understand customer problems" | customer-research | Synthesizes interviews, reviews, data | 2–3K | If already have clear ICP (save tokens) |
| "Understand competitors" | competitive-analysis | Positioning, gaps, war games | 1.5–2K | If only need quick feature comparison |
| "Build content strategy" | content-strategy | Topic clusters, keywords, editorial cal | 1–1.5K | If already have a list (use copywriting) |
| "Measure campaign performance" | analytics-tracking | Implementation, dashboard, GTM | 1–1.5K | If already tracking (just pull data) |
| "Design A/B test" | ab-test-setup | Hypothesis, variants, sample size | 1–1.5K | If test is trivial (manual quickstart) |

---

## Example: Multi-Skill Campaign (Cold Outbound)

**Project:** Launch outbound to VP Marketing at mid-market SaaS
**Timeline:** 2 weeks
**Budget:** 8K tokens

**Day 1:**
- **Input:** project-marketing-context.md (ICP = VP Marketing, mid-market SaaS, pain = manual reporting)
- **Skill:** cold-email
- **Output:** 5-email sequence (initial + 3 follow-ups) + personalization framework
- **Token Cost:** 2K
- **Quality Check:** Does each email address their pain? Use their language? Stand out from 50 other emails they get?

**Day 2:**
- **Input:** Cold email sequence from Day 1
- **Skill:** founder-sales (craft sales call framework for warm intros)
- **Output:** Sales call script, objection handling, demo flow
- **Token Cost:** 1.2K

**Day 3:**
- **Input:** Campaign IDs, email addresses
- **Skill:** analytics-tracking (set up open, click, reply tracking)
- **Output:** Tracking implementation, success dashboards
- **Token Cost:** 1K

**Day 4–5:**
- **Input:** Initial email + 2 variations
- **Skill:** ab-test-setup (test subject line + opening hook)
- **Output:** Test design, sample size, success thresholds
- **Token Cost:** 1.2K

**Day 6–14:**
- **Execution:** Send sequence, measure, iterate
- **Skill:** designing-surveys (exit survey if they unsubscribe: "What was the objection?")
- **Token Cost:** 0.8K

**Learnings Loop:**
- **Input:** Reply rate (15%), objection themes (budget concerns)
- **Skill:** copywriting (update cold email to address budget objection)
- **Output:** Revised email sequence v2
- **Token Cost:** 1.2K (amortized across next batch)

**Total:** ~8K tokens for a full cold outbound campaign with measurement + optimization.

---

## Preventing Token Creep

**Anti-Pattern 1: Re-running research for every campaign**
- Fix: Reuse project-marketing-context.md
- Save: 4–6K tokens per campaign

**Anti-Pattern 2: Sequential skill execution (waiting for each output)**
- Fix: Run execution skills in parallel
- Save: 10–20% time, not token-specific but faster feedback

**Anti-Pattern 3: Over-iterating on polish**
- Fix: Skip copy-editing drafts, only polish for publication
- Save: 0.5K per draft cycle × 5 cycles = 2.5K per project

**Anti-Pattern 4: Using wrong skill for task**
- Fix: Use the skill selection matrix above
- Save: 0.5–1.5K per task (using efficient skill)

**Anti-Pattern 5: Not documenting learnings**
- Fix: Log winning angles, objections, customer language in project context
- Save: Avoid re-learning the same lessons (2–3K per mistake avoided)

---

*Marketing OS v1.0 · Skill Orchestration Matrix · 2026-04-07*
*Reference for token efficiency, skill routing, and campaign workflows*
