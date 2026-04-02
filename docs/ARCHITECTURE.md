# docgen System Architecture

How the documentation generation system works.

---

## Core Components

### 1. Framework (system/)

**Purpose:** Authoritative reference for all standards

**Contents:**
- `guides/` — 10 production standards (Content Guide, Exit Rules, Token Optimization, etc.)
- `templates/` — Output templates (canonical doc structure, DEBT template, project instructions)
- `checklists/` — Quality verification (human pass, AI pass, token efficiency)
- `examples/` — Perfect example docs showing all standards applied

**Usage:** Everything else references these guides. They are read-only truth sources.

### 2. Builders (builders/)

**Purpose:** Domain-specific documentation generators

**Structure per domain (e.g., GTM):**
```
builders/gtm/
├── builder.md          — Questionnaire logic (what to ask users)
├── rules.md            — Output rules (GTM-specific standards)
├── token_budget.md     — Token limit (4000 for GTM strategy)
└── examples/           — Sample GTM docs
```

**Flow:**
1. User answers questionnaire in `builder.md`
2. Builder generates doc using `DOC_CANONICAL_TEMPLATE.md`
3. Output runs through rules in `rules.md`
4. Token count checked against `token_budget.md`
5. Doc stored in `output/gtm/v1.0/`

### 3. Output (output/)

**Purpose:** Store generated documentation with versioning

**Structure per domain:**
```
output/gtm/
├── v1.0/               — Initial release
│   ├── GTM_Strategy_2026.md
│   ├── GTM_Strategy_2026.DEBT.md
│   └── metadata.json
├── v1.1/               — Patch update
├── v2.0/               — Major revision
└── archive/            — Deprecated versions ([DEPRECATED] prefix)
```

**Versioning:**
- v1.0 = initial
- v1.1 = patch (typo, clarification)
- v2.0 = major (new approach)
- Deprecated versions moved to archive/

### 4. Skills (skills/)

**Purpose:** Track reusable workflows

**Folders:**
- `published/` — Production skills (auto-added to projects)
- `suggested/` — Skills under review (from doc generation patterns)
- `archived/` — Deprecated skills

### 5. Config (config/)

**Purpose:** System-wide rules and budgets

**Contents:**
- `token_budgets.json` — Token limits per doc type (2500 for setup, 4000 for GTM, etc.)
- `domain_definitions.json` — What each domain covers (GTM, Design, Branding, etc.)
- Additional config as system grows

### 6. Metrics (metrics/)

**Purpose:** Track all generated docs

**Contents:**
- `generation_log.md` — Append-only log of every doc created
- Monthly summaries (count, avg quality, avg tokens, etc.)

### 7. Backlog (backlog/)

**Purpose:** System-wide technical debt

**Contents:**
- `SYSTEM_DEBT.md` — Framework improvements (P0-P3 items)

### 8. Projects (projects/)

**Purpose:** Claude Projects configurations

**Folders per domain:**
```
projects/docgen_base/              — Base system
projects/gtm_docs/                 — GTM builder
projects/design_docs/              — Design builder
etc.
```

Each contains:
- `instructions.md` — Custom instructions for Claude
- `knowledge_base/` — Reference documents

---

## Production Flow

```
User → Ask for GTM doc
  ↓
Builder/Questionnaire
  (what needs to be in GTM doc?)
  ↓
Output Generated
  (using DOC_CANONICAL_TEMPLATE.md)
  ↓
Exit Gate 1: Validation
  ✓ Metadata valid?
  ↓
Exit Gate 2: Structure
  ✓ All sections present?
  ↓
Exit Gate 3: Content Quality
  ✓ Clear & accurate?
  ↓
Exit Gate 4: Quality Check
  ✓ Human pass + AI pass + Token pass?
  ↓
Create DEBT.md
  (known limitations, backlog)
  ↓
Name File
  (GTM_Strategy_2026.md per SYSTEM_File_Naming.md)
  ↓
Exit Gate 5: Shipping
  ✓ All gates pass + DEBT exists + metadata complete?
  ↓
Store in output/gtm/v1.0/
  └─ GTM_Strategy_2026.md
  └─ GTM_Strategy_2026.DEBT.md
  └─ metadata.json
  ↓
Add to Claude Projects
  (docgen_base + gtm_docs)
  ↓
✅ PRODUCTION
```

---

## Quality Gates

### Gate 1: Validation (Input Check)
- **What:** Does metadata exist and is it valid?
- **Fail:** Fix frontmatter, re-run
- **Owner:** Automated

### Gate 2: Structure (Template Compliance)
- **What:** Does doc follow DOC_CANONICAL_TEMPLATE.md?
- **Fail:** Add missing sections
- **Owner:** Automated or manual

### Gate 3: Content Quality (Clarity/Accuracy)
- **What:** Is it clear, accurate, complete?
- **Fail:** Rewrite for clarity
- **Owner:** Manual (human review)

### Gate 4: Quality (Human + AI + Token)
- **What:** Human checklist + AI checklist + token budget OK?
- **Fail:** Optimize or cut content
- **Owner:** Automated + manual

### Gate 5: Shipping (Final Approval)
- **What:** All 4 gates + DEBT.md + metadata complete?
- **Fail:** Return to earlier gate
- **Owner:** Manual (project owner)

---

## Templates

### DOC_CANONICAL_TEMPLATE.md

Every doc must follow this structure:

