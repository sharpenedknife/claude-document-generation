# Research Hub — Questionnaire Templates
**Version:** 2.0 · Copy-Paste Ready
**Usage:** Fill and paste into Research Hub to start research session

---

## FOR HUMANS — Universal Research Request

**Copy this template, fill in the blanks, paste into Research Hub:**

```
🔬 RESEARCH REQUEST

Question: [What do you want to know? Be specific.]

Why: [What decision does this support?]

Mode: [Pick 1–6: Competitive | Market | Technical | User Research | Document | Synthesis]
      [Or describe: "I'm researching..."]

Depth: [Quick (3 min) | Standard (5-10 min) | Deep (15-20 min) | Ultradeep (30+ min)]
       [Default: Standard unless urgent/comprehensive needed]

Deadline: [When do you need output? e.g., "today by 3pm" or "no deadline"]

Sources (optional): [Any specific sources? e.g., "focus on Reddit", "only academic papers"]
                    [Or "all sources OK"]

Output Format (optional): [Markdown table | Narrative | JSON | Structured list]
                          [Default: mode-default format]

Additional Context: [Anything else I should know? Constraints, assumptions, team context?]
```

---

## MODE-SPECIFIC TEMPLATES

### 1️⃣ COMPETITIVE RESEARCH

**Copy, fill, paste into Research Hub:**

```
🔬 COMPETITIVE RESEARCH REQUEST

Question: Who are my main competitors and where can I win?

Mode: Competitive

Competitors to analyze: [List 3–5 specific companies/products]
                        Example: "Notion, Obsidian, Roam Research"

Strategic question: [What gap are we looking for?]
                    Example: "We want to position as the 'simple, offline-first' alternative"
                    Or: "What feature are they all missing?"

Market/Geography: [Where do we compete?]
                  Example: "US tech professionals", "Global indie creators", "EU enterprises"

Depth: [Quick | Standard | Deep]

Sources (optional): [Any sources to prioritize? e.g., G2, ProductHunt, official websites]
```

**Expected Output:**
- Competitor comparison table (Name | Features | Weakness | Pricing | Customer)
- 3 differentiation opportunities (ranked by addressable market)
- Recommended positioning (1–2 sentences)
- All claims cited

---

### 2️⃣ MARKET RESEARCH

**Copy, fill, paste into Research Hub:**

```
🔬 MARKET RESEARCH REQUEST

Question: How big is this opportunity?

Mode: Market

Product: [What does it do + who it's for? 2 sentences]
         Example: "A no-code workflow automation tool for non-technical operations managers at mid-market companies"

Target Customer Segment: [Define precisely]
                        Role: [Title, e.g., "Operations Manager"]
                        Company Size: [e.g., "50–500 employees"]
                        Geography: [e.g., "US + Canada"]
                        Industry: [e.g., "Manufacturing, Logistics" or "any"]

Time Horizon: [Current market | 3-year | 5-year]

Sizing Method Preference: [Top-down (analyst reports) | Bottom-up (user acquisition) | Value-theory (willingness to pay) | All 3]

Depth: [Quick | Standard | Deep]

Additional Notes: [Any known benchmarks? Competitive pricing? Customer acquisition cost targets?]
```

**Expected Output:**
- TAM / SAM / SOM with calculations and method
- Key assumptions (each marked: STATED / INFERRED / ASSUMED)
- Market growth rate (if available)
- Confidence level (High / Medium / Low with reasoning)
- All sources cited

---

### 3️⃣ TECHNICAL RESEARCH

**Copy, fill, paste into Research Hub:**

```
🔬 TECHNICAL RESEARCH REQUEST

Question: [What decision are we making?]
          Example: "Should we use PostgreSQL or MongoDB for our feature store?"

Mode: Technical

Options to compare: [List 2–4 specific technologies/frameworks]
                   Example: "LangChain vs LlamaIndex vs OpenAI Assistant API"

Decision criteria (what matters most): [Rank by importance]
                                       1. [Cost / Latency / Dev Experience / Scalability / Security / Support]
                                       2. [Next priority]
                                       3. [Next priority]

Use case context: [What are you building? Scale? Team expertise?]
                 Example: "LLM-powered document Q&A for enterprise customers. Scale: 100K daily queries. Team: 3 engineers, all Python experts"

Depth: [Quick | Standard | Deep]

Sources: [Any official benchmarks or real-world comparisons you know about?]
```

**Expected Output:**
- Comparison table (Option | Pros | Cons | Best For | Cost/Effort)
- Tradeoff analysis matrix (criteria vs options)
- Implementation gotchas (real-world challenges)
- Recommendation + rationale tied to your criteria
- All sources (docs, benchmarks, real code)

---

### 4️⃣ USER RESEARCH

**Copy, fill, paste into Research Hub:**

```
🔬 USER RESEARCH REQUEST

Question: [What do we want to understand about users?]
          Example: "What does the current workflow look like for data analysts doing exploratory analysis?"

Mode: User Research

Target User Profile: [Be specific]
                    Role: [e.g., "Senior Data Analyst"]
                    Context: [Where do they work? Company type? Tools they already use?]
                    Experience Level: [Beginner / Intermediate / Expert]
                    Use Case: [What problem are they solving?]

Problem Area: [What pain point does your product solve?]
              Example: "Current tools are slow to query, hard to iterate on, require SQL expertise"

Sources to explore: [Reddit | G2 Reviews | Twitter/X | YouTube | LinkedIn | Interviews | Other]
                   [Or: "All sources, prioritized by volume"]

Depth: [Quick | Standard | Deep]

Geographic/Industry Focus: [e.g., "US tech companies", "EU fintechs", "Global"]
```

