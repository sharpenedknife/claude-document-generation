# Marketing OS — Tasks & Backlog
**Version:** 1.1 | **Date:** 2026-04-07 | **Architecture:** v1.6 — 3-Tier Brain/Skills/GPTs

---

## Setup Checklist (Do Once)

- [ ] **Build all 6 ChatGPT GPTs** inside the single "Marketing OS" ChatGPT Project
  — ICP Builder · Messaging Builder · Funnel Builder · Content Builder · Build Planner · Landing Builder
  — Each GPT: paste instructions from `GPT_0X_[Name].md`, enable correct capabilities, add 4 conversation starters
- [ ] **Create Claude.ai Marketing OS Project**
  — Upload `MARKETING_OS_CLAUDE_v1.6_2026-04-07.md` to Knowledge
  — Set custom instructions (paste from SetupGuide Step 3)
  — Add 4 conversation starters (🧠 · 📊 · 🏗️ · 🔄)
- [ ] **Create Marketing OS Custom Style in Claude.ai**
  — Profile → Styles → Create Style → paste from SetupGuide Step 5
- [ ] **Seed Claude memory** (first session)
  — "Remember: Product = [X]. Primary ICP = [role, company, pain]. Format preference = artifact for all structured output."
- [ ] **Test the brief → execute → evaluate loop** with one real task
  — Click 🧠 in Claude → get brief → paste in Content Builder → return output → evaluate
- [ ] **Test HTML landing page production**
  — Click 🏗️ in Claude → describe a product + ICP → verify HTML artifact opens and renders

---

## Active (This Month)

- [ ] **First ICP profile** — Run ICP Builder GPT on your primary product. Bring output to Claude for evaluation. Store profile in Claude Project Knowledge.
- [ ] **First landing page** — Use the full workflow: ICP Builder → Messaging Builder → Landing Builder draft → Claude HTML artifact. Measure: does the HTML render correctly? Is it developer-handoff ready?
- [ ] **Upload Documentation Builder output** — When Documentation Builder generates docs for a product, upload `CONTEXT_Product.md` and `CONTEXT_Technical.md` to Claude Project Knowledge. This replaces manual context setup.
- [ ] **Test Claude Skill escalation** — Deliberately score a ChatGPT output <5, then escalate to the equivalent Claude Skill. Verify the quality jump is worth the extra tokens.

---

## Backlog — Enhancements

### High Priority

- [ ] **Winning angles library** — After 5+ campaigns, extract top-performing copy angles (hooks, headlines, CTAs that scored ≥8/10). Store in a `MARKETING_OS_WinningAngles_v1.0.md` file in Project Knowledge. Claude references when generating briefs.
- [ ] **Objection database** — Collect objections from sales calls and email replies per ICP. Store in Project Knowledge. Claude pre-empts them in every brief automatically.
- [ ] **Scheduled Tasks in ChatGPT** — Set up the 3 recurring tasks (weekly brief reminder, monthly ICP refresh, Friday check-in). See `CHATGPT_PROJECTS_AND_TASKS_v1.0.md` for prompts.
- [ ] **Quality score log** — After every Claude evaluation, log: date · content type · score · verdict · what was fixed. Build pattern over time. Template: `| Date | Type | Score | Verdict | Fix Applied |`

### Medium Priority

- [ ] **HTML artifact library** — Keep a record of every landing page Claude builds. File: `MARKETING_OS_HTMLLibrary_v1.0.md` with: page name · date · shareable link · conversion rate if known. Reference when building similar pages.
- [ ] **Tier 2 skill test results** — Run each Claude Skill once, log: skill name · input quality · output quality · tokens used · vs ChatGPT GPT comparison. Decide which skills are worth using in production vs. sticking to GPT.
- [ ] **Brief quality retrospective** — After 10+ briefs, review: which brief fields produce the best GPT output? Which fields does ChatGPT ignore? Trim the brief format to keep only what actually affects quality.
- [ ] **Custom GPT knowledge uploads** — Upload ICP profiles + messaging frameworks to the GPTs that need them (Messaging Builder, Content Builder, Landing Builder). Currently GPTs are stateless; knowledge files improve quality for repeat products.

