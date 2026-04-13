# Global AGENTS.md (Codex Configuration)

**Copy to:** `~/.codex/AGENTS.md`

This is the global behavior configuration for Codex across all projects.

---

## Global Behavior Rules

### Before Execution
- Always propose a plan before making changes
- Show the diff before writing files
- Ask for approval on risky operations (force push, destructive changes, etc.)

### During Execution
- Make minimal diffs—don't refactor unless requested
- Run tests before finalizing changes
- Preserve existing code style and conventions
- Comment code only if non-obvious

### Error Handling
- Stop and ask if you encounter ambiguity
- Provide specific error messages, not generic ones
- Suggest fixes, not just problems

### Code Quality
- No console.log debugging left in code
- All new functions have examples or tests
- No hardcoded values (use constants or env vars)

### Git & Version Control
- Commit messages follow: `type(scope): description`
- One logical change per commit
- Never force push without explicit permission

---

## Standard Commands

```
dev:    npm run dev       # Start development server
build:  npm run build     # Build for production
test:   npm run test      # Run tests
lint:   npm run lint      # Lint code
```

---

## Preferred Tech Stack

- Language: TypeScript (strict mode)
- Framework: React (functional components, hooks only)
- Database: PostgreSQL
- Testing: Jest + React Testing Library
- API: REST (consider GraphQL for complex queries)

---

## Testing Requirements

- All new logic must have tests
- Minimum 70% code coverage
- Run full test suite before finalizing changes
- Integration tests for API changes

---

## Default Assumptions (Unless Project AGENTS.md Says Otherwise)

- Prefer minimal dependencies
- Avoid package bloat
- Upgrade dependencies quarterly
- Security patches applied immediately
