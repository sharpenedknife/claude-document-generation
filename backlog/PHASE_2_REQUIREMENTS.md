# Phase 2: Requirements and Architecture

**Status:** Planning (Phase 1 complete, Phase 2 incoming)

---

## Overview

Phase 2 expands docgen from a generation-only system to an **ingestion + generation + integration** platform.

**Core capability shift:**
- Phase 1: Manual creation → docs via templates
- Phase 2: **Content ingestion** → intelligent extraction → docs via templates

**Key principle:** User always chooses actions. No auto-execution. All integrations interactive.

---

## 1. Input Source Ingestion

Docgen can now consume existing content and convert to production docs.

### Supported Input Formats

| Source | Format | Use Case |
|--------|--------|----------|
| Landing page | URL → HTML scrape | Extract product positioning, features, benefits |
| PDF | PDF text extraction | Convert existing docs, white papers, specs |
| Google Docs | URL or file | Internal docs, designs, specs |
| Slides | PPTX/PDF | Presentation content → written docs |
| Email/Gmail | Raw email or thread | Extract decisions, meeting notes, processes |
| Word/DOCX | File upload | Migration from legacy docs |

### Input Processing Pipeline

```
Input Source (landing page, PDF, Gmail, etc.)
  ↓
Intelligent Extraction
  (Claude AI extracts: structure, key points, data)
  ↓
Show User: "What I found"
  - Title, sections, key concepts
  - Confidence score (how well extracted)
  ↓
User Chooses:
  ✓ Use this extraction
  ✓ Edit extraction before proceeding
  ✗ Cancel and try different source
  ↓
Map to Doc Type
  "This looks like: GTM strategy / Design guide / API reference"
  User confirms or changes
  ↓
Generate Doc
  Using DOC_CANONICAL_TEMPLATE + extracted content
  ↓
Run 5 Exit Gates
  (same as manually created docs)
  ↓
Show User: "Generated doc + what's next"
  - Quality score
  - What's missing (from DEBT.md)
  ↓
User Chooses:
  ✓ Accept doc
  ✓ Edit before shipping
  ✓ Regenerate with different approach
  ✗ Cancel
  ↓
Post-Generation Actions
  (Confluence, Jira, etc.)
```

### Example Flow: Landing Page → GTM Doc

```
User: Upload landing page URL
  "https://acme.com"
  ↓
Docgen extracts:
  Title: "Acme - Enterprise API Platform"
  Features: [REST API, WebSocket, Webhooks, Rate limiting]
  Target: "Enterprise developers"
  Use cases: [Real-time data, Integration, Automation]
  Positioning: "Fastest, most reliable"
  ↓
Shows user:
  ┌─────────────────────────────────┐
  │ EXTRACTED CONTENT               │
  │                                 │
  │ Title: Acme - Enterprise API    │
  │ Type: API / Developer Platform  │
  │                                 │
  │ Key points:                     │
  │ • REST + WebSocket             │
  │ • Real-time capabilities        │
  │ • Enterprise focus              │
  │                                 │
  │ Quality: 78% confidence         │
  │                                 │
  │ [Accept] [Edit] [Retry] [Cancel]│
  └─────────────────────────────────┘
  ↓
User: [Accept]
  ↓
Docgen asks:
  "Map to doc type?"
  - GTM Strategy
  - API Reference
  - Feature Guide
  - Competitive Analysis
  - Other
  ↓
User: "API Reference"
  ↓
Generate doc using:
  - Extracted content
  - DOC_CANONICAL_TEMPLATE.md
  - API doc rules
  - Token budget (3000)
  ↓
Run gates:
  Gate 1: ✓ Metadata valid
  Gate 2: ✓ Sections present
  Gate 3: ✓ Content clear
  Gate 4: ✓ Quality score 87
  Gate 5: ✓ DEBT.md created
  ↓
Show user:
  ┌──────────────────────────────────┐
  │ DOC GENERATED                    │
  │                                  │
  │ Title: Acme API Reference        │
  │ Quality: 87/100                  │
  │ Tokens: 2847 / 3000              │
  │ Status: Ready to ship            │
  │                                  │
  │ What's missing (DEBT):           │
  │ - Authentication examples (P1)   │
  │ - Error codes reference (P2)     │
  │ - Webhooks guide (P2)            │
  │                                  │
  │ Next:                            │
  │ [Ship to Confluence]             │
  │ [Create Jira Story]              │
  │ [Edit + Rerun Gates]             │
  │ [Cancel]                         │
  └──────────────────────────────────┘
  ↓
User: [Ship to Confluence]
  ↓
Shows: "Which space? Which page format?"
  [Choose space] [Choose template]
  ↓
Posts to Confluence
```

