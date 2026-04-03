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

## How Intake Works — Flexible Context Collection

No question is mandatory. Users can provide context however they want — paste API docs, describe the integration freeform, share existing MCP configs, or answer structured questions. Claude assesses what's needed and asks only for the gaps.

---

## Context Assessment

### Tier 1 — Minimum (can generate basic setup guide)
- [ ] **What system to connect to** — name and type of external system

Warn: "I know the system but not the specifics of what Claude needs to read or do. I'll generate a setup guide but the API reference and auth sections will be generic. Want me to proceed, or add more detail about the specific operations?"

### Tier 2 — Solid (good documentation)
Everything in Tier 1, plus:
- [ ] **Read operations** — what data Claude needs
- [ ] **Write operations** — what actions Claude takes
- [ ] **Auth method** — how to authenticate

### Tier 3 — Full (production-ready docs)
Everything in Tier 2, plus: operator persona, environment, error scenarios, happy-path example.

---

## Conversational Question Guide

Use these to fill gaps — only ask what's missing.

### Opening
> "Tell me about the MCP integration you need. What external system should Claude connect to, and what should it read or do? You can paste API docs, describe it freeform, or share an existing config."

---

**Q1: System Name & Type**
**Ask when:** System isn't clear.
**Ask:** "What external system does this MCP connect to? Name, type, and docs URL if available."
**Default if skipped:** Cannot default — this is minimum Tier 1 context.

**Q2: What Claude Needs to Read**
**Ask when:** Read operations aren't specified.
**Ask:** "What data does Claude need to read from this system? Be specific."
**Default if skipped:** Infer from system type (e.g., Slack → messages, channels, users). Mark as INFERRED.

**Q3: What Claude Needs to Do (Actions)**
**Ask when:** Write operations aren't specified.
**Ask:** "What actions must Claude take in this system?"
**Default if skipped:** Assume read-only. Mark as ASSUMED.

**Q4: Authentication**
**Ask when:** Auth method unknown.
**Ask:** "How does the MCP authenticate? API key, OAuth, service account?"
**Default if skipped:** Infer from system type. Mark as ASSUMED.

**Q5: Who Operates It**
**Ask when:** Operator persona unclear.
**Ask:** "Who installs and runs this MCP server? Developer, ops, or end user?"
**Default if skipped:** Assume developer. Mark as ASSUMED.

**Q6: Environment**
**Ask when:** Deployment context unclear.
**Ask:** "Where does this MCP run? Local, cloud, or inside Cowork/Claude Code?"
**Default if skipped:** Assume local developer machine. Mark as ASSUMED.

**Q7: Error Scenarios**
**Ask when:** User hasn't mentioned failure modes.
**Ask:** "What are the most common failure modes?"
**Default if skipped:** Generate generic error scenarios (auth failure, rate limit, not found). Mark as INFERRED.

**Q8: Happy Path Example**
**Ask when:** No example provided.
**Ask:** "Describe a complete example: user says → MCP calls → Claude returns."
**Default if skipped:** Generate from context. Mark as INFERRED.

---

## Outputs to Generate

Based on answers, generate in this order:

1. **`{system}-setup-guide.md`** — Installation, authentication, environment setup, verification
2. **`{system}-api-reference.md`** — Every available tool/command with params, returns, errors
3. **`{system}-schema-reference.md`** *(if applicable)* — Data models, field definitions, types
4. **`{system}-auth-guide.md`** *(if complex auth)* — Separate auth doc for OAuth, service accounts, etc.
5. **`{system}-troubleshooting.md`** — Top 5–7 error signatures with root causes and fixes

---

## Generation Checklist

- [ ] Context assessed — tier identified, assumptions listed
- [ ] User confirmed generation plan
- [ ] System name and API/tool type identified
- [ ] Every read operation listed with field-level specifics (or marked INFERRED)
- [ ] Every write action listed with required inputs and confirmation behavior (or marked ASSUMED read-only)
- [ ] Auth method documented (or marked ASSUMED with best guess)
- [ ] Operator persona confirmed or defaulted
- [ ] At least one complete end-to-end example
- [ ] Error signatures are exact strings (not "some kind of auth error")
- [ ] No hallucinated content — all items traceable to user input or marked ASSUMED/INFERRED
- [ ] All outputs pass Gates 1–5 before delivery
