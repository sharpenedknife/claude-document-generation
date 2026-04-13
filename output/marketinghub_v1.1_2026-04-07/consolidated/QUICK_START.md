# Marketing OS — Quick Start Guide
**Version:** 1.0 | **Date:** 2026-04-07 | **Read time:** 3 minutes

---

## What You Have

Two complete marketing systems — one for Claude, one for ChatGPT. They share strategic frameworks but are optimized for each platform's strengths.

```
marketinghub_v1.0_2026-04-07.zip
├── claude/          ← Primary system (use this daily)
├── chatgpt/         ← Supplementary (specialized personas + canvas editing)
└── consolidated/    ← Single-file merges (for easy upload)
```

---

## Step 1: Decide Where to Start (2 min)

**Start with Claude if you:**
- Want full-funnel orchestration (research → outbound → content → measurement)
- Need token budget control
- Work with multiple projects that share the same skill set
- Want to dictate strategy and have Claude route the right tools

**Start with ChatGPT if you:**
- Want specialized personas (dedicated research, messaging critic, copy rewriter)
- Work primarily with long documents you want to edit inline (canvas)
- Already have a strong ChatGPT workflow

**Recommended:** Start with Claude for your first project context, then use ChatGPT GPTs for specialized tasks (Messaging Builder for copy review, Content Builder for writing/editing, Funnel Builder for CRO work).

---

## Step 2: Set Up Claude (10 min)

### 2a. Create the Project

```
Claude.ai → Projects → + New Project → Name: "Marketing OS"
```

### 2b. Upload Files

**Option A — Quick setup (one file):**
Upload `consolidated/CONTEXT_Marketing_OS_Claude.md` to Project Knowledge.

**Option B — Full setup (recommended):**
Upload from the `claude/` folder in this order:

```
1. MARKETING_OS_CLAUDE_v1.1_2026-04-07.md     ← Upload first (primary instructions)
2. MARKETING_OS_SkillOrchestration_Matrix.md
3. MARKETING_OS_KnowledgeStructure.md
4. MARKETING_OS_Instructions.md
5. MARKETING_OS_TokenOptimization.md
6. MARKETING_OS_SetupGuide_v1.1.md
7. MARKETING_OS_ProjectContext_Template.md
8. MARKETING_OS_Research_GTM_Framework.md
```

### 2c. Add Conversation Starters

In Project Settings → Conversation Starters, paste one per field:

```
🚀 Start a new project — build my marketing context from scratch
```
```
📧 Write a cold email campaign — I'll tell you the project
```
```
📊 Review this week's performance and tell me what to do next
```
```
✍ I need copy — landing page, email, or ad creative
```

### 2d. Test

Click "🚀 Start a new project" — Claude should ask for your ICP and project description.

**✅ Setup complete if:** Claude asks 2–3 questions and tells you the token estimate upfront.

---

## Step 3: Set Up ChatGPT (20 min)

### 3a. Create 5 Projects

```
ChatGPT → Projects → + New Project
```

Create these 5 (in order):
1. **Marketing OS** — upload `chatgpt/PROJECT_01_Marketing_OS.md`
2. **Content Engine** — upload `chatgpt/PROJECT_02_Content_Engine.md`
3. **Funnel / CRO** — upload `chatgpt/PROJECT_03_Funnel_CRO.md`
4. **Client Template** — upload `chatgpt/PROJECT_04_Client_Template.md`
5. **Coding / Product Dev** — upload `chatgpt/PROJECT_05_Coding_Product_Dev.md`

### 3b. Create 5 Custom GPTs

```
ChatGPT → Explore GPTs → + Create
```

For each GPT: paste the file contents as the system prompt, then add 4 conversation starters.

| GPT Name | File | Key Capability |
|----------|------|---------------|
| ICP Builder | `GPT_01_ICP_Builder.md` | Market maps, buyer profiles, competitor gaps |
| Messaging Builder | `GPT_02_Messaging_Builder.md` | 1–10 scoring rubric + rewrites |
| Funnel Builder | `GPT_03_Funnel_Builder.md` | Journey design + canvas funnel maps |
| Content Builder | `GPT_04_Content_Builder.md` | Write or rewrite any content format, 3 versions |
| Build Planner | `GPT_05_Build_Planner.md` | Feature specs + launch plans + GTM alignment |

**Conversation starters are already in each GPT file** (top of each file) — paste them directly into GPT → Configure → Conversation Starters.

### 3c. Test

Open **Messaging Builder GPT** → click "Critique this headline" → paste any headline.

**✅ Setup complete if:** You get a score grid (Q1–Q4) + 3 rewrites.

---

## Step 4: First Real Task (15 min)

