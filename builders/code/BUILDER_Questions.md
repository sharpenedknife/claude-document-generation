# Builder: Code Documentation

**Domain:** `code`
**Use when:** Generating technical documentation for code — setup guides, API docs, architecture docs, ADRs, troubleshooting guides. All code in output is subject to `SYSTEM_Coding_Standards.md`.

---

## Intake Questions

**Q1: Doc type?**
> Choose: `setup-guide` | `api-guide` | `architecture` | `adr` | `troubleshooting`

**Q2: What system or codebase is this for?**
> Name, language/stack, version, brief description.

**Q3: Who is the reader?**
> `beginner` | `intermediate` | `advanced` | `all`
> Are they using this to BUILD, RUN, or MAINTAIN the system?

**Q4: What prerequisites are required?**
> List tools (with versions), access requirements, knowledge needed.

**Q5: What are the exact commands/endpoints/patterns to document?**
> Be specific. For setup guides: the full installation sequence.
> For API docs: the endpoint method + path + parameters.
> For architecture: the components and their relationships.

**Q6: What does a successful run look like?**
> What exact output confirms success? (Terminal output, HTTP response, file created, etc.)

**Q7: What are the top 3–5 errors or failure modes?**
> Provide exact error messages if known. These become the Troubleshooting section.

**Q8 (ADR only): What alternatives were considered?**
> List alternatives and why each was rejected.

---

## RESEARCH GATE (mandatory — runs after Q0, before Q1)

After Q0 is answered, STOP. Do not ask Q1 yet.

Tell the user:

> "Before I document your code, gather these:
>
> **1. Paste or attach the code to be documented.**
>    I will not document code I haven't read. No exceptions.
>
> **2. What does a correct run of this code look like?**
>    Paste a sample input and its expected output.
>
> **3. Who maintains this code?**
>    New team member / senior dev / external API consumer — this locks the depth and format.
>
> Come back with the code and these answers."

Wait for user to return. Proceed to Q1 only after they respond.

---

## Outputs to Generate

1. **`CODE_[TOPIC]_v1.0_[DATE].md`** — The documentation
2. **`CODE_[TOPIC]_DEBT.md`** — Known gaps (missing error signatures, untested commands, etc.)

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

## Code Quality Enforcement

Before delivering any code documentation:

1. Run SYSTEM_Coding_Standards.md checklist against every code block
2. Verify all commands were actually tested (or flag as "untested — verify before shipping")
3. Confirm model strings use current versions from RESEARCH_Claude_Project_Best_Practices.md
4. Mark AI-generated code blocks with the required marker comment

---

## Generation Checklist

- [ ] Language/stack confirmed
- [ ] All code blocks have language tags
- [ ] All commands show Expected output
- [ ] No hardcoded secrets
- [ ] Dependencies version-pinned
- [ ] Code within line-count limits
- [ ] Error signatures are exact strings (not descriptions)
- [ ] Token count within budget (`config/token_budgets.json`)
- [ ] Gate 1 verified before delivery
