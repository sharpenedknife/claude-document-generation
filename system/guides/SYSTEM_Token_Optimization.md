# Token Optimization: Quality Per Token

Docs must be high-quality AND efficient. This defines token budgets and optimization rules.

---

## Generation Behavioral Rules

These rules apply **during writing**, not at review. Internalize before writing the first word of any doc.

### Rule 1 — BLUF: Conclusion First

State the conclusion or key fact in the first sentence of every section. Explanation follows. Never warm up to a point.

```
❌  "There are several approaches to consider when designing authentication..."
✅  "Use JWT with refresh tokens. Store refresh tokens in httpOnly cookies."
```

### Rule 2 — Tables Over Paragraphs

Any comparison, list of options, or structured data (fields, endpoints, errors) goes in a table. Prose explanations of structured data are always more tokens than equivalent tables.

```
❌  "The User entity has an id field which is a UUID, a name field which is a string..."
✅  | Field | Type | Required | Default |
    |-------|------|----------|---------|
    | id    | UUID | yes      | gen()   |
```

### Rule 3 — No Cross-Doc Repetition

In a multi-doc bundle, each doc owns one topic. Never restate context from another doc — reference it by filename.

```
❌  "As defined earlier, the User entity has the following fields: id (UUID)..."
✅  "User entity fields: see DATA_Schema.md § User"
```

### Rule 4 — Section Body Cap: 120 Words

Each prose section body is capped at 120 words (~160 tokens). If more detail is needed, split into a sub-section or move to a separate doc. Exception: code blocks don't count toward the word cap.

### Rule 5 — Decision Records: 3 Lines Max

Every CONFIRMED/ASSUMED decision record in the Assumption Register:
- Line 1: Decision + status (CONFIRMED/ASSUMED)
- Line 2: Rationale (one clause)
- Line 3: Impact if wrong (one clause)

No prose narrative around decision records.

### Rule 6 — Acceptance Criteria: GIVEN/WHEN/THEN Only

```
❌  "The login feature should work correctly and handle errors appropriately."
✅  GIVEN: valid credentials WHEN: POST /auth/login THEN: 200 + JWT returned
```

One line per criterion. No prose explanation of what the criterion means.

### Rule 7 — Code Blocks: Minimal But Runnable

Show the exact command or minimal working example. No defensive boilerplate (try/catch, logging, comments) unless error handling is the point of the example.

```
❌  // Full example with error handling, logging, and edge cases
    async function createUser(data) {
      try { ... } catch (e) { logger.error(e); throw e; }
    }

✅  await db.user.create({ data })
```

### Rule 8 — Never Pad to Fill Budget

Token budget = ceiling, not target. A 1,200-token PRD that passes all gates is better than a 2,500-token PRD. Quality score does not increase by using more tokens.

---

## Core Principle

**Quality per token** = quality_score ÷ token_count

A 100-point doc in 2K tokens is better than the same 100-point doc in 4K tokens.

**Target:** 0.03+ quality points per token (85 quality score ÷ 2500 tokens = 0.034)

---

## Token Budgets by Doc Type

All budgets are HARD LIMITS. Exceeding by >10% = Gate 4 FAIL.

**Source of truth:** `config/token_budgets.json` — always check that file for current budgets and rationale. Do not duplicate budget values here.

**Quick reference:** Budgets range from 1,200 tokens (project-instructions) to 3,500 tokens (architecture). The `note` field in each budget entry explains the rationale. When in doubt, open `config/token_budgets.json`.

---

## How to Stay Within Budget

### 1. Prerequisites: Max 800 tokens

```markdown
## Prerequisites

### Level 1: Tools & Software
- **Tool Name** (required)
  - Check: [command]
  - Install: [link]
  - Why: [one sentence]

### Level 2-4
[Continue as needed]

**Ready?** [verification command]
```

**Optimization:**
- Don't repeat install links (reference once, then "see link above")
- Combine similar items ("Node + npm" not "Node (600 tokens) then npm (400 tokens)")
- Level 3 (Knowledge) = one line each
- Level 4 (State) = one line each

