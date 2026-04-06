# Codex Build Prompts — Documentation Builder Port
**Series of task prompts to give Codex to build the ChatGPT-equivalent Documentation Builder.**
Last updated: April 2026

> **How to use:** Submit these prompts to Codex in order. Each is a standalone task.
> Wait for each PR to be reviewed and merged before submitting the next.
> Repo must be connected to Codex via GitHub integration before starting.

---

## PRE-TASK: Repo Setup (do this manually before submitting any Codex task)

1. Fork or clone the Documentation Builder repo
2. Place `AGENTS.md` at repo root (use the file in `output/chatgpt-port/AGENTS.md`)
3. Connect repo to Codex via GitHub integration in Codex settings
4. Confirm Codex can read `AGENTS.md` by running: `codex run "What are your operating rules?"`

---

## TASK 1 — Scaffold ChatGPT Project Builder

**Submit to Codex:**

```
Create a new builder for ChatGPT Projects in the Documentation Builder system.

Context:
- The existing Claude Project builder is at builders/claude-project/ (BUILDER_Questions.md + BUILDER_Rules.md)
- We need an equivalent builder for ChatGPT Projects at builders/chatgpt-project/

What to create:

1. builders/chatgpt-project/BUILDER_Questions.md
   - Mirror the structure of builders/claude-project/BUILDER_Questions.md
   - Q0: What does this ChatGPT Project do? Who uses it?
   - RESEARCH GATE (same pattern as other builders): Ask user to collect manual workflows, reference files list, 3 real example requests, and 3 constraints before proceeding
   - Q1: Project name and one-liner
   - Q2: Primary use cases (max 5)
   - Q3: Knowledge base files (what files/docs does ChatGPT need to know?)
   - Q4: Custom instructions content (what rules + behaviors?)
   - Q5: Conversation starters (4 prompts)
   - Q6: GPT Actions needed? (external API integrations)
   - Q7: Skills needed? (which SKILL.md workflows to embed as inline instructions)
   - Q8: Distribution (private project / shared team / published GPT)
   - Context Tier Assessment section (same as other builders)
   - Context Confirmation section
   - Output Bundle section:
     | # | File | Purpose |
     | 1 | CHATGPT_CUSTOM_INSTRUCTIONS.md | Ready-to-paste Field A + Field B content |
     | 2 | KNOWLEDGE_BASE_MANIFEST.md | List of files to upload + priority order |
     | 3 | CONVERSATION_STARTERS.md | 4 starter prompts + rationale |
     | 4 | GPT_ACTIONS_SCHEMA.md | OpenAPI schemas (if Q6 needs actions) |
     | 5 | SETUP_GUIDE.md | Step-by-step setup instructions for ChatGPT Projects UI |

2. builders/chatgpt-project/BUILDER_Rules.md
   - Rules for generating each output doc
   - Custom Instructions rules: Field A max 1500 chars, Field B max 1500 chars
   - Knowledge base rules: max 20 files, prioritization criteria
   - Skills embedding rules: how to condense SKILL.md into inline instructions
   - GPT Actions rules: OpenAPI schema format requirements
   - Quality gate adaptations for ChatGPT platform

Read builders/claude-project/BUILDER_Questions.md and BUILDER_Rules.md as reference.
Follow the same section structure and quality standards.
Run all 5 exit gates on both generated files before committing.
Commit to builders/chatgpt-project/ and open a PR.
```

---

## TASK 2 — Create AGENTS.md Generator

**Submit to Codex:**

```
Create a script that generates AGENTS.md from CLAUDE.md.

Context:
- CLAUDE.md is the Claude Projects operating file (at repo root)
- AGENTS.md is the Codex equivalent (same content, Codex-adapted)
- We need a script that syncs them so they never drift

What to create:

1. scripts/generate_agents_md.py
   - Input: CLAUDE.md (repo root)
   - Output: AGENTS.md (repo root)
   - Transformations:
     a. Replace "Claude" → "Codex" in headings only (not in content referring to Claude Projects as a build type)
     b. Replace tool references in the Rules section:
        - "Read SKILL.md" → keep as-is (same pattern)
        - Add Codex-specific workflow section if not present (see output/chatgpt-port/AGENTS.md for reference)
     c. Add Codex Tool Reference table at end (map Claude tools → Codex equivalents)
     d. Update "How to Set Up" section with Codex setup steps
     e. Check total size: warn if > 28 KiB (approaching 32 KiB Codex limit)
   - Preserve all Rules, File Map, Quality Gates, and Authoritative File Priority sections unchanged
   - Output AGENTS.md to repo root

2. scripts/validate_agents_md.py
   - Check AGENTS.md exists and is under 32 KiB
   - Check required sections present: What This Is, Rules, File Map, Quality Gate Cheat Sheet
   - Check all file paths referenced in File Map actually exist in repo
   - Report missing files as warnings (not errors — repo may be partial)
   - Exit code 0 = valid, 1 = invalid

3. .github/workflows/sync_agents_md.yml
   - Trigger: on push to main when CLAUDE.md changes
   - Run: python scripts/generate_agents_md.py
   - Commit result: "chore: sync AGENTS.md from CLAUDE.md"
   - Run: python scripts/validate_agents_md.py
   - Fail CI if validation fails

Use Python 3.11+. No external dependencies beyond stdlib.
Run quality gates on all generated files.
Commit to scripts/ and .github/workflows/, open PR.
```

