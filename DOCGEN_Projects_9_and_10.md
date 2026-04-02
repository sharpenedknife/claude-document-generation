# Docgen: Main Projects 9 & 10

## Project 9: AI Skill Generator

**Time:** 1.5 hours  
**Best for:** Creating reusable Claude skills  
**Input:** Skill purpose + trigger conditions + examples  
**Reusable:** Yes (across all conversations)

### Documents Generated

#### 1. Skill Definition ([skill-name].md)
```yaml
Sections:
  - Skill name & tagline
  - Purpose (what it does)
  - When to use (trigger conditions)
  - Scope & boundaries
  - Capabilities
  - Limitations
  - Example usage (3-5 examples)
  - Output format
  - Related skills

AI-readable for: Claude to understand when/how to use skill
```

#### 2. Trigger Patterns (trigger-patterns.md)
```yaml
Sections:
  - Pattern matching rules
    - Keywords: ["customer research", "user interviews", "market research"]
    - Phrases: ["I need to understand", "Help me analyze"]
    - Context: [user is product manager, founder, marketer]
  - Activation rules
    - Automatic trigger conditions
    - Manual trigger phrases
    - Fallback behavior
  - Confidence scoring (how certain to activate)
  
AI-readable for: Pattern matching logic
```

#### 3. Implementation Guide (implementation-guide.md)
```yaml
Sections:
  - Input parameters (what user provides)
  - Process steps (how skill executes)
  - Output structure (what skill returns)
  - Error handling
  - Validation rules
  - Integration points
  - Dependencies

AI-readable for: Developers integrating skill
```

#### 4. Usage Examples (examples.md)
```yaml
Sections:
  - Example 1:
    User: "I need to research customer needs"
    Skill response: [detailed example]
    
  - Example 2:
    User: "Help me conduct user interviews"
    Skill response: [detailed example]
    
  - Example 3:
    User: "Analyze what our customers want"
    Skill response: [detailed example]

AI-readable for: Understanding expected behavior
```

#### 5. Related Skills (related-skills.md)
```yaml
Sections:
  - Companion skills (work together)
  - Prerequisite skills (learn first)
  - Alternative skills (when to use instead)
  - Workflow chains (how to combine)

Example:
  This skill: customer-research
  Works with: competitive-analysis, market-sizing, personas
  Chain: customer-research → competitive-analysis → positioning
```

### Questionnaire

```
Q1: What's your skill about?
    "Help users research customer needs through interviews and surveys"

Q2: Who's the user?
    "Product managers, founders, UX researchers"

Q3: When should it trigger automatically?
    "When user mentions: customer research, interviews, feedback collection"

Q4: What's the output?
    "Structured research document with: findings, key insights, 
     synthesis, next steps"

Q5: What's the main process?
    "1. Ask what they want to research
     2. Guide them through research methods
     3. Help conduct interviews/surveys
     4. Synthesize findings
     5. Deliver structured report"

Q6: Give an example:
    User input: "I need to understand why customers churn"
    Skill output: [Type your expected response...]

Q7: Related skills to mention?
    "Competitive analysis, personas, retention strategy"

[Generate skill package (5 files)]
```

---

## Project 10: Claude Project Generator

**Time:** 2 hours  
**Best for:** Creating custom Claude Projects  
**Input:** Project purpose + workflow + tools + docs  
**Scope:** Project-specific (not reusable)

### Documents Generated

#### 1. Project Instructions (PROJECT_INSTRUCTIONS_[name].md)
```yaml
Sections:
  - System message (Claude's role in this project)
  - Purpose & scope
  - Capabilities (what Claude can do)
  - Limitations (what Claude can't do)
  - Available commands/workflows
  - Success criteria
  - How memory works (if enabled)
  - Tool integrations available
  
AI-readable for: Claude running the project
```

#### 2. Welcome Message (welcome-message.md)
```yaml
Content:
  - Friendly greeting
  - What this project is for
  - What user can ask
  - Example commands/requests
  - How to get help
  - Quick start guide
  
Display: First message user sees on project entry
```

#### 3. Conversation Examples (conversation-flow-examples.md)
```yaml
Sections:
  - Example conversation 1:
    Interaction 1:
      User: [request]
      Claude: [response with structure]
    Interaction 2:
      User: [follow-up]
      Claude: [refined response]
    
  - Example conversation 2:
    [Different workflow example]
    
  - Example conversation 3:
    [Error case example]

AI-readable for: Understanding expected conversation patterns
```

#### 4. MCP Integrations (mcp-integrations.md)
```yaml
Sections:
  - Required MCP servers:
    - GitHub: [permissions needed, example usage]
    - Notion: [permissions needed, example usage]
    - Jira: [permissions needed, example usage]
  
  - Setup instructions:
    For each tool:
      - How to connect (OAuth steps)
      - Permissions to grant
      - What each permission allows
      - Troubleshooting
  
  - Example API calls:
    GitHub: [example commands]
    Notion: [example commands]
    Jira: [example commands]

AI-readable for: Using tools effectively
```

#### 5. Memory System (memory-system.md)
```yaml
Sections:
  - What to remember:
    - User's goals
    - Key decisions made
    - Project context
    - Preferences
  
  - Memory structure:
    - How information is organized
    - Tags/categories
    - Relationships
  
  - Update frequency:
    - When memory updates
    - What triggers saves
    - Retention period
  
  - User preferences:
    - How to handle memory
    - Privacy settings
    - What NOT to remember

AI-readable for: Memory system operation
```

### Questionnaire

