# File Naming Convention

All files follow strict naming pattern for clarity, searchability, and automation.

---

## Master Pattern

```
{CATEGORY}_{TOPIC}_{VERSION}_{DATE}.md
```

---

## Definitions

### CATEGORY (Required)

What domain or type of document:

| Category | Use For | Examples |
|----------|---------|----------|
| GTM | Go-to-market | GTM_Strategy, GTM_Competitive_Analysis |
| DESIGN | Design/UX docs | DESIGN_Button_System, DESIGN_Dark_Mode |
| BRANDING | Brand/messaging | BRANDING_Voice, BRANDING_Visual_Identity |
| CONTENT | Content strategy/guidelines | CONTENT_Blog_Strategy, CONTENT_SEO_Guide |
| ICP | Customer profiles | ICP_Enterprise_CTOs, ICP_Mid_Market_SMB |
| WEB | Web development | WEB_React_Setup, WEB_Deploy_Guide |
| SKILL | Reusable workflows | SKILL_Market_Research, SKILL_Content_Optimization |
| SYSTEM | Docgen framework | SYSTEM_Exit_Rules, SYSTEM_Token_Optimization |

### TOPIC (Required)

Main topic of the document (snake_case):

**Good:**
- `GTM_Strategy`
- `Competitive_Analysis`
- `Button_Component`
- `Voice_Guidelines`

**Bad:**
- `GTM Strategy` (spaces, not snake_case)
- `gtm_strategy` (lowercase, inconsistent with pattern)
- `GTM_Strat` (abbreviated, unclear)
- `Strategy` (missing category)

### VERSION (Optional, include if needed)

Only if multiple versions exist in parallel:

```
v1.0      # Initial release
v1.1      # Minor update
v2.0      # Major revision
```

**Include VERSION when:**
- Multiple versions in active use (v1.0, v2.0)
- Backwards compatibility matters

**Skip VERSION when:**
- Only one version exists
- Versioning tracked in folder structure instead (better)

### DATE (Optional, include for dated docs)

Publication or revision date (YYYY-MM-DD):

```
2026-04-02
2026-Q1
2026
```

**Include DATE when:**
- Content has shelf life (GTM strategies, market analysis)
- Quarterly/annual updates
- Need to distinguish "old" from "current"

**Skip DATE when:**
- Evergreen content (How to Install Node)
- Versioning via v1.0, v2.0 instead

---

## Complete Examples

### Pattern 1: Evergreen setup guide (no version, no date)
```
WEB_React_Setup_Guide.md
DESIGN_Button_Component.md
SYSTEM_Exit_Rules.md
```

### Pattern 2: Dated strategy doc
```
GTM_Strategy_2026-04-02.md
GTM_Strategy_2026-Q1.md
GTM_Strategy_2026.md
```

### Pattern 3: Versioned competitive analysis
```
GTM_Competitive_Analysis_v1.0.md
GTM_Competitive_Analysis_v2.0.md
CONTENT_Blog_Strategy_v1.1.md
```

### Pattern 4: All three (rare, only if absolutely necessary)
```
GTM_Strategy_v2.0_2026-Q2.md
DESIGN_System_v3.1_2026-04-15.md
```

---

## File Types & Companions

### Main document
```
{NAME}.md
```

### Companion debt file
```
{NAME}.DEBT.md
```

### Companion metadata
```
{NAME}.metadata.json
```

**All three always together:**
```
GTM_Strategy_2026.md           ← Main doc
GTM_Strategy_2026.DEBT.md      ← Debt tracking
GTM_Strategy_2026.metadata.json ← Generation metadata
```

---

## Forbidden Characters & Patterns