---

## 2. New Domains (Phase 2)

### Domain 8: Product Development

**Scope:** Product specs, roadmaps, feature requirements, user research

**Doc types:**
- Product specification (PRD)
- Feature requirement
- User research synthesis
- Product roadmap
- Development guide

**Token budget:** 4500 (longer, more detail)
**Primary audience:** Product, Engineering, Design
**Priority:** 1

**Starting material:** Product briefs, feature requests, user interviews, competitor analysis

### Domain 9: Project Management

**Scope:** Project plans, processes, workflows, sprints, retrospectives

**Doc types:**
- Project plan
- Process documentation
- Workflow guide
- Sprint report
- Retrospective summary

**Token budget:** 3500
**Primary audience:** Project leads, Team, Stakeholders
**Priority:** 2

**Starting material:** Project briefs, meeting notes, Jira epics, process docs

---

## 3. Prompt Builder + Embed in Chat

**Capability:** Generate optimized prompts, paste directly into chat.

### Flow

```
User: "Build me a prompt for extracting GTM strategy from landing pages"
  ↓
Prompt builder generates:
  - Instruction
  - Examples (few-shot)
  - Temperature setting
  - Token budget
  - Output format (JSON/Markdown)
  ↓
Shows user:
  ┌─────────────────────────────────┐
  │ GENERATED PROMPT                │
  │                                 │
  │ System: "Extract GTM elements..." │
  │ Temperature: 0.7                │
  │ Max tokens: 1500                │
  │                                 │
  │ Examples:                       │
  │ Input: [landing page]           │
  │ Output: {positioning, market...}│
  │                                 │
  │ [Copy to Clipboard]             │
  │ [Embed in Chat]                 │
  │ [Regenerate]                    │
  └─────────────────────────────────┘
  ↓
User: [Embed in Chat]
  ↓
Prompt appears in chat, ready to use:

  System prompt copied:
  "Extract GTM elements from content...
   Return JSON with: positioning, market, features..."

  Now paste content and run.
```

**Why embed instead of just copy:**
- User sees exact prompt they'll execute
- Can test it right there
- Can modify before use
- Full visibility into what Claude sees

### New Domain: Prompts

**In docgen:**
```
builders/prompts/
├── builder.md          — Questions: What task? Audience? Format?
├── rules.md            — Prompt quality standards
├── token_budget.md     — Token limits
└── examples/           — Perfect prompt examples
```

**Quality gates for prompts:**
- Gate 1: Prompt is valid (no syntax errors)
- Gate 2: Structure (instruction + examples + format)
- Gate 3: Clarity (unambiguous, specific)
- Gate 4: Effectiveness (examples work, temperature appropriate)
- Gate 5: Shipping (tested, output format validated)

---

## 4. Jira & Confluence Integration

**Principle:** User chooses actions at each step. No auto-execution.

### Confluence Integration

**Action: Post Page**

```
User generates doc → [Ship to Confluence]
  ↓
Docgen asks:
  ┌──────────────────────────────────┐
  │ POST TO CONFLUENCE               │
  │                                  │
  │ Space: [Dropdown]                │
  │ Parent page: [Optional]          │
  │ Labels: [Tags]                   │
  │ Notify: [Users]                  │
  │                                  │
  │ Update existing?                 │
  │ ○ No, create new page            │
  │ ○ Yes, update (which page?)      │
  │                                  │
  │ [Preview] [Post] [Cancel]        │
  └──────────────────────────────────┘
  ↓
User chooses options
  ↓
Shows preview of what will post
  ↓
User: [Post]
  ↓
Creates/updates page in Confluence
  ↓
Returns: "Posted to DOCS/GTM Strategy"
  Link: https://confluence.company.com/...
```

### Jira Integration

**Action: Create Ticket/Story**

