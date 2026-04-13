# Marketing OS Restructured for ChatGPT
**Version:** 1.1 | **Date:** 2026-04-07 | **Architecture:** Projects/GPTs/Codex

---

## What Changed

The original Marketing OS was **monolithic** — one big system trying to be everything.

This version is **layered** — Projects hold context, GPTs hold methods, Codex handles execution. No mixing responsibilities.

---

## How to Install

### In ChatGPT

**Step 1: Create 5 Projects**
- Go to ChatGPT → Projects
- Create new project for each:
  - `Marketing OS` (use PROJECT_01_Marketing_OS.md as instructions)
  - `Content Engine` (use PROJECT_02_Content_Engine.md)
  - `Funnel / CRO` (use PROJECT_03_Funnel_CRO.md)
  - `[ClientName] Projects` (template: PROJECT_04_Client_Template.md, project-only memory)
  - `Coding / Product Dev` (use PROJECT_05_Coding_Product_Dev.md)

**Step 2: Create 5 GPTs**
- Go to ChatGPT → Create a GPT
- For each, use the GPT template as instructions:
  - `Research Architect` (use GPT_01_Research_Architect.md)
  - `Positioning & Messaging Critic` (use GPT_02_Messaging_Critic.md)
  - `Funnel Builder` (use GPT_03_Funnel_Builder.md)
  - `Copy / Email Rewriter` (use GPT_04_Copy_Rewriter.md)
  - `PRD / Product Thinker` (use GPT_05_PRD_Product_Thinker.md)

**Step 3: Add Knowledge Files (Optional)**
- Upload supporting docs to relevant Projects
- Create `.md` files for research, ICPs, tone guides, campaigns

### In Your Code Repos (Codex)

**Step 1: Global Config**
- Copy `AGENTS_GLOBAL.md` to `~/.codex/AGENTS.md`
- This sets global behavior rules for Codex

**Step 2: Per-Repo Config**
- Copy `AGENTS_PROJECT_TEMPLATE.md` to repo root as `AGENTS.md`
- Replace placeholders with your project specifics
- Update as repo evolves

---

## What's Included

### Projects (5)
- `PROJECT_01_Marketing_OS.md`
- `PROJECT_02_Content_Engine.md`
- `PROJECT_03_Funnel_CRO.md`
- `PROJECT_04_Client_Template.md`
- `PROJECT_05_Coding_Product_Dev.md`

### GPTs (5)
- `GPT_01_Research_Architect.md`
- `GPT_02_Messaging_Critic.md`
- `GPT_03_Funnel_Builder.md`
- `GPT_04_Copy_Rewriter.md`
- `GPT_05_PRD_Product_Thinker.md`

### Codex Setup (2)
- `AGENTS_GLOBAL.md` (→ `~/.codex/AGENTS.md`)
- `AGENTS_PROJECT_TEMPLATE.md` (→ repo `/AGENTS.md`)

### Architecture
- `ARCHITECTURE.md` (how it all fits together)

---

## Key Differences from v1.0

| Aspect | v1.0 | v1.1 |
|--------|------|------|
| Structure | 1 monolithic system | 3 separated layers |
| Projects | 1 catch-all | 5 focused, single-responsibility |
| GPTs | 1 big GPT | 5 specialized GPTs (stateless) |
| Memory | Everything in one place | Proper isolation (project-only for clients) |
| Codex | Not integrated | Full integration (AGENTS.md) |
| Context bleed | High (all projects mix) | Low (isolated by design) |
| Reusability | Low (everything is project-specific) | High (GPTs are stateless, reusable methods) |

---

## When to Use What

### Marketing OS Project
- Define ICPs and research customer problems
- Analyze competitors and identify positioning gaps
- Frame strategic decisions
- Archive quarterly strategy docs

### Content Engine Project
- Store tone guides and brand voice
- Build reusable content frameworks
- Execute content across channels
- Maintain editorial standards

### Funnel / CRO Project
- Map user journeys and identify drop-off points
- Design landing page flows
- Plan A/B tests and experiments
- Track conversion metrics and learnings

### Client Projects
- Isolated execution for each client
- All client-specific context stays here
- Use project-only memory to prevent bleed
- No cross-client contamination

### Coding / Product Dev Project
- Convert strategy into product specs
- Write PRDs that engineering can build from
- Track architecture decisions
- Plan features and roadmap

---

### Research Architect GPT
- When you have a vague question and need research design
- When you need to structure a discovery process
- When you need to plan customer interviews or surveys

### Positioning & Messaging Critic GPT
- When you have copy/positioning you want pressure-tested
- When you need to kill generic language
- When you need to prove every claim

### Funnel Builder GPT
- When you need to map user journeys
- When you need to identify friction points
- When you need to design conversion flows

### Copy / Email Rewriter GPT
- When you need copy polished for clarity
- When you need to reduce fluff and improve persuasion
- When you need multiple versions of the same message

### PRD / Product Thinker GPT
- When you have an idea and need a full PRD
- When you need product specs for engineering
- When you need to think through edge cases

---

## Real Workflow Examples

**Example 1: Launch a Cold Outbound Campaign**
```
1. Marketing OS Project → Define target ICP
2. Research Architect GPT → Design if-we-research methodology (optional)
3. Positioning Critic GPT → Validate messaging for this ICP
4. Content Engine Project → Create cold email templates
5. Copy Rewriter GPT → Polish emails for clarity
6. Funnel / CRO Project → Design funnel (email → landing page → trial)
7. Coding / Product Dev → Define success metrics and tracking
8. Codex → Implement tracking setup
```

**Example 2: Optimize a Failing Landing Page**
```
1. Funnel / CRO Project → Diagnose where people drop off
2. Funnel Builder GPT → Redesign the journey
3. Positioning Critic GPT → Is headline clear and compelling?
4. Copy Rewriter GPT → Improve clarity of CTA
5. Funnel / CRO Project → A/B test design
6. Codex → Implement variants and tracking
7. Measure → Track results, update learnings
```

---

## Common Mistakes to Avoid

❌ **Putting project-specific data in GPTs**
→ GPTs are stateless; they're methods, not memory

❌ **Using default memory for client projects**
→ Use project-only memory to prevent cross-client bleed

❌ **Creating too many GPTs**
→ 5 is enough; consolidate instead of proliferating

❌ **Skipping AGENTS.md in repos**
→ Codex needs rules to behave predictably

❌ **Mixing strategy + execution in one project**
→ Keep Marketing OS (strategy) separate from Content Engine (execution)

---

## Next Steps

1. **Read ARCHITECTURE.md** — understand how layers work together
2. **Create your 5 Projects** in ChatGPT using the templates
3. **Create your 5 GPTs** using the templates
4. **Test with one workflow** — e.g., launch a campaign
5. **Add AGENTS.md** to your coding repos
6. **Update as you evolve** — this system is living, not static

---

## Support

- **How do layers work?** → See ARCHITECTURE.md
- **How do I set up a project?** → See PROJECT_* files
- **How do I create a GPT?** → See GPT_* files
- **How do I configure Codex?** → See AGENTS_* files

---

*Marketing OS Restructured v1.1 · ChatGPT Architecture*
*Keep it small, keep it focused, keep it organized.*
