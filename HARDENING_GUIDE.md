# Hardening Guide — Language Fixes for Enforcement
**Version:** 1.0 · April 2026
**Purpose:** Show specific language changes to convert soft recommendations into hard rules

---

## Summary: Where the Softness Is

Your original docs use permissive language that allows Claude to skip or reinterpret rules:

| Problem Pattern | Current Language | Hardened Version | Impact |
|---|---|---|---|
| Optional gates | "Use quality gates" | "MUST run all 5 quality gates before shipping" | Forces execution |
| Soft modals | "should", "may", "consider" | "MUST", "WILL", "APPLY" | Removes wiggle room |
| Permissive questions | "All questions are optional" | "Tier 1 context is MANDATORY before proceeding" | Enforces collection |
| Weak defaults | "Use smart defaults if needed" | "EVERY assumption MUST be marked [ASSUMED]" | Tracks uncertainty |
| Skippable steps | "You may skip X if Y" | "NO EXCEPTIONS. Follow 6-gate sequence in order." | Blocks shortcuts |
| Vague success | "should pass quality gates" | "MINIMUM 85/100. FAIL if below. No exceptions." | Hard threshold |

---

## Pattern 1: Optional Gates → Mandatory Gates

### Current (Soft)
```
"Run quality gates on every doc."
```

### Hardened
```
"EVERY doc MUST pass all 5 quality gates before shipping.
No exceptions. If any gate fails: STOP. Rewrite. Re-submit.
Minimum score: 85/100 (Products: 90/100)."
```

**Why:** "Run" is passive. "MUST" is active. "No exceptions" blocks wiggle room. Minimum score is a hard threshold.

---

## Pattern 2: Permissive Language → Hard Requirements

### Current (Soft)
```
"No question is mandatory. Users can provide context however they want."
```

### Hardened
```
"Tier 1 context is MANDATORY before proceeding.
- What does it do? (required)
- Who uses it? (required)

If user refuses to provide Tier 1: Do NOT generate.
Offer to create a template instead."
```

**Why:** Explicit requirements. Clear consequence if refused. No option to skip.

---

## Pattern 3: Modal Verbs → Imperative Verbs

### Modal Verbs (Soft)
```
- should confirm the plan
- may use defaults
- could apply skills
- might generate
- consider using templates
- try implementing
```

### Imperative Verbs (Hard)
```
- MUST confirm the plan
- WILL mark defaults with [ASSUMED]
- APPLY skills at each stage
- GENERATE in dependency order
- USE templates (never skip)
- IMPLEMENT exactly as specified
```

**Why:** Modal verbs allow exceptions. Imperatives demand action.

---

## Pattern 4: Unclear Conditions → Explicit Gates

### Current (Soft)
```
"If context is thin, warn the user and list assumptions."
```

### Hardened
```
"FAIL CONDITION: If Tier 1 is incomplete, STOP.
Ask user to provide:
1. What does it do? (missing)
2. Who uses it? (missing)

Do NOT proceed without both. Do NOT invent context."
```

**Why:** Explicit fail condition. No ambiguity. Required input named.

---

## Pattern 5: Flexible Sequence → Locked Sequence

### Current (Soft)
```
"Follow these steps in order: Step 1 → Step 2 → Step 3..."
```

### Hardened
```
"STRICT SEQUENCE. Do NOT skip or reorder.

GATE 1 → GATE 2 → GATE 3 → GATE 4 → GATE 5 → GATE 6

Proceed to next gate only when previous gate is confirmed.
FAIL if: You reorder, skip, or parallelize."
```

**Why:** "Strict" removes flexibility. "Do NOT" is explicit. Fail condition blocks attempts.

---

## Pattern 6: Vague Success Metrics → Hard Thresholds

### Current (Soft)
```
"Output should pass quality gates and be of high quality."
```

### Hardened
```
"MINIMUM QUALITY SCORE: 85/100 (Products: 90/100)

FAIL if: Any doc scores below minimum. Do NOT ship.
Rewrite and re-gate. No exceptions."
```

**Why:** Specific number. Clear pass/fail boundary. "No exceptions" blocks workarounds.

---

## Pattern 7: Assumption Handling → Mandatory Marking

### Current (Soft)
```
"Mark assumptions with [ASSUMED] when appropriate."
```

### Hardened
```
"EVERY assumption MUST be marked. No exceptions.

Required markers:
[ASSUMED] — You inferred this; user hasn't confirmed
[INFERRED] — You derived from context; likely correct
[NEEDS INPUT] — User MUST provide this

FAIL if: Any unmarked assumption ships."
```

**Why:** "Must" + "No exceptions". Three explicit marker types. Fail condition with enforcement.

---

