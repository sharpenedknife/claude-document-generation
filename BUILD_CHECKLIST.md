# Docgen: Complete Build Checklist

**Total Build Time:** 7 hours (was 12 with accelerators: web-artifacts-builder, prompt-engineer, skill-creator, ai-evals)  
**Start Date:** [Today]  
**Target:** Working system with all 10 projects  
**Accelerators Used:** web-artifacts-builder (UI), prompt-engineer (prompts), skill-creator (meta-generators), ai-evals (quality gates)

---

## Phase 1: Chat Interface + UI (1.5 hours) — USING web-artifacts-builder

### Task 1.1: Create Interactive Chat UI Widget
**Time:** 1.5 hours (was 2h, saved 0.5h with web-artifacts-builder)  
**Output:** Interactive React/HTML widget  
**Tools:** web-artifacts-builder skill

**What to build:**
```
Interactive Menu Widget:
├── Welcome section (emoji + description)
├── 10 Project buttons (clickable, styled)
├── Dynamic questionnaire panel
│   ├── Questions show based on project selected
│   ├── Form inputs (text, checkbox, select)
│   └── Progress indicator (Q1 of 7)
├── Workflow selection (if applicable)
│   ├── Checkboxes for 0-2 workflows
│   └── Sub-items expand on click
├── Permission gates (modal)
│   ├── "Research API calls?" Yes/No/Partial
│   └── Cost + time warning
├── Output destination selection
│   ├── Multi-select (Zip, GitHub, Notion, Drive, Email)
│   └── OAuth buttons (GitHub, Notion, Drive)
└── Results preview
    ├── Doc list with quality scores
    ├── Delivery status
    └── Download/Share buttons
```

**Checklist:**
- [ ] Menu with 10 projects (buttons, not text)
- [ ] Click project → shows relevant questions
- [ ] Questions populate based on project type
- [ ] Workflow sub-menu (expandable)
- [ ] Permission gates work (show/hide based on selection)
- [ ] Output destination checkboxes + OAuth triggers
- [ ] Form submission → sends data to CLI
- [ ] Error display (red alerts, recovery buttons)
- [ ] Mobile responsive

**Acceptance:** Interactive widget, all 10 project paths clickable, data flows to backend

---

### Task 1.2: Connect UI to CLI (Wire Backend)
**Time:** 0.25 hours  
**Output:** Chat ↔ CLI communication

**What to do:**
- [ ] UI form submit → sends JSON to CLI command
- [ ] CLI runs: `docgen generate --config config.json`
- [ ] CLI returns results.json
- [ ] UI displays results in widget
- [ ] Error handling: show error message in UI

**Example flow:**
```javascript
// User clicks "Generate"
const config = {
  project: "fast-product-mvp",
  answers: {
    product_description: "...",
    target_user: "...",
    ...
  },
  destinations: ["zip", "github", "notion"],
  github_repo: "user/repo"
};

// Send to CLI
await fetch("/api/docgen/generate", {
  method: "POST",
  body: JSON.stringify(config)
});

// Get results
const results = await response.json();
// Display in UI: "✓ 3 docs generated, Quality: 87/100"
```

**Acceptance:** Full round-trip works (UI → CLI → Results → Display)

---

## Phase 2: CLI Backend - Generators (3 hours total) — USING prompt-engineer + skill-creator ✅ COMPLETE

### Task 2.1: Generate Prompts with prompt-engineer (30 mins) ✅
**Time:** 0.5 hours (was 2h+ for manual prompt writing)  
**Output:** Optimized prompts for each generator  
**Tools:** prompt-engineer skill

**Instead of writing each prompt by hand:**

Use `prompt-engineer` to generate + optimize prompts:
```python
from building_with_llms import optimize_prompt

PRD_PROMPT = optimize_prompt(
  goal="Generate a Product Requirements Document",
  context="Using DOC_CANONICAL_TEMPLATE.md",
  examples=[
    {"input": "SaaS for teams", "output": "PRD with sections: overview, problem, solution..."}
  ],
  constraints=[
    "Must have all 8 YAML fields",
    "No token budget exceeded",
    "Examples included"
  ],
  desired_format=DOC_CANONICAL_TEMPLATE
)
```

**Generate for each project:**
- [ ] PRD prompt (optimized)
- [ ] UX Requirements prompt
- [ ] Technical Specs prompt
- [ ] Monetization prompt
- [ ] Marketing prompts (messaging, positioning, branding, ICPs)
- [ ] Development Plan prompt
- [ ] Custom prompt template

**Output:** `code/prompts/` with 8 optimized prompt files

