# DOCGEN: Final Implementation Specification

**What we're building:** Claude Project with decision tree chat interface + CLI backend

---

## Welcome Message (Project Instructions)

This is the first message user sees when entering the Docgen project.

### Strategy: Make it Clear, Friendly, Actionable

```
👋 Welcome to Docgen!

I help you generate comprehensive product documentation 
in 30 minutes to 2 hours — starting from your idea, 
existing materials, or both.

What would you like to create?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 NEW PROJECT (Main Project Options)

1️⃣  📊 Fast Product MVP
   PRD + UX + Technical Specs
   Perfect for: Building MVP in 4-6 weeks
   Time: 2 hours

2️⃣  🚀 Feature Release
   Add to existing product with safety review
   Perfect for: Shipping new feature
   Time: 2.5 hours

3️⃣  ⚙️  Workflow Automation
   Automate internal processes
   Perfect for: Engineering & operations
   Time: 2 hours

4️⃣  💰 Revenue Stream
   Pricing + monetization strategy
   Perfect for: Monetizing your product
   Time: 1.5 hours

5️⃣  🎨 Brand Marketing
   Brand identity + messaging
   Perfect for: Building brand from scratch
   Time: 2 hours

6️⃣  📢 Product Marketing
   Full go-to-market strategy
   Perfect for: Launching product
   Time: 2.5 hours

7️⃣  📄 Summarize Existing Files
   Extract insights from your docs
   Perfect for: Understanding existing materials
   Time: 30 minutes

8️⃣  🎯 Custom Documentation
   Describe what you need, I'll generate it
   Perfect for: Anything not listed above
   Time: 1-2 hours (variable)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Or just tell me what you're building, and I'll guide you.

Examples:
• "I'm building an API for payment processing"
• "I want to launch my SaaS next month"
• "I need to document our current architecture"
• "Help me think through pricing"

**Type a number (1-8) or describe your project:**
```

---

## Chat Flow (After User Responds)

### Path 1: User Picks Main Project (e.g., "1")

```
You: "1"

Docgen:
Q1: What's your product?
[Text input]

You: "A real-time collaboration tool for teams"

Docgen:
Q2: Who's your target user?
[Text input]

You: "Product teams at 10-100 person startups"

Docgen:
Q3: What problem does it solve?
[Text input]

You: "Too much time in meetings, not enough async collaboration"

[Continue with 3-5 more clarifying questions]

Docgen:
📋 Generating documentation based on your answers...
   
   Selected:
   ✓ PRD (Product Requirements Document)
   ✓ UX Requirements (User Flows + Wireframes)
   ✓ specifiers.md (Tech Stack + Architecture)
   
   Time estimate: 2 hours
   
   Want to add additional workflows? (0-2 allowed)
   
   Additional Workflows:
   ○ API Reference
   ○ Monetization
   ○ Coding
   ○ Marketing
   ○ Custom Files Summarize
   ○ Custom Context Docs
   ○ No, generate main project only
```

### Path 2: User Picks Workflow (e.g., adds "Marketing")

```
You: "Yes, add Marketing workflow"

Docgen:
Which marketing docs do you want?

Select all that apply:
☑ Messaging (value prop, tagline)
☑ Positioning (market position, differentiation)
☑ Branding (voice, visual identity)
☑ ICPs & Personas (target customers, buyers)
☐ Competitive Landscape (requires research API)
☐ Growth & CRO (growth loops, retention)
☐ Market Assessment (TAM, market sizing - requires research)

You: [Check boxes]

Docgen:
✓ Selected 4 marketing documents

⚠️  Competitive Landscape requires market research API calls.
   This will take 5-10 mins and may have costs.
   
   Include it?
   ○ Yes, full research
   ○ No, skip
   ○ Basic outline only (no research)

You: "No, skip"

Docgen:
✓ Ready to generate 7 documents total!
  • 3 from Fast Product MVP
  • 4 from Marketing workflow

Can I generate these now?
[Yes, Generate] [No, Review First] [Change Options]
```

### Path 3: Permission Gates

```
Docgen:
? Generate Competitive Landscape with market research?
  (This will use API credits and take ~10 mins)
  
  ○ Yes, fully researched
  ○ No, basic outline only
  ○ Skip entirely
  
You: "Yes, fully researched"

[Docgen calls research APIs, shows progress]
⏳ Researching competitors...
⏳ Analyzing market position...
⏳ Generating landscape doc...
✓ Complete

Docgen:
? Choose output destinations (1 or more):

☑ Zip File (download .zip)
☑ GitHub (push to repo)
☑ Notion (create pages)
☑ Google Drive (create folder)
☐ Email (send links + zip)

You: [Select destinations]

Docgen:
? GitHub repository?
  (e.g., username/product-docs)
  
You: "mycompany/api-platform"

Docgen:
? Notion workspace?
  [OAuth: Sign in with Google]

[User authorizes]

Docgen:
? Google Drive folder?
  [OAuth: Sign in with Google]

[User selects folder: My Drive > Docs]
```

### Path 4: Generation & Results

