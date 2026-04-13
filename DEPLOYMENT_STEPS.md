# Deployment Steps — Apply Hardened Rules to Claude.ai
**Version:** 1.0 · April 2026
**Time to implement:** ~15 minutes

---

## Overview

You have 3 new files that enforce hard rules:
1. **CLAUDE_HARDENED.md** — Replace the soft CLAUDE.md
2. **PROJECT_INSTRUCTIONS_HARDENED.md** — Paste into Claude.ai Project Settings
3. **HARDENING_GUIDE.md** — Reference for hardening other docs

This guide shows how to deploy them and verify they work.

---

## Step 1: Backup Current Files

Before making changes, save your current setup:

```
Current files (keep as backup):
- CLAUDE.md (original, soft version)
- PROJECT_INSTRUCTIONS_Docgen_Production.md (original)
```

You won't delete these. You'll version them as v2.x and replace with v3.0 (hardened).

---

## Step 2: Replace CLAUDE.md

In your workspace folder (wherever the project lives):

### Action
1. Rename current: `CLAUDE.md` → `CLAUDE_v2.5_SOFT.md` (backup)
2. Copy contents of `CLAUDE_HARDENED.md` → new `CLAUDE.md`
3. Verify file exists: `/Documentation/CLAUDE.md`

### Verification
Open CLAUDE.md and verify these lines appear:
```
## CARDINAL RULE — ALWAYS SHOW MENU FIRST
Your very first response in **every new conversation** MUST display the navigation menu below. No exceptions.
```

---

## Step 3: Update Claude.ai Project Settings

Go to **claude.ai → Your Project → Settings → Custom Instructions**

### Action
1. Delete current custom instructions (save a copy first if you want)
2. Copy the ENTIRE contents of `PROJECT_INSTRUCTIONS_HARDENED.md`
3. Paste into the Custom Instructions field
4. Click Save

### Verification
Start a new conversation in the project. Your very first response should be the navigation menu with no preamble.

---

## Step 4: Update REFERENCE Files (Medium Priority)

If you have REFERENCE_System.md and REFERENCE_Builders.md, harden them using the patterns in HARDENING_GUIDE.md:

### Priority 1 (Critical)
Search and replace in REFERENCE_System.md and REFERENCE_Builders.md:
```
Old pattern              → New pattern
"should"                 → "MUST"
"may use"                → "WILL"
"consider using"         → "USE" (imperative)
"All questions optional" → "Tier 1 is MANDATORY"
"can skip"               → "NO EXCEPTIONS"
```

### Priority 2 (Important)
Add FAIL conditions to every rule. Use HARDENING_GUIDE.md as a template.

### Priority 3 (Polish)
Remove vague success criteria. Replace with explicit thresholds (e.g., "85/100 minimum").

---

## Step 5: Test the Hardened Rules

Start a new conversation in the project and verify:

### Test 1: Menu Appears First
**Action:** Say "hi" in a new project conversation
**Expected:** Navigation menu shows before any greeting

**Result:** ✅ PASS | ❌ FAIL (If fail: verify PROJECT_INSTRUCTIONS updated)

### Test 2: Build Type is Identified Before Context
**Action:** Say "I want to build a SaaS app"
**Expected:** Claude identifies as "Product" and states "I will now collect Tier 1 context"

**Result:** ✅ PASS | ❌ FAIL (If fail: verify CLAUDE.md Gate 1 language)

### Test 3: Tier 1 Context is Required
**Action:** Provide only product name, nothing else
**Expected:** Claude asks "Who uses it?" and "What does it do?" — does NOT generate

**Result:** ✅ PASS | ❌ FAIL (If fail: verify Gate 2 enforcement in CLAUDE.md)

### Test 4: Plan Must Be Confirmed
**Action:** Provide Tier 1 context, then wait
**Expected:** Claude shows generation plan and asks "Does this look right?" — does NOT generate without approval

**Result:** ✅ PASS | ❌ FAIL (If fail: verify Gate 3 language)

