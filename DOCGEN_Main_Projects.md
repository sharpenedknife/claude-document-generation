# DOCGEN: Main Projects Specification

Each main project generates a specific set of documents. User can add up to 2 workflows on top.

---

## Project 1: Fast Product MVP (Startup Focus)

**Time:** 2 hours  
**Best for:** Building MVP in 4-6 weeks  
**Input:** Product idea + target user  

### Documents Generated

#### 1. PRD (Product Requirements Document)
```yaml
Sections:
  - Overview (1 sentence)
  - Problem statement
  - Solution overview
  - Target user
  - Key features (MVP only)
  - Success metrics
  - Timeline (4-6 weeks)
  - Scope & non-scope
  - Acceptance criteria per feature

AI-readable for: Claude to understand product
```

#### 2. UX Requirements
```yaml
Sections:
  - User journey map (text description)
  - Core user flows (3-5 main flows)
  - Wireframe descriptions (no images)
    - Login/Signup
    - Main dashboard
    - Key feature pages
  - Interaction patterns
  - Accessibility requirements (WCAG AA)

AI-readable for: Claude to design + code UI
```

#### 3. specifiers.md (Technical Specs)
```yaml
Sections:
  - Tech stack (frontend, backend, DB, hosting)
  - Data model (main entities + relationships)
  - API endpoints (if backend)
  - Environment variables needed
  - Third-party integrations
  - Performance targets
  - Security requirements (auth, data protection)

AI-readable for: Claude to scaffold code
```

### Questionnaire

```
Q1: What's your product?
    "A real-time collaboration tool for remote teams"

Q2: Who's the target user?
    "Product teams at 10-100 person startups"

Q3: What's the main problem you're solving?
    "Teams waste time in async communication and meetings"

Q4: Top 3 features for MVP?
    "1. Document collaboration
     2. Comment threads
     3. Real-time presence"

Q5: Timeline?
    "6 weeks"

Q6: Tech preferences?
    "React + Node.js + PostgreSQL"

[Generate]
```

---

## Project 2: Feature Release (Existing Product)

**Time:** 2.5 hours  
**Best for:** Shipping new feature to existing product  
**Input:** Product + feature idea + target users  

### Documents Generated

#### 1. PRD (Feature-Focused)
```yaml
Sections:
  - Feature overview
  - Why now? (market timing, user feedback)
  - Target user segment
  - Problem this solves
  - Success metrics (adoption, engagement, revenue)
  - Feature details
  - Edge cases & error handling
  - Acceptance criteria
  - Rollout strategy (phased, A/B test, etc.)
```

#### 2. UX Requirements
```yaml
Sections:
  - User flows for feature
  - Integration with existing flows
  - Wireframe descriptions
  - Interaction states (loading, error, success)
  - Mobile considerations
  - Accessibility
```

#### 3. specifiers.md
```yaml
Sections:
  - Implementation approach
  - API changes needed
  - Database changes
  - Dependencies
  - Performance impact
  - Backward compatibility concerns
```

#### 4. safety.md (Feature Safety)
```yaml
Sections:
  - Security considerations
  - Privacy implications
  - Rate limiting / abuse prevention
  - Data retention
  - Compliance requirements
  - Testing strategy (unit, integration, e2e)
  - Rollback plan
  - Monitoring & alerting
```

### Questionnaire

```
Q1: What feature are you building?
    "AI-powered meeting summaries"

Q2: For which user segment?
    "Enterprise customers"

Q3: Why now?
    "4 top customers requested it, AI costs dropped"

Q4: Success metrics?
    "50% adoption, 10% time saved per meeting"

Q5: Timeline?
    "8 weeks"

Q6: Rollout strategy?
    "Phased: beta with 3 customers, then gradual rollout"

[Generate]
```

---

## Project 3: Workflow Automation

**Time:** 2 hours  
**Best for:** Automating internal processes  
**Input:** Current workflow + pain points  

### Documents Generated

#### 1. Process Documentation
```yaml
Sections:
  - Current workflow (as-is)
  - Pain points & bottlenecks
  - Desired workflow (to-be)
  - Automation opportunities
  - Tools/integrations needed
  - Step-by-step process
  - Roles & responsibilities
  - Approvals & guardrails
```

