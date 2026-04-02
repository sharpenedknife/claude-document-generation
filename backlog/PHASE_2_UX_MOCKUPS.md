# Phase 2 UX Mockups: Interactive Flows

Visual representation of how users will interact with docgen Phase 2.

---

## Flow 1: `docgen ingest` (Landing Page → Doc)

```
$ docgen ingest https://acme.com landing-page

⏳ Extracting content from acme.com...

✓ Extraction complete

┌────────────────────────────────────────────┐
│ EXTRACTED CONTENT FROM ACME.COM            │
├────────────────────────────────────────────┤
│                                            │
│ Title: Acme - Enterprise API Platform     │
│ Type: Developer platform                  │
│ Confidence: 82%                           │
│                                            │
│ Key sections found:                       │
│ • Product overview                        │
│ • Key features (REST, WebSocket, etc)    │
│ • Use cases                               │
│ • Pricing                                 │
│ • Target audience                        │
│ • Integration examples                    │
│                                            │
│ Extracted key points:                    │
│ ✓ Positioning: "Fastest, most reliable"  │
│ ✓ Features: [REST API, WebSocket, ...]   │
│ ✓ Audience: Enterprise developers        │
│ ✓ Use cases: [Real-time, Integration...] │
│                                            │
│ This looks like a good starting point.   │
│                                            │
├────────────────────────────────────────────┤
│ [Accept] [Edit] [Retry] [Cancel]         │
└────────────────────────────────────────────┘

→ User selects: [Accept]

? What type of document should this become?

  ○ API Reference
  ○ GTM Strategy
  ○ Feature Guide
  ○ Product Specification
  ○ Competitive Analysis
  ○ Design Guide
  ○ Other

→ User selects: API Reference

⏳ Generating API Reference using extracted content...
⏳ Running exit gates...

┌────────────────────────────────────────────┐
│ ✓ GATES PASSED                             │
├────────────────────────────────────────────┤
│                                            │
│ Document: Acme_API_Reference_v1.0         │
│                                            │
│ Quality Score: 89/100                     │
│ Tokens: 2,847 / 3,000 (budget OK)         │
│ Status: PRODUCTION READY                  │
│                                            │
│ Exit Gates:                               │
│ ✓ Gate 1: Validation passed              │
│ ✓ Gate 2: Structure valid                │
│ ✓ Gate 3: Content quality OK             │
│ ✓ Gate 4: Human+AI+Token passed          │
│ ✓ Gate 5: Ready to ship                  │
│                                            │
│ DEBT Summary (what's not included):       │
│ • P1: Authentication examples (P1.1)      │
│ • P1: Error codes reference (P1.2)        │
│ • P2: Webhooks guide (P2.1)               │
│ • P2: Rate limiting details (P2.2)        │
│                                            │
├────────────────────────────────────────────┤
│ Next action?                              │
│                                            │
│ [View Doc]   [Edit + Rerun]  [Delete]     │
│ [Confluence] [Jira Issues]    [GitHub]    │
│ [Keep Draft] [Done]                       │
└────────────────────────────────────────────┘

→ User selects: [Confluence]

? Post to Confluence

Space: [━━━━━━━━━━━━━━━━━] 
  APIs ↓
  - Developer Docs
  - Public API
  - Internal Tools

→ User selects: Developer Docs

Parent page: [━━━━━━━━━━━━━━━━━]
  None (root)
  - Getting Started
  - API Reference
  - Tutorials

→ User selects: API Reference

Labels: acme, api, reference
        [Add more]

Notify: [Search users...]
        [Product team]

Update existing page?
  ○ No, create new page
  ○ Yes, update existing

→ Selected: No, create new

Version: v1.0 ✓

┌────────────────────────────────────────────┐
│ PREVIEW: CONFLUENCE                        │
├────────────────────────────────────────────┤
│                                            │
│ Space: Developer Docs                     │
│ Parent: API Reference                     │
│ Title: Acme API Reference v1.0             │
│ Labels: acme, api, reference               │
│ Notify: Product team                       │
│                                            │
│ Content: [2,847 words, 12 sections]        │
│ Will be posted as: New page                │
│ URL: /wiki/spaces/DEVDOCS/pages/Acme...   │
│                                            │
├────────────────────────────────────────────┤
│ [Confirm & Post] [Cancel] [Edit Options]   │
└────────────────────────────────────────────┘

→ User selects: [Confirm & Post]

⏳ Posting to Confluence...

✓ Successfully posted!

Page URL: https://confluence.company.com/wiki/spaces/DEVDOCS/pages/12847/Acme_API_Reference

Document saved to: output/web_dev/v1.0/Acme_API_Reference_v1.0.md
DEBT file: output/web_dev/v1.0/Acme_API_Reference_v1.0.DEBT.md

Done!
```

