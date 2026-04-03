# Chat-Ready Reference Files

These three consolidated files are optimized for Claude.ai Chat uploads. They merge individual source files from the Documentation Builder project into flat, single-file references.

## Files

### REFERENCE_Builders.md (72.4 KB)
**Content:** All builder intake questions + rules + SKILL MAP routing table

**Includes:**
- Product Builder questions & rules
- Claude Project Builder questions & rules
- Skill Builder questions & rules
- MCP Builder questions & rules
- AI-Docs Builder questions & rules
- Code Builder questions & rules
- SKILL MAP (AI routing table for skill assignment at each generation stage)

**Use when:** Building any type of project and need access to intake questions, builder rules, or skill routing logic.

### REFERENCE_System.md (180.1 KB)
**Content:** All 15 system guides (standards, frameworks, best practices)

**Includes:**
- SYSTEM_Build_Decision_Framework
- SYSTEM_Content_Guide
- SYSTEM_Exit_Rules
- SYSTEM_File_Naming
- SYSTEM_Coding_Standards
- SYSTEM_Architecture
- SYSTEM_Agent_Architecture
- SYSTEM_AI_First_Format
- SYSTEM_Project_Instructions_Rules
- SYSTEM_Token_Optimization
- SYSTEM_User_Journey
- SYSTEM_Version_Control
- SYSTEM_Prerequisites_Guide
- SYSTEM_Master_Index
- RESEARCH_Claude_Project_Best_Practices

**Use when:** Need to understand system-wide standards, AI-first architectural patterns, content guidelines, or quality gates.

### REFERENCE_Templates.md (57.1 KB)
**Content:** All templates, checklists, examples, and configuration

**Includes:**
- Output Templates (DOC_CANONICAL, DEV_PLAN, STARTER_PROMPT, DEBT_Specification)
- Project Instructions Templates (Docgen production & AI-first variations)
- Quality Checklists (Token Efficiency, Human Quality, AI Quality)
- Reference Examples (Perfect Setup Guide, and others)
- Configuration files

**Use when:** Need template structures, quality checklists, or example implementations to follow.

## How to Use

1. **Upload all three files to Claude.ai Projects** as project knowledge
2. **Reference by filename** in conversations: "Check REFERENCE_System.md for the quality gates" or "Show me the template from REFERENCE_Templates.md"
3. **Search within files** using Claude.ai's file search feature

## Original Source Files

For individual files, direct edits, or version control:
```
Documentation/
├── builders/
│   ├── product/
│   ├── claude-project/
│   ├── skill/
│   ├── mcp/
│   ├── ai-docs/
│   └── code/
├── system/
│   ├── guides/
│   ├── templates/
│   ├── checklists/
│   └── examples/
├── skills/
│   └── SKILL_MAP.md
└── config/
```

**GitHub:** https://github.com/sharpenedknife/claude-document-generation

## Version

- Created: 2026-04-04
- Builder Version: 2.5
- Python script: rebuild_references.py

## Maintenance

To rebuild these consolidated files:
```bash
python3 rebuild_references.py
```

The script merges all source files in dependency order and outputs to `/chat/`.