**Expected Output:**
- User profile (detailed portrait)
- Current workflow (step-by-step, without your product)
- Top 3 pain points (ranked by severity)
- First value moment (what makes them say "yes")
- Common objections (why might they resist)
- Direct quotes (minimum 2, with attribution)
- All sources cited

---

### 5️⃣ DOCUMENT ANALYSIS

**Copy, fill, paste into Research Hub:**

```
🔬 DOCUMENT ANALYSIS REQUEST

Question: [What specific question should these docs answer?]
          Example: "What is the current architecture of our data pipeline?"

Mode: Document Analysis

[Attach or paste the documents here — PDF, Markdown, plain text, or URL]

Output Format: [Key findings list | Narrative | JSON | Table | Custom]

Handling contradictions: [Highlight & note sources | Follow most recent | Get consensus]

Depth: [Quick (skim) | Standard (thorough read) | Deep (detailed analysis with cross-references)]

Additional notes: [Any specific sections to focus on? Known gaps in the docs?]
```

**Expected Output:**
- Key findings (numbered, each with source location: page/section)
- Direct answer to your question
- Contradictions (if any, with dates and reasoning)
- Gaps (what the docs don't cover)
- Confidence level (High / Medium / Low)
- All citations include precise location

---

### 6️⃣ SYNTHESIS

**Copy, fill, paste into Research Hub:**

```
🔬 SYNTHESIS REQUEST

Question: [What single coherent picture are we building?]
          Example: "Given all our research on competitors + users + market size, what's our go/no-go recommendation?"

Mode: Synthesis

What we're synthesizing: [Paste findings from other research OR describe the research you want consolidated]

                        Option A: "Here are my findings from competitive + market research..."
                        Option B: "Synthesize findings from Competitive, Market, and User Research modes"

Output audience: [Who is this for? Determines tone + detail]
                 Example: "Executive summary for CEO", "Technical spec for engineering", "Investor pitch"

Key question to answer: [What narrative should tie all findings together?]
                        Example: "Is this market opportunity real + defensible?"

Tone: [Executive / Technical / Investor / Product-focused]

Format: [Narrative summary | Structured bullets | Decision matrix | Story]

Depth: [Quick | Standard | Deep]
```

**Expected Output:**
- Executive summary (3 sentences, one core answer)
- Key insights (5–8 numbered, each tagged STATED / INFERRED / ASSUMED)
- Strategic implications (what to do)
- Risks and opportunities (if applicable)
- Open questions (what still needs research)
- Recommended next step (if needed)

---

## FOR AIs — Cross-Chat Research Handoff Template

**If research started in another chat and you're passing it to Research Hub:**

**Copy this template, fill, paste into Research Hub:**

```
🤖 AI RESEARCH HANDOFF (For Research Hub)

Context: [Project brief, 1–2 sentences]
         Example: "Building an AI-powered market research platform. Targeting startups in Series A/B looking to make data-driven decisions."

Research Question: [What needs researching?]

Mode: [1–6: Competitive | Market | Technical | User | Document | Synthesis]

Depth: [Quick | Standard | Deep | Ultradeep]

What's already known: [Any context from the original chat?]
                     Example: "We know there are 5 direct competitors. Market size estimated at $2B. Tech stack: Python + LLM."

Sources to prioritize: [Any specific domains or types? e.g., "G2 reviews", "academic papers", "GitHub repos"]

Sources to avoid: [e.g., "No gated content", "No TechCrunch articles", "Skip vendors' own marketing"]

Output format required: [Markdown | JSON | Structured list | Narrative | Raw findings]

How will this research be used? [Helps Hub optimize output tone/detail]
                               Example: "Engineering team will use this for architecture decision"

Return location: [Where should findings go?]
                Example: "Paste findings back in [original chat name]"

Confidence requirements: [High confidence needed? Can we do quick research?]
                        Example: "High confidence needed for investor pitch"
```

**Key Rules for AI-to-AI Research:**
1. Be specific in questions (vague questions = vague research)
2. Mark your output format explicitly (JSON vs narrative matters)
3. Tell Hub how the research will be used (helps with tone + rigor level)
4. Specify confidence requirements upfront
5. Always include "return location" so findings get back to the right place

---

## HOW TO USE THESE TEMPLATES

### For Humans (Chat Mode)

1. **Pick your research mode** (1–6)
2. **Copy the mode-specific template** from above
3. **Fill in all blanks** (skip optional fields if not needed)
4. **Paste into Research Hub**
5. **Get back structured research** in expected format

### For AIs (Cross-Chat Handoff)

1. **In your original chat, fill the AI research handoff template**
2. **Paste entire template + context into Research Hub**
3. **Research Hub executes + returns findings in your requested format**
4. **Copy findings back to original chat** and continue

---

## TIPS FOR BEST RESULTS

**Be Specific:**
- ❌ "Research competitors"
- ✅ "Who are the top 5 Notion competitors and what's our differentiation opportunity in offline-first?"

**State the Decision:**
- ❌ "Tell me about vector databases"
- ✅ "Should we use Pinecone or Weaviate for our RAG pipeline? Context: 100K documents, real-time retrieval, cost-sensitive"

**Show Your Constraints:**
- ❌ "Research the market"
- ✅ "Size the TAM for AI-powered code review tools targeting mid-market engineering teams in North America, current year"

**Depth = Trade-off:**
- Quick = fast answer, fewer sources, good enough for directional decisions
- Standard = balanced (5–10 min, multiple sources, good for most decisions)
- Deep = comprehensive (15–20 min, exhaustive sources, for critical decisions)

---

*Questionnaire Templates v2.0 · April 2026*
*Copy-paste ready. Fill-in-the-blanks. Ready to research.*
