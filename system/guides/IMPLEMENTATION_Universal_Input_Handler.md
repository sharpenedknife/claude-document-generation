# IMPLEMENTATION: Universal Input Handler

**Input:** File path, URL, or file upload  
**Output:** ExtractionResult (JSON with title, sections, confidence, etc.)  
**Time to implement:** ~3 hours (one handler for all 7 types)

---

## Input Examples & Expected Output

### Example 1: Web Link (Landing Page)

**Input:**
```bash
$ docgen ingest https://acme.com
```

**Expected Output:**
```json
{
  "title": "Acme - Enterprise API Platform",
  "type_detected": "api_reference",
  "sections": [
    {"name": "Hero", "type": "hero", "content": "Fastest, most reliable API platform..."},
    {"name": "Features", "type": "features", "content": "REST API, WebSocket, Webhooks..."},
    {"name": "Pricing", "type": "pricing", "content": "Free: $0, Pro: $99, Enterprise: Custom"}
  ],
  "key_points": ["Enterprise-grade", "Real-time", "99.99% uptime", "Sub-100ms"],
  "tables": [],
  "confidence": 0.82,
  "source_type": "web",
  "errors": [],
  "raw_content": "[Full HTML text extracted]"
}
```

---

### Example 2: PDF Upload

**Input:**
```bash
$ docgen ingest document.pdf
```

**Expected Output:**
```json
{
  "title": "API Integration Guide v2.1",
  "type_detected": "feature_guide",
  "sections": [
    {"name": "Overview", "type": "overview", "content": "This guide covers..."},
    {"name": "Authentication", "type": "process", "content": "Step 1: Get API key..."},
    {"name": "Error Codes", "type": "table", "content": "400: Bad Request, 401: Unauthorized..."}
  ],
  "key_points": ["OAuth 2.0", "API keys", "Rate limiting"],
  "tables": [
    {
      "title": "Error Codes",
      "rows": [
        ["Code", "Meaning", "Fix"],
        ["400", "Bad Request", "Check parameters"],
        ["401", "Unauthorized", "Verify token"]
      ]
    }
  ],
  "confidence": 0.88,
  "source_type": "pdf",
  "errors": [],
  "raw_content": "[PDF text extracted from all pages]"
}
```

---

### Example 3: Google Sheets Link

**Input:**
```bash
$ docgen ingest https://docs.google.com/spreadsheets/d/ABC123/
```

**Expected Output:**
```json
{
  "title": "Q2 2026 Product Roadmap",
  "type_detected": "product_spec",
  "sections": [
    {"name": "Overview", "type": "overview", "content": "Q2 priorities..."},
    {"name": "Features", "type": "table", "content": "[Sheet data as table]"}
  ],
  "key_points": ["Feature A: High priority", "Feature B: Medium", "Feature C: Low"],
  "tables": [
    {
      "title": "Q2 Roadmap",
      "rows": [
        ["Feature", "Priority", "Owner", "Status"],
        ["Authentication v2", "P0", "Alice", "In Progress"],
        ["Analytics", "P1", "Bob", "Planned"]
      ]
    }
  ],
  "confidence": 0.90,
  "source_type": "google_sheets",
  "errors": [],
  "raw_content": "[Sheet data extracted]"
}
```

---

### Example 4: PowerPoint Presentation

**Input:**
```bash
$ docgen ingest deck.pptx
```

**Expected Output:**
```json
{
  "title": "Product Launch Deck",
  "type_detected": "gtm_strategy",
  "sections": [
    {"name": "Slide 1: Title", "type": "hero", "content": "Product Launch: Q2 2026"},
    {"name": "Slide 2: Problem", "type": "overview", "content": "Customer pain point: No integration..."},
    {"name": "Slide 3: Solution", "type": "features", "content": "Our API provides: Fast, Reliable..."},
    {"name": "Slide 4: Go-to-Market", "type": "process", "content": "Phase 1: Beta..., Phase 2: GA..."}
  ],
  "key_points": ["Problem: Integration pain", "Solution: Universal API", "GTM: Beta → GA"],
  "tables": [],
  "confidence": 0.80,
  "source_type": "pptx",
  "errors": [],
  "raw_content": "[All slide text combined]"
}
```

---

### Example 5: Excel Spreadsheet

**Input:**
```bash
$ docgen ingest budget.xlsx
```

**Expected Output:**
```json
{
  "title": "2026 Budget Allocation",
  "type_detected": "product_spec",
  "sections": [
    {"name": "Overview", "type": "overview", "content": "Budget by department..."},
    {"name": "Data", "type": "table", "content": "[Sheet data]"}
  ],
  "key_points": ["Engineering: $2M", "Marketing: $1M", "Sales: $1.5M"],
  "tables": [
    {
      "title": "Budget",
      "rows": [
        ["Department", "Amount", "Headcount"],
        ["Engineering", "$2000000", "20"],
        ["Marketing", "$1000000", "5"]
      ]
    }
  ],
  "confidence": 0.95,
  "source_type": "xlsx",
  "errors": [],
  "raw_content": "[Excel data extracted]"
}
```

---

### Example 6: Google Docs Link

**Input:**
```bash
$ docgen ingest https://docs.google.com/document/d/ABC123/
```

