# Documentation Builder — CLAUDE.md
**Master navigation for the Documentation Generation System.**
Last updated: April 2026

---

## What This Is

**Goal:** User provides project context → generate complete, top-tier implementation documentation for AI to build that thing.

The "thing" being built is one of four primary types: a **Product** (software/app/SaaS — 11-doc implementation bundle with PRD + UX + UI + dev plan + starter prompt), a **Claude Project** (persistent AI assistant workspace), a **Skill** (repeatable workflow/slash command), or an **MCP Server** (live external tool integration). Single AI docs and code docs are also supported. Do not start generating until the build type is confirmed and minimum context is collected. See `system/guides/SYSTEM_Build_Decision_Framework.md` for the decision framework and context gates.

**Interactive mode:** Collect context conversationally → confirm generation plan → generate in correct order → deliver zip → offer to refine individual docs on request.

Every output passes 5 quality gates before it ships. Every doc type has a template, a token budget, and a naming convention.

---

## Rules

1. **Run quality gates on every doc.** No exceptions. Use `system/guides/SYSTEM_Exit_Rules.md`.
2. **Use templates.** Every doc type has a template in `system/templates/output/`. Use it.
3. **Quote the rules file.** When flagging an issue, cite `SYSTEM_*` filename + section.
4. **Respect token budgets.** Check `config/token_budgets.json` before approving any doc.
5. **Name files correctly.** See `system/guides/SYSTEM_File_Naming.md`. Framework files: `{TYPE}_{Topic}.md`. Output docs: `{DOMAIN}_{Topic}_v{X.Y}_{YYYY-MM-DD}.md`. No deviations.
6. **Apply coding standards to all code blocks.** Use `system/guides/SYSTEM_Coding_Standards.md`. Code violations = Gate 3 fail.
7. **Identify the build type first.** Read `system/guides/SYSTEM_Build_Decision_Framework.md` → Q0 Gate before routing to any builder. Wrong build type = wrong docs.
8. **Use the right builder.** Claude Project → `builders/claude-project/`. Skill/slash command → `builders/skill/`. MCP server → `builders/mcp/`. Single AI doc → `builders/ai-docs/`. Code doc → `builders/code/`.
9. **Always deliver output as a zip.** Every session that produces or modifies docs must end with a versioned zip of the full `Documentation/` folder: `Documentation_Builder_v{X.Y}_{YYYY-MM-DD}.zip`. No exceptions.
10. **Load skills on demand, never upfront.** Read `skills/SKILL_MAP.md` once at Step 3. Read each `SKILL.md` only when at that generation stage. Max 2 skills active per stage. For stack skills: read ONE (the one matching Q5). Never preload.

---

## File Map

