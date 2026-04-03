# Rules: AI Docs Builder

---

## Content Rules (All AI Docs)

1. **Write for both human and AI readers simultaneously.** Every section must be machine-parseable (structured metadata) AND human-readable (clear prose).

2. **Audience-appropriate depth.** `beginner` = zero assumed knowledge, full commands, every step. `advanced` = skip boilerplate, focus on non-obvious parts. `all` = layered: basics first, advanced details in subsections.

3. **No vague language.** Flag these immediately as Gate 3 violations:
   - "Configure properly" → specify the exact config
   - "Make sure it works" → specify the exact verification command
   - "Follow best practices" → cite the specific practice
   - "As appropriate" → specify the condition

4. **Every claim needs specifics.** No unsourced assertions. "Claude performs better" → "Claude Sonnet 4.6 achieves X% on Y benchmark (source: Anthropic docs, [date])."

5. **AI metadata blocks are required in all steps.** See DOC_CANONICAL_TEMPLATE.md § Section 3.

## How-To Specific Rules

- Steps are numbered 1, 2, 3 — not bullets
- Each step has one action only
- Every executable command shows Expected output
- Prerequisite verification command at the end of Prerequisites section

## Reference Doc Specific Rules

- Tables preferred over prose for structured data
- Every option has: type, required/optional, default, example
- Alphabetical ordering within tables
- No how-to content in reference docs — link to how-to instead

## System Guide Specific Rules

- These are rules files — write as laws, not suggestions
- Use positive + negative examples (GOOD/BAD patterns) for every rule
- Rules must be falsifiable (you can check if they're violated)
- Max 5 rules per section — more than 5 = restructure into subsections

## Update Doc Rules

- Increment version in frontmatter (1.0 → 1.1 for minor, 1.1 → 2.0 for major rewrite)
- Log what changed in a `## Changelog` section at the bottom
- Never delete sections — deprecate with `[DEPRECATED]` marker and reason
- Update DEBT.md to remove resolved items and add new ones