### Test 5: Quality Gates Are Enforced
**Action:** Generate a doc (any doc) and check the output
**Expected:** Output includes a quality score at the bottom, marked GATE PASSED or GATE FAILED

**Result:** ✅ PASS | ❌ FAIL (If fail: verify Gate 5 quality framework)

### Test 6: Assumptions Are Marked
**Action:** Generate any doc with uncertain context
**Expected:** Every assumption has [ASSUMED], [INFERRED], or [NEEDS INPUT] tag

**Result:** ✅ PASS | ❌ FAIL (If fail: verify assumption marking in CLAUDE.md Rule 12)

---

## Step 6: If Tests Fail — Troubleshooting

| Test Fails | Likely Cause | Fix |
|---|---|---|
| Menu doesn't show first | PROJECT_INSTRUCTIONS not updated | Re-check Step 3. Verify paste is complete. |
| Build type not identified | CLAUDE.md GATE 1 text not loaded | Verify CLAUDE.md exists in workspace. Check spelling of Gate 1. |
| Tier 1 not enforced | CLAUDE.md GATE 2 text not loaded | Same as above. Verify "GATE 2" exact spelling. |
| Plan not shown | CLAUDE.md GATE 3 not updated | Verify CLAUDE.md has the 6-gate workflow. Check for old "Step 1-6" language. |
| Quality gates missing | CLAUDE.md GATE 5 text not loaded | Verify quality gate section with 5-gate table. |
| Assumptions not marked | CLAUDE.md Rule 12 not loaded | Search CLAUDE.md for "[ASSUMED]" text. Must appear in Rule 12. |

**If still failing after checking:**
1. Clear browser cache (cmd+shift+R or ctrl+shift+R)
2. Reload the project page
3. Start a completely new conversation (not a reply)
4. If still fails: manually copy PROJECT_INSTRUCTIONS_HARDENED.md text again (verify no formatting issues)

---

## Step 7: Harden Remaining Docs (Optional, Lower Priority)

These can be done later, but recommended:

### REFERENCE_System.md
Use patterns from HARDENING_GUIDE.md § "Pattern 1–12" to replace soft language.

Time: ~20 minutes

### REFERENCE_Builders.md
Search for: "all questions are optional" → Replace with explicit Tier requirements

Time: ~15 minutes

### Builder-specific files
(e.g., builders/product/BUILDER_Questions.md)

Search for soft modals (should, may, consider) and replace with imperatives (MUST, WILL, APPLY).

Time: ~10 minutes each

---

## Step 8: Document the Change

Create a CHANGELOG entry:

```markdown
# CHANGELOG — Documentation Builder

## v3.0 · April 2026 — HARDENED RULES

### Major Changes
- All soft modal verbs (should, may, could) replaced with hard imperatives (MUST, WILL)
- 6-gate workflow is now strict sequence (no reordering, no skipping)
- Tier 1 context (what + who) is MANDATORY before proceeding
- Generation plan MUST be confirmed with user before any doc is written
- All assumptions MUST be marked with [ASSUMED], [INFERRED], or [NEEDS INPUT]
- Quality gates are hard stops (minimum 85/100 / 90/100 for products)
- Project Instructions completely rewritten for maximum enforceability

### Files Changed
- CLAUDE.md → CLAUDE.md (v2.5 backed up as CLAUDE_v2.5_SOFT.md)
- PROJECT_INSTRUCTIONS_Docgen_Production.md → PROJECT_INSTRUCTIONS_HARDENED.md
- (New files for reference: HARDENING_GUIDE.md, DEPLOYMENT_STEPS.md)

### Enforcement Improvements
- "Show menu" → MANDATORY in first response (no exceptions)
- "Run quality gates" → All 5 gates MUST pass before shipping
- "Collect context" → Tier 1 MANDATORY (not optional)
- "Mark assumptions" → EVERY assumption MUST have tag
- "Confirm plan" → Explicit user approval REQUIRED

### Backward Compatibility
Old CLAUDE.md (v2.5) saved as `CLAUDE_v2.5_SOFT.md` for reference.
Not used by new projects. Can be deleted after migration complete.

---
```