**Acceptance:** Each prompt generates valid docs on first try

---

### Task 2.2: Project Generators 1-8 (1.5 hours)
**Time:** 1.5 hours (was 2h)  
**Output:** `code/generators/`

Each generator now uses optimized prompt:

```python
# prd_generator.py
from prompts import PRD_PROMPT
from docx_handler import populate_template

def generate_prd(answers: dict) -> str:
    response = claude_api.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=3000,
        system=PRD_PROMPT,
        messages=[{"role": "user", "content": format_answers(answers)}]
    )
    
    # Populate template
    doc = populate_template(
        template=DOC_CANONICAL_TEMPLATE,
        content=response.content[0].text,
        metadata={"title": "PRD", "version": "1.0"}
    )
    return doc
```

**Build these generators:**
- [x] prd_generator.py (uses optimized prompt) ✓
- [x] ux_generator.py ✓
- [x] specifiers_generator.py ✓
- [x] monetization_generator.py ✓
- [x] marketing_generator.py ✓
- [x] branding_generator.py ✓
- [x] dev_plan_generator.py ✓
- [x] custom_generator.py ✓

**Acceptance:** Each generator produces valid markdown with YAML frontmatter ✅

---

### Task 2.3: Meta Generators 9-10 (1 hour) — USING skill-creator
**Time:** 1 hour (was 2h+ for manual writing)  
**Output:** `code/generators/skill_generator.py`, `project_generator.py`  
**Tools:** skill-creator skill

**Copy logic from skill-creator skill:**

```python
# skill_generator.py - reuse skill-creator logic
from skill_creator import SkillGenerator

class DocgenSkillGenerator:
    def __init__(self):
        self.base_generator = SkillGenerator()
    
    def generate(self, answers: dict):
        # Use skill-creator's structure
        skill = {
            "name": answers["skill_name"],
            "description": answers["what_it_does"],
            "triggers": self.base_generator.generate_triggers(
                answers["trigger_phrases"]
            ),
            "examples": self.base_generator.generate_examples(
                answers["usage_examples"]
            ),
            "implementation": self.base_generator.generate_impl_guide(
                answers["process_steps"]
            )
        }
        return skill

# project_generator.py
class DocgenProjectGenerator:
    def generate(self, answers: dict):
        project = {
            "instructions": self.generate_instructions(answers),
            "welcome": self.generate_welcome(answers),
            "examples": self.generate_examples(answers),
            "integrations": self.generate_integrations(answers["tools"]),
            "memory": self.generate_memory_system(answers)
        }
        return project
```

**Generate:**
- [ ] Skill definition + triggers + examples (via skill-creator logic)
- [ ] Project Instructions + welcome + examples (project-specific)
- [ ] Tool integration guides
- [ ] Memory system config

**Acceptance:** Skills and Projects generate correctly and are production-ready

---

## Phase 3: CLI Backend - Destinations (2 hours)

### Task 3.1: Destination Handlers
**Time:** 1.5 hours  
**Output:** `code/destinations/`

- [ ] `zip_handler.py`
  - [ ] Create folder structure
  - [ ] Copy all .md files
  - [ ] Copy .metadata.json
  - [ ] Create README.md (index)
  - [ ] Create SUMMARY.md (quality scores)
  - [ ] Zip everything
  - [ ] Return zip path for download

- [ ] `github_handler.py`
  - [ ] Accept repo URL + branch name
  - [ ] Create /docs folder
  - [ ] Push files
  - [ ] Optionally create PR
  - [ ] Return commit hash + branch link

- [ ] `notion_handler.py`
  - [ ] Accept API key or OAuth
  - [ ] Create workspace/database
  - [ ] Upload each file as page
  - [ ] Set properties (status, quality, date)
  - [ ] Return workspace link

- [ ] `google_drive_handler.py`
  - [ ] Accept OAuth token
  - [ ] Create folder
  - [ ] Upload files
  - [ ] Set sharing permissions
  - [ ] Return folder link

- [ ] `email_handler.py`
  - [ ] Accept email address
  - [ ] Create summary email
  - [ ] Attach zip file
  - [ ] Include links (GitHub, Notion, Drive)
  - [ ] Send via SMTP

**Acceptance:** Each destination creates files in correct format

---

### Task 3.2: Destination Integration
**Time:** 0.5 hours

- [ ] Multiple destinations work simultaneously
- [ ] One delivery can send to 3+ destinations
- [ ] All destination APIs handle errors gracefully
- [ ] User sees progress for each destination
- [ ] Final summary shows all delivery locations

**Acceptance:** Generate doc, pick 3 destinations, all 3 receive files