❌ **NEVER use:**
- Spaces (use snake_case)
- CamelCase (use snake_case)
- Dashes/hyphens (use underscores)
- Special chars (@#$%^&)
- Abbreviations (use full words)
- Emojis
- Multiple consecutive underscores

✅ **Always use:**
- Lowercase for domains (gtm, not GTM, except CATEGORY prefix)
- snake_case for spacing
- Full words (not acronyms, except in CATEGORY)
- YYYY-MM-DD for dates

**Examples:**

```
❌ BAD
GTM Strategy 2026.md
gtm-strategy-2026.md
GTM__Strategy.md
GTM_Strat_v1.md
GTM_Competitive_Analysis_(final).md

✅ GOOD
GTM_Strategy_2026.md
GTM_Competitive_Analysis_v1.0.md
DESIGN_Dark_Mode_Guide.md
BRANDING_Voice_Guidelines_2026-Q1.md
WEB_React_Performance_Optimization.md
```

---

## Special Cases

### System/Framework Documents
Prefix with SYSTEM_:
```
SYSTEM_Exit_Rules.md
SYSTEM_Token_Optimization_Guide.md
SYSTEM_Production_Folder_Structure.md
DOC_Canonical_Template.md (no SYSTEM_ needed, universal)
```

### Skill Documents
Prefix with SKILL_:
```
SKILL_Market_Research_Framework.md
SKILL_Content_Gap_Analysis.md
SKILL_GTM_Competitive_Mapping.md
```

### Template Documents
Prefix with TEMPLATE_:
```
TEMPLATE_GTM_Builder_Questionnaire.md
TEMPLATE_Design_System_Doc.md
TEMPLATE_ICP_Definition.md
```

### Archived/Deprecated
Include [ARCHIVED] or [DEPRECATED] prefix:
```
[ARCHIVED]_GTM_Strategy_2025.md
[DEPRECATED]_Old_Design_System_v0.9.md
```

---

## Folder + Filename Combined

Full path should make sense:

```
✅ GOOD STRUCTURE:
output/gtm/v1.0/GTM_Strategy_2026-Q1.md
output/gtm/v1.0/GTM_Strategy_2026-Q1.DEBT.md

output/design/v1.0/DESIGN_Button_System.md
output/design/v1.0/DESIGN_Button_System.DEBT.md

builders/gtm/GTM_Builder_Rules.md
builders/gtm/examples/GTM_Strategy_Example_v1.md

❌ BAD STRUCTURE:
output/GTM_Strategy_2026-Q1.md (no version folder)
design/button/DESIGN_Button.md (redundant "design" in name + folder)
v1.0/GTM_Strategy_2026.md (version in folder + filename)
```

---

## Lookup & Search

Good file naming = easy to find.

**Search examples:**

```bash
# Find all GTM docs
ls output/gtm/*/GTM_*.md

# Find all v1.0 docs across domains
find output/*/v1.0/ -name "*.md"

# Find archived docs
find . -name "[ARCHIVED]_*.md"

# Find recent docs
ls -lt output/*/*.md | head -20

# Find by date
ls output/*/v*/*_2026-04*.md
```

---

## Naming Checklist

Before saving a file, verify:

- [ ] CATEGORY correct (GTM|DESIGN|BRANDING|CONTENT|ICP|WEB|SKILL|SYSTEM)
- [ ] TOPIC clear and specific (snake_case, full words)
- [ ] VERSION included if multiple versions exist (v1.0, v2.0)
- [ ] DATE included if time-sensitive (YYYY-MM-DD or YYYY-Q#)
- [ ] File uses underscores (not spaces, not dashes)
- [ ] No special characters or emojis
- [ ] DEBT.md companion exists (if applicable)
- [ ] metadata.json companion exists (if generated)
- [ ] Full path makes sense (folder + filename)
- [ ] Can be found with simple command-line search

---

## Automation: Naming Rules in Builder

Builder should enforce:

1. User provides CATEGORY (dropdown)
2. User provides TOPIC (text input, auto snake_case)
3. Builder auto-detects VERSION (if v1.0 exists, suggest v1.1)
4. Builder auto-detects DATE (if user selects "dated doc", use today)
5. Generate filename: `{CATEGORY}_{TOPIC}_{VERSION}_{DATE}.md`
6. Create companions automatically:
   - `{NAME}.DEBT.md`
   - `{NAME}.metadata.json`
7. Validate: filename searchable, no forbidden chars

**Validation**
```javascript
// Pseudocode
filename = `${CATEGORY}_${TOPIC}${VERSION}${DATE}.md`;

// Check for forbidden chars
if (filename.contains(/[\s\-()]/)) {
  error("File contains spaces, dashes, or special chars");
}

// Check length
if (filename.length > 100) {
  error("Filename too long (>100 chars)");
}

// Check uniqueness
if (fileExists(filename)) {
  error("File already exists. Update version or use new topic.");
}

// All good - create file + companions
create(filename);
create(`${filename}.DEBT.md`);
create(`${filename}.metadata.json`);
```

---

## Migration from Old Names

If you have existing files with bad names, rename them:

```bash
# Before
DESIGN System Components v1.md
gtm-competitive-analysis.md
Content-Strategy-Q1-2026.md

# After
DESIGN_System_Components_v1.0.md
GTM_Competitive_Analysis.md
CONTENT_Strategy_2026-Q1.md
```

Use this script to verify all files in a folder:

```bash
#!/bin/bash
# Check file naming compliance

for file in *.md; do
  # Filename must match pattern
  if [[ ! $file =~ ^[A-Z][A-Z0-9_]*_[a-z0-9_]+(_v[0-9]\.[0-9])?(_[0-9]{4}(-[0-9]{2})?)?\.md$ ]]; then
    echo "❌ BAD: $file"
  else
    echo "✅ GOOD: $file"
  fi
done
```

---

## Real-World Naming Examples

```
✅ GOOD NAMES (production-ready):

GTM_Strategy_2026-Q1.md
GTM_Competitive_Analysis_v1.0.md
GTM_Sales_Playbook_Enterprise.md
GTM_ICP_Definition_Mid_Market.md

DESIGN_Button_System.md
DESIGN_Dark_Mode_Guide_v1.0.md
DESIGN_Typography_Scale.md
DESIGN_Color_Palette_2026.md

BRANDING_Voice_Guidelines.md
BRANDING_Visual_Identity_v2.0.md
BRANDING_Messaging_Framework.md

CONTENT_Blog_Strategy_2026.md
CONTENT_SEO_Playbook_v1.1.md
CONTENT_Gap_Analysis_Q1_2026.md

ICP_Enterprise_CTOs.md
ICP_Mid_Market_Product_Leaders.md
ICP_Startup_Founders.md

WEB_React_Setup_Guide.md
WEB_Deploy_to_Production.md
WEB_Performance_Optimization_v1.0.md

SKILL_Market_Research_Framework.md
SKILL_Content_Gap_Analysis.md
SKILL_Competitive_Mapping.md

SYSTEM_Exit_Rules.md
SYSTEM_Token_Optimization_Guide.md
```

Consistency across all these enables:
- Easy discovery
- Automated processing
- Clear versioning
- Team communication
- Time-based archiving
