# SYSTEM_File_Naming.md — LLM-Optimized Naming Convention

**Why naming matters for AI:** Claude reads filenames before reading content. A file named `SYSTEM_Exit_Rules.md` tells Claude "this is a system framework file about exit rules" before it processes a single word. A file named `rules.md` tells it nothing. Research confirms: descriptive filenames improve AI retrieval accuracy significantly in RAG contexts.

---

## Core Principle

**The filename is the first question it answers.** Every filename should complete the sentence: "This file contains [FILENAME]."

- `SYSTEM_Exit_Rules.md` → "This file contains system exit rules." ✅
- `BUILDER_Questions.md` → "This file contains builder questions." ✅
- `rules.md` → "This file contains... rules? For what?" ❌
- `doc1.md` → No signal at all. ❌

---

## Two Naming Patterns

### Pattern A: Framework Files (system infrastructure)

Files that ARE the documentation system — guides, templates, checklists, builders, research.

```
{TYPE}_{Topic}.md
```

Examples:
```
SYSTEM_Exit_Rules.md
CHECKLIST_Human_Quality.md
BUILDER_Questions.md
RESEARCH_Claude_Best_Practices.md
PROJECT_INSTRUCTIONS_Docgen_Production.md
```

### Pattern B: Generated Output Documents (docs the system produces)

Files that are produced BY the system — the deliverables for users.

```
{DOMAIN}_{Topic}_v{X.Y}_{YYYY-MM-DD}.md
```

Examples:
```
CODE_Stripe_Setup_v1.0_2026-04-03.md
AI-DOCS_Welcome_Guide_v1.0_2026-04-03.md
CLAUDE-PROJECT_Marketing_Hub_v1.0_2026-04-03.md
REFERENCE_API_Config_v2.1_2026-04-03.md
```

---

## TYPE Prefixes — Framework Files

Every framework file MUST start with one of these TYPE prefixes. Type prefix = ALL_CAPS + underscore.

| TYPE Prefix | What It Signals | Examples |
|---|---|---|
| `SYSTEM_` | Authoritative framework rule — read-only, never edit | `SYSTEM_Exit_Rules.md`, `SYSTEM_Coding_Standards.md` |
| `TEMPLATE_` | Document template — blank structure to fill in | `TEMPLATE_Debt_Standard.md` |
| `DOC_` | THE canonical output template | `DOC_CANONICAL_TEMPLATE.md` |
| `CHECKLIST_` | Quality gate checklist | `CHECKLIST_Human_Quality.md`, `CHECKLIST_AI_Quality.md` |
| `EXAMPLE_` | Complete example showing target quality | `EXAMPLE_Perfect_Setup_Guide.md` |
| `BUILDER_` | Builder intake questionnaire or rules file | `BUILDER_Questions.md`, `BUILDER_Rules.md` |
| `RESEARCH_` | Research findings and external source synthesis | `RESEARCH_Claude_Project_Best_Practices.md` |
| `PROJECT_INSTRUCTIONS_` | Claude.ai project instructions — paste-ready | `PROJECT_INSTRUCTIONS_Docgen_Production.md` |
| `LOG_` | Logs, metrics, generation tracking | `LOG_Generation.md` |
| `DEBT_` | Technical debt specification or tracker | `DEBT_Specification.md`, `SYSTEM_DEBT.md` |

### Special auto-detected files (no TYPE prefix)

These file names are auto-detected by tools and must be EXACT — no prefix:

| File | Why exact | Detected by |
|---|---|---|
| `CLAUDE.md` | Auto-loaded by Claude Code, Claude Projects | Claude |
| `README.md` | Auto-displayed by GitHub, file browsers | GitHub, many tools |
| `CONTRIBUTING.md` | Standard open-source convention | GitHub |
| `LICENSE` | Standard convention — no extension | GitHub, npm, pip |

---

## DOMAIN Categories — Output Documents

Must match `config/domain_definitions.json`. Used as the CATEGORY prefix in output file names.

| Domain prefix | Domain | Description |
|---|---|---|
| `CLAUDE-PROJECT_` | claude-project | Full Claude project setup from an idea |
| `AI-DOCS_` | ai-docs | Individual AI docs (how-tos, references, features) |
| `CODE_` | code | Code documentation (setup, API, architecture, ADR) |
| `REFERENCE_` | reference | Reference material (configs, schemas, commands) |

---

## Separator Rules

This is critical for LLM parsing. Different separators communicate different relationships:

| Separator | Role | Where |
|---|---|---|
| `_` (underscore) | Separates **elements** from each other | Between TYPE and Topic; between Topic and Version; between Version and Date |
| `_` or PascalCase | Separates **words within** an element | `Exit_Rules` or `ExitRules` — both valid within a topic |
| `-` (hyphen) | Separates words in **folder names only** | `claude-project/`, `ai-docs/` — never in file names |
| Never use spaces | N/A | Spaces break paths and LLM file tools |

```
SYSTEM_Exit_Rules.md
^      ^ ^         ^
TYPE   _ Topic     .ext

CODE_Stripe_Setup_v1.0_2026-04-03.md
^    ^      ^     ^    ^
DOM  _Topic_      _Ver _Date
```

---

## Topic Naming Rules

Topics in framework files use `PascalCase` or `Title_Case`:

```
✅ GOOD  SYSTEM_Exit_Rules.md       (Title_Case — first letter each word)
✅ GOOD  SYSTEM_ExitRules.md        (PascalCase — also valid)
❌ BAD   SYSTEM_exit_rules.md       (all lowercase — no visual separation from prefix)
❌ BAD   SYSTEM_EXITRULES.md        (all caps — looks like another prefix)
❌ BAD   SYSTEM_Exit-Rules.md       (hyphen in filename — reserved for folders)
```

Topics in output documents use `Title_Case` (matches the document's title):

```
✅ GOOD  CODE_Stripe_Payment_Setup_v1.0_2026-04-03.md
❌ BAD   CODE_stripe-payment-setup_v1.0_2026-04-03.md
❌ BAD   CODE_StripePaymentSetup_v1.0_2026-04-03.md  (PascalCase harder to read at speed)
```

---

## Version Rules

```
v1.0    Initial release
v1.1    Minor update (backwards compatible)
v2.0    Major revision (breaking changes or full rewrite)
```

**Include VERSION when:** Multiple versions in active use, or backwards compatibility tracking needed.

**Omit VERSION when:** Only one version exists, or version tracked in folder structure.

---

## Date Rules

Use ISO 8601 format: `YYYY-MM-DD`. Always. No exceptions.

```
✅ 2026-04-03   (ISO 8601 — sorts correctly, machine-readable)
❌ April 2026   (not sortable)
❌ 04-03-2026   (ambiguous locale format)
❌ 2026-Q1      (acceptable for quarterly docs only)
```

**Include DATE when:** Content has a shelf life, quarterly/annual updates, or distinguishing "old" from "current" matters.

**Omit DATE when:** Evergreen content, or using version numbers instead.

---

## Companion Files

Every generated output document ships with two companions:

```
CODE_Stripe_Setup_v1.0_2026-04-03.md          ← Main doc
CODE_Stripe_Setup_v1.0_2026-04-03.DEBT.md     ← Known gaps
CODE_Stripe_Setup_v1.0_2026-04-03.metadata.json ← Generation metadata
```

All three always together. Missing a companion = Gate 5 fail.

---

## Folder + Filename Combined Context

The folder provides the domain context. The filename provides the type + topic context. Together they create unambiguous meaning for an AI agent navigating the workspace.

```
✅ GOOD — full context from path alone:
system/guides/SYSTEM_Exit_Rules.md
  └── "system framework guide: exit rules"

builders/claude-project/BUILDER_Questions.md
  └── "builder for claude-project domain: intake questions"

output/claude-project/v1.0/CLAUDE-PROJECT_Code_Reviewer_v1.0_2026-04-03.md
  └── "output: claude-project domain, Code Reviewer assistant, version 1.0, April 2026"

❌ BAD — ambiguous path:
builders/claude-project/rules.md
  └── "rules? for what? for whom? which version?"

output/doc1.md
  └── completely opaque to AI and humans
```

---

## Forbidden Patterns

❌ Never use in file names:
- Spaces → `Exit Rules.md` (use `Exit_Rules.md`)
- Hyphens → `Exit-Rules.md` (use `Exit_Rules.md` — hyphens for folders only)
- Special chars → `(final)`, `#`, `@`, `$`, `%`
- Emojis → `🚀_Launch.md`
- Double underscores → `SYSTEM__Exit.md`
- Consecutive version + date without underscore → `v1.02026-04-03`
- Abbreviations in topic → `Sys_Ex_Rl.md` (spell it out)
- `[ARCHIVED]` or `[DEPRECATED]` brackets → use `ARCHIVED_` or `DEPRECATED_` prefix instead

---

## Naming Checklist

Before saving any file, verify:

**Framework files:**
- [ ] Starts with a valid TYPE prefix (`SYSTEM_`, `CHECKLIST_`, `BUILDER_`, etc.)
- [ ] Topic is PascalCase or Title_Case (not all-lowercase, not all-caps)
- [ ] No hyphens in filename (hyphens only in folder names)
- [ ] No spaces or special characters

**Output documents:**
- [ ] Starts with valid DOMAIN prefix (`CLAUDE-PROJECT_`, `AI-DOCS_`, `CODE_`, `REFERENCE_`)
- [ ] Topic is Title_Case, underscore-separated words
- [ ] Version included if needed (`v1.0` format)
- [ ] Date in ISO 8601 if time-sensitive (`YYYY-MM-DD`)
- [ ] Both companion files created (`DEBT.md`, `metadata.json`)

**Both:**
- [ ] Full path makes unambiguous sense (folder + filename together)
- [ ] Filename answers "What does this file contain?" without reading it

---

## Migration Reference

Current violations → corrected names:

| Was | Should be | Reason |
|---|---|---|
| `builder.md` | `BUILDER_Questions.md` | No type prefix |
| `rules.md` | `BUILDER_Rules.md` | No type prefix |
| `generation_log.md` | `LOG_Generation.md` | No type prefix |
| `Project_Instructions_X.md` | `PROJECT_INSTRUCTIONS_X.md` | Inconsistent case |
| `[ARCHIVED]_doc.md` | `ARCHIVED_doc.md` | Brackets break many systems |
| `doc-topic.md` | `DOC_Topic.md` | Hyphens in filenames reserved for folders |

---

*Documentation Builder · File Naming Standard v1.1 · April 2026*
*Research basis: Anthropic context engineering docs, RAG knowledge base best practices, Claude Code community conventions*
