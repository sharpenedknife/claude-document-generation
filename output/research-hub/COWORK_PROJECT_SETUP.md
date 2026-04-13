# Research Hub — Cowork Project Setup
**Version:** 2.0 · Multi-Agent Research Pipeline
**Status:** Ready to Deploy

---

## PROJECT STRUCTURE

Create this directory structure in your workspace:

```
research-hub-cowork/
├── product.md              (project brief)
├── tracks.md               (active research tracks)
├── workflow.md             (research orchestration)
├── .claude-cowork.yaml     (Cowork config)
└── docs/
    ├── CLAUDE.md
    ├── OPERATING_RULES.md
    ├── RESEARCH_MODE_GUIDES.md
    ├── QUESTIONNAIRE_TEMPLATES.md
    └── SETUP_GUIDE.md
```

---

## STEP 1: Create product.md

```markdown
# Research Hub — Cowork Project

## Project Brief

AI-powered distributed research utility for building projects. Conducts structured research across 6 modes using parallel agents.

## Architecture

- **Coordinator Agent:** Orchestrates research tasks, consolidates findings
- **Mode Agents:** One per research mode (Competitive, Market, Technical, User, Document, Synthesis)
- **Parallel Execution:** Multiple research tracks simultaneously
- **Quality Gates:** Auto-scoring on all outputs (target: 85+/100)

## Success Metrics

- Research quality score: 85+/100
- Time to research completion: <20 minutes per request
- Sources cited: 100% of claims
- Token efficiency: <2,500 tokens per comprehensive research

## Skills Available

- deep-research (primary framework)
- prompt-engineering-patterns (query structuring)
- llm-evaluation (quality scoring)
- rag-implementation (document analysis)
- team-composition-patterns (agent orchestration)
- task-coordination-strategies (dependency management)
- context-driven-development (project context)
- data-storytelling (findings synthesis)
- langchain-architecture (agent design)

## Constraints

- Token budget: 10,000 per session (soft limit)
- Depth: Quick/Standard/Deep/Ultradeep (default: Standard)
- Sources: Web + documents (internal KB in v3.0)
- Confidentiality: All findings marked with [STATED]/[INFERRED]/[ASSUMED]

---

## Key Questions (What We Research)

1. Market opportunity (TAM/SAM/SOM) for our target segments
2. Competitive landscape (positioning, gaps, threats)
3. User needs (workflows, pain points, objections)
4. Technical architecture decisions (tool/framework comparisons)
5. Synthesis of findings into strategic narrative

---

## Team

- **Coordinator:** Manages orchestration, consolidates results
- **Competitive Agent:** Analyzes competitor landscape
- **Market Agent:** Sizes opportunity, analyzes trends
- **Technical Agent:** Evaluates technologies, compares approaches
- **User Agent:** Researches user workflows and needs
- **Document Agent:** Analyzes uploaded documents
- **Synthesis Agent:** Consolidates findings into strategy

All agents run in parallel when possible. Coordinator waits for dependencies.
```

---

## STEP 2: Create tracks.md

```markdown
# Active Research Tracks

## Track 1: Competitive Analysis

**Status:** Ready
**Trigger:** "Research competitive landscape"
**Agent:** competitive-analyzer (parallel, one per competitor)
**Output:** Competitor table + gaps + positioning recommendation
**Depth:** Standard (1,200 tokens) or Deep (2,000 tokens)
**Dependencies:** None (parallel)
**Success Criteria:**
- 3+ competitors analyzed
- Clear gaps identified
- Positioning recommendation provided
- All sources cited

---

## Track 2: Market Sizing

**Status:** Ready
**Trigger:** "Size the market opportunity"
**Agent:** market-analyzer (parallel, one per method)
**Output:** TAM/SAM/SOM with assumptions + confidence
**Depth:** Standard (1,400 tokens) or Deep (2,000 tokens)
**Dependencies:** None (parallel)
**Success Criteria:**
- TAM calculated (top-down or bottom-up)
- SAM clearly scoped
- SOM realistic for Year 1
- All assumptions marked + sources cited

---

## Track 3: User Research

**Status:** Ready
**Trigger:** "Research user needs and workflows"
**Agent:** user-analyzer (parallel, one per segment)
**Output:** User profiles + workflows + pain points + quotes
**Depth:** Standard (1,300 tokens) or Deep (1,900 tokens)
**Dependencies:** None (parallel)
**Success Criteria:**
- User workflow documented (step-by-step)
- Top 3 pain points ranked by severity
- First value moment identified
- Min 2 direct quotes with sources

---

## Track 4: Technical Evaluation

**Status:** Ready
**Trigger:** "Evaluate technology options"
**Agent:** technical-analyzer (parallel, one per option)
**Output:** Comparison table + tradeoffs + recommendation
**Depth:** Standard (1,200 tokens) or Deep (1,800 tokens)
**Dependencies:** None (parallel)
**Success Criteria:**
- All options fairly evaluated
- Tradeoffs explicitly stated
- Implementation gotchas documented
- Recommendation tied to decision criteria

---

## Track 5: Document Analysis

**Status:** Ready
**Trigger:** "Analyze documents"
**Agent:** document-analyzer (sequential, one doc at a time)
**Output:** Key findings + answer + gaps + confidence
**Depth:** Quick (500 tokens) or Standard (800 tokens)
**Dependencies:** Documents must be uploaded first
**Success Criteria:**
- All findings cited with page/section
- Contradictions flagged if found
- Gaps clearly identified
- Answer directly addresses question

---

## Track 6: Synthesis

**Status:** Ready (requires other track outputs)
**Trigger:** "Synthesize all research"
**Agent:** synthesis-agent (sequential, runs after others)
**Output:** Executive summary + insights + implications + next step
**Depth:** Standard (1,000 tokens) or Deep (1,400 tokens)
**Dependencies:** Requires outputs from 1+ other tracks
**Success Criteria:**
- Single coherent narrative
- All insights tagged [STATED]/[INFERRED]/[ASSUMED]
- Strategic implications clear
- Open questions identified

---

## Running Multiple Tracks in Parallel

**Example: Full Competitive + Market Research**

```
cowork spawn research-hub \
  --depth=standard \
  --tracks=competitive,market,user \
  --output=json
