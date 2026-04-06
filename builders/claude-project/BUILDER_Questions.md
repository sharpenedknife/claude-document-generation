# Builder: Claude Project Setup

**Domain:** `claude-project`
**Use when:** Someone has an idea and needs a full Claude project generated from scratch — CLAUDE.md, project instructions, system guides, folder structure, knowledge base file list.

---

## Intake Questions

Ask these in order. Do not generate until all answers collected.

**Q1: Project Name**
> What's the name of this Claude project? (e.g., "Documentation Builder", "Code Reviewer", "Sales Enablement Assistant")

**Q2: Core Purpose (The Idea)**
> Describe the project in 1–3 sentences. What will Claude do in this project? What problem does it solve?

**Q3: Primary User**
> Who will use this project day-to-day? (e.g., software engineer, marketing manager, sales rep, founder)
> Are they technical? What's their level of familiarity with Claude?

**Q4: Key Tasks**
> List the top 3–5 tasks Claude will perform in this project. Be specific.
> Example: "Write SEO blog posts", "Review pull requests", "Generate cold emails from prospect data"

**Q5: Domains / Topics**
> What subject areas does this project touch? (e.g., code, marketing, sales, documentation, design, data)

**Q6: Connected Tools**
> Will this project connect to external tools via MCP? (e.g., Slack, Jira, Ahrefs, Notion, Google Drive)
> List any known integrations.

**Q7: Output Types**
> What types of documents or outputs should Claude produce?
> Example: "Markdown docs", "JSON configs", "HTML pages", "Word documents", "Slack messages"

**Q8: Quality Requirements**
> Are there specific quality gates, review processes, or standards Claude must follow?
> Example: "All code must pass linting", "Docs must pass 5-gate quality check", "Responses under 200 words"

---

## RESEARCH GATE (mandatory — runs after Q0, before Q1)

After Q0 is answered, STOP. Do not ask Q1 yet.

Tell the user:

> "Before I design your Claude Project, go collect these 4 things and come back:
>
> **1. What does the person using this assistant do manually today?**
>    Write out the exact steps they follow — this becomes the knowledge base structure.
>
> **2. What files, docs, or reference material does Claude need to know?**
>    List them by name — these become knowledge base uploads.
>
> **3. Write 3 real example requests users will send this assistant.**
>    These become the project instruction examples and test cases.
>
> **4. What should Claude NEVER do in this project?**
>    Constraints drive instruction quality more than capabilities. List at least 3.
>
> Come back with these 4 answers."

Wait for the user to return before proceeding to Q1.
If they want to skip: warn about ASSUMED items, proceed only on explicit confirmation.

---

## Context Tier Assessment (run before confirming generation plan)

Before showing the generation plan, assess how complete the user's intake is:

- **Tier 1 — Minimal (proceed with caution):** User answered Q0 only, or gave fewer than 3 sentences of detail total.
  → Say: "I have minimal context. I'll be making significant assumptions — every unverified item will be marked ASSUMED. Want to add more before I generate, or proceed with assumptions?"

- **Tier 2 — Solid:** Q0 through Q5 answered with specific, non-vague content.
  → Note any remaining defaults. Confirm and proceed.

- **Tier 3 — Full:** All questions answered with concrete, specific details.
  → Best output possible. Confirm and proceed.

Never skip this assessment. Never present assumptions as confirmed facts.

---

## Outputs to Generate

Based on answers, generate in this order:

1. **`CLAUDE.md`** — Master navigation (use `builders/claude-project/rules.md` for structure rules)
2. **`system/guides/SYSTEM_Master_Index.md`** — Quick reference for the domain
3. **`system/templates/project_instructions/PROJECT_INSTRUCTIONS_[Name].md`** — Project instructions (follow `SYSTEM_Project_Instructions_Rules.md` exactly)
4. **`config/domain_definitions.json`** — Domain registry
5. **`config/token_budgets.json`** — Token budgets per doc type
6. **`README.md`** — Setup guide (3 steps: create project → sync folder → paste instructions)

---

## Generation Checklist

- [ ] All 8 questions answered before generation starts
- [ ] CLAUDE.md is ≤ 200 lines
- [ ] Project instructions are 500–800 words
- [ ] Project instructions follow 6-section structure from `SYSTEM_Project_Instructions_Rules.md`
- [ ] Domain definitions reflect actual domains used in this project
- [ ] Token budgets set per doc type
- [ ] README has exact 3-step setup
- [ ] All outputs pass Gate 1 before delivery