---

## TASK 3 — Port Skill Files to Codex Format

**Submit to Codex:**

```
Port the Documentation Builder skill files to Codex Skills format.

Context:
- Claude Skills live in skills/ directory (SKILL.md per skill)
- Codex Skills live in ~/.codex/skills/ and use the same SKILL.md format
- Key difference: tool references must be updated for Codex

What to create:

1. scripts/port_skills_to_codex.py
   - Input: skills/ directory (all SKILL.md files)
   - Output: codex-skills/ directory (Codex-adapted copies)
   - Transformations per SKILL.md:
     a. Replace in tool call examples:
        - `Skill tool: X` → `use-skill X` (in code blocks and examples)
        - `TodoWrite` → `update_plan`
        - `Bash` → shell commands (keep content, update framing)
     b. Update "How to Use This Skill" sections: replace Claude-specific invocation with Codex CLI instructions
     c. Keep YAML frontmatter identical (name, description, type fields same)
     d. Add frontmatter field: `codex_compatible: true`
   - Log: for each skill, print "Ported: {name}" or "Skipped: {name} — reason"

2. codex-skills/ directory
   - Contains all ported SKILL.md files
   - README.md explaining: "Copy these to ~/.codex/skills/ to install"

3. scripts/install_codex_skills.sh
   - Copies codex-skills/ → ~/.codex/skills/
   - Prints install summary
   - Usage: bash scripts/install_codex_skills.sh

Run the script against the current skills/ directory.
Commit codex-skills/ and scripts/ files, open PR.
```

---

## TASK 4 — Create Skill Embedding Tool (for ChatGPT)

**Submit to Codex:**

```
Create a tool that converts SKILL.md files into condensed inline instructions for ChatGPT Custom Instructions.

Context:
- ChatGPT Projects have no Skill equivalent
- Workaround: embed condensed skill playbooks directly in Custom Instructions Field B
- Field B has ~1500 char limit, so skills must be condensed
- We need to condense the most important stage skills for the Documentation Builder

What to create:

1. scripts/condense_skill_for_chatgpt.py
   - Input: path to a SKILL.md file + max_chars limit (default: 300 per skill)
   - Output: condensed inline instruction block
   - Algorithm:
     a. Extract: skill name (from YAML frontmatter)
     b. Extract: "When to Use" section → becomes trigger condition
     c. Extract: numbered steps from main procedure → keep first 5 steps max
     d. Extract: primary output format description (1 sentence)
     e. Format as: "SKILL [{name}]: When {trigger}, follow these steps: 1) ... 2) ... Output: ..."
     f. Truncate to max_chars if needed, ending at a complete sentence

2. scripts/generate_chatgpt_field_b.py
   - Input: list of skill names to embed (from config or CLI args)
   - Priority skills to embed for Documentation Builder:
     - writing-prds
     - architecture-designer
     - feature-forge
     - prompt-engineer
   - Output: complete Field B text ready to paste into ChatGPT
   - Includes: operating rules (from output/chatgpt-port/CHATGPT_CUSTOM_INSTRUCTIONS.md) + condensed skills
   - Validates total length <= 1500 chars
   - If over limit: drops lowest-priority skills and warns

3. output/chatgpt-port/CHATGPT_FIELD_B_GENERATED.md
   - Run the script and commit the generated output
   - This is the ready-to-paste Field B content with skills embedded

Run all scripts. Validate output is under 1500 chars. Commit to scripts/ and output/chatgpt-port/, open PR.
```

---

## TASK 5 — Build ChatGPT Knowledge Base Merger

**Submit to Codex:**