```

**Coordinator waits for:**
1. Competitive agent (3 competitors analyzed)
2. Market agent (TAM/SAM/SOM calculated)
3. User agent (3 pain points identified)

**Then consolidates into:**
- Single research report
- Cross-findings analysis
- Combined next steps
- Overall confidence score

---

## Track History

| Track | Last Run | Status | Output Quality |
|-------|----------|--------|-----------------|
| Competitive | [Date] | ✅ Complete | 92/100 |
| Market | [Date] | ✅ Complete | 91/100 |
| User | [Date] | ✅ Complete | 90/100 |
| Technical | [Date] | ⏳ In Progress | - |
| Document | [Date] | ⏳ Queued | - |
| Synthesis | [Date] | ⏸ Waiting | - |
```

---

## STEP 3: Create workflow.md

```markdown
# Research Hub — Cowork Workflow

## Phase 1: Initialize

1. User provides research request (via questionnaire template)
2. Coordinator parses request → identifies mode(s) + depth
3. Load mode-specific skills (on-demand, not all upfront)
4. Spawn agents for parallel tracks

---

## Phase 2: Execute (Parallel)

**Each agent independently:**
- Runs research gate (mode-specific questions)
- Gathers sources (web search, documents, etc.)
- Structures findings (output format for mode)
- Auto-scores quality (target: 85+/100)

**Timeline:**
- Quick mode: 3–5 minutes per agent
- Standard mode: 5–10 minutes per agent
- Deep mode: 15–20 minutes per agent

---

## Phase 3: Consolidate

**Coordinator:**
1. Waits for all agents to complete
2. Checks quality scores (if <85, flags for rerun)
3. Resolves contradictions (if any)
4. Builds single narrative (if synthesis needed)
5. Packages findings (markdown, JSON, or custom format)

---

## Phase 4: Return & Archive

**Output to user:**
- Structured findings (one report per mode)
- Quality scores (transparency)
- Sources cited (all links provided)
- Open questions (what still needs research)
- Suggested next steps

**Archive to project:**
- Add to tracks.md history
- Update product.md with learnings
- Log any issues/improvements

---

## Skill Loading Strategy (Token Optimization)

### Load Immediately

- `prompt-engineering-patterns` (all agents use this)
- `context-driven-development` (coordinator uses this)

### Load Per Mode

| Mode | Load | Keep in Memory |
|------|------|-----------------|
| Competitive | `team-composition-patterns`, `competitive-analysis` | 5 min |
| Market | `team-composition-patterns`, `ai-product-strategy` | 5 min |
| Technical | `team-composition-patterns`, `evaluating-new-technology` | 5 min |
| User | `team-composition-patterns`, `customer-research` | 5 min |
| Document | `rag-implementation`, `building-with-llms` | 5 min |
| Synthesis | `data-storytelling`, `ai-evals` | 5 min |

**Unload after use.** Don't keep unused skills in memory.

---

## Quality Gate Checkpoint

Every research track must:

1. **Factuality Check** (25 pts)
   - [ ] All claims cited [source: URL]
   - [ ] Sources are credible
   - [ ] Minimum 3 sources per major claim

2. **Completeness Check** (25 pts)
   - [ ] Answers the research question fully
   - [ ] No missing pieces for decision-making
   - [ ] 90%+ coverage of requested scope

3. **Structure Check** (25 pts)
   - [ ] All required sections present
   - [ ] Output format matches mode specification
   - [ ] Well-formatted and scannable

4. **Actionability Check** (25 pts)
   - [ ] Clear next steps
   - [ ] No vague language (banned words removed)
   - [ ] AI/human can act on findings

**Minimum Pass Score: 85/100**
**If below: Rerun with higher depth or clarified scope**

---

## Common Workflows

### "Quick Competitive Assessment" (15 min)

```
1. User: "Who are our top 3 competitors?"
2. Coordinator: Spawn competitive-analyzer (×3 agents, parallel)
3. Each agent: 5 min research (quick depth)
4. Consolidate: 2 min
5. Return: Competitor overview table + top gaps
6. Quality: 88/100 (good for directional decisions)
```

### "Full Market + Competitive + User Research" (45 min)

```
1. User: "Size the market + understand competition + research users"
2. Coordinator: Spawn 3 agents in parallel
   - market-analyzer (TAM/SAM/SOM) → 10 min
   - competitive-analyzer (landscape) → 10 min
   - user-analyzer (workflows) → 10 min
