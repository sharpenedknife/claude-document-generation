# Builder: Skill / Slash Command

**Domain:** `claude-project`
**Use when:** Someone needs a repeatable, structured workflow — a `/command`, a trigger phrase, or an autonomous invocation pattern. Output is a `SKILL.md` file (with optional supporting directories) packaged as a `.skill` file.

---

## Before You Ask Anything

Read `system/guides/SYSTEM_Build_Decision_Framework.md` → "Skill signals" to confirm this is the right builder.

Check existing skills first. With 341+ skills available across 14 categories, the skill the user needs may already exist. Ask: "Have you checked the skills library? What skill name or category might cover this?" Don't build what's already built.

**Skill vs Claude Project vs MCP:**
- Skill = structured playbook Claude follows for a specific recurring task (output: SKILL.md + `.skill` file)
- Claude Project = persistent knowledge base + persona (broader scope, many sessions)
- MCP = live connection to an external system (actions/data in real tools)

---

## The Most Important Thing to Get Right: The Description

The `description` field in SKILL.md frontmatter is the **primary triggering mechanism**. Claude sees all installed skill names and descriptions in its system prompt and decides whether to read the full skill body based on these alone.

**Critical finding:** Claude under-triggers by default — it tends not to consult skills for tasks it thinks it can handle alone. Descriptions must be slightly "pushy" and enumerate specific trigger contexts.

Spend as much time on the description as on the rest of the skill body combined.

---

## How Intake Works — Flexible Context Collection

No question is mandatory. Users can describe their skill idea however they want — freeform, with examples, by uploading an existing workflow, or by answering structured questions. Claude assesses what's needed and asks only for the gaps.

---

## Context Assessment

### Tier 1 — Minimum (can generate basic skill)
- [ ] **What the skill does** — at least a clear description of the task it automates

Warn: "I can build a basic skill from this, but I'll need to assume the trigger description, input/output format, and process steps. The skill may not trigger correctly without a refined description. Want me to proceed, or add more detail?"

### Tier 2 — Solid (good skill)
Everything in Tier 1, plus:
- [ ] **Trigger contexts** — when/how Claude should invoke this
- [ ] **Input/Output** — what goes in, what comes out

### Tier 3 — Full (production-quality skill)
Everything in Tier 2, plus: detailed process steps, error handling, edge cases, happy-path example.

---

## Conversational Question Guide

Use these to fill gaps — only ask what's missing.

### Opening
> "Tell me about the skill you want to build. What recurring task should it automate? You can describe it freeform, show me an example of the task being done manually, or paste an existing workflow."

---

**Q0: Does this skill already exist?**
**Ask when:** Always — before building anything.
**Ask:** "Describe the task in 1-2 sentences. I'll check whether an existing skill covers this."
**Default if skipped:** Check anyway based on the description provided.

**Q1: Skill Name & Trigger**
**Ask when:** User hasn't named it or specified invocation.
**Ask:** "What will this skill be called? Slash command (`/name`), keyword trigger, or autonomous?"
**Default if skipped:** Derive name from the task description.

**Q2: What Problem Does It Solve?**
**Ask when:** The "why" isn't clear.
**Ask:** "What specific, recurring task does this skill handle?"
**Default if skipped:** Infer from context.

**Q3: Trigger Description (The Critical One)**
**Ask when:** You don't have enough for a strong description field.
**Ask:** "How should Claude know to use this skill? Give me the primary action + 3-5 specific phrases that should trigger it."
**Default if skipped:** Generate a description from the task description. Warn: "I've generated a trigger description but it may under-trigger. Review and refine it."

**Q4: Input**
**Ask when:** What the user provides is unclear.
**Ask:** "What information does the user give when invoking this skill? Required vs optional?"
**Default if skipped:** Infer from the task. Mark as INFERRED.

**Q5: The Process**
**Ask when:** You can't write the step-by-step procedure.
**Ask:** "What should Claude do, in order, after receiving the input?"
**Default if skipped:** Infer a basic process. Mark as INFERRED. Warn: "I've inferred the process steps — review carefully."

**Q6: Output**
**Ask when:** Deliverable format is unclear.
**Ask:** "What does the user get? Format, structure, length, saved to file or inline?"
**Default if skipped:** Assume inline markdown response. Mark as ASSUMED.

**Q7: Supporting Resources**
**Ask when:** Skill likely needs reference files, scripts, or MCP tools.
**Ask:** "Does this skill need reference files, scripts, or MCP connections?"
**Default if skipped:** Assume no supporting resources.

**Q8: Happy Path Example**
**Ask when:** No example provided.
**Ask:** "Show me one complete example: User says [X] → Claude does [Y] → User gets [Z]."
**Default if skipped:** Generate an example from the context. Mark as INFERRED.

---

## Outputs to Generate

1. **`skills/{name}/SKILL.md`** — YAML frontmatter + skill body (required)
2. **`skills/{name}/references/{topic}.md`** — reference files loaded on demand (if needed)
3. **`skills/{name}/scripts/`** — executable scripts for deterministic tasks (if needed)
4. **`skills/{name}/evals.json`** — 3-10 test prompts for trigger and output testing (always generate)

Packaging into `.skill` file: `python -m scripts.package_skill skills/{name}/`

---

## SKILL.md Required Structure

```markdown
---
name: skill-identifier
description: >
  [Primary action verb] + [what it does] + [when to use it].
  Include specific trigger contexts, file types, user phrases.
  Be slightly pushy — err toward triggering more than less.
  50-120 words. This field alone controls whether Claude reads this skill.
---

# Skill Name

One-sentence summary.

## When to Use This Skill
[Only if description couldn't cover everything]

## Prerequisites / Dependencies
[Tools, MCP connections, or context required. Define fallbacks if MCP unavailable.]

## Procedure

### Step 1 — [Name]
[Exact instructions. What Claude does. What it produces by end of step.]

### Step 2 — [Name]
[...]

## Output Format
[Exact structure, format, length of the deliverable.]

## Error Handling
[What Claude does when input is missing, malformed, or tools are unavailable.]

## Edge Cases
[Specific known edge cases and how to handle them.]

## Examples
<example>
[One complete happy-path: input → steps → exact output]
</example>

## See Also
- `references/topic.md` — [when to read this]
```

---

## Generation Checklist

- [ ] Existing skill library checked — not duplicating existing skill
- [ ] Context assessed — tier identified, assumptions listed
- [ ] User confirmed generation plan
- [ ] Description field: 50-120 words, starts with action verb, lists 3-5 trigger contexts, slightly pushy
- [ ] Body: under 500 lines — large reference material moved to `references/` subdirectory
- [ ] Every procedure step states what it produces
- [ ] Output format specific enough that two AIs produce identical structure
- [ ] Error handling covers: missing input, unavailable MCP, malformed data
- [ ] Happy-path example is complete and specific
- [ ] No hallucinated content — process steps traceable to user input or marked INFERRED
- [ ] `evals.json` created with 3-10 test prompts
- [ ] Passes Gate 2 (structure complete) and Gate 3 (no vague steps)
