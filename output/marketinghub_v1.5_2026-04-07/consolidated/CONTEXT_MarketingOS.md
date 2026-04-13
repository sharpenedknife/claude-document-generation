# Marketing OS — Consolidated Claude Context
**v1.5 · 2026-04-07 · Upload to Claude.ai Project Knowledge**
---
# Marketing OS — Claude Brain
**v1.5 · 2026-04-07 · Hardened — upload to Project Knowledge**

---

## ROLE

You are Marketing OS. You generate briefs for ChatGPT GPTs and evaluate what they return. You do not write final marketing copy yourself.

**You do:** strategy, brief generation, routing, evaluation, memory.
**You don't:** write emails, ads, landing pages, blog posts, social copy, or do web research.

---

## 5 RULES — ALWAYS

1. **Artifact always.** Any output ≥10 lines opens in a Markdown artifact. Never dump structure into chat.
2. **Brief format.** Every brief uses the 📋 template below, exactly. No freeform briefs.
3. **Evaluation format.** Every evaluation uses the 📊 template below, exactly. Score all 4 dimensions.
4. **Don't write copy.** If Denis asks for copy directly, respond: "I'll generate a brief for [GPT name] — paste it in ChatGPT to get the copy." Then generate the brief.
5. **Memory.** After context changes, update memory: active product, ICP, current campaign, last evaluation score.

---

## ROUTING

| Denis says | Route to |
|---|---|
| ICP / customer research / who are my customers | ICP Builder |
| Score this copy / is this messaging right | Messaging Builder |
| Write [email / ad / post / thread / newsletter] | Content Builder |
| Build my funnel / where am I losing people | Funnel Builder |
| Write a landing page / build my page | Landing Builder |
| Plan this feature / write a spec | Build Planner |
| Full strategy / GTM plan / what should I do | Claude brain — strategy artifact |
| Evaluate this / score this output | Claude brain — evaluation artifact |

Multi-GPT campaigns: produce all briefs in one artifact, numbered in sequence.

---

## BRIEF FORMAT

Open in Markdown artifact. Use exactly:

```
📋 BRIEF FOR [GPT NAME]
━━━━━━━━━━━━━━━━━━━━━━━
Project: [name]
ICP: [role · company size · primary pain — 1 line]
Goal: [what to produce — specific]
━━━━━━━━━━━━━━━━━━━━━━━
[GPT-SPECIFIC FIELDS]
━━━━━━━━━━━━━━━━━━━━━━━
Tone: [direct / warm / authoritative / challenger]
Versions: [number]
Format: [specific — e.g. "5-email sequence, 150 words each"]
━━━━━━━━━━━━━━━━━━━━━━━
```

GPT-specific fields:
- **ICP Builder** → `Depth: [1 persona / segmentation] | Pull from: [G2 · Reddit · LinkedIn · forums] | Output: [profiles / quotes / triggers]`
- **Messaging Builder** → `Task: [build / score / rewrite] | Pillars: [list] | Proof: [stats / quotes] | Competitors: [list]`
- **Funnel Builder** → `Task: [design / audit] | Current funnel: [stages + drop-offs] | Web research: [yes/no]`
- **Content Builder** → `Type: [email / sequence / ad / blog / LinkedIn / social] | Messages: [2-3 key points] | Objections: [list] | Proof: [available]`
- **Build Planner** → `Feature: [what] | User problem: [specific] | Success metric: [KPI] | Scope: [MVP/full] | Ship: [date]`
- **Landing Builder** → `CTA: [action] | Sections: [full / specific] | Proof: [quote/stat] | Visual mockup: [yes/no]`

---

## EVALUATION FORMAT

Open in Markdown artifact. Use exactly:

```
📊 EVALUATION — [type] · [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORE: [X]/10   VERDICT: SHIP ✅ / REVISE ⚠️ / REWRITE ❌

ICP Match:          [X]/10 · [specific reason — quote the weak line]
Messaging:          [X]/10 · [what lands, what doesn't]
Differentiation:    [X]/10 · [does it sound like anyone else?]
Objection Handling: [X]/10 · [what objection is unaddressed?]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT WORKS: [1-2 specific lines that land]
WHAT FAILS: [1-2 specific failures — exact quote]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Score ≥7] ✅ SHIP — [optional minor edits, 1 line]
[Score <7]  ⚠️ REVISION BRIEF:
[Immediately write the revision brief using the 📋 format above]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Thresholds: 9–10 ship · 7–8 ship with edits · 5–6 revise · 1–4 rewrite.

---

## CONVERSATION STARTER BEHAVIOR

- **🧠 Plan my next campaign** → Ask goal + ICP. Produce campaign plan + first brief. Both in one artifact.
- **📊 Evaluate this output** → "Paste the ChatGPT output." Then evaluate.
- **🗺️ Build my GTM strategy** → Engage extended thinking. Produce full GTM artifact.
- **🔄 Update my project context** → Ask what changed. Update memory. Confirm.

---

## STYLE

Direct. No preamble. Lead with the action. No "Great question." No hedging without resolution.
Marketing-literate: use ICP, GTM, TOFU/MOFU/BOFU correctly.
Model: Sonnet default. Opus for full GTM strategy. Haiku for routing-only questions.

---

*Marketing OS v1.5 · Hardened · 2026-04-07*

---

# Marketing OS — Knowledge Structure
**Version:** 1.0 | **Date:** 2026-04-07 | **Purpose:** Reusable templates and libraries shared across all projects

---

## Overview

This document contains **templates and libraries** that are project-agnostic. Once created, they apply to ALL projects. Reference these when building campaigns, writing copy, and designing flows.

---

## Library 1: Customer Language Patterns

**Use these phrases when you encounter them in customer interviews. These will work for ANY ICP.**

### Pain Point Language Patterns
- "It's [specific time]—wasting hours on [task]"
- "We can't [specific capability]—it's killing us"
- "Everyone tells us we should [outcome], but we're stuck on [blocker]"
- "[Person/Team] is frustrated because [pain]"
- "This costs us $[amount]/month in lost [metric]"
- "We've tried [solution], but it didn't [desired outcome]"

### Desire Language Patterns
- "What we really want is [outcome] in [timeframe]"
- "If we could just [action], we'd [result]"
- "I'd pay for something that [specific capability]"
- "We're looking for [outcome], not [alternative]"

### Objection Language Patterns
- "Our team is worried about [concern]"
- "We've been burned by [similar solution]"
- "It's too [attribute] for us"
- "We don't have [resource] to implement this"

### Buying Signal Language Patterns
- "We're currently evaluating [category]"
- "We need to solve [problem] by [date]"
- "The board is pushing us to [outcome]"
- "Budget is approved if we can [condition]"

---

## Library 2: Message Pillar Templates

**These are generic pillar templates. Customize them per project.**

### Pillar 1: Problem Validation (Problem Statement + Proof)
**Template:**
```
"[ICP Role] at [Company Type] spend [X hours/days] on [Task],
costing $[Amount] in lost [Metric].

But it doesn't have to be this way."
```

**Example:**
```
"VP Marketing at mid-market SaaS spends 15 hours/week on reporting,
costing $15,000/month in lost strategic work.

But it doesn't have to be this way."
```

---

### Pillar 2: Unique Solution (Your Approach)
**Template:**
```
"Unlike [competitor approach], [Your Company] [Unique Action] by [Method].
This means [Outcome] without [Pain/Cost/Friction]."
```

**Example:**
```
"Unlike manual reporting dashboards, Mercury automates compliance
by integrating with your existing stack. This means clean, accurate
reports without learning new software."
```

---

### Pillar 3: Credibility & Trust (Proof)
**Template:**
```
"[Number] [Group] trust [Your Company] to [Outcome].
[Specific Case Study / Stat / Credential]."
```

**Example:**
```
"500+ mid-market teams trust Mercury to save 15 hours/week.
Brex, Notion, and Mercury Customers (case studies available)."
```

---

### Pillar 4: Desired Outcome (Their Version of Success)
**Template:**
```
"Imagine: [Time/Resource Freed Up] + [Capability Gained].
[Emotional payoff or business impact]."
```

**Example:**
```
"Imagine: 15 hours/week reclaimed + confidence in accuracy.
Your marketing team focuses on strategy instead of admin."
```

---

### Pillar 5: Movement / Social Proof (Trend or Community)
**Template:**
```
"[Number] [Group] are already [Action].
[Specific example or statistic about the movement]."
```

**Example:**
```
"500+ founders are already automating compliance with Mercury.
Join the movement to reclaim your time."
```

---

## Library 3: Cold Email Templates

### Structure (Proven to Work)
```
Subject: [Personalized, specific to their role/company]

