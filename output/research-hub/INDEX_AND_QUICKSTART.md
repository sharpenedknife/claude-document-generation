# Research Hub — Index & Quickstart
**Version:** 2.0 · April 2026
**All documents at a glance. Start here.**

---

## START HERE — Choose Your Path

### Path A: "I Want to Deploy This Now" (10 minutes)

1. **SETUP_GUIDE.md**
   - Chat mode installation (5 min)
   - Or Cowork mode installation (15 min)
   - Test with first research request

2. **QUESTIONNAIRE_TEMPLATES.md**
   - Copy the right template for your research mode
   - Fill blanks
   - Paste into Research Hub

3. **Done.** Research Hub is live.

---

### Path B: "I Want to Understand How This Works" (30 minutes)

**Read in this order:**

1. **CLAUDE.md** (5 min read)
   - Overview of 6 research modes
   - The 4-gate workflow
   - Operating rules at a glance

2. **OPERATING_RULES.md** (10 min read)
   - Detailed research gates per mode
   - Quality scoring system (how to score 85+/100)
   - Token optimization rules

3. **RESEARCH_MODE_GUIDES.md** (10 min read)
   - Deep framework for each of 6 modes
   - Execution steps (what to do in each mode)
   - Output templates (what to expect back)

4. **SETUP_GUIDE.md** (5 min read)
   - Install to Claude Projects (Chat mode)
   - Or install to Cowork (multi-agent research)

5. **QUESTIONNAIRE_TEMPLATES.md** (reference as needed)
   - When you actually start a research request

---

### Path C: "I'm a Developer / Building on Top of This" (1 hour)

**Read everything in this order:**

1. **CLAUDE.md** → Understand the system design
2. **OPERATING_RULES.md** → Understand the gates + quality standards
3. **RESEARCH_MODE_GUIDES.md** → Understand each framework
4. **SETUP_GUIDE.md** → See skill loading + architecture
5. **QUESTIONNAIRE_TEMPLATES.md** → See input/output contracts
6. **Explore `/new-skills/`** → Reference deep-research, rag-implementation, prompt-engineering skills

---

## DOCUMENT REFERENCE GUIDE

### CLAUDE.md
**What:** Project instructions for Claude.ai Projects custom instructions field
**Contains:** Menu, 4-gate workflow, 6 research modes, operating rules, conversation starters
**Read if:** Setting up project OR understanding high-level workflow
**Length:** ~8 KB

### OPERATING_RULES.md
**What:** Detailed operating procedures for each research mode
**Contains:** Mode-specific research gates (3–5 questions each), quality scoring system, token optimization rules
**Read if:** Want to understand how research actually executes OR need to score/evaluate research
**Length:** ~12 KB

### RESEARCH_MODE_GUIDES.md
**What:** Step-by-step frameworks for all 6 modes
**Contains:** Porter's 5 Forces (Competitive), TAM/SAM/SOM (Market), Decision Matrix (Technical), JTBD (User), Extraction (Document), Thematic Analysis (Synthesis)
**Read if:** Understand what happens when you run each mode OR creating your own research templates
**Length:** ~14 KB

### QUESTIONNAIRE_TEMPLATES.md
**What:** Copy-paste templates for all 6 modes (user + AI versions)
**Contains:** Pre-filled questionnaires, best practices tips, how to use templates
**Read if:** Actually starting a research request (just copy + fill + paste)
**Length:** ~8 KB

### SETUP_GUIDE.md
**What:** Installation instructions for Chat mode and Cowork mode
**Contains:** Step-by-step setup, knowledge base sources, skill loading, troubleshooting
**Read if:** Deploying Research Hub OR troubleshooting issues
**Length:** ~10 KB

---

## THE 6 RESEARCH MODES AT A GLANCE

| Mode | When | Input Question | Output Format | Framework | Tokens |
|------|------|------------------|-----------|-----------|--------|
| **1. Competitive** | "Who do we compete with? Where's the gap?" | Top 3 competitors + strategic question | Landscape table + 3 opportunities + positioning | Porter's 5 Forces | 800–2000 |
| **2. Market** | "How big is this opportunity?" | Customer segment + geography + timeframe | TAM/SAM/SOM + assumptions + confidence | TAM/SAM/SOM sizing | 900–2200 |
| **3. Technical** | "Which tool/approach should we use?" | 2–4 options + decision criteria | Comparison table + tradeoffs + recommendation | Decision matrix | 700–1800 |
| **4. User Research** | "What do users actually need/do?" | User role + problem area + sources | Workflow + pain points + objections + quotes | Jobs to Be Done | 800–1900 |
| **5. Document Analysis** | "Extract insights from files I upload" | Documents + specific question | Key findings + answer + gaps + confidence | Extraction + synthesis | 500–1200 |
| **6. Synthesis** | "Consolidate multiple research into one narrative" | Findings from other modes | Executive summary + insights + implications + next step | Thematic analysis | 600–1400 |

---

## THE 4-GATE WORKFLOW

Every research session follows these gates:

```
START → GATE 1: Identify Mode → GATE 2: Tier 1 Context
  ↓
  ├─ "What do you want to know?" ← User answers
  ├─ "Why does it matter?" ← User answers
  ↓
GATE 3: Mode-Specific Research Gate → Ask 3–5 mode-specific questions
  ↓
GATE 4: Execute & Return Findings → Structured output in specified format
  ↓
AUTO-SCORE (Factuality 25% + Completeness 25% + Structure 25% + Actionability 25%)
  ↓
IF Score ≥ 85/100: Return findings
IF Score < 85/100: Rerun or ask for clarification
  ↓
END
```

---

## QUALITY SCORING CHECKLIST

