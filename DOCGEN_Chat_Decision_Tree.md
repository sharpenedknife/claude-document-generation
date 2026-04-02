# DOCGEN: Chat Decision Tree Logic

**Purpose:** User navigates menu → selects project + workflows → chooses output → generates docs

---

## Step 1: Main Project (Choose 1 or None)

User picks **exactly 1** main project or skips to workflows only.

| Project | Docs Generated | Time | Use Case |
|---------|---------------|------|----------|
| **Fast Product MVP** | PRD, UX, specifiers.md | 2h | Building MVP fast |
| **Feature Release** | PRD, UX, specifiers.md, safety.md | 2.5h | Shipping new feature |
| **Workflow Automation** | Dev Plan, Process Docs, Safety | 2h | Automating internal processes |
| **Revenue Stream** | Monetization, Pricing, Business Model | 1.5h | New revenue model |
| **Brand Marketing** | Brand Guidelines, Messaging, Positioning, Voice | 2h | Brand identity |
| **Product Marketing** | Messaging, Positioning, ICPs, Competitive Landscape, Go-to-Market | 2.5h | Launch strategy |
| **Custom Files Summarize** | Summary doc + extracted key points | 30m | Understand existing materials |
| **Custom Context Project** | User describes → docgen generates custom docs | Variable | Whatever you need |
| **(Skip)** | — | — | Jump to workflows only |

---

## Step 2: Workflows (Choose 0-2 Additional)

User can pick **0, 1, or 2** additional workflows beyond main project.

Each workflow = set of docs.

### Workflow Set 1: API Reference
```
Generates:
  • API specification (endpoints, parameters, responses)
  • Authentication guide
  • Error codes & handling
  • Rate limiting docs
  
Input: Ingest existing API, codebase, or describe
Time: 1.5h
```

### Workflow Set 2: Monetization
**User chooses subitems (can pick multiple):**

```
☑ Project Budgeting
    • Cost breakdown
    • Resource allocation
    • Runway calculation
    • Financing needs
    Time: 1h

☑ Pricing & Subscriptions
    • Pricing tiers (Free/Pro/Enterprise)
    • Feature matrix
    • Packaging strategy
    • Revenue projections
    Time: 1h
```

### Workflow Set 3: Coding
**User chooses subitems:**

```
☑ Development Plan
    • Sprint breakdown (Week 1-4, 1-12, etc.)
    • Task list by feature
    • Dependencies & blockers
    • Timeline + milestones
    Time: 1.5h

☑ PRD File
    • Product requirements document
    • Features & acceptance criteria
    • Success metrics
    • Edge cases & error handling
    Time: 1h

☑ Frontend UI Requirements
    • Component library specs
    • Responsive breakpoints
    • Interaction states
    • Accessibility requirements
    Time: 1h

☑ UX Requirements
    • User flows & journeys
    • Wireframe descriptions (no images)
    • Information architecture
    • User testing criteria
    Time: 1h
```

### Workflow Set 4: Marketing
**User chooses subitems (can pick multiple or all):**

```
☑ Messaging
    • Value proposition
    • Key messaging pillars
    • Tagline
    • Elevator pitch
    Time: 45m

☑ Positioning
    • Market position
    • Competitive advantage
    • Differentiation
    • Positioning statement
    Time: 45m

☑ Branding
    • Brand voice guidelines
    • Visual identity specs
    • Brand personality
    • Brand story
    Time: 1h

☑ ICPs & Personas
    • Ideal Customer Profile
    • Buyer personas (3-5)
    • Psychographics
    • Decision-making process
    Time: 1h

☑ Competitive Landscape
    • Direct competitors
    • Indirect competitors
    • Feature comparison
    • Market gaps
    Time: 1h
    [OPTIONAL: Asks permission for research API calls]

☑ Growth & CRO
    • Growth loops
    • Conversion optimization targets
    • Retention strategies
    • Viral mechanics
    Time: 1h

☑ Market Assessment
    • Total addressable market (TAM)
    • Market trends
    • Entry strategy
    • Market timing
    Time: 1h
    [OPTIONAL: Asks permission for research API calls]
```

### Workflow Set 5: Custom Files Summarize
```
User uploads/links:
  • Existing docs
  • PDFs
  • Competitor materials
  • Market research
  
Docgen:
  • Extracts key points
  • Generates summary doc
  • Identifies gaps
  • Suggests next steps
  
Time: 30m
```