```
Create a script that merges multiple Documentation Builder system files into a single upload-ready file for ChatGPT Projects.

Context:
- ChatGPT Projects allow max 20 file uploads
- The Documentation Builder system has 30+ relevant files
- We need to merge lower-priority files to fit within the 20-file limit

What to create:

1. scripts/merge_for_chatgpt_kb.py
   - Reads config: config/chatgpt_kb_manifest.json (create this too)
   - config/chatgpt_kb_manifest.json format:
     {
       "priority_1_individual": ["list of files to upload individually"],
       "priority_2_merged": [
         {"output": "merged_builders.md", "inputs": ["list of files to merge"]},
         {"output": "merged_system_guides.md", "inputs": ["list of files"]}
       ],
       "excluded": ["list of files not needed in ChatGPT"]
     }
   - For each merge group: concatenate files with clear section headers
   - Output all files to: output/chatgpt-port/knowledge-base/
   - Print manifest: file name, size in KB, what it contains

2. config/chatgpt_kb_manifest.json
   - Priority 1 (upload individually, 8 files):
     system/guides/SYSTEM_Exit_Rules.md,
     system/guides/SYSTEM_Build_Decision_Framework.md,
     system/guides/SYSTEM_Content_Guide.md,
     system/templates/output/DOC_CANONICAL_TEMPLATE.md,
     system/templates/output/DEV_PLAN_TEMPLATE.md,
     system/templates/output/STARTER_PROMPT_TEMPLATE.md,
     builders/product/BUILDER_Questions.md,
     builders/product/BUILDER_Rules.md
   - Priority 2 (merge, target 8 output files):
     - merged_builders_chatgpt_skill_mcp.md = chatgpt-project + skill + mcp builders
     - merged_system_guides_2.md = File_Naming + Token_Optimization + Coding_Standards
     - merged_checklists.md = all 3 checklists combined
     - merged_config.md = token_budgets.json + domain_definitions.json
   - Excluded: output/, backlog/, metrics/, skills/ (too large / not needed)

3. output/chatgpt-port/knowledge-base/
   - Run the script and populate this directory
   - README.md: upload order, which files to prioritize

Total output files must be <= 20. Validate before committing.
Commit scripts/ + config/ + output/chatgpt-port/knowledge-base/, open PR.
```

---

## TASK 6 — Final Integration Test

**Submit to Codex:**

```
Run an end-to-end integration test of the Documentation Builder ChatGPT port.

What to test and document:

1. Validate all output files in output/chatgpt-port/:
   - AGENTS.md: check size < 32 KiB, required sections present
   - CHATGPT_CUSTOM_INSTRUCTIONS.md: check Field A <= 1500 chars, Field B <= 1500 chars
   - knowledge-base/: check total files <= 20, all files readable
   - CODEX_BUILD_PROMPTS.md: check all referenced scripts exist in scripts/

2. Validate all scripts:
   - Run scripts/validate_agents_md.py — must pass
   - Run scripts/merge_for_chatgpt_kb.py — must produce <= 20 files
   - Run scripts/generate_chatgpt_field_b.py — must produce <= 1500 chars

3. Generate output/chatgpt-port/PORT_VALIDATION_REPORT.md containing:
   - Date: 2026-04-XX
   - All files validated (list with pass/fail)
   - All scripts validated (list with pass/fail)
   - Total knowledge base files: N/20
   - Field A length: N/1500 chars
   - Field B length: N/1500 chars
   - AGENTS.md size: N KiB / 32 KiB limit
   - Any warnings or issues found
   - Setup instructions: exactly what to do to deploy the ChatGPT version

Run quality gates on PORT_VALIDATION_REPORT.md.
Commit report, open PR.
```

---

## TASK 7 — Sync Script (Ongoing Maintenance)

**Submit to Codex after all above tasks are merged:**

```
Create a maintenance script that keeps Claude and Codex/ChatGPT versions in sync when the Documentation Builder is updated.

What to create:

scripts/sync_all_platforms.sh
  - Step 1: Run scripts/generate_agents_md.py (sync CLAUDE.md → AGENTS.md)
  - Step 2: Run scripts/validate_agents_md.py (validate AGENTS.md)
  - Step 3: Run scripts/merge_for_chatgpt_kb.py (rebuild ChatGPT knowledge base files)
  - Step 4: Run scripts/generate_chatgpt_field_b.py (rebuild ChatGPT Field B)
  - Step 5: Run scripts/port_skills_to_codex.py (re-port any updated skills)
  - Step 6: Print summary: "Sync complete. Review output/chatgpt-port/ before deploying."
  - Step 7: Open draft PR with all changed files titled "chore: sync all platform variants"

Also create:
.github/workflows/sync_platforms.yml
  - Trigger: manual workflow_dispatch OR on push to main when builders/, system/, or skills/ changes
  - Run: bash scripts/sync_all_platforms.sh
  - Create draft PR automatically

This ensures the ChatGPT and Codex versions never drift from the Claude source of truth.
Commit scripts/ and .github/workflows/, open PR.
```

---

## Execution Order Summary

| Task | What it builds | Estimated time |
|------|---------------|----------------|
| 1 | ChatGPT Project builder (Questions + Rules) | 15-30 min |
| 2 | AGENTS.md generator + CI workflow | 10-15 min |
| 3 | Codex Skills porter + install script | 15-20 min |
| 4 | Skill condensation for ChatGPT Field B | 10-15 min |
| 5 | Knowledge base merger (20-file limit) | 10-15 min |
| 6 | Integration test + validation report | 15-20 min |
| 7 | Sync script for ongoing maintenance | 10-15 min |

**Total:** ~90-130 minutes of Codex agent time across 7 sequential PRs.

---

*Generated: April 2026*
*Source: Documentation Builder v1.5 · OpenAI_vs_Claude_Ecosystem_Comparison.md*