---

## Step 9: Verify Deployment in Production

After deploying, run a real test:

### Test Scenario
1. Start a new conversation in the Claude.ai project
2. Say: "I want to build a mobile app for task tracking"
3. Verify each gate in sequence:
   - Gate 1: Build type identified as "Product" ✓
   - Gate 2: Asked "What does it do?" and "Who uses it?" ✓
   - Gate 3: Showed full generation plan and asked for approval ✓
   - Gate 4: Did NOT generate until approval was given ✓
   - Gate 5: Output includes quality scores ✓
   - Gate 6: Final delivery is versioned zip ✓

**Expected outcome:** If all 6 gates pass, the hardening is working.

---

## Step 10: Brief the Team (If Applicable)

If others use this project, update them:

### Message Template
```
Subject: Documentation Builder v3.0 — Hardened Rules

The Documentation Builder project has been upgraded to v3.0 with stricter enforcement:

Key changes:
1. Menu always shows first (no exceptions)
2. Context collection is Tier-1 mandatory (not optional)
3. Generation plan must be approved before any docs are generated
4. All assumptions must be marked [ASSUMED] or [INFERRED]
5. Quality gates are hard stops (85/100 minimum)

If you notice stricter behavior from the system, it's working correctly.

Old rules (v2.5) are available as CLAUDE_v2.5_SOFT.md for reference only.

Questions? Check HARDENING_GUIDE.md for the rationale.
```

---

## Quick Reference: What Changed

| Aspect | Old (v2.5) | New (v3.0) | Effect |
|---|---|---|---|
| Menu on first message | Recommended | MANDATORY | No escape hatch |
| Build type | Identify early | GATE 1 (strict) | Forces classification before context |
| Tier 1 context | Optional questions | MANDATORY before proceeding | No guessing |
| Generation plan | Nice to show | GATE 3 (must confirm) | Explicit approval required |
| Quality gates | Run on every doc | Hard stops (85/100 min) | No shipping below threshold |
| Assumptions | Mark if important | MARK EVERY ONE | 100% transparency |
| Modal verbs | "Should", "may", "consider" | "MUST", "WILL", "APPLY" | Zero ambiguity |
| Sequence | "Follow in order" | STRICT SEQUENCE (6 gates) | No reordering or skipping |

---

## Rollback Plan (If Needed)

If hardened rules cause problems:

1. Rename current: `CLAUDE.md` → `CLAUDE_v3.0_HARD.md`
2. Restore backup: `CLAUDE_v2.5_SOFT.md` → `CLAUDE.md`
3. Revert PROJECT_INSTRUCTIONS to old version
4. Restart project conversations

Time to rollback: ~2 minutes

---

## Success Metrics

After deployment, measure:

1. **Menu always shows first**: 100% of new conversations
2. **Build type classified before context**: 100% of sessions
3. **Tier 1 context collected**: 95%+ (only fails if user abandons)
4. **Generation plan confirmed**: 95%+ (only fails if user rejects)
5. **Quality gates passed**: 100% of shipped docs (85/100 minimum)
6. **Assumptions marked**: 100% of generated docs
7. **Zero vague language**: 100% of output docs

---

## Next Steps After Deployment

1. **Monitor first 5 sessions** — Verify hardening is working as expected
2. **Harden REFERENCE files** (lower priority but recommended)
3. **Document any edge cases** — Update SYSTEM_DEBT.md if issues arise
4. **Annual review** — Check if rules are still current (April 2027)

---

## Support

If rules are being broken:
1. Check PROJECT_INSTRUCTIONS were pasted completely
2. Clear browser cache
3. Start a brand-new conversation (not a continuation)
4. If still broken: Share a screenshot with the exact violation

---

*Deployment Guide v1.0 · April 2026*
*Estimated time to full deployment: 15 minutes*
*Estimated time to verify: 10 minutes*
*Total: ~25 minutes*
