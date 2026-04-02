# Docgen Integration Guide: Widget → CLI → Delivery

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│  Interactive Widget (React/HTML)                        │
│  - 10 Project menu                                       │
│  - Dynamic questionnaire                                │
│  - Workflow selection                                   │
│  - Destination selection                                │
└──────────────────┬──────────────────────────────────────┘
                   │
                   │ sendPrompt("Generate...") / JSON POST
                   ↓
┌─────────────────────────────────────────────────────────┐
│  CLI Backend (Python)                                   │
│  - Parse user input                                     │
│  - Load answers JSON                                    │
│  - Call generators                                      │
└──────────────────┬──────────────────────────────────────┘
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
    ┌────────┐ ┌──────────┐ ┌────────┐
    │Prompt  │ │Generator │ │Validator
    │Files   │ │(10 types)│ │(5 gates)
    └────────┘ └──────────┘ └────────┘
        │          │          │
        └──────────┼──────────┘
                   ↓
    ┌──────────────────────────┐
    │  Generated Docs          │
    │  + Quality Metadata      │
    └──────────────┬───────────┘
                   │
        ┌──────────┼──────────────────┐
        ↓          ↓          ↓        ↓
    ┌──────┐  ┌──────┐  ┌────────┐ ┌────────┐
    │ Zip  │  │GitHub│  │ Notion │ │Drive   │
    │ File │  │Push  │  │Pages   │ │Upload  │
    └──────┘  └──────┘  └────────┘ └────────┘
        │          │          │        │
        └──────────┴──────────┴────────┘
                   │
                   ↓
        User downloads/accesses docs
```

## Widget → CLI Communication

### Option 1: sendPrompt() Trigger

User clicks "Generate Docs" in widget:

```javascript
// Widget (interactive_menu.html)
function generateDocs() {
  const config = {
    project: selectedProject,
    workflows: selectedWorkflows,
    destinations: selectedDestinations,
    answers: formData
  };
  
  // Send to Claude as chat message
  sendPrompt(`Generate my ${config.projectName} documentation with: 
    workflows [${config.workflows.join(', ')}], 
    send to ${config.destinations.join(', ')}`);
}
```

This triggers Claude to:
1. Parse the message
2. Extract project type, workflows, destinations
3. Run CLI command with answers

### Option 2: HTTP POST (For Standalone Server)

```javascript
// Send config as JSON
const response = await fetch('/api/docgen/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    project: 1,
    answers: {q0: "...", q1: "...", ...},
    destinations: ['zip', 'github']
  })
});

const result = await response.json();
// { status: 'SUCCESS', docs: [...], quality_score: 87 }
```

## CLI Command Flow

### 1. Receive Input

```python
# cli/main.py
parser.add_argument('--project', type=int)
parser.add_argument('--answers', type=str)  # JSON file path
parser.add_argument('--destinations', type=str)  # zip,github,notion

args = parser.parse_args()
answers = json.load(open(args.answers))
destinations = args.destinations.split(',')
```

### 2. Generate Document

```python
from generators.base_generator import get_generator

generator = get_generator(args.project)  # Get right generator
result = generator.generate(answers)     # Call Claude API
# result = {
#   'filename': 'PRD.md',
#   'content': '---\ntitle: ...\n---\n...',
#   'metadata': {...}
# }
```

### 3. Validate with Quality Gates

```python
from gates.validator import QualityGateValidator

validator = QualityGateValidator()
gates = validator.validate_all(
  document=result['content'],
  doc_type=result['metadata']['category']
)

# gates = {
#   'gate_1_validation': True,
#   'gate_2_structure': True,
#   'gate_3_content': True,
#   'gate_4': {...},
#   'status': 'PRODUCTION_READY'
# }
```

### 4. Deliver to Destinations

```python
from destinations.zip_handler import ZipHandler
from destinations.github_handler import GitHubHandler

docs_to_deliver = [result]  # Could be multiple

