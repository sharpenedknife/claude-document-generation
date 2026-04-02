# CLI: MVP Specification

**Command:** `docgen ingest`  
**Purpose:** Accept any input, extract, generate doc, user chooses actions  
**UX:** Interactive terminal UI with previews and menus

---

## Command Variations (All Work)

### Variation 1: Web Link
```bash
$ docgen ingest https://acme.com

⏳ Fetching https://acme.com...
⏳ Extracting content...
✓ Done

[Show preview]
```

### Variation 2: Local File (Auto-Detect Type)
```bash
$ docgen ingest document.pdf

⏳ Reading document.pdf...
⏳ Extracting content...
✓ Done

[Show preview]
```

### Variation 3: Specify Type Explicitly
```bash
$ docgen ingest document.pdf --type pdf
$ docgen ingest slides.pptx --type pptx
$ docgen ingest data.xlsx --type xlsx
$ docgen ingest https://sheets.google.com/... --type google-sheets
```

### Variation 4: Interactive Prompt (No Args)
```bash
$ docgen ingest

? What's your source?
  (web link, file path, or drag-and-drop)
  
→ User: https://acme.com
→ [Enter]

⏳ Processing...
```

### Variation 5: Batch (Multiple Files)
```bash
$ docgen ingest document.pdf slides.pptx data.xlsx

? Create one doc with all, or separate?
  ○ One combined doc
  ○ Separate docs
  
→ User chooses
```

---

## Full Flow: Interactive UI

### Step 1: Input + Processing

```
$ docgen ingest https://acme.com

⏳ Fetching URL...
⏳ Parsing HTML...
⏳ Extracting sections...
⏳ Scoring confidence...

✓ Extraction complete
```

### Step 2: Preview (User Reviews What Was Extracted)

```
┌──────────────────────────────────────┐
│ EXTRACTED CONTENT                    │
├──────────────────────────────────────┤
│                                      │
│ Source: https://acme.com             │
│ Title: Acme - Enterprise API         │
│ Confidence: 82%                      │
│                                      │
│ Found:                               │
│ • 4 sections                         │
│ • 5 key points                       │
│ • 0 tables                           │
│                                      │
│ Sections:                            │
│ 1. Hero: "Fastest, most reliable..." │
│ 2. Features: "REST API, WebSocket"   │
│ 3. Pricing: "Free, Pro, Enterprise"  │
│ 4. About: "Founded 2020..."          │
│                                      │
│ Errors: None                         │
│                                      │
├──────────────────────────────────────┤
│ [Accept] [Edit] [Retry] [Cancel]     │
└──────────────────────────────────────┘
```

### Step 3: User Chooses Action

#### Option A: [Accept]
```
? Document type (auto-detected)?

  ○ API Reference (auto-detected)
  ○ GTM Strategy
  ○ Feature Guide
  ○ Product Specification
  ○ Process Guide
  ○ Other

→ User confirms: API Reference

⏳ Generating doc...
⏳ Running exit gates...

[Jump to Step 5: Results]
```

#### Option B: [Edit]
```
Edit mode (vi/nano style):

Title: Acme - Enterprise API Platform
[Edit title? Y/n]: n

Sections (1/4):
  Name: Hero
  Type: hero
  Content: "Fastest, most reliable API platform for 
           enterprise developers. Sub-100ms latency, 
           99.99% uptime."
  [Edit? Y/n]: y
  
  [Open editor]
  [Save and continue to next section]

[After all sections edited, continue to Step 3 menu]
```

#### Option C: [Retry]
```
? Retry with different source?

[Text input for new URL/file path]

→ User: https://different-site.com

⏳ Fetching new source...
[Jump back to Step 2: Preview]
```

### Step 4: Doc Type Mapping

```
? What type of document is this?

  ○ API Reference (confidence: 92%)
  ○ GTM Strategy
  ○ Feature Guide
  ○ Product Specification
  ○ Process Guide
  ○ Design Guide
  ○ Content Guide
  ○ Branding Guide
  ○ ICP (Ideal Customer Profile)
  ○ Other: ______________

→ User selects: API Reference
```

### Step 5: Generation + Gates

```
⏳ Generating document...
  • Populating template
  • Running Gate 1 (validation)...
  • Running Gate 2 (structure)...
  • Running Gate 3 (content)...
  • Running Gate 4 (quality)...
  • Running Gate 5 (shipping)...

✓ All gates passed!
```

### Step 6: Results