**Expected Output:**
```json
{
  "title": "Engineering Design Document",
  "type_detected": "feature_guide",
  "sections": [
    {"name": "Overview", "type": "overview", "content": "This document describes..."},
    {"name": "Architecture", "type": "process", "content": "System components: API, DB, Cache..."},
    {"name": "Data Model", "type": "table", "content": "[Tables from doc]"}
  ],
  "key_points": ["Microservices", "PostgreSQL", "Redis cache"],
  "tables": [
    {
      "title": "API Endpoints",
      "rows": [
        ["Endpoint", "Method", "Auth"],
        ["/users", "GET", "Bearer token"],
        ["/users", "POST", "Bearer token"]
      ]
    }
  ],
  "confidence": 0.85,
  "source_type": "google_docs",
  "errors": [],
  "raw_content": "[Doc content extracted]"
}
```

---

### Example 7: Word Document

**Input:**
```bash
$ docgen ingest proposal.docx
```

**Expected Output:**
```json
{
  "title": "Customer Proposal: Acme Inc",
  "type_detected": "gtm_strategy",
  "sections": [
    {"name": "Executive Summary", "type": "overview", "content": "We propose..."},
    {"name": "Solution Overview", "type": "features", "content": "Our offering includes..."},
    {"name": "Pricing", "type": "pricing", "content": "Implementation: $50K, Annual: $25K"}
  ],
  "key_points": ["3-month implementation", "$50K + $25K/year", "Dedicated support"],
  "tables": [],
  "confidence": 0.87,
  "source_type": "docx",
  "errors": [],
  "raw_content": "[Document text extracted]"
}
```

---

## Error Handling Examples

### Error 1: File Not Found
```bash
$ docgen ingest nonexistent.pdf
✗ Error: File not found
Checked: /home/user/nonexistent.pdf
Try: docgen ingest [valid file path]
```

### Error 2: URL Unreachable
```bash
$ docgen ingest https://invalid-domain-xyz.com
✗ Error: Cannot reach URL (tried 3 times)
Check: Is URL correct? Is network active?
Try: docgen ingest [different URL]
```

### Error 3: Unsupported Format
```bash
$ docgen ingest file.unknown
✗ Error: Unsupported format: .unknown
Supported: web (https://), pdf, pptx, xlsx, docx, google sheets, google docs
```

### Error 4: Low Confidence
```bash
$ docgen ingest minimal.pdf
⚠ Warning: Confidence score is low (45%)
Content may not extract well from this source.
Options:
  [Accept anyway] [Edit extraction] [Retry with different source]
```

---

## Implementation Strategy

### Phase 1: Core Handler (1 hour)
```python
def handle_input(source: str) -> ExtractionResult:
    """Universal input handler for 7 types."""
    
    # Detect type
    input_type = detect_input_type(source)
    
    # Route to extractor
    if input_type == "web":
        raw_content = fetch_url(source)
    elif input_type == "pdf":
        raw_content = extract_pdf(source)
    elif input_type == "pptx":
        raw_content = extract_pptx(source)
    elif input_type == "xlsx":
        raw_content = extract_xlsx(source)
    elif input_type == "docx":
        raw_content = extract_docx(source)
    elif input_type == "google_sheets":
        raw_content = extract_google_sheets(source)
    elif input_type == "google_docs":
        raw_content = extract_google_docs(source)
    
    # Normalize
    result = normalize_to_json(raw_content, input_type)
    
    # Score confidence
    result.confidence = score_confidence(result)
    
    return result
```

### Phase 2: Type-Specific Extractors (2 hours)
- `extract_url()` — BeautifulSoup HTML parsing
- `extract_pdf()` — pdfplumber for text
- `extract_pptx()` — python-pptx for slides
- `extract_xlsx()` — openpyxl for sheets
- `extract_docx()` — python-docx for docs
- `extract_google_sheets()` — URL scrape (or API)
- `extract_google_docs()` — URL scrape (or API)

### Phase 3: Confidence Scoring (30 mins)
```python
def score_confidence(result: ExtractionResult) -> float:
    """Score 0-1 based on what was extracted."""
    score = 0.0
    score += 0.3 if result.title else 0  # Title found
    score += 0.3 if len(result.sections) >= 2 else 0  # 2+ sections
    score += 0.2 if result.key_points else 0  # Key points found
    score += 0.2 if not result.errors else 0  # No errors
    return min(score, 1.0)
```

---

## Tests (What counts as passing?)

**Test 1: Web Link**
- ✓ Extracts title
- ✓ Finds 3+ sections
- ✓ Confidence > 75%
- ✓ No errors

**Test 2: PDF**
- ✓ Extracts text from all pages
- ✓ Finds 2+ sections
- ✓ Confidence > 80%
- ✓ Handles multi-page correctly

**Test 3: Google Sheets**
- ✓ Extracts sheet data
- ✓ Converts to table format
- ✓ Confidence > 85%

**Test 4: PowerPoint**
- ✓ Extracts text from all slides
- ✓ Preserves slide order
- ✓ Combines into sections

**Test 5: Error Case (unreachable URL)**
- ✓ Fails gracefully with ExtractionError
- ✓ Shows helpful message

**Test 6: Low Confidence (minimal content)**
- ✓ Returns warning
- ✓ User can still preview

---

## Success = Working MVP

When all 7 types work (even if imperfectly):
- User can upload/link any content
- System extracts something useful
- User sees preview
- User chooses: [Accept] or [Edit] or [Retry]
- Doc generates + gates run
- File saved to output/

Perfect extraction quality is Phase 2. MVP = working flow.