for destination in destinations:
  if destination == 'zip':
    handler = ZipHandler()
    link = handler.create_zip(docs_to_deliver)
  elif destination == 'github':
    handler = GitHubHandler()
    link = handler.push(docs_to_deliver)
  # etc...
```

### 5. Return Results

```python
return {
  'status': 'SUCCESS',
  'docs': [
    {
      'filename': 'PRD.md',
      'content': '...',
      'metadata': {...}
    }
  ],
  'delivery': {
    'zip': {'status': 'SUCCESS', 'link': '...'},
    'github': {'status': 'SUCCESS', 'link': '...'}
  },
  'quality_score': 87
}
```

## File Structure

```
docgen/
├── code/
│   ├── cli/
│   │   └── main.py                 # Entry point
│   ├── generators/
│   │   ├── base_generator.py       # Base class + 10 generators
│   │   └── workflows/              # Workflow generators (todo)
│   ├── gates/
│   │   └── validator.py            # 5-level quality gates
│   ├── destinations/
│   │   ├── zip_handler.py          # ✓ Complete
│   │   ├── github_handler.py       # Stub (needs OAuth)
│   │   ├── notion_handler.py       # Stub (needs API token)
│   │   └── drive_handler.py        # Stub (needs credentials)
│   ├── prompts/
│   │   ├── prd_prompt.txt          # ✓ 10 prompts
│   │   ├── ux_prompt.txt
│   │   ├── specifiers_prompt.txt
│   │   ├── dev_plan_prompt.txt
│   │   ├── monetization_prompt.txt
│   │   ├── marketing_prompt.txt
│   │   ├── custom_prompt.txt
│   │   ├── skill_prompt.txt
│   │   ├── project_prompt.txt
│   │   └── summary_prompt.txt
│   ├── test_e2e.py                 # ✓ End-to-end tests
│   └── requirements.txt             # ✓ Dependencies
│
└── widget/
    ├── interactive_menu.html        # ✓ React component
    └── bundle.html                  # (after bundling)
```

## Testing the System

### 1. Manual Test (No API)

```bash
cd code
python3 test_e2e.py
```

This runs:
1. Generate sample PRD
2. Run quality gates
3. Create zip file
4. Report results

### 2. Integration Test (With Claude API)

```bash
# Set API key
export ANTHROPIC_API_KEY="sk-..."

# Create sample answers
cat > answers.json << EOF
{
  "q0": "A SaaS platform for teams",
  "q1": "Engineering teams at startups",
  "q2": "Spend too much time on docs",
  "q3": "Quick doc generation"
}
EOF

# Run generator
python3 cli/main.py generate \
  --project 1 \
  --answers answers.json \
  --destinations zip,github
```

## Next Steps

### Phase 3: Complete Integration
1. Add OAuth/API auth for GitHub, Notion, Drive
2. Implement workflow generators (Projects 2, 5, 6)
3. Create HTTP server wrapper (FastAPI/Flask)
4. Add error handling and retry logic
5. Deploy as Claude Project

### Current Status
- ✅ Interactive widget (Day 1)
- ✅ Prompt optimization (Day 2)
- ✅ Base generator framework (Day 2)
- ✅ Quality gates (Day 2)
- ✅ Zip delivery (Day 2)
- ⏳ Full integration testing
- ⏳ OAuth implementations
- ⏳ Workflow generators

## Architecture Decisions

**Why separate prompts?**
- Each doc type has different structure/requirements
- Easier to optimize/test individual prompts
- Token budget can be fine-tuned per type

**Why base generator class?**
- DRY principle - shared logic
- Easy to add new generators (inherit + override get_title, etc.)
- Consistent API handling, error handling

**Why 5 quality gates?**
- Catch structural issues early (Gate 1-2)
- Validate content quality (Gate 3)
- Ensure token budgets respected (Gate 4)
- Prevent shipping broken docs (Gate 5)

**Why multiple destinations?**
- Different workflows need different delivery
- Zip for offline, GitHub for CI/CD, Notion for team knowledge base
- Users choose what works for them