```
┌──────────────────────────────────────┐
│ ✓ DOCUMENT GENERATED                 │
├──────────────────────────────────────┤
│                                      │
│ Document:                            │
│   Acme_API_Reference_v1.0            │
│                                      │
│ Quality Score: 89/100                │
│ Tokens: 2,847 / 3,000 (budget OK)    │
│ Status: PRODUCTION READY             │
│                                      │
│ Saved to:                            │
│   output/web_dev/v1.0/               │
│     Acme_API_Reference_v1.0.md       │
│     Acme_API_Reference_v1.0.DEBT.md  │
│     Acme_API_Reference_v1.0.metadata │
│                                      │
│ DEBT Items (what's missing):         │
│ • P1: Authentication examples        │
│ • P1: Error codes reference          │
│ • P2: Webhooks guide                 │
│ • P2: Rate limiting details          │
│                                      │
├──────────────────────────────────────┤
│ Next?                                │
│                                      │
│ [View Doc]    (less)                 │
│ [View DEBT]   (edit backlog)         │
│ [Edit + Rerun] (change doc + re-run) │
│ [Confluence]  (post to Confluence)   │
│ [Jira]        (create issues)        │
│ [GitHub]      (commit + push)        │
│ [Done]        (exit)                 │
│                                      │
└──────────────────────────────────────┘
```

---

## Error Handling (Interactive)

### Error: File Not Found
```
$ docgen ingest nonexistent.pdf

✗ Error: File not found
  Checked: /home/user/nonexistent.pdf

Options:
  [Try different file]
  [Enter URL instead]
  [Cancel]
```

### Error: URL Unreachable
```
$ docgen ingest https://invalid-domain.xyz

✗ Error: Cannot reach URL
  Status: Connection timeout after 3 retries

Options:
  [Try different URL]
  [Upload file instead]
  [Cancel]
```

### Error: Low Confidence (Recoverable)
```
⚠ Warning: Low confidence (42%)

This content may not extract well.
The system found minimal structure.

Options:
  [Accept anyway] (may need heavy editing)
  [Try different source]
  [Cancel]
```

### Error: Unsupported Format
```
$ docgen ingest file.xyz

✗ Error: Unsupported format
  
Supported formats:
  • Web: https://example.com
  • PDF: file.pdf
  • PowerPoint: file.pptx
  • Excel: file.xlsx
  • Word: file.docx
  • Google Sheets: https://sheets.google.com/...
  • Google Docs: https://docs.google.com/...
```

---

## Other CLI Commands (Post-MVP)

These are mentioned but **NOT** built in MVP:

```bash
$ docgen validate FILE           # Run 5 gates (Phase 2)
$ docgen confluence POST FILE    # Post to Confluence (Phase 2)
$ docgen jira ISSUES FILE        # Create Jira issues (Phase 2)
$ docgen prompt "task"           # Generate prompt (Phase 2)
$ docgen list DOMAIN             # List docs (Phase 2)
$ docgen metrics MONTH           # Show metrics (Phase 2)
```

MVP = Just `docgen ingest` command.

---

## Implementation Checklist

### CLI Framework (30 mins)
- [ ] Use Click library for CLI
- [ ] Main command: `docgen ingest`
- [ ] Accept: file path, URL, or interactive prompt
- [ ] Handle --type flag (optional)

### Input Handler Integration (1 hour)
- [ ] Call universal_input_handler()
- [ ] Show progress (⏳ messages)
- [ ] Catch errors, show user-friendly messages

### Preview UI (1 hour)
- [ ] Display extraction results in formatted box
- [ ] Show: title, sections, confidence, key points
- [ ] [Accept] [Edit] [Retry] buttons

### Doc Type Mapping (30 mins)
- [ ] Interactive menu of doc types
- [ ] User chooses (or confirm auto-detected)

### Generation (30 mins)
- [ ] Call docgen generation function
- [ ] Run 5 exit gates
- [ ] Show results

### File Output (30 mins)
- [ ] Save .md, .DEBT.md, .metadata.json
- [ ] Display results summary
- [ ] Show next action options

**Total: ~4 hours for full MVP**

---

## Success = Working Flow

MVP done when:

```bash
$ docgen ingest https://acme.com

✓ Extracts
✓ Shows preview
✓ User: [Accept]
✓ Generates doc
✓ Runs gates
✓ Saves files
✓ Shows results: "Doc created, quality 87/100"
```

Does it work? Yes = MVP complete.
