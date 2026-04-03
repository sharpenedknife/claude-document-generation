# Skill Map — AI Routing Table for Doc Generation
**What this is:** Operational instructions for Docgen. At each generation stage, this map tells you which skill to apply. Skills encode domain expertise — using them produces better docs than generating from scratch.
**When to read:** At Step 3 of the Interactive Operating Mode, before showing the generation plan. Re-read at each generation stage (Step 4).
**Last updated:** April 2026

---

## Routing Rules

1. **Before generating any doc**, find the current stage in this map.
2. **Apply the skill:**
   - **Cowork / Claude Code:** Call the skill using the `Skill` tool. Pass intake context (Q0–Q8 answers + previously generated docs) as input. Use the skill's output as the raw draft.
   - **Claude.ai Chat:** Skills aren't callable. Instead, apply the specific domain expertise each skill represents. The skill name tells you WHAT expertise to bring — e.g., `skills-library:architecture-designer` means: apply system design patterns, scalability tradeoffs, and framework-correct file structures.
3. **Format and gate the draft.** Apply DOC_CANONICAL_TEMPLATE formatting. Run all 5 quality gates. Skill output is a starting point, not a finished doc.
4. **If no skill matches**, generate from the template directly.
5. **Stack-specific skills are mandatory** — when the user picks a tech stack in Q5, the corresponding framework skill must be applied during Architecture, Setup, Dev Plan, and Starter Prompt generation. Skipping = generic file paths and config instead of framework-correct ones.

---

## Product Builder (Type 1) — Generation Order

### Stage 1: PRD Generation
**Call:** `skills-library:writing-prds`
**Input:** Q0 context, Q1 one-liner, Q2 MVP features, Q3 user flows
**Fallback if not available:** `product-management:write-spec`
**Then:** Run through DOC_CANONICAL_TEMPLATE + quality gates

