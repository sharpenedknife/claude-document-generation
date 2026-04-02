# Ingestion System Design

## One-Sentence Purpose
Extract title, sections, key points from landing page HTML → structured JSON → user decides action.

---

## Architecture

```
URL Input
  ↓
Fetch + Parse HTML
  ↓
Extract: title, sections, key_points, confidence
  ↓
Return JSON
  ↓
User Preview (✓ Accept | ✗ Reject | ⟳ Retry)
  ↓
Map to Doc Type
  ↓
Generate Doc (using template + extracted content)
  ↓
Run 5 Exit Gates
  ↓
Save to output/ + show result
```

---

## Extraction Layer

**Input:** URL (string)  
**Output:** ExtractionResult (JSON)

```json
{
  "title": "Acme - Enterprise API Platform",
  "sections": [
    {"name": "Hero", "type": "hero", "content": "text..."},
    {"name": "Features", "type": "features", "content": "text..."}
  ],
  "key_points": ["Real-time", "99.99% uptime"],
  "confidence": 0.82,
  "errors": []
}
```

**Extraction Process:**
1. Fetch URL (timeout 10s, retry 3x)
2. Parse HTML (BeautifulSoup)
3. Find sections: h1, h2, divs with semantic classes
4. Extract text + type (hero/features/pricing/about/cta)
5. Score confidence (sections found / expected)
6. Return JSON

**Confidence Scoring:**
- Title found: +20%
- 3+ sections: +60%
- Key points extracted: +20%
- Result: 0-100%, capped at 100%

---

## Error Handling

| Error | Action |
|-------|--------|
| Network unreachable | Retry 3x, then fail with "URL not reachable" |
| HTML parse error | Skip section, continue, log in errors[] |
| No title found | Fail: "No content found" |
| Confidence < 60% | Warn user, allow edit or retry |
| Timeout (>10s) | Fail: "Page took too long to load" |

---

## Success Criteria (MVP)

✓ Extracts title  
✓ Extracts 2+ sections  
✓ Confidence > 60%  
✓ User can preview before accepting  
✓ Handles network errors gracefully  

---

## Next Layer (Mapping)

After extraction:
1. User sees preview
2. User chooses: [Accept] [Edit] [Retry]
3. If Accept → Ask doc type
4. Map to DOC_CANONICAL_TEMPLATE
5. Generate doc
6. Run 5 gates
7. Save

