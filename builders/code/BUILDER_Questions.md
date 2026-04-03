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

## Outputs to Generate

1. **`CODE_[TOPIC]_v1.0_[DATE].md`** — The documentation
2. **`CODE_[TOPIC]_DEBT.md`** — Known gaps (missing error signatures, untested commands, etc.)

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
