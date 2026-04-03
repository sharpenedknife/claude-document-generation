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
