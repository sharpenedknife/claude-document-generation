---
for_document: "docgen_system"
generated_at: 2026-04-02T15:25:00Z
total_items: 12
critical_items: 0
high_priority_items: 4
medium_priority_items: 5
low_priority_items: 3
---

# Technical Debt: Docgen System

For: Documentation Generation System (docgen framework)

---

## Overview

The docgen system is production-ready for use. This debt tracks future improvements, automation enhancements, and domain-specific features that will make the system more powerful over time.

No critical items. System ships complete.

---

## Priority 1: High (Should Address Soon)

### Item 1.1: Builder Automation Framework
- **Type:** feature_missing
- **Impact:** Builders currently manual. Automation reduces 80% of builder work.
- **Effort:** 2-3 weeks
- **Owner:** Engineering team
- **Details:** Create questionnaire → output generator → gate runner → file namer pipeline. Automates entire flow for each domain builder.

### Item 1.2: Skill Suggestion Engine
- **Type:** feature_missing
- **Impact:** Patterns detected manually. Auto-suggestion surfaces repeatable workflows.
- **Effort:** 1-2 weeks
- **Owner:** Product/Engineering
- **Details:** Analyze generated docs for repeating patterns → suggest skill creation. Detects when 3+ docs follow same workflow.

### Item 1.3: Token Budget Validation Script
- **Type:** tooling_missing
- **Impact:** Manually checking tokens. Automation prevents budget overruns.
- **Effort:** 3-5 days
- **Owner:** Engineering
- **Details:** Script that counts tokens in doc, compares to domain budget, flags overages. Integrate into exit gate 4.

### Item 1.4: Monthly Metrics Dashboard
- **Type:** tooling_missing
- **Impact:** No visibility into quality trends. Dashboard shows health over time.
- **Effort:** 1 week
- **Owner:** Analytics/Product
- **Details:** Plot: quality scores by domain, token efficiency, gate pass rates, skills created, docs generated. Identify trends.

---

## Priority 2: Medium (Nice to Have)

### Item 2.1: Example Library
- **Type:** documentation_incomplete
- **Impact:** No examples of "perfect docs" for each type. Examples teach by showing.
- **Effort:** 2-3 days
- **Owner:** Documentation
- **Details:** Create 1-2 example docs per type (setup, API, GTM, etc.) showing all standards perfectly applied.

### Item 2.2: Domain-Specific Checklists
- **Type:** feature_missing
- **Impact:** Generic checklists. Domain-specific checklists catch domain issues faster.
- **Effort:** 3-5 days
- **Owner:** Domain experts
- **Details:** GTM-specific quality checks, Design-specific checks, Content-specific checks. Supplement gate 3.

### Item 2.3: Deprecation Automation
- **Type:** process_automation
- **Impact:** Manual deprecation process. Automation reduces errors and overhead.
- **Effort:** 3-5 days
- **Owner:** Engineering
- **Details:** Script that marks v1.x deprecated, moves to archive/, updates projects, logs deprecation. One command to deprecate.

### Item 2.4: Cross-Doc Link Validation
- **Type:** tooling_missing
- **Impact:** Broken links discovered by users. Validation catches before shipping.
- **Effort:** 2-3 days
- **Owner:** Engineering
- **Details:** Scan all doc references, verify targets exist. Integrate into exit gate 5.

### Item 2.5: Skill Auto-Integration
- **Type:** feature_missing
- **Impact:** Published skills manual. Auto-integration adds to projects automatically.
- **Effort:** 3-5 days
- **Owner:** Engineering
- **Details:** When skill marked "published", auto-add to docgen_base project knowledge base.

---

## Priority 3: Low (Future Backlog)

### Item 3.1: Template Generator
- **Type:** feature_nice_to_have
- **Impact:** Creating new domain builders manual. Generator speeds up setup.
- **Effort:** 1 week
- **Owner:** Engineering
- **Details:** CLI tool: "create-builder gtm" → generates builder folder structure + questionnaire template + output rules.

### Item 3.2: AI Quality Auto-Fixer
- **Type:** feature_experimental
- **Impact:** Gate 3 failures require manual rewrite. AI could suggest fixes.
- **Effort:** 2-3 weeks (requires prompt engineering)
- **Owner:** AI/Product
- **Details:** Claude suggests rewrites for vague language, missing examples, unclear steps. Human reviews + approves.

### Item 3.3: Multi-Language Support
- **Type:** feature_future
- **Impact:** All docs currently English-only. Multi-language expands reach.
- **Effort:** 4-6 weeks (per language)
- **Owner:** Localization team
- **Details:** Templates + guides + examples translated. Start with Russian (user preference noted).

---

## Known Limitations

### Limitation 1: Manual Builder Creation
- **Scope:** Creating new domain builders requires manual setup
- **Reason:** No builder generator yet (P1 item 1.1)
- **Workaround:** Use existing builder structure as template, follow SYSTEM_Folder_Structure.md

### Limitation 2: No Analytics Yet
- **Scope:** Cannot track quality trends, doc generation volume, most-used builders
- **Reason:** No dashboard implemented (P1 item 1.4)
- **Workaround:** Manual review of metrics/generation_log.md monthly

