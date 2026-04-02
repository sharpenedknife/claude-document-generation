# DEBT.md Specification

Every document MUST have an accompanying DEBT.md file listing known limitations, backlog features, and future improvements.

DEBT.md is NOT for users. It's for the docgen team tracking what's incomplete.

---

## File Naming

```
{DocName}.md          # Main document
{DocName}.DEBT.md     # Companion debt file
```

**Examples:**
```
GTM_Strategy_2026Q1.md
GTM_Strategy_2026Q1.DEBT.md

API_Reference_v1.md
API_Reference_v1.DEBT.md
```

---

## Frontmatter

```yaml
---
for_document: "{DocName}.md"
generated_at: YYYY-MM-DDTHH:MM:SSZ
total_items: N
critical_items: N (P0)
high_priority_items: N (P1)
medium_priority_items: N (P2)
low_priority_items: N (P3)
---
```

---

## Structure

```markdown
# Technical Debt: {DocName}

For document: [{DocName}]({path_to_doc}.md)

---

## Overview

Brief explanation of why this document has debt:
- What's complete now
- What's deferred
- What was cut for token budget
- Known gaps or limitations

---

## Priority 0: Critical (Blocks Production)

**Status:** None (document wouldn't ship if any P0 items exist)

---

## Priority 1: High (Should Address Soon)

### Item 1.1: [Title]
- **Type:** [missing_section|incomplete|unclear|needs_verification|needs_examples]
- **Impact:** [What breaks without this]
- **Effort:** [1-3 hours|4-8 hours|1-3 days|> 1 week]
- **Owner:** [Who should fix]
- **Details:** [Why it's incomplete, what's needed]

Example:
```markdown
### Item 1.1: Add Competitive Analysis Table
- **Type:** missing_section
- **Impact:** GTM strategy incomplete without knowing competitive landscape
- **Effort:** 4-8 hours
- **Owner:** Product team
- **Details:** Need to research 5 main competitors (Slack, Microsoft Teams, Google Chat)
  and create comparison table. Should include: feature matrix, pricing, target market.
```

---

## Priority 2: Medium (Nice to Have)

### Item 2.1: [Title]
- **Type:** [enhancement|optimization|clarification|additional_example]
- **Impact:** [Helpful but not blocking]
- **Effort:** [estimate]
- **Owner:** [suggestion]
- **Details:** [Description]

Example:
```markdown
### Item 2.1: Add Pricing Tier Breakdown
- **Type:** enhancement
- **Impact:** Users can't estimate costs without pricing details
- **Effort:** 2-3 hours
- **Owner:** Sales/Finance team
- **Details:** Add table breaking down: basic/pro/enterprise pricing
  and what's included in each tier. Include annual discount rates.
```

---

## Priority 3: Low (Future Backlog)

### Item 3.1: [Title]
- **Type:** [nice_to_have|future_feature|research|depends_on_something]
- **Impact:** [Would be nice, not essential]
- **Effort:** [estimate]
- **Owner:** [suggestion]
- **Details:** [Description]

Example:
```markdown
### Item 3.1: Add Case Studies
- **Type:** future_feature
- **Impact:** Would strengthen credibility, not needed for MVP
- **Effort:** 3-5 days
- **Owner:** Marketing
- **Details:** Research and write 2-3 case studies showing GTM success stories
  from our customers. Depends on customer approval + interview time.

### Item 3.2: Add Video Walkthrough
- **Type:** future_feature
- **Impact:** Video format would help some learners, doc is readable without
- **Effort:** 1-2 days
- **Owner:** Content team
- **Details:** Record 15-20 minute walkthrough of GTM strategy execution.
  Needs: scripting, recording, editing.
```

---

## Known Limitations

```markdown
## Known Limitations

