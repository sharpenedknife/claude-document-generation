# CLI MVP Spec

**Command:** `docgen ingest URL landing-page`

---

## User Flow (Terminal Output)

```
$ docgen ingest https://acme.com landing-page

⏳ Fetching https://acme.com...
✓ Fetched

⏳ Extracting content...
✓ Extracted

┌──────────────────────────────────────────┐
│ EXTRACTED CONTENT                        │
├──────────────────────────────────────────┤
│                                          │
│ Title: Acme - Enterprise API Platform   │
│ Sections found: 4                        │
│ Confidence: 82%                          │
│                                          │
│ Sections:                                │
│ • Hero                                   │
│ • Features                               │
│ • Pricing                                │
│ • Contact                                │
│                                          │
│ Key points (first 5):                    │
│ • Real-time data integration             │
│ • 99.99% uptime SLA                      │
│ • Enterprise-grade security              │
│                                          │
├──────────────────────────────────────────┤
│ [A] Accept  [E] Edit  [R] Retry [Q] Quit │
└──────────────────────────────────────────┘

→ User presses: A
```

---

## After Accept: Doc Type Selection

```
? What type of document?

  1. API Reference
  2. GTM Strategy
  3. Feature Guide
  4. Product Specification
  5. Design Overview
  6. Other (manually specify)

→ User selects: 1
```

---

## Generation

```
⏳ Generating API Reference doc...
  Using: extracted content + DOC_CANONICAL_TEMPLATE

⏳ Running exit gates...
  Gate 1: Validation ✓
  Gate 2: Structure ✓
  Gate 3: Content Quality ✓
  Gate 4: Human+AI+Token ✓
  Gate 5: Shipping ✓

✓ ALL GATES PASSED
```

---

## Result

```
┌──────────────────────────────────────────┐
│ ✓ DOCUMENT GENERATED                     │
├──────────────────────────────────────────┤
│                                          │
│ Title: Acme API Reference                │
│ Quality Score: 89/100                    │
│ Tokens: 2,847 / 3,000 (OK)               │
│ Status: PRODUCTION READY                 │
│                                          │
│ Saved to:                                │
│ output/web_dev/v1.0/                     │
│   Acme_API_Reference_v1.0.md             │
│   Acme_API_Reference_v1.0.DEBT.md        │
│   Acme_API_Reference_v1.0.metadata.json  │
│                                          │
│ DEBT Summary (what's missing):           │
│ P1 (High):                               │
│   - Authentication examples              │
│   - Error codes reference                │
│ P2 (Medium):                             │
│   - Webhook guide                        │
│   - Rate limiting details                │
│                                          │
│ What's next?                             │
│ • View doc: cat output/.../Acme_API...  │
│ • Edit doc: edit output/.../Acme_API... │
│ • Done                                   │
│                                          │
├──────────────────────────────────────────┤
│ [V] View  [E] Edit  [D] Done             │
└──────────────────────────────────────────┘

→ User presses: V
(Shows generated doc)

→ User presses: D
(Exits)

Done! Generated doc is ready.
```

---

## Code Structure

```python
# cli/commands/ingest.py

import click
from ingestion.extractors.landing_page import extract_landing_page
from ingestion.mappers import map_to_doc_type
from generators import generate_doc
from gates import run_all_gates

@click.command()
@click.argument('url')
@click.argument('source_type')
def ingest(url, source_type):
    """
    Ingest content from URL and generate doc.
    
    $ docgen ingest https://acme.com landing-page
    """
    
    # Step 1: Extract
    click.echo(f"⏳ Fetching {url}...")
    result = extract_landing_page(url)
    click.echo("✓ Extracted\n")
    
    # Step 2: Show preview + user choice
    _show_preview(result)
    choice = click.prompt("Action", type=click.Choice(['A', 'E', 'R', 'Q']))
    
    if choice == 'Q':
        click.echo("Cancelled.")
        return
    elif choice == 'R':
        ingest(url, source_type)  # Retry
        return
    elif choice == 'E':
        result = _edit_extraction(result)
    
    # Step 3: Map to doc type
    doc_type = _ask_doc_type()
    
    # Step 4: Generate doc
    click.echo("\n⏳ Generating doc...")
    doc = generate_doc(result, doc_type)
    
    # Step 5: Run gates
    click.echo("⏳ Running exit gates...")
    gates_result = run_all_gates(doc)
    if not gates_result.passed_all:
        click.echo("✗ Gates failed. See DEBT.md")
        return
    
    # Step 6: Show result + save
    click.echo("✓ ALL GATES PASSED\n")
    _show_result(doc, gates_result)
    
    # Final choice
    choice = click.prompt("What next?", type=click.Choice(['V', 'E', 'D']))
    if choice == 'V':
        _view_doc(doc)
    elif choice == 'E':
        _edit_doc(doc)

def _show_preview(extraction):
    """Display extraction preview"""
    click.echo(f"Title: {extraction.title}")
    click.echo(f"Sections: {len(extraction.sections)}")
    click.echo(f"Confidence: {extraction.confidence*100:.0f}%")
    # ... show sections, key points

def _ask_doc_type():
    """Ask user to choose doc type"""
    choices = ["API Reference", "GTM Strategy", "Feature Guide", "Other"]
    return click.prompt("Doc type", type=click.Choice(choices))

def _show_result(doc, gates):
    """Display generation result"""
    click.echo(f"Quality: {gates.quality_score}/100")
    click.echo(f"Tokens: {gates.token_count} / {gates.token_budget}")
    # ... show DEBT items
```

---

## Exit Conditions

| User Action | Result |
|-------------|--------|
| [A] Accept | Generate → Gates → Save → Show result |
| [E] Edit | Editor opens → Re-extract → Show preview again |
| [R] Retry | Fetch URL again from start |
| [Q] Quit | Cancel, discard, exit |

---

## Files Created

On success, creates 3 files in `output/`:

```
output/
  {DOMAIN}/v1.0/
    {TITLE}_v1.0.md          ← Generated doc
    {TITLE}_v1.0.DEBT.md     ← Debt items
    {TITLE}_v1.0.metadata.json ← Metadata
```

Example:
```
output/web_dev/v1.0/
  Acme_API_Reference_v1.0.md
  Acme_API_Reference_v1.0.DEBT.md
  Acme_API_Reference_v1.0.metadata.json
```

---

## Error Handling (User-Friendly)

| Error | Message | Action |
|-------|---------|--------|
| URL unreachable | "Can't reach URL. Check internet or URL." | Retry or quit |
| Parse error | "Can't read page (invalid HTML)." | Retry or quit |
| No content | "No content found on page." | Try different URL or quit |
| Low confidence | "Low confidence (45%). Edit or retry?" | User chooses |

No crashes. Graceful failures.

---

## Testing

Test the flow:
```bash
$ docgen ingest https://github.com landing-page
$ docgen ingest https://stripe.com landing-page
$ docgen ingest https://invalid-url.com landing-page  # Should fail gracefully
```

All 3 should work without crashes.

