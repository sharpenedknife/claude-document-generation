# Version Control Strategy

How to version documents, manage updates, deprecate, and archive.

---

## Core Principle

**One version is current. All others are archival.**

A doc can have v1.0, v1.1, v2.0 but only ONE is "production" (users see it).

---

## Version Numbering

```
v1.0  = Initial release (production)
v1.1  = Patch update (bug fix, clarification) (production)
v1.2  = Patch update (production)
v2.0  = Major revision (new content, structure, approach) (production)
```

**When to increment:**

| Change | Version | Example |
|--------|---------|---------|
| Typo fix | Patch (v1.0 → v1.1) | "Fix: 'environemnt' → 'environment'" |
| Clarification | Patch (v1.0 → v1.1) | "Add example to Step 3 for clarity" |
| 1-2 new sections | Patch (v1.0 → v1.1) | "Add 2 troubleshooting errors" |
| Structural changes | Minor (v1.0 → v2.0) | "Reorganize prerequisites, add validation section" |
| New approach/context | Minor (v1.0 → v2.0) | "GTM Strategy completely rewritten for new market segment" |
| Content outdated (>1 year) | Deprecate v1.x, create v2.0 | Market shifted, new numbers, new approach |

---

## File Structure

```
output/{domain}/
├── v1.0/                    # Original release
│   ├── {DOC_NAME}.md        # Live version (what users see)
│   ├── {DOC_NAME}.DEBT.md   # Known limitations
│   └── metadata.json        # Generation metadata
│
├── v1.1/                    # Patch update
│   ├── {DOC_NAME}.md        # Updated version
│   ├── {DOC_NAME}.DEBT.md   # Remaining debt
│   └── metadata.json        # New generation metadata
│
├── v2.0/                    # Major revision
│   ├── {DOC_NAME}.md        # Rewritten version
│   ├── {DOC_NAME}.DEBT.md   # New debt list
│   └── metadata.json        # New metadata
│
└── archive/                 # Old versions (< 1 year old)
    ├── [DEPRECATED]_{DOC_NAME}_v1.0_2025.md
    └── [DEPRECATED]_{DOC_NAME}_v1.1_2025.md
```

**Rules:**
- Only ONE version folder is "current" (others are historical)
- `archive/` contains deprecated versions (marked with [DEPRECATED])
- Each version folder is self-contained (can access any version anytime)

---

## Status Field (In Frontmatter)

Every doc frontmatter includes:

```yaml
status: production|draft|review|deprecated
version: 1.0|1.1|2.0|etc
deprecated_date: YYYY-MM-DD (if deprecated)
```

### Status Definitions

**production:** Current, live version. Users see this.

**draft:** Being written, not complete. Not shipped.

**review:** Completed but awaiting approval. All gates passed, waiting final sign-off.

**deprecated:** Old version, no longer recommended. Archived but accessible.

---

## Deprecation Process

### Step 1: Create Newer Version

User creates v2.0 (major update) or v1.1 (patch).

```yaml
version: 2.0
status: production  # ← This becomes the new current
```

### Step 2: Mark Old Version Deprecated

Old v1.0 file renamed and moved:

```
Before: output/gtm/v1.0/GTM_Strategy_2026.md
After:  output/gtm/archive/[DEPRECATED]_GTM_Strategy_2026_v1.0_2025.md
```

Old v1.0 frontmatter updated:

```yaml
version: 1.0
status: deprecated
deprecated_date: 2026-04-02
replacement_version: 2.0
migration_guide: "See: GTM_Strategy_v2.0_Migration_Guide.md"
```

### Step 3: Create Migration Guide (If Major Change)

For v1.0 → v2.0, create optional migration doc:

```
SYSTEM_GTM_Strategy_v2.0_Migration_Guide.md

Contents:
- What changed in v2.0
- Why it changed
- How to migrate from v1.0 approach
- New features
- Removed features
```

### Step 4: Update Related Docs

If other docs reference deprecated v1.0:

```markdown
# Old doc reference
See: GTM_Strategy_2026_v1.0  ← Users might have bookmarks
```

Update to:

```markdown
# New doc reference (with deprecation notice)
See: GTM_Strategy_2026_v2.0 (v1.0 is deprecated)
```

### Step 5: Announce Deprecation