### Stage 2: UX Generation
**Call:** `design:user-research` (if user hasn't validated flows) → then `skills-library:ui-ux-pro-max`
**Input:** PRD output + Q3 user types and flows
**Also call:** `design:ux-copy` for microcopy in the flows
**Then:** Quality gates

### Stage 3: UI Generation
**Call:** `skills-library:ui-ux-pro-max`
**Input:** UX output + Q3 flows
**Also call:** `design:accessibility-review` on the generated screen specs
**Also call:** `design:design-handoff` to generate component specs
**Stack-specific:** If React/Next.js → also call `skills-library:ui-styling` for shadcn/Tailwind component mapping
**Then:** Quality gates

### Stage 4: Vision
**No skill available.** Generate from template using Q0–Q3 context.

### Stage 5: Architecture
**Call:** `skills-library:architecture-designer`
**Input:** PRD + Data entities (Q4) + Tech stack (Q5) + Integrations (Q6)
**Also call:** `skills-library:api-designer` for API layer decisions
**Stack-specific (mandatory):** Call the framework skill from the stack table below. Feed it the architecture context and ask it to validate/enhance the file structure and technology choices.
**Then:** Quality gates

### Stage 6: Data Schema
**Call:** `skills-library:sql-pro` or `skills-library:postgres-pro` (based on Q5 database choice)
**Input:** Architecture output + Q4 data entities + user flows from UX
**Then:** Quality gates

### Stage 7: API Spec
**Call:** `skills-library:api-designer`
**Input:** Architecture output + Data Schema + PRD features
**If GraphQL:** Call `skills-library:graphql-architect` instead
**Then:** Quality gates

### Stage 8: Environment Setup
**Call:** `skills-library:devops-engineer` (for Docker/CI/CD) or `skills-library:cloud-architect` (for cloud deployment)
**Input:** Architecture + Tech stack + Integrations (Q6)
**Stack-specific:** Call framework skill for setup commands and configuration
**Then:** Quality gates

### Stage 9: Dev Plan
**Call:** `skills-library:feature-forge` for requirements → task breakdown
**Also call:** Stack-specific framework skill to validate phase tasks and file paths
**Also call:** `engineering:testing-strategy` for the testing phase
**Also call:** `engineering:deploy-checklist` for the deployment phase
**Input:** ALL previous docs (PRD through Setup)
**Then:** Quality gates (90/100 target)

### Stage 10: CLAUDE.md
**No skill needed.** Generate from template — this is Docgen's core output.

### Stage 11: Starter Prompt
**Call:** `skills-library:vibe-coding` for AI coding best practices
**Also call:** `skills-library:prompt-engineer` to optimize the prompt
**Input:** Dev Plan + CLAUDE.md + tool choice (Q7)
**Then:** Quality gates

---

## Claude Project Builder (Type 2) — Generation Order

### Project Instructions
**Call:** `skills-library:prompt-engineer`
**Input:** Q0 context, purpose, target users

### Knowledge Base Structure
**Call:** `skills-library:rag-architect` (if project needs retrieval over large docs)
**Input:** What knowledge the project needs access to

### Custom Skills (if project needs them)
**Call:** `skill-creator`
**Input:** Identified workflow patterns from intake

### MCP Integrations (if project needs live tools)
**Call:** `skills-library:mcp-developer` or `mcp-builder`
**Input:** Q6 integrations list

### Dev Plan + Starter Prompt
**Call:** `skills-library:prompt-engineer` for the starter prompt
**Call:** `skills-library:vibe-coding` for coding best practices

---

## Skill Builder (Type 3) — Generation Order

### SKILL.md
**Call:** `skill-creator` — **always, no exceptions**
**Input:** All intake answers (Q0–Q8)
**This skill handles the entire lifecycle:** create, structure, validate

### evals.json
**Call:** `ai-evals`
**Input:** SKILL.md output + expected behaviors

### Before Building — Duplicate Check
**Call:** Search the 341-skill catalog. If a matching skill exists, recommend customizing it instead of building from scratch. Categories to search:
- Check skill name/description against user's stated purpose
- Check `skills-library:*` variants first (these are installable)

---

## MCP Server Builder (Type 4) — Generation Order

### Setup Guide + API Reference
**Call:** `mcp-builder` — **always, no exceptions**
**Also call:** `skills-library:mcp-developer` for implementation details
**Input:** All intake answers

### Tool Schema Design
**Call:** `skills-library:api-designer`
**Input:** What the MCP server needs to read/write

### Auth Guide
**Call:** `mcp-builder` (handles auth patterns)

### Testing
**Call:** `engineering:testing-strategy`

---

## Stack-Specific Skill Table (Mandatory at Stages 5, 8, 9, 11)

When the user answers Q5 (tech stack), look up the framework skill below. Call it during Architecture, Setup, Dev Plan, and Starter Prompt generation to validate technology-specific decisions.

| Stack component | Skill to call |
|----------------|---------------|
| Next.js | `skills-library:nextjs-developer` |
| React | `skills-library:react-expert` |
| Vue 3 | `skills-library:vue-expert` |
| Angular | `skills-library:angular-architect` |
| React Native / Expo | `skills-library:react-native-expert` |
| Flutter | `skills-library:flutter-expert` |
| Swift / iOS | `skills-library:swift-expert` |
| NestJS | `skills-library:nestjs-expert` |
| Express / Node.js | `skills-library:javascript-pro` |
| FastAPI | `skills-library:fastapi-expert` |
| Django | `skills-library:django-expert` |
| Rails | `skills-library:rails-expert` |
| Laravel | `skills-library:laravel-specialist` |
| Spring Boot | `skills-library:spring-boot-engineer` |
| .NET / ASP.NET Core | `skills-library:dotnet-core-expert` |
| Go | `skills-library:golang-pro` |
| Rust | `skills-library:rust-engineer` |
| PHP | `skills-library:php-pro` |
| Python | `skills-library:python-pro` |
| TypeScript | `skills-library:typescript-pro` |
| PostgreSQL | `skills-library:postgres-pro` |
| SQL (general) | `skills-library:sql-pro` |
| GraphQL | `skills-library:graphql-architect` |
| WebSockets | `skills-library:websocket-engineer` |
| Kubernetes | `skills-library:kubernetes-specialist` |
| Terraform / IaC | `skills-library:terraform-engineer` |
| Docker / CI/CD | `skills-library:devops-engineer` |
| Playwright / E2E | `skills-library:playwright-expert` |
| WordPress | `skills-library:wordpress-pro` |
| Shopify | `skills-library:shopify-expert` |
| Salesforce | `skills-library:salesforce-developer` |

---

## Post-Bundle Skills (recommend to user after delivery)

After delivering the bundle, tell the user about these skills for their next phase:

### Go-to-Market
`marketing:campaign-plan`, `marketing:content-creation`, `marketing:email-sequence`, `marketing:seo-audit`, `skills-library:launch-marketing`, `skills-library:positioning-messaging`, `skills-library:copywriting`, `sales:competitive-intelligence`, `sales:draft-outreach`

### Growth & Optimization
`skills-library:page-cro`, `skills-library:signup-flow-cro`, `skills-library:onboarding-cro`, `skills-library:ab-test-setup`, `skills-library:churn-prevention`

### Pre-Build Validation (recommend if user hasn't validated)
`discovery:start-discovery`, `discovery:make-research`, `discovery:make-solution`, `discovery:make-decomposition`, `design:research-synthesis`, `skills-library:customer-research`, `skills-library:measuring-product-market-fit`

---

*This file is read by Docgen at generation time. It is not a user-facing document.*
