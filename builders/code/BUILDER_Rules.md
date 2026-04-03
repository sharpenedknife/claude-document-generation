# Rules: Code Builder

---

## Code Documentation Rules (All Types)

1. **SYSTEM_Coding_Standards.md applies to every code block.** No exceptions. Any code block violating those standards = Gate 3 fail.

2. **Commands must be tested or explicitly flagged.** If a command hasn't been verified: prefix with `# ⚠️ Untested — verify before shipping`.

3. **Error signatures must be exact strings.** Copy from actual error output. "Something goes wrong with the connection" is not an error signature. `"ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"` is.

4. **One concept per doc.** Don't document the setup AND the architecture AND the API in one file. Split into separate docs. Each gets its own token budget.

5. **Version all external dependencies.** If the doc says "use library X" — it must say which version of X.

## Setup Guide Rules

- Prerequisites section is mandatory (Level 1–4 structure)
- Every step has exactly one action
- Verification step at the end
- "Uninstall / clean up" steps included if setup can be reversed

## API Guide Rules

- One endpoint per section
- Request example: full curl command with all required headers
- Response example: complete JSON, not truncated
- Error codes table: every known code with fix
- Rate limits documented if they exist

## Architecture Doc Rules

- Start with a system diagram (ASCII or Mermaid)
- One section per component
- Data flow described explicitly
- Decision rationale included
- "Not included" section: what's explicitly out of scope

## ADR Rules

- Context: what problem triggered this decision
- Decision: the exact choice made (one sentence)
- Consequences: what becomes easier, what becomes harder
- Alternatives considered: list with rejection reason
- Status: `Accepted` | `Deprecated` | `Superseded by [ADR title]`
- ADRs are immutable once status = Accepted — create a new ADR to supersede

## Troubleshooting Rules

- Error signature first (exact string), then root cause, then fix
- Fix steps must be commands, not descriptions
- "Verification" step at the end of each fix
- Max 5-7 errors per doc — move the rest to DEBT.md