Every research must pass all 4 dimensions to score 85+/100:

### ✅ Factuality (0–25 pts)
- [ ] Every claim has [source: URL] citation
- [ ] Sources are credible (no hallucination)
- [ ] Minimum 3 sources per major claim

### ✅ Completeness (0–25 pts)
- [ ] Answers the original question directly
- [ ] No excess, no missing pieces
- [ ] 90%+ coverage of requested scope

### ✅ Structure (0–25 pts)
- [ ] Has all required sections (summary, findings, framework, implications, confidence, unknowns, next step)
- [ ] Well-formatted and easy to scan
- [ ] Output contract met (see RESEARCH_MODE_GUIDES.md)

### ✅ Actionability (0–25 pts)
- [ ] Clear next steps (not vague)
- [ ] No banned words (should, may, might, could, seems, possibly)
- [ ] AI/human can act on this

**Minimum pass:** 85/100. If below, rerun.

---

## OPERATING RULES SUMMARY

1. **Show menu first** (every new session)
2. **Run 4 gates** in order (no skipping)
3. **Load skills on-demand** (not all upfront)
4. **Web search first** (then synthesize)
5. **Mark claims** ([STATED] / [INFERRED] / [ASSUMED])
6. **Cite all sources** ([source: URL])
7. **No hallucination** (if source not found, say so)
8. **Auto-score** (aim for 85+/100)
9. **No vague language** (ban: should, may, might, could, seems, appears, possibly, perhaps, maybe)
10. **Stay token-efficient** (quick/standard/deep modes)

---

## SKILL MAPPING (What Skill Runs When)

| Research Mode | Load This Skill | Also Load | Token Impact |
|---------------|-----------------|-----------|--------------|
| Competitive | `competitive-analysis` | `prompt-engineering-patterns` | 50–150 tokens |
| Market | `ai-product-strategy` | `building-with-llms` | 50–150 tokens |
| Technical | `evaluating-new-technology` | `ai-evals` | 50–150 tokens |
| User | `customer-research` | `conducting-user-interviews` | 50–150 tokens |
| Document | `building-with-llms` (RAG) | `prompt-engineering-patterns` | 50–150 tokens |
| Synthesis | `ai-evals` | `prompt-engineering-patterns` | 50–150 tokens |

**Never preload all skills.** Load only when executing that mode. Saves ~400–500 tokens per session.

---

## TOKEN BUDGETS BY MODE & DEPTH

| Mode | Quick | Standard | Deep | Ultradeep |
|------|-------|----------|------|-----------|
| Competitive | 800 | 1200 | 1800 | 2500 |
| Market | 900 | 1400 | 2000 | 2800 |
| Technical | 700 | 1200 | 1800 | 2400 |
| User | 800 | 1300 | 1900 | 2600 |
| Document | 500 | 800 | 1200 | 1800 |
| Synthesis | 600 | 1000 | 1400 | 2000 |

**Total project budget:** 6,000–8,000 tokens for comprehensive research (all 6 modes, standard depth)

---

## KNOWLEDGE SOURCES

### Included in v2.0 (External)
- Web search (Google, Bing)
- Academic databases (ArXiv, Scholar)
- Market data (Crunchbase, G2, Gartner)
- User voices (Reddit, ProductHunt, Twitter)
- Technical docs (GitHub, official docs, Stack Overflow)
- Document uploads (PDF, Markdown, TXT)

### Backlog for v3.0 (Internal)
- Internal wikis
- Previous research archives
- Company documents
- Customer interview transcripts
- Product specifications

---

## TROUBLESHOOTING QUICK REFERENCE

| Problem | Cause | Solution |
|---------|-------|----------|
| Score < 85/100 | Missing citations | Add [source: URL] tags to every claim |
| Score < 85/100 | Vague language | Replace "should" with "IS" or "WILL" |
| Score < 85/100 | Incomplete answer | Rerun with higher depth (Quick → Standard → Deep) |
| Too many tokens | Scope too broad | Narrow: "US market only" instead of "global" |
| Too many tokens | Depth too high | Reduce: use "Quick" for directional decisions |
| Results too shallow | Depth too low | Increase: use "Deep" for critical decisions |
| Contradictions found | Sources disagree | This is normal; Hub flags it + recommends which source to trust |
| Can't find source | Source doesn't exist | Hub says "Source not found. Recommend searching [X]" |

---

## QUICK START (5 MINUTES)

1. Go to **SETUP_GUIDE.md** → Follow Chat mode installation
2. Go to **QUESTIONNAIRE_TEMPLATES.md** → Pick your research mode
3. Copy + fill + paste questionnaire into Research Hub
4. Get back structured findings
5. Review against quality gates (this checklist above)

---

## FULL DOCUMENTATION TREE

```
Research Hub v2.0
├── CLAUDE.md (← Start if new)
├── OPERATING_RULES.md (← Read for details)
├── RESEARCH_MODE_GUIDES.md (← Reference per mode)
├── QUESTIONNAIRE_TEMPLATES.md (← Copy-paste when researching)
├── SETUP_GUIDE.md (← Read for installation)
└── INDEX_AND_QUICKSTART.md (← You are here)
```

---

## CONTACT / SUPPORT

**Need help?**
- See SETUP_GUIDE.md → Troubleshooting section
- Review OPERATING_RULES.md for quality gates
- Check QUESTIONNAIRE_TEMPLATES.md for correct input format

**Want to extend this?**
- Modify RESEARCH_MODE_GUIDES.md to add frameworks
- Update OPERATING_RULES.md for new quality standards
- Build skills on top of this (see `/new-skills/` folder)

---

*Index & Quickstart v2.0 · April 2026*
*All paths lead to structured research.*
