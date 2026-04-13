# Research Hub — Research Mode Guides
**Version:** 2.0 · Frameworks + Execution for All 6 Modes
**Purpose:** Step-by-step guides for each research type

---

## 1️⃣ COMPETITIVE RESEARCH

### Framework: Porter's Five Forces + Positioning Map

**Porter's Five Forces Applied to Your Competitive Position:**
- Threat of new entrants (how easy is it to enter this market?)
- Bargaining power of buyers (how much control do customers have?)
- Bargaining power of suppliers (how much control do vendors have?)
- Threat of substitutes (what else solves this problem?)
- Rivalry among competitors (how intense is competition?)

**Your position:** Where do you have the least competition or the highest defensibility?

---

### Execution Steps

**Step 1 — Competitor Discovery**
- Identify 3–5 direct competitors (ask: "Who do our target customers consider as alternatives?")
- For each: visit product, read G2 reviews, check pricing page, scan product roadmap
- Document: core features, target customer, pricing, positioning

**Step 2 — Gap Analysis**
- What features does EVERY competitor have? (table stakes)
- What features do SOME have? (differentiators)
- What features does NO ONE have? (white space opportunity)
- Rank opportunities by: addressable market size × competitive intensity

**Step 3 — Positioning**
- What is our defensible difference? (not just features, but value angle)
- Who do we win against? (which competitor's customers would choose us?)
- What is our 1-sentence position? (fill this template)
  - "We are the [category] for [customer] who care about [value], unlike [competitor] which is [what they are]"

---

### Output Template

```
## Competitive Research Findings

**Competitors Analyzed:** [List names]

### Competitor Landscape Table

| Competitor | Core Features | Customer Target | Pricing | Weakness |
|------------|--------------|-----------------|---------|----------|
| [Name]    | [List]       | [Role/Company]  | [$/mo]  | [Gap]    |
| [Name]    | [List]       | [Role/Company]  | [$/mo]  | [Gap]    |

### White Space Opportunities (Ranked by Market Size)

1. **[Opportunity]** (Market size: __, Addressable to us: __)
   - Who wants this: [Target customer]
   - Why competitors haven't done it: [Reason]
   - Source: [URL / quote]

2. **[Opportunity]**
3. **[Opportunity]**

### Recommended Positioning

"We are the [category] for [customer] who [value], unlike [competitor name]."

### Strategic Implications

- We can win customers from: [Competitor 1, Competitor 2]
- We should NOT compete with: [Competitor who owns this]
- First marketing angle to test: [1-2 sentences]

**Confidence:** High / Medium / Low
**Sources:** [Cited above with [source: domain] tags]
**What's Still Unknown:** [Any gaps in competitive landscape?]
```

---

## 2️⃣ MARKET RESEARCH

### Framework: TAM / SAM / SOM (Total / Serviceable / Obtainable)

**TAM (Total Addressable Market):**
- Global opportunity for the problem you solve
- "How many people have this problem worldwide?"
- Method: Top-down (analyst reports) or bottom-up (sum customer segments)

**SAM (Serviceable Addressable Market):**
- Market segment YOU can realistically serve
- "How many of those people are in our target geography + company type?"
- Usually 5–15% of TAM

**SOM (Serviceable Obtainable Market):**
- Realistic Year 1 capture (how many customers can you actually win?)
- Usually 5–15% of SAM, or based on sales targets
- Most actionable number for go/no-go decisions

---

### Execution Steps

**Step 1 — TAM Sizing (Pick one or both methods)**

**Top-Down:**
- Find analyst report (Gartner, IDC, CB Insights) for your category
- Cite: current market size + CAGR
- Example: "Gartner reports the workflow automation market is $5B, growing at 15% CAGR"

**Bottom-Up:**
- Count addressable customers: [Segment 1 size] + [Segment 2 size] + [Segment 3 size]
- Multiply by [average willingness to pay]
- Example: "1M mid-market companies × $500/year = $500M TAM"

**Step 2 — SAM Sizing**
- Apply your constraints: geography (e.g., US only) + company size (e.g., 50–500 employees) + industry (e.g., Tech)
- Calculate: "TAM × [% that fits your constraints] = SAM"
- Example: "TAM $5B × 10% (only US tech companies) = $500M SAM"

**Step 3 — SOM Sizing**
- Year 1 realistic capture: [Acquisition strategy] × [time to reach customers]
- Example: "100 customers × $10K ACV = $1M Year 1 SOM" (validate this is achievable)

**Step 4 — List All Assumptions**
- What did you ASSUME vs INFER vs get from data?
- Mark confidence: High (backed by research) / Medium (reasonable estimate) / Low (guess)

---

### Output Template

```
## Market Research Findings

### TAM / SAM / SOM

| Metric | Size | Method | Key Assumption |
|--------|------|--------|-----------------|
| **TAM** | $[X]B | Top-down: [source] / Bottom-up: [method] | [Assumption with confidence] |
| **SAM** | $[X]M | TAM × [%] (for US / mid-market / tech only) | [Assumption with confidence] |
| **SOM** | $[X]M | [Acquisition plan] × [customers achievable Year 1] | [Assumption with confidence] |

**Overall Confidence:** High / Medium / Low
**Reasoning:** [Why we trust or don't trust these numbers]

### Market Growth

- Current CAGR: [X]% (source: [analyst report])
- Growth drivers: [Trend 1], [Trend 2], [Trend 3]
- Headwinds: [Risk 1], [Risk 2]

### Key Assumptions (Detailed)

1. **[Assumption]** — Confidence: High / Medium / Low
   - Basis: [Cited data or reasoning]
   - Validation method: [How to verify this]

2. **[Assumption]**

### Strategic Implications

- Is this big enough for a venture-scale business? [Yes/No, reasoning]
- Who is our most addressable sub-segment? [Specific description]
- What would make this market larger? [1–2 growth levers]

**Sources:** [All cited]
**What's Still Unknown:** [Gaps in market data]
**Suggested Next Research:** [How to get more confidence]
```

---

## 3️⃣ TECHNICAL RESEARCH

### Framework: Decision Matrix (Criteria × Options)

| Criteria (weighted) | Option A | Option B | Option C | Winner |
|-----|-----|-----|-----|-----|
| Cost (weight: 30%) | $500/mo | $2,000/mo | $100/mo | C |
| Latency (weight: 40%) | 100ms | 20ms | 500ms | B |
| Developer Experience (weight: 20%) | 7/10 | 8/10 | 5/10 | B |
| Scalability (weight: 10%) | 1M/day | 10M/day | 100K/day | B |
| **SCORE** | 6.1 | 7.8 | 3.5 | **B** |

---

### Execution Steps

**Step 1 — Define Decision Criteria**
- What matters most for YOUR use case?
- Weight them: cost (30%) + performance (40%) + ease (20%) + scalability (10%) [adjust to your priorities]

**Step 2 — Research Each Option**
- Official docs: features, pricing, performance benchmarks
- Real-world comparisons: GitHub discussions, Reddit, blog posts with actual usage
- Known limitations: common gotchas, setup complexity, support quality

**Step 3 — Score Each Option**
- Against each criterion: 0–10 score
- Multiply by weight
- Total = decision recommendation

**Step 4 — Highlight Tradeoffs**
- What do you gain/lose with each choice?
- "Option B is 10x faster but costs 4x more"
- "Option C is cheapest but doesn't scale"

---

### Output Template

```
## Technical Research Findings

### Decision Question
[Your decision question]

### Options Evaluated
[List of 2–4 options]

### Decision Criteria (Weighted)
1. [Criterion] — [%] weight — [Justification]
2. [Criterion] — [%] weight
3. [Criterion] — [%] weight

### Comparison Table

| Criteria | [Option A] | [Option B] | [Option C] |
|----------|-----------|-----------|-----------|
| [Criterion 1] | [Score/10] | [Score/10] | [Score/10] |
| [Criterion 2] | [Score/10] | [Score/10] | [Score/10] |
| **Weighted Score** | **[X.X]** | **[X.X]** | **[X.X]** |

### Detailed Comparison

**Option A: [Name]**
- Pros: [Feature], [Benefit], [Advantage]
- Cons: [Limitation], [Cost], [Challenge]
- Best for: [Use case where it shines]
- Cost: [Detailed pricing breakdown]
- Learning curve: [How hard to implement]
- Source: [Official docs + real-world references]

**Option B: [Name]**
- Pros, Cons, Best for, Cost, Learning curve, Source

**Option C: [Name]**
- Pros, Cons, Best for, Cost, Learning curve, Source

### Key Tradeoffs

- **Speed vs Cost:** Option B is fastest but 4x more expensive than Option C
- **Ease vs Performance:** Option A easiest to set up but slowest in production
- **Flexibility vs Simplicity:** Option C most flexible but requires more custom code

### Implementation Gotchas (Real-World Challenges)

1. **[Option A Gotcha]** — How to avoid it: [Solution]
2. **[Option B Gotcha]** — How to avoid it: [Solution]
3. **[Option C Gotcha]** — How to avoid it: [Solution]

### Recommendation

**We recommend: [Option A / B / C] because:**
- Aligns best with our priorities: [Criteria 1], [Criteria 2], [Criteria 3]
- Tradeoff analysis: [Why we chose this over others]
- Implementation risk: [What could go wrong and how to mitigate]

**Confidence:** High / Medium / Low
**Sources:** [Cited in sections above]
**What's Still Unknown:** [Gaps in technical data — e.g., "Haven't tested at 10M scale yet"]
**Suggested Next Step:** [Run POC / Get team consensus / Decision review]
```

---

## 4️⃣ USER RESEARCH

### Framework: Jobs to Be Done (JTBD)

**The Job:** What is the user trying to accomplish in their workflow?
**The Pain:** What's hard about doing it today?
**The Gain:** What would make them say "this is perfect"?

---

### Execution Steps

**Step 1 — Define User Segment**
- Role, context, experience level
- "Senior data analyst at mid-market SaaS, 5+ years experience, building internal dashboards"

**Step 2 — Current Workflow (Without Your Solution)**
- Step-by-step: How do they do it today?
- Tools they use: [Tool 1], [Tool 2], [Manual process]
- Time investment: How long does it take?
- Friction points: Where do they get stuck?

**Step 3 — Pain Points**
- What's hard? (Rank by frequency and severity)
- Example: "Current tool requires SQL expertise (barrier: 80% of ops managers don't have it)"

**Step 4 — First Value Moment**
- What makes them say "yes, this is for me"?
- Not a full feature list — one specific moment where it clicks
- Example: "Dragging 3 fields and seeing instant results without writing code"

**Step 5 — Common Objections**
- Why might they NOT adopt your solution?
- Switching costs ("We've already trained people on the old tool")
- Fear ("What if I mess up the data?")
- Skepticism ("Does it really work without SQL?")

---

### Output Template

```
## User Research Findings

### User Profile

**Role:** [Title, context]
**Experience Level:** [Beginner / Intermediate / Expert]
**Company Type:** [Size, industry]
**Use Case:** [What are they trying to accomplish?]

**Direct Quote:** "[Quote about their problem]" — [Source, date]

### Current Workflow (Today, Without Your Solution)

1. [Step 1] — Pain point: [What's hard here?]
2. [Step 2] — Pain point: [What's hard here?]
3. [Step 3] — Pain point: [What's hard here?]

**Tools used:** [Tool 1], [Tool 2], [Manual process]
**Time investment:** [X hours/week]

### Top 3 Pain Points

1. **[Pain point]** — Severity: Critical / High / Medium
   - Why it matters: [Impact on their work]
   - Who feels it most: [User segment]
   - Source: [Reddit thread / G2 review / Interview quote]

2. **[Pain point]** — Severity: Critical / High / Medium
3. **[Pain point]** — Severity: Critical / High / Medium

### First Value Moment (What Makes Them Say "Yes")

"[Specific moment/action] without [barrier/friction]"

Example: "Being able to create a custom report by dragging 3 fields, no SQL required"

**Source:** [User quote / Interview / Observation]

### Common Objections (Why They Might Resist)

1. **[Objection]** — How to address: [Solution]
   - Frequency: [How common is this objection?]
   - Severity: [Deal-breaker or nice-to-have?]

2. **[Objection]** — How to address: [Solution]
3. **[Objection]** — How to address: [Solution]

### Voice of Customer

**Direct Quotes (minimum 2):**
- "[Quote 1]" — [Source: Reddit thread / G2 / Interview]
- "[Quote 2]" — [Source]

### Strategic Implications

- What is our earliest adopter segment? [Specific profile]
- What messaging would resonate most? [Value proposition test]
- What feature is non-negotiable for MVP? [Based on pain points]

**Confidence:** High / Medium / Low
**Sources:** [Reddit, G2, Twitter, interviews — linked]
**What's Still Unknown:** [e.g., "Haven't interviewed power users yet"]
**Suggested Next Research:** [Customer interviews / User testing / Segment validation]
```

---

## 5️⃣ DOCUMENT ANALYSIS

### Framework: Extraction + Synthesis + Gap Identification

---

### Execution Steps

**Step 1 — Clarify the Question**
- What specific answer are we looking for?
- Not "Tell me about this doc" but "Does this doc explain X? What's the current Y?"

**Step 2 — Skim for Structure**
- Table of contents, headings, key sections
- Where might the answer be?

**Step 3 — Extract Findings**
- Each finding gets: statement + exact source location (page/section) + confidence
- [STATED] = document explicitly says it
- [INFERRED] = logically deducible from document
- [ASSUMED] = making an educated guess (mark as such)

**Step 4 — Identify Contradictions**
- Do different parts of the doc contradict?
- Do multiple docs say different things?
- Note: source, date, context for each

**Step 5 — Flag Gaps**
- What the document does NOT say
- What would be valuable to know but isn't covered
- Recommend next research

---

### Output Template

```
## Document Analysis Findings

**Document(s) Analyzed:** [List with dates]

**Research Question:** [What we were looking for]

### Key Findings

1. **[Finding]** — [Page / Section reference]
   - Basis: [STATED / INFERRED / ASSUMED]
   - Direct quote: "[Quote from doc]"
   - Confidence: High / Medium / Low

2. **[Finding]** — [Page / Section reference]
   - Basis: [STATED / INFERRED / ASSUMED]
   - Direct quote: "[Quote from doc]"
   - Confidence: High / Medium / Low

[Continue for all findings]

### Direct Answer to Your Question

[1–2 sentences, directly addressing what you asked]

### Contradictions Found

1. **[Contradiction]**
   - Source A says: [Quote + page]
   - Source B says: [Quote + page]
   - Most likely explanation: [Date difference? Context difference?]
   - Recommendation: Trust [Source] because [reasoning]

2. **[Contradiction]**

[Or: "No contradictions found"]

### Gaps (What's NOT Covered)

- [Gap 1] — Would be valuable to know
- [Gap 2] — Unclear from documents
- [Gap 3] — Recommend researching separately

### Confidence Assessment

- Overall confidence in findings: High / Medium / Low
- Reasoning: [Source quality, recency, consistency]

**Sources:** [All documents cited above with page references]
**What's Still Unknown:** [Gaps and follow-up questions]
**Suggested Next Research:** [If needed]
```

---

## 6️⃣ SYNTHESIS

### Framework: Thematic Analysis + Pattern Recognition

**What you're doing:** Taking multiple research findings and building ONE coherent narrative.

**Not a:** Sum of findings (that's a report)
**Actually a:** Single story about what all this data means together

---

### Execution Steps

**Step 1 — List All Findings**
- Paste or describe competitive findings, market findings, user research, etc.
- Each source is labeled with [STATED], [INFERRED], [ASSUMED]

**Step 2 — Find Themes**
- What patterns do you see across findings?
- Example: All competitors target large enterprises, but users are mid-market → GAP
- Example: Market growing 20% CAGR but users report high friction → OPPORTUNITY

**Step 3 — Build One Narrative**
- What is the single story these findings tell?
- Not "We learned X, Y, Z" but "The market is moving toward [direction] because [reason]"

**Step 4 — Derive Implications**
- If this narrative is true, what should we DO?
- Go / No-go decision?
- Pivot the product?
- Change messaging?

**Step 5 — Identify Open Questions**
- What still needs research?
- What contradicts?
- What assumptions need validation?

---

### Output Template

```
## Synthesis Findings

### Executive Summary

[One paragraph, 3 sentences max, answers the core question directly]

Example: "The market is real and growing (+20% CAGR), but all incumbents are locked into serving large enterprises. Mid-market users report critical friction around ease-of-use and pricing. We have a clear positioning opportunity."

### Key Insights (Synthesized Across Findings)

1. **[Insight]** — Backed by: [Competitive + Market research]
   - What we learned: [Statement]
   - Basis: [STATED / INFERRED / ASSUMED]
   - Confidence: High / Medium / Low
   - Implication: [What to do with this insight]

2. **[Insight]** — Backed by: [User research + Document analysis]
   - What we learned: [Statement]
   - Basis: [STATED / INFERRED / ASSUMED]
   - Confidence: High / Medium / Low
   - Implication: [What to do with this insight]

[Continue for 5–8 key insights]

### Strategic Implications & Recommendation

**Go / No-go decision:** [Go / No-go with reasoning]

**Recommended next steps:**
1. [Action based on findings]
2. [Action based on findings]
3. [Action based on findings]

**Risks to monitor:**
- [Risk 1 based on assumptions]
- [Risk 2 based on gaps]

**Opportunities to pursue:**
- [Opportunity 1]
- [Opportunity 2]

### Open Questions (What Still Needs Research)

- [Gap 1] — How to fill it: [Suggested research]
- [Gap 2] — How to fill it: [Suggested research]
- [Contradiction 1] — How to resolve: [Suggested research]

**Overall Confidence:** High / Medium / Low
**Reasoning:** [Why we do or don't trust this narrative]

**Sources:** [All research findings cited]
**Suggested Next Research:** [Priority order if continuing]
```

---

*Research Mode Guides v2.0 · April 2026*
*Frameworks + execution for production research.*
# Research Hub — Setup Guide
**Version:** 2.0 · Chat + Cowork Installation
**Time to deploy:** 10 min (Chat) / 20 min (Cowork)

---

## OPTION A: CHAT MODE (Recommended for First-Time Users)

### Quick Start (5 minutes)

1. **Create a new Claude Project**
   - Go to Claude.ai → New Project
   - Name it: "Research Hub"

2. **Upload Knowledge Base (Optional)**
   - Copy the following files into the project's knowledge base:
   - `CLAUDE.md` (project instructions)
   - `OPERATING_RULES.md` (research gates + quality scoring)
   - `RESEARCH_MODE_GUIDES.md` (frameworks for each mode)
   - `QUESTIONNAIRE_TEMPLATES.md` (copy-paste templates)

3. **Set Custom Instructions**

   **Field: "What would you like Claude to know?"**
   ```
   I am the Research Hub — a specialized AI workspace for conducting structured research across 6 modes:
   1. Competitive (positioning, gaps, differentiation)
   2. Market (TAM/SAM/SOM sizing, trends)
   3. Technical (tool/architecture comparisons, tradeoffs)
   4. User Research (workflows, pain points, objections)
   5. Document Analysis (extract insights from uploaded files)
   6. Synthesis (consolidate findings into strategic narrative)

   Every research output is:
   - Structured (mode-specific framework applied)
   - Cited (all claims backed by sources, marked [source: URL])
   - Marked (assumptions tagged [STATED]/[INFERRED]/[ASSUMED])
   - Actionable (clear implications and next steps)

   My operating constraints:
   - Token efficiency: 500–2,000 tokens per research (depth-dependent)
   - Zero hallucination: Never cite sources I haven't found
   - Quality gates: Auto-score every research output (target: 85+/100)
   ```

   **Field: "How would you like to respond?"**
   ```
   RESEARCH HUB OPERATING RULES:

   1. START EVERY SESSION with the menu (show 6 research modes)
   2. RUN THE 4-GATE WORKFLOW:
      - Gate 1: Identify mode (user picks or you classify)
      - Gate 2: Collect Tier 1 context ("What?" + "Why?")
      - Gate 3: Run mode-specific research gate (3–5 questions)
      - Gate 4: Execute research + return findings in output format

   3. APPLY THE FRAMEWORK for that mode (see RESEARCH_MODE_GUIDES.md)

   4. STRUCTURE ALL OUTPUTS as:
      - Executive Summary (3 sentences max)
      - Key Findings (numbered, each marked [STATED]/[INFERRED]/[ASSUMED])
      - Framework Analysis (Porter's 5 Forces, TAM/SAM/SOM, JTBD, etc.)
      - Implications & Next Steps
      - Confidence Level (High/Medium/Low with reasoning)
      - What's Still Unknown
      - Suggested Next Research

   5. MARK EVERY CLAIM with basis:
      - [STATED] = user provided
      - [INFERRED] = logical deduction
      - [ASSUMED] = best guess (needs validation)

   6. CITE ALL SOURCES inline: [source: URL/document]
      - Never hallucinate sources. If unknown: "Source not found. Recommend searching [X]"

   7. AUTO-SCORE EVERY RESEARCH before returning:
      - Factuality (25 pts): All claims cited?
      - Completeness (25 pts): Answers the question?
      - Structure (25 pts): Output contract met?
      - Actionability (25 pts): Can user/AI act on this?
      - Minimum pass: 85/100. If below, rerun.

   8. NO VAGUE LANGUAGE. Ban these words in outputs:
      "should, may, might, consider, try, could, seems, appears, possibly, perhaps, maybe"
      Use instead: "IS", "WILL", "DOES", "MUST", "APPLY", "USE"

   9. LOAD SKILLS ON-DEMAND ONLY (see SKILL_LOADING.md):
      - Competitive: competitive-analysis + prompt-engineering-patterns
      - Market: ai-product-strategy + building-with-llms
      - Technical: evaluating-new-technology + ai-evals
      - User: customer-research + conducting-user-interviews
      - Document: building-with-llms (RAG) + prompt-engineering
      - Synthesis: ai-evals + prompt-engineering-patterns

   10. TOKEN OPTIMIZATION:
       - Web search first (factual lookups, 0 tokens)
       - Synthesize only when needed
       - Quick mode: 500–800 tokens
       - Standard mode: 1,200–1,600 tokens
       - Deep mode: 1,800–2,200 tokens
   ```

4. **Add Conversation Starters (Optional but Recommended)**

   Set these to help users jump in fast:
   - 🎯 "Research a market" — Size the opportunity and map competitive landscape
   - 🔍 "Competitive deep-dive" — Who are my top competitors and their positioning?
   - 💡 "Technical evaluation" — Should I use [Tool A] or [Tool B]?
   - 👥 "User research" — What do my target users actually need?
   - 📄 "Analyze documents" — I'll upload files; extract key insights
   - 🧩 "Synthesize findings" — Consolidate all research into one story

5. **Test It**
   - Click "Research a market"
   - Fill the market research questionnaire template (from QUESTIONNAIRE_TEMPLATES.md)
   - Get back structured TAM/SAM/SOM findings

---

## OPTION B: COWORK MODE (For Multi-Agent Research)

### Setup (15–20 minutes)

Cowork mode lets you spawn parallel agents for research (one per competitor, one per market segment, etc.) and have them coordinate.

**Prerequisites:**
- Cowork installed on your machine
- Access to the new-skills folder

**Step 1 — Install Core Skills to Cowork**

Copy these skills to `~/.claude/skills/`:

```bash
# From your new-skills folder, copy:
cp -r agents-main/plugins/llm-application-dev/skills/prompt-engineering-patterns ~/.claude/skills/
cp -r agents-main/plugins/llm-application-dev/skills/llm-evaluation ~/.claude/skills/
cp -r agents-main/plugins/business-analytics/skills/data-storytelling ~/.claude/skills/
cp -r agents-main/plugins/conductor/skills/context-driven-development ~/.claude/skills/

# For multi-agent orchestration:
cp -r agents-main/plugins/agent-teams/skills/team-composition-patterns ~/.claude/skills/
cp -r agents-main/plugins/agent-teams/skills/task-coordination-strategies ~/.claude/skills/

# Deep research skill:
cp -r claude-deep-research-skill-main ~/.claude/skills/deep-research
```

**Step 2 — Create Project Context Files**

Create a `conductor/` directory for your research project:

```
research-hub/
├── product.md          (project brief)
├── tracks.md           (active research tracks)
└── workflow.md         (research process)
```

**product.md:**
```markdown
# Research Hub Project

## Project Brief
AI-powered research utility for [your use case].

## Key Questions
1. [Main research question 1]
2. [Main research question 2]
3. [Main research question 3]

## Constraints
- Token budget: X per research
- Depth: Standard (unless specified)
- Sources: Web + documents (internal knowledge base TBD)

## Success Metrics
- Research quality score: 85+/100
- Time to research: <15 min per request
- Sources cited: 100%
```

**tracks.md:**
```markdown
# Active Research Tracks

## Track 1: Competitive Analysis
- Status: In progress / Not started
- Agents: 1 per competitor (e.g., CompetitorA-Analyzer, CompetitorB-Analyzer)
- Output: Competitive landscape table + gaps

## Track 2: Market Sizing
- Status: In progress / Not started
- Agents: 1 per method (TAM-Calculator, SAM-Calculator, SOM-Estimator)
- Output: TAM/SAM/SOM with assumptions

## Track 3: User Research
- Status: In progress / Not started
- Agents: 1 per user segment (Enterprise-Users, SMB-Users, Indie-Users)
- Output: User profiles + pain points + quotes

[Add your research tracks]
```

**Step 3 — Spawn Research Agents**

Example: Competitive research with parallel agents

```
# Spawn one agent per competitor
cowork spawn research-hub --mode=competitive --competitor=Notion --task="Analyze Notion's positioning, features, pricing, weakness"
cowork spawn research-hub --mode=competitive --competitor=Obsidian --task="Analyze Obsidian's positioning, features, pricing, weakness"
cowork spawn research-hub --mode=competitive --competitor=Roam --task="Analyze Roam's positioning, features, pricing, weakness"

# Coordinator agent synthesizes results
cowork spawn research-hub --mode=competitive --role=coordinator --task="Consolidate findings into competitive landscape + gaps"
```

**Step 4 — Coordinate Results**

Use `task-coordination-strategies` skill to:
- Track dependencies (e.g., Coordinator waits for all Analyzer agents to finish)
- Consolidate outputs (merge findings into single report)
- Score quality (apply OPERATING_RULES.md quality gates)

---

## KNOWLEDGE BASE: EXTERNAL SOURCES (v2.0)

### Sources Included in Research Hub

**Web Search (Primary):**
- Google Search (via WebSearch)
- Bing (via WebSearch)
- Specialized domains (arxiv.org, crunchbase.com, g2.com, reddit.com, twitter.com)

**Academic & Market Data:**
- ArXiv (AI/ML papers)
- Scholar.google.com (academic research)
- Gartner reports (enterprise market data)
- CB Insights (startup data)
- PitchBook (funding data)

**User Voices:**
- Reddit (communities, pain points)
- ProductHunt (early adopter feedback)
- G2 Reviews (customer testimonials)
- Twitter/X (community discussions)
- YouTube comments (user sentiment)

**Technical Documentation:**
- GitHub (code, repos, discussions)
- Official product documentation
- Stack Overflow (implementation questions)
- Blog posts (real-world usage)

### Document Analysis (Upload Files)

For document research, you can upload:
- PDF files
- Markdown (.md)
- Plain text (.txt)
- Screenshots

Hub uses RAG (Retrieval-Augmented Generation) for semantic search within documents.

### Internal Knowledge Base (Backlog — v3.0)

Coming soon: Ability to ingest and index your own:
- Internal wikis
- Previous research archives
- Company documents
- Customer interviews
- Product specifications

---

## TROUBLESHOOTING

### "Research quality score is below 85/100"

**Possible causes:**
- Sources not cited: Add inline [source: URL] tags
- Vague language: Replace "should" with "IS" or "WILL"
- Incomplete answer: Does it directly answer the question?
- Missing confidence level: Add "Confidence: High/Medium/Low" section

**Fix:** Rerun the research with clearer scope or higher depth level.

### "I'm spending too many tokens"

**Optimization steps:**
1. Use "Quick" mode (500–800 tokens) for directional decisions
2. Narrow scope: "US market only" instead of "global market"
3. Fewer sources: 3–5 credible sources instead of 10+
4. Web search first: Don't synthesize until you have data

### "Results feel shallow"

**Depth progression:**
- Quick (3 min): Directional answer from 1–2 sources
- Standard (5–10 min): Balanced answer from 5–7 sources ← DEFAULT
- Deep (15–20 min): Comprehensive from 10+ sources with analysis
- Ultradeep (30+ min): PhD-level rigor, multiple frameworks

**Fix:** Specify "Deep" mode in questionnaire.

### "Contradictions between sources"

**This is normal and valuable.** Hub will:
1. Flag the contradiction explicitly
2. Note source, date, context for each
3. Recommend which to trust based on recency + credibility
4. Suggest how to resolve (e.g., "Contact both vendors for clarification")

---

## NEXT STEPS

1. **Choose your deployment:** Chat (easy) or Cowork (powerful)
2. **Pick your first research** using conversation starters
3. **Fill the questionnaire template** for your mode
4. **Review the research output** against quality gates (OPERATING_RULES.md)
5. **Act on findings** → next step recommendation

---

## SKILL LOADING REFERENCE

**To minimize tokens, load only relevant skills per research mode:**

| Mode | Primary Skill | Secondary Skill |
|------|--------------|-----------------|
| Competitive | competitive-analysis | prompt-engineering-patterns |
| Market | ai-product-strategy | building-with-llms |
| Technical | evaluating-new-technology | ai-evals |
| User | customer-research | conducting-user-interviews |
| Document | building-with-llms | prompt-engineering-patterns |
| Synthesis | ai-evals | prompt-engineering-patterns |

Never preload all skills. Load on-demand only.

---

*Setup Guide v2.0 · April 2026*
*Deploy in 5–20 minutes. Research in minutes.*