**Token counts:**
- Simple setup: 150-250 tokens
- Medium setup: 300-500 tokens
- Complex setup: 600-800 tokens (near limit)

### 2. Steps: Max 50 tokens per step

Each step should be:
```markdown
### Step N: [Action]

1. Run: [command]
   Expected: [output]
   
   **AI metadata:** [2-3 lines max]
```

**Token estimate per step:**
- Simple (command + expected): 30-40 tokens
- Medium (command + expected + error reference): 40-60 tokens
- Complex (command + expected + metadata + reference): 60-80 tokens

**If step exceeds 80 tokens:** Split into two steps.

### 3. Troubleshooting: Max 60 tokens per error

```markdown
### Error: "[signature]"

**Root cause:** [one sentence]

**Fix:**
1. [Step 1]
2. [Step 2]
3. [Verify]

**AI metadata:** [one line max]
```

**Token estimate:**
- Simple error: 30-40 tokens
- Medium error: 40-60 tokens (limit)
- Complex error: 70-100 tokens (move to DEBT.md)

**Rules:**
- Max 5 errors per doc
- If more needed: Add to DEBT.md as "Add X, Y, Z error handling"

### 4. Content Sections: Max 4 paragraphs = ~400 tokens

Each section (Why This Matters, Overview subsection, etc.):
```markdown
## Section Title

[Paragraph 1: Main point - ~80 tokens]
[Paragraph 2: Detail/support - ~80 tokens]
[Paragraph 3: Application - ~80 tokens]
[Paragraph 4: Context - ~80 tokens MAX]
```

**If content exceeds 400 tokens:** Break into multiple sections or move to separate doc.

### 5. Examples: Max 30% of doc tokens

If doc is 2500 tokens:
- Code examples: max 750 tokens total
- Reference tables: max 500 tokens total
- Illustrations (described): max 300 tokens total

**Example optimization:**
```markdown
❌ BAD (500 tokens):
"Here's a complete example with full error handling,
logging, edge cases, authentication flow..."

✅ GOOD (150 tokens):
```bash
curl -X GET https://api.example.com/users
```

Response: `{"users": [...]}`

[Link to: Complete example with error handling in appendix]
```

---

## Token Optimization Checklist

Before Gate 4, run this:

### Prose Sections
- [ ] Overview: 2 sentences, no filler
- [ ] Why This Matters: 3-5 bullets, not paragraphs
- [ ] What's Next: 3 options max, 1-2 sentences each
- [ ] Sections: ≤ 4 paragraphs each
- [ ] Examples: Simplified, reference full example in doc

### Step-by-Step
- [ ] Prerequisites: 200-800 tokens (not 1500)
- [ ] Each step: 30-60 tokens (not 100+)
- [ ] Errors: 5 max, 60 tokens each (move rest to DEBT)
- [ ] Metadata blocks: 3-5 lines, not 10+

### Structure
- [ ] No redundancy (same info in two places = remove one)
- [ ] No theoretical explanation (link to why instead)
- [ ] No "nice to know" (move to DEBT.md as "P3: Add X")
- [ ] No generic disclaimers ("Please note...", "It's important...")

### Cuts to Make
- [ ] "For more information, see..." → Replace with specific link
- [ ] "There are many ways..." → Show the one best way
- [ ] "You might want to consider..." → "Do X because Y"
- [ ] Generic intro/conclusion → Remove entirely
- [ ] Duplicate concepts → Consolidate into one section

---

## Quality Score Calculation

**Quality Score = (factors) → 0-100**

```
Base score: 50

+ 10: Passes human quality checklist (all items true)
+ 10: Passes AI quality checklist (all items true)
+ 10: Passes token efficiency (within budget, no fluff)
+ 10: Clear expected output (testable, specific)
+ 10: All steps/errors have AI metadata
+ 5:  All cross-references use doc titles
+ 5:  All external links verified working
+ 5:  Error signatures verified exact
+ 5:  Related docs exist and relevant
+ 5:  No vague language detected

Minus points:
- 5: Each vague phrase ("proper", "configure", "ensure")
- 3: Each broken link
- 5: Each unclear error signature
- 10: Exceeds token budget
- 10: Missing critical section (Expected Output, etc.)

Final: (Base + additions - subtractions) / 100 = Quality Score
```

