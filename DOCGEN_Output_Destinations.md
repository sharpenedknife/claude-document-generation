# DOCGEN: Output Destinations

User chooses 1+ destinations where generated docs are saved/pushed.

---

## Destination 1: Zip File (Local Download)

**Always available. Works offline.**

### What Gets Zipped

```
docgen_output_[timestamp].zip (e.g., docgen_output_20260402_1830.zip)
│
├── README.md                    ← Index + quick start guide
├── 00_SUMMARY.md               ← What was generated, quality scores
│
├── project/                    ← Main project docs
│   ├── PRD.md
│   ├── UX_Requirements.md
│   ├── specifiers.md
│   └── PRD.metadata.json
│
├── workflows/                  ← Additional workflow docs
│   ├── Development_Plan.md
│   ├── Messaging.md
│   ├── Positioning.md
│   └── [metadata files]
│
├── generated_at/               ← Metadata
│   ├── docgen_config.json     (what was selected)
│   ├── generation_log.md      (timestamps, API calls)
│   └── quality_gates.json     (gate results per doc)
│
└── assets/                     ← Optional (brand guidelines, etc.)
    └── [if brand docs generated]
```

### Quality Gates

Each `.md` has companion `.metadata.json`:
```json
{
  "filename": "PRD.md",
  "gate_1_validation": "PASS",
  "gate_2_structure": "PASS",
  "gate_3_content": "PASS",
  "gate_4_quality": "PASS (89/100)",
  "gate_5_shipping": "PASS",
  "status": "PRODUCTION_READY",
  "generated_at": "2026-04-02T18:30:00Z"
}
```

### Delivery

```
✓ Zip created: docgen_output_20260402_1830.zip
Size: 2.3 MB
Download link: [Auto-download in browser]

Contents: 12 documents + metadata + README
```

---

## Destination 2: GitHub (Push to Repo)

**Requires:** GitHub token or OAuth  
**Scope:** Create/update branch, push docs

### User Setup

```
? GitHub repository?
  [Text input: username/repo-name]
  
? Branch?
  [Default: main] [Or: main, feature/docgen, docs-v1]

? Commit message?
  [Default: "Docgen: Generated product docs"]
```

### What Gets Pushed

```
repo/
├── docs/                       ← New folder
│   ├── README.md              ← Index
│   ├── project/
│   │   ├── PRD.md
│   │   ├── UX_Requirements.md
│   │   └── specifiers.md
│   ├── workflows/
│   │   ├── Development_Plan.md
│   │   └── [others]
│   └── .metadata.json         ← Generation metadata
│
└── [existing repo files untouched]
```

### Commit Details

```
Commit: "Docgen: Generated product docs"
Author: Docgen Bot
Timestamp: 2026-04-02 18:30:00 UTC

Files changed: 12 new files
  + docs/README.md
  + docs/project/PRD.md
  + docs/project/UX_Requirements.md
  + docs/workflows/Development_Plan.md
  + [etc.]

Pull request: (optional) Create PR instead of pushing to main
  ? Create PR? Yes / No
  ? PR title? [Auto-fill: "Docgen: Generated product docs"]
  ? PR description? [Auto-fill with summary]
```

### Delivery

```
✓ Pushed to GitHub
  Repository: github.com/user/repo
  Branch: main (or feature/docgen)
  Commit: abc1234
  Files: 12 new files
  
Next?
[View on GitHub] [Create PR] [Done]
```

---

## Destination 3: Notion (Create Workspace + Pages)

**Requires:** Notion API key + Workspace access  
**Scope:** Create pages, structure docs

### User Setup

```
? Notion workspace?
  [OAuth: Connect to Notion account]
  OR
  [Paste API key]

? Parent page / Database?
  [Dropdown: Select folder or create new]
  Default: "Docgen Output"

? Page structure?
  ○ Flat (all docs at same level)
  ○ Nested (Folders for each doc type)
  ○ Database (Searchable table with filters)
  
Default: Nested
```

### What Gets Created

```
Notion Workspace
│
└── Docgen Output           ← Parent folder
    │
    ├── 📋 Project
    │   ├── 📄 PRD
    │   │   (Properties: status, quality, date)
    │   ├── 📄 UX Requirements
    │   └── 📄 specifiers
    │
    ├── ⚙️ Workflows
    │   ├── 📄 Development Plan
    │   ├── 📄 Messaging
    │   └── 📄 Positioning
    │
    ├── 📊 Quality Report
    │   (Table: Document, Status, Quality Score)
    │
    └── 📌 Summary
        (Links to all docs + next actions)
```

### Database Option

If user picks "Database":
```
Notion Database: "Generated Documents"

Fields:
  • Name (title)
  • Type (Project, Workflow, API, etc.)
  • Status (✅ Production Ready, ⚠️ Needs Work, ❌ Failed)
  • Quality Score (0-100)
  • Workflow Set (if applicable)
  • Generated Date
  • Download (link to markdown)

Filters:
  • By Type
  • By Status
  • By Quality Score
```

