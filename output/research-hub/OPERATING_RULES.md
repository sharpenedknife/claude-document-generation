# Research Hub — Operating Rules
**Version:** 2.0 · Detailed Gates + Quality Scoring
**Purpose:** Hardened procedures for research execution across all 6 modes

---

## MODE-SPECIFIC RESEARCH GATES

Each mode has a 3-question research gate. Validate before executing.

### 1️⃣ COMPETITIVE RESEARCH GATE

**Input Questions:**
1. **Who are the top 3–5 competitors to focus on?** (avoid rabbit holes)
   - *If vague:* "List specific company names or products"
2. **What's the key strategic question?** (positioning gap, feature differentiation, market shift)
   - *If missing:* "We're researching to [decide positioning / find market gap / understand threat]"
3. **What market/geography should we focus on?** (US tech? EU? Global?)
   - *If global:* "Limiting scope to [geography] for tractability"

**Execution:**
- Web search for each competitor: product, positioning, pricing, target customer
- Identify gaps (features, segments, use cases they're NOT serving)
- Build competitor landscape table
- Derive 3 differentiation opportunities + recommended positioning

**Output Format:**
- Competitor comparison table (Name | Core Features | Weakness | Pricing | Target Customer)
- Differentiation opportunities (ranked by addressable market size)
- Recommended positioning (1–2 sentences)
- Sources (inline citations, minimum 3 per competitor)

**Quality Score Weights:**
- Competitor coverage: 25% (all requested competitors analyzed)
- Gap identification: 25% (actionable, specific opportunities)
- Source quality: 25% (credible, recent sources only)
- Clarity: 25% (no ambiguity, AI can act on this)

**Token Budget:** 800–1,500 (quick to standard) / 2,000+ (deep)

---

### 2️⃣ MARKET RESEARCH GATE

**Input Questions:**
1. **What's your target customer segment?** (role, company size, geography, use case)
   - *If vague:* "Define: title/role, company size range, industry"
2. **What's the time horizon?** (current market? 3-year projection? 5-year?)
   - *Default:* Current year unless specified
3. **Which sizing method?** (top-down: analyst reports; bottom-up: user acquisition; value-theory: willingness to pay)
   - *Default:* Top-down + bottom-up for triangulation

**Execution:**
- TAM (Total Addressable Market): global opportunity for this problem
- SAM (Serviceable Addressable Market): your segment only
- SOM (Serviceable Obtainable Market): realistic Year 1 capture
- Include method for each (explain the math)
- List all assumptions (mark CONFIRMED / INFERRED / ASSUMED)

**Output Format:**
- TAM / SAM / SOM with calculations and method
- Key assumptions (each marked with confidence: High/Medium/Low)
- Market growth rate (if available)
- Sources (minimum 5 credible sources for sizing)
- Confidence level (High/Medium/Low with reasoning)

**Quality Score Weights:**
- Sizing rigor: 30% (justified method, not guesses)
- Assumption transparency: 25% (every assumption marked + sourced)
- Source quality: 25% (analyst reports, SEC filings, industry surveys)
- Actionability: 20% (clear implications for go/no-go decision)

**Token Budget:** 900–1,600 (quick to standard) / 2,000+ (deep)

---

### 3️⃣ TECHNICAL RESEARCH GATE

**Input Questions:**
1. **What decision does this research support?** (e.g., "Choose between vector DBs", "Decide on auth approach")
   - *If missing:* Stop — research is only useful if tied to a decision
2. **What are the 2–4 options to compare?** (specific tools, approaches, or frameworks)
   - *If >5:* "Narrowing to top 4 based on [criteria]. Others considered: [list]"
3. **What matters most?** (latency, cost, dev experience, scalability, security, support)
   - *If unclear:* Assume: ease of setup > cost > performance (adjust if wrong)

**Execution:**
- For each option: pros, cons, best-use-case, cost, learning curve
- Tradeoff analysis: show what you gain/lose with each choice
- Real-world gotchas (common pitfalls, setup challenges)
- Recommendation with rationale (tied to decision criteria)

**Output Format:**
- Comparison table (Option | Pros | Cons | Best For | Cost / Effort)
- Tradeoff analysis (matrix: criteria vs options, weighted scoring)
- Gotchas (implementation realities, common mistakes)
- Recommendation + rationale
- Sources (docs, benchmarks, real-world comparisons)

**Quality Score Weights:**
- Completeness: 25% (all options fully evaluated)
- Tradeoff clarity: 30% (AI can see exact tradeoffs)
- Sourcing: 20% (benchmarks, real code, official docs)
- Decision support: 25% (recommendation tied to stated criteria)

**Token Budget:** 700–1,400 (quick to standard) / 1,800+ (deep)

---

### 4️⃣ USER RESEARCH GATE

**Input Questions:**
1. **Who is the target user?** (role, context, technical level, use case)
   - *Example:* "Senior data engineer at mid-market SaaS, building internal dashboards"
2. **What problem are we solving for them?** (what pain point? what outcome do they want?)
   - *If unclear:* "We believe [user] struggles with [problem]. Correct?"
3. **Where will we find user voices?** (Reddit, G2 reviews, interviews, Twitter, etc.)
   - *If multiple:* Research in this priority order: Reddit + Twitter > G2 > YouTube > Interviews

**Execution:**
- Current workflow (step-by-step, without your product)
- Top 3 pain points (with severity: critical / high / medium)
- First value moment (what makes them say "this works for me")
- Common objections (why they might NOT adopt)
- Direct quotes (if available, with attribution)

**Output Format:**
- User profile (role, context, technical level, use case)
- Current workflow (numbered steps, realistic)
- Pain points (ranked by frequency + severity)
- First value moment (1–2 sentences)
- Objections (top 3 reasons they might resist)
- Direct quotes (minimum 2, with source)
- Sources (specific Reddit threads, G2 reviews, etc.)

**Quality Score Weights:**
- User specificity: 25% (clear portrait, not generic)
- Workflow detail: 20% (AI can understand real steps)
- Sourcing: 30% (quotes backed by real users, specific sources)
- Actionability: 25% (product team can act on pain points)

**Token Budget:** 800–1,300 (quick to standard) / 1,600+ (deep)

---

### 5️⃣ DOCUMENT ANALYSIS GATE

**Input Questions:**
1. **What question are we answering from these docs?** (must be specific)
   - *If vague:* "Extract X / Answer Y / Find patterns about Z"
2. **How should I handle contradictions?** (highlight them? follow newest source? get consensus?)
   - *Default:* Highlight and note date/source for each
3. **Output format?** (key findings list, narrative, JSON, table, etc.)
   - *Default:* Key findings list with source citations

**Execution:**
- Scan all documents for answer to question
- Extract key findings (each with source location: page, section, line)
- Identify contradictions (note date, context, which source is more reliable)
- Flag gaps (what the docs DON'T cover)
- Cite every claim with page/section reference

**Output Format:**
- Key findings (numbered, each with source location)
- Direct answer to original question
- Contradictions (if any, with dates and reasoning)
- Gaps (what's not covered)
- Confidence (High/Medium/Low based on source quality + consistency)

**Quality Score Weights:**
- Citation accuracy: 40% (every finding has precise source reference)
- Completeness: 30% (all relevant findings extracted)
- Honesty: 20% (contradictions flagged, gaps noted)
- Format adherence: 10% (matches requested output format)

**Token Budget:** 500–1,200 (depends on doc length + complexity)

---

### 6️⃣ SYNTHESIS GATE

**Input Questions:**
1. **What are we synthesizing?** (paste findings from 1–5 modes, or describe sources)
   - *If scattered:* "Gathering research from [modes], now synthesizing"
2. **Who's the output for?** (CEO decision? Product roadmap? Investor pitch? Tech spec?)
   - *Determines tone + detail level*
3. **What's the key question?** (single coherent narrative around what?)
   - *If missing:* "Synthesizing to answer: [question you define]"

**Execution:**
- Identify common themes across findings
- Resolve conflicts (which sources are most credible)
- Build single coherent narrative (not a list)
- Derive implications (what does this mean for us?)
- Recommend next step (if research is incomplete, say so)

**Output Format:**
- Executive summary (3 sentences, one answer)
- Key insights (5–8 numbered, tagged STATED / INFERRED / ASSUMED)
- Strategic implications (what to do with this)
- Risks / Opportunities (if applicable)
- Open questions (what still needs research)
- Recommended next step (if needed)

**Quality Score Weights:**
- Coherence: 30% (single narrative, not fragmented)
- Claim rigor: 30% (every insight tagged + sourced)
- Insights: 25% (non-obvious connections across findings)
- Decision support: 15% (recommendation is clear)

**Token Budget:** 600–1,400 (depends on input volume)

---

## QUALITY SCORING SYSTEM

Every research output is auto-scored on 4 dimensions (0–25 pts each = 100 max).

### Dimension 1: FACTUALITY (0–25 pts)
**Are all claims cited to credible sources?**

- **25 pts:** Every claim has inline citation + source quality verified (credible domain, recent, expert)
- **20 pts:** 95%+ claims cited, mostly high-quality sources, minor gaps
- **15 pts:** 80%+ claims cited, mix of good and questionable sources
- **10 pts:** 60%+ claims cited, some unverified statements
- **5 pts:** <60% claims cited, many floating statements
- **0 pts:** No citations, or heavily hallucinated

**Auto-check:** Scan output for [source: ...] tags. Count cited vs uncited claims.

---

### Dimension 2: COMPLETENESS (0–25 pts)
**Does it fully answer the original question?**

- **25 pts:** Answers all aspects of the question directly + no excess
- **20 pts:** Answers 90%+ of the question, minor gaps
- **15 pts:** Answers ~75% of the question, some important gaps
- **10 pts:** Answers ~50% of the question, significant gaps
- **5 pts:** Partial answer, large gaps remain
- **0 pts:** Doesn't answer the question

**Auto-check:** Compare output to Gate input question. Does it directly answer YES/NO + supporting detail?

---

### Dimension 3: STRUCTURE (0–25 pts)
**Does it follow the output contract?**

- **25 pts:** All required sections present + well-formatted (summary, findings, framework, implications, confidence, unknowns, next step)
- **20 pts:** Missing 1 optional section, otherwise complete
- **15 pts:** Missing 1 required section, rest present
- **10 pts:** Missing 2+ required sections
- **5 pts:** Only partially structured
- **0 pts:** No structure, jumbled findings

**Auto-check:** Count required sections present (see mode-specific output formats above).

---

### Dimension 4: ACTIONABILITY (0–25 pts)
**Can an AI or human act on this?**

- **25 pts:** Crystal clear next steps, no ambiguity, includes data for decision
- **20 pts:** Clear next steps, minor ambiguity
- **15 pts:** Somewhat actionable, needs interpretation
- **10 pts:** Vague next steps, requires follow-up
- **5 pts:** Very unclear what to do with findings
- **0 pts:** Not actionable at all

**Auto-check:** Scan for vague language (should, may, might, could, etc.). Check for explicit recommendations.

---

## MINIMUM PASSING SCORE

**Competitive, Market, Technical, User, Synthesis:** 85/100
**Document Analysis:** 80/100 (lower bar because inputs are fixed)

**If Below Minimum:**
- Rerun the research with adjusted scope or sources
- Or ask user for clarification on what was missing
- Return revised findings

---

## TOKEN OPTIMIZATION RULES

**Rule 1 — Load Skills On-Demand Only**

| Research Mode | Load These Skills |
|---------------|------------------|
| Competitive | `competitive-analysis` + `prompt-engineering-patterns` |
| Market | `ai-product-strategy` + `building-with-llms` |
| Technical | `evaluating-new-technology` + `ai-evals` |
| User Research | `customer-research` + `conducting-user-interviews` |
| Document | `building-with-llms` (RAG) + `prompt-engineering` |
| Synthesis | `ai-evals` + `prompt-engineering-patterns` |

**Never preload all skills.** Load only when executing that mode.

**Rule 2 — Web Search First, LLM Second**

For factual lookups (competitor prices, market data, user quotes):
- Use web search directly (fast, cheap, 0 tokens vs. LLM interpretation)
- Only synthesize/analyze with LLM when you have results

**Rule 3 — Batch Small Researches**

If user has 3 quick questions:
- Batch them into one session vs. three separate passes
- Saves context switching overhead

**Rule 4 — Depth Scoping**

- **Quick:** 3 min, 500–800 tokens (answer obvious question fast)
- **Standard:** 5–10 min, 1,200–1,600 tokens (balanced rigor + speed)
- **Deep:** 15–20 min, 1,800–2,200 tokens (comprehensive, multiple sources)
- **Ultradeep:** 30+ min, 2,500+ tokens (PhD-level rigor, extensive synthesis)

**Default to STANDARD unless user specifies.**

---

## HALLUCINATION PREVENTION

**Non-Negotiable Rules:**

1. **Never cite sources you haven't actually found**
   - If you don't know something: "Source not found. Suggest searching [specific source]"
   - Never write [source: TBD] or [citation needed]

2. **Never fabricate data**
   - Market sizes, pricing, metrics MUST come from research
   - If estimate needed, say: "Estimated [X] based on [methodology], not verified"

3. **Always mark assumptions**
   - [STATED] = user told us
   - [INFERRED] = logical deduction from data
   - [ASSUMED] = best guess, needs verification
   - Never mix assumption types without marking

4. **Document contradictions honestly**
   - If sources disagree on fact: note which source, what's different, why
   - Don't hide contradictions; they're valuable for research

---

*Operating Rules v2.0 · April 2026*
*Hardened, token-efficient, AI-ready research execution.*
