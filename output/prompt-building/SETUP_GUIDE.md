# Prompt Building — Skills for All Claude Projects
**Skills to add to every Claude project for better prompt quality.**
Last updated: April 2026

---

## Why These Skills Go in Every Project

These 3 skills give any Claude project the ability to: write better prompts, evaluate whether prompts are working, and build multi-step prompt chains. They're foundational — domain-agnostic and useful regardless of what the project does.

---

## The 3 Skills

### 1. `prompt-engineering-patterns`
**Source:** `new-skills/llm-application-dev`
**Mode:** Chat + Cowork
**What it adds to any project:**
- Few-shot learning with dynamic example selection
- Chain-of-thought with self-verification loop
- Structured output using Pydantic schemas
- Progressive disclosure (simple → detailed based on user need)
- Error recovery and fallback strategies when prompts fail
- Role-based system prompt design
- Token efficiency + prompt caching patterns
- Performance KPI tracking for prompt quality

**When to call it:** When you need to write or refine any prompt, system instruction, or project instruction. This is the meta-skill — it improves everything else.

---

### 2. `llm-evaluation`
**Source:** `new-skills/llm-application-dev`
**Mode:** Chat + Cowork
**What it adds to any project:**
- Automated quality metrics: BLEU, ROUGE, BERTScore
- Custom metrics: groundedness, toxicity, factuality
- LLM-as-Judge patterns: single output scoring, pairwise comparison, reference-based
- A/B testing framework for prompt variants
- Regression detection (did a prompt change break quality?)
- Integration with LangSmith for production tracing

**When to call it:** After generating a prompt or project instruction, run evaluation to score it before shipping. Also use when comparing two prompt variants.

---

### 3. `langchain-architecture`
**Source:** `new-skills/llm-application-dev`
**Mode:** Chat + Cowork
**What it adds to any project:**
- LangGraph state management for multi-step prompt chains
- ReAct agent pattern for tool-using prompts
- RAG integration within prompt chains
- Memory systems: buffer, summary, token-based, vector store
- Streaming + async patterns for production
- LangSmith tracing for debugging prompt chains

**When to call it:** When a project needs prompt chains (not just single prompts) — multi-step workflows, agent loops, or memory-enabled assistants.

---

### Bonus: `similarity-search-patterns`
**Source:** `new-skills/llm-application-dev`
**Mode:** Chat + Cowork
**When to add:** If the project does any form of semantic matching — finding similar prompts, few-shot example retrieval, or document lookup. Covers cosine/Euclidean/dot product distance, HNSW index, pgvector, Qdrant, Pinecone.

---

## Installation

### For Chat Mode (Claude Projects)
Upload these files to your Claude Project knowledge base:
- `skills/prompt-engineering-patterns/SKILL.md`
- `skills/llm-evaluation/SKILL.md`
- `skills/langchain-architecture/SKILL.md` (if building LLM apps)

Add to your project instructions (Field B):
```
PROMPT QUALITY RULES:
- When writing any system prompt, project instruction, or prompt template: read prompt-engineering-patterns from knowledge base and apply it.
- When evaluating prompt output quality: read llm-evaluation from knowledge base and score the output.
- When building multi-step prompt chains: read langchain-architecture from knowledge base.
- Always mark unvalidated prompts as DRAFT until evaluated against at least 3 test cases.
```

### For Cowork Mode
Install globally so every project can use them:
```bash
cp -r "skills/prompt-engineering-patterns" ~/.claude/skills/
cp -r "skills/llm-evaluation" ~/.claude/skills/
cp -r "skills/langchain-architecture" ~/.claude/skills/
cp -r "skills/similarity-search-patterns" ~/.claude/skills/
```

After copying, they're available in every Cowork session via `Skill tool: prompt-engineering-patterns`.

### For This Documentation Builder Specifically
These skills are already in `skills/` (copied during this session). No extra steps needed for Cowork use within this project.

---

## How They Work Together

```
WRITE PROMPT
    ↓
prompt-engineering-patterns → structures it (few-shot, CoT, role, output format)
    ↓
llm-evaluation → scores it (groundedness, factuality, A/B variants)
    ↓  (if multi-step)
langchain-architecture → chains it (state, memory, tools, agents)
    ↓  (if needs example retrieval)
similarity-search-patterns → finds relevant few-shot examples semantically
```

---

## Which Projects Get Which Skills

| Project type | Must-have | Nice-to-have |
|--------------|-----------|--------------|
| Any Claude Project | `prompt-engineering-patterns` | `llm-evaluation` |
| Documentation Builder | `prompt-engineering-patterns` + `llm-evaluation` | `langchain-architecture` |
| Research Hub | `prompt-engineering-patterns` + `llm-evaluation` | `similarity-search-patterns` |
| LLM App builder | All 4 | — |
| Simple chat assistant | `prompt-engineering-patterns` | — |

---

## Token Loading Rule

Load prompt-building skills only when writing or evaluating prompts — not at session start:

- Writing project instructions → read `prompt-engineering-patterns/SKILL.md`
- Scoring a prompt → read `llm-evaluation/SKILL.md`
- Building a chain → read `langchain-architecture/SKILL.md`
- Never load all 3 at once unless doing a full prompt-system review.

---

*Prompt Building Skills v1.0 · April 2026*
