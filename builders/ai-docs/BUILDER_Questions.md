# Builder: AI Documentation

**Domain:** `ai-docs`
**Use when:** Generating or updating a single document for an AI workflow, Claude project, or AI implementation. Also covers process docs, how-to guides, and feature docs.

Three modes:

1. **New doc from scratch** — Generate a complete doc for a new topic
2. **Update existing doc** — Improve, extend, or correct an existing document
3. **Gap-fill** — Add a missing section to an existing doc

---

## Mode 1: New Doc from Scratch

**Q1: Doc type?**
> Choose: `how-to` | `reference` | `feature` | `process` | `system-guide`

**Q2: What is this doc about?**
> Describe the topic in 1 sentence. What does the reader do or learn?

**Q3: Who reads this?**
> Audience: `beginner` | `intermediate` | `advanced` | `all`
> Are they human, AI system, or both?

**Q4: What must the reader already know or have?**
> List prerequisites. If none, say "none."

**Q5: What are the 3–5 main things this doc covers?**
> These become the main sections.

**Q6: Are there code examples?**
> If yes: What language? What does the code do? (Applies `SYSTEM_Coding_Standards.md`)

**Q7: What does success look like?**
> What can the reader do or verify after completing this doc?

---

## RESEARCH GATE (mandatory — runs after Q0, before Q1)

After Q0 is answered, STOP. Do not ask Q1 yet.

Tell the user:

> "Before I generate your AI doc, collect these first:
>
> **1. What is the exact behavior you need documented?**
>    Run the feature or workflow yourself once. Write down what you observe — not what the spec says.
>
> **2. Who will read this doc?**
>    Beginner / intermediate / advanced. This locks the vocabulary and depth.
>
> **3. What question should this doc answer when someone searches for it?**
>    Write the exact search query a reader would use. This becomes the title.
>
> Come back with these 3 things."

Wait for user to return. Proceed to Q1 only after they respond.

---

## Mode 2: Update Existing Doc

**Q1: What is the file name of the existing doc?**
> Provide exact file path.

**Q2: What specifically needs to change?**
> Be precise: "Add error handling to Step 3", "Update model string to claude-sonnet-4-6", "Add prerequisites section"

**Q3: What gate(s) did this doc fail?**
> If you know — helps target the fix.

**Q4: Are there sections to preserve exactly?**
> List sections that must not change.

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

## Mode 3: Gap-Fill

**Q1: What doc is being extended?**
> Provide exact file path.

**Q2: What section is missing?**
> Describe the gap.

**Q3: What's the token budget remaining?**
> Check `config/token_budgets.json` for the doc type. New section must fit within remaining budget.

---

## Outputs to Generate

For new docs:
1. **`[CATEGORY]_[TOPIC]_v1.0_[DATE].md`** — The document itself
2. **`[DOCNAME]_DEBT.md`** — Known gaps (even if empty, template must exist)

For updates:
1. **Updated version of existing doc** — Increment version in frontmatter (v1.0 → v1.1)
2. **Updated DEBT.md** — Add/remove debt items as appropriate

---

## Generation Checklist

- [ ] Doc type confirmed before generating
- [ ] DOC_CANONICAL_TEMPLATE.md structure followed exactly
- [ ] Code blocks pass SYSTEM_Coding_Standards.md
- [ ] File named using pattern `{CATEGORY}_{TOPIC}_{VERSION}_{DATE}.md`
- [ ] Token count checked against `config/token_budgets.json`
- [ ] Gate 1 checked before delivery
