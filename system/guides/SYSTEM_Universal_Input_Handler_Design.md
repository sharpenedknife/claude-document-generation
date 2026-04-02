# SYSTEM: Universal Input Handler Design

**Purpose:** Accept any content source, extract structured data, prepare for doc generation.

**Scope (MVP):** 7 input types. One handler. One flow.

---

## Architecture

```
Input (7 types)
  ↓
Detect Type
  ↓
Extract Content (type-specific)
  ↓
Normalize to JSON
  ↓
Score Confidence
  ↓
Show Preview to User
  ↓
User Chooses:
  ✓ Accept → Generate Doc
  ✓ Edit → Modify extraction
  ✗ Retry → Different source
```

---

## Supported Input Types

| Type | Format | Source | Method |
|------|--------|--------|--------|
| Web Link | HTML | https://example.com | URL fetch + parse |
| PDF | PDF file | document.pdf | Upload + text extract |
| Presentation | PPTX/PDF | slides.pptx | Upload + slide text extract |
| Excel | XLSX | data.xlsx | Upload + sheet extract |
| Word | DOCX | document.docx | Upload + text extract |
| Google Sheet | URL | https://sheets.google.com/... | URL fetch + API |
| Google Docs | URL | https://docs.google.com/... | URL fetch + API |

---

## Extraction Output (Unified)

All extractors return same JSON:

```json
{
  "title": "Extracted Title",
  "type_detected": "api_reference|gtm_strategy|feature_guide|product_spec|process|other",
  "sections": [
    {
      "name": "Section Name",
      "content": "Section text content",
      "type": "hero|features|pricing|process|table|overview|other"
    }
  ],
  "key_points": ["Point 1", "Point 2", "Point 3"],
  "tables": [
    {
      "title": "Table name",
      "rows": [["col1", "col2"], ["val1", "val2"]]
    }
  ],
  "confidence": 0.82,
  "source_type": "web|pdf|pptx|xlsx|docx|google_sheets|google_docs",
  "errors": ["warning 1", "warning 2"],
  "raw_content": "Full text extracted"
}
```

---

## Type Detection (Smart)

If user doesn't specify input type, detect from:
- File extension (.pdf, .docx, .xlsx)
- URL pattern (sheets.google.com, docs.google.com, github.com)
- Content headers (Content-Type for URLs)

Example:
```
$ docgen ingest document.pdf
  → Auto-detect: PDF
  → Extract pages → text

$ docgen ingest https://docs.google.com/spreadsheets/...
  → Auto-detect: Google Sheets
  → Fetch + extract rows

$ docgen ingest slides.pptx
  → Auto-detect: PPTX
  → Extract slides → combine text
```

---

## Error Handling (MVP)

| Error | Behavior |
|-------|----------|
| File not found | Fail with message |
| URL unreachable | Retry 2x, then fail |
| Unsupported format | Suggest supported formats |
| Empty content | Warn, ask to retry |
| Parse error | Skip section, continue |
| Confidence < 50% | Warn user, offer to edit |

---

## Success Criteria

✓ Accept any of 7 input types  
✓ Extract title + sections + key points  
✓ Confidence score (0-1)  
✓ Return unified JSON  
✓ Handle errors gracefully  
✓ User can preview + edit + regenerate  

---

## Dependencies

- **Web (URL):** requests, BeautifulSoup
- **PDF:** pdfplumber or PyPDF2
- **PPTX:** python-pptx
- **XLSX:** openpyxl or pandas
- **DOCX:** python-docx
- **Google Sheets/Docs:** google-api-python-client (optional, falls back to web scrape)

---

## Next: Implementation

See: IMPLEMENTATION_Universal_Input_Handler.md
