# Production Folder Structure for Docgen System

## Root Directory Organization

```
docgen/
├── README.md                          # Entry point, quick start
├── VERSION.md                         # Current system version & changelog
│
├── system/                            # Core docgen framework (read-only reference)
│   ├── guides/
│   │   ├── 00_START_HERE_Master_Index.md
│   │   ├── Documentation_Content_Guide.md
│   │   ├── Prerequisites_Guide.md
│   │   ├── AI_First_Documentation_Format.md
│   │   ├── Project_Chat_Instructions_Rules.md
│   │   ├── Token_Optimization_Guide.md
│   │   ├── Exit_Rules_and_Gates.md
│   │   └── File_Naming_Convention.md
│   │
│   ├── templates/
│   │   ├── output/
│   │   │   ├── DOC_CANONICAL_TEMPLATE.md          # Master template for all output docs
│   │   │   ├── DEBT_TEMPLATE.md                   # Backlog/debt template
│   │   │   └── SKILL_TEMPLATE.md                  # Skill suggestion template
│   │   │
│   │   ├── builders/
│   │   │   ├── gtm_builder_template.md
│   │   │   ├── design_builder_template.md
│   │   │   ├── branding_builder_template.md
│   │   │   ├── content_builder_template.md
│   │   │   ├── icp_builder_template.md
│   │   │   └── web_dev_builder_template.md
│   │   │
│   │   └── project_instructions/
│   │       ├── docgen_base_instructions.md
│   │       ├── docgen_ai_first_instructions.md
│   │       └── builder_mode_instructions.md
│   │
│   ├── checklists/
│   │   ├── quality_checklist.md           # Human quality gates
│   │   ├── ai_quality_checklist.md        # AI parsing quality gates
│   │   ├── token_efficiency_checklist.md  # Token optimization gates
│   │   ├── exit_gate_checklist_level_1.md # Gate 1: Validation
│   │   ├── exit_gate_checklist_level_2.md # Gate 2: Structure
│   │   ├── exit_gate_checklist_level_3.md # Gate 3: Content
│   │   ├── exit_gate_checklist_level_4.md # Gate 4: Quality
│   │   └── exit_gate_checklist_level_5.md # Gate 5: Shipping
│   │
│   └── examples/
│       ├── good_setup_guide.md
│       ├── good_api_guide.md
│       ├── good_gtm_doc.md
│       ├── good_debt.md
│       └── good_skill.md
│
├── builders/                          # Active builder implementations
│   ├── gtm/
│   │   ├── builder.md                 # GTM builder questionnaire + logic
│   │   ├── rules.md                   # GTM-specific output rules
│   │   ├── token_budget.md            # GTM doc token limits
│   │   └── examples/                  # Sample GTM docs produced
│   │       ├── gtm_sample_1.md
│   │       └── gtm_sample_2.md
│   │
│   ├── design/
│   │   ├── builder.md
│   │   ├── rules.md
│   │   ├── token_budget.md
│   │   └── examples/
│   │
│   ├── branding/
│   │   ├── builder.md
│   │   ├── rules.md
│   │   ├── token_budget.md
│   │   └── examples/
│   │
│   ├── content/
│   │   ├── builder.md
│   │   ├── rules.md
│   │   ├── token_budget.md
│   │   └── examples/
│   │
│   ├── icp/
│   │   ├── builder.md
│   │   ├── rules.md
│   │   ├── token_budget.md
│   │   └── examples/
│   │
│   └── web_dev/
│       ├── builder.md
│       ├── rules.md
│       ├── token_budget.md
│       └── examples/
│
├── output/                           # Generated documentation (versioned)
│   ├── gtm/
│   │   ├── v1.0/
│   │   │   ├── GTM_Strategy_2026Q1.md
│   │   │   ├── GTM_Strategy_2026Q1.DEBT.md
│   │   │   └── metadata.json          # Generation metadata
│   │   ├── v1.1/
│   │   └── archive/                  # Deprecated versions
│   │
│   ├── design/
│   │   ├── v1.0/
│   │   ├── v1.1/
│   │   └── archive/
│   │
│   ├── branding/
│   ├── content/
│   ├── icp/
│   └── web_dev/
│
├── skills/                          # Generated or suggested skills
│   ├── published/                   # Production skills
│   │   ├── gtm_market_analysis.md
│   │   ├── brand_voice_enforcement.md
│   │   └── web_performance_audit.md
│   │
│   ├── suggested/                   # Skill suggestions from doc generation
│   │   ├── gtm_competitive_research.md (status: review)
│   │   ├── content_gap_analysis.md (status: review)
│   │   └── icp_validation.md (status: review)
│   │
│   └── archived/                    # Deprecated skills
│       └── old_gtm_v1.md
│
├── projects/                        # Claude Projects for different use cases
│   ├── docgen_base/
│   │   ├── instructions.md           # Custom instructions
│   │   ├── knowledge_base/
│   │   │   └── [system guides]
│   │   └── metadata.json
│   │
│   ├── gtm_docs/
│   │   ├── instructions.md
│   │   ├── knowledge_base/
│   │   │   ├── [GTM builder rules]
│   │   │   └── [GTM examples]
│   │   └── metadata.json
│   │
│   └── [similar for other domains]
│
├── config/                          # Configuration & rules
│   ├── naming_convention.md          # File naming rules
│   ├── version_strategy.md           # Versioning & deprecation
│   ├── exit_rules.md                 # All 5 gate definitions
│   ├── token_budgets.json            # Token limits by doc type
│   ├── domain_definitions.json       # What each domain covers
│   └── integration_rules.md          # How builders integrate with system
│
├── metrics/                         # Quality & performance tracking
│   ├── quality_metrics.md           # How to measure doc quality
│   ├── token_efficiency.md          # Token usage analysis
│   ├── generation_log.md            # All docs ever generated (append-only)
│   └── skill_usage_log.md           # Skill invocation tracking
│
├── backlog/                         # System-wide backlog
│   ├── SYSTEM_DEBT.md               # Docgen framework improvements
│   ├── BUILDER_DEBT.md              # Builder improvements needed
│   └── DOMAIN_DEBT.md               # Domain-specific improvements
│
└── docs/                            # Documentation about the system itself
    ├── ARCHITECTURE.md              # How it all fits together
    ├── BUILDER_DEVELOPMENT.md       # How to create new builders
    ├── INTEGRATION_GUIDE.md         # How to integrate with Claude Projects
    └── TROUBLESHOOTING.md           # Common issues & solutions
```

