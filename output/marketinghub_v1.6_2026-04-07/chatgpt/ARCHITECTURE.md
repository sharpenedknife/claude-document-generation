# Marketing OS Restructured — Architecture Guide

**Version:** 1.1 | **Date:** 2026-04-07 | **For:** ChatGPT

This is your workspace architecture: how PROJECTS, GPTs, and CODEX work together.

---

## The Three Layers

### Layer 1: PROJECTS (Memory + Context)
**What they are:** Persistent conversations that hold evolving knowledge.
**What they store:** Research, decisions, files, accumulated learning.
**When to use:** Ongoing work, strategy, execution tracking.
**Memory mode:** Default (shared) or project-only (isolated).

**Your 5 Core Projects:**
1. **Marketing OS** — Strategy, research, positioning
2. **Content Engine** — Production standards, frameworks, tone
3. **Funnel / CRO** — Journey design, optimization, experiments
4. **Client Projects** — Isolated per client (use project-only memory)
5. **Coding / Product Dev** — Specs, architecture, roadmap

---

### Layer 2: GPTs (Methods + Logic)
**What they are:** Reusable thinking patterns, stateless.
**What they do:** They run your methodology without holding context.
**When to use:** When you need a specific framework or critique applied.
**Memory mode:** None (GPTs don't learn or remember across sessions).

**Your 5 Core GPTs:**
1. **Research Architect** — Design research methodology, create briefs
2. **Positioning & Messaging Critic** — Pressure-test clarity & differentiation
3. **Funnel Builder** — Map user journeys, identify friction
4. **Copy / Email Rewriter** — Polish copy, improve clarity and conversion
5. **PRD / Product Thinker** — Convert ideas → product specs

---

### Layer 3: CODEX (Execution)
**What it is:** Your engineering agent—builds, deploys, fixes.
**What it does:** Code changes, file manipulation, testing, automation.
**When to use:** Implementation, not planning.
**Configuration:** AGENTS.md (global) + repo-local AGENTS.md.

---

## How They Work Together

### Example Workflow 1: Launch a Campaign

```
Step 1: STRATEGY (Marketing OS Project)
└─ Ask: "What should we focus on this quarter?"
   Output: Strategy doc, channel prioritization

Step 2: RESEARCH (Research Architect GPT)
└─ Ask: "Design customer research to validate this positioning"
   Output: Research brief, questions, methodology

Step 3: MESSAGING (Messaging Critic GPT)
└─ Ask: "Review our current positioning against competitors"
   Output: Critique, weak points, rewrite suggestions
   → Update Marketing OS with findings

Step 4: PRODUCTION (Content Engine Project)
└─ Ask: "Write blog post about [topic] for LinkedIn"
   Output: Content ready to publish

Step 5: FUNNEL (Funnel Builder GPT)
└─ Ask: "Design landing page flow to convert LinkedIn traffic"
   Output: Funnel map, stage assignments, CTA strategy

Step 6: COPY (Copy Rewriter GPT)
└─ Ask: "Polish the landing page headline and CTA"
   Output: Tighter, more persuasive versions

Step 7: MEASURE (Funnel / CRO Project)
└─ Ask: "Set up A/B test for headline variants"
   Output: Test design, success metrics, launch plan

Step 8: BUILD (Coding / Product Dev Project → Codex)
└─ Ask: "Implement the landing page from the PRD"
   → Handoff to Codex (via AGENTS.md)
```

---

### Example Workflow 2: Optimize Conversion

```
Current State: Landing page converting at 2%

Step 1: FUNNEL DIAGNOSIS (Funnel / CRO Project)
└─ Audit: Where do people drop off?
   Output: Drop-off analysis, heatmap data

Step 2: FUNNEL DESIGN (Funnel Builder GPT)
└─ Ask: "Design optimized flow for this journey"
   Output: New funnel map with clearer stages

Step 3: MESSAGING FIX (Messaging Critic GPT)
└─ Ask: "Does our headline clearly state the benefit?"
   Output: Critique, new headline options

Step 4: COPY IMPROVEMENT (Copy Rewriter GPT)
└─ Ask: "Improve clarity of this CTA button text"
   Output: 3 versions, each more direct

Step 5: TEST DESIGN (Funnel / CRO Project)
└─ Ask: "Design A/B test for landing page improvements"
   Output: Test hypothesis, variants, success metrics

Step 6: IMPLEMENT (Codex via Coding / Product Dev)
└─ Ask: "Update landing page with new variants"
   → Codex uses AGENTS.md to execute
   Output: Live test, tracking enabled
```

---

## Decision Tree: Which One Do I Use?

```
Do I need to REMEMBER this for next time?
├─ YES → Use PROJECT
│  (strategy, client context, accumulated research)
│
└─ NO → Do I need a REUSABLE METHOD?
   ├─ YES → Use GPT
   │  (research design, messaging critique, funnel mapping, copy polish, product specs)
   │
   └─ NO → Do I need to BUILD or EXECUTE code?
      ├─ YES → Use CODEX
      │  (implement, deploy, automate, fix bugs)
      │
      └─ NO → Just chat with me
         (quick questions, brainstorming, context setting)
```

---

## Context Isolation & Safety

### When to Use Project-Only Memory

Use **project-only memory** for:
- **Client Projects** (prevent cross-client context bleed)
- **Sensitive work** (NDAs, confidential strategy)
- **Parallel projects** (working on competitor products simultaneously)

Use **default memory** for:
- **Shared learnings** (marketing OS strategy applies to all projects)
- **Reusable frameworks** (content engine tone applies everywhere)
- **Cross-project patterns** (funnel learnings benefit all campaigns)

---

## Workflow: Adding to This System

### If You Need a New GPT
1. Identify the reusable methodology
2. Define when to use it (what problem does it solve?)
3. Write the GPT following `GPT_TEMPLATE.md`
4. Test with 2-3 scenarios
5. Add to this architecture guide

### If You Need a New Project
1. Identify the ongoing work (strategy, production, optimization?)
2. Define scope (what's in/out?)
3. Create project using `PROJECT_TEMPLATE.md`
4. Set memory mode (default or project-only?)
5. Link to relevant GPTs in this guide

### If You Need Codex Rules
1. Create `/AGENTS.md` in your repo
2. Use `AGENTS_PROJECT_TEMPLATE.md` as starting point
3. Define commands, testing, code rules
4. Update as project evolves

---

## Checklist: Is Your System Well-Designed?

- [ ] Maximum 5–7 Projects (no sprawl)
- [ ] Maximum 5–6 GPTs (focused methods only)
- [ ] Each Project has clear purpose + scope
- [ ] Each GPT is stateless (holds no project data)
- [ ] Client Projects use project-only memory
- [ ] AGENTS.md files exist (global + per-repo)
- [ ] Decision tree is clear (which layer for this task?)
- [ ] Handoff from Projects → GPTs → Codex is seamless

---

## Common Anti-Patterns to Avoid

❌ **Too many Projects**
→ Consolidate overlapping ones

❌ **Project-specific data inside GPTs**
→ Move to the relevant Project

❌ **GPTs that evolve over time**
→ That's a Project, not a GPT

❌ **Codex without AGENTS.md**
→ Code execution becomes unpredictable

❌ **Mixing strategy + execution in one Project**
→ Use separate Projects with clear separation

---

## Your System Map

```
┌───────────────────────────────────────────────────────────┐
│                    CHATGPT PROJECTS                        │
├───────────────┬───────────────┬───────────────┬───────────┤
│ Marketing OS  │ Content       │ Funnel / CRO  │ [Clients] │
│ (Strategy)    │ Engine        │ (Optimize)    │ (Isolated)│
│               │ (Produce)     │               │           │
└───────────────┴───────────────┴───────────────┴───────────┘
         ↓              ↓              ↓              ↓
┌───────────────────────────────────────────────────────────┐
│                    CHATGPT GPTS                            │
├──────────┬──────────────┬──────────┬───────────┬──────────┤
│ Research │ Positioning  │ Funnel   │ Copy      │ PRD /    │
│Architect │ & Messaging  │ Builder  │ Rewriter  │ Product  │
└──────────┴──────────────┴──────────┴───────────┴──────────┘
         ↓              ↓              ↓              ↓
┌───────────────────────────────────────────────────────────┐
│              CODEX (Engineering Execution)                 │
│  ├─ Global AGENTS.md (behavior rules)                     │
│  ├─ Repo AGENTS.md (project-specific commands/rules)      │
│  └─ Skills (feature-builder, bug-fixer, api-integrator)   │
└───────────────────────────────────────────────────────────┘
```

---

## Getting Started

1. **Set up your 5 Projects** in ChatGPT using `PROJECT_*.md` templates
2. **Activate your 5 GPTs** using `GPT_*.md` templates
3. **Add AGENTS.md files** to your coding projects
4. **Follow the workflow** for campaigns and optimization
5. **Update this guide** as you evolve the system

---

*Marketing OS Restructured v1.1 · Architecture Guide for ChatGPT*