### Option A: Build Your First Project Context (Claude)

This is the most important first step — all other skills depend on it.

1. Open Marketing OS in Claude.ai
2. Click "🚀 Start a new project"
3. Answer Claude's questions (ICP, channels, what you sell)
4. Get back: `[ProjectName]_marketing.md`
5. Upload it to your project
6. Ready for any campaign

### Option B: Get a Messaging Critique (ChatGPT)

If you have existing copy to improve:

1. Open **Messaging Builder GPT** in ChatGPT
2. Paste your landing page headline or cold email opening
3. Get: score grid (Q1–Q4) + 3 rewrites
4. Use the best rewrite

---

## Platform Quick Reference

### Claude — What to Say

| Goal | What to Type |
|------|-------------|
| Switch modes | `research mode` / `campaign mode` / `quick mode` |
| Start project | `🚀 Start a new project` |
| Cold email | `📧 Write a cold email campaign` |
| Copy | `✍ I need copy for [page/channel]` |
| Review | `📊 Review this week's performance` |
| Update context | `Update [Project] context — [what changed]` |
| Switch projects | `Switch to [Project B] context` |

### ChatGPT — Which GPT for What

| Task | GPT | Trigger |
|------|-----|---------|
| Research brief or ICP | ICP Builder | "Map my ideal customer" |
| Score my copy | Messaging Builder | "Score my landing page copy" |
| Audit my funnel | Funnel Builder | "Find my biggest conversion leak" |
| Write or rewrite content | Content Builder | "Write me a cold email / Make this sharper" |
| Feature spec or launch plan | Build Planner | "Turn this idea into a build plan" |

---

## Files in This Bundle

```
marketinghub_v1.0_2026-04-07.zip
│
├── claude/                                          ← Upload these to Claude Project
│   ├── MARKETING_OS_CLAUDE_v1.1_2026-04-07.md      ← PRIMARY (upload first)
│   ├── MARKETING_OS_Instructions_v1.0_2026-04-07.md
│   ├── MARKETING_OS_KnowledgeStructure_v1.0_2026-04-07.md
│   ├── MARKETING_OS_SkillOrchestration_Matrix_v1.0_2026-04-07.md
│   ├── MARKETING_OS_Research_GTM_Framework_v1.0_2026-04-07.md
│   ├── MARKETING_OS_ProjectContext_Template_v1.0_2026-04-07.md
│   ├── MARKETING_OS_TokenOptimization_v1.0_2026-04-07.md
│   ├── MARKETING_OS_SetupGuide_v1.1_2026-04-07.md
│   ├── MARKETING_OS_tasks_v1.0_2026-04-07.md
│   └── MARKETING_OS_README_v1.0_2026-04-07.md      ← This file's source
│
├── chatgpt/                                         ← Use per Project/GPT
│   ├── PROJECT_01_Marketing_OS.md
│   ├── PROJECT_02_Content_Engine.md
│   ├── PROJECT_03_Funnel_CRO.md
│   ├── PROJECT_04_Client_Template.md
│   ├── PROJECT_05_Coding_Product_Dev.md
│   ├── GPT_01_ICP_Builder.md                        ← v1.3 buyer profiles + competitor gaps
│   ├── GPT_02_Messaging_Builder.md                   ← v1.2 scoring rubric + rewrites
│   ├── GPT_03_Funnel_Builder.md                     ← v1.2 journey design + canvas
│   ├── GPT_04_Content_Builder.md                    ← v1.3 write/rewrite all formats
│   ├── GPT_05_Build_Planner.md                      ← v1.3 specs + launch plans + GTM
│   ├── AGENTS_GLOBAL.md
│   ├── AGENTS_PROJECT_TEMPLATE.md
│   ├── ARCHITECTURE.md
│   └── README_ChatGPT_Version.md
│
└── consolidated/                                    ← Single-file uploads
    ├── CONTEXT_Marketing_OS_Claude.md               ← All Claude docs merged
    ├── CONTEXT_Marketing_OS_ChatGPT.md              ← All ChatGPT docs merged
    └── QUICK_START.md                               ← This file
```

---

## Next After Setup

1. **Create project context** → Claude.ai → "🚀 Start a new project" (most important first step)
2. **Run first campaign** → Claude.ai → "📧 Write a cold email campaign"
3. **Score your existing copy** → ChatGPT → Messaging Builder → paste copy
4. **Set up tracking** → Claude.ai → "Set up analytics tracking for [Campaign]"
5. **Review after 1 week** → Claude.ai → "📊 Review this week's performance"

---

*Marketing OS v1.0 · Quick Start · 2026-04-07*
*Full-funnel marketing for solo operators — Claude + ChatGPT*