---

## File Organization Rules

### 1. System/ Directory (Read-Only Reference)
- Contains master docgen framework
- Never modified except by system updates
- All builders reference these guides
- Version tracked in VERSION.md

### 2. Builders/ Directory (Active Implementations)
- One folder per domain (gtm, design, branding, content, icp, web_dev)
- Each contains:
  - `builder.md`: Questionnaire + logic
  - `rules.md`: Domain-specific output rules
  - `token_budget.md`: Token limits for this domain
  - `examples/`: Sample outputs
- Add new builder: Create new folder, follow pattern

### 3. Output/ Directory (Generated Docs)
- Organized by domain, then by version
- Each doc has:
  - Main file: `{DOC_NAME}.md`
  - Debt file: `{DOC_NAME}.DEBT.md`
  - Metadata: `metadata.json` (creation date, builder version, tokens used, quality score)
- Versions: Keep v1.0, v1.1, etc. separately
- Archive: Move outdated to `archive/` when deprecated

### 4. Skills/ Directory (Knowledge Artifacts)
- **published/**: Production-ready skills (auto-loaded into Projects)
- **suggested/**: Skills awaiting review (status field indicates review stage)
- **archived/**: Deprecated skills (keep for reference)
- Each skill: `{skill_name}.md` with status in frontmatter

### 5. Projects/ Directory (Claude Project Configs)
- One folder per active Claude Project
- Contains: custom instructions + knowledge base list
- `metadata.json`: Project purpose, active domains, version
- Synced with `system/templates/project_instructions/`

### 6. Config/ Directory (Rules & Standards)
- Naming conventions
- Versioning strategy
- Exit gate definitions
- Token budgets
- Domain definitions
- Integration rules

### 7. Metrics/ Directory (Quality Tracking)
- Append-only logs (never delete)
- Track every doc generated
- Track every skill invoked
- Analyze quality + token efficiency

### 8. Backlog/ Directory (Technical Debt)
- `SYSTEM_DEBT.md`: Docgen framework improvements
- `BUILDER_DEBT.md`: Builder feature requests
- `DOMAIN_DEBT.md`: Domain-specific gaps
- Each generated doc has own DEBT.md (stored with doc)

---

## Key Principles

**Immutability:**
- System/ never changes (versioned separately)
- Output/ docs versioned (never overwrite v1.0)
- Metrics/ append-only (never delete generation records)

**Traceability:**
- Every doc has metadata.json (when created, by what builder, token cost, quality score)
- Every skill has status field (published/suggested/archived)
- Every generation logged in metrics/

**Scalability:**
- Domain-based organization (add domains by adding builders/)
- Versioning allows parallel doc development (v1.0, v1.1, v2.0)
- Archive prevents old docs from confusing users

**Quality:**
- Exit gates prevent bad docs shipping
- Token budgets prevent bloat
- Metrics track quality over time

---

## Migration Path (Current → Production)

**Current state:** All files in /mnt/project/ root

**Step 1:** Create folders (system/, builders/, output/, etc.)

**Step 2:** Move existing framework files to system/guides/ and system/templates/

**Step 3:** Create first builder (GTM) in builders/gtm/

**Step 4:** Set up metrics/ logging and output/ versioning

**Step 5:** Establish exit gates + token budgets

**Step 6:** Publish as production-ready

---

## File Access Patterns

**For humans:**
```
README.md → system/guides/00_START_HERE → specific guide/builder
```

**For builders:**
```
builders/{domain}/builder.md → system/templates/DOC_CANONICAL_TEMPLATE.md → system/guides/[relevant]
```

**For Claude Projects:**
```
projects/{project}/instructions.md → system/templates/project_instructions/ → builders/{domain}/
```

**For quality checks:**
```
config/exit_rules.md → checklists/exit_gate_checklist_level_{N}.md → metrics/quality_metrics.md
```

---

## Initialization Script (Pseudocode)

```bash
docgen/
├── init.sh                          # Creates this structure
└── update.sh                        # Syncs projects, validates structure
```

When new builder created:
1. `builders/{domain}/` folder initialized
2. `projects/{domain}/` project prepared
3. `output/{domain}/` ready for versions
4. `metrics/generation_log.md` updated

When doc generated:
1. `output/{domain}/v{X}.{Y}/{DOC_NAME}.md` created
2. `output/{domain}/v{X}.{Y}/{DOC_NAME}.DEBT.md` created
3. `output/{domain}/v{X}.{Y}/metadata.json` created
4. `metrics/generation_log.md` appended
5. If skill suggested: `skills/suggested/{skill}.md` created with `status: review`
