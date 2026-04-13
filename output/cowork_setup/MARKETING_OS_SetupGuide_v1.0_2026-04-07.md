# Marketing OS — Setup Guide
**Version:** 1.0 | **Date:** 2026-04-07 | **Purpose:** How to activate and use the Marketing OS in Claude.ai and Cowork

---

## Quick Start (5 Minutes)

### Step 1: Load This Project in Claude.ai
1. Go to **Claude.ai → Projects**
2. Create new project: "Marketing OS"
3. Add these docs to project context:
   - MARKETING_OS_CLAUDE_v1.0.md (Custom instructions)
   - MARKETING_OS_SkillOrchestration_Matrix_v1.0.md (Skill routing)
   - MARKETING_OS_KnowledgeStructure_v1.0.md (Templates)

### Step 2: Create Your First Project Context
1. Make a new file: `[ProjectName]_marketing.md`
2. Use the template: **MARKETING_OS_ProjectContext_Template_v1.0.md**
3. Fill in: ICP, messaging, positioning, channels
4. Upload to project

### Step 3: Run Your First Campaign
1. Say: "I want to run a cold email campaign for [Project Name]"
2. System will load your context
3. Route to **cold-email** skill
4. Deliver email sequence
5. Evaluate (score it 1–10)
6. Ship or revise

---

## Installation (15 Minutes)

### Option A: Claude.ai Projects (Recommended)

**Step 1: Create Claude Project**
```
Claude.ai → Projects → New Project → "Marketing OS"
```

**Step 2: Add Core Docs (Project Instructions)**
Upload these 3 files to project context:
```
✅ MARKETING_OS_CLAUDE_v1.0.md
✅ MARKETING_OS_SkillOrchestration_Matrix_v1.0.md
✅ MARKETING_OS_KnowledgeStructure_v1.0.md
```

**Step 3: Add Reference Docs (Knowledge Base)**
Upload these as optional context (users can reference):
```
📖 MARKETING_OS_Research_GTM_Framework_v1.0.md
📖 MARKETING_OS_ProjectContext_Template_v1.0.md
📖 MARKETING_OS_Instructions_v1.0.md
📖 MARKETING_OS_TokenOptimization_v1.0.md
📖 MARKETING_OS_SetupGuide_v1.0.md (this file)
```

**Step 4: Test**
- Open the project
- Say: "I want to build project context for [YourCompany]"
- System should acknowledge and ask for Tier 1 context (ICP + channels)

---

### Option B: Cowork Mode (For Solo Use)

**Step 1: Folder Structure**
```
/agents/
├── CLAUDE.md (use MARKETING_OS_CLAUDE_v1.0.md)
├── project_marketing_context.md (create per project)
└── REFERENCE/ (optional reference docs)
    ├── MARKETING_OS_SkillOrchestration_Matrix.md
    ├── MARKETING_OS_KnowledgeStructure.md
    ├── tasks.md
    └── [other reference docs]
```

**Step 2: Copy Files**
- Move all MARKETING_OS_*.md files to your Cowork workspace
- Create `/agents/` folder
- Add custom instructions (CLAUDE.md)

**Step 3: Create Project Contexts**
- For each client/project, create: `[ProjectName]_marketing.md`
- Use the template
- Store in `/agents/` or `/projects/` folder

**Step 4: Reference in Cowork**
- Tell Claude: "My marketing system is in [Folder]"
- Claude loads context automatically

---

## First-Time Setup Checklist

- [ ] Decided: Claude.ai Projects OR Cowork mode?
- [ ] Created project/workspace
- [ ] Added CLAUDE.md (custom instructions)
- [ ] Added Skill Orchestration Matrix (reference)
- [ ] Added Knowledge Structure (templates)
- [ ] Created first project context file ([ProjectName]_marketing.md)
- [ ] Filled in: ICP, messaging, positioning (Tier 1 minimum)
- [ ] Tested: Asked Claude to route a skill
- [ ] Evaluated: First output scored 7+/10?

---

## Using the System (Daily Workflow)

