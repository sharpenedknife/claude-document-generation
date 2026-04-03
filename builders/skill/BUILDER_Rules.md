# Builder Rules: Skill / Slash Command

**Applies to:** All SKILL.md files and supporting skill assets
**Authority:** After `SYSTEM_Exit_Rules.md` and `SYSTEM_Content_Guide.md`.
**Source:** Skills Manager project instructions + community skill authoring best practices

---

## Rule 1: The Description Is the Skill

The `description` YAML frontmatter field is the **only thing Claude reads** before deciding whether to load the full skill. Everything else — the body, procedures, examples — is irrelevant if the description fails to trigger.

**Description requirements:**
- 50–120 words (hard limits — too short doesn't trigger, too long wastes context)
- Starts with a primary action verb: "Creates", "Analyzes", "Drafts", "Converts", "Builds"
- States WHAT the skill does AND WHEN to use it
- Lists 3–5 specific trigger phrases or contexts
- Uses "whenever" or "always use when" at least once
- Is slightly pushy — Claude under-triggers by default, so descriptions must compensate

```yaml
# BAD — only says what, not when:
description: Creates charts from data.

# BAD — too vague:
description: Helps with documents.

# BAD — too narrow:
description: Only for .docx files with tracked changes when the user says "review".

# GOOD — what + when + slightly pushy:
description: >
  Creates charts and data visualizations from spreadsheets, CSVs, or raw numbers.
  Use this whenever the user mentions charts, graphs, plotting, visualizing data,
  or asks to "show" numerical data — even if they don't say "chart" explicitly.
  Always use this skill when the user shares tabular data and wants to understand
  trends, comparisons, or distributions.
```

---

## Rule 2: SKILL.md Body Is a Playbook, Not a Description

Every sentence in the body must be an instruction Claude can follow — not a description of what Claude might do.

**Bad:** "Claude will help the user with their campaign planning needs."
**Good:** "Ask: What is the campaign goal? (brand awareness / lead gen / product launch). Wait for answer before proceeding to Step 2."

Body must be **under 500 lines**. If you're approaching the limit, move reference material to `references/` files and link them with guidance on when to read them.

---

## Rule 3: Directory Structure

```
skill-name/
├── SKILL.md              ← required
├── scripts/              ← optional; Python/bash for deterministic tasks
├── references/           ← optional; docs loaded into context on demand
├── assets/               ← optional; templates, fonts, icons
└── evals.json            ← always generate; 3-10 test prompts
```

Reference files in `references/` should be linked from SKILL.md with a "See Also" section that says WHEN to read each one — not just that it exists.

---

## Rule 4: Intake Must Be Gated

The skill must not produce output until minimum required inputs are collected. Mark optionals clearly.

```markdown
## Procedure

### Step 1 — Collect Inputs
Required before proceeding:
- [ ] [Input 1] (required) — ask: "[exact question to user]"
- [ ] [Input 2] (required) — ask: "[exact question]"
- [ ] [Input 3] (optional) — ask only if [condition]; default: [value]

If any required input is missing, ask for it. Do not proceed with placeholders.
```

---

## Rule 5: Every Procedure Step Has an Expected Output

```markdown
# BAD:
### Step 2 — Research the company.

# GOOD:
### Step 2 — Research Company Context
Search web for "[company] recent news" and "[company] product focus".
Output: 3-5 bullet points covering funding, product direction, and recent launches.
If no results found: note "no recent news found" and proceed to Step 3 with available info.
```

---

## Rule 6: Error Handling Is Mandatory

Every skill must define what Claude does when things go wrong. No skill ships without an Error Handling section.

Required error scenarios to cover:
- Required input is missing or malformed
- MCP tool is unavailable or returns an error (define the fallback)
- External search returns no results
- Generated output doesn't match expected format

```markdown
## Error Handling

**Missing required input:** Ask once. If still not provided after second ask, tell user what
you need and stop: "I need [X] to proceed. Please provide it and I'll continue."

**MCP unavailable:** If [tool] is not connected, fall back to: [specific alternative behavior].
Never silently fail — always tell the user what you're doing instead.

**No search results:** Note it explicitly: "Found no recent information on [X]."
Continue with available context rather than inventing data.
```

---

## Rule 7: The Example Is the Most Valuable Part

The `<example>` block in the skill body is what makes the skill immediately usable and testable. It must be:
- A specific, realistic scenario (not "user asks for X and Claude helps")
- Complete: trigger → every step → exact output shown
- Wrapped in `<example>` XML tags

If you can't write a complete example, the skill is underspecified — go back and clarify the procedure.

---

## Rule 8: Always Generate evals.json

Every skill output must include an `evals.json` with test prompts. Minimum 3, target 5-10.

```json
{
  "skill": "skill-name",
  "test_prompts": [
    {
      "id": "core-use-case",
      "prompt": "[Realistic user input for the main use case]",
      "should_trigger": true,
      "expected_output_contains": ["[key element 1]", "[key element 2]"]
    },
    {
      "id": "edge-case-1",
      "prompt": "[Input that tests an edge case]",
      "should_trigger": true,
      "expected_output_contains": ["[what should appear]"]
    },
    {
      "id": "should-not-trigger",
      "prompt": "[Input that looks similar but shouldn't use this skill]",
      "should_trigger": false
    }
  ]
}
```

Test prompts must be: substantive (not trivially simple), realistic user language (casual, messy, ambiguous), and cover core use case + at least 2 edge cases + 1 should-NOT-trigger case.

---

## Rule 9: Packaging

After generation and testing, package the skill:
```bash
python -m scripts.package_skill skills/{name}/
```

Present the resulting `.skill` file to the user for installation. Skills are installed by the user — do not attempt to install them directly.

---

## Rule 10: MCP Dependencies Must Be Declared and Fallback-Defined

```markdown
## Prerequisites / Dependencies

| Tool | MCP connector | Required for | Fallback if unavailable |
|---|---|---|---|
| Slack | slack-by-salesforce | Read channel messages | Draft message for user to send manually |
| Jira | atlassian | Create follow-up tickets | List action items for user to log manually |

If [MCP] is unavailable, Claude must [specific fallback behavior] and inform the user.
```

---

## Gate Applicability

| Gate | Applies? | Notes |
|---|---|---|
| Gate 1 (naming) | Yes | `skills/{name}/SKILL.md` |
| Gate 2 (structure) | Yes | YAML frontmatter + all required sections present |
| Gate 3 (content) | Yes | Description 50-120w, no vague steps, error handling present |
| Gate 4 (token budget) | Partial | Body under 500 lines; description under 120 words |
| Gate 5 (shipping) | Yes | evals.json present, version stamp in frontmatter |
