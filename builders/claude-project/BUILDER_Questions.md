# Builder: Claude Project Setup

**Domain:** `claude-project`
**Use when:** Someone has an idea and needs a full Claude project generated from scratch — CLAUDE.md, project instructions, system guides, folder structure, knowledge base file list.

---

## How Intake Works — Flexible Context Collection

No question is mandatory. Users can provide context however they want — answer questions, paste existing notes, describe the idea freeform, or upload reference materials. Claude dynamically assesses whether enough context exists to generate quality output.

---

## Context Assessment

### Tier 1 — Minimum (can generate, heavy defaults)
- [ ] **What Claude does** — at least a sentence describing the project purpose

Warn: "I have the basic idea but will need to assume the user type, key tasks, output formats, and quality standards. Want me to proceed with defaults, or add more detail?"

### Tier 2 — Solid (good generation)
Everything in Tier 1, plus:
- [ ] **Who uses it** — primary user type
- [ ] **Key tasks** — at least 2-3 things Claude will do

### Tier 3 — Full (best output)
Everything in Tier 2, plus: domains, connected tools, output types, quality requirements.

---

## Conversational Question Guide

Use these to fill gaps — only ask what's missing from the user's input.

### Opening
> "Tell me about the Claude project you want to build. What should Claude do, and who will use it? You can describe it however you like — freeform, bullet points, or paste existing notes."

---

**Q1: Project Name**
**Ask when:** User hasn't named the project.
**Ask:** "What's the name of this Claude project?"
**Default if skipped:** Derive from the purpose description.

**Q2: Core Purpose**
**Ask when:** You can't summarize what Claude does in this project.
**Ask:** "Describe the project in 1–3 sentences. What will Claude do? What problem does it solve?"
**Default if skipped:** Cannot default — this is the minimum Tier 1 context. Ask again.

**Q3: Primary User**
**Ask when:** You don't know who uses this.
**Ask:** "Who will use this project day-to-day? Are they technical?"
**Default if skipped:** Infer from purpose. Mark as INFERRED.

**Q4: Key Tasks**
**Ask when:** You can't list what Claude will do.
**Ask:** "List the top 3–5 tasks Claude will perform. Be specific."
**Default if skipped:** Infer from purpose. Mark as INFERRED.

**Q5: Domains / Topics**
**Ask when:** Subject areas are unclear.
**Ask:** "What subject areas does this project touch?"
**Default if skipped:** Infer from tasks.

**Q6: Connected Tools**
**Ask when:** Project likely needs external connections.
**Ask:** "Will this project connect to external tools via MCP?"
**Default if skipped:** Assume none.

**Q7: Output Types**
**Ask when:** Output format matters for the project.
**Ask:** "What types of outputs should Claude produce?"
**Default if skipped:** Assume markdown docs + inline chat responses.

**Q8: Quality Requirements**
**Ask when:** User hasn't mentioned standards.
**Ask:** "Any specific quality gates, review processes, or standards Claude must follow?"
**Default if skipped:** Assume general quality guidelines, no special gates.

---

## Context Confirmation

Before generating, show confirmed vs. assumed:

> "Here's what I'm working with:
> **Confirmed:** [items from user input]
> **Assumed:** [defaults with reasoning]
>
> Generating: CLAUDE.md, Project Instructions, System Guide, Domain Config, Token Budgets, README
> Proceed?"

---

## Outputs to Generate

Based on answers, generate in this order:

1. **`CLAUDE.md`** — Master navigation
2. **`system/guides/SYSTEM_Master_Index.md`** — Quick reference for the domain
3. **`system/templates/project_instructions/PROJECT_INSTRUCTIONS_[Name].md`** — Project instructions
4. **`config/domain_definitions.json`** — Domain registry
5. **`config/token_budgets.json`** — Token budgets per doc type
6. **`README.md`** — Setup guide (3 steps: create project → sync folder → paste instructions)

---

## Generation Checklist

- [ ] Context assessed — tier identified, assumptions listed
- [ ] User confirmed generation plan (or said "proceed" with defaults)
- [ ] CLAUDE.md is ≤ 200 lines
- [ ] Project instructions are 500–800 words
- [ ] Project instructions follow 6-section structure from `SYSTEM_Project_Instructions_Rules.md`
- [ ] All ASSUMED items marked in output
- [ ] No hallucinated content — everything traceable to user input or marked ASSUMED
- [ ] All outputs pass Gate 1 before delivery
