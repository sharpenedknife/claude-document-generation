# MVP Implementation Checklist

**Goal:** Working MVP in 4 hours  
**Start:** Now  
**Done:** When all ✅

---

## Phase 1: Core Logic (Hour 1)

### Input Handler
- [ ] `ingestion/handler.py` created
- [ ] `detect_input_type()` function works
  - [ ] Detects .pdf files
  - [ ] Detects .pptx files
  - [ ] Detects .xlsx files
  - [ ] Detects .docx files
  - [ ] Detects https:// URLs
  - [ ] Detects google.com URLs
- [ ] `handle_input()` main function created
- [ ] Returns `ExtractionResult` with required fields

### Data Structure
- [ ] `ExtractionResult` class/dict defined with:
  - [ ] `title: str`
  - [ ] `sections: List[Dict]`
  - [ ] `key_points: List[str]`
  - [ ] `tables: List[Dict]`
  - [ ] `confidence: float`
  - [ ] `source_type: str`
  - [ ] `errors: List[str]`
  - [ ] `raw_content: str`

**Test:** 
```bash
python -c "from code.ingestion.handler import ExtractionResult; print('OK')"
```

---

## Phase 2: Extractors (Hour 2)

### Web Extractor
- [ ] `extractors/web.py` created
- [ ] `fetch_url()` gets HTML with retries
- [ ] `parse_html()` finds title + sections
- [ ] Returns ExtractionResult
- [ ] **Test:** `extract_web('https://acme.com')`

### PDF Extractor
- [ ] `extractors/pdf.py` created
- [ ] `extract_pdf()` reads file
- [ ] Extracts text from all pages
- [ ] Returns ExtractionResult
- [ ] **Test:** `extract_pdf('document.pdf')`

### PowerPoint Extractor
- [ ] `extractors/pptx.py` created
- [ ] `extract_pptx()` reads slide text
- [ ] Preserves slide order
- [ ] Returns ExtractionResult
- [ ] **Test:** `extract_pptx('slides.pptx')`

### Excel Extractor
- [ ] `extractors/xlsx.py` created
- [ ] `extract_xlsx()` reads sheets
- [ ] Converts to table format
- [ ] Returns ExtractionResult
- [ ] **Test:** `extract_xlsx('data.xlsx')`

### Word Extractor
- [ ] `extractors/docx.py` created
- [ ] `extract_docx()` reads document
- [ ] Preserves section structure
- [ ] Returns ExtractionResult
- [ ] **Test:** `extract_docx('document.docx')`

### Google Sheets (Fallback: URL Scrape)
- [ ] `extractors/google_sheets.py` created
- [ ] `extract_google_sheets()` handles URL
- [ ] Returns ExtractionResult
- [ ] **Test:** `extract_google_sheets('https://docs.google.com/spreadsheets/...')`

### Google Docs (Fallback: URL Scrape)
- [ ] `extractors/google_docs.py` created
- [ ] `extract_google_docs()` handles URL
- [ ] Returns ExtractionResult
- [ ] **Test:** `extract_google_docs('https://docs.google.com/document/...')`

### Confidence Scoring
- [ ] `score_confidence()` function implemented
- [ ] Scores 0-1 based on:
  - [ ] Title found (0.3)
  - [ ] 2+ sections found (0.3)
  - [ ] Key points found (0.2)
  - [ ] No errors (0.2)

**Test All Extractors:**
```bash
# Create test files in code/tests/samples/
# - test_landing_page.html
# - sample.pdf
# - sample.pptx
# - sample.xlsx
# - sample.docx

# Run each extractor
python -c "from code.extractors.web import extract_web; result = extract_web('https://acme.com'); print(f'Confidence: {result[\"confidence\"]}')"
python -c "from code.extractors.pdf import extract_pdf; result = extract_pdf('code/tests/samples/sample.pdf'); print(f'Title: {result[\"title\"]}')"
# ... etc for all 7
```

---

## Phase 3: CLI Interface (Hour 3)

### Main CLI Command
- [ ] `cli/main.py` created
- [ ] Uses Click library
- [ ] `docgen ingest [SOURCE]` command works
- [ ] Accepts file path or URL
- [ ] Optional `--type` flag
- [ ] Calls `handle_input()`

### Progress Display
- [ ] Shows `⏳ Fetching...` messages
- [ ] Shows `⏳ Extracting...` messages
- [ ] Shows `✓ Done` when complete
- [ ] Shows `✗ Error` if fails

### Preview UI
- [ ] Displays extraction in formatted box
- [ ] Shows:
  - [ ] Source
  - [ ] Title
  - [ ] Confidence %
  - [ ] Number of sections/key points/tables
  - [ ] List of errors (if any)
- [ ] Formatted nicely (borders, spacing)

### User Interaction Menu
- [ ] Shows: `[Accept] [Edit] [Retry] [Cancel]`
- [ ] Accepts keyboard input
- [ ] Routes to correct next step