#### 2. Development Plan
```yaml
Sections:
  - Architecture (how automation runs)
  - Triggers & conditions
  - Error handling & alerts
  - Rollback procedures
  - Testing approach
  - Phase 1, 2, 3 implementation
```

#### 3. safety.md
```yaml
Sections:
  - Data handling (PII, sensitive info)
  - Access controls
  - Audit logging
  - Approval workflows (who approves what)
  - Disaster recovery
```

### Questionnaire

```
Q1: What process are you automating?
    "Customer onboarding workflow"

Q2: Current pain points?
    "Manual data entry, slow approvals, email ping-pong"

Q3: Tools you use?
    "Salesforce, HubSpot, Slack, Google Workspace"

Q4: Timeline?
    "4 weeks"

Q5: Who owns this?
    "Customer Success team"

[Generate]
```

---

## Project 4: Revenue Stream

**Time:** 1.5 hours  
**Best for:** Adding new revenue model  
**Input:** Product + business model idea  

### Documents Generated

#### 1. Monetization Strategy
```yaml
Sections:
  - Revenue model (SaaS, freemium, marketplace, etc.)
  - Target customer segment
  - Pricing philosophy
  - Pricing tiers (3-5 options)
  - Feature matrix
  - Annual / monthly breakdown
  - Revenue projections (year 1-3)
  - Competitive pricing analysis
  - Packaging strategy
```

#### 2. Pricing & Subscriptions
```yaml
Sections:
  - Free tier (if applicable)
    - Features included
    - Limits
  - Pro tier
    - Price point
    - Features
    - Target customer
  - Enterprise tier
    - Custom pricing factors
    - Included features
    - Support level
  - Upgrade paths
  - Churn mitigation
```

#### 3. Business Model Canvas
```yaml
Sections:
  - Key partnerships
  - Key activities
  - Value proposition
  - Customer relationships
  - Revenue streams (multiple)
  - Key resources
  - Cost structure
  - Customer segments
```

### Questionnaire

```
Q1: What's your product?
    "Analytics dashboard for e-commerce"

Q2: Current pricing?
    "Currently free/open source"

Q3: Target customer (paying)?
    "E-commerce stores doing $1M+ annual revenue"

Q4: What's the WTP (willingness to pay)?
    "$100-500/month"

Q5: Pricing model preference?
    "Usage-based + flat tier"

Q6: Expected revenue year 1?
    "$500K target"

[Generate]
```

---

## Project 5: Brand Marketing

**Time:** 2 hours  
**Best for:** Building brand identity from scratch  
**Input:** Product + company vision  

### Documents Generated

#### 1. Brand Guidelines
```yaml
Sections:
  - Brand story
  - Brand mission & values
  - Brand personality (5 attributes)
  - Brand voice (tone, style, language)
  - Visual identity specs
  - Logo usage guidelines
  - Color palette + guidelines
  - Typography
  - Photography style
  - Design principles
```

#### 2. Messaging Strategy
```yaml
Sections:
  - Key messaging pillars (3-4)
  - Tagline
  - Elevator pitch (20 seconds)
  - Value propositions (3 main)
  - Proof points / social proof
  - Brand narrative
```

#### 3. Positioning Statement
```yaml
Sections:
  - Target market
  - Market position
  - Key differentiators
  - Competitive landscape
  - Why us vs. competitors
  - Brand promise
```

#### 4. Brand Voice Guidelines
```yaml
Sections:
  - Vocabulary (words to use, avoid)
  - Tone examples
    - Formal communications
    - Social media
    - Customer support
    - Error messages
  - Grammar & style
  - Cultural sensitivity notes
```

### Questionnaire

```
Q1: Company/product name?
    "Acme Analytics"

Q2: What's your mission?
    "Democratize data analytics for small businesses"

Q3: Brand personality (3 words)?
    "Trustworthy, Simple, Empowering"

Q4: Target audience?
    "SMB founders, 25-45, non-technical"

Q5: Unique brand story?
    "Founded by founders who struggled with complex tools"

Q6: Visual style preference?
    "Modern, clean, approachable (think Stripe/Notion)"

[Generate]
```