```
Documentation/
├── CLAUDE.md                              ← You are here
│
├── system/                                ← Read-only framework (never edit)
│   ├── guides/
│   │   ├── SYSTEM_Master_Index.md                    ← Start here
│   │   ├── SYSTEM_Exit_Rules.md                      ← 5-gate quality framework
│   │   ├── SYSTEM_File_Naming.md                     ← LLM-optimized naming conventions
│   │   ├── SYSTEM_Content_Guide.md                   ← Section standards for every doc type
│   │   ├── SYSTEM_Token_Optimization.md              ← Token budgets and quality targets
│   │   ├── SYSTEM_Prerequisites_Guide.md             ← Prerequisite section deep-dive
│   │   ├── SYSTEM_Project_Instructions_Rules.md      ← Rules for writing project instructions
│   │   ├── SYSTEM_Coding_Standards.md                ← Code quality rules (Gate 3)
│   │   ├── SYSTEM_AI_First_Format.md                 ← AI-optimised documentation format
│   │   ├── SYSTEM_Version_Control.md                 ← Versioning and deprecation rules
│   │   ├── SYSTEM_Architecture.md                    ← System architecture overview
│   │   ├── SYSTEM_Build_Decision_Framework.md        ← Projects vs Skills vs MCPs decision guide
│   │   ├── SYSTEM_Agent_Architecture.md              ← AI agent patterns: 4-part framework, orchestration, memory, ReAct vs Plan-Execute
│   │   └── RESEARCH_Claude_Project_Best_Practices.md ← Research: AI agents, MCPs, AI docs, vibe coding, skills ecosystem, deployment
│   │
│   ├── templates/
│   │   ├── output/
│   │   │   ├── DOC_CANONICAL_TEMPLATE.md             ← THE output format for all docs
│   │   │   ├── DEV_PLAN_TEMPLATE.md                  ← Development plan template (product builder)
│   │   │   ├── STARTER_PROMPT_TEMPLATE.md            ← AI coding tool starter prompt template
│   │   │   └── DEBT_Specification.md                 ← Debt entry format
│   │   └── project_instructions/
│   │       ├── PROJECT_INSTRUCTIONS_Docgen_Production.md  ← Paste into Claude.ai ✓
│   │       └── PROJECT_INSTRUCTIONS_Docgen_AI_First.md
│   │
│   ├── checklists/
│   │   ├── CHECKLIST_Human_Quality.md     ← Gate 3 manual review
│   │   ├── CHECKLIST_AI_Quality.md        ← Gate 4 AI self-review
│   │   └── CHECKLIST_Token_Efficiency.md  ← Gate 4 token budget check
│   │
│   └── examples/
│       └── EXAMPLE_Perfect_Setup_Guide.md ← Reference: what 85+ quality looks like
│
├── builders/                              ← Build-type questionnaires + rules
│   ├── product/                           ← ★ Product / startup / SaaS (11-doc bundle)
│   │   ├── BUILDER_Questions.md           ← 8 intake questions + output bundle spec
│   │   └── BUILDER_Rules.md               ← PRD/UX/UI/DevPlan/StarterPrompt rules (90/100 target)
│   ├── claude-project/                    ← Full Claude project from idea
│   │   ├── BUILDER_Questions.md           ← Intake questions + output list
│   │   └── BUILDER_Rules.md               ← CLAUDE.md, instructions, config rules
│   ├── skill/                             ← Skill / slash command
│   │   ├── BUILDER_Questions.md           ← Intake questions (8 required)
│   │   └── BUILDER_Rules.md               ← SKILL.md structure + quality rules
│   ├── mcp/                               ← MCP server documentation
│   │   ├── BUILDER_Questions.md           ← Intake questions (8 required)
│   │   └── BUILDER_Rules.md               ← API ref, auth, error, fallback rules
│   ├── ai-docs/                           ← Single AI doc generation/update
│   │   ├── BUILDER_Questions.md           ← Intake questions (3 modes)
│   │   └── BUILDER_Rules.md               ← Content, how-to, reference rules
│   └── code/                              ← Code documentation
│       ├── BUILDER_Questions.md           ← Intake questions + code quality gate
│       └── BUILDER_Rules.md               ← Setup, API, architecture, ADR rules
│
├── output/                                ← All generated docs
│   └── {domain}/v{X.Y}/{DOMAIN}_{Topic}_v{X.Y}_{YYYY-MM-DD}.md
│
├── config/
│   ├── domain_definitions.json            ← Domain registry (4 domains)
│   └── token_budgets.json                 ← Hard limits per doc type
│
├── skills/                                ← Drop your own skills here (not part of docgen system)
│
├── backlog/
│   └── SYSTEM_DEBT.md                     ← Known gaps and future work
│
└── metrics/
    └── LOG_Generation.md                  ← Track what's been generated
```

---

## Quality Gate Cheat Sheet

| Gate | Checks | Fail action |
|------|--------|-------------|
| 1 · Validation | File name, metadata, domain | Rename and resubmit |
| 2 · Structure | All required sections present | Add missing sections |
| 3 · Content | No vague language, claims backed, code standards | Rewrite |
| 4 · Quality | Token budget, human review, AI review | Cut or revise |
| 5 · Shipping | Version stamped, DEBT logged | Confirm and ship |

Minimum quality score: **85/100**

---

## Authoritative File Priority

When files conflict: `SYSTEM_Exit_Rules.md` > `SYSTEM_Content_Guide.md` > `SYSTEM_Build_Decision_Framework.md` > `builders/[type]/BUILDER_Rules.md` > everything else.

---

## How to Set Up the Claude Project

1. Go to claude.ai → New Project → "Documentation Builder"
2. Sync this folder as the knowledge base
3. Paste `system/templates/project_instructions/PROJECT_INSTRUCTIONS_Docgen_Production.md` into Project Instructions

---

*Documentation Builder v1.5 · April 2026*