### Low Priority

- [ ] **Image generation workflow** — Landing Builder can generate DALL-E hero mockups. Test: does it produce useful visual direction for developers? Or is it noise? Keep if useful, remove from instructions if not.
- [ ] **Voice mode testing** — Test dictating campaign requests via Claude voice mode on mobile. Useful for capturing ideas on the go. Verify Claude opens artifacts correctly on mobile.
- [ ] **A/B result tracking doc** — Create a running log: what was tested, hypothesis, winner, improvement. Feed winners back into brief templates.

---

## Known Issues

| Issue | Severity | Status | Workaround |
|---|---|---|---|
| Memory not available in custom GPTs | High | Platform limitation — won't fix | Context comes from Claude briefs. GPTs are intentionally stateless. |
| Canvas doesn't auto-open 100% of the time | Medium | GPT instruction adds explicit rule | If it doesn't open: type "Open canvas and put the output there" |
| Code Interpreter requires explicit trigger | Medium | Noted in GPT instructions | Ask explicitly: "Build this as a table in Code Interpreter, offer CSV" |
| Claude model selection is manual | Low | User-controlled | Override in chat: "Use Opus for this" / "Use Haiku for this" |
| Extended thinking fires inconsistently | Low | Criteria defined in CLAUDE.md | Say "Use deep thinking" to force it |
| HTML artifact requires no external dependencies | Low | By design | Claude builds self-contained HTML with inline CSS. No CDN links. |
| ChatGPT Scheduled Tasks don't run inside GPTs | Medium | Platform limitation | Scheduled task outputs land in main ChatGPT, not in a GPT. Copy output manually to the right GPT. |

---

## Decided (Won't Do)

| Decision | Reason |
|---|---|
| Per-product ChatGPT Projects | One "Marketing OS" project for all — context comes from Claude briefs |
| Claude executes all content directly | Budget: Claude at ~$20K+ tokens/month for copy alone vs ChatGPT flat $20/month |
| Auto-sync between Claude and ChatGPT | No API bridge. Manual paste is the workflow. Intentional. |
| Real-time performance monitoring | Out of scope. Use native analytics (GA4, Mailchimp, etc.) |
| Automated project context updates | Manual review required — forces Denis to verify context is current |

---

## Session Log

| Date | Version | Tokens (est.) | What Was Done |
|---|---|---|---|
| 2026-04-07 | v1.0 | ~45K | Initial build — full dual-platform system (Claude + ChatGPT) |
| 2026-04-07 | v1.1 | ~15K | UX layer: conversation starters, canvas, scoring rubrics |
| 2026-04-07 | v1.2 | ~8K | Landing page workflow added (Landing Builder GPT) |
| 2026-04-07 | v1.3 | ~10K | Brain/execution architecture — Claude = brain, ChatGPT = execution |
| 2026-04-07 | v1.4 | ~20K | Full platform UI/UX: Artifacts, Style, Code Interpreter, Image Gen, Scheduled Tasks |
| 2026-04-07 | v1.5 | ~12K | Hardened: all files cut to <90 lines, critical rules top-loaded |
| 2026-04-07 | v1.6 | ~8K | HTML production added to Claude, single ChatGPT project, stateless GPTs |

---

## Monthly Token Budget Reference

| Mode | Claude tokens | ChatGPT |
|---|---|---|
| Execution only (briefs + eval) | 8–15K | flat $20 |
| + HTML production (3–5 pages) | 15–25K | flat $20 |
| + Claude Skills (escalation) | 20–35K | flat $20 |
| New market entry / launch month | 30–50K | flat $20 |

Claude Pro: flat $20/month. Tokens are per-session, not metered on Pro.
Claude API (if using): ~$0.003/1K tokens (Sonnet). 20K tokens = $0.06.

---

## How to Update This File

After every session:
1. Move completed active tasks to Session Log
2. Add any new known issues discovered
3. Log tokens used (estimate from session)
4. Note any brief format changes or quality improvements

---

*Marketing OS Tasks v1.1 · 3-Tier Architecture · 2026-04-07*
