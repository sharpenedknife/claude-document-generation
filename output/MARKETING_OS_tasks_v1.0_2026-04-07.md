# Marketing OS — Tasks & Backlog
**Version:** 1.0 | **Date:** 2026-04-07 | **Purpose:** Known issues, improvement ideas, and future enhancements

---

## Active (Do This Month)

- [ ] **Create first project-marketing-context.md** — Pick one active project, run customer-research + competitive-analysis, output the context file. Takes 1 session, ~5–6K tokens. Required before the system is fully usable.
- [ ] **Test all 4 Claude conversation starters** — Open Marketing OS project in Claude.ai, click each starter, verify routing is correct (right skill, right token estimate, right output format).
- [ ] **Test 2 ChatGPT GPTs** — Open Research Architect and Copy Rewriter, click a conversation starter each, verify canvas opens for long outputs.
- [ ] **Set up analytics tracking for first campaign** — Use analytics-tracking skill to implement open/click/reply tracking for the first cold email campaign.

---

## Backlog — Enhancements

### High Priority

- [ ] **Client isolation test** — Create a second project context (different client) and verify Claude correctly switches context without bleeding between projects. Expected behavior: "Switch to [Project B]" → Claude loads B context, forgets A.
- [ ] **Token usage tracking** — Build a lightweight token log. After each session, Claude estimates tokens used. Monthly: check if within 20–30K budget. Implement as a simple markdown table in tasks.md.
- [ ] **Quality score history** — Log quality scores per campaign. After 5+ campaigns, analyze: what angles score highest? Use to update messaging pillars in project context.
- [ ] **Skill gap audit** — Some skills (designing-growth-loops, community-building, behavioral-product-design) haven't been tested in this system yet. Run one workflow through each, note output quality.
- [ ] **ChatGPT memory protocol** — Define exactly when to update ChatGPT memory. Current gap: memory gets updated ad-hoc. Standardize: update after every session with ICP/messaging/channel learnings.

### Medium Priority

- [ ] **Winning angles library** — After 10+ campaigns, extract top-performing angles (subject lines, hooks, headlines). Store in MARKETING_OS_KnowledgeStructure.md under a new "Winning Angles" section.
- [ ] **Objection handling database** — Collect objections raised in sales calls and email replies. Store per ICP in project-marketing-context.md. Use to pre-empt in future copy.
- [ ] **Multi-project dashboard** — As projects multiply, need a way to see all active projects + their status in one view. Create a simple /agents/DASHBOARD.md that lists: project, active campaigns, last update, next action.
- [ ] **Content calendar integration** — Content Engine in ChatGPT needs an editorial calendar file. Create editorial_calendar.md template and integrate with content-strategy skill workflow.
- [ ] **ChatGPT Projects file structure** — Each project needs its own file set (tone_voice.md, frameworks.md, channel_rules.md). Create these for Marketing OS and Content Engine projects.

### Low Priority

- [ ] **Voice mode testing (ChatGPT)** — Test using voice mode with Marketing OS and Content Engine projects. Useful for dictating campaign ideas during commutes. Note any workflow gaps.
- [ ] **DALL-E integration** — Test using ChatGPT's DALL-E for ad creative image generation alongside Copy Rewriter's text output. Note workflow for combining image + copy in canvas.
- [ ] **Research Architect → external tools** — Research Architect currently operates on provided context only. Explore: can it pull from specific URLs (G2 reviews, Reddit threads, LinkedIn posts) to gather real customer language?
- [ ] **Email platform connection** — Investigate direct integration with Mailchimp/ConvertKit/Apollo. Currently: Claude writes emails → Denis pastes manually. Ideal: Claude outputs in platform-ready format with merge tags.
- [ ] **A/B test results tracking** — Create a simple tracking doc: test, hypothesis, variants, results, winner. Feed results back into quality improvement loop.

---

## Known Issues

| Issue | Severity | Status | Notes |
|-------|----------|--------|-------|
| ChatGPT Projects don't persist files between sessions without re-upload | Medium | Open | Denis must re-upload project context files when starting a new ChatGPT session in a project. Mitigated by memory feature. |
| Claude extended thinking not always triggered for research tasks | Low | Open | Add explicit triggers in CLAUDE.md v1.1. Denis can force with "think carefully about this." |
| Token estimates are approximations | Low | Accepted | Real token counts vary by output length. Estimates are conservative — actual may be 10–20% lower. |
| Conversation starters require Claude Pro/Team | Medium | Accepted | Free plan users: manually type the starter text instead. Not a system limitation. |
| Canvas mode doesn't open automatically for all GPTs without the rule | Medium | Fixed in v1.2 | All 5 GPT files now include canvas rule in system prompt. |

---

## Decided (Won't Do)

| Decision | Reason |
|----------|--------|
| Auto-sync between Claude and ChatGPT projects | No API bridge exists. Manual sync is acceptable — platforms serve different UX needs. |
| Merge Claude and ChatGPT into one workflow | Platforms have different strengths. Claude for strategy/tokens, ChatGPT for canvas/personas. Separation is intentional. |
| Real-time campaign performance monitoring | Out of scope for a prompt-based system. Use native analytics tools (Mailchimp, LinkedIn, Google Analytics). |
| Automated project context updates | Risk of context drift without Denis review. Manual update after each campaign is intentional — forces reflection. |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-07 | Initial release — full dual-platform system (Claude + ChatGPT) |
| v1.1 | 2026-04-07 | UX layer added: conversation starters, artifact mode, mode commands, canvas triggers, scoring rubrics |

---

## Session Log

| Date | Session | Tokens Used | Outcome |
|------|---------|-------------|---------|
| 2026-04-07 | Initial build — all 8 Claude docs + 13 ChatGPT docs | ~45K (est.) | System v1.0 complete |
| 2026-04-07 | UX enhancement — v1.1 (conversation starters, canvas, modes) | ~15K (est.) | System v1.1 complete |

---

## Token Budget Remaining (April 2026)

**Monthly budget:** 20–30K tokens
**Used this month:** ~60K (setup phase — one-time)
**Next month budget:** 20–30K (execution phase)

*Setup token usage is higher than normal — this is a one-time cost. Ongoing monthly usage will normalize to 20–30K.*

---

*Marketing OS v1.0 · Tasks & Backlog · 2026-04-07*
*Update this file after every session with: tokens used, quality scores, learnings*