```
User has doc + DEBT.md → [Create Jira Issues]
  ↓
Docgen asks:
  ┌──────────────────────────────────┐
  │ CREATE JIRA ISSUES               │
  │                                  │
  │ Project: [Dropdown]              │
  │ Issue type:                      │
  │ ○ Story                          │
  │ ○ Task                           │
  │ ○ Bug                            │
  │ ○ Epic                           │
  │                                  │
  │ Create from:                     │
  │ ☑ DEBT P1 items (4 issues)       │
  │ ☐ DEBT P2 items (5 issues)       │
  │ ☐ DEBT P3 items (3 issues)       │
  │                                  │
  │ Link to doc? ☑                   │
  │ Assignee: [User dropdown]        │
  │ Sprint: [Sprint dropdown]        │
  │                                  │
  │ [Preview] [Create] [Cancel]      │
  └──────────────────────────────────┘
  ↓
User chooses:
  - Which DEBT items
  - Ticket type
  - Assignee
  - Sprint
  ↓
Shows preview
  ↓
User: [Create]
  ↓
Creates N tickets in Jira
  ↓
Returns: "Created 4 stories"
  - DOCS-142: Add authentication examples
  - DOCS-143: Error codes reference
  - DOCS-144: Webhook guide
  - DOCS-145: Rate limiting examples
```

---

## 5. CLI via Claude Code

**Not a separate tool.** Uses Claude Code's native capabilities.

### Entry point: `docgen` command

```bash
docgen --help

DOCGEN v2.0 - Documentation Generation System

Usage:
  docgen COMMAND [OPTIONS]

COMMANDS:

  Create & Generate:
    create DOMAIN              Create new doc (GTM, Design, Branding, etc.)
    ingest SOURCE TYPE         Ingest content (landing-page, pdf, gmail, etc.)
    prompt TASK                Generate optimized prompt for task

  Validate & Manage:
    validate FILE              Run 5 exit gates on doc
    list DOMAIN                List all docs in domain
    show DOC                   Show doc + metadata
    debt DOC                   Show DEBT.md for doc

  Integration:
    confluence POST DOC        Post doc to Confluence (interactive)
    jira ISSUES DOC            Create Jira issues from DEBT (interactive)
    github PUSH DOMAIN         Push domain docs to GitHub

  Utility:
    config SHOW                Show system config
    metrics MONTH              Show monthly metrics
    version                    Show docgen version

EXAMPLES:

  $ docgen create GTM
    Interactive questionnaire for GTM strategy

  $ docgen ingest https://acme.com landing-page
    Extract content from landing page, map to doc type

  $ docgen ingest document.pdf pdf
    Extract text from PDF, ask what to do with it

  $ docgen validate my_doc.md
    Run all 5 exit gates, show results

  $ docgen confluence POST GTM_Strategy_2026.md
    Interactive: choose space, format, notify users, then post

  $ docgen jira ISSUES GTM_Strategy_2026.md
    Interactive: choose DEBT items, issue type, assignee, then create

  $ docgen prompt "Extract positioning from web content"
    Generate optimized prompt with examples

  $ docgen list gtm
    Show all GTM docs (all versions)

  $ docgen metrics april
    Show April metrics (docs generated, quality, etc.)
```

### Implementation

**In Code.md:**
```python
#!/usr/bin/env python3
"""Docgen CLI - Documentation generation system"""

import click
import subprocess
from pathlib import Path

@click.group()
def cli():
    """Docgen - Production documentation framework"""
    pass

@cli.command()
@click.argument('domain')
def create(domain):
    """Create new doc in domain (interactive questionnaire)"""
    # Call Claude Project for interactive questionnaire
    # Returns: doc content + metadata
    pass

@cli.command()
@click.argument('source')
@click.argument('type')
def ingest(source, type):
    """Ingest content from various sources"""
    # URL/PDF/Gmail/Slides → extract → show user
    pass

@cli.command()
@click.argument('doc_file')
def validate(doc_file):
    """Run 5 exit gates on document"""
    # Check gates 1-5
    # Show results
    pass

@cli.command()
@click.argument('action')
@click.argument('doc_file')
def confluence(action, doc_file):
    """Post to Confluence (interactive)"""
    # Show options: space, update vs new, labels, notify
    # User chooses
    # Post
    pass

@cli.command()
@click.argument('action')
@click.argument('doc_file')
def jira(action, doc_file):
    """Create Jira issues from DEBT (interactive)"""
    # Show DEBT items
    # User chooses which to create
    # Create tickets
    pass

if __name__ == '__main__':
    cli()
```

**Usage:**
```bash
$ docgen create gtm
$ docgen ingest landing_page.pdf pdf
$ docgen validate my_doc.md
$ docgen confluence POST my_doc.md
$ docgen jira ISSUES my_doc.md
```

---

## 6. Interactive UX: Command Lists vs Code

**Problem:** Project Instructions show all options as text. Overwhelming. Hard to discover.

**Solution:** Split responsibilities.

### Project (Static)
- Framework docs (guides)
- Standards (templates)
- Examples
- **Not:** Command lists, interactive flows