**Example:**
```
Setup guide:
Base:                        50
+ Human quality:             10
+ AI quality:                10
+ Token efficiency:          10
+ Clear expected output:     10
+ AI metadata blocks:        10
+ Doc title references:      5
+ Working links:             5
+ Verified error signatures: 5
+ Related docs exist:        5
+ No vague language:         5

Subtractions:
- 1 broken link:             -3
- 1 missing error signature: -5

Total: 117 / 100 = 1.00 = 100 (capped at 100)
Quality Score: 92 (after manual adjustments for edge cases)
```

---

## Token Budget Exceptions

**When can you exceed budget?**

Only if:
1. Quality score would drop below 80 if you cut more
2. Exceeding is < 10% over budget (2500 budget + 250 overage = OK)
3. Overage justified in DEBT.md under "Content Decisions"

**Example:**
```markdown
## DEBT.md - Content Decisions

### Budget Overage (Item P0)
- Token budget: 2500
- Actual: 2680
- Overage: 180 tokens (7%)
- Reason: 3 error signatures essential for user success (not optional)
- Future: Refactor examples to reduce by 150 tokens
```

**If exceeding > 10%:** NOT APPROVED. Cut content, move to DEBT.md, or split into two docs.

---

## Token Tracking Template

Every doc must include this in metadata.json:

```json
{
  "token_budget": 2500,
  "token_count": 2347,
  "token_ratio": 0.94,
  "budget_status": "PASS",
  
  "token_breakdown": {
    "frontmatter": 45,
    "overview_section": 120,
    "prerequisites": 420,
    "content_sections": 980,
    "steps": 420,
    "troubleshooting": 240,
    "ai_metadata_blocks": 60,
    "examples": 200,
    "other": 42
  },
  
  "optimization_notes": [
    "Removed 300-token theoretical explanation section",
    "Consolidated 3 similar prerequisites into 1",
    "Moved advanced examples to separate doc (DEBT.md item)"
  ],
  
  "quality_score": 92,
  "quality_calculation": {
    "base": 50,
    "human_checklist": 10,
    "ai_checklist": 10,
    "token_efficiency": 10,
    "expected_output": 10,
    "metadata_blocks": 10,
    "doc_title_refs": 5,
    "working_links": 5,
    "error_signatures": 5,
    "related_docs": 5,
    "no_vague_language": 5,
    "penalties": -8,
    "final": 92
  }
}
```

---

## Benchmarks: Quality Per Token

**Excellent (0.035+):**
- 87 quality score ÷ 2500 tokens = 0.0348 ✅

**Good (0.030-0.035):**
- 85 quality score ÷ 2800 tokens = 0.0304 ✅

**Acceptable (0.025-0.030):**
- 80 quality score ÷ 3200 tokens = 0.0250 ⚠️

**Poor (< 0.025):**
- 82 quality score ÷ 3500 tokens = 0.0234 ❌
- Action: Cut tokens or improve quality

---

## Monthly Token Audit

Every month, analyze:

```markdown
## Monthly Token Report

### Metrics
- Total docs generated: X
- Avg tokens per doc: Y
- Avg quality score: Z
- Quality/token ratio: Q/T

### Trends
- Docs exceeding budget: N (%) [target: < 5%]
- Quality scores below 85: N (%) [target: < 10%]
- Token bloat areas: [section types averaging above budget]
- Quality issues: [recurring Gate 3-4 failures]

### Adjustments for Next Month
- Reduce budget for [domain]? (avg: 3200, budget: 2500)
- Improve quality for [domain]? (avg score: 78)
- Split [doc_type] into two? (avg tokens: 4100)
```

This tracking prevents budget creep and quality drift.