Add entry to DEPRECATION_LOG.md:

```markdown
## Deprecation Log

### GTM_Strategy_2026 (v1.0 → v2.0)
- **Deprecated:** 2026-04-02
- **Version:** v1.0
- **Reason:** New market segment requires different GTM approach
- **Replacement:** GTM_Strategy_2026_v2.0
- **Migration Guide:** See SYSTEM_GTM_Strategy_v2.0_Migration_Guide.md
- **EOL Date:** 2026-07-02 (3 months from deprecation)
- **Users affected:** Sales team, Product marketing
- **Archive location:** output/gtm/archive/[DEPRECATED]_GTM_Strategy_2026_v1.0_2025.md
```

---

## Version Lifespan

```
v1.0 Published        Today: 2026-04-02
    ↓
v1.1 Small update     2026-04-15 (13 days later, same version folder)
    ↓
v2.0 Major revision   2026-05-01 (new folder: v2.0/)
    ↓
v1.1 deprecated       2026-05-01 (marked deprecated, moved to archive/)
    ↓
v1.1 EOL              2026-08-01 (90 days after deprecation)
    ↓
v1.1 deleted          2026-08-01 (or kept in archive forever)
```

**Default lifespan:**
- v1.x: 6 months as current, then deprecated, then EOL at 9 months
- v2.x: Current until v3.0, then 6-month deprecation period

---

## What Users See

```
Current (Production):
✅ v2.0 ← Direct link in Projects
   "This is the current version"

Older (Archived):
📦 v1.1 ← Accessible but marked deprecated
   "This version is deprecated. See: v2.0"

   v1.0 ← Accessible but marked deprecated
   "This version is deprecated. See: v2.0"
```

---

## Update Types & Process

### Type 1: Patch Update (v1.0 → v1.1)

**When:** Typo, clarification, 1-2 new errors, example fix