### Limitation 1: [What's Limited]
- **Scope:** [What won't work]
- **Reason:** [Why it's limited]
- **Workaround:** [How users should work around it, if any]

Example:
### Limitation 1: Does Not Cover Enterprise Sales
- **Scope:** GTM strategy assumes mid-market (50-500 employees), not enterprise (1000+)
- **Reason:** Enterprise GTM requires 2x longer sales cycle, different decision trees
- **Workaround:** See: [link to separate enterprise GTM doc]

### Limitation 2: Data as of Q1 2026
- **Scope:** Market analysis, competitor pricing, market size estimates
- **Reason:** Markets change quarterly, this doc was current Feb-Mar 2026
- **Workaround:** Check quarterly updates in [link to update schedule]
```

---

## Skills to Create (If Applicable)

```markdown
## Suggested Skills

If patterns emerge, suggest creating reusable skills:

### Skill 1: [Skill Name]
- **Type:** repeatable_process
- **Usage:** When user needs to [what problem does skill solve]
- **Scope:** [What the skill would cover]
- **Status:** [suggested|in_progress|published]
- **Owner:** [Who should build]

Example:
### Skill 1: Market Analysis Framework
- **Type:** repeatable_process
- **Usage:** When creating GTM strategy for any new market segment
- **Scope:** Step-by-step process for analyzing market size, growth, competition, buyer personas
- **Status:** suggested
- **Owner:** Product/Research team
```

---

## Content Decisions

```markdown
## Content Decisions

Document why certain content was cut, deferred, or simplified:

### Decision 1: [What Was Cut/Deferred]
- **Original Plan:** [What was supposed to be included]
- **Actual:** [What's in the doc]
- **Reason:** [Token budget|Quality over quantity|Out of scope|Dependency not ready]
- **Impact:** [What users can't do without this]
- **When to Revisit:** [Condition for adding it back]

Example:
### Decision 1: Simplified Pricing Analysis
- **Original Plan:** Detailed price elasticity analysis, customer lifetime value calcs
- **Actual:** Simple pricing tier comparison table
- **Reason:** Token budget (would have added 800+ tokens)
- **Impact:** Users can't optimize pricing strategy without elasticity data
- **When to Revisit:** After GTM v1.0 ships, create separate "Advanced Pricing Strategy" doc
```

---

## Dependencies

```markdown
## Dependencies

Items that depend on other work being done first:

### Dependency 1: [What's Blocked]
- **Blocks:** [What item(s) depend on this]
- **Waiting For:** [What needs to happen first]
- **Owner:** [Who controls the dependency]
- **Expected Date:** [When will it be ready]

Example:
### Dependency 1: Customer Interview Data
- **Blocks:** Item 1.1 (Add Competitive Analysis - need ICP validation)
- **Waiting For:** Sales team to complete 10 customer discovery interviews
- **Owner:** Sales team
- **Expected Date:** End of Q2 2026
```

---

## Verification Needed

```markdown
## Items Needing Verification

Content that should be verified before finalizing:

### Verification 1: [What Needs Verification]
- **Current Status:** [What's in the doc now]
- **Who Should Verify:** [Department/person]
- **How to Verify:** [Process or test]
- **Blocker?:** [Yes|No]

Example:
### Verification 1: Competitive Pricing Data
- **Current Status:** Pricing from public websites + Q1 2026 reports
- **Who Should Verify:** Sales team (they talk to prospects)
- **How to Verify:** 5-customer feedback survey on pricing accuracy
- **Blocker?:** No (can ship with caveat "verify with your sales team")

### Verification 2: Market Size Numbers
- **Current Status:** From Gartner report Q1 2026
- **Who Should Verify:** Research/Analytics team
- **How to Verify:** Cross-check against 2-3 other research firms
- **Blocker?:** Yes (market size is foundational)
```

---

## Changelog

Track why this DEBT.md exists and how it's evolving:

```markdown
## Changelog

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-02 | Created initial DEBT.md | Document shipped, P1 items deferred for v1.1 |
| 2026-04-10 | Moved Item 1.2 from P2→P1 | Sales team flagged competitive analysis as urgent |
| 2026-05-01 | Closed Item 2.1 | Pricing breakdown added in v1.1 update |
| 2026-05-15 | Added Dependency 1 | Waiting for customer data from interviews |
```

---

## DEBT.md Quality Checklist

Every DEBT.md must have:

- [ ] Frontmatter with total_items count
- [ ] Overview explaining why doc has debt
- [ ] P0 section (should be empty if doc shipped)
- [ ] P1+ items with Type, Impact, Effort, Owner, Details
- [ ] Known Limitations section
- [ ] Content Decisions explaining what was cut and why
- [ ] Dependencies listed with owners + expected dates
- [ ] Verification items with process for checking
- [ ] Changelog showing evolution
- [ ] Total items counts match (frontmatter = actual items)

---

## Template to Copy

```markdown
---
for_document: "{DocName}.md"
generated_at: YYYY-MM-DDTHH:MM:SSZ
total_items: 8
critical_items: 0
high_priority_items: 3
medium_priority_items: 3
low_priority_items: 2
---

# Technical Debt: {DocName}

For document: [{DocName}]({path}).md

---

## Overview

[Why this document has debt - what's done, what's deferred]

---

## Priority 0: Critical (Blocks Production)

None. Document is production-ready.

---

## Priority 1: High (Should Address Soon)

### Item 1.1: [Title]
- **Type:** [type]
- **Impact:** [impact]
- **Effort:** [estimate]
- **Owner:** [owner]
- **Details:** [description]

---

## Priority 2: Medium (Nice to Have)

### Item 2.1: [Title]
- **Type:** [type]
- **Impact:** [impact]
- **Effort:** [estimate]
- **Owner:** [owner]
- **Details:** [description]

---

## Priority 3: Low (Future Backlog)

### Item 3.1: [Title]
- **Type:** [type]
- **Impact:** [impact]
- **Effort:** [estimate]
- **Owner:** [owner]
- **Details:** [description]

---

## Known Limitations

### Limitation 1: [What's Limited]
- **Scope:** [What won't work]
- **Reason:** [Why]
- **Workaround:** [If any]

---

## Content Decisions

### Decision 1: [What Was Cut]
- **Original Plan:** [Plan]
- **Actual:** [What's in doc]
- **Reason:** [Why deferred]
- **Impact:** [What users lose]
- **When to Revisit:** [Condition]

---

## Dependencies

### Dependency 1: [What's Blocked]
- **Blocks:** [Items affected]
- **Waiting For:** [What's needed]
- **Owner:** [Who controls it]
- **Expected Date:** [When ready]

---

## Verification Needed

### Verification 1: [What Needs Check]
- **Current Status:** [What's there now]
- **Who Should Verify:** [Department]
- **How to Verify:** [Process]
- **Blocker?:** [Yes|No]

---

## Changelog

| Date | Change | Reason |
|------|--------|--------|
| YYYY-MM-DD | [Initial creation] | Document shipped |

---

**This DEBT.md is living. Update as items are closed or new debt discovered.**
```

---

## Automation: Auto-Generate DEBT.md

Builder should auto-create DEBT.md with:

1. **P0 items:** None (if doc ships)
2. **P1-P3 items:** Items user mentioned during builder questionnaire
3. **Known Limitations:** From builder's domain knowledge
4. **Content Decisions:** Cuts made for token budget
5. **Dependencies:** Flagged from prerequisites or cross-doc links

**Then human adds:**
- Specific effort estimates
- Owner assignments
- Verification processes
- Detailed descriptions

Final DEBT.md is human-reviewed before doc ships.
