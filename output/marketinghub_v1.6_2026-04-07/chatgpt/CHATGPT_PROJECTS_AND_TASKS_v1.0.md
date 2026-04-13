# Marketing Hub — ChatGPT Projects & Scheduled Tasks Setup
**Version:** 1.0 | **Date:** 2026-04-07
**Purpose:** Persistent context + automated marketing triggers

---

## WHY CHATGPT PROJECTS

ChatGPT Projects give you:
- Persistent custom instructions per product (survive between sessions)
- Memory tied to the project (ChatGPT remembers what you told it)
- File attachments that persist (ICP profiles, briefs, brand docs)
- Clean separation between products / clients

Each product you're marketing gets its own ChatGPT Project. GPTs run inside the project — they inherit its context.

---

## PROJECT SETUP — ONE PER PRODUCT

### Step 1: Create the Project

1. **chatgpt.com → Projects → New Project**
2. Name: `[Product Name] — Marketing`
3. Description: `Marketing context for [product]. Uses Marketing OS brief system from Claude.`

### Step 2: Upload Files to Project

Upload these to the Project (not to individual GPTs — Project files are available to all GPTs within it):

| File | Source | When to update |
|------|--------|---------------|
| ICP profiles | Output from ICP Builder | When ICP changes or new segment added |
| Messaging framework | Output from Messaging Builder | When positioning changes |
| QUICK_START.md | Marketing Hub bundle | One time at setup |

### Step 3: Set Project Custom Instructions

In Project → Instructions, paste:

```
This is the marketing workspace for [Product Name].

Product: [1-2 sentence description]
Primary ICP: [role, company size, main pain]
Secondary ICP: [if applicable]
Stage: [pre-launch / early traction / growth / scale]
Current focus: [channel or campaign Denis is running now]

When I paste a 📋 BRIEF FOR [GPT NAME]:
- Execute the brief immediately
- Do not ask me to clarify anything already in the brief
- Open canvas for all outputs
- End with "➡️ Bring this back to Claude for evaluation"

GPTs I use in this project:
- ICP Builder → customer research + profiles
- Messaging Builder → positioning + copy scoring
- Funnel Builder → funnel design + conversion audit
- Content Builder → all copy execution
- Build Planner → specs + launch plans
- Landing Builder → landing page copy + mockups
```

### Step 4: Enable Memory in the Project

ChatGPT Projects have memory. After a few sessions, ChatGPT will remember:
- Which ICP is the current focus
- What campaigns are running
- Denis's tone preferences
- What's been tried and discarded

To seed memory manually: start a conversation in the project and say:
```
Remember: My primary ICP is [description]. 
Current campaign: [what I'm running].
Preferred tone: direct, no filler.
I always use the 📋 BRIEF format from Claude.
```

---

## SCHEDULED TASKS SETUP

ChatGPT Scheduled Tasks run automated prompts on a schedule. Up to 10 active tasks.

Go to: **chatgpt.com → bottom left → Scheduled tasks → New task**

### Task 1: Weekly Content Brief Reminder (Every Monday, 9am)

**Name:** `Weekly Content Brief`
**Schedule:** Every Monday at 9:00 AM
**Prompt:**
```
It's Monday. Based on what I've been working on, remind me:
1. What content pieces are in progress from last week?
2. What should I brief Claude to plan this week?
3. What's the one highest-leverage content move I should make this week?

Keep it to 5 lines max. I'll take it to Claude for the actual brief.
```

### Task 2: ICP Research Refresh (Every 4 Weeks, Monday)

**Name:** `Monthly ICP Refresh`
**Schedule:** 1st Monday of each month, 8:00 AM
**Prompt:**
```
It's been a month. Do a quick search:
1. What are people saying about [pain point / product category] on Reddit and G2 this month?
2. Any new competitor moves or messaging shifts?
3. Is the ICP language I'm using still current?

Give me 3 bullet points I can bring to Claude to update my ICP brief.
```
**Capabilities needed:** Web Search ON (use ICP Builder GPT for this task, or enable web search in the project)

### Task 3: Campaign Status Ping (Every Friday, 5pm)

**Name:** `Friday Campaign Check`
**Schedule:** Every Friday at 5:00 PM
**Prompt:**
```
Friday check-in. What did I work on in Marketing OS this week?
Give me:
- Campaigns started
- Content shipped
- Anything still in evaluation with Claude
- One thing to follow up on Monday

3-5 bullet points. Quick.
```

### Task 4: Launch Countdown (One-time, set per launch)

**Name:** `[Launch Name] T-7 Check`
**Schedule:** One-time, 7 days before launch date
**Prompt:**
```
Launch is in 7 days. Run through the launch checklist:
- Landing page: ready?
- Email sequence: briefed to Content Builder?
- ICP research: done?
- Messaging validated by Claude?
- Anything still outstanding?

Tell me what's missing. I'll take it to Claude immediately.
```

---

## PROJECT TEMPLATE LIBRARY

Keep these in your ChatGPT Project as pinned files or in the Project's knowledge:

### Brief Templates (reference card)

```
━━━ CONTENT BUILDER ━━━
📋 BRIEF FOR CONTENT BUILDER
Project: | ICP: | Goal:
Content type: | Length: | Versions: 3
Key messages: | Objections: | Proof:
Tone: | Format:

━━━ ICP BUILDER ━━━
📋 BRIEF FOR ICP BUILDER
Project: | Market: | Goal:
Depth: | Pull from: | Output:

━━━ LANDING BUILDER ━━━
📋 BRIEF FOR LANDING BUILDER
Project: | ICP: | Primary CTA:
Sections: | Proof: | Tone:
Visual mockup: yes/no
```

Save this as `BRIEF_TEMPLATES.md` in Project knowledge. When you need to self-generate a brief without Claude, use this reference.

---

## WHAT LIVES WHERE

| Content | Lives in |
|---------|---------|
| ICP research output | ChatGPT Project files |
| Messaging framework | ChatGPT Project files |
| Current brief from Claude | Chat — paste and execute |
| Evaluated content | Return to Claude in chat |
| Content calendar | Code Interpreter → CSV → save locally |
| A/B test tracker | Code Interpreter → CSV → save locally |
| Scheduled triggers | ChatGPT Scheduled Tasks |
| Strategy and context | Claude.ai Project (Marketing OS) |

---

## TROUBLESHOOTING

**ChatGPT forgot my ICP between sessions**
→ Memory is active in Projects. Refresh it: open the project, say "Remember: My ICP is [description]. Confirm you have this."

**Scheduled task ran but used wrong GPT**
→ Scheduled tasks run in the default ChatGPT, not inside a GPT. For research tasks, set ICP Builder as the active GPT when the task fires, or paste the task output into ICP Builder manually.

**File I uploaded to project isn't being referenced**
→ Explicitly reference it: "Using the ICP profile I uploaded, build this brief." ChatGPT doesn't auto-read files unless prompted.

**Task limit reached (10 active)**
→ Delete completed one-time tasks (launch countdowns). Keep: weekly content brief, monthly ICP refresh, Friday check-in. Use remaining slots for active launch countdowns.

---

*ChatGPT Projects & Scheduled Tasks v1.0 · Marketing Hub · 2026-04-07*