3. Consolidate: 5 min
4. Synthesis: Build single narrative from all 3
5. Return: Executive summary + insights + strategy
6. Quality: 91/100 (high confidence for strategic decisions)
```

### "Technical Deep-Dive" (30 min)

```
1. User: "Should we use PostgreSQL or MongoDB?"
2. Coordinator: Spawn technical-analyzer (deep mode)
3. Agent: Detailed comparison (15 min)
4. Quality check: 92/100
5. Return: Comparison matrix + tradeoffs + recommendation
6. Next: Schedule architecture decision meeting
```

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Agent takes too long | Depth too high | Reduce to "quick" or "standard" |
| Quality score < 85 | Missing citations | Ask agent to rerun with better sourcing |
| Contradictory findings | Sources disagree | Coordinator flags + recommends which source to trust |
| Too many tokens | Running all modes | Run one mode at a time, or increase token budget |
| Agent hallucinated source | Source doesn't exist | Rerun with explicit "cite sources only" constraint |

---

## Next Phase (v3.0)

- [ ] Internal knowledge base integration
- [ ] Persistent research archive + search
- [ ] Custom evaluation frameworks
- [ ] Slack/Teams integration
- [ ] Scheduled research runs
- [ ] Research sharing + collaboration
```

---

## STEP 4: Create Cowork config file

Create `.claude-cowork.yaml` in project root:

```yaml
version: 2.0
project: Research Hub
created: 2026-04-06

skills:
  loaded_on_demand: true
  available:
    - deep-research
    - prompt-engineering-patterns
    - llm-evaluation
    - rag-implementation
    - team-composition-patterns
    - task-coordination-strategies
    - context-driven-development
    - data-storytelling
    - langchain-architecture

agents:
  coordinator:
    role: "Orchestrate research tasks, consolidate findings"
    skills: [context-driven-development, task-coordination-strategies]

  competitive-analyzer:
    role: "Analyze competitor landscape"
    skills: [team-composition-patterns, prompt-engineering-patterns]
    parallel: true

  market-analyzer:
    role: "Size market opportunity"
    skills: [team-composition-patterns, prompt-engineering-patterns]
    parallel: true

  technical-analyzer:
    role: "Evaluate technology options"
    skills: [team-composition-patterns, prompt-engineering-patterns]
    parallel: true

  user-analyzer:
    role: "Research user needs"
    skills: [team-composition-patterns, prompt-engineering-patterns]
    parallel: true

  document-analyzer:
    role: "Analyze uploaded documents"
    skills: [rag-implementation, prompt-engineering-patterns]
    parallel: false

  synthesis-agent:
    role: "Consolidate findings into narrative"
    skills: [data-storytelling, prompt-engineering-patterns]
    depends_on: [competitive-analyzer, market-analyzer, user-analyzer]

token_budgets:
  session_limit: 10000
  per_mode:
    quick: 500-800
    standard: 1200-1600
    deep: 1800-2200
    ultradeep: 2500+

quality_gates:
  minimum_score: 85
  dimensions:
    - factuality: 25
    - completeness: 25
    - structure: 25
    - actionability: 25

output_formats:
  - markdown
  - json
  - structured
```

---

## DEPLOYMENT CHECKLIST

- [✅] Skills copied to `~/.claude/skills/` (9 skills)
- [ ] Directory structure created (research-hub-cowork/)
- [ ] product.md created (project brief)
- [ ] tracks.md created (research tracks)
- [ ] workflow.md created (orchestration guide)
- [ ] .claude-cowork.yaml created (config)
- [ ] Docs/ folder populated (CLAUDE.md, etc.)
- [ ] First research request tested
- [ ] Quality gates verified (target: 85+/100)

---

*Research Hub — Cowork Setup v2.0 · Ready to Deploy*