### Formatting

Each doc block contains:
```
Title: PRD
Status: ✅ Production Ready
Quality: 89/100
Generated: April 2, 2026

[Doc content - nicely formatted with headings, code blocks]

Properties:
  Status: Production Ready
  Document Type: Project / PRD
  Generated: 2026-04-02
```

### Delivery

```
✓ Created in Notion
  Workspace: My Workspace
  Parent: Docgen Output
  Pages: 12 created
  
Next?
[Open in Notion] [Share Access] [Done]
```

---

## Destination 4: Google Drive (Create Folder + Upload)

**Requires:** Google OAuth  
**Scope:** Create folder, upload files

### User Setup

```
? Google Drive folder?
  [OAuth: Connect to Google]
  
? Parent folder?
  [Dropdown: My Drive, Shared Drive, Specific folder]
  Default: My Drive > Docgen Output

? File format?
  ○ Markdown (.md) files
  ○ Google Docs (native)
  ○ PDF (for sharing)
  ○ All formats
  
Default: Markdown + Google Docs
```

### What Gets Created

```
Google Drive
│
└── Docgen Output           ← Folder (created)
    │
    ├── 📁 Project         ← Subfolder
    │   ├── 📄 PRD.md / 📄 PRD (Google Doc)
    │   ├── 📄 UX_Requirements.md
    │   └── 📄 specifiers.md
    │
    ├── 📁 Workflows       ← Subfolder
    │   ├── 📄 Development_Plan.md
    │   └── [others]
    │
    ├── 📄 README.md       ← Index
    ├── 📄 SUMMARY.md      ← Quality report
    │
    └── 📊 metadata.json   ← Generation metadata
```

### Sharing Options

```
? Share these files?
  ○ Don't share (only me)
  ○ Share with team (select users)
  ○ Make public (shareable link)
  
If sharing:
  ☑ View access
  ☑ Comment access
  ☑ Edit access
```

### Delivery

```
✓ Uploaded to Google Drive
  Folder: Docgen Output
  Location: My Drive
  Files: 12 uploaded
  
Sharing:
  ○ Private (only you)
  ○ Shared with [team emails]
  ○ Public (link)

Next?
[Open in Drive] [Share Link] [Done]
```

---

## Destination 5: Email (Send Links + Zip)

**Requires:** User email confirmation  
**Scope:** Send zip + links to all docs

### User Setup

```
? Email address(es)?
  [user@example.com]
  [Add more recipients]

? What to include?
  ☑ Zip file (attachment)
  ☑ Links (Notion, GitHub, Drive)
  ☑ Summary document
  ☑ Quality report
  
? Email message?
  [Pre-filled template - user can edit]
```

### Email Content

```
Subject: Your Docgen Output: [Project Name]

Hi [User],

Your documentation has been generated and is ready to use!

📦 Downloads
• Zip File: [Download Link] (expires in 7 days)

📍 Locations
• GitHub: [Link to repo/branch]
• Notion: [Link to workspace]
• Google Drive: [Link to folder]

📊 Summary
Generated: 12 documents
Quality: All ✅ Production Ready
Time: 2h 15m

Documents:
1. PRD (89/100)
2. UX Requirements (92/100)
3. specifiers.md (85/100)
[... etc]

Next Steps:
1. Review docs in your preferred location
2. Share with team
3. Start implementation

Questions? Reply to this email.

---
Docgen v1.0
```

### Delivery

```
✓ Email sent to user@example.com
  Subject: "Your Docgen Output: [Project Name]"
  
Attachments: docgen_output.zip (2.3 MB)
Links: GitHub, Notion, Google Drive
TTL: 7 days
```

---

## Multiple Destinations

User can choose **1 or more**:

```
✓ Zip File
✓ GitHub (feature/docs branch)
✓ Notion (Docgen Output database)
✓ Google Drive (Docgen Output folder)
☐ Email

Zip: Ready now
GitHub: Pushed to feature/docgen
Notion: Created Docgen Output workspace
Drive: Uploaded to My Drive

All delivery methods completed!
```

---

## Summary View

After generation, user sees:

```
┌─────────────────────────────────┐
│ ✓ 12 DOCUMENTS GENERATED        │
├─────────────────────────────────┤
│ Quality: All Production Ready    │
│ Time: 2h 15m                    │
│                                 │
│ 📦 Zip:    docgen_output.zip    │
│ 🐙 GitHub: [Link]               │
│ 🗂️  Notion: [Link]              │
│ 🚀 Drive:  [Link]               │
│ 📧 Email:  [Link]               │
│                                 │
│ [Download All] [View Summary]   │
│ [Share] [Done]                  │
└─────────────────────────────────┘
```

---

**All files delivered. User can access from any location.**