## Pattern 8: Skill Loading → Strict Load Order

### Current (Soft)
```
"Check the SKILL MAP at each stage. Load skills as needed."
```

### Hardened
```
"STRICT LOAD ORDER:

Do NOT preload all skills upfront.
- At GATE 3: READ SKILL_MAP.md (identify skills)
- At generation time: READ only that specific SKILL.md
- Max 2 active skills per stage

FAIL if: You reference skills before their generation stage.
FAIL if: You preload all skills upfront."
```

**Why:** Explicit don't. Named load points. Explicit fail conditions.

---

## Pattern 9: Flexible Naming → Strict Naming Convention

### Current (Soft)
```
"Use correct file naming conventions (see SYSTEM_File_Naming)."
```

### Hardened
```
"File naming is NON-NEGOTIABLE.

Output files: {DOMAIN}_{Topic}_v{X.Y}_{YYYY-MM-DD}.md

Example: PRODUCT_Architecture_v1.0_2026-04-06.md

FAIL if: File name doesn't match convention.
Action: Rename before shipping. Do NOT ship with wrong names."
```

**Why:** Specific pattern. Example. Explicit fail condition with recovery step.

---

## Pattern 10: Optional Confirmation → Mandatory Confirmation

### Current (Soft)
```
"Show the plan to the user and get confirmation."
```

### Hardened
```
"MANDATORY CONFIRMATION POINT.

Display plan with:
- Every doc you will generate
- Which skill handles each doc
- All [ASSUMED] and [INFERRED] markers

Ask explicitly: 'Does this look right? Should I proceed?'

Wait for approval. Do NOT generate without:
- 'yes' | 'sounds good' | 'go ahead' | equivalent

FAIL if: User says no. Revise plan and re-show.
FAIL if: You proceed without explicit user approval."
```

**Why:** Three separate mandatory elements. Explicit approval words listed. Dual fail conditions.

---

## Pattern 11: Weak Conflict Resolution → Enforced Hierarchy

### Current (Soft)
```
"When files conflict: SYSTEM_Exit_Rules wins."
```

### Hardened
```
"AUTHORITY HIERARCHY (absolute, no exceptions):

1. SYSTEM_Exit_Rules.md ← HIGHEST
2. SYSTEM_Content_Guide.md
3. SYSTEM_Build_Decision_Framework.md
4. BUILDER_Rules.md
5. All other files ← LOWEST

If conflict: Cite the winning rule. Explain which wins.
Proceed with higher-priority rule.

FAIL if: You follow lower-priority rule in conflict."
```

**Why:** Numbered list. "No exceptions". Required citation. Explicit fail condition.

---

## Pattern 12: Vague Do's and Don'ts → Explicit Lists

### Current (Soft)
```
"Try to follow best practices. Avoid common mistakes."
```

### Hardened
```
"NEVER DO THESE (Automatic Fail):
❌ Skip menu in first response
❌ Generate without confirming plan
❌ Proceed with less than Tier 1 context
❌ Skip quality gates
❌ Ship unmarked assumption
[... 7 more explicit don'ts]

ALWAYS DO THESE (Automatic Pass Requirement):
✅ Show menu in first response
✅ Identify build type before other action
✅ Collect Tier 1 context before proceeding
[... 7 more explicit do's]"
```

**Why:** Checkboxes. "Automatic fail/pass". Explicit, countable list.

---

## How to Apply This Across Your Docs

### Step 1: Find Soft Modal Verbs (High Priority)
Search for: should | may | might | could | consider | try | appear | seem | possible

Replace with: MUST | WILL | DOES | APPLY | USE | IS | WILL NOT

### Step 2: Find Optional Language (High Priority)
Search for: optional | flexible | can | may provide | feel free

Replace with: MANDATORY | REQUIRED | MUST | WILL

### Step 3: Find Weak Conditions (Medium Priority)
Search for: if needed | as appropriate | when possible | try to

Replace with: FAIL if | MUST | ALWAYS | NO EXCEPTIONS

### Step 4: Find Vague Thresholds (Medium Priority)
Search for: high quality | should work | be good | acceptable

Replace with: MINIMUM 85/100 | MUST PASS | REQUIRED SCORE | NO EXCEPTIONS

### Step 5: Find Unmarked Assumptions (High Priority)
Search for: probably | likely | generally | typically

Replace with: [ASSUMED] or [INFERRED] with explicit marker

### Step 6: Add Fail Conditions (High Priority)
For every MUST statement, add:
```
"FAIL if: [explicit failure condition]"
```

### Step 7: Remove "Consider" and "Try" (High Priority)
Replace all:
- "Consider using X" → "USE X"
- "Try to implement" → "IMPLEMENT exactly"
- "Look for X" → "IDENTIFY X"