### Morning Ritual (5 minutes)
1. Open Marketing OS project in Claude
2. Ask: "What's my status this week for [Project]?"
3. Claude loads project context
4. Review: What campaigns are live? What metrics came in overnight?

### Campaign Execution (1–2 hours)
1. Decide: What do I need? (copy, cold email, strategy, measurement?)
2. Describe request to Claude: "I need [outcome]"
3. Claude routes skill + estimates tokens
4. You approve or adjust scope
5. Claude executes
6. You evaluate (7+/10?) and ship or revise

### Weekly Review (30 minutes)
1. Open Marketing OS
2. Ask: "Summarize this week's campaign performance for [Project]"
3. Claude pulls metrics, highlights wins/losses
4. Ask: "What should we test next?"
5. Update project context with learnings

### Monthly Planning (1 hour)
1. Ask: "Plan next month for [Project]"
2. Claude:
   - Reviews current metrics
   - Suggests which channels/angles to scale
   - Recommends new experiments
   - Allocates token budget
3. You approve plan
4. Claude creates execution checklist

---

## Common Workflows

### Workflow 1: "I Need Copy"

**You say:** "I need landing page copy for [Project]"

**System does:**
1. Loads [Project]_marketing.md
2. Routes to **copywriting** skill
3. Asks: Scope? (Home page, pricing page, feature page?)
4. Estimates tokens (1.5–2K)
5. Executes copy
6. Evaluates (ICP match? Messaging alignment? Objection handling?)
7. Delivers: Draft + quality score + revision suggestions

**You do:** Review copy, approve, or ask for revision

---

### Workflow 2: "I Need a Cold Email Campaign"

**You say:** "Run cold email campaign for [Project]"

**System does:**
1. Loads [Project]_marketing.md
2. Routes to **cold-email** skill
3. Asks: How many variations? (1, 5, 10?)
4. Asks: Which ICP segment? (All, or specific company size?)
5. Estimates tokens (1.5–2.5K)
6. Executes: 5 email variations + 3 follow-ups
7. Also routes to **email-sequence** skill (nurture path)
8. Also routes to **analytics-tracking** (measurement setup)
9. Evaluates quality
10. Delivers: Full email sequence + tracking setup

**You do:** Copy emails, launch campaign, monitor replies

---

### Workflow 3: "I Need Strategy"

**You say:** "I'm starting a new project: [Description]"

**System does:**
1. Asks Tier 1 questions: "What's your ICP? What channels?"
2. Routes to **customer-research** + **competitive-analysis** (if needed)
3. Routes to **brand-storytelling** (if brand unclear)
4. Synthesizes into: [ProjectName]_marketing.md
5. Delivers: Complete project context ready for execution

**You do:** Provide research, approve context, start campaigns

---

### Workflow 4: "I Need Measurement"

**You say:** "Set up tracking for [Campaign Name]"

**System does:**
1. Loads campaign context
2. Routes to **analytics-tracking** skill
3. Asks: What events to track? (Opens, clicks, conversions?)
4. Sets up tracking implementation (what to measure, where, how)
5. Creates dashboard spec (metrics to watch weekly)
6. Estimates: 1–1.5K tokens

**You do:** Implement tracking in your platform

---

## How to Update Project Context

**When to update:**
- After 1 week of campaign data (learnings)
- After customer research (new ICP insights)
- When competitive landscape shifts
- When messaging tests reveal winning angles

**How to update:**
1. Open [ProjectName]_marketing.md
2. Find section to update (ICP, messaging, channels, etc.)
3. Revise with new data
4. Save
5. Tell Claude: "I updated [ProjectName] context. Use it for next campaign."

**Example:**
> "After running cold emails, I discovered VP Marketers respond 25% better to [specific angle]. Update messaging pillar #2?"
> Claude: "Done. Updated [Project]_marketing.md. Next campaign will emphasize [angle]."

---

## Evaluating Quality (When to Publish vs. Revise)

**After Claude executes any skill output (email, copy, strategy):**

### Quick Evaluation (30 seconds)
- Does it feel right? (Gut check)
- Does it match the ICP? (Quick scan)
- Would I send/publish this? (Honest answer)

