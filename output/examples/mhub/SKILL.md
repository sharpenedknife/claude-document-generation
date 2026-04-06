---
name: mhub
description: >
  Opens the airSlate Marketing Hub — a visual navigation menu for all marketing workflows.
  Use this skill whenever the user types /mhub, says "open marketing hub", "marketing menu",
  "take me to the hub", or asks for help with any marketing task and wants to choose from
  available workflows. Always use this skill when the user needs content creation, campaign
  planning, brand voice review, SEO audit, competitive intelligence, email sequences, or
  Slack announcements. Routes to the correct specialist workflow based on user selection.
---

# Marketing Hub — /mhub

Visual navigation menu for all airSlate marketing workflows. Renders a menu on invocation and routes to the correct skill based on user selection.

## On Invocation

Immediately render the navigation menu below as an HTML artifact. Do not ask questions first — show the menu, then wait for the user's selection.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Marketing Hub</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #0f0f13;
    color: #e8e8f0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px;
  }
  .hub {
    width: 100%;
    max-width: 760px;
  }
  .header {
    text-align: center;
    margin-bottom: 32px;
  }
  .header h1 {
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #fff;
  }
  .header h1 span { color: #7c6af7; }
  .header p {
    margin-top: 8px;
    font-size: 14px;
    color: #888;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
  .card {
    background: #1a1a24;
    border: 1px solid #2a2a38;
    border-radius: 12px;
    padding: 20px;
    cursor: pointer;
    transition: all 0.15s ease;
    position: relative;
    overflow: hidden;
  }
  .card:hover {
    border-color: #7c6af7;
    background: #1e1e2e;
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(124, 106, 247, 0.15);
  }
  .card .icon {
    font-size: 28px;
    margin-bottom: 12px;
    display: block;
  }
  .card h3 {
    font-size: 15px;
    font-weight: 600;
    color: #fff;
    margin-bottom: 6px;
  }
  .card p {
    font-size: 12px;
    color: #666;
    line-height: 1.5;
  }
  .card .badge {
    position: absolute;
    top: 14px;
    right: 14px;
    font-size: 10px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 20px;
    background: rgba(124, 106, 247, 0.15);
    color: #7c6af7;
    letter-spacing: 0.3px;
  }
  .card.wide {
    grid-column: span 2;
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 16px 20px;
  }
  .card.wide .icon { margin-bottom: 0; font-size: 22px; }
  .card.wide h3 { margin-bottom: 2px; font-size: 14px; }
  .card.wide p { font-size: 12px; }
  .shortcut {
    margin-top: 20px;
    padding: 14px 20px;
    background: #13131a;
    border: 1px solid #1e1e2a;
    border-radius: 10px;
    font-size: 12px;
    color: #555;
    text-align: center;
  }
  .shortcut kbd {
    background: #1e1e2e;
    border: 1px solid #333;
    border-radius: 4px;
    padding: 2px 7px;
    font-size: 11px;
    color: #888;
    font-family: monospace;
  }
</style>
</head>
<body>
<div class="hub">
  <div class="header">
    <h1>✦ <span>Marketing</span> Hub</h1>
    <p>airSlate · What would you like to work on today?</p>
  </div>

  <div class="grid">
    <div class="card" onclick="select('content')">
      <span class="icon">✍️</span>
      <div class="badge">Create</div>
      <h3>Content Creation</h3>
      <p>Blog posts, social copy, emails, landing pages, press releases</p>
    </div>

    <div class="card" onclick="select('campaign')">
      <span class="icon">🚀</span>
      <div class="badge">Plan</div>
      <h3>Campaign Planning</h3>
      <p>Full campaign briefs, calendars, channel strategy, success metrics</p>
    </div>

    <div class="card" onclick="select('brand')">
      <span class="icon">🎨</span>
      <div class="badge">Review</div>
      <h3>Brand Voice Review</h3>
      <p>Check any draft against airSlate brand guidelines before it ships</p>
    </div>

    <div class="card" onclick="select('seo')">
      <span class="icon">📈</span>
      <div class="badge">Audit</div>
      <h3>SEO & Performance</h3>
      <p>Keyword research, content gaps, rank tracking, performance reports</p>
    </div>

    <div class="card" onclick="select('competitive')">
      <span class="icon">🔍</span>
      <div class="badge">Intel</div>
      <h3>Competitive Intelligence</h3>
      <p>Research competitors, build battlecards, find positioning gaps</p>
    </div>

    <div class="card" onclick="select('email')">
      <span class="icon">📧</span>
      <div class="badge">Sequence</div>
      <h3>Email Sequences</h3>
      <p>Onboarding, nurture, re-engagement flows with timing and branching</p>
    </div>

    <div class="card wide" onclick="select('slack')">
      <span class="icon">💬</span>
      <div>
        <h3>Slack Announcements</h3>
        <p>Draft, format, and send announcements to team channels</p>
      </div>
    </div>
  </div>

  <div class="shortcut">
    Type a number or keyword, or just describe what you need →&nbsp;
    <kbd>content</kbd>&nbsp;<kbd>campaign</kbd>&nbsp;<kbd>brand</kbd>&nbsp;<kbd>seo</kbd>&nbsp;<kbd>competitive</kbd>&nbsp;<kbd>email</kbd>&nbsp;<kbd>slack</kbd>
  </div>
</div>

<script>
function select(type) {
  const map = {
    content: "Content Creation — I'll help you write blog posts, social copy, emails, or landing pages. What are you working on?",
    campaign: "Campaign Planning — Let's build a campaign brief. What's the goal and timeline?",
    brand: "Brand Voice Review — Paste the content you'd like me to check against airSlate brand guidelines.",
    seo: "SEO & Performance — Are we doing keyword research, a site audit, or a performance report?",
    competitive: "Competitive Intelligence — Which competitor or market are we researching?",
    email: "Email Sequences — What type of sequence: onboarding, nurture, re-engagement, or win-back?",
    slack: "Slack Announcements — What's the announcement and which channel?"
  };
  document.body.innerHTML = '<div style="font-family:-apple-system,sans-serif;background:#0f0f13;color:#e8e8f0;height:100vh;display:flex;align-items:center;justify-content:center;font-size:16px;padding:32px;text-align:center;">' + map[type] + '</div>';
}
</script>
</body>
</html>
```

## Routing After Selection

When the user selects a workflow (by clicking, typing a keyword, or describing a task):

| Selection | Route to |
|-----------|----------|
| content | `marketing:content-creation` skill |
| campaign | `marketing:campaign-plan` skill |
| brand | `marketing:brand-review` skill |
| seo | `marketing:seo-audit` skill |
| competitive | `marketing:competitive-brief` skill |
| email | `marketing:email-sequence` skill |
| slack | `slack-by-salesforce:draft-announcement` skill |

## Context to Apply

- Always apply airSlate brand voice (professional but approachable, B2B automation focus)
- Reference brand guidelines from `Documentation/` folder if available in session
- For Slack/Notion/Confluence/Jira tasks, use connected MCP tools to act directly — don't just generate content
- For content creation, ask for target audience, channel, and goal before drafting

## Invocation Patterns

This skill activates on:
- `/mhub` (explicit command)
- "open marketing hub"
- "take me to the hub"
- "marketing menu"
