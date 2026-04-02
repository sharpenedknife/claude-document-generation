# Docgen: Complete 10 Main Projects

**Updated:** All 10 main projects (choose 1 or none)

---

## All 10 Main Projects at a Glance

| # | Project | Docs Generated | Time | Use Case |
|---|---------|-----------------|------|----------|
| 1 | Fast Product MVP | PRD, UX, specifiers | 2h | Building MVP |
| 2 | Feature Release | PRD, UX, specifiers, safety | 2.5h | Shipping feature |
| 3 | Workflow Automation | Process docs, Dev plan, safety | 2h | Automating processes |
| 4 | Revenue Stream | Monetization, pricing, business model | 1.5h | Adding revenue |
| 5 | Brand Marketing | Brand, messaging, positioning, voice | 2h | Brand identity |
| 6 | Product Marketing | All of 5 + ICPs, competitive landscape, GTM | 2.5h | Go-to-market |
| 7 | Custom Files Summarize | Executive summary, extracted specs, gaps | 30m | Understanding docs |
| 8 | Custom Documentation | Whatever user describes | Variable | Anything else |
| **9** | **AI Skill Generator** | **Skill definition, triggers, implementation, examples** | **1.5h** | **Creating reusable Claude skills** |
| **10** | **Claude Project Generator** | **Project Instructions, welcome, memory, integrations** | **2h** | **Creating custom Claude Projects** |

---

## New: Project 9 - AI Skill Generator

**Purpose:** Create reusable Claude skills (work across conversations)

### Questionnaire
```
Q1: What does your skill do?
Q2: Who's the user?
Q3: When should it trigger?
Q4: What's the output format?
Q5: Main process steps?
Q6: Example usage?
Q7: Related skills?
```

### Generates (5 files)
```
1. [skill-name].md
   - Definition, purpose, when to use, examples
   
2. trigger-patterns.md
   - Pattern matching rules, activation logic
   
3. implementation-guide.md
   - Input/output, parameters, integration
   
4. examples.md
   - 3-5 detailed usage examples
   
5. related-skills.md
   - Companion skills, workflows, chains
```

### Output Quality
- All files pass 5 exit gates
- Reusable (can be added to Claude library)
- Triggered automatically by pattern matching
- Works in any conversation

**Example:**
```
Skill: customer-research
Triggers: "I need to research customers" / "user interviews" / "market feedback"
Output: Structured research document with findings & synthesis
```

---

## New: Project 10 - Claude Project Generator

**Purpose:** Create custom Claude Projects (dedicated workspaces)

### Questionnaire
```
Q1: What's this project for?
Q2: What's the main workflow?
Q3: What docs/templates needed?
Q4: What tool integrations?
Q5: Should it remember things?
Q6: Example interaction?
Q7: Team size?
Q8: Project duration?
```

### Generates (5 files)
```
1. PROJECT_INSTRUCTIONS_[name].md
   - System message, role, capabilities, commands
   
2. welcome-message.md
   - First message user sees
   
3. conversation-examples.md
   - Sample interactions & workflows
   
4. mcp-integrations.md
   - Tool setup, OAuth, API examples
   
5. memory-system.md
   - What to remember, how long, structure
```

### Output Quality
- All files pass 5 exit gates
- Project-specific (can't be reused)
- Deployed directly to Claude Projects
- Can reference generated docs from other projects

**Example:**
```
Project: Product Development Hub
References: PRD, UX Requirements, specifiers
Integrations: GitHub, Notion, Jira
Memory: Remembers key decisions, context
Duration: 3 months
```

---

## Key Difference: Skill vs Project

| Skill | Project |
|-------|---------|
| Reusable across conversations | Specific to one project |
| Triggered by patterns | Always available in project |
| Focused task | Broad workflow |
| No memory | Persistent memory |
| Works in any context | Project-only |
| Add to library | Deploy as workspace |

---

## Integration: Product → Skill → Project

### Workflow Example

```
STEP 1: Create Product Docs (Project 1: Fast Product MVP)
────────────────────────────────────────────────────────
Generates: PRD, UX, specifiers
Delivered: Zip + Notion


STEP 2: Create Skill for Extracting Insights (Project 9)
────────────────────────────────────────────────────────
Input: "I need a skill that extracts key insights from product docs"

Generates: 
  • customer-insights-extractor skill
  • Triggered by: "extract insights", "what matters most"
  • Output: Structured insights document
  
Delivered: Zip (can be added to Claude library)


STEP 3: Create Project to Manage Product (Project 10)
──────────────────────────────────────────────────────
Input: "Create project for managing this product"

Generates:
  • PROJECT_INSTRUCTIONS_ProductHub.md
  • References: PRD, UX, specifiers from Step 1
  • Integrations: GitHub, Notion, Jira
  • Memory: Enabled
  
User then:
  → Copy PROJECT_INSTRUCTIONS into Claude Projects
  → Connect MCP tools
  → Project runs with your PRD, UX, specs baked in
  → Can trigger customer-insights-extractor skill when needed


Result:
  ✓ Product docs created
  ✓ Reusable skill for insights
  ✓ Dedicated project to manage it
  ✓ All integrated, everything passes quality gates
```

---

## Complete User Flow (All 10 Projects)

```
User enters Docgen

Welcome: "What would you like to create?"

Options:
  1-8: Product-related (docs, marketing, revenue, etc.)
  9: Create a reusable skill
  10: Create a custom project
  (Or describe what you need)

Path A: User picks "1" (Fast Product MVP)
  → Generate PRD, UX, specifiers
  → Can then add workflows (Coding, Marketing, etc.)
  → Deliver to Zip, GitHub, Notion, Drive
  → User has product docs

Path B: User picks "9" (AI Skill)
  → Answer questions about skill
  → Generate skill package (5 files)
  → Reusable in any context
  → Add to Claude library

Path C: User picks "10" (Claude Project)
  → Answer questions about project
  → Optionally link to docs from Path A
  → Generate project instructions + setup
  → Deploy as custom Claude Project

Path D: User does Path A, then Path C
  → Create product docs
  → Create project to manage them
  → Project has docs embedded/referenced
  → Everything integrated
```

---

## Technical Implementation

**All 10 projects follow same pattern:**
1. Welcome message shows all 10
2. User picks 1
3. Contextual questions
4. Generate files
5. Run 5 quality gates
6. Choose output destination
7. Deliver + summarize

**New elements for Projects 9 & 10:**
- Skill projects check: trigger patterns valid, examples work
- Project projects check: instructions clear, integrations feasible, memory system sound
- Both check: can they reference other generated docs?

---

## Success Criteria (Complete System)

✅ User can create **any** of 10 project types  
✅ Each project type generates correct docs  
✅ All docs pass 5 exit quality gates  
✅ Output to 5+ destinations  
✅ Skills are reusable  
✅ Projects can reference other docs  
✅ Everything is AI-readable for Claude  

When all ✅, system complete.

---

## Summary

**10 Main Projects:**
- **1-6:** Product-related (MVP, features, monetization, marketing)
- **7-8:** Utilities (summarize, custom)
- **9-10:** Meta-documentation (skills, projects)

**Can combine:**
- Any main project (1)
- With 0-2 workflows
- To any output destination
- Creating 3-15 final documents

**Result:**
- Complete product documentation
- Reusable skills
- Custom Claude Projects
- All production-ready

---

**10 projects. 1 decision tree. Infinite combinations. Everything in Docgen.**
