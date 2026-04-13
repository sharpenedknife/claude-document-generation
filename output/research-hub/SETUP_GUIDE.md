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
