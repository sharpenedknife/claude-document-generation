# Active Campaigns
**Last updated:** [YYYY-MM-DD]
**Updated by:** Claude (auto) / Denis (manual)

---

## How to use this file

Claude reads this at session start to understand what's running, what's been shipped, and what's blocked.
After every session where campaign status changes: Claude updates this file automatically.
Denis can also update manually between sessions.

---

## Active Campaigns

### Campaign: [Name]
**Status:** 🟡 In Progress
**Goal:** [What success looks like — specific metric]
**ICP:** [Which profile from ICP.md]
**Channel:** [Email / LinkedIn / Paid / Content / etc.]
**Start date:** [Date]
**Target date:** [Date]

**Where it is now:**
- [x] ICP brief generated — [date]
- [x] ICP Builder output received — score [X]/10
- [ ] Messaging brief sent to Messaging Builder
- [ ] Copy brief sent to Content Builder
- [ ] Copy evaluated — awaiting
- [ ] Revision sent (if needed)
- [ ] Shipped

**Last evaluation:** [Date] · [Content type] · Score: [X]/10 · Verdict: [SHIP / REVISE]
**Next action:** [What Denis or Claude needs to do next]

**Files:**
- Brief: `briefs/[date]_[gpt]_brief.md`
- Output: `output/copy/[type]_[date].md`

---

### Campaign: [Name]
**Status:** 🟢 Shipped
**Goal:** [Metric]
**Channel:** [Channel]
**Shipped:** [Date]
**Final score:** [X]/10
**Result:** [What happened — open rate, CTR, replies, conversions if known]
**What worked:** [Specific angle or element that performed]
**What to repeat:** [Yes/No — and why]

---

### Campaign: [Name]
**Status:** 🔴 Blocked
**Blocked by:** [What's missing — ICP data / copy not approved / waiting for asset]
**Next action:** [Specific step to unblock]

---

## Campaign Queue (Not Yet Started)

| Campaign | Goal | Channel | ICP | Priority | Notes |
|---|---|---|---|---|---|
| [Name] | [Goal] | [Channel] | [ICP] | [High/Med/Low] | [Notes] |
| [Name] | [Goal] | [Channel] | [ICP] | [High/Med/Low] | [Notes] |

---

## Shipped Campaigns — Archive

| Campaign | Channel | Score | Result | Date shipped |
|---|---|---|---|---|
| [Name] | [Channel] | [X]/10 | [Metric result] | [Date] |

---

## Campaign Templates In Progress

| Template | Type | Purpose | Status |
|---|---|---|---|
| [Name] | [Email / Ad / Page] | [What it's for] | [Draft / Evaluated / Production] |

---

## Monthly Summary

**Month:** [Month Year]
**Campaigns run:** [N]
**Average evaluation score:** [X]/10
**Channels used:** [List]
**Best performer:** [Campaign name · score · result]
**Insight for next month:** [What to do differently]

---

*Claude updates this file automatically after:*
- *Generating a campaign brief*
- *Evaluating ChatGPT output*
- *Shipping production content*
*Denis updates manually when external results come in (open rates, conversions, etc.)*