---

## Flow 2: `docgen jira` (DEBT → Issues)

```
$ docgen jira ISSUES output/web_dev/v1.0/Acme_API_Reference_v1.0.md

Reading DEBT items from Acme_API_Reference_v1.0.DEBT.md...

Found 4 P1 items, 4 P2 items, 2 P3 items (10 total)

? Which items to create as Jira issues?

Issue type: Story ↓
  - Story
  - Task
  - Bug
  - Epic

→ Selected: Story

Create from:
  ☑ P1 items (4 issues)
    - [P1.1] Authentication examples
    - [P1.2] Error codes reference
    - [P1.3] Rate limiting guide
    - [P1.4] Webhook examples
  
  ☐ P2 items (4 issues)
    - [P2.1] SDKs documentation
    - [P2.2] Migration guide
    - [P2.3] Deprecation notice
    - [P2.4] Performance tips

  ☐ P3 items (2 issues)
    - [P3.1] Video tutorials
    - [P3.2] Example applications

Project: [━━━━━━━━━━━━━━━━━]
  Docs (DOCS)
  Products (PROD)
  Engineering (ENG)

→ Selected: DOCS

Sprint: [━━━━━━━━━━━━━━━━━]
  Sprint 47 (Current)
  Sprint 48 (Next)
  Backlog
  
→ Selected: Sprint 48

Assignee: [━━━━━━━━━━━━━━━━━]
  Unassigned
  @alice
  @bob
  @team-docs

→ Selected: @team-docs

Link to source doc?
  ☑ Yes, add Confluence link
  
Labels:
  api, acme, documentation
  [Add more]

┌────────────────────────────────────────────┐
│ PREVIEW: JIRA                              │
├────────────────────────────────────────────┤
│                                            │
│ Creating 4 stories in project DOCS         │
│                                            │
│ Story 1: [P1.1] Authentication examples    │
│ Description: "Add authentication examples" │
│ Assignee: @team-docs                       │
│ Sprint: Sprint 48                          │
│ Labels: api, acme, documentation           │
│ Linked: https://confluence.company.com/... │
│                                            │
│ Story 2: [P1.2] Error codes reference      │
│ [...]                                      │
│                                            │
│ Story 3: [P1.3] Rate limiting guide        │
│ [...]                                      │
│                                            │
│ Story 4: [P1.4] Webhook examples           │
│ [...]                                      │
│                                            │
│ Total: 4 stories will be created           │
│                                            │
├────────────────────────────────────────────┤
│ [Confirm & Create] [Cancel] [Edit Options]  │
└────────────────────────────────────────────┘

→ User selects: [Confirm & Create]

⏳ Creating issues in Jira...

✓ Successfully created 4 stories!

Stories created:
  • DOCS-247: [P1.1] Authentication examples
  • DOCS-248: [P1.2] Error codes reference
  • DOCS-249: [P1.3] Rate limiting guide
  • DOCS-250: [P1.4] Webhook examples

Sprint 48 updated with 4 new stories.
Team notified.

Done!
```

---

## Flow 3: `docgen prompt` (Generate → Embed)