```
Q1: What's this project for?
    "Manage product development from idea to launch"

Q2: What's the primary workflow?
    "Week 1-2: Research & discovery
     Week 3-4: Build PRD & UX
     Week 5-6: Plan development
     Week 7+: Execution & launch"

Q3: What documents/templates needed?
    Options:
    ○ Create from scratch (answer more questions)
    ○ Link to previous Docgen outputs
    ○ Upload existing documents
    
    User: "Link to my Fast Product MVP output"
    [Docgen loads PRD, UX, specifiers]

Q4: What tools to integrate?
    [Checkboxes]
    ☑ GitHub (code management)
    ☑ Notion (documentation)
    ☑ Jira (task tracking)
    ☐ Slack (team communication)
    ☐ Gmail (email)
    
Q5: Should it remember things?
    ○ Yes, full memory (remembers all decisions, context)
    ○ Partial memory (key decisions only)
    ○ No memory (stateless, each session fresh)
    
    User: "Yes, full memory"

Q6: Example workflow in this project?
    Describe interaction you want to support:
    "User: 'Let's start with research phase'
     Claude: [Guide through research process]
     User: [Provides findings]
     Claude: [Synthesizes, suggests next]"

Q7: Team size using this?
    "3-5 people"

Q8: Project duration?
    "3 months"

[Generate project package (5 files)]
```

---

## Integration: Product → Project Flow

### Scenario: User builds product, then creates project

```
STEP 1: Generate Product Docs
───────────────────────────────

User: "1" (Fast Product MVP)
[Answers 5 questions]
Result: PRD.md, UX_Requirements.md, specifiers.md

Output options: Zip, GitHub, Notion, Drive
User selects: Zip + Notion

Files delivered to Notion workspace.


STEP 2: Generate Claude Project for Those Docs
──────────────────────────────────────────────

User (in same chat): "Now create a Claude Project to manage this"

Docgen:
  "Great! I can create a Project that uses the docs you just generated.
   
   Q1: What's the project for?
   User: 'Managing product development'
   
   Q2: Should it use the PRD, UX, and specs you just created?
   User: 'Yes'"

Docgen shows:
  "Ready to generate Project Instructions for:
   
   ✓ Product Management Hub
   ✓ Uses: PRD, UX Requirements, specifiers
   ✓ Tools: GitHub, Notion, Jira
   ✓ Memory: Enabled
   ✓ Team: 3-5 people
   
   Generate?"

User: "Yes"

Result:
  - PROJECT_INSTRUCTIONS_ProductManagementHub.md
  - welcome-message.md
  - conversation-examples.md
  - mcp-integrations.md
  - memory-system.md

Output: Zip file (or direct to GitHub, Notion)

User then:
  1. Copy PROJECT_INSTRUCTIONS into Claude Projects
  2. Connect MCP tools (GitHub, Notion, Jira)
  3. Project live, ready to use

```

---

## Technical: How Projects Reference Docs

**Project Instructions can reference generated docs:**

```
In PROJECT_INSTRUCTIONS_ProductManagementHub.md:

You have access to these documents:

📄 PRD: [Embedded or linked]
  Purpose: Product requirements
  Last updated: 2026-04-02
  
📄 UX Requirements: [Embedded or linked]
  Purpose: User flows and specs
  Last updated: 2026-04-02
  
📄 Technical Specs: [Embedded or linked]
  Purpose: Architecture and tech stack
  Last updated: 2026-04-02

When user asks "What's our timeline?", reference PRD.
When user asks "What's the user flow?", reference UX Requirements.
```

---

## File Size Comparison

### Skill Package
```
Total: ~150KB
  • skill-name.md: 20KB
  • trigger-patterns.md: 10KB
  • implementation-guide.md: 15KB
  • examples.md: 30KB
  • related-skills.md: 5KB
  • metadata.json: 2KB

Single file → use in any context
Focused → easy to understand
Reusable → across projects
```

### Project Package
```
Total: ~300KB (if includes docs)
  • PROJECT_INSTRUCTIONS.md: 80KB
  • welcome-message.md: 10KB
  • conversation-examples.md: 40KB
  • mcp-integrations.md: 30KB
  • memory-system.md: 20KB
  • embedded docs (PRD, UX, etc.): 120KB
  • metadata.json: 5KB

Complete package → import as-is
Complex → many components
Project-specific → not reusable
```

---

## Quality Gates

Both Skills and Projects run same 5 gates:

```
Gate 1: Validation
  ✓ YAML valid
  ✓ Required fields present
  ✓ Document type recognized

Gate 2: Structure
  ✓ All sections present
  ✓ Proper formatting
  ✓ Cross-references valid

Gate 3: Content Quality
  ✓ Clear & specific
  ✓ Examples provided
  ✓ Trigger patterns precise (for Skills)
  ✓ Memory system clear (for Projects)

Gate 4: Quality Metrics
  ✓ Token budget OK
  ✓ Quality score ≥ 80/100
  ✓ Checklists pass

Gate 5: Shipping Ready
  ✓ All gates passed
  ✓ Metadata complete
  ✓ Status = PRODUCTION_READY
```

---

## Summary Table

| Aspect | Skill (9th) | Project (10th) |
|--------|-----------|----------------|
| **Purpose** | Reusable task | Project environment |
| **Time** | 1.5h | 2h |
| **Main output** | skill-name.md | PROJECT_INSTRUCTIONS.md |
| **Can reference docs?** | No | Yes |
| **Standalone?** | Yes | Yes |
| **After product docs?** | Optional | Common |
| **Integration** | Pattern matching | Full environment |
| **Users** | Any Claude context | Project members |

---

**Both ready to implement. Same questionnaire flow as other projects.**