### Document Type Mapping
- [ ] If user chooses [Accept]:
  - [ ] Show doc type menu
  - [ ] Options: API Reference, GTM, Feature Guide, Product Spec, Process, Design, Content, Branding, ICP, Other
  - [ ] User confirms or changes
  - [ ] Continue to generation

**Test CLI:**
```bash
python code/cli/main.py ingest https://acme.com
python code/cli/main.py ingest document.pdf
python code/cli/main.py ingest slides.pptx --type pptx
```

---

## Phase 4: Integration & Output (Hour 4)

### Generation
- [ ] Calls docgen's `generate_doc()` function
  - [ ] Populates `DOC_CANONICAL_TEMPLATE.md`
  - [ ] Inserts extracted content into sections
  - [ ] Creates metadata
- [ ] Returns generated doc text

### Exit Gates
- [ ] Runs all 5 gates:
  - [ ] Gate 1: Validation (YAML, metadata)
  - [ ] Gate 2: Structure (all sections present)
  - [ ] Gate 3: Content (clear, accurate)
  - [ ] Gate 4: Quality (human + AI + token)
  - [ ] Gate 5: Shipping (all gates + DEBT)
- [ ] Shows results for each gate
- [ ] Fails if any gate fails

### DEBT Generation
- [ ] Creates `.DEBT.md` file
- [ ] Lists P1, P2, P3 items
- [ ] Based on what's missing from extracted content

### File Output
- [ ] Creates output folder structure:
  - [ ] `output/{domain}/v1.0/`
  - [ ] `.md` file
  - [ ] `.DEBT.md` file
  - [ ] `.metadata.json` file
- [ ] Filenames follow pattern: `{CATEGORY}_{TOPIC}_{VERSION}_{DATE}.md`

### Results Display
- [ ] Shows summary box with:
  - [ ] Document name
  - [ ] Quality score (X/100)
  - [ ] Token count
  - [ ] Status (PRODUCTION READY, NEEDS WORK, etc.)
  - [ ] File paths
  - [ ] DEBT summary
  - [ ] Next action options: [View Doc] [View DEBT] [Edit + Rerun] [Done]

**Test Integration:**
```bash
python code/cli/main.py ingest https://acme.com

# Should output:
# ✓ DOCUMENT GENERATED
# Document: Acme_API_Reference_v1.0
# Quality: 89/100
# ...
# Files saved to: output/web_dev/v1.0/
```

---

## Error Handling (Throughout)

- [ ] File not found → Show helpful error
- [ ] URL unreachable → Retry logic + fail gracefully
- [ ] Unsupported format → List supported formats
- [ ] Low confidence → Warn user, offer options
- [ ] Parse errors → Skip section, log, continue
- [ ] Gate failures → Show which gates failed + why

---

## Testing Strategy

### Unit Tests
- [ ] Each extractor works independently
- [ ] Confidence scoring correct
- [ ] Data structure validation

### Integration Tests
- [ ] CLI accepts input
- [ ] Handler routes to correct extractor
- [ ] Preview displays correctly
- [ ] User input (Accept/Edit/Retry) works
- [ ] Generation + gates run
- [ ] Files save correctly

### Manual Tests (Hand Testing)

**Test 1: Happy Path (Web)**
```bash
$ python code/cli/main.py ingest https://acme.com

[Extracts] → [Shows preview] → [User: Accept] → [Generates] → [Runs gates] → [Saves files] ✓
```

**Test 2: Happy Path (PDF)**
```bash
$ python code/cli/main.py ingest sample.pdf

[Same flow] ✓
```

**Test 3: Error Path**
```bash
$ python code/cli/main.py ingest nonexistent.pdf

[Shows error] → [Options: try different file, upload, cancel] ✓
```

**Test 4: Low Confidence**
```bash
$ python code/cli/main.py ingest minimal_content.pdf

[Warns: confidence 45%] → [User can accept anyway or retry] ✓
```

---

## Done Checklist

✅ **MVP Complete When:**

- [ ] Can ingest 7 input types (web, PDF, PPTX, XLSX, DOCX, Google Sheets, Google Docs)
- [ ] Shows extraction preview
- [ ] User can choose: [Accept] [Edit] [Retry]
- [ ] Generates doc from accepted extraction
- [ ] Runs all 5 exit gates
- [ ] Saves .md + .DEBT.md + .metadata.json
- [ ] Shows quality score + next actions
- [ ] All error cases handled gracefully

**Time:** 4 hours  
**Start:** Now  
**Finish:** When all ✅

---

## Stuck?

Common issues:

| Issue | Fix |
|-------|-----|
| PDF not extracting text | Try pdfplumber, not PyPDF2 |
| Google Sheets URL not working | Fall back to web scrape (requests + BeautifulSoup) |
| Click menu not responding | Ensure input() is used, not input prompt from Click |
| Confidence always 0 | Check scoring logic, ensure fields are populated |
| Files not saving | Check output/ folder exists, permissions OK |

---

## Next (After MVP Works)

- Phase 2: Confluence integration
- Phase 2: Jira integration
- Phase 2: Prompt builder
- Phase 3: Product Dev + Project Mgmt domains

But first: Get MVP working. 4 hours. Go.
