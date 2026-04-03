# Exit Rules: 5-Level Gate System

No document ships without passing ALL 5 gates. Each gate is a hard stop.

---

## Gate Architecture

```
Level 1: Validation (Input Check)
    ↓ (PASS → continue, FAIL → return to builder)
Level 2: Structure (Template Compliance)
    ↓ (PASS → continue, FAIL → fix structure)
Level 3: Content (Quality Standards)
    ↓ (PASS → continue, FAIL → rewrite)
Level 4: Quality (Human + AI + Token Check)
    ↓ (PASS → continue, FAIL → optimize)
Level 5: Shipping (Final Approval)
    ↓
📦 PRODUCTION
```

Each gate has:
- Exit criteria (what must be true)
- Failure reason (why it failed)
- Recovery action (how to fix)
- Owner (who approves)

---

## Gate Level 1: Validation (Input Check)

**Purpose:** Verify builder collected necessary information before generating.

**Exit Criteria (ALL must be true):**
- [ ] Frontmatter has all 8 required fields
- [ ] YAML is valid (no syntax errors)
- [ ] doc_type is valid — one of: `project-setup`, `claude-md`, `project-instructions`, `system-guide`, `how-to`, `reference`, `feature`, `process`, `update`, `setup-guide`, `api-guide`, `architecture`, `adr`, `troubleshooting`, `config-reference`, `schema-reference`, `command-reference`
- [ ] domain is valid — one of: `claude-project`, `ai-docs`, `code`, `reference` (see `config/domain_definitions.json`)
- [ ] audience is valid (beginner, intermediate, advanced, or all)
- [ ] difficulty is valid (easy, medium, or hard)
- [ ] status is valid (production, draft, or review)
- [ ] title exists and starts with action verb
- [ ] overview is provided and exactly 2 sentences
- [ ] builder_session_id is unique (no duplicate generation)

**What Fails This Gate:**
- Missing frontmatter
- Invalid YAML syntax
- Unknown doc_type
- Unclear audience level
- Title doesn't answer "what/why"
- No overview provided

**Recovery Action:**
1. Return to builder questionnaire
2. Re-run builder questions
3. Generate new doc
4. Re-run Gate 1

**Owner:** Automated validation (Claude or system script)

**Example Pass:**
```yaml
---
doc_type: project-setup
domain: claude-project
builder_version: v1.1
generated_by: claude-project_builder
generated_at: 2026-04-03T10:00:00Z
builder_session_id: sess_abc123def456
audience: intermediate
difficulty: medium
time_estimate: "1-hour"
prerequisites: [claude-account, idea-description]
status: production
version: 1.0
quality_score: 0
exit_gates_passed: []
---

# How to Set Up a Claude Project from an Idea

Generate all required Claude project files (CLAUDE.md, project instructions, system guides) from a single idea description.
This ensures your Claude project has production-quality instructions, knowledge base structure, and quality gates from day one.
```

**Example Fail:**
```yaml
---
doc_type: unknown_type          # ❌ INVALID — not in approved list
audience: all skill levels      # ❌ INVALID — not in enum
---

# Claude Project                # ❌ No action verb
This document is about Claude projects in general.
It covers how to use Claude.
```

---

## Gate Level 2: Structure (Template Compliance)

**Purpose:** Verify doc follows DOC_CANONICAL_TEMPLATE structure.

**Exit Criteria (ALL must be true):**
- [ ] Section 1: Title + Overview (exists, 2 sentences, keywords defined)
- [ ] Section 2: Prerequisites (if applicable, uses Level 1-4, no vague items)
- [ ] Section 3: Content (appropriate for doc_type, organized logically)
- [ ] Section 4: Expected Output (table with commands, not prose)
- [ ] Section 5: Troubleshooting (if errors mentioned, each has signature)
- [ ] Section 6: Why This Matters (if relevant, explains rationale)
- [ ] Section 7: What's Next (references other docs by title, includes conditions)
- [ ] No forbidden sections (no "Best Practices", no generic disclaimers)
- [ ] AI metadata blocks in all steps/errors
- [ ] Preconditions/postconditions defined for all steps

**What Fails This Gate:**
- Missing required sections
- Expected Output in prose instead of table
- Troubleshooting errors without signatures
- "See above" instead of doc title references
- Missing AI metadata blocks
- Vague prerequisites ("be comfortable with...")
- No success indicator

**Recovery Action:**
1. Identify failed sections
2. Rewrite using DOC_CANONICAL_TEMPLATE
3. Add missing AI metadata blocks
4. Convert prose Expected Output to table
5. Re-run Gate 2

**Owner:** Automated structure check (can be done via regex or Claude)

**Example Pass:**
```markdown
## What Success Looks Like

| Check | Expected | Command |
|-------|----------|---------|
| Files created | 5 new files in project root | `ls -la \| grep -E "\.md$" \| wc -l` |
| Config valid | No errors when parsed | `yaml -c ./.docgen.yaml` |
```

