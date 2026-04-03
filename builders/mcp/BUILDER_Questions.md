# Builder: MCP Server

**Domain:** `reference` (MCP docs are operational reference, not AI-project docs)
**Use when:** Someone needs to document, set up, or help Claude connect to an external system via Model Context Protocol.

---

## Before You Ask Anything

Read `system/guides/SYSTEM_Build_Decision_Framework.md` → "MCP Server signals" to confirm this is the right builder.

**MCP vs Skill vs Claude Project:**
- MCP = live data + actions in external systems (Slack, Jira, databases, APIs)
- Skill = structured Claude workflow (no live external connection)
- Claude Project = persistent knowledge + persona

If the user wants Claude to both know things AND connect to tools: build the Project first, then document the MCPs.

---

## Intake Questions

Ask all questions before generating. Do not generate with unknowns.

**Q1: System Name & Type**
> What external system does this MCP connect to?
> - Name: (e.g., Slack, Jira, Ahrefs, Salesforce, PostgreSQL, internal REST API)
> - Type: SaaS tool / database / REST API / GraphQL API / file system / other
> - Official docs URL (if exists):

**Q2: What Claude Needs to Read**
> List the data Claude needs to read from this system.
> Be specific — not "Slack messages" but "messages from specific channels", "thread replies", "file attachments".
> For each: what is the data, how often does it change, is it sensitive?

**Q3: What Claude Needs to Do (Actions)**
> List the actions Claude must take in this system.
> Examples: "create Jira ticket", "send Slack message", "update Salesforce record", "run SQL query", "create calendar event"
> For each: inputs required, expected output, reversible or not?

**Q4: Authentication**
> How does the MCP authenticate?
> - API key (where obtained, rotation frequency)
> - OAuth 2.0 (which grant type, scopes needed)
> - Service account / JWT
> - Other
> Is auth per-user or shared (org-wide)?

**Q5: Who Operates It**
> Who installs and runs this MCP server?
> - Developer (self-hosted, command line)
> - Ops/DevOps (managed deployment)
> - End user (via Cowork plugin, no terminal access)
> What is their technical level?

**Q6: Environment**
> Where does this MCP run?
> - Local (developer machine)
> - Cloud (which provider, always-on)
> - Inside Cowork / Claude Code (plugin)
> Any environment constraints (network access, firewall, VPN)?

**Q7: Error Scenarios**
> What are the most common failure modes?
> Examples: "auth token expires", "API rate limit hit", "Jira project not found", "no results returned"
> For each: what should Claude do when this happens?

**Q8: Happy Path Example**
> Describe a complete example from user request to result:
> - User says: [exact request]
> - MCP calls: [which endpoints/tools, with what params]
> - Claude returns: [exact output]
> This becomes the primary example in the setup guide.

---

## Outputs to Generate

Based on answers, generate in this order:

1. **`{system}-setup-guide.md`** — Installation, authentication, environment setup, verification
2. **`{system}-api-reference.md`** — Every available tool/command with params, returns, errors
3. **`{system}-schema-reference.md`** *(if applicable)* — Data models, field definitions, types
4. **`{system}-auth-guide.md`** *(if complex auth)* — Separate auth doc for OAuth, service accounts, etc.
5. **`{system}-troubleshooting.md`** — Top 5–7 error signatures with root causes and fixes

Use doc type tokens from `config/token_budgets.json`. File names follow `DOMAIN_Topic_v{X.Y}_{YYYY-MM-DD}.md`.

---

## Generation Checklist

- [ ] All 8 questions answered before generation starts
- [ ] System name and API/tool type identified
- [ ] Every read operation listed with field-level specifics
- [ ] Every write action listed with required inputs and confirmation behavior
- [ ] Auth method documented with exact steps to obtain credentials
- [ ] Operator persona confirmed (developer / ops / end user) — drives tone and technical depth
- [ ] At least one complete end-to-end example
- [ ] Error signatures are exact strings (not "some kind of auth error")
- [ ] All outputs pass Gates 1–5 before delivery