---

## Phase 4: Quality Gates (0.5 hours) — USING ai-evals

### Task 4.1: Implement Gates with ai-evals
**Time:** 0.5 hours (was 1h)  
**Output:** `code/gates/validator.py`  
**Tools:** ai-evals skill

**Use ai-evals instead of writing gates manually:**

```python
from ai_evals import Evaluator

class DocgenValidator:
    def __init__(self):
        self.evaluator = Evaluator()
    
    def run_all_gates(self, document: str, doc_type: str):
        """Run 5 gates using ai-evals"""
        
        # Gate 1: Validation
        gate_1 = self.evaluator.validate_structure(
            document,
            required_fields=["title", "description", "version", "date", "author", "category", "status", "tags"],
            format="yaml_frontmatter"
        )
        
        # Gate 2: Structure
        gate_2 = self.evaluator.check_sections(
            document,
            required_sections=self.get_required_sections(doc_type)
        )
        
        # Gate 3: Content Quality
        gate_3 = self.evaluator.analyze_content(
            document,
            criteria=[
                "no_vague_language",
                "includes_examples",
                "clear_instructions",
                "proper_formatting"
            ]
        )
        
        # Gate 4: Quality Metrics
        gate_4 = self.evaluator.score_quality(
            document,
            min_score=80,
            check_token_budget=True,
            budget_limit=self.get_token_budget(doc_type)
        )
        
        # Gate 5: Shipping Ready
        gate_5 = all([gate_1, gate_2, gate_3, gate_4])
        
        return {
            "gate_1_validation": gate_1,
            "gate_2_structure": gate_2,
            "gate_3_content": gate_3,
            "gate_4_metrics": gate_4,
            "gate_5_shipping": gate_5,
            "status": "PRODUCTION_READY" if gate_5 else "NEEDS_REVIEW",
            "quality_score": gate_4.get("score", 0)
        }
```

**Checklist:**
- [ ] Gate 1 (Validation): YAML valid, required fields ✓
- [ ] Gate 2 (Structure): All sections present ✓
- [ ] Gate 3 (Content): No vague language, examples present ✓
- [ ] Gate 4 (Metrics): Token budget OK, quality ≥ 80/100 ✓
- [ ] Gate 5 (Shipping): All 4 gates pass ✓
- [ ] Report: Which gate failed (if any) ✓

**Acceptance:** Run on 5 different docs, gates work correctly

---

## Phase 5: Integration (1 hour)

### Task 5.1: Chat → CLI Communication
**Time:** 0.5 hours

- [ ] Chat captures all questionnaire answers
- [ ] Chat sends answers to CLI command
- [ ] CLI runs generators
- [ ] CLI runs quality gates
- [ ] CLI handles each destination
- [ ] Results returned to chat

**Example flow:**
```
User in chat: "1" (Fast Product MVP)
Chat: [Collects 5-7 answers via questions]
Chat: Calls CLI: 
  docgen generate \
    --project fast-product-mvp \
    --answers answers.json \
    --destinations zip,github,notion
CLI: Generates docs
CLI: Runs 5 gates
CLI: Delivers to destinations
CLI: Returns: {status, docs, quality_scores, links}
Chat: Shows summary to user
```

**Acceptance:** End-to-end flow works

---

### Task 5.2: Error Handling & Recovery
**Time:** 0.5 hours

- [ ] Generator fails → Show error, ask to retry
- [ ] Gate fails → Show which gate, which doc, what's missing
- [ ] Destination fails → Try next, mark as failed, allow manual retry
- [ ] Network error → Graceful retry with backoff
- [ ] User cancels → Cleanup temp files

**Acceptance:** System handles 5 different error scenarios gracefully

---

## Phase 6: Testing & Validation (1 hour)

### Task 6.1: End-to-End Tests

Test complete workflows:
- [ ] **Workflow A:** Project 1 → PRD + UX + specifiers → Zip
  - [ ] All 3 docs generated
  - [ ] All 5 gates pass
  - [ ] Quality scores ≥ 85
  - [ ] Zip file created
  - [ ] Files extractable

- [ ] **Workflow B:** Project 9 → Skill package → Zip
  - [ ] 5 skill files generated
  - [ ] Trigger patterns valid
  - [ ] All gates pass
  - [ ] Reusable in other contexts

- [ ] **Workflow C:** Project 1 → Project 10 → PRD embedded → Zip
  - [ ] Project 1 docs created
  - [ ] Project Instructions references those docs
  - [ ] Project is deployable
  - [ ] All gates pass

