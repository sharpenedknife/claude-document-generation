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

## Intake Questions

Ask all questions before generating. Do not generate with unknowns.

**Q0: Does this skill already exist?**
> Before we build, let's check. Describe the task in 1-2 sentences.
> I'll check whether an existing skill (from the 341-skill library) already covers this.
> If yes: should we use the existing skill, customize it, or build a distinct version?

**Q1: Skill Name & Trigger**
> What will this skill be called?
> - Slash command: `/name` (e.g., `/docgen`, `/review-pr`, `/campaign-plan`)
> - Keyword trigger: phrase Claude recognizes (e.g., "draft announcement", "start my day")
> - Autonomous: Claude invokes it when detecting a pattern (e.g., whenever a transcript is shared)
> The name becomes the directory name and the `name` frontmatter field.

**Q2: What Problem Does It Solve?**
> In 1-3 sentences: what specific, recurring task does this skill handle?
> What does a user need to do today that this skill will make reliable and repeatable?

**Q3: Trigger Description (The Critical One)**
> How should Claude know to use this skill? Give me:
> - The primary action it performs (start with a verb: "Creates", "Analyzes", "Drafts")
> - 3-5 specific phrases or contexts that should trigger it
> - Any file types or domains involved
> - Should it trigger even when the user doesn't use the exact skill name?
> Example: "Creates charts from data. Use whenever the user mentions charts, graphs, plotting,
> visualizing data, or asks to 'show' numbers — even if they don't say 'chart' explicitly."

**Q4: Input — What Does the User Provide?**
> What information does the user give when invoking this skill?
> Which inputs are required vs optional?
> What happens if a required input is missing — ask for it or fail gracefully?

**Q5: The Process — Step by Step**
> What should Claude do, in order, after receiving the input?
> Be specific about each step: what Claude reads, asks, generates, or calls.
> Each step must state what it produces by the end.

**Q6: Output — What Does the User Get?**
> Exact deliverable:
> - Format: markdown, HTML file, Slack message, JSON, inline response?
> - Approximate length/structure?
> - Saved to file or delivered inline in chat?

**Q7: Supporting Resources**
> Does this skill need:
> - `references/` files: docs, guidelines, templates loaded into context on demand?
> - `scripts/`: Python/bash for deterministic operations (file creation, data processing)?
> - `assets/`: templates, fonts, icons used in output?
> Does it depend on MCP tools? (List them — and define fallback if MCP is unavailable)

**Q8: Happy Path Example**
> One complete example from trigger to output:
> User says: [exact input] → Claude does: [steps] → User gets: [exact output format shown]
> This becomes the `<example>` block in the skill body.

---

## RESEARCH GATE (mandatory — runs after Q0, before Q1)

After Q0 is answered, STOP. Do not ask Q1 yet.

Tell the user:

> "Before I write your SKILL.md, do these 3 things and come back:
>
> **1. Do the task manually once right now. Write out every step.**
>    The skill body is a playbook — it must match what actually works, not what you think works.
>
> **2. Write 5 different ways a user might ask for this skill.**
>    These become the trigger description — the single most important field in SKILL.md.
>    Example: 'run A/B test', 'set up split test', 'test two versions', 'experiment design', 'measure variant'
>
> **3. What does a bad output look like? Name one failure mode.**
>    This becomes the Error Handling section.
>
> Come back with these 3 things."

Wait for user to return before proceeding to Q1.
If they want to skip: warn, proceed on explicit confirmation, mark ASSUMED.

---

## Context Tier Assessment (run before confirming generation plan)

Before showing the generation plan, assess how complete the user's intake is:

- **Tier 1 — Minimal (proceed with caution):** User answered Q0 only, or gave fewer than 3 sentences of detail total.
  → Say: "I have minimal context. I'll be making significant assumptions — every unverified item will be marked ASSUMED. Want to add more before I generate, or proceed with assumptions?"

- **Tier 2 — Solid:** Q0 through Q5 answered with specific, non-vague content.
  → Note any remaining defaults. Confirm and proceed.

- **Tier 3 — Full:** All questions answered with concrete, specific details.
  → Best output possible. Confirm and proceed.

Never skip this assessment. Never present assumptions as confirmed facts.

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
- [ ] All 8 questions answered before generation starts
- [ ] Description field: 50-120 words, starts with action verb, lists 3-5 trigger contexts, slightly pushy
- [ ] Body: under 500 lines — large reference material moved to `references/` subdirectory
- [ ] Every procedure step states what it produces
- [ ] Output format is specific enough that two AIs produce identical structure
- [ ] Error handling covers: missing input, unavailable MCP, malformed data
- [ ] Happy-path example is complete and specific (not hypothetical)
- [ ] `evals.json` created with 3-10 test prompts (core use case + 2 edge cases + 1 should-NOT-trigger)
- [ ] Passes Gate 2 (structure complete) and Gate 3 (no vague steps)
