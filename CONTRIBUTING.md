# Contributing to docgen

## How to Contribute

### Reporting Issues

Found a bug or improvement idea? Open an issue describing:
- What happened
- What you expected
- Steps to reproduce (if applicable)

### Improving Documentation

1. Fork the repo
2. Create a branch: `git checkout -b improve/your-feature`
3. Make your changes following production standards
4. Run docs through all 5 exit gates (use checklists)
5. Submit a pull request

### Adding a New Builder

Want to add a new domain builder (e.g., mobile development)?

1. Create folder: `builders/your_domain/`
2. Create `builder.md` (questionnaire logic)
3. Create `rules.md` (output standards for domain)
4. Create `token_budget.md` (token limits)
5. Add to `config/domain_definitions.json`
6. Submit PR

### Standards You Must Follow

- Every doc must pass all 5 exit gates
- Use naming convention: `{CATEGORY}_{TOPIC}_{VERSION}_{DATE}.md`
- Include DEBT.md file with known limitations
- Include metadata.json with generation details
- Follow `DOC_CANONICAL_TEMPLATE.md` structure

### Quality Checklist for Contributions

- [ ] Doc passes Gate 1 (validation)
- [ ] Doc passes Gate 2 (structure)
- [ ] Doc passes Gate 3 (content quality)
- [ ] Doc passes Gate 4 (human+AI+token)
- [ ] Doc passes Gate 5 (shipping)
- [ ] DEBT.md file created
- [ ] metadata.json generated
- [ ] File named correctly
- [ ] Related docs updated
- [ ] No duplicates in codebase

## Questions?

Refer to the appropriate guide in `system/guides/`:
- Structure questions → `SYSTEM_Content_Guide.md`
- Quality questions → `SYSTEM_Exit_Rules.md`
- Naming questions → `SYSTEM_File_Naming.md`
