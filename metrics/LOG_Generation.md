# Generation Log

**Append-only.** One row per generated doc. Do not edit past rows.
**Updated:** After every generation session.

---

## How to Log

After each doc generation, append one row to the table below:

```
| YYYY-MM-DD | {doc_name} | {domain} | {type} | v{X.Y} | {builder} | {tokens} | {score}/100 | {gates: 1-5} | PASS/FAIL |
```

- **tokens:** Estimate from output length. 1 page ≈ 500 tokens. Use `wc -w output/{file}.md` × 1.3 as rough count.
- **score:** Run CHECKLIST_AI_Quality.md, calculate per SYSTEM_Token_Optimization.md formula.
- **gates:** List gate numbers passed (e.g. "1,2,3,4,5" = all). First failed gate stops the list.
- **status:** PASS (gates 1–5 all passed) or FAIL:{gate} (e.g. FAIL:3 = content gate failed).

**Quality/token:** After logging, calculate: `score ÷ tokens`. Target ≥ 0.030. Log to Monthly Summary.

---

## Log

| Date | Doc | Domain | Type | Version | Builder | Tokens | Score | Gates | Status |
|------|-----|--------|------|---------|---------|--------|-------|-------|--------|
| 2026-04-04 | SYSTEM improvements (T-01–T-22) | system | audit | v1.5 | — | — | — | — | DONE |
| 2026-04-06 | SKILL_MAP + builder rules (prompt-building wiring) | system | improvement | v1.6 | — | — | — | — | DONE |
| 2026-04-06 | ChatGPT port (AGENTS.md, CHATGPT_CUSTOM_INSTRUCTIONS, chatgpt-project builder) | chatgpt-port | output | v1.6 | chatgpt-project | — | — | — | DONE |

---

## Monthly Summary

### April 2026

| Metric | Value | Target |
|--------|-------|--------|
| Total docs generated | 0 (system work only) | — |
| Docs within token budget | — | ≥ 95% |
| Avg quality score | — | ≥ 85 |
| Avg tokens/doc | — | ≤ budget |
| Avg quality/token | — | ≥ 0.030 |
| Gate pass rate (first attempt) | — | ≥ 80% |
| Most common builder | — | — |
| Most common failure gate | — | — |

**Action items this month:** Start logging real docs. Validate token budgets after first 5 per type.

---

## Budget Reference (Quick Lookup)

| Doc Type | Budget | Quality/token target |
|----------|--------|---------------------|
| PRD | 2,500 | 0.034 |
| UX Research | 1,800 | 0.047 |
| UI Spec | 1,800 | 0.047 |
| Product Vision | 1,000 | 0.085 |
| Data Schema | 2,000 | 0.043 |
| API Spec | 3,000 | 0.028 |
| Architecture | 3,500 | 0.024 |
| Dev Plan | 3,500 | 0.024 |
| Starter Prompt | 800 | 0.106 |
| CLAUDE.md (product) | 1,500 | 0.057 |
| Setup Guide | 2,500 | 0.034 |
| **Bundle total (11 docs)** | **22,000** | **≥ 0.030 avg** |

*Source of truth: `config/token_budgets.json`*
