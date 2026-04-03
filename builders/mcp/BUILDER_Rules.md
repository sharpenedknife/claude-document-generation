# Builder Rules: MCP Server Documentation

**Applies to:** All MCP server documentation (setup guides, API references, schema docs, auth guides, troubleshooting)
**Authority:** These rules apply after `SYSTEM_Exit_Rules.md` and `SYSTEM_Content_Guide.md`.

---

## Rule 1: Every Tool/Command Must Be Fully Documented

The API reference must cover every available MCP tool. For each tool:

```markdown
### tool_name

**Purpose:** One sentence — what this tool does and why you'd call it.

**Parameters:**
| Parameter | Type | Required | Description |
|---|---|---|---|
| param_name | string | Yes | What it is, valid values, constraints |

**Returns:**
```json
{
  "field": "value",
  "description": "what this field contains"
}
```

**Example call:**
```json
{
  "tool": "tool_name",
  "params": { "param_name": "example_value" }
}
```

**Errors:**
| Error code / message | Root cause | Fix |
|---|---|---|
| "Not found" | Resource doesn't exist | Verify ID, check permissions |
```

No tool is documented with less than: purpose, params table, return shape, one example, error table.

---

## Rule 2: Auth Steps Must Be Runnable

Authentication documentation must include exact, runnable steps — not conceptual descriptions.

**Bad:**
> Obtain an API key from the provider and add it to your environment.

**Good:**
```markdown
### Step 1: Obtain API Key
1. Go to https://app.example.com/settings/api
2. Click "Generate new key"
3. Copy the key (shown once — store it now)
   Expected: key format is `sk-xxxxxxxxxxxxxxxxxxxx` (32 chars after `sk-`)

### Step 2: Configure Environment
1. Add to `.env`:
   ```
   EXAMPLE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
   ```
2. Verify: `echo $EXAMPLE_API_KEY` (should print your key, not blank)
```

---

## Rule 3: Error Signatures Must Be Exact Strings

Troubleshooting docs must use the actual error text that appears in logs or Claude's response — not paraphrases.

**Bad:** "If there's a permission error..."
**Good:** `"Error: Forbidden (403) — Missing scope: channels:read"`

To obtain exact strings: test the MCP, trigger the error, copy the output verbatim. If untested, mark as: `[DEBT: verify exact error signature — not yet tested]`.

---

## Rule 4: Rate Limits and Quotas Must Be Documented

Every API has limits. Document them explicitly:

```markdown
## Rate Limits

| Endpoint / Action | Limit | Reset period | Claude behavior when hit |
|---|---|---|---|
| Search messages | 50 req/min | Per minute | Wait 60s, retry once, then inform user |
| Create ticket | 100 req/hour | Per hour | Inform user, queue action for manual follow-up |
```

If rate limits are unknown: note this as DEBT. Do not omit the section.

---

## Rule 5: Actions Must Document Reversibility

For every write action, state whether it is reversible and what the revert process is.

```markdown
### createJiraIssue

**Reversibility:** Reversible
**How to undo:** Call `deleteJiraIssue` with the returned `issue_id`, or delete manually at [Jira issue URL].

**Caution:** Issues are visible to all project members immediately on creation. Notify relevant stakeholders if creating on their behalf.
```

Irreversible actions (deletes, sends) must include a confirmation step in the process docs:

```markdown
Before executing: confirm with user — "This will send a Slack message to #general. Proceed? (yes/no)"
```

---

## Rule 6: Fallback Behavior Must Be Defined

When an MCP is unavailable or returns an error, Claude must have explicit fallback instructions — not just error handling.

```markdown
## Fallback Behavior

If the Slack MCP is not connected or returns an error:
1. Inform user: "I can't reach Slack right now. I'll draft the message for you to send manually."
2. Generate the message in Slack mrkdwn format
3. Provide the channel name and suggested send time
```

"Try again later" is not a fallback. A fallback always delivers value to the user.

---

## Rule 7: Setup Guide Must End With a Verification Test

Every setup guide ends with a verification step that confirms the MCP is working:

```markdown
## Verify Setup

Run this command (or ask Claude to run it):
```
[exact verification command or Claude prompt]
```
Expected output:
```
[exact success output]
```

If you see this instead:
```
[exact failure output]
```
→ See Troubleshooting → [relevant error section].
```

---

## Rule 8: Operator Persona Drives Depth

The technical depth of every section must match the operator persona identified in Q5:

| Operator | Depth level |
|---|---|
| Developer | Full CLI commands, env var names, JSON configs, exact API call syntax |
| Ops/DevOps | Deployment configs, environment management, monitoring, log locations |
| End user | No terminal. Step-by-step GUI instructions, screenshots described, no raw JSON |

Do not mix depths within a single doc. If two operators need different docs, generate two docs.

---

## Gate Applicability

| Gate | Applies? | Notes |
|---|---|---|
| Gate 1 (naming) | Yes | `reference_{system}-{doctype}_v{X.Y}_{YYYY-MM-DD}.md` |
| Gate 2 (structure) | Yes | All required sections must be present per doc type |
| Gate 3 (content) | Yes | Error signatures exact, auth steps runnable, no vague fallbacks |
| Gate 4 (token budget) | Yes | `api-guide`: 3000 tokens · `setup-guide`: 2500 · `troubleshooting`: 2200 |
| Gate 5 (shipping) | Yes | Version stamp + all DEBTs logged before marking pass |
