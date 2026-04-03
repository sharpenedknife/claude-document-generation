# Documentation Builder (Docgen)

AI-powered documentation generation system. Describe what you want to build — get a complete, implementation-ready bundle an AI coding agent can use to start building immediately.

**Status:** ✅ Production Ready (v2.1)

---

## What It Does

You describe your project. Docgen asks the right questions, then generates a complete bundle of documentation that an AI coding agent (Claude, Cursor, Windsurf, Codex) can use to build the thing correctly — without you needing to know how to write technical specs.

**Four build types:**

| Type | What you get | Use when |
|------|-------------|----------|
| 🏗️ Product / Startup | 11-doc implementation bundle (PRD · UX · UI · Architecture · Data Schema · API Spec · Setup · Dev Plan · CLAUDE.md · Starter Prompt) | Building an app, SaaS, tool, or platform |
| 🤖 Claude Project | CLAUDE.md · Project instructions · Knowledge base structure | Setting up a persistent Claude workspace for a team |
| ⚡ Skill | SKILL.md · evals.json · packaging | Creating a repeatable workflow or `/command` |
| 🔌 MCP Integration | Setup · API Reference · Auth · Troubleshooting guides | Connecting Claude to a live external tool |

---

## Quick Start (Claude Projects)

1. Go to [claude.ai](https://claude.ai) → Projects → **New Project** → name it `Documentation Builder`
2. In Project Instructions, paste the contents of `system/templates/project_instructions/PROJECT_INSTRUCTIONS_Docgen_Production.md`
3. Upload the knowledge base: all files from `system/`, all files from `builders/`, plus `CLAUDE.md` and `config/token_budgets.json`
4. Open a chat → say **"hi"** → the navigation menu appears automatically
5. Describe what you want to build — Docgen asks questions, confirms scope, generates your bundle

For detailed setup instructions, see `output/DOCGEN_Startup_Guide_v1.0_2026-04-03.md`.

---

## How It Works

```
You describe idea
      ↓
Docgen identifies build type (Product / Claude Project / Skill / MCP)
      ↓
Conversational intake — asks 8 questions, one at a time
      ↓
Confirms generation plan (your last chance to adjust scope)
      ↓
Generates all docs in dependency order
      ↓
Delivers zip bundle
      ↓
You paste STARTER_PROMPT into your AI tool → start building
```

---

## File Structure

```
Documentation/
├── CLAUDE.md                        ← Master navigation (start here)
├── README.md                        ← This file
│
├── system/                          ← Read-only framework
│   ├── guides/                      ← 14 system standards + research
│   ├── templates/
│   │   ├── output/                  ← DOC_CANONICAL_TEMPLATE, DEV_PLAN_TEMPLATE, STARTER_PROMPT_TEMPLATE
│   │   └── project_instructions/   ← Paste into Claude.ai Projects
│   ├── checklists/                  ← Quality gate verification
│   └── examples/                   ← Reference: what 85+ quality looks like
│
├── builders/                        ← Build-type questionnaires + rules
│   ├── product/     ★              ← Product builder (11-doc bundle, 90/100 quality target)
│   ├── claude-project/
│   ├── skill/
│   ├── mcp/
│   ├── ai-docs/
│   └── code/
│
├── output/                          ← All generated docs + examples
├── config/                          ← Domain definitions, token budgets
├── backlog/                         ← SYSTEM_DEBT.md
├── metrics/                         ← LOG_Generation.md
└── skills/                          ← Drop your own skills here
```

---

## Quality Standards

Every generated doc passes 5 quality gates before it ships:

| Gate | Checks | Fail = |
|------|--------|--------|
| 1 · Validation | File name, metadata, domain | Rename and resubmit |
| 2 · Structure | All required sections present | Add missing sections |
| 3 · Content | No vague language, claims backed, code standards | Rewrite |
| 4 · Quality | Token budget, human review, AI review | Cut or revise |
| 5 · Shipping | Version stamped, DEBT logged | Confirm and ship |

- **Minimum quality score:** 85/100 (product bundles: 90/100)
- **Token budgets:** enforced per doc type — see `config/token_budgets.json`

---

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Master navigation + rules for the entire system |
| `system/guides/SYSTEM_Exit_Rules.md` | The 5 quality gates — authoritative |
| `system/guides/SYSTEM_Build_Decision_Framework.md` | How to identify what type of thing to build |
| `system/guides/SYSTEM_Content_Guide.md` | Required sections per doc type |
| `system/templates/output/DOC_CANONICAL_TEMPLATE.md` | The only valid output format |
| `system/templates/output/DEV_PLAN_TEMPLATE.md` | Development plan structure |
| `system/templates/output/STARTER_PROMPT_TEMPLATE.md` | AI coding tool starter prompt |
| `builders/product/BUILDER_Questions.md` | 8 intake questions for product builds |
| `builders/product/BUILDER_Rules.md` | Rules enforced on every product doc |
| `output/DOCGEN_Startup_Guide_v1.0_2026-04-03.md` | Human setup + usage guide |
| `output/DOCGEN_Navigation_Menu.html` | Interactive HTML navigation menu |

---

## Product Bundle Contents (11 docs)

When you build a product, Docgen generates:

```
{ProductName}_Implementation_Bundle_v1.0_{date}/
├── PRD_{name}_v1.0.md          ← Feature requirements + acceptance criteria
├── UX_{name}_v1.0.md           ← User journeys + flows
├── UI_{name}_v1.0.md           ← Screen list + component specs
├── PRODUCT_Vision_{name}_v1.0.md
├── ARCH_System_{name}_v1.0.md  ← Tech stack + folder structure
├── DATA_Schema_{name}_v1.0.md  ← Database entities + relationships
├── API_Spec_{name}_v1.0.md     ← All API endpoints
├── SETUP_Environment_{name}_v1.0.md ← Setup + deployment
├── DEV_Plan_{name}_v1.0.md     ← ★ Implementation plan (phases → files → criteria)
├── CLAUDE.md                   ← For the new project (read this first)
└── STARTER_PROMPT_{name}.md    ← ★ Paste into AI tool to begin building
```

The ★ files are what you use to start building. Paste `STARTER_PROMPT` into Claude, Cursor, or Windsurf. The AI reads all context files and begins Phase 0.

---

## Contributing

See `CONTRIBUTING.md`

## License

MIT License — see `LICENSE`

---

*Documentation Builder v2.1 · April 2026*
*Repo: [github.com/sharpenedknife/claude-document-generation](https://github.com/sharpenedknife/claude-document-generation)*
