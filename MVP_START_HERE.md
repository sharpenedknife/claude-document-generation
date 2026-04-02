# MVP Build: Start Here

**Status:** 3 design docs complete. Ready to code.

## Read These First (15 mins)

1. **SYSTEM_Universal_Input_Handler_Design.md** — What we're building
2. **IMPLEMENTATION_Universal_Input_Handler.md** — Exact specs + examples
3. **CLI_MVP_Spec.md** — User interface + flows

## What You're Building (4 Hours)

### Code Structure
```
code/
├── cli/
│   └── main.py              ← Click CLI entry point
├── ingestion/
│   └── handler.py           ← Universal input handler
├── extractors/
│   ├── web.py              ← URL → HTML parse
│   ├── pdf.py              ← PDF → text
│   ├── pptx.py             ← PPTX → slides
│   ├── xlsx.py             ← XLSX → sheets
│   ├── docx.py             ← DOCX → text
│   ├── google_sheets.py     ← Sheets URL → rows
│   └── google_docs.py       ← Docs URL → text
├── generation/
│   └── generator.py         ← Template → doc
└── gates/
    └── validator.py         ← Run 5 exit gates
```

### 4-Hour Breakdown

**Hour 1: Universal Input Handler**
```python
# ingestion/handler.py
def handle_input(source: str) -> ExtractionResult:
    - Detect input type (web, pdf, pptx, xlsx, docx, google_sheets, google_docs)
    - Route to correct extractor
    - Normalize output
    - Score confidence
    - Return result
```

**Hour 2: Extractors (All 7)**
```python
# extractors/web.py, pdf.py, pptx.py, xlsx.py, docx.py, google_sheets.py, google_docs.py
# Each returns: ExtractionResult with title, sections[], key_points[], tables[], confidence
```

**Hour 3: CLI Interface**
```python
# cli/main.py
@click.command()
@click.argument('source')
@click.option('--type', default=None)
def ingest(source, type):
    - Call handler.handle_input()
    - Show preview (formatted box)
    - Ask user: [Accept] [Edit] [Retry]
    - If Accept: map doc type + generate
    - Show results
```

**Hour 4: Integration**
```python
# cli/main.py (continued)
- Call docgen's own generator
- Run 5 exit gates
- Save to output/ folder
- Show: quality score, DEBT, next actions
```

## Dependencies to Install

```bash
pip install click requests beautifulsoup4 pdfplumber python-pptx openpyxl python-docx google-api-python-client
```

## Start Coding

**Option A: Quick & Dirty (Recommended for MVP)**
1. Code everything in one `main.py` file
2. Get working first
3. Refactor structure later

**Option B: Clean Structure (Recommended for Phase 2)**
1. Folder structure above
2. Modular from day 1
3. Easier to test

**Recommendation:** Option B (takes same time, saves future pain)

## Test As You Go

After each piece works, test:
```bash
# Test 1: Web extractor
$ python -c "from code.extractors.web import extract_web; print(extract_web('https://acme.com'))"

# Test 2: PDF extractor
$ python -c "from code.extractors.pdf import extract_pdf; print(extract_pdf('document.pdf'))"

# Test 3: CLI
$ python code/cli/main.py ingest https://acme.com
$ python code/cli/main.py ingest document.pdf
```

## MVP Success Criteria

✓ Can ingest any of 7 input types  
✓ Shows preview  
✓ User chooses: [Accept] [Edit] [Retry]  
✓ Generates doc  
✓ Runs 5 exit gates  
✓ Saves to output/ folder  
✓ Shows quality score + DEBT  

When all ✓, MVP is done.

## Next (Phase 2)

After MVP works:
- [ ] Add Confluence integration
- [ ] Add Jira integration
- [ ] Add Prompt builder
- [ ] Add Product Dev + Project Mgmt domains
- [ ] Add metrics/dashboard

But first: Get MVP working. Everything else flows from that.

---

**Current Time Estimate: 4 hours to working MVP**

Let's go.