### Full Evaluation (2 minutes)
Score on 4 questions:
1. **ICP Match (1–10):** Does it speak to my customer in their language?
2. **Messaging (1–10):** Does it hit my message pillars?
3. **Differentiation (1–10):** Is this unique to my company?
4. **Objections (1–10):** Does it address common concerns?

Average score = Quality Score
- **7–10:** Ready to publish
- **5–6:** Decent, but could be better (ask for revision)
- **1–4:** Missing something critical (revise)

---

## Token Budget Tracking

### Weekly Check-In
```
Q: How many tokens have I used this week?
A: [Claude pulls usage from past week]

Q: Am I on track for my 25K monthly budget?
A: [Math: weekly usage × 4 weeks = projected monthly]
```

### Monthly Review
```
Q: Summary of token usage for [Month]?
A: [Shows breakdown: Research 2K, Execution 12K, Measurement 4K, Iteration 2K = 20K total]

Q: What was most expensive?
A: [Execution phase, cold email + content]

Q: Can I optimize?
A: [Yes: batch more tasks, skip editing drafts, reuse context]
```

---

## Troubleshooting

### Problem: "Claude doesn't know my project context"
**Solution:** Make sure project file is in project (Claude.ai) or loaded in system prompt (Cowork)

### Problem: "Claude is routing to wrong skill"
**Solution:** Be more specific. Say: "I need a cold email, not general copywriting"

### Problem: "Output quality is below 7/10"
**Solution:** Check if ICP is clear in context. Usually a messaging problem, not skill problem.

### Problem: "Tokens are running high"
**Solution:** Batch tasks (5 emails instead of 1), skip polish for drafts, reuse context

### Problem: "I want to switch projects"
**Solution:** Say: "Switch to [Project B context]" and Claude will load it

---

## Advanced: Custom Skills & Integrations

### Adding New Skills
The system uses 25+ built-in marketing skills. If you need something custom:
1. Document the workflow
2. Add to tasks.md as "Future Enhancement"
3. Create custom prompt in CLAUDE.md

### Connecting to Tools
- **CRM (HubSpot, Pipedrive):** Use analytics-tracking + form-cro
- **Email Platform (Mailchimp, ConvertKit):** Use email-sequence skill
- **Ad Platform (LinkedIn, Facebook):** Use ad-creative + analytics-tracking
- **Website (Webflow, WordPress):** Use copywriting + form-cro

---

## Monthly Cadence

### Week 1: Planning
- Review last month's metrics
- Plan this month's campaigns
- Update project contexts with learnings

### Week 2: Execution
- Run primary campaigns (outbound, content, ads)
- Set up tracking
- Monitor early metrics

### Week 3: Optimization
- A/B test winning angles
- Pause underperformers
- Run follow-up campaigns

### Week 4: Analysis & Planning
- Full review of month's results
- Document learnings in project context
- Plan next month

---

## One-Pager: System Architecture

```
Claude Project (Marketing OS)
├── CLAUDE.md (Lean orchestration rules)
├── SkillOrchestration_Matrix (Routing logic)
├── KnowledgeStructure (Templates & libraries)
│
├── [Project A]_marketing.md (ICP, messaging, channels)
├── [Project B]_marketing.md
└── [Project C]_marketing.md

All projects → Share the same 25+ marketing skills
All skills → Reference the same templates + libraries
All campaigns → Report to shared metrics + learnings
```

---

## Support & Resources

**If stuck:**
- Reference the **MARKETING_OS_Instructions.md** (detailed behavioral rules)
- Check **MARKETING_OS_KnowledgeStructure.md** (templates)
- Review **MARKETING_OS_SkillOrchestration_Matrix.md** (which skill for what?)
- Check **MARKETING_OS_TokenOptimization_v1.0.md** (budgets)
- Look at **tasks.md** (known gaps + improvements)

**If you find a bug:**
- Document it in **tasks.md** under "Known Issues"
- Describe: What did you ask? What went wrong? What should happen?

**If you want to improve:**
- Add feature request to **tasks.md** under "Future Enhancements"

---

*Marketing OS v1.0 · Setup Guide · 2026-04-07*
*Everything you need to activate and use the system.*