```
$ docgen prompt "Generate prompt for extracting GTM from web content"

⏳ Building prompt for your task...

┌────────────────────────────────────────────┐
│ GENERATED PROMPT                           │
├────────────────────────────────────────────┤
│                                            │
│ System:                                    │
│ "You are a GTM analyst. Extract key GTM   │
│  elements from marketing content.          │
│  Return structured JSON with:              │
│  - positioning, target_market,             │
│  - key_differentiators, business_model,    │
│  - go_to_market_strategy"                  │
│                                            │
│ Parameters:                                │
│ • Temperature: 0.7 (balanced)              │
│ • Max tokens: 2000                         │
│ • Output format: JSON                      │
│                                            │
│ Example input:                             │
│ "Acme is the fastest API platform..."     │
│                                            │
│ Example output:                            │
│ {                                          │
│   "positioning": "Speed + Reliability",   │
│   "target_market": "Enterprise devs",     │
│   "key_differentiators": [                │
│     "Sub-100ms latency",                  │
│     "99.99% uptime",                      │
│     "Free tier available"                 │
│   ],                                       │
│   "business_model": "Freemium",           │
│   "gtm_strategy": "Developer-first"       │
│ }                                          │
│                                            │
├────────────────────────────────────────────┤
│ Quality: 92/100                            │
│ Tokens: 850 (est. for your input)         │
│                                            │
│ [Copy] [Embed in Chat] [Regenerate]       │
│ [Edit Manually] [Save as Skill]            │
└────────────────────────────────────────────┘

→ User selects: [Embed in Chat]

Copied to chat! Now paste your content and run this prompt:

╔════════════════════════════════════════════╗
║ PROMPT EMBEDDED IN CHAT                    ║
╠════════════════════════════════════════════╣
║                                            ║
║ System: "You are a GTM analyst. Extract    ║
║ key GTM elements from marketing content.   ║
║ Return structured JSON with:               ║
║ - positioning, target_market,              ║
║ - key_differentiators, business_model,     ║
║ - go_to_market_strategy"                   ║
║                                            ║
║ [Parameters: temp=0.7, tokens=2000]        ║
║                                            ║
║ Now paste content below:                   ║
║ [Content here]                             ║
║                                            ║
║ [Run Prompt]                               ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Flow 4: `docgen validate` (Run Gates)

```
$ docgen validate output/gtm/v1.0/GTM_Strategy_2026.md

⏳ Running exit gates on GTM_Strategy_2026.md...

┌────────────────────────────────────────────┐
│ GATE 1: VALIDATION                         │
├────────────────────────────────────────────┤
│ ✓ Frontmatter present                      │
│ ✓ YAML valid                               │
│ ✓ All 8 required fields present            │
│ ✓ doc_type is valid                        │
│ ✓ audience level valid                     │
│ ✓ title starts with action verb            │
│ ✓ overview is 2 sentences                  │
│ ✓ builder_session_id is unique             │
│                                            │
│ RESULT: ✓ PASS                             │
└────────────────────────────────────────────┘

⏳ Running Gate 2...

┌────────────────────────────────────────────┐
│ GATE 2: STRUCTURE                          │
├────────────────────────────────────────────┤
│ ✓ Title + Overview section                 │
│ ✓ Prerequisites section (Level 1-4)        │
│ ✓ Content sections present                 │
│ ✓ Expected Output section (table format)   │
│ ✓ Troubleshooting section                  │
│ ✓ Why This Matters section                 │
│ ✓ What's Next section (doc titles)         │
│ ✗ Error: Some cross-refs use URLs (fix:   │
│   convert to doc titles)                   │
│                                            │
│ RESULT: ⚠ PASS WITH WARNINGS               │
│ Action: Fix 3 URL references               │
└────────────────────────────────────────────┘

⏳ Running Gate 3...

┌────────────────────────────────────────────┐
│ GATE 3: CONTENT QUALITY                    │
├────────────────────────────────────────────┤
│ ✓ Overview explains what & why             │
│ ✓ All commands exact + testable            │
│ ✓ Expected output shown                    │
│ ✓ Errors have root cause + fix             │
│ ✓ Prerequisites realistic                  │
│ ✓ All links to resources (not homepage)    │
│ ✓ Cross-refs use doc titles                │
│ ✓ No unexplained acronyms                  │
│ ✓ No ambiguous pronouns                    │
│ ✓ Tone consistent                          │
│ ✗ Error: Vague phrase "configure properly" │
│   (Line 247)                               │
│ ✗ Error: No examples for 2 concepts        │
│                                            │
│ RESULT: ⚠ NEEDS WORK                       │
│ Actions: [Fix 2 issues]                    │
└────────────────────────────────────────────┘

⏳ Running Gate 4...

┌────────────────────────────────────────────┐
│ GATE 4: QUALITY (Human + AI + Token)       │
├────────────────────────────────────────────┤
│ Human Checklist:                           │
│ ✓ 16/16 items pass                         │
│                                            │
│ AI Checklist:                              │
│ ✓ Frontmatter extracts correctly           │
│ ✓ Prerequisites parseable                  │
│ ✓ Preconditions/postconditions defined     │
│ ✓ Error signatures exact                   │
│ ✓ All links in metadata                    │
│ ✓ Success table has commands               │
│ ✓ Related docs discoverable                │
│                                            │
│ Token Efficiency:                          │
│ Token count: 3,847 / 4,000 budget          │
│ Ratio: 96% of budget (OK)                  │
│ Quality/token: 0.032 (target: 0.03+)       │
│ Quality Score: 87/100                      │
│                                            │
│ RESULT: ✓ PASS                             │
│ (After fixing Gate 3 issues)                │
└────────────────────────────────────────────┘