---

## File-by-File Hardening Checklist

- [ ] **CLAUDE.md**
  - [ ] "Rules" section uses MUST (not should)
  - [ ] "Optional questions" is removed
  - [ ] All 6 gates are numbered, strict sequence
  - [ ] Quality gate minimum score is explicit (85/100 / 90/100)
  - [ ] Fail conditions provided for every gate

- [ ] **REFERENCE_System.md**
  - [ ] No "may use" or "should consider"
  - [ ] All patterns are MUST/WILL
  - [ ] Prerequisites are marked MANDATORY
  - [ ] Assumptions are marked with tags

- [ ] **REFERENCE_Builders.md**
  - [ ] Tier 1 is MANDATORY (not optional)
  - [ ] Default assumptions are marked [ASSUMED]
  - [ ] Questions list shows which are mandatory vs. informational
  - [ ] Context gates have explicit FAIL conditions

- [ ] **PROJECT_INSTRUCTIONS_Docgen_Production.md**
  - [ ] First rule: ALWAYS show menu
  - [ ] 6-gate sequence is strict
  - [ ] No modal verbs in rules
  - [ ] Quality gates are hard stops
  - [ ] Fail conditions provided for every rule

---

## Examples of Effective Hardening

### Example 1: Quality Gates

**Before (Soft):**
```
"Run quality gates on every doc to ensure quality."
```

**After (Hard):**
```
"EVERY doc MUST pass all 5 quality gates before shipping.

Gate 1 · Validation: File name, metadata, domain
Gate 2 · Structure: All required sections present
Gate 3 · Content: No vague language, claims backed
Gate 4 · Quality: Score ≥85/100, within budget, readable
Gate 5 · Shipping: Version stamped, DEBT logged

MINIMUM SCORE: 85/100 (Products: 90/100)

FAIL if: Any gate fails. Stop. Rewrite. Re-gate.
FAIL if: Doc scores below minimum. Do NOT ship."
```

### Example 2: Build Type Identification

**Before (Soft):**
```
"Try to identify the build type from the user's description."
```

**After (Hard):**
```
"GATE 1: Identify Build Type

MANDATORY. Do NOT skip.

READ SYSTEM_Build_Decision_Framework.
Ask user: 'Which best describes what you're building?'
- Product / Startup
- Claude Project
- Skill
- MCP Server
- Other

FAIL if: Classification is ambiguous.
Recovery: Ask clarifying questions until certain."
```

### Example 3: Assumption Marking

**Before (Soft):**
```
"Mark important assumptions in the documentation."
```

**After (Hard):**
```
"EVERY assumption MUST be marked. No exceptions.

Required tag format:
[ASSUMED] — You inferred; user hasn't confirmed
[INFERRED] — You derived from context; likely correct
[NEEDS INPUT] — User MUST provide

Examples:
✓ [ASSUMED] We are building a web app, not mobile.
✓ [INFERRED] Users authenticate via OAuth.
✗ Smart caching improves performance.  ← NO MARKER = FAIL

FAIL if: Any assumption shipped without a marker."
```

---

## The 3-Word Test

After hardening a rule, read it aloud. It should contain **at least one** of these words:
- MUST (imperative)
- WILL NOT (absolute negative)
- FAIL if (consequence)
- NO EXCEPTIONS (completeness)

**Example:**
- ❌ "Consider using templates" (no strength words)
- ✅ "MUST use templates. FAIL if structure ignored." (has MUST + FAIL)

---

## Enforcement Tone

Hardened rules use this tone:
1. **Direct**: "You MUST do X"
2. **Specific**: "FAIL if Y occurs"
3. **Complete**: "No exceptions. Always. Every time."
4. **Cited**: "See SYSTEM_Exit_Rules § XYZ"

Avoid:
- ❌ "Try to..." (weak)
- ❌ "...when possible" (escape hatch)
- ❌ "...consider using..." (optional)
- ❌ "...should..." (permissive)

---

## Deployment Checklist

Before deploying hardened rules to Claude.ai:

- [ ] Copied PROJECT_INSTRUCTIONS_HARDENED.md into Project Settings
- [ ] Updated CLAUDE.md with CLAUDE_HARDENED.md content
- [ ] Updated all REFERENCE_*.md files to remove soft modal verbs
- [ ] Updated all BUILDER_Questions.md to mark Tier 1 as MANDATORY
- [ ] Added FAIL conditions to every rule with consequences
- [ ] Tested: First message shows menu (no exceptions)
- [ ] Tested: Gate sequence cannot be skipped
- [ ] Tested: Quality gates block shipping below minimum

---

*Hardening Guide v1.0 · April 2026*
