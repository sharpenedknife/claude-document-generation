# Project Chat Instructions — Generation Rules

## What They Are

Custom instructions Claude receives when operating in a specific Claude Project. Define role, constraints, response format, and how Claude interprets context from the project's knowledge base.

**Scope:** Project-level behavior, not global Claude behavior.

---

## Core Rules

### 1. Length Constraint: 500–800 words max
- Longer = more tokens burned, less context for actual work
- Too short (< 300 words) = vague, contradictory behavior
- Target: Dense, no filler

### 2. Structure (recommended order)
1. **Role** — Who Claude becomes in this project (2-3 sentences)
2. **Context Interpretation** — How to read uploaded docs (2-3 sentences)
3. **Response Format** — What users should expect (style, structure, length)
4. **Do's** — 3–5 specific behaviors (bullet points)
5. **Don'ts** — 3–5 things never to do (bullet points)
6. **Examples** — 1–2 good responses, 1–2 bad responses (short snippets)

### 3. Role Definition
**Format:** One sentence for what you are, one for what you provide.

**Good:**
- "You are a technical documentation reviewer. You evaluate docs for clarity, completeness, and usability, then provide specific fixes."

**Bad:**
- "Help users with documentation." (vague, could mean anything)
- "You are an expert in all areas of documentation." (overpromise, no specificity)

### 4. Context Interpretation
**Critical rule:** Tell Claude how to use uploaded files, not what files exist.

**Good:**
- "Treat all .md files in this project as authoritative reference material. If a question relates to a topic covered in the files, quote relevant sections before answering."
- "Use prerequisites_guide.md as the gold standard for what good prerequisites look like."

**Bad:**
- "This project contains a prerequisites guide, documentation ecosystem plan, and templates." (listing, not instruction)
- "Read all the files." (too vague—which files? how should they inform behavior?)

### 5. Response Format Rules
**Be specific about:**
- Length (e.g., "Keep answers under 200 words unless user asks for depth")
- Structure (e.g., "Organize as: Problem → Root Cause → Fix → Why")
- Tone (e.g., "Direct, no preamble, no corporate jargon")
- Examples (e.g., "Always show before/after code or before/after copy")
- When to ask vs. answer (e.g., "If requirements are ambiguous, stop and ask. Don't guess.")

**Bad format examples:**
- "Be helpful and accurate." (meaningless)
- "Provide comprehensive responses." (how comprehensive? what does that look like?)
- "Use best practices." (which practices?)

### 6. Do's — Specific Behaviors
Each do must be:
- One action (not "do X and Y")
- Observable (someone could verify you're doing it)
- Tied to project purpose

**Good:**
- "Quote the prerequisites template whenever discussing what good prerequisites look like."
- "When evaluating docs, always reference the quality checklist."
- "If user asks for a doc type not in the templates, suggest the closest match + explain why."

**Bad:**
- "Always be thorough." (unmeasurable)
- "Help the user succeed." (too broad)

### 7. Don'ts — Hard Constraints
Things Claude must never do in this project, even if user asks.

**Good:**
- "Never generate documentation without referencing the Documentation_Content_Guide first."
- "Don't create prerequisites that violate the anti-patterns list."
- "Never suggest docs are finished without running the quality checklist."

**Bad:**
- "Don't be unhelpful." (not a constraint, it's obvious)
- "Don't make mistakes." (unmeasurable, implies you won't)

### 8. Examples — Show, Don't Tell
**Include:**
- 1 good response (full, or key excerpt)
- 1 bad response (the mistake you want to avoid)
- 2–3 sentences explaining why one is better

**Length:** Keep examples short (3–5 lines each).

**Example structure:**
```
GOOD:
User: "How should prerequisites be organized?"
Claude: [Answer that quotes template and gives specific structure]

BAD:
User: "How should prerequisites be organized?"
Claude: [Generic answer with no reference to project docs]

Why: Good answer anchors to the project's standard; bad answer ignores project context.
```

### 9. Negative Space Matters
**Don't include:**
- Links to files (Claude can't click them; you're relying on filenames)
- Assumptions about what Claude knows (you've already uploaded the docs)
- "You are an AI language model..." preamble (assume Claude knows what it is)
- Detailed file descriptions (save that for CLAUDE.md)
- Instructions on how to use Claude (focus on project-specific behavior)

---

## Anti-Patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| "Answer all questions accurately" | Unmeasurable, vague | "Quote the prerequisites template before answering questions about structure" |
| "Be professional and clear" | Describe what that looks like? | "Use short sentences. No jargon. Show examples." |
| "Help with documentation tasks" | What tasks? How? | "When user asks for a doc, suggest the matching template + explain why it fits" |
| "Use best practices" | Whose practices? | "Reference the quality checklist for every doc review" |
| "Think step by step" | Already built into Claude | Focus on project-specific logic instead |
| Listing files | "This project has A, B, C files" | "Use file A to validate B" (instruction, not listing) |

---

## Generation Process

### Step 1: Define Role Clearly
Answer:
- What singular perspective does Claude have in this project?
- What does Claude produce / provide?
- What's the success metric?

### Step 2: Extract "How to Use Context"
From CLAUDE.md or project overview:
- What files are most important?
- Which docs are reference (truth source) vs. examples vs. tools?
- How should conflicting info be resolved?

### Step 3: Write Response Format
Complete this sentence:
- "When a user asks me something, I should respond by: [structure], in [tone], at [length]"

### Step 4: List Specific Do's & Don'ts
For each:
- Is it observable?
- Is it project-specific (not general Claude behavior)?
- Can someone verify compliance?

### Step 5: Add Examples
Show:
- What good looks like in this project
- What bad looks like (common mistake)
- Why the difference matters

### Step 6: Test with Reader Claude
New conversation, paste instructions + ask:
- "In this project, how should I respond to [realistic question]?"
- "What should I never do in this project?"

Fix any ambiguity Reader Claude surfaces.

---

## Template

```markdown
# [Project Name] — Custom Instructions

## Role
[1 sentence: what you are] [1 sentence: what you provide]

## How to Use Project Context
[2–3 sentences: how to read/reference uploaded docs. Which are authoritative? How should they inform responses?]

## Response Format
[2–3 rules about length, structure, tone, examples. Be specific.]

## Do's
- [Specific action #1]
- [Specific action #2]
- [Specific action #3]

## Don'ts
- [Never do X]
- [Never do Y]
- [Never do Z]

## Examples

GOOD:
[Example response that follows the rules]

BAD:
[Example that violates the rules]

Why: [Explanation of the difference]
```

---

## Quality Checklist for Project Instructions

- [ ] Role statement is one sentence, specific, tied to project purpose
- [ ] Context interpretation tells Claude *how* to use docs, not just that they exist
- [ ] Response format rules are specific (length, structure, tone, when to ask vs. answer)
- [ ] Each do/don't is observable and project-specific
- [ ] Examples show good + bad with explanation
- [ ] No links to files (assume file names are known)
- [ ] No general Claude behavior rules (focus on project uniqueness)
- [ ] Total length 500–800 words
- [ ] No vague words: "helpful," "professional," "thorough," "best practices," "comprehensive"
- [ ] Reader Claude test passed (fresh instance answers questions correctly)