Opening Hook: [Specific observation about their company or role]

Problem Recognition: [State their problem in their language]

Pivot: But here's what we've seen work...

Solution: [How your approach solves it]

Proof: [Case study / stat / social proof]

CTA: [Specific, low-friction ask]

Signature: [Name, title, LinkedIn, maybe one credential]
```

### Email Template 1: Problem Recognition Angle
```
Hi [Name],

[Specific observation]: I noticed [Company] is [specific action/signal that shows they have the problem].

Most [Role] at [Company Size] are stuck [Problem Statement].

What we've seen work: [Unique approach].

This helped [Case Study: Role/Company] [Specific Outcome] in [Timeframe].

Curious if this could work for [Company]?

[CTA: Low friction — "Chat briefly?"]

[Signature]
```

### Email Template 2: Credibility Angle
```
Hi [Name],

I work with [Number] [Role] at [Company Type].

Most are struggling with [Problem].

Here's what's changed: [Why now / What's different].

[Case Study: Problem → Solution → Outcome]

Wondering if [Company] is dealing with [Specific Problem]?

[CTA: "Quick call?"]

[Signature]
```

### Email Template 3: Differentiation Angle
```
Hi [Name],

[Specific research point]: You mentioned [specific thing they said/wrote].

Most [Role] who want [Outcome] try [Competitor Approach].

But we've found [Your Unique Angle] works better because [Reason].

[Proof: Stat or Case Study]

Worth a conversation?

[CTA]

[Signature]
```

### Follow-Up Templates
**Follow-Up 1 (2 days later):**
```
[Name] — Quick follow-up from my note above.

[Restate value + new angle]

[CTA: Lower friction — "Free consultation?"]
```

**Follow-Up 2 (4 days later):**
```
[Name] — One more thing:

[Different angle / proof / case study]

[CTA: "Let's chat"]
```

**Follow-Up 3 (1 week later):**
```
[Name] — Last note:

I know most of you are busy. But if [Outcome] is even remotely on your radar this quarter, this is worth 15 minutes.

[CTA: Direct calendar link]
```

---

## Library 4: Landing Page Copy Templates

### Sales Page Structure
```
HERO (Above the fold):
- Headline: [Outcome-focused, not feature]
- Subheadline: [Specific problem solved]
- Hero Image/Video: [Proof of transformation or product in action]
- CTA: [Primary action — clear, specific]

SECTION 2: Problem Validation
- [Specific statistic or customer quote about the problem]
- Pain points (3–5 bullets)
- Why it matters [emotional or business impact]

SECTION 3: Unique Solution
- How you solve it differently
- 3–5 unique capabilities (not features)
- Why that difference matters

SECTION 4: How It Works
- Step-by-step: From signup to outcome
- 3–5 steps, each showing transformation

SECTION 5: Social Proof
- Customer testimonials (3–5)
- Case study (before/after)
- Numbers (customers, impact, growth)
- Logos of known companies

SECTION 6: Objection Handling
- FAQ addressing common objections
- Pricing/affordability addressed
- Switching cost / implementation concern addressed
- "Why us vs. alternatives" comparison

SECTION 7: Limited Offer / Urgency
- Free trial / demo / consultation
- Limited time / spots
- Clear CTA + calendar link

SECTION 8: Final CTA
- Reiterate transformation
- Reminder of proof
- Call to action
```

---

## Library 5: Email Sequence Templates

### Nurture Sequence Structure (5–10 Emails)

**Email 1 (Immediately):** Welcome + What to Expect
```
Subject: Welcome to [Resource/Community]

Content:
- Thank you for subscribing
- What they'll get (value promise)
- First email coming tomorrow
- [Soft CTA: Forward to a friend]
```

**Email 2 (Day 2):** Problem Recognition + Story
```
Subject: The [Problem] problem most [Role] have

Content:
- Customer story: How [Customer] faced [Problem]
- Why this problem is widespread
- One insight they can apply today
- [Soft CTA: Reply with your biggest challenge]
```

**Email 3 (Day 4):** Solution Mechanism
```
Subject: How [Company] solved [Problem]

Content:
- Explain your unique approach
- Why this approach works (mechanism)
- Case study or proof
- [CTA: Free resource / guide / audit]
```

**Email 4 (Day 7):** Objection Handling
```
Subject: Doubt? Here's why others were skeptical too...

Content:
- Common objection: [Common doubt]
- Why that doubt is valid
- How you address it
- Customer proof that doubt was unfounded
- [CTA: Free trial / demo]
```

**Email 5 (Day 10):** Limited Offer / Urgency
```
Subject: [Limited offer] — ending [date]

Content:
- Specific offer (discount, bonus, limited spots)
- What's included
- Why now (scarcity / deadline)
- [CTA: Claim offer]
```

---

## Library 6: Ad Creative Templates

### Cold Prospecting Ad (LinkedIn)
```
Headline: [Benefit-focused, not feature]
Primary Image: [Customer testimonial / proof / transformation]
Copy:
"[Problem statement most [ICP] face]

What most don't realize: [Unique insight]

[Company] helps [ICP] [Specific outcome] by [Unique approach].

[Proof or stat]

Try free for [timeframe]: [Link]"

CTA: Download Guide / Try Free / Book Demo
```

### Remarketing Ad (Website Visitors)
```
Headline: "Come back. Here's what you missed."
Copy: "[Customer name], you visited us on [Date].

[Problem you were likely exploring]

We've helped [Number] [ICP] [Specific outcome].

Let's talk about [specific problem they came for]."

CTA: "Schedule Demo" / "See Case Study"
```

### Brand Awareness Ad (New Audience)
```
Headline: "[Outcome] without [Pain/Cost]"
Copy: "[Problem statement]

But [Company] changes that with [Unique approach].

[Customer proof]

[Company] is trusted by [Number] [Group].

[CTA]"
```

---

## Library 7: Positioning Statements (By Use Case)

### For B2B SaaS (Mid-Market)
```
"For [VP Title] at [Company Size], [Product] is the [Category] that
[Specific outcome] because [Reason], unlike [Competitor approach]."

Example:
"For VP Marketing at $20–100M SaaS, Mercury is the compliance platform
that automates audits in 3 clicks because founders need to focus on
growth, unlike manual audit workflows."
```

### For Enterprise
```
"For [CxO] responsible for [Function], [Product] is the [Category]
that [Measurable outcome] while [Important constraint], unlike [Alternative]."

Example:
"For CISO managing security compliance, CloudGuard is the platform
that reduces audit prep from 6 weeks to 2 days while maintaining
SOC 2 standards, unlike point solutions."
```

### For Outbound/Marketplace
```
"For [Target Audience] looking for [Outcome], [Company] is the
[Unique angle] because [Proof/Difference]."

Example:
"For freelance designers looking for steady client work, OnlyProjects
is the platform where clients come to you (not the reverse) because
we focus on quality over volume."
```

---

## Library 8: Customer Research Questions (Reusable)

### Discovery Interview Questions
1. "What's your biggest challenge with [Topic]?"
2. "How does that impact your work/business?"
3. "How do you currently solve this?"
4. "What doesn't work about your current approach?"
5. "If you could change one thing, what would it be?"
6. "What outcomes matter most to you?"
7. "Who else influences this decision?"
8. "What's your budget for solutions like this?"
9. "What would make you switch from [current solution]?"
10. "What does success look like 6 months from now?"

### Win/Loss Analysis Questions
**If they bought:**
1. "What was the deciding factor?"
2. "What almost stopped you?"
3. "What could we have done differently?"

**If they didn't:**
1. "What was the main reason?"
2. "Did you choose a competitor? Which one?"
3. "What could we have done to win?"

---

## Library 9: Metrics & Success Thresholds

| Channel/Tactic | Industry Baseline | Excellent | Your Target |
|---|---|---|---|
| Cold Email | 2–3% reply rate | 8–10% | ___ |
| Content (Blog) | 0.5–2% conversion | 5%+ | ___ |
| Landing Page | 2–5% conversion | 10%+ | ___ |
| Paid Ads (LinkedIn) | 1–2% CTR | 3%+ CTR | ___ |
| Email Sequence | 20–30% engagement | 50%+ engagement | ___ |
| Sales Demo | 20–40% qualified | 50%+ close rate | ___ |

---

## Library 10: Objection Response Framework

| Objection | Root Cause | Response Framework |
|---|---|---|
| "It's too expensive" | Price sensitivity | [Total Cost of Ownership] vs. [alternative cost]. ROI calculation. |
| "We're not ready" | Timing concern | [Trigger that makes them ready] is [Timeframe]. Let's plan. |
| "We tried something similar" | Bad past experience | [Competitor difference]. [Proof it works better]. |
| "Our team doesn't have time" | Implementation concern | [Setup time]. [Implementation support included]. |
| "We need to think about it" | Not convinced | [Specific outcome they'd gain]. [Proof from peer company]. |
| "Let me check with my team" | Not the decision-maker | [Decision-maker title]. [How to involve them]. |

---

## How to Use These Libraries

**When creating copy:**
1. Pick the relevant template (landing page, email, cold email)
2. Customize it for YOUR project's ICP and messaging
3. Reference the customer language library for authentic phrasing
4. Test using ab-test-setup skill

**When stuck:**
1. Reference the pattern library (message pillars, positioning statements)
2. See examples
3. Adapt to your specific ICP

**When evaluating:**
1. Use the metrics library for success thresholds
2. Compare your output to baseline
3. Decide: Excellent, Good, or Needs Revision

---

*Marketing OS v1.0 · Knowledge Structure · 2026-04-07*
*Reusable across all projects. Customize per project context.*

---

# [PROJECT NAME] — Marketing Context
**Version:** 1.0
**Date:** YYYY-MM-DD
**Project:** [Project/Client Name]
**Created by:** Denis
**Status:** [Draft / Active / Archived]

---

## Quick Reference

**ICP:** [1 sentence description of ideal customer]
**Positioning:** [1 sentence positioning statement]
**Primary Channels:** [Tier 1 channels, max 3]
**GTM Phase:** [Research / Launch / Scaling / Optimizing]

---

## Section 1: ICP (Ideal Customer Profile)

### Company Profile
- **Industry:** [Which vertical? SaaS, B2B, D2C, Enterprise, etc.]
- **Company Size:** [# employees, revenue range, growth stage]
- **Geography:** [Target regions: US, EU, APAC, Global?]
- **Business Model:** [Subscription, one-time, service-based, marketplace?]
- **Revenue Model:** [How do THEY make money?]

### Buyer Role & Responsibility
- **Primary Buyer Title:** [CEO, VP Marketing, Marketing Manager, IC developer, etc.]
- **Secondary Influences:** [Who else influences the decision?]
- **Budget Authority:** [Does this person control spend? How much?]
- **Success Metric (Their's):** [What does winning look like for them?]
- **Reporting Structure:** [Do they have a team? How big?]

### Pain Points (Use Customer Quotes)
1. **Primary Pain:** [Top problem] — Quote: *"[customer language]"*
2. **Secondary Pain:** [Related problem] — Quote: *"[customer language]"*
3. **Tertiary Pain:** [Underlying problem] — Quote: *"[customer language]"*

### Motivations & Desired Outcome
- **Core Desire:** [What outcome do they want?]
- **Buying Trigger:** [What event makes them start looking?]
- **Timeline:** [How urgent is this problem?]
- **Constraints:** [Budget caps, technical requirements, political blockers?]

### Buying Behavior
- **Buying Cycle:** [How long from awareness to decision? Days, weeks, months?]
- **Decision Process:** [Self-serve, demo, committee, procurement?]
- **Deal Size:** [Average contract value for solutions like yours?]
- **Common Objections:** [What stops them from buying?]
  - Objection 1: [and how we address it]
  - Objection 2: [and how we address it]
  - Objection 3: [and how we address it]

### Channel Affinity
- **Primary Digital Channels:** [Twitter, LinkedIn, Reddit, Slack communities, industry forums?]
- **Content Format Preference:** [Blogs, videos, newsletters, podcasts, whitepapers, case studies?]
- **Sales Preference:** [Self-serve, freemium, demos, cold calls, partner referrals?]
- **Information Sources:** [Where do they research solutions? G2, Reddit, peer recommendations, analyst reports?]

---

## Section 2: Positioning & Messaging

### Positioning Statement (One Sentence)
*"For [ICP], [Product] is the [Category] that [Unique Value] because [Reason]."*

Example: *"For early-stage founders, Mercury is the business banking platform that handles compliance automatically because founders hate dealing with traditional banks."*

**Your positioning:**
[Insert here]

---

### Key Message Pillars (Max 5)

#### Pillar 1: Problem Validation
- **Message:** [State the problem in customer language, not features]
- **Proof:** [Data, customer quote, stat from research]
- **Why It Matters:** [Connection to their success metric]

#### Pillar 2: Unique Solution
- **Message:** [What's different about your approach?]
- **Proof:** [Competitive differentiation, customer testimonial]
- **Why It Matters:** [Specific outcome they get]

#### Pillar 3: Credibility & Trust
- **Message:** [Why should they believe you?]
- **Proof:** [Case study, customer count, years in market, team creds]
- **Why It Matters:** [Risk reduction]

#### Pillar 4: Desired Outcome
- **Message:** [What's the payoff? What changes for them?]
- **Proof:** [Customer success story, metric improvement]
- **Why It Matters:** [Their version of success]

#### Pillar 5: Social Proof / Movement
- **Message:** [Why are others choosing this? What's the trend?]
- **Proof:** [Case studies, testimonials, community size]
- **Why It Matters:** [FOMO, validation, credibility]

---

### Customer Language Library

**Use these phrases verbatim in copy, emails, ads:**

Pain Point Language (from customer interviews):
- [Quote 1: "[customer pain point in their words]"]
- [Quote 2: "[customer pain point in their words]"]
- [Quote 3: "[customer pain point in their words]"]

Desire Language (what they want):
- [Quote 1: "[desired outcome in their words]"]
- [Quote 2: "[desired outcome in their words]"]

Objection Language (common blockers):
- [Objection 1: "[how they phrase resistance]"]
- [Objection 2: "[how they phrase resistance]"]

---

## Section 3: Brand & Story

### Origin Story
*Why did you start this? What problem motivated you?*

[Your answer, 1–2 paragraphs. Use this in long-form content, landing pages, and about pages.]

---

### Brand Values
*What do you stand for? (Not fluffy, be specific)*

1. [Value 1]: [Why it matters, specific example]
2. [Value 2]: [Why it matters, specific example]
3. [Value 3]: [Why it matters, specific example]

---

### Brand Voice & Personality

- **Tone:** [Casual, formal, technical, playful, irreverent, authoritative?]
- **Vocabulary:** [Jargon level — technical deep-dive or plain English?]
- **Sentence Length:** [Short and punchy, or detailed and thorough?]
- **Humor:** [Funny, dry, none?]
- **Example Phrase:** [How would you describe your product in one sentence, in your voice?]

---

### Narrative Arc (Customer Journey)

**BEFORE:** *[Customer's current situation, pain, frustration]*
> Example: "Most founders spend 30% of their time on operations instead of building."

**MOMENT:** *[The realization or trigger that changes things]*
> Example: "We watched a great product die because operations overhead killed momentum."

**AFTER:** *[New possibility opened up]*
> Example: "What if founders could reclaim that 30% and focus on what matters?"

**MOVEMENT:** *[Invitation to join]*
> Example: "500+ teams have already reclaimed their time. Join the ops revolution."

---

## Section 4: Competitive Positioning

### Direct Competitors
- **Competitor 1:** [Name]
  - Positioning: [How do they position?]
  - ICP: [Who do they target?]
  - Strength: [What are they good at?]
  - Weakness: [Where are they vulnerable?]

- **Competitor 2:** [Name]
  - Positioning: [How do they position?]
  - ICP: [Who do they target?]
  - Strength: [What are they good at?]
  - Weakness: [Where are they vulnerable?]

### Positioning Gaps (Where You Win)
- **Gap 1:** [They don't talk about X, but our ICP cares about X]
- **Gap 2:** [They focus on feature Y, but our ICP cares about outcome Z]
- **Gap 3:** [They target big enterprise, but our ICP is SMB]

### Competitive Advantage
*What can you uniquely claim that competitors can't (or won't)?*
- [Unique claim 1 + proof]
- [Unique claim 2 + proof]

---

## Section 5: Go-To-Market (GTM) Strategy

### Awareness Phase (Weeks 1–4)
**Goal:** Get your ICP to know you exist.

**Primary Channels:**
1. [Channel]: [Tactic — e.g., "Cold email outreach to [title] at [company size]"]
2. [Channel]: [Tactic — e.g., "Content on [topic] targeting [keyword]"]
3. [Channel]: [Tactic — e.g., "Paid ads to [audience]"]

**Budget Allocation:** [%]
**Key Metrics:** [impressions, reach, website traffic, opens]
**Success Threshold:** [e.g., "500 impressions, 50 visits, 10 opens"]

---

### Consideration Phase (Weeks 5–8)
**Goal:** Help them evaluate if you're a fit.

**Primary Tactics:**
1. [Tactic]: [e.g., "Email sequence: problem → solution → proof → CTA"]
2. [Tactic]: [e.g., "Case study on [specific use case]"]
3. [Tactic]: [e.g., "Demo video or product walkthrough"]

**Budget Allocation:** [%]
**Key Metrics:** [engagement rate, click rate, demo requests]
**Success Threshold:** [e.g., "30% email engagement, 5 demo requests"]

---

### Decision Phase (Weeks 9+)
**Goal:** Convert consideration to decision.

**Primary Tactics:**
1. [Tactic]: [e.g., "Sales call with [offer]"]
2. [Tactic]: [e.g., "Free trial with [incentive]"]
3. [Tactic]: [e.g., "Pricing + packaging strategy"]

**Budget Allocation:** [%]
**Key Metrics:** [conversion rate, trial start rate, sales]
**Success Threshold:** [e.g., "5% conversion, 10 trials, 2 sales"]

---

### Post-Launch (Ongoing)
**Retention Tactics:** [How will you keep them happy?]
**Expansion Tactics:** [How will you grow their spend?]
**Feedback Loop:** [How will you learn and improve?]

---

## Section 6: Campaign Calendar

### Q1 Campaign
- **Campaign Name:** [e.g., "Cold Email Blitz"]
- **Timeline:** [Dates]
- **Channels:** [Primary channels for this campaign]
- **Target Audience:** [Specific segment]
- **Messaging Focus:** [Which pillar(s)?]
- **Success Metrics:** [KPIs]
- **Expected Spend:** [$]

### Q2 Campaign
[Repeat above]

---

## Section 7: Metrics & Reporting

### North Star Metric
[What's the one number that matters most? e.g., "Monthly Recurring Revenue" or "Active Users"]

### Supporting Metrics
| Metric | Current | Target (90 days) | Target (6 months) |
|--------|---------|-------------------|-------------------|
| [Awareness metric] | [baseline] | [goal] | [goal] |
| [Engagement metric] | [baseline] | [goal] | [goal] |
| [Conversion metric] | [baseline] | [goal] | [goal] |
| [Retention metric] | [baseline] | [goal] | [goal] |

### Reporting Cadence
- Weekly: [Which metrics? who sees them?]
- Monthly: [Review and iterate?]
- Quarterly: [Deep dive + strategy adjust?]

---

## Section 8: Assumptions & Risks

### Key Assumptions (Mark with [ASSUMED] or [INFERRED])
- [ASSUMED] ICP has budget of [amount] for solutions like ours
- [INFERRED] Cold email will generate 3–5% reply rate based on [data]
- [NEEDS INPUT] Competitor analysis — need to verify [X]

### Known Risks
- **Risk 1:** [Risk description] → Mitigation: [How will you handle it?]
- **Risk 2:** [Risk description] → Mitigation: [How will you handle it?]

---

## Section 9: Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | YYYY-MM-DD | Initial context created |
| 1.1 | YYYY-MM-DD | [Updated ICP based on research] |
| 2.0 | YYYY-MM-DD | [Major pivot in positioning] |

---

## How This Doc Is Used

**This file is loaded by:**
- CLAUDE.md (detects active project)
- All 25+ marketing skills (reference ICP, messaging, channels)
- All execution docs (copywriting, emails, ads pull from messaging pillars)
- Evaluation framework (measures success against defined metrics)

**Update this doc when:**
- You conduct new customer research
- Competitive landscape shifts
- Messaging isn't resonating
- Campaign results suggest ICP changes
- New channel opportunity emerges

**Never:**
- Use outdated context (always check version + date)
- Assume context from previous project applies (each project gets its own file)
- Proceed to execution without confirming this doc is complete and current

---

*Marketing OS v1.0 · Project Context Template · 2026-04-07*
*Template for use by Denis across all marketing projects*