### Limitation 3: No Automation for Exit Gates
- **Scope:** Running all 5 gates currently manual
- **Reason:** No gate automation pipeline (P1 item 1.1)
- **Workaround:** Use checklists in system/checklists/ to verify manually

### Limitation 4: Token Budgets Unvalidated Against Real Sessions
- **Scope:** Token budgets in `config/token_budgets.json` are estimates from templates, not measured from real generation sessions.
- **Reason:** System has not yet run 10+ real production sessions to calibrate (Verification 1 in this file).
- **Workaround:** After every 5 real sessions, measure actual tokens/stage and adjust budgets if needed.

---

## Content Decisions

### Decision 1: English-Only Launch
- **Original Plan:** Multi-language (EN, RU, etc.)
- **Actual:** English-only initially
- **Reason:** Time to market. Russian support in P3 (item 3.3)
- **Impact:** Non-English users need translation or English proficiency
- **When to Revisit:** After first 50 docs generated, if demand warrants

### Decision 2: Manual Questionnaires
- **Original Plan:** Auto-generated questionnaires from domain analysis
- **Actual:** Hand-crafted questionnaires per builder
- **Reason:** Better UX, more targeted questions
- **Impact:** Creating new builders takes longer
- **When to Revisit:** When builder automation framework ready (P1 item 1.1)

---

## Dependencies

### Dependency 1: Builder Automation Framework (P1.1)
- **Blocks:** Scaling to 10+ builders efficiently
- **Waiting For:** Engineering availability
- **Owner:** Engineering team
- **Expected Date:** Q3 2026

### Dependency 2: Metrics Dashboard (P1.4)
- **Blocks:** Visibility into system health
- **Waiting For:** Analytics team + engineering
- **Owner:** Analytics/Product
- **Expected Date:** Q2 2026

---

## Verification Needed

### Verification 1: Token Budgets Realistic
- **Current Status:** Budgets expanded in v1.6 to cover product bundle doc types (PRD, UX, UI, Vision, Data Schema, Dev Plan, Starter Prompt). Not yet validated against real generated docs.
- **Who Should Verify:** Log actual token counts in `metrics/LOG_Generation.md` for first 10 generated docs per type
- **How to Verify:** Compare LOG_Generation.md `tokens` column to `config/token_budgets.json` budgets. If avg actual > 80% of budget for any type, tighten generation rules. If avg actual < 50% of budget, lower the budget.
- **Monitoring trigger:** After every 5 docs of same type, review ratio. If quality/token < 0.028, initiate budget review.
- **Blocker?:** No (budgets are now type-specific; v1.6 generation behavioral rules enforce lean writing)

### Verification 2: Exit Gates Sufficient
- **Current Status:** Defined theoretically. Not tested with real user workflows.
- **Who Should Verify:** Product team after 5 docs generate
- **How to Verify:** Check if gates catch all quality issues users encounter
- **Blocker?:** No (gates can evolve)

---

## Skills to Create (From System Patterns)

If patterns emerge, suggest creating reusable skills:

### Potential Skill 1: Doc Gap Analysis
- **Type:** repeatable_process
- **Usage:** When reviewing completeness of doc set
- **Scope:** Analyze all docs, identify missing coverage, suggest new docs needed
- **Status:** suggested
- **Owner:** Product/Documentation team

### Potential Skill 2: Quality Gate Automation
- **Type:** process_automation
- **Usage:** Running all 5 gates manually across multiple docs
- **Scope:** Batch run gates, report failures, auto-fix where possible
- **Status:** suggested
- **Owner:** Engineering team

---

## Changelog

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-04 | Added Research Gates to all 4 builders (T-01–T-04) | Forces data collection before generation — prevents ASSUMED-heavy docs |
| 2026-04-04 | Added lazy skill loading rules to SKILL_MAP, project instructions, CLAUDE.md (T-05–T-07) | Prevents context window waste from preloading unused skills |
| 2026-04-06 | Wired prompt-building:* plugin skills to SKILL_MAP stages 5+11 and BUILDER_Rules (product + claude-project) | AI-native products now call installed skills instead of reading local SKILL.md files |
| 2026-04-06 | Added product bundle doc-type budgets to token_budgets.json (T-23) | PRD, UX, UI, Vision, Data Schema, Dev Plan, Starter Prompt now have specific token caps |
| 2026-04-06 | Added generation behavioral rules to SYSTEM_Token_Optimization.md (T-24) | Lean writing rules enforced during generation, not just at review |
| 2026-04-06 | Added token constraint header to DOC_CANONICAL_TEMPLATE.md (T-25) | Every doc now declares its budget upfront |
| 2026-04-06 | Added Write Lean pre-generation checklist to SKILL_MAP.md (T-26) | Generator applies token constraints before writing first word |
| 2026-04-02 | Created initial SYSTEM_DEBT.md | System shipped v1.0, logged improvement backlog |

---

**This SYSTEM_DEBT.md is living. Update as items are completed or new debt discovered.**
