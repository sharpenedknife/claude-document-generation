# IMPLEMENTATION: Landing Page Extractor

**Status:** Ready to code  
**Priority:** P1 (MVP)  
**Complexity:** Medium  

---

## Specification

**Module:** `ingestion/extractors/landing_page.py`  
**Function:** `extract_landing_page(url: str) -> ExtractionResult`

---

## Input/Output

### Input
```python
url: str
# Example: "https://acme.com"
```

### Output
```python
ExtractionResult(
  title: str,
  sections: List[Section],
  key_points: List[str],
  confidence: float,  # 0.0-1.0
  errors: List[str]
)
```

### Section Structure
```python
@dataclass
class Section:
  name: str           # "Features", "Pricing", etc.
  type: str           # "hero", "features", "pricing", "about", "cta"
  content: str        # Full text of section
```

---

## Algorithm

```
1. Fetch URL (timeout 10s, retry 3x)
2. Parse HTML (BeautifulSoup)
3. Find title (from <title>, <h1>, og:title)
4. Find sections (h2/h3, semantic divs)
5. Score confidence (title + sections + key points)
6. Extract key points (bullets, bold text)
7. Identify section types (features, pricing, etc.)
8. Return JSON with confidence >= 0.6 for success
```

---

## Test Cases

### Test 1: Real landing page
```python
result = extract_landing_page("https://github.com")
assert result.title  # Has title
assert len(result.sections) >= 3
assert result.confidence > 0.70
assert result.errors == []
```

### Test 2: Simple HTML
```python
html = """
<html>
  <title>Test Product</title>
  <h1>Hero Section</h1>
  <h2>Features</h2>
  <ul><li>Fast</li><li>Reliable</li></ul>
  <h2>Pricing</h2>
  <p>$9/month</p>
</html>
"""
result = extract_landing_page("file:///tmp/test.html")
assert result.title == "Test Product"
assert len(result.sections) >= 2
assert result.confidence >= 0.60
```

### Test 3: Network error
```python
result = extract_landing_page("https://invalid-12345.com")
# Should handle gracefully: raise ExtractionError or return errors[]
```

### Test 4: Empty page
```python
html = "<html><title>Empty</title><body></body></html>"
# Should fail with confidence < 0.6 or ExtractionError
```

---

## Code Template

```python
# ingestion/extractors/landing_page.py

from dataclasses import dataclass
from typing import List
import requests
from bs4 import BeautifulSoup

@dataclass
class Section:
    name: str
    type: str
    content: str

@dataclass
class ExtractionResult:
    title: str
    sections: List[Section]
    key_points: List[str]
    confidence: float
    errors: List[str]

def extract_landing_page(url: str) -> ExtractionResult:
    """Extract content from landing page URL"""
    # 1. Fetch URL (with retries)
    # 2. Parse HTML
    # 3. Extract title
    # 4. Extract sections
    # 5. Extract key points
    # 6. Score confidence
    # 7. Return result
    pass

def _fetch_url(url: str) -> str:
    """Fetch with timeout 10s, retry 3x"""
    pass

def _extract_sections(soup) -> List[Section]:
    """Find h2/h3 + content"""
    pass

def _score_confidence(result: ExtractionResult) -> float:
    """Calculate 0-1.0 score"""
    pass
```

---

## Dependencies
```
requests
beautifulsoup4
lxml
```

---

## Success (MVP)
✓ Extracts title  
✓ Extracts 2+ sections  
✓ Confidence >= 0.6  
✓ Handles errors (no crashes)  
✓ Returns < 5 seconds  

