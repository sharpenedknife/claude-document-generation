# Rules: Claude Project Builder

**These rules govern all output from the claude-project builder.**

---

## CLAUDE.md Rules

1. **Max 200 lines.** Beyond this, compliance degrades. Prune ruthlessly.
2. **No content from SYSTEM_* files inline.** Tell Claude WHERE to find information — don't paste the content. Progressive disclosure.
3. **Required sections in order:**
   - What This Is (2 sentences)
   - Rules (max 5, numbered, action-verb each)
   - File Map (folder tree with ← annotations)
   - Quality Gate Cheat Sheet (table)
   - Authoritative File Priority (when files conflict)
   - How to Set Up the Claude Project (3 steps)
4. **File map annotations must be accurate.** Every folder and file in the map must actually exist in the workspace.
5. **No prose paragraphs.** Bullets, tables, code blocks only. This is a navigation document.

## Project Instructions Rules

**Always call `Skill tool: prompt-building:prompt-engineering-patterns` before writing project instructions.** Apply its output for: role-based system prompt structure, progressive disclosure (simple → detailed), structured output format, and error recovery patterns. This skill is installed and callable — do not fall back to reading a local SKILL.md.

Follow `SYSTEM_Project_Instructions_Rules.md` exactly. Key constraints:
- 500–800 words total
- 6 sections: Role → Context Interpretation → Response Format → Do's (5) → Don'ts (5) → Examples
- "Read CLAUDE.md first" must be Do #1
- 2–3 labeled examples (at least 1 GOOD, 1 BAD)
- Timestamp: `Last updated: [Month Year]`

## Domain Definitions Rules

- Only define domains that are ACTUALLY used in this project
- Do not carry over domains from other projects
- Each domain needs: name, description, doc_types[], primary_audience, priority, status

## Token Budget Rules

- Every doc type that could be generated in this project must have a budget
- Use `config/token_budgets.json` from this system as reference for reasonable ranges
- Do not set budgets higher than the reference unless justified in rationale field

## LLM-Focused Claude Projects — Additional Skills

When the Claude Project being built handles prompts, evaluations, or LLM chains (e.g., a research assistant, a doc generator, a coding agent), call these skills during generation:

| Stage | Call |
|-------|------|
| Project Instructions | `Skill tool: prompt-building:prompt-engineering-patterns` (always) |
| Knowledge Base Structure (if RAG) | `Skill tool: prompt-building:similarity-search-patterns` |
| Custom Skills that call LLMs | `Skill tool: prompt-building:langchain-architecture` |
| Evaluating output quality section | `Skill tool: prompt-building:llm-evaluation` |

---

## README Rules

- Exactly 3 steps: (1) Create project on claude.ai, (2) Sync folder, (3) Paste project instructions
- Link to exact file paths for steps 2 and 3
- Include what the project will do in 2 sentences at the top
