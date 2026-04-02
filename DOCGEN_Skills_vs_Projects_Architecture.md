# Docgen Architecture: Skills vs Projects (Technical Differences)

**Both** are Claude customization packages. **Different purposes, different structures.**

---

## Foundational Difference

### **Skill (9th Main Project)**

**What it is:** Reusable tool/workflow that Claude activates when conditions match  
**Where it runs:** Any Claude conversation (claude.ai, Projects, API, etc.)  
**Trigger:** Pattern matching + user request + context  
**Scope:** Specific task/domain  
**Lifecycle:** Persistent, shareable, library-able

**Example:**
```
Skill: "customer-research"
Triggers when: User mentions "research customers" OR "customer interviews" OR "market research"
Does: Guide user through research process, ask questions, synthesize findings
Returns: Structured customer research document
Can be used in: Any Project, any conversation, any context
```

### **Project (10th Main Project)**

**What it is:** Persistent chat environment with custom rules, memory, and tools  
**Where it runs:** Claude.ai Projects only (dedicated workspace)  
**Trigger:** User opens the project  
**Scope:** Broad workflow (e.g., "Docgen", "Product Management", "Design System")  
**Lifecycle:** Ongoing, stateful, project-specific

**Example:**
```
Project: "Product Development Hub"
Provides: Persistent workspace for building products
Includes: PRD template, UX framework, dev plan, quality gates
Remembers: What user built, previous decisions, preferences
Tools: GitHub integration, Notion, Jira
Workflow: Multi-turn conversation over days/weeks
```

---

## Technical Comparison