**Process:**
1. Clone v1.0 folder to v1.1
2. Make edits in v1.1 files
3. Update version in frontmatter: `version: 1.1`
4. Update metadata.json (new date, unchanged doc_type)
5. Run Exit Gates 3-5 only (skip structure check, we know it's good)
6. Mark v1.0 as no-longer-current (optional, depends on storage)
7. Users see v1.1 in Projects

**Example:** Fix 3 broken links, clarify Step 2, add new troubleshooting error

### Type 2: Major Revision (v1.x → v2.0)

**When:** New approach, new structure, updated context, different audience

**Process:**
1. Create NEW doc: v2.0 (not edit v1.x)
2. Rewrite or significantly restructure
3. Use same doc_type, new version: `version: 2.0`
4. Run ALL Exit Gates (1-5)
5. Create DEBT.md for v2.0 (fresh list)
6. Create migration guide if major (optional)
7. Mark v1.x as `deprecated: true` in frontmatter
8. Move v1.x files to `archive/` folder
9. Rename: `{NAME}.md` → `[DEPRECATED]_{NAME}_v1.x_YYYY.md`
10. Update metadata.json with deprecation notice
11. Users see v2.0 in Projects, can access v1.x in archive

**Example:** GTM strategy changes for new market segment, new structure, new metrics

---

## In Claude Projects

### Current Version Only

Users see only ONE version in project knowledge base:

```
Projects/docgen/knowledge_base/
├── GTM_Strategy_2026_v2.0.md       ← CURRENT
├── DESIGN_Button_System_v1.0.md    ← CURRENT
├── BRANDING_Voice_Guidelines.md    ← CURRENT (no version)
└── [Archived docs not shown here]
```

Project instructions:

```markdown
## Document Versions

If you're looking for an older version of a doc:

1. **Check project knowledge base** (current versions only)
2. **For archived versions**, see output/archive/ in the docgen repo
3. **For migration guides**, see SYSTEM_Migration guides
```

### Update Process

When v1.0 → v2.0:

1. New v2.0 created and tested
2. v1.0 marked deprecated in docgen folder
3. Project knowledge base updated:
   - Remove v1.0 file
   - Add v2.0 file
   - Update related_docs references
4. v1.0 accessible via docgen repo archive for historical reference

---

## Deprecation Timeline

```
Month 1: v2.0 published, v1.0 deprecated
  - v1.0 marked [DEPRECATED] in archive
  - Users notified: "v2.0 available, see migration guide"
  - Both versions visible (v2.0 current)

Month 2-3: v1.0 in deprecation period
  - Active notification: "v1.0 deprecated, use v2.0"
  - Support: Questions about v1.0 → redirect to v2.0
  - v1.0 still accessible in archive

Month 4: v1.0 EOL
  - v1.0 removed from archive searches
  - Still accessible if linked directly
  - Support: v1.0 questions → "No longer supported"

Month 6-12: v1.0 in cold storage
  - Deleted from project access
  - Still in git history if needed
  - Special request only
```

---

## Version Tracking

Every doc has metadata.json tracking all versions:

```json
{
  "document": "GTM_Strategy_2026",
  "current_version": "2.0",
  "status": "production",
  
  "version_history": [
    {
      "version": "1.0",
      "released": "2026-01-15",
      "status": "deprecated",
      "reason": "New market segment GTM requires v2.0",
      "replacement": "2.0",
      "eol_date": "2026-08-15",
      "location": "output/gtm/archive/"
    },
    {
      "version": "1.1",
      "released": "2026-02-01",
      "status": "deprecated",
      "reason": "Superseded by v2.0",
      "replacement": "2.0",
      "eol_date": "2026-08-01",
      "location": "output/gtm/archive/"
    },
    {
      "version": "2.0",
      "released": "2026-05-01",
      "status": "production",
      "reason": "Current version",
      "replacement": null,
      "eol_date": null,
      "location": "output/gtm/v2.0/"
    }
  ]
}
```

---

## Automation: Version Management

Builder should support:

```
User actions:
1. "Update existing doc" → Increment version (1.0→1.1 or 1.x→2.0)
2. Select update type:
   - "Patch (typo/clarification)" → v1.1
   - "Minor (add sections)" → v1.2
   - "Major (new approach)" → v2.0
3. Clone current version
4. Edit in new version folder
5. Run appropriate exit gates
6. Deprecate old version (automated)
7. Update Projects knowledge base (automated)
8. Log in version history (automated)
```

---

## Version Cleanup

Every 6 months, audit versions:

```bash
#!/bin/bash
# Find deprecated docs >1 year old

find output/ -name "[DEPRECATED]*.md" -mtime +365 | while read file; do
  echo "Can delete (>1 year old): $file"
done
```

Decision: Keep in archive 1-2 years, then delete (keep in git history).

---

## Version Control Checklist

Before shipping v2.0:

- [ ] v1.x is marked `status: deprecated`
- [ ] v1.x moved to `archive/` folder
- [ ] v1.x renamed with [DEPRECATED] prefix
- [ ] v2.0 frontmatter: `version: 2.0`, `status: production`
- [ ] v2.0 metadata.json created
- [ ] Migration guide created (if major change)
- [ ] DEPRECATION_LOG.md updated
- [ ] Related docs updated to reference v2.0
- [ ] Projects knowledge base updated (v1.x removed, v2.0 added)
- [ ] Users notified if applicable (email, chat, etc.)
- [ ] v1.x EOL date set (6-12 months out)

---

## Real-World Example: GTM Strategy Versioning

```
Timeline:
Q1 2026: v1.0 published (mid-market focus)
↓
Q2 2026: v1.1 patch (add competitive analysis)
↓
Q3 2026: v2.0 major revision (enterprise focus, new market)
         v1.0 & v1.1 deprecated

Folder structure Q3:
output/gtm/
├── v1.0/
│   ├── GTM_Strategy_2026.md (OLD, don't use)
│   └── ...
├── v1.1/
│   ├── GTM_Strategy_2026.md (OLD, don't use)
│   └── ...
├── v2.0/
│   ├── GTM_Strategy_2026.md (CURRENT)
│   └── ...
├── archive/
│   ├── [DEPRECATED]_GTM_Strategy_2026_v1.0_Q1_2026.md
│   ├── [DEPRECATED]_GTM_Strategy_2026_v1.1_Q2_2026.md
│   └── SYSTEM_GTM_Strategy_v2.0_Migration_Guide.md
```

Users see: GTM_Strategy_2026_v2.0 (current)
Can access: Old versions in archive if needed
Know: v1.x is deprecated, should migrate