- [ ] **Workflow D:** Project 1 + Marketing workflow → 7 docs → GitHub + Notion
  - [ ] 7 docs generated
  - [ ] GitHub: Files in /docs folder
  - [ ] Notion: Database created with properties
  - [ ] All gates pass

**Acceptance:** All 4 workflows complete successfully

---

### Task 6.2: Quality Validation

For each generated doc type, verify:
- [ ] YAML frontmatter valid
- [ ] All sections present
- [ ] Examples included
- [ ] No vague language
- [ ] Token count within budget
- [ ] Gate 5 = PRODUCTION_READY
- [ ] metadata.json valid

**Acceptance:** Sample docs from all 10 projects pass quality check

---

## Verification Checklist

Run this before marking "complete":

### Chat Interface
- [ ] Welcome message displays
- [ ] All 10 options visible
- [ ] Option 1 questionnaire works
- [ ] Option 9 questionnaire works
- [ ] Option 10 questionnaire works
- [ ] Workflow addition works
- [ ] Output selection works
- [ ] Error recovery works

### Generation
- [ ] Project 1: PRD, UX, specifiers generated ✓
- [ ] Project 2: PRD, UX, specifiers, safety ✓
- [ ] Project 3: Process, dev plan, safety ✓
- [ ] Project 4: Monetization, pricing ✓
- [ ] Project 5: Brand, messaging, positioning, voice ✓
- [ ] Project 6: All of 5 + ICPs + competitive + GTM ✓
- [ ] Project 7: Summary + extracted specs + gaps ✓
- [ ] Project 8: Custom doc from description ✓
- [ ] Project 9: Skill + triggers + implementation + examples + related ✓
- [ ] Project 10: Project Instructions + welcome + examples + integrations + memory ✓

### Quality Gates
- [ ] Gate 1 (Validation): All docs pass ✓
- [ ] Gate 2 (Structure): All sections present ✓
- [ ] Gate 3 (Content): No vague language ✓
- [ ] Gate 4 (Metrics): Quality ≥ 80/100 ✓
- [ ] Gate 5 (Shipping): PRODUCTION_READY status ✓

### Destinations
- [ ] Zip: Files in correct structure ✓
- [ ] GitHub: Files pushed, PR created ✓
- [ ] Notion: Workspace created, pages uploaded ✓
- [ ] Google Drive: Folder created, files uploaded ✓
- [ ] Email: Summary sent with links ✓

### Integration
- [ ] Project 1 → Zip works
- [ ] Project 1 + Project 9 → Zip + GitHub works
- [ ] Project 1 → Project 10 (with embedded docs) → Zip works
- [ ] Project 1 + Coding workflow → 5+ docs → Multiple destinations works

### Success Message
When all checks pass:
```
✅ DOCGEN SYSTEM COMPLETE

Generated: 10 project types
Quality gates: All pass
Destinations: 5 working
Integration: End-to-end verified

Ready for production.
```

---

## Files to Commit to GitHub

After build complete:
```
docgen/
├── system/                          (Phase 1 framework - unchanged)
│   ├── guides/
│   ├── templates/
│   └── checklists/
│
├── code/                            (Phase 2 implementation - new)
│   ├── cli/main.py
│   ├── generators/
│   │   ├── prd_generator.py
│   │   ├── ux_generator.py
│   │   ├── [8 more generators]
│   │   └── workflows/
│   ├── destinations/
│   │   ├── zip_handler.py
│   │   ├── github_handler.py
│   │   ├── [3 more handlers]
│   └── gates/validator.py
│
├── PROJECT_INSTRUCTIONS_Docgen_Chat.md
├── README.md (update with build status)
├── CONTRIBUTING.md (how to add new projects)
├── .gitignore (exclude /output, /temp, .env)
└── requirements.txt (Python dependencies)
```

---

## Dependency Installation

Before building, install:
```bash
pip install click requests beautifulsoup4 pdfplumber \
  python-pptx openpyxl python-docx google-api-python-client \
  PyGithub notion-client google-auth-oauthlib python-dotenv
```

---

## Build Command (Once Complete)

```bash
# Start Docgen chat
# User enters Claude Projects
# Pastes PROJECT_INSTRUCTIONS_Docgen_Chat.md as instructions
# System ready

# Or run CLI directly:
python code/cli/main.py generate \
  --project fast-product-mvp \
  --answers answers.json \
  --destinations zip,github,notion
```

---

## Success = System Shipped

When all checks ✅ and all workflows complete:

**Docgen is production-ready.**

Next: Deploy to Claude Projects, announce, gather feedback.

---

**12 hours to complete this checklist. Then: infinite documentation possibilities.**