---

## Project 6: Product Marketing

**Time:** 2.5 hours  
**Best for:** Go-to-market strategy  
**Input:** Product + market + timeline  

### Documents Generated

All of Project 5 (Brand) + 3 additional docs:

#### 4. ICPs & Personas
```yaml
Sections:
  - Ideal Customer Profile (ICP)
    - Company size
    - Industry
    - Annual revenue
    - Pain points
    - Goals
    - Budget
  - 3-5 buyer personas
    - Name, title, age
    - Goals & challenges
    - Decision-making process
    - Technology preferences
    - Success metrics they care about
```

#### 5. Competitive Landscape
```yaml
Sections:
  - Direct competitors (5-7)
  - Indirect competitors
  - Feature comparison matrix
  - Pricing comparison
  - Market gaps / opportunities
  - Our competitive advantage
  - How we win
  
[OPTIONAL: Research API call for data]
```

#### 6. Go-to-Market Plan
```yaml
Sections:
  - Launch timeline (4 weeks before to 8 weeks after)
  - Pre-launch activities
    - Content marketing
    - Partnerships
    - Beta signups
  - Launch week
    - Launch channels
    - PR strategy
    - Event/webinar
  - Post-launch (30-60-90 days)
    - Customer onboarding
    - Feedback loops
    - Optimization
  - Success metrics
  - Budget allocation
```

### Questionnaire

```
Q1: What's the product?
    "AI writing assistant for teams"

Q2: Launch date?
    "3 months from now"

Q3: Target market?
    "Agencies, 20-200 people"

Q4: Main competition?
    "Copy.ai, Jasper, ChatGPT"

Q5: Key differentiator?
    "Built for team collaboration, not individual"

Q6: Budget for launch?
    "$50K"

[Generate]
```

---

## Project 7: Custom Files Summarize

**Time:** 30 minutes  
**Best for:** Understanding existing materials  
**Input:** Upload/link documents  

### Documents Generated

#### 1. Executive Summary
```yaml
Sections:
  - What the documents are about
  - Key findings
  - Important decisions made
  - Recommendations
  - Next steps
```

#### 2. Extracted Specs
```yaml
Sections:
  - Key features mentioned
  - Timeline / dates
  - Budget figures
  - Team structure
  - Tech stack
  - Success metrics
```

#### 3. Gap Analysis
```yaml
Sections:
  - What's missing
  - Unclear requirements
  - Conflicting information
  - Areas needing clarification
```

### Input

```
User uploads/links:
  • Pitch deck
  • Competitor analysis
  • Market research PDF
  • Previous PRD
  • Founder notes
  
Docgen extracts + summarizes
```

---

## Project 8: Custom Context Project

**Time:** 1-2 hours (variable)  
**Best for:** Anything not covered above  
**Input:** User description + clarifying questions  

### Flow

```
User: "I need a technical architecture document 
       for distributed payment processing"

Docgen:
  Q1: Who's the audience? (team, external, investors?)
  Q2: Scope? (payments, identity, settlements?)
  Q3: Scale? (1000 tx/sec or 100?)
  Q4: Constraints? (regulations, latency, cost?)
  Q5: Existing systems? (custom or third-party?)
  
Docgen:
  → Generates technical architecture doc
  → Runs quality gates
  → Delivers
```

### Documents Generated

```
1. Custom specification (tailored to request)
2. Implementation guide
3. Testing strategy
4. Deployment plan (if applicable)
5. Maintenance guide
```

---

## Workflow Combinations

Users can pick 1 main project + 0-2 workflows:

**Example 1:** Fast Product MVP + Coding workflow
```
Docs: PRD, UX, specifiers
    + Development Plan
    + Frontend UI Requirements
    = 5 documents total
```

**Example 2:** Feature Release + Marketing workflow
```
Docs: PRD, UX, specifiers, safety
    + Messaging
    + Positioning
    + ICPs & Personas
    = 7 documents total
```

**Example 3:** Custom Documentation + Monetization workflow
```
Docs: Custom [whatever user describes]
    + Pricing & Subscriptions
    + Project Budgeting
    = 3-4 documents total
```

---

**All docs generated pass 5 exit gates before delivery.**