### Workflow Set 6: Custom Context Docs
```
User describes:
  "I need a technical architecture document for 
   distributed payment processing system"
  
Docgen:
  • Asks follow-up questions (audience, scope, constraints)
  • Generates custom document
  • Runs quality gates
  
Time: Variable (1-2h)
```

---

## Permission Gates (For Optional Steps)

**When generating docs that require research/API calls:**

```
? "Competitive Landscape" requires market research API calls
  This may take 5-10 mins and incur costs.
  
  Generate? 
  ○ Yes, generate fully researched doc
  ○ No, skip (I'll provide my own)
  ○ Partial (basic outline, no research)
```

**Same for:**
- Market Assessment
- Competitive Landscape
- ICPs & Personas (if research-based)

---

## Step 3: Output Destination

User chooses **1 or more** where to send generated docs:

```
Where should docs go?

☑ Zip File (download locally)
☑ GitHub (create repo + push)
☑ Notion (create workspace + pages)
☑ Google Drive (create folder + upload)
☑ Email (send zip + links)

Choose at least 1.
```

**Implementation:**
- Zip: Always works
- GitHub: Ask for repo URL
- Notion: Ask for workspace API key
- Google Drive: Ask for drive folder link
- Email: Ask for recipient email

---

## Complete Flow Example

```
User: "I'm building a SaaS API platform"

→ Step 1: Main Project
   ? What's your main focus?
   User: "Fast Product MVP"
   Generates: PRD, UX, specifiers.md

→ Step 2: Additional Workflows?
   ? Want to add up to 2 more workflows?
   
   User: "Yes"
   
   Workflow 1: Coding
     ? Which coding docs?
     ☑ Development Plan
     ☑ UX Requirements
   
   Workflow 2: Marketing
     ? Which marketing docs?
     ☑ Messaging
     ☑ Positioning
     ☑ ICPs & Personas
     
     ? ICPs require research. Generate?
     User: "Yes"
     [Docgen researches market, generates docs]

→ Step 3: Output?
   ? Where should docs go?
   ☑ Zip File
   ☑ GitHub (repo: github.com/user/api-platform)
   ☑ Notion (workspace: notion.so/myworkspace)

→ Generation
   ⏳ Generating 11 documents...
   ✓ All 11 docs ready
   
→ Delivery
   ✓ Zip created: docgen_output.zip (2.3MB)
   ✓ GitHub: Pushed to main branch
   ✓ Notion: Created folder "API Platform Project"

→ Summary
   Generated docs:
   • PRD
   • UX Requirements
   • specifiers.md
   • Development Plan
   • Messaging
   • Positioning
   • ICPs & Personas
   • Competitive Landscape (researched)
   
   Quality scores: All ✓ PRODUCTION READY
   
   Next?
   [View Summary] [Download Zip] [View GitHub] [Open Notion] [Done]
```

---

## Chat Logic (Project Instructions)

**Welcome:**
```
Welcome to Docgen!

I help you generate comprehensive product documentation 
from zero (or existing materials).

What would you like to create?

1. 📊 Fast Product MVP
2. 🚀 Feature Release
3. ⚙️ Workflow Automation
4. 💰 Revenue Stream
5. 🎨 Brand Marketing
6. 📢 Product Marketing
7. 📄 Summarize Existing Files
8. 🎯 Custom Documentation
9. ⏭️ Skip to Workflows Only

(Or just describe what you need)
```

**Menu Navigation:**
- User picks option → Clarifying questions
- Questions answered → Show selected docs summary
- User confirms → Generate
- Ask permissions for research steps
- Choose output destination
- Generate + deliver

---

## Edge Cases (User Can)

- **Pick same doc twice:** No (system prevents)
- **Pick conflicting workflows:** Yes (Marketing + Custom Context both allowed)
- **Change mind mid-flow:** Yes (go back to previous step)
- **Skip research:** Yes (Permission gate handles this)
- **Provide own materials:** Yes (Upload/link to Workflow: Custom Files Summarize)
- **Get partial docs:** Yes (User can pick specific subitems)

---

## Success Criteria

✓ User completes decision tree  
✓ User approves/skips research steps  
✓ All selected docs generated  
✓ Quality gates pass (or show failures)  
✓ Files delivered to chosen destinations  
✓ User gets summary + next actions  

---

**Next: Implementation specs for each main project + workflow.**