```
Docgen:
⏳ Generating 7 documents...

Gate 1 (Validation): ✓ All valid
Gate 2 (Structure): ✓ All sections present
Gate 3 (Content): ✓ Clear & accurate
Gate 4 (Quality): ✓ Human + AI review passed
Gate 5 (Shipping): ✓ Ready to deliver

📦 Delivering to destinations...

✓ Zip File created: docgen_output_20260402_1830.zip
✓ GitHub: Pushed to main branch (12 files)
✓ Notion: Created "Docgen Output" workspace (12 pages)
✓ Google Drive: Uploaded to Docs folder (12 files)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SUMMARY

Generated Documents (7 total):
✅ PRD (89/100)
✅ UX Requirements (92/100)
✅ specifiers.md (85/100)
✅ Messaging (88/100)
✅ Positioning (90/100)
✅ Branding (86/100)
✅ ICPs & Personas (87/100)

Status: All Production Ready ✓

📍 Available at:
  • Download: [Zip link]
  • GitHub: github.com/mycompany/api-platform
  • Notion: [Workspace link]
  • Google Drive: [Folder link]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Steps:
1. ✅ Review docs in Notion / GitHub / Drive
2. 👥 Share with your team
3. 💻 Start implementation

Any questions about the docs?
You can:
  • Ask for clarification on specific documents
  • Request regeneration with different options
  • Create additional documents
  • Start over with a new project

What would you like to do?

[View PRD] [View UX] [Create Another Project] [Done]
```

---

## Implementation: 3 Parts

### Part 1: Chat Interface (Project Instructions)

**File:** `PROJECT_INSTRUCTIONS_Docgen_Chat.md`

**Size:** 2000-2500 words (fits Project Instructions limit)

**Content:**
- Welcome message (above)
- Decision tree logic
- Clarifying questions for each path
- Permission gate handling
- Output destination selection
- Routes to CLI commands

**How it works:**
1. User enters chat
2. Sees welcome message + menu
3. Picks option (1-8) or describes project
4. Docgen asks clarifying questions
5. Shows selected documents summary
6. Asks for permissions (if needed)
7. Selects output destinations
8. Triggers CLI: `docgen create [PROJECT] [WORKFLOWS]`
9. Shows results + summary

---

### Part 2: CLI Backend (Python)

**What it does:**
- Receives project + workflow selections from Project Instructions
- Generates docs via questionnaire data
- Runs 5 exit gates
- Delivers to destinations (Zip, GitHub, Notion, Drive)

**Code structure:**
```
code/
├── cli/
│   └── main.py
│       @click.command()
│       def generate_docs(project, workflows, destinations):
│           # 1. Map project → doc templates
│           # 2. Populate with answers
│           # 3. Run 5 gates
│           # 4. Deliver to destinations
│           # 5. Return summary
│
├── generators/
│   ├── prd_generator.py
│   ├── ux_generator.py
│   ├── monetization_generator.py
│   └── [others per workflow]
│
├── destinations/
│   ├── zip_handler.py
│   ├── github_handler.py
│   ├── notion_handler.py
│   └── google_drive_handler.py
│
└── gates/
    └── validator.py (runs 5 gates)
```

---

### Part 3: Welcome Message Management

**In Claude Projects, welcome message is set in Project Instructions:**

```
In PROJECT_INSTRUCTIONS_Docgen_Chat.md:

---
**SYSTEM MESSAGE (shown on project entry):**

👋 Welcome to Docgen! [see above]

---
```

**How to update welcome:**
1. Edit `PROJECT_INSTRUCTIONS_Docgen_Chat.md`
2. Update the welcome section
3. Publish to project
4. Takes effect immediately for new sessions

**Dynamic elements:**
```
Can include:
✓ Emoji & formatting
✓ Links
✓ Buttons/interactive elements (via Markdown)
✓ User context (name, timezone, etc.)
✗ Real-time data (pull from APIs)
```

**Best practice:**
```
1. Keep welcome short (2-3 bullet points)
2. Show 8 main options clearly
3. Include "Or describe..." for flexibility
4. Link to docs/examples
5. Set clear expectations (time, output format)
```

---

## Implementation Timeline

**Phase 1: Chat Interface (2 hours)**
- Write PROJECT_INSTRUCTIONS_Docgen_Chat.md
- Test decision tree logic in chat
- Verify all paths work

**Phase 2: CLI Backend (6 hours)**
- Build generators for each project type
- Implement destination handlers (Zip, GitHub, Notion, Drive)
- Connect chat → CLI command execution
- Test end-to-end

**Phase 3: Integration (2 hours)**
- Chat → CLI communication
- Results back to chat
- Quality gates verification
- Error handling

**Total: ~10 hours to fully working system**

---

## Testing Checklist

- [ ] Welcome message displays correctly
- [ ] All 8 main options work
- [ ] Clarifying questions flow naturally
- [ ] Permissions gates work (yes/no/partial)
- [ ] Destination selection works (1+ picks)
- [ ] GitHub OAuth connects
- [ ] Notion OAuth connects
- [ ] Google Drive OAuth connects
- [ ] Zip file generates correctly
- [ ] All 5 gates run and pass
- [ ] Results summary shows quality scores
- [ ] User can regenerate with different options
- [ ] Custom doc generation works (free text input)

---

## Success Criteria

✅ User enters → sees welcome message  
✅ User picks option → gets clarifying questions  
✅ User answers → documents generate  
✅ User approves permissions → docs delivered  
✅ User receives docs in 1+ locations  
✅ All docs pass 5 exit gates  
✅ User gets summary + next actions  

When all ✅, system is complete.

---

## Next: Build It

1. **Today:** Write PROJECT_INSTRUCTIONS_Docgen_Chat.md (2 hours)
2. **Tomorrow:** Build CLI backend (6 hours)
3. **Next day:** Integration + testing (2 hours)

10 hours → Complete, working Docgen system.
