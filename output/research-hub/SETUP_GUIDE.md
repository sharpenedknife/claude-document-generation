# Research Hub — Setup Guide
**Custom Claude Project for any kind of research.**
Last updated: April 2026

---

## What This Project Does

A persistent Claude workspace that can conduct, synthesize, and structure research across domains — market analysis, competitive intelligence, technical deep-dives, literature review, and RAG-powered document research. Works in both Chat and Cowork mode.

---

## Skills Selected (from new-skills audit)

### Core Research Skills (Chat + Cowork)

| Skill | Source | What it gives you |
|-------|--------|-------------------|
| `rag-implementation` | llm-application-dev | Build knowledge-grounded research from your own documents (vector DB + retrieval) |
| `hybrid-search-implementation` | llm-application-dev | Combine keyword + semantic search for higher recall when researching large corpora |
| `embedding-strategies` | llm-application-dev | Optimize how research documents are chunked and indexed for retrieval |
| `llm-evaluation` | llm-application-dev | Score research output quality — groundedness, factuality, completeness |
| `prompt-engineering-patterns` | llm-application-dev | Structure research queries for precision: few-shot, CoT, structured output |
| `competitive-landscape` | startup-business-analyst | Porter's Five Forces, Blue Ocean, positioning maps — for competitive research |
| `market-sizing-analysis` | startup-business-analyst | TAM/SAM/SOM with top-down, bottom-up, value-theory methods |
| `data-storytelling` | business-analytics | Turn research findings into executive-ready narratives and presentations |
| `context-driven-development` | conductor | Maintain research context across sessions (product.md, tracks.md pattern) |

### Orchestration Skills (Cowork only — multi-agent research)

| Skill | What it gives you |
|-------|-------------------|
| `team-composition-patterns` | Preset research team: assign agents to parallel research tracks |
| `task-coordination-strategies` | Decompose large research tasks across parallel agents with dependency graphs |

---

## How to Set Up (Claude Projects / Chat)

1. **Create a new Claude Project** named "Research Hub"

2. **Upload knowledge base files** (pick what fits your research domain):
   - `skills/rag-implementation/SKILL.md`
   - `skills/hybrid-search-implementation/SKILL.md`
   - `skills/prompt-engineering-patterns/SKILL.md`
   - `skills/competitive-landscape/SKILL.md`
   - `skills/market-sizing-analysis/SKILL.md`
   - `skills/data-storytelling/SKILL.md`
   - `skills/context-driven-development/SKILL.md`

3. **Paste these Custom Instructions:**

**Field A — "What would you like ChatGPT/Claude to know?"**
```
I am a Research Hub — a specialized AI workspace for conducting structured research across domains: market analysis, competitive intelligence, technical literature, document analysis, and expert synthesis.

I support 5 research modes:
1. Document research — analyze uploaded files, extract key insights, answer questions grounded in the docs
2. Competitive research — competitor landscape, positioning, differentiation opportunities
3. Market research — TAM/SAM/SOM sizing, trend analysis, customer segment profiling
4. Technical research — deep-dives into technologies, architectures, tradeoffs
5. Synthesis — consolidate findings from multiple sources into structured reports

Every research output is: structured (framework-based), cited (claims backed by sources), and action-oriented (ends with implications or next steps).
```

**Field B — "How would you like to respond?"**
```
RESEARCH HUB OPERATING RULES:

1. ALWAYS ask which research mode before starting (Document / Competitive / Market / Technical / Synthesis).

2. ALWAYS ask for the research question in the format: "What do you want to know, and why does it matter?" before researching.

3. Run a RESEARCH GATE before starting work:
   - Document research: "What documents are you providing? What question should I answer from them?"
   - Competitive research: "Who are the top 3 competitors to focus on? What's the key strategic question?"
   - Market research: "What's the target geography, customer segment, and time horizon?"
   - Technical research: "What decision does this research need to support?"
   - Synthesis: "What sources/findings are we synthesizing? What's the output format?"

4. Apply the appropriate framework from knowledge base (Porter's Five Forces, TAM/SAM/SOM, RAG pipeline, etc.)

5. Structure ALL research outputs as:
   - Executive Summary (3 sentences max)
   - Key Findings (numbered, each with source/basis)
   - Framework Analysis (relevant model applied)
   - Implications / Recommendations
   - Open Questions / Next Steps

6. Mark every claim with its basis: [STATED] (user provided), [INFERRED] (logical deduction), [ASSUMED] (best guess).

7. Never hallucinate sources. If you don't know — say so and propose how to find it.
```

4. **Set 4 conversation starters:**
   - `Research a market: size the opportunity and map the competitive landscape`
   - `Analyze documents: I'll upload files and you extract key insights`
   - `Technical deep-dive: research a technology, architecture, or tool`
   - `Synthesize research: consolidate findings into a structured report`

---

## How to Set Up (Cowork Mode)

For multi-agent parallel research using the agent-teams skills:

1. Install skills to Cowork:
   ```
   cp -r skills/rag-implementation ~/.claude/skills/
   cp -r skills/hybrid-search-implementation ~/.claude/skills/
   cp -r skills/prompt-engineering-patterns ~/.claude/skills/
   cp -r skills/competitive-landscape ~/.claude/skills/
   cp -r skills/market-sizing-analysis ~/.claude/skills/
   cp -r skills/data-storytelling ~/.claude/skills/
   cp -r skills/context-driven-development ~/.claude/skills/
   cp -r skills/team-composition-patterns ~/.claude/skills/
   cp -r skills/task-coordination-strategies ~/.claude/skills/
   ```

2. For parallel research sessions, use the Research preset from `team-composition-patterns`:
   - Spawn agents per research track (e.g., one per competitor, one per market segment)
   - Coordinate via `task-coordination-strategies` dependency graph
   - Consolidate with `data-storytelling` for final output

3. Use `context-driven-development` to maintain a `conductor/` directory with:
   - `product.md` → research project brief
   - `tracks.md` → active research tracks
   - `workflow.md` → research process

---

## Skill Loading (Token Optimization)

Load skills on demand per research type — never preload all:

| Research type | Load these skills |
|--------------|------------------|
| Document research | `rag-implementation` + `hybrid-search-implementation` |
| Competitive | `competitive-landscape` + `prompt-engineering-patterns` |
| Market sizing | `market-sizing-analysis` + `data-storytelling` |
| Technical | `prompt-engineering-patterns` + `llm-evaluation` |
| Synthesis | `data-storytelling` + `context-driven-development` |
| Multi-agent (Cowork) | `team-composition-patterns` + `task-coordination-strategies` |

---

*Research Hub v1.0 · April 2026*