### Code (Dynamic)
- `docgen create` → Interactive questionnaire
- `docgen ingest` → Extract + user chooses
- `docgen confluence` → Menu options
- `docgen jira` → Menu options
- `docgen prompt` → Generate + embed in chat

**Benefits:**
- ✅ No overwhelming lists in Project
- ✅ Guided flow (one question at a time)
- ✅ User always chooses (no auto-execution)
- ✅ Discoverable via `--help`
- ✅ Works offline (Code) or online (API calls)

---

## Architecture: Phase 2 Complete

```
docgen/
│
├── system/                 # Framework (v1.0, unchanged)
│   ├── guides/            # 10 standards
│   ├── templates/         # Output templates
│   ├── checklists/        # Quality verification
│   └── examples/          # Perfect examples
│
├── builders/              # Builders (Phase 1 + 2)
│   ├── gtm/              # Existing
│   ├── design/           # Existing
│   ├── branding/         # Existing
│   ├── content/          # Existing
│   ├── icp/              # Existing
│   ├── web_dev/          # Existing
│   ├── product_dev/      # NEW
│   ├── project_mgmt/     # NEW
│   └── prompts/          # NEW
│
├── ingestion/             # NEW: Input processing
│   ├── extractors/
│   │   ├── landing_page.py   (URL scraper)
│   │   ├── pdf.py            (PDF text extraction)
│   │   ├── gmail.py          (Email extraction)
│   │   ├── slides.py         (PPTX/PDF slides)
│   │   └── gdocs.py          (Google Docs)
│   ├── mappers/             # Map extracted → doc type
│   └── enrichers/           # Add context + metadata
│
├── integrations/          # NEW: External APIs
│   ├── confluence.py      (Atlassian API)
│   ├── jira.py           (Jira REST API)
│   ├── gmail.py          (Gmail API)
│   ├── github.py         (GitHub API)
│   └── openai.py         (Direct Claude API for prompts)
│
├── cli/                   # NEW: Command interface
│   ├── main.py           (Click CLI)
│   ├── commands/
│   │   ├── create.py
│   │   ├── ingest.py
│   │   ├── validate.py
│   │   ├── confluence.py
│   │   ├── jira.py
│   │   ├── prompt.py
│   │   └── ...
│   └── ui/               # Terminal UI components
│       ├── menus.py
│       ├── preview.py
│       └── confirm.py
│
├── output/               # Generated docs
├── skills/              # Reusable skills
├── projects/            # Claude Projects
├── config/              # System config
├── metrics/             # Tracking
├── backlog/             # DEBT
│
└── docs/                # Documentation
    ├── ARCHITECTURE.md
    ├── PHASE_2_REQUIREMENTS.md ← You are here
    └── CLI_GUIDE.md
```

---

## Implementation Order (Phase 2)

**P1 (High Priority):**
1. Landing page ingestion (URL scraper + extractor)
2. New domains (Product Dev, Project Management)
3. Confluence integration (post page, interactive menu)
4. CLI foundation (Click framework, basic commands)
5. Prompt builder (generate + embed in chat)

**P2 (Medium Priority):**
6. PDF/Slides ingestion
7. Jira integration (create stories/tasks)
8. Gmail integration (extract meeting notes)
9. Interactive menus (Preview, Confirm, Choose)
10. Metrics dashboard

**P3 (Nice to Have):**
11. GitHub direct integration
12. Template suggestions (based on content)
13. Automated DEBT generation (from extracted gaps)
14. Web UI (instead of CLI)

---

## Success Criteria (Phase 2)

When complete:
- ✅ Can ingest 5 input types (landing page, PDF, slides, email, docs)
- ✅ User chooses actions at each step (interactive, not auto)
- ✅ 9 domains total (6 + 3 new)
- ✅ Confluence integration (post/update pages)
- ✅ Jira integration (create issues from DEBT)
- ✅ Prompt builder (generate + embed in chat)
- ✅ CLI via Code (all major commands)
- ✅ Good UX (menus, previews, confirmations, no overwhelming text)

---

## Known Unknowns

1. **Input quality:** How well does extraction work for messy inputs (email threads, PDFs)?
   - Answer: Test with real data, iterate

2. **Token costs:** Ingestion + generation doubles token usage. Optimize?
   - Answer: Add ingestion budget tracking to metrics

3. **User preferences:** Confluence space, Jira project, GitHub token management?
   - Answer: Store in config/user_config.json (per-user)

---

**Status:** Ready for Phase 2 development.