⏳ Running Gate 5...

┌────────────────────────────────────────────┐
│ GATE 5: SHIPPING                           │
├────────────────────────────────────────────┤
│ ✓ Gate 1: PASS                             │
│ ⚠ Gate 2: PASS WITH WARNINGS (fix 3 URLs) │
│ ⚠ Gate 3: NEEDS WORK (fix 2 issues)       │
│ ✓ Gate 4: PASS                             │
│                                            │
│ DEBT.md: ✓ Exists, 8 items                 │
│ metadata.json: ✓ Complete                  │
│ Status: Currently "draft"                  │
│                                            │
│ RESULT: ⚠ NOT READY TO SHIP                │
│                                            │
│ Required fixes:                            │
│ 1. Gate 2: Convert 3 URLs to doc titles    │
│ 2. Gate 3: Remove vague phrase (line 247)  │
│ 3. Gate 3: Add 2 missing examples          │
│                                            │
│ After fixes, re-run gates. Should pass.    │
│                                            │
├────────────────────────────────────────────┤
│ [View Details] [Fix Now] [Save as Draft]   │
│ [View DEBT] [Retry]                        │
└────────────────────────────────────────────┘

→ User selects: [Fix Now]

(Opens editor with flagged sections)

[User fixes issues]

$ docgen validate output/gtm/v1.0/GTM_Strategy_2026.md

✓ All gates passed!

Document is ready to ship.

Next: docgen confluence POST output/gtm/v1.0/GTM_Strategy_2026.md
```

---

## Flow 5: `docgen create gtm` (Interactive Questionnaire)

```
$ docgen create gtm

⏳ Launching GTM Builder...

┌────────────────────────────────────────────┐
│ GTM STRATEGY BUILDER                       │
│ Answer 8 questions. Takes 10 minutes.      │
├────────────────────────────────────────────┤
│ Question 1 of 8                            │
│                                            │
│ What's your product/service?               │
│ (1-2 sentences)                            │
│                                            │
│ → Acme Enterprise API Platform for real-time │
│   data integration                          │
│                                            │
└────────────────────────────────────────────┘

┌────────────────────────────────────────────┐
│ Question 2 of 8                            │
│                                            │
│ Who's your ideal customer?                 │
│ (company size, industry, role)             │
│                                            │
│ → Enterprise (500+ employees) SaaS         │
│   companies. Primary user: VP Engineering  │
│                                            │
└────────────────────────────────────────────┘

[... Questions 3-7 ...]

┌────────────────────────────────────────────┐
│ Question 8 of 8                            │
│                                            │
│ What's your timeline?                      │
│                                            │
│ → 4 weeks to launch first campaign         │
│                                            │
└────────────────────────────────────────────┘

⏳ Generating GTM Strategy doc...
⏳ Running exit gates...
⏳ Creating DEBT.md...

┌────────────────────────────────────────────┐
│ ✓ GTM STRATEGY CREATED                     │
├────────────────────────────────────────────┤
│                                            │
│ Document: GTM_Strategy_2026_v1.0           │
│ Quality: 91/100                            │
│ Tokens: 3,920 / 4,000                      │
│ Status: PRODUCTION READY                   │
│                                            │
│ Next?                                      │
│ [View] [Edit] [Confluence] [Jira] [Done]   │
│                                            │
└────────────────────────────────────────────┘
```

---

## Key UX Principles (Applied to All Flows)

1. **User Always Chooses**
   - No auto-execution
   - Show preview before action
   - [Confirm] button required

2. **Progressive Disclosure**
   - One question/decision at a time
   - Not overwhelming lists
   - Related options grouped

3. **Clear Feedback**
   - ✓ Success indicators
   - ⚠ Warnings with fixes
   - ✗ Errors with solutions

4. **Context Preservation**
   - Show document name, quality, tokens
   - Reference related docs
   - Link to outputs

5. **Next Steps Guidance**
   - What can I do next?
   - Suggested next action
   - Links to related commands

---

These mockups are the target UX for Phase 2.
