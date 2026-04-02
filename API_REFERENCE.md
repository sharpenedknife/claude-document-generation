# Docgen HTTP API Reference

**Base URL:** `http://localhost:5000`  
**Version:** 1.0  
**Authentication:** None (configure ANTHROPIC_API_KEY in .env)

---

## Endpoints

### Health Check
```
GET /health
```

**Response (200):**
```json
{
  "status": "healthy",
  "timestamp": "2026-04-02T14:30:00",
  "version": "1.0"
}
```

---

### List Projects
```
GET /api/docgen/projects
```

**Response (200):**
```json
{
  "status": "ok",
  "projects": [
    {
      "id": 1,
      "name": "Fast Product MVP",
      "time": "2h",
      "questions": 7
    },
    ...
  ],
  "total": 10
}
```

---

### Generate Documentation
```
POST /api/docgen/generate
Content-Type: application/json
```

**Request:**
```json
{
  "project": 1,
  "answers": {
    "q0": "A SaaS documentation platform",
    "q1": "Product managers at startups",
    "q2": "Manual docs take 2-4 weeks",
    "q3": "AI-powered generation with quality gates",
    "q4": "Q2 2026",
    "q5": "Python + Claude API",
    "q6": "$50,000"
  },
  "destinations": ["zip", "github"]
}
```

**Response (200):**
```json
{
  "status": "SUCCESS",
  "document": {
    "filename": "PRD.md",
    "word_count": 2847,
    "tokens": 710
  },
  "quality": {
    "score": 87,
    "status": "PRODUCTION_READY",
    "gates_passed": 5
  },
  "delivery": {
    "zip": {
      "status": "SUCCESS",
      "path": "output/docgen_20260402_142530.zip"
    }
  },
  "generation_id": 1
}
```

**Error Response (400):**
```json
{
  "status": "FAILED",
  "error": "Quality gate validation failed",
  "details": ["Missing section: Overview"],
  "quality_score": 45
}
```

**Required Fields:**
- `project` (integer, 1-10): Project type ID
- `answers` (object): Questionnaire answers (q0-q7)
- `destinations` (array): ["zip", "github", "notion", "drive"]

**Valid Projects:**
- 1: Fast Product MVP
- 2: Feature Release
- 3: Workflow Automation
- 4: Revenue Stream
- 5: Brand Marketing
- 6: Product Marketing
- 7: Summarize Files
- 8: Custom Docs
- 9: AI Skill
- 10: Claude Project

**Valid Destinations:**
- `zip` - Create .zip file locally
- `github` - Push to GitHub (stub)
- `notion` - Sync to Notion (stub)
- `drive` - Upload to Google Drive (stub)
- `email` - Email results (stub)

---

### Validate Document
```
POST /api/docgen/validate
Content-Type: application/json
```

**Request:**
```json
{
  "content": "---\ntitle: Test Doc\n...\n---\n\n## Overview\nTest\n...",
  "category": "Product"
}
```

**Response (200):**
```json
{
  "status": "ok",
  "validation": {
    "gate_1_validation": true,
    "gate_2_structure": true,
    "gate_3_content": true,
    "gate_4": {
      "pass": true,
      "metrics": {
        "tokens": 710,
        "budget": 3000,
        "quality_score": 87
      }
    },
    "gate_5_shipping": true,
    "status": "PRODUCTION_READY",
    "passed_gates": 5
  },
  "production_ready": true
}
```

**Categories:**
- Product
- Design
- Engineering
- Business
- Skill
- Project
- Analysis
- Custom

---

### Get Generation Status
```
GET /api/docgen/status
GET /api/docgen/status?id=1
```

**Response (200) - All generations:**
```json
{
  "status": "ok",
  "total_generations": 3,
  "recent": [
    {
      "timestamp": "2026-04-02T14:30:00",
      "project_id": 1,
      "status": "SUCCESS",
      "quality_score": 87,
      "destinations": ["zip"]
    }
  ]
}
```

**Response (200) - Specific generation:**
```json
{
  "status": "found",
  "generation": {
    "timestamp": "2026-04-02T14:30:00",
    "project_id": 1,
    "status": "SUCCESS",
    "quality_score": 87,
    "destinations": ["zip"]
  }
}
```

**Response (404):**
```json
{
  "status": "not_found",
  "error": "Generation ID 999 not found"
}
```

---

### Get API Information
```
GET /api/docgen/info
```

**Response (200):**
```json
{
  "name": "Docgen API",
  "version": "1.0",
  "status": "operational",
  "endpoints": {
    "POST /api/docgen/generate": "Generate documentation",
    "GET /api/docgen/projects": "List available projects",
    "GET /api/docgen/status": "Get generation status",
    "POST /api/docgen/validate": "Validate document",
    "GET /health": "Health check"
  },
  "generations_count": 3
}
```

---

## Error Codes

| Code | Error | Meaning |
|------|-------|---------|
| 200 | OK | Success |
| 400 | Bad Request | Invalid input (missing fields, invalid project) |
| 404 | Not Found | Resource not found (invalid generation ID, endpoint) |
| 500 | Server Error | Internal error during generation |

---

## Examples

### cURL - Generate PRD

```bash
curl -X POST http://localhost:5000/api/docgen/generate \
  -H "Content-Type: application/json" \
  -d '{
    "project": 1,
    "answers": {
      "q0": "A SaaS documentation platform",
      "q1": "Product managers at startups",
      "q2": "Manual docs take weeks",
      "q3": "AI-powered generation",
      "q4": "Q2 2026",
      "q5": "Python + Claude",
      "q6": "$50,000"
    },
    "destinations": ["zip"]
  }'
```

### Python - Generate with Requests

```python
import requests
import json

response = requests.post(
    'http://localhost:5000/api/docgen/generate',
    json={
        'project': 1,
        'answers': {
            'q0': 'My product...',
            'q1': 'Target users...',
            # ... q2-q6
        },
        'destinations': ['zip']
    }
)

result = response.json()
if result['status'] == 'SUCCESS':
    print(f"Quality: {result['quality']['score']}/100")
    print(f"Zip: {result['delivery']['zip']['path']}")
```

### JavaScript - Fetch API

```javascript
const response = await fetch('http://localhost:5000/api/docgen/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    project: 1,
    answers: {
      q0: 'My product description...',
      q1: 'Target users...',
      // ... q2-q6
    },
    destinations: ['zip']
  })
});

const result = await response.json();
console.log(`Quality Score: ${result.quality.score}/100`);
console.log(`Status: ${result.quality.status}`);
```

---

## Rate Limiting

Currently: No rate limiting (can be added in production)

**Recommended for production:**
- 100 requests per minute per IP
- 10 concurrent generations
- 30 second timeout per request

---

## Best Practices

1. **Always validate responses** - Check `status` field first
2. **Handle errors gracefully** - Implement retry logic for 5xx errors
3. **Use appropriate projects** - Choose project that matches your needs
4. **Provide complete answers** - All questionnaire fields required
5. **Monitor quality scores** - Ensure score ≥80 before using docs
6. **Cache projects list** - Use /api/docgen/projects once at startup
7. **Implement logging** - Track all API calls for debugging

---

## Limits

| Limit | Value |
|-------|-------|
| Max document size | 50KB |
| Max request size | 16MB |
| Max questions per project | 8 |
| Max destinations per request | 5 |
| Generation timeout | 300 seconds |
| Quality score min | 0 |
| Quality score max | 100 |
| Token budget min | 1500 |
| Token budget max | 4500 |

---

**API Version:** 1.0  
**Last Updated:** 2026-04-02  
**Status:** ✅ Production Ready
