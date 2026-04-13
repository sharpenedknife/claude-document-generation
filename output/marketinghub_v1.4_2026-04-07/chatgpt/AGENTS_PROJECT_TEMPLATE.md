# Project AGENTS.md (Repository-Level Codex Configuration)

**Copy to:** `/AGENTS.md` (root of your repo)

Replace [PLACEHOLDER] sections with your project specifics.

---

## Project Overview

**Repo:** [github.com/...]
**Language:** [TypeScript/Python/Go/etc.]
**Purpose:** [What this project does]
**Owner:** [Your name / team]

---

## Project Structure

```
[your-project]/
├── src/
│   ├── components/    [React components]
│   ├── pages/        [Next.js pages or routes]
│   ├── api/          [Backend handlers]
│   ├── lib/          [Utilities, helpers]
│   └── types/        [TypeScript definitions]
├── tests/            [Test files]
├── public/           [Static assets]
├── docs/             [Documentation]
└── [config files]
```

---

## Commands (Project-Specific)

```
dev:       [command to start dev server]
build:     [command to build for production]
test:      [command to run tests]
test:e2e:  [command to run end-to-end tests]
lint:      [command to lint]
deploy:    [command to deploy]
```

Example (Next.js):
```
dev:       npm run dev
build:     npm run build
test:      npm run test -- --watch
test:e2e:  npm run test:e2e
lint:      npm run lint
deploy:    vercel --prod
```

---

## Code Rules (This Project)

### TypeScript
- `strict: true` in tsconfig.json
- No `any` type—use generics or union types
- All API responses must be typed

### Naming Conventions
- Components: `PascalCase` (MyComponent.tsx)
- Utilities: `camelCase` (formatDate.ts)
- Constants: `UPPER_SNAKE_CASE` (API_BASE_URL)
- Files: match export name (utils/parseJSON.ts exports parseJSON)

### Component Structure
- Functional components only (no class components)
- Hooks for state management
- Props interface defined at top of file
- JSDoc comments for non-obvious logic

### Testing
- Unit tests for business logic
- Integration tests for API changes
- E2E tests for critical user flows
- Min 70% coverage for new code

---

## Git Workflow

### Commit Format
```
type(scope): description

[optional body]
[optional footer]
```

Types: `feat` | `fix` | `refactor` | `test` | `docs` | `chore`

Example:
```
feat(auth): implement JWT token refresh

- Add refresh token endpoint
- Auto-renew on expiration
- Store tokens in httpOnly cookies

Closes #123
```

### Branch Naming
- Feature: `feature/short-description`
- Bug fix: `fix/issue-description`
- Refactor: `refactor/area-of-change`

### PR Requirements
- Minimum 1 approval before merge
- All tests passing
- No console.log or debugger statements
- Squash commits before merge (unless history needed)

---

## Deployment

**Environment:** [staging / production]
**Trigger:** [Manual / Auto on merge / Scheduled]
**Check Before Deploy:**
- [ ] All tests passing
- [ ] No console errors in build
- [ ] Environment variables set correctly
- [ ] Database migrations applied (if needed)

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| [common issue 1] | [how to fix it] |
| [common issue 2] | [how to fix it] |
| [common issue 3] | [how to fix it] |

---

## Resources

- **Docs:** [link to project documentation]
- **Architecture:** [link to architecture doc]
- **Incidents:** [link to incident reports]
- **Runbooks:** [link to runbooks]

---

## When in Doubt

1. Check existing code patterns—follow them
2. If unclear, ask the owner or team
3. If a pattern is missing, document it here for next time

---

*Project AGENTS.md v1.1 · Update as project evolves*
