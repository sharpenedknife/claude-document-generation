# Documentation Generation System (docgen)

Production-grade documentation framework for creating, structuring, and validating high-quality docs at scale.

**Status:** ✅ Production Ready (v1.0)

---

## What It Is

docgen is a complete system for generating, validating, and managing technical documentation. It enforces production standards through 5-level quality gates, ensures token efficiency, and provides templates for consistent, high-quality output.

## Key Features

- **5-Level Quality Gates:** Validation → Structure → Content → Quality → Shipping
- **Token Optimization:** Budget-aware docs (2K-4K tokens depending on type)
- **Production Templates:** Canonical structure for all doc types
- **Automatic DEBT Tracking:** Known limitations, backlog, deprecations
- **Version Control:** v1.0, v1.1, v2.0 with deprecation process
- **Multi-Domain:** GTM, Design, Branding, Content, ICP, Web Development

## Quick Start

1. **Read the framework:** `system/guides/SYSTEM_Master_Index.md`
2. **Understand standards:** `system/guides/SYSTEM_Content_Guide.md`
3. **See an example:** `system/examples/EXAMPLE_Perfect_Setup_Guide.md`
4. **Run a doc through gates:** Use checklists in `system/checklists/`
5. **Output your doc:** `output/{domain}/v1.0/{DOC_NAME}.md`

## File Structure

```
docgen/
├── system/              # Framework (read-only reference)
│   ├── guides/         # 10 production standards
│   ├── templates/      # Output templates
│   ├── checklists/     # Quality verification checklists
│   └── examples/       # Perfect example docs
├── builders/           # 6 domain builders (ready to populate)
├── output/             # Generated docs (versioned by domain)
├── skills/             # Published + suggested reusable skills
├── projects/           # Claude Projects configurations
├── config/             # Rules, budgets, domain definitions
├── metrics/            # Generation logs and tracking
├── backlog/            # Technical debt (SYSTEM_DEBT.md)
└── docs/               # System documentation
```

## For Different Use Cases

### Building a Doc
1. Follow `SYSTEM_Content_Guide.md` for structure
2. Check `SYSTEM_Prerequisites_Guide.md` for prereqs
3. Use `DOC_CANONICAL_TEMPLATE.md` for format
4. Run through 5 exit gates using checklists
5. Name using `SYSTEM_File_Naming.md` pattern
6. Store in `output/{domain}/v1.0/`

### Creating a Builder (e.g., GTM)
1. Review `system/guides/SYSTEM_Ecosystem_Strategy.md` (Priority 1)
2. Create questionnaire in `builders/gtm/builder.md`
3. Define rules in `builders/gtm/rules.md`
4. Set token budget in `builders/gtm/token_budget.md`
5. Output docs using templates

### Setting Up Claude Projects
1. Copy custom instructions from `system/templates/project_instructions/PROJECT_INSTRUCTIONS_Docgen_Production.md`
2. Upload as knowledge base:
   - All files from `system/guides/`
   - All files from `system/templates/`
3. Create in Claude Projects
4. Users now have production-grade doc creation

### Understanding Quality
- Read: `SYSTEM_Exit_Rules.md` (5-level gates)
- Read: `SYSTEM_Token_Optimization.md` (budgets + efficiency)
- Check: `system/checklists/` (verification checklists)

## Production Standards

### 5 Exit Gates (No doc ships without passing all 5)

| Gate | Check | Fail = |
|------|-------|--------|
| 1 | Validation | Fix metadata, re-run |
| 2 | Structure | Add missing sections |
| 3 | Content Quality | Rewrite for clarity |
| 4 | Human+AI+Token | Optimize or cut content |
| 5 | Shipping | All gates + DEBT + metadata |

### Token Budgets

- Setup guide: 2500 tokens
- GTM strategy: 4000 tokens  
- API guide: 3000 tokens
- (See `config/token_budgets.json` for all types)

### Quality Target

- Minimum quality score: 85
- Quality per token: 0.03+ (quality score ÷ token count)

## Key Files to Know

**Start Here:**
- `system/guides/SYSTEM_Master_Index.md` — Navigation & quick reference
- `system/guides/SYSTEM_Content_Guide.md` — Doc section standards
- `system/guides/SYSTEM_Exit_Rules.md` — Quality gates

**Production Standards:**
- `system/guides/SYSTEM_File_Naming.md` — Naming conventions
- `system/guides/SYSTEM_Token_Optimization.md` — Token budgets
- `system/guides/SYSTEM_Version_Control.md` — Versioning & deprecation

**Templates:**
- `system/templates/output/DOC_CANONICAL_TEMPLATE.md` — Output format
- `system/templates/output/TEMPLATE_DEBT_Standard.md` — Backlog format
- `system/templates/project_instructions/PROJECT_INSTRUCTIONS_Docgen_Production.md` — Claude Projects setup

**Checklists:**
- `system/checklists/CHECKLIST_Human_Quality.md` — Gate 3 verification
- `system/checklists/CHECKLIST_AI_Quality.md` — Gate 4 AI portion
- `system/checklists/CHECKLIST_Token_Efficiency.md` — Gate 4 token portion

## Example Doc

See: `system/examples/EXAMPLE_Perfect_Setup_Guide.md`

This is a perfect example showing all standards correctly applied. Use it as a reference.

## Current Status

✅ **Production Ready v1.0**

- 10 production standards documented
- 3 output templates created
- 5-level quality gates defined
- Token budgets set per doc type
- Folder structure organized for scale
- Example doc included
- 6 domain builders ready to populate

**Not Yet Implemented (see `backlog/SYSTEM_DEBT.md`):**
- Builder automation framework (P1)
- Skill suggestion engine (P1)
- Token validation script (P1)
- Monthly metrics dashboard (P1)
- Domain-specific checklists (P2)

## Getting Started

```bash
# Clone this repo
git clone https://github.com/your-org/docgen.git
cd docgen

# Read the master index
cat system/guides/SYSTEM_Master_Index.md

# See an example
cat system/examples/EXAMPLE_Perfect_Setup_Guide.md

# Check your first doc against gates
# Use checklists in system/checklists/
```

## Contributing

See: `CONTRIBUTING.md`

## License

MIT License — See `LICENSE`

## Questions?

- **Which standards apply to my doc?** → See `system/guides/SYSTEM_Content_Guide.md`
- **How do I name files?** → See `system/guides/SYSTEM_File_Naming.md`
- **What's a quality gate?** → See `system/guides/SYSTEM_Exit_Rules.md`
- **How do I version docs?** → See `system/guides/SYSTEM_Version_Control.md`
- **What's the token budget?** → See `config/token_budgets.json`

---

**Built for:** Teams that want production-quality documentation without the chaos.

**Perfect for:** SaaS products, APIs, frameworks, tools, internal wikis.