**Example Fail:**
```markdown
## Expected Outcome

After completing the setup, you should see files in your project.
Everything should be working correctly without errors.
Try running the validation script to make sure.

## Common Issues

If you get an error, check the logs.
Make sure all prerequisites are installed.
```

---

## Gate Level 3: Content (Quality Standards)

**Purpose:** Verify content quality, accuracy, completeness.

**Exit Criteria (ALL must be true):**
- [ ] Overview explains what AND why (not just what)
- [ ] All commands are exact and testable (not "install X")
- [ ] Expected output shown after each step
- [ ] Every error has Root cause + Fix steps
- [ ] Prerequisites are realistic (don't ask for unreasonable knowledge)
- [ ] All external links go directly to download/resource (not homepage)
- [ ] All cross-references use doc titles (not URLs)
- [ ] No acronyms without first definition
- [ ] No ambiguous pronouns ("it", "this", "that" without clear referent)
- [ ] Tone consistent throughout
- [ ] No contradictions between sections
- [ ] **All code blocks pass SYSTEM_Coding_Standards.md checklist:** language tag present, expected output shown, no hardcoded secrets, imports present, dependencies version-pinned, within line-count limits, model strings are current

**What Fails This Gate:**
- Steps are descriptions not commands ("Install the library" vs. `npm install x`)
- No expected output shown
- Errors listed without root causes
- Prerequisites too demanding ("Expert knowledge of Kubernetes")
- Broken external links
- Vague references ("See above")
- Unexplained acronyms
- Inconsistent advice

**Recovery Action:**
1. For each failure, rewrite that section
2. Make commands exact and testable
3. Add expected output
4. Explain error causes
5. Make prerequisites realistic
6. Fix all links and references
7. Define all acronyms
8. Re-run Gate 3

**Owner:** Human review or Claude quality check

**Example Pass:**
```markdown
### Step 1: Install Node.js 16

1. Go to: https://nodejs.org/en/download/ (select LTS v16+)
2. Download the installer for your OS
3. Run the installer, accept defaults
4. Restart terminal (close and reopen)
5. Verify: `node --version` (should show v16.0.0+)

Expected: Terminal shows version number like "v16.13.0"

**AI metadata:**
- Precondition: Administrative access to computer
- Postcondition: Node.js 16+ installed and in PATH
```

**Example Fail:**
```markdown
### Step 1: Set up Node

Install Node.js on your computer. Make sure you get the right version.
Then configure it properly so it works with your project.

**AI metadata:**
- Precondition: You have a computer
- Postcondition: Node is installed
```

---

## Gate Level 4: Quality (Human + AI + Token Check)

**Purpose:** Verify doc passes human quality, AI parsing, and token efficiency.

**Exit Criteria (ALL must be true):**

### Human Quality Check (from Documentation_Content_Guide.md)
- [ ] Content serves clear purpose (passes "why this section?" test)
- [ ] Beginner can follow without external help
- [ ] All steps are actionable (not theoretical)
- [ ] Expected output is specific (not vague)
- [ ] Troubleshooting is organized by symptom, not cause

### AI Quality Check (from AI_First_Documentation_Format.md)
- [ ] Frontmatter extracts correctly (test: Can Claude read it?)
- [ ] Prerequisites are parseable (Levels 1-4 consistent)
- [ ] Steps have preconditions/postconditions (machine readable)
- [ ] Error signatures are exact (copy-paste from actual error output)
- [ ] All links in metadata, not prose
- [ ] Success table has runnable commands
- [ ] Related docs are discoverable from frontmatter

### Token Efficiency Check (see token_budgets.json)
- [ ] Doc token count ≤ domain budget
- [ ] Prose sections are ≤ 4 paragraphs
- [ ] Every section serves purpose (no fluff)
- [ ] Examples are concise but complete
- [ ] Errors: Only top 3-5 included (rest in DEBT.md)

**What Fails This Gate:**
- Human: Beginner can't follow steps
- AI: Claude can't extract prerequisites from metadata
- Token: Setup guide is 8K tokens (budget is 3K)
- Quality score < 85
- Any exit gate criteria unchecked

**Recovery Action:**
1. **Human issues:** Rewrite for clarity, test with user
2. **AI issues:** Fix metadata blocks, ensure parseable structure
3. **Token issues:** Remove non-essential sections, move to DEBT.md
4. **Quality score:** Address low-scoring sections
5. Run all three checks again

**Owner:** Automated checks + human review (if quality_score < 85)

**Token Check Example:**

```json
{
  "doc_type": "how-to",
  "domain": "ai-docs",
  "budget_tokens": 2200,
  "actual_tokens": 2050,
  "token_ratio": 0.93,
  "status": "PASS"
}
```

```json
{
  "doc_type": "project-setup",
  "domain": "claude-project",
  "budget_tokens": 5000,
  "actual_tokens": 8400,
  "token_ratio": 1.68,
  "status": "FAIL - exceeds budget by 68%. Reduce by 3400 tokens or split into 2 docs."
}
```

---

## Gate Level 5: Shipping (Final Approval)

**Purpose:** Final sign-off before doc goes to production.

**Exit Criteria (ALL must be true):**
- [ ] Gate 1 PASSED: Validation
- [ ] Gate 2 PASSED: Structure
- [ ] Gate 3 PASSED: Content Quality
- [ ] Gate 4 PASSED: Human + AI + Token Quality
- [ ] DEBT.md created with known limitations
- [ ] metadata.json complete with quality_score, exit_gates_passed
- [ ] Version number assigned (v1.0, v1.1, etc.)
- [ ] Status set to "production" (not draft/review)
- [ ] Related docs checked (exist and correct)
- [ ] Skill suggestion reviewed (published, suggested, or declined)
- [ ] Doc added to appropriate project knowledge base
- [ ] Generation logged in metrics/generation_log.md

**What Fails This Gate:**
- Any earlier gate failed
- DEBT.md missing or incomplete
- metadata.json incomplete
- Status still "draft" or "review"
- Related docs don't exist
- No entry in generation log

**Recovery Action:**
1. Return to failing gate
2. Fix all issues
3. Re-run Gates 1-4
4. Create DEBT.md
5. Generate metadata.json
6. Update status to "production"
7. Add to metrics log
8. Re-run Gate 5

**Owner:** Project owner or team lead (not automated)

**Final Checklist:**
```markdown
## Shipping Checklist

### Gate Status
- [✅] Gate 1: Validation PASSED
- [✅] Gate 2: Structure PASSED
- [✅] Gate 3: Content Quality PASSED
- [✅] Gate 4: Human + AI + Token Quality PASSED

### Production Readiness
- [✅] DEBT.md exists with all known issues
- [✅] metadata.json has quality_score >= 85
- [✅] All exit_gates_passed: [1,2,3,4,5]
- [✅] Status: production
- [✅] Version: v1.0

### Documentation
- [✅] Related docs exist and are current
- [✅] Skill suggestion reviewed (status: published/suggested/declined)
- [✅] Doc added to project knowledge base
- [✅] Generation logged in metrics/generation_log.md

### Sign-Off
- Reviewed by: [name]
- Date: YYYY-MM-DD
- Approved for shipping: YES ✅
```

---

## Gate Failure Recovery Matrix

| Gate | Failure | Time to Fix | Recovery | Escalation |
|------|---------|------------|----------|------------|
| 1 | Invalid frontmatter | 5 min | Re-run builder | Builder has bug |
| 2 | Missing sections | 15 min | Add sections manually | Template unclear |
| 3 | Vague instructions | 30 min | Rewrite with examples | Builder needs improvement |
| 4 | Token bloat | 20 min | Remove non-essentials, move to DEBT | Domain budget too tight |
| 5 | Missing DEBT.md | 10 min | Generate from builder feedback | Builder output incomplete |

---

## Gate Performance Metrics

Track for continuous improvement:

```json
{
  "gates_performance": {
    "gate_1_validation": {
      "total_documents": 450,
      "pass_rate": 0.98,
      "common_failures": ["invalid_doc_type", "missing_audience"],
      "avg_time_to_fix_minutes": 3
    },
    "gate_2_structure": {
      "total_documents": 441,
      "pass_rate": 0.94,
      "common_failures": ["missing_metadata_blocks", "prose_expected_output"],
      "avg_time_to_fix_minutes": 12
    },
    "gate_3_content": {
      "total_documents": 415,
      "pass_rate": 0.88,
      "common_failures": ["vague_steps", "no_expected_output", "broken_links"],
      "avg_time_to_fix_minutes": 28
    },
    "gate_4_quality": {
      "total_documents": 366,
      "pass_rate": 0.92,
      "common_failures": ["token_budget_exceeded", "quality_score_low"],
      "avg_time_to_fix_minutes": 22
    },
    "gate_5_shipping": {
      "total_documents": 336,
      "pass_rate": 0.99,
      "common_failures": ["missing_debt_md", "related_docs_broken"],
      "avg_time_to_fix_minutes": 8
    }
  }
}
```

---

## No Doc Ships Without All 5 Gates Passing

This is non-negotiable. A doc that:
- Passes Gates 1-4 but fails Gate 5 → stays in draft
- Passes Gate 4 but fails Gate 3 → goes back to rewriting
- Fails ANY gate → cannot be marked "production"

**Status meanings:**
- **draft:** Failed at least one gate, still being fixed
- **review:** Passed all gates, awaiting final approval (Gate 5)
- **production:** All 5 gates PASSED, shipping to users
- **deprecated:** Was production, now archived

Only "production" docs are visible to users in projects/output.