```
1. YAML Frontmatter (8 required fields)
2. Title + Overview (exactly 2 sentences)
3. Prerequisites (Level 1-4 if applicable)
4. Content (type-appropriate)
5. Expected Output (table with commands)
6. Troubleshooting (errors with signatures)
7. Why This Matters (optional)
8. What's Next (related docs)
```

Plus:
- AI metadata blocks (preconditions/postconditions)
- metadata.json (quality score, tokens, gates)
- DEBT.md (known limitations, backlog)

### DEBT Template

Every doc includes DEBT.md listing:
- P0 items (critical, none if shipped)
- P1 items (high priority)
- P2 items (medium priority)
- P3 items (low priority)

Plus:
- Known limitations
- Content decisions (why things cut)
- Dependencies
- Verification needs
- Skills to create

---

## Token Optimization

**Budgets per type:**
- Setup guide: 2500 tokens
- GTM strategy: 4000 tokens
- API guide: 3000 tokens
- (See config/token_budgets.json)

**Quality per token:** 0.03+ (quality score ÷ token count)

**Optimization rules:**
- No fluff or theory
- Examples concise but complete
- Prose ≤ 4 paragraphs per section
- Only top 3-5 errors (rest in DEBT.md)
- Every section must serve purpose

---

## File Naming

Pattern: `{CATEGORY}_{TOPIC}_{VERSION}_{DATE}.md`

Examples:
- `GTM_Strategy_2026.md` (evergreen)
- `GTM_Competitive_Analysis_v1.0.md` (versioned)
- `[DEPRECATED]_Old_Strategy_v1.0.md` (archived)

---

## Version Control

**v1.0** = Initial release (in v1.0/ folder)
**v1.1** = Patch (same folder, new version file)
**v2.0** = Major revision (new v2.0/ folder, v1.x moved to archive/)

**Deprecation:**
1. Create v2.0 (new folder)
2. Mark v1.x deprecated (status field)
3. Move v1.x to archive/ with [DEPRECATED] prefix
4. Set EOL date (6-12 months)

---

## Claude Projects Integration

Each Claude Project has:

1. **Custom Instructions** (from PROJECT_INSTRUCTIONS_Docgen_Production.md)
   - Role definition
   - How to use uploaded framework
   - Response format
   - Do's and Don'ts

2. **Knowledge Base** (from system/)
   - All guides (SYSTEM_*.md)
   - All templates (DOC_CANONICAL_TEMPLATE.md, TEMPLATE_DEBT.md, etc.)
   - Examples

3. **Domain-Specific Projects**
   - docgen_base — Core system
   - gtm_docs — GTM builder
   - design_docs — Design builder
   - etc.

---

## Automation Opportunities (see backlog/)

**P1 (High Priority):**
- Builder automation framework (questionnaire → output → gates)
- Skill suggestion engine (detect patterns → suggest skills)
- Token validation script (check budgets automatically)
- Monthly metrics dashboard (quality trends)

**P2 (Medium Priority):**
- Domain-specific checklists
- Deprecation automation
- Cross-doc link validation
- Skill auto-integration

---

## Extensibility

### Adding a New Domain

1. Create `builders/{new_domain}/`
2. Create `builder.md`, `rules.md`, `token_budget.md`
3. Add to `config/domain_definitions.json`
4. Create `output/{new_domain}/{v1.0,v1.1,v2.0,archive}/`
5. Create `projects/{new_domain}_docs/`

### Adding a New Doc Type

1. Add to `DOC_CANONICAL_TEMPLATE.md` (section for type-specific examples)
2. Update `config/token_budgets.json` (add budget)
3. Create type-specific checklist in `system/checklists/`
4. Document in appropriate guide

### Adding Automation

1. Create script in `automation/` (not yet created)
2. Reference from relevant gate or process
3. Document in `docs/`
4. Add to CONTRIBUTING.md

---

## Directory Tree

```
docgen/
├── README.md                   # Start here
├── CONTRIBUTING.md             # How to contribute
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore patterns
│
├── system/                     # Framework (read-only reference)
│   ├── guides/                 # 10 production standards
│   ├── templates/              # Output templates
│   ├── checklists/             # Quality verification
│   └── examples/               # Perfect example docs
│
├── builders/                   # Domain builders
│   ├── gtm/                    # Go-to-market
│   ├── design/                 # Design & UX
│   ├── branding/               # Branding & voice
│   ├── content/                # Content strategy
│   ├── icp/                    # Ideal customer profile
│   └── web_dev/                # Web development
│
├── output/                     # Generated docs (versioned)
│   ├── gtm/{v1.0,v1.1,v2.0,archive}
│   ├── design/
│   ├── branding/
│   ├── content/
│   ├── icp/
│   └── web_dev/
│
├── skills/                     # Reusable workflows
│   ├── published/              # Production skills
│   ├── suggested/              # Under review
│   └── archived/               # Deprecated
│
├── projects/                   # Claude Projects configs
│   ├── docgen_base/            # Core system
│   ├── gtm_docs/               # GTM builder
│   └── [other domains]
│
├── config/                     # System configuration
│   ├── token_budgets.json      # Token limits
│   └── domain_definitions.json # Domain specs
│
├── metrics/                    # Tracking & logs
│   └── generation_log.md       # All docs created
│
├── backlog/                    # Technical debt
│   └── SYSTEM_DEBT.md          # Framework improvements
│
└── docs/                       # System documentation
    └── ARCHITECTURE.md         # This file
```

---

That's the system. Scalable, production-grade, extensible.