| Aspect | Skill | Project |
|--------|-------|---------|
| **Type** | Triggerable workflow | Chat environment |
| **Entry** | Pattern match + request | User opens project |
| **Scope** | Focused task | Broad domain |
| **State** | Stateless (per invocation) | Stateful (persistent) |
| **Memory** | None (each invocation fresh) | Optional (remembers across sessions) |
| **Integration** | Any conversation | Project-only |
| **Tools** | Limited (Claude's built-in) | Rich (MCP servers) |
| **Duration** | Minutes | Days/weeks |
| **Sharing** | Library → reusable | Private to user |

---

## When to Use Each

### Use **Skill** When

User needs Claude to:
- Handle a specific task (research, analysis, planning)
- Be triggered automatically (pattern match)
- Work in any context (not just one project)
- Be reusable across multiple projects
- Solve a focused problem (not an ongoing workflow)

**Example skills:**
- customer-research (gathers customer insights)
- competitive-analysis (analyzes competitors)
- content-strategy (plans content)
- user-testing (designs user tests)
- pricing-analysis (evaluates pricing models)

### Use **Project** When

User needs Claude to:
- Provide persistent workspace for workflow
- Maintain state across sessions (remember decisions)
- Offer multiple related tools (Notion, GitHub, Jira)
- Guide complex multi-step process
- Be deeply integrated (not triggered, but environment)

**Example projects:**
- Product Development Hub (PRD, UX, dev plan, monetization)
- Design System Manager (components, tokens, guidelines)
- Content Calendar (planning, drafting, publishing)
- Sales Pipeline (deals, forecasts, accounts)
- Docgen (what we're building)

---

## Integration: Product → Project Flow

User can build product using Fast Product MVP, then create Project for it.

### Step 1: Generate Product Docs

```
User: "I want to build a SaaS"

Main Project: Fast Product MVP
  ↓ Generates:
  - PRD.md
  - UX_Requirements.md
  - specifiers.md
  - safety.md (optional)
  
Output: Zip file with 3-4 documents
```

### Step 2: Generate Project for Those Docs

```
User: "Now create a Claude Project to manage this product"

Main Project: Claude Project (10th)
  
Questions:
Q1: What's this project for?
    "Managing the product I just defined"

Q2: What docs should it reference?
    [Options: Link to previous generation, or upload new]
    User: [Select PRD, UX from previous]

Q3: What tools need integration?
    [Checkboxes: GitHub, Notion, Jira, etc.]
    User: Selects: GitHub, Notion

Q4: What workflow?
    "Week 1-2: Design review, Week 3-4: Engineering kickoff"

Generates:
  - PROJECT_INSTRUCTIONS_ProductName.md
  - welcome-message.md
  - conversation-examples.md
  - tool-integration-guide.md
  - memory-system.md
  
Output: Zip with all Project setup files
```

### Step 3: Deploy Project

```
User opens Claude Projects
  → Click "Create New"
  → Paste PROJECT_INSTRUCTIONS_ProductName.md
  → Connect MCP tools (GitHub, Notion, Jira)
  → Project live
```

---

## File Structure Output

### Skill Package (9th Main Project)

```
docgen_skill_[name]_v1.0.zip
│
├── [skill-name].md                 ← Main skill definition
│   • What it does
│   • When to use
│   • How it works
│   • Examples
│
├── trigger-patterns.md             ← Pattern matching rules
│   • Regex patterns
│   • Trigger phrases
│   • Context conditions
│   • Fallback behavior
│
├── implementation-guide.md         ← For developers
│   • Parameters
│   • Return format
│   • Error handling
│   • Integration points
│
├── examples.md                     ← Usage examples
│   • "I want to research customers"
│   • "Help me analyze competitors"
│   • Etc.
│
├── related-skills.md               ← Companion skills
│   • Links to related skills
│   • How they work together
│   • Workflow chains
│
└── metadata.json
    • skill_name
    • version
    • domain
    • trigger_patterns[]
    • dependencies[]
    • quality_score
```

### Project Package (10th Main Project)

```
docgen_project_[name]_v1.0.zip
│
├── PROJECT_INSTRUCTIONS_[name].md  ← Main instructions
│   • System message
│   • Role & capabilities
│   • Available commands
│   • Success criteria
│
├── welcome-message.md              ← What user sees on entry
│   • Friendly greeting
│   • What's available
│   • Quick start
│
├── conversation-flow-examples.md   ← Sample interactions
│   • User: "Let's build a PRD"
│   • Claude: [Response]
│   • User: [Follow-up]
│   • Claude: [Result]
│
├── mcp-integrations.md             ← Tool setup
│   • Which MCP servers needed
│   • OAuth setup instructions
│   • Permission scopes
│   • Example API calls
│
├── memory-system.md                ← How memory works
│   • What to remember
│   • How long to remember
│   • Memory structure
│   • Update triggers
│
└── metadata.json
    • project_name
    • version
    • mcp_servers[]
    • memory_enabled
    • quality_score
```

---

## Why Separate (Not Combined)

**Could we combine into one project with embedded skills?**

Technically yes, but **not recommended** because:

1. **Reusability**
   - Skill: Used in 100 projects
   - Project: Specific to one use case
   - Combined: Can't reuse

2. **Complexity**
   - Skill: Simple, focused, easy to test
   - Project: Complex, stateful, many integrations
   - Combined: Bloated, hard to maintain

3. **Lifecycle**
   - Skill: Update once → works everywhere
   - Project: Update once → works for one user
   - Combined: Updates affect both (risky)

4. **Scope**
   - Skill: "How to do X"
   - Project: "Complete workflow for Y"
   - Combined: Neither clear

**Better pattern:** Skills as building blocks, Projects assemble them.

---

## Integration Pattern

```
User has:
  Skill: customer-research
  Skill: competitive-analysis
  Skill: market-sizing
  
User creates:
  Project: Product Marketing Hub
  
Project imports:
  → Triggers customer-research when user says "research customers"
  → Triggers competitive-analysis when user says "analyze competitors"
  → Triggers market-sizing when user says "what's TAM"
  → But also provides project-level memory, tools, workflows
```

---

## Questionnaire Differences

### **Skill Questionnaire (9th Main Project)**

```
Q1: What does your skill do?
    "Help users research customer needs"

Q2: When should it be triggered?
    "When user mentions customer research, interviews, feedback"

Q3: What's the output?
    "Structured research document with insights"

Q4: Who's the user?
    "Product managers, founders"

Q5: Examples of it being used?
    "User: 'I need to research my market'
     Skill: [Ask questions, guide research, synthesize]"

Q6: Related skills?
    "Competitive analysis, market sizing"

[Generate skill package]
```

### **Project Questionnaire (10th Main Project)**

```
Q1: What's this project for?
    "Managing product development lifecycle"

Q2: What's the main workflow?
    "Week 1-2: Research, Week 3-4: Build, Week 5+: Launch"

Q3: What docs/templates needed?
    [Options: Upload existing, link to previous Docgen output, create new]

Q4: What integrations?
    [Checkboxes: GitHub, Notion, Jira, Gmail, Slack, etc.]

Q5: How much should it remember?
    ○ Everything (full memory)
    ○ Key decisions only
    ○ None (stateless)

Q6: Example workflow?
    "User: 'Let's build a PRD'
     Claude: [Guides through questions, generates PRD]
     User: [Reviews, asks questions]
     Claude: [Refines]"

[Generate project package]
```

---

## Summary

| Question | Skill | Project |
|----------|-------|---------|
| **Reusable?** | Yes (library) | No (project-specific) |
| **Persistent?** | No | Yes |
| **Tools?** | Limited | Rich (MCP) |
| **Memory?** | No | Yes (optional) |
| **When to build?** | For focused task | For complete workflow |
| **Output format** | skill-name.md + metadata | PROJECT_INSTRUCTIONS + config |

**Both valuable. Different purposes. Both in Docgen.**

---

**Next: Build questionnaires for both (9th and 10th main projects)**
