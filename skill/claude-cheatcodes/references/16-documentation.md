# 16-documentation

READMEs, API docs, ADRs, runbooks, onboarding guides, changelogs, docstrings, technical writing.

24 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Write API Documentation

**id:** `16-documentation/api-docs` · **Difficulty:** intermediate · **Tags:** api, documentation, openapi, developer-experience

**Placeholders:** [DESCRIBE YOUR API], [THIRD-PARTY DEVELOPERS]

````text
Write comprehensive API documentation.

API: [DESCRIBE YOUR API]
Audience: [THIRD-PARTY DEVELOPERS]

1. **Overview**: what the API does in 2 sentences
2. **Authentication**: how to get and use API keys/tokens
3. **Base URL**: production and sandbox
4. **Request format**: content-type, encoding
5. **Response format**: envelope structure, status codes
6. **Rate limits**: limits + how to handle 429
7. **Errors**: complete error code reference with solutions
8. **Versioning**: current version, how to upgrade

For each endpoint:
9. Method + path
10. Description of what it does
11. Request parameters (path, query, body) with types and required/optional
12. Request body example (JSON)
13. Response body example
14. Error responses specific to this endpoint
15. Code examples in 3 languages (curl, JavaScript, Python)

Output: complete API documentation in Markdown.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Architecture Decision Records

**id:** `16-documentation/architecture-decision-records` · **Difficulty:** intermediate · **Tags:** adr, architecture, documentation, decisions

**Placeholders:** [JUSTIFICATION], [LIST KEY TECHNICAL DECISIONS YOUR TEAM HAS MADE], [OPTION], [POSITIVE OUTCOMES], [TRADEOFFS AND RISKS]

````text
Write Architecture Decision Records (ADRs) for my team.

Decisions to document: [LIST KEY TECHNICAL DECISIONS YOUR TEAM HAS MADE]

ADR format (Nygard style):
```markdown
# ADR-001: Use PostgreSQL as the Primary Database

Status: Accepted
Date: 2024-01-15
Deciders: Engineering team

## Context
[What is the issue that motivates this decision?]

## Decision Drivers
* [Driver 1]
* [Driver 2]

## Considered Options
* [Option A]
* [Option B]

## Decision Outcome
Chosen option: [OPTION]

Because: [JUSTIFICATION]

## Consequences
* Good: [POSITIVE OUTCOMES]
* Bad: [TRADEOFFS AND RISKS]

## Options Comparison
| Criteria | Option A | Option B |
```

Write ADRs for my decisions covering:
1. Database choice
2. API style (REST vs GraphQL)
3. Authentication method
4. Deployment platform
5. Testing strategy
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Document System Architecture

**id:** `16-documentation/architecture-docs` · **Difficulty:** advanced · **Tags:** architecture, documentation, diagrams, adr

**Placeholders:** [DESCRIBE YOUR SYSTEM]

````text
Document my system architecture.

System: [DESCRIBE YOUR SYSTEM]

1. **Architecture overview**: high-level description in plain English
2. **Diagram**: C4 model diagram (Context → Container → Component)
   - Context: how your system fits in the world
   - Container: main deployable units
   - Component: major components within each container
3. **Technology choices**: what and why for key decisions
4. **Data flow**: how data moves through the system
5. **Security architecture**: auth, network, data protection overview
6. **Scaling strategy**: how it handles growth
7. **Failure modes**: what happens when X fails
8. **External dependencies**: third-party services and their criticality

ADRs (Architecture Decision Records):
9. One ADR per significant decision
10. Format: Status, Context, Decision, Consequences

Output: architecture document + 3 example ADRs.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Better Changelogs

**id:** `16-documentation/changelog-writing` · **Difficulty:** beginner · **Tags:** changelog, documentation, releases, communication

**Placeholders:** [LIST YOUR CHANGES], [PASTE OR DESCRIBE]

````text
Write user-facing changelogs for my releases.

Current release notes/changelog: [PASTE OR DESCRIBE]
Changes in this release: [LIST YOUR CHANGES]

Changelog principles (Keep a Changelog):
1. **For humans, not computers**: don't paste git log
2. **Latest first**: newest version at top
3. **Types**: Added, Changed, Deprecated, Removed, Fixed, Security
4. **User perspective**: how does this change affect me?
5. **Link to issues/PRs**: for users who want details

Examples of good vs bad:
- Bad: 'Fix bug in user module'
- Good: 'Fixed an issue where saving your profile photo would fail for images larger than 10MB'

For each change in my release:
6. Categorize it correctly
7. Rewrite it from the user's perspective
8. Note any migration steps needed
9. Link relevant documentation

Output: formatted CHANGELOG.md section for my release.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Better Code Comments

**id:** `16-documentation/code-comments` · **Difficulty:** beginner · **Tags:** comments, documentation, code-quality, best-practices

**Placeholders:** [PASTE YOUR CODE]

````text
Improve code comments and documentation in my codebase.

Code: [PASTE YOUR CODE]

Comment principles:
1. **Why, not what**: code shows what, comments explain why
2. **Don't state the obvious**: `i++ // increment i` is useless
3. **Business context**: why this specific algorithm? Why this value?
4. **Gotchas**: warn about non-obvious behavior, performance implications
5. **TODO format**: `// TODO(username): description` with actionable notes

Docstring standards:
6. **JSDoc** (JavaScript): @param, @returns, @throws, @example
7. **Python docstrings**: Google style or NumPy style
8. **Class docs**: purpose, invariants, usage example
9. **Function docs**: what it does, params, return, side effects

For each function/class in my code:
- Remove misleading comments
- Add missing why-comments
- Add complete JSDoc/docstrings

Output: fully documented code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write a CONTRIBUTING Guide

**id:** `16-documentation/contributing-guide` · **Difficulty:** beginner · **Tags:** contributing, open-source, documentation, community

**Placeholders:** [DESCRIBE ANY FRICTION], [DESCRIBE YOUR PROJECT]

````text
Write a CONTRIBUTING.md guide for my open source project.

Project: [DESCRIBE YOUR PROJECT]
Current contributor experience: [DESCRIBE ANY FRICTION]

Sections to include:
1. **Code of Conduct**: link to your CODE_OF_CONDUCT.md
2. **Getting started**: fork → clone → install → run → first change
3. **Development environment**: prerequisites, setup commands
4. **Branch naming**: `feature/`, `fix/`, `docs/`
5. **Commit message format**: Conventional Commits
6. **Code style**: link to linting config, formatting rules
7. **Testing**: how to run tests, coverage requirements
8. **Pull request process**: what to expect after submitting
9. **Review process**: what we look for in review
10. **Issue reporting**: bug report template, feature request template
11. **Good first issues**: how to find starter issues
12. **Contact**: where to ask questions (Discord, forum)

Output: complete CONTRIBUTING.md.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create a Data Dictionary

**id:** `16-documentation/data-dictionary` · **Difficulty:** beginner · **Tags:** data-dictionary, documentation, database, data

**Placeholders:** [DATA ANALYSTS / ENGINEERS / PRODUCT MANAGERS], [DESCRIBE], [NAME]

````text
Create a comprehensive data dictionary.

Database/System: [DESCRIBE]
Audience: [DATA ANALYSTS / ENGINEERS / PRODUCT MANAGERS]

Data dictionary format:

**Table/Collection: [NAME]**
| Column | Type | Nullable | Description | Example | Notes |
|---|---|---|---|---|---|
| id | UUID | No | Unique identifier | `550e8400-...` | Auto-generated |
| created_at | TIMESTAMPTZ | No | When record was created | `2024-01-15T10:30:00Z` | UTC always |
| status | VARCHAR(20) | No | Current status | `active` | Enum: active, inactive, deleted |

**Relationships**: what this table connects to
**Business rules**: constraints beyond the schema
**Common queries**: typical access patterns
**Owner**: team that owns this data

Create data dictionary for all tables in my system.
Format as Markdown suitable for a team wiki.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Audit and Improve Existing Documentation

**id:** `16-documentation/documentation-audit` · **Difficulty:** intermediate · **Tags:** documentation, audit, improvement, quality

**Placeholders:** [DESCRIBE USER PAIN POINTS], [DESCRIBE YOUR DOCS / PASTE SAMPLE]

````text
Audit and improve my existing documentation.

Documentation to audit: [DESCRIBE YOUR DOCS / PASTE SAMPLE]
Complaints you've received: [DESCRIBE USER PAIN POINTS]

Audit dimensions:
1. **Accuracy**: is it still correct?
2. **Completeness**: are there obvious gaps?
3. **Discoverability**: can users find what they need?
4. **Clarity**: is it clear to the target audience?
5. **Examples**: are there enough concrete examples?
6. **Freshness**: when was it last updated?
7. **Structure**: logical flow and hierarchy?
8. **Search**: can users find via search?

For each piece of documentation:
9. Current state assessment
10. Specific improvements needed
11. Priority (critical/important/nice-to-have)

Improvements to make:
12. Add missing sections
13. Rewrite unclear explanations
14. Add code examples
15. Fix outdated information

Output: audit report + prioritized improvement list.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Documentation Site with Docusaurus

**id:** `16-documentation/docusaurus-docs-site` · **Difficulty:** intermediate · **Tags:** docusaurus, documentation, react, website

**Placeholders:** [DESCRIBE YOUR DOCS]

````text
Build a documentation website with Docusaurus.

Documentation to host: [DESCRIBE YOUR DOCS]

1. **Setup**: `npx create-docusaurus@latest my-docs classic --typescript`
2. **Configuration**: `docusaurus.config.ts` — navbar, footer, themes
3. **Content**: Markdown/MDX files in `docs/` folder
4. **Sidebar**: auto-generated or custom `sidebars.ts`
5. **Components**: MDX lets you embed React components in docs
6. **Versioning**: multiple doc versions for different releases
7. **Search**: Algolia DocSearch (free for open source)
8. **Blog**: built-in blog for release notes
9. **Custom theme**: extend Docusaurus theme for your brand
10. **Deployment**: GitHub Pages, Vercel, Netlify (one command)

Features to configure:
11. Dark mode toggle
12. i18n for multiple languages
13. OpenAPI plugin for API reference
14. Analytics: Plausible or Google Analytics

Output: complete Docusaurus site for my docs.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Engineering Blog Posts

**id:** `16-documentation/engineering-blog` · **Difficulty:** intermediate · **Tags:** blog, writing, engineering, communication

**Placeholders:** [DESCRIBE WHAT YOU BUILT OR LEARNED], [OTHER ENGINEERS], [WHAT'S THE MAIN TAKEAWAY]

````text
Write an engineering blog post about a technical topic.

Topic: [DESCRIBE WHAT YOU BUILT OR LEARNED]
Audience: [OTHER ENGINEERS]
Key insight: [WHAT'S THE MAIN TAKEAWAY]

Blog post structure:
1. **Title**: specific, benefit-driven, SEO-optimized
   - 'How We Reduced API Latency by 80% with Redis'
2. **Introduction hook**: the problem you faced (1 paragraph)
3. **The journey**: what you tried, what failed
4. **The solution**: the approach that worked (with code)
5. **Results**: metrics, before/after comparison
6. **Lessons learned**: what others can apply
7. **Conclusion**: summary + what's next

Blog writing tips:
8. Show real code, not pseudocode
9. Include diagrams for architecture explanations
10. Be specific: numbers, not 'much faster'
11. Mention what didn't work (more credible)
12. First draft rule: write fast, edit later

Output: complete blog post draft.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design an Interactive Tutorial

**id:** `16-documentation/interactive-tutorial` · **Difficulty:** intermediate · **Tags:** tutorial, learning, education, ux

**Placeholders:** [DESCRIBE WHAT YOU'RE TEACHING], [WHAT SHOULD THE USER BE ABLE TO DO AFTER COMPLETING]

````text
Design an interactive tutorial for my product or technology.

Learning goal: [WHAT SHOULD THE USER BE ABLE TO DO AFTER COMPLETING]
Technology: [DESCRIBE WHAT YOU'RE TEACHING]

Interactive tutorial design:
1. **Learning objectives**: specific, measurable goals
2. **Prerequisites**: what users need before starting
3. **Chapters**: 5-8 progressive chapters
4. **Each chapter**:
   - Concept explanation (minimal text)
   - Interactive example (user runs code or clicks through UI)
   - Challenge: user applies the concept
   - Feedback: immediate, specific feedback
5. **Progression**: each chapter builds on the last
6. **Aha moments**: design for 1 aha moment per chapter
7. **Completion certificate**: gamification element

Format options:
8. **In-browser coding**: like freeCodeCamp, Codecademy
9. **Guided tour**: Shepherd.js overlay on real app
10. **Sandbox environment**: live environment to experiment

Output: complete chapter outline + Chapter 1 design.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Internal Documentation System

**id:** `16-documentation/internal-docs` · **Difficulty:** intermediate · **Tags:** documentation, confluence, notion, wiki

**Placeholders:** [DESCRIBE: no docs / scattered docs / outdated docs]

````text
Set up an internal documentation system for my engineering team.

Team size: [N engineers]
Current state: [DESCRIBE: no docs / scattered docs / outdated docs]

Documentation system design:
1. **Tool selection**: Notion / Confluence / GitBook / docs-as-code (MDX)
   - Recommendation based on team size and existing tools
2. **Information architecture**: how to organize content
3. **Templates**: one template per document type
4. **Ownership**: every document has an owner
5. **Review cycle**: quarterly review → mark as stale or update

Essential docs to create first:
6. **Onboarding guide**: new engineer day 1-30
7. **Development setup**: how to run everything locally
8. **Architecture overview**: what we've built and why
9. **Runbooks**: common operational procedures
10. **On-call guide**: what to do when paged
11. **Decision log**: major technical decisions and rationale
12. **Team processes**: how we work (standups, PRs, deployments)

Output: documentation system setup guide.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Document TypeScript Code with JSDoc

**id:** `16-documentation/jsdoc-typescript-docs` · **Difficulty:** intermediate · **Tags:** jsdoc, typescript, documentation, api

**Placeholders:** [PASTE YOUR TYPESCRIPT CODE]

````text
Add comprehensive JSDoc documentation to my TypeScript code.

Code to document: [PASTE YOUR TYPESCRIPT CODE]

JSDoc patterns for TypeScript:
1. **Function documentation**:
```typescript
/**
 * Brief description of what the function does.
 *
 * @param userId - The unique identifier of the user
 * @param options - Configuration options
 * @returns The created user object
 * @throws {ValidationError} When userId is invalid
 * @example
 * ```typescript
 * const user = await getUser('user_123', { includeProfile: true });
 * ```
 */
```

2. **Interface documentation**: document each property
3. **Class documentation**: describe the class, constructor, public methods
4. **Type aliases**: document complex types
5. **Deprecated**: `@deprecated Use newFunction() instead`
6. **Internal**: `@internal` for non-public API

Generate docs:
7. TypeDoc: `typedoc --entryPoints src/index.ts`
8. Output: static HTML documentation site

Document all exported symbols in my code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Incident Postmortems

**id:** `16-documentation/postmortem-writing` · **Difficulty:** intermediate · **Tags:** postmortem, incident, documentation, reliability

**Placeholders:** [DESCRIBE HOW IT WAS RESOLVED], [DESCRIBE USER IMPACT AND DURATION], [DESCRIBE WHAT HAPPENED]

````text
Write a blameless postmortem for an incident.

Incident: [DESCRIBE WHAT HAPPENED]
Impact: [DESCRIBE USER IMPACT AND DURATION]
Resolution: [DESCRIBE HOW IT WAS RESOLVED]

Postmortem template:

**Summary** (2-3 sentences): what happened, impact, duration

**Timeline**:
- HH:MM - First alert / user report
- HH:MM - On-call engineer paged
- HH:MM - Root cause identified
- HH:MM - Fix deployed
- HH:MM - Incident resolved

**Root cause**: the actual technical reason (not just 'human error')

**Contributing factors**: what made the system fragile

**What went well**: things that helped us resolve faster

**What went wrong**: gaps in our system

**Action items** (specific, assigned, with due dates):
| Action | Owner | Due Date |

**Blameless principle**: focus on systems and processes, not individuals
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write a Perfect README

**id:** `16-documentation/readme-generator` · **Difficulty:** beginner · **Tags:** readme, documentation, open-source, markdown

**Placeholders:** [DESCRIBE YOUR PROJECT], [DEVELOPERS / END USERS / STUDENTS], [OPTIONAL]

````text
Write a perfect README for my project.

Project: [DESCRIBE YOUR PROJECT]
Audience: [DEVELOPERS / END USERS / STUDENTS]
GitHub URL: [OPTIONAL]

README sections:
1. **Header**: project name + tagline + badges (build, coverage, license)
2. **Demo**: GIF or screenshot first (show, don't just tell)
3. **Features**: bullet list of key capabilities
4. **Quick Start**: get running in < 5 commands
5. **Installation**: full prerequisites + step-by-step
6. **Usage**: common use cases with code examples
7. **Configuration**: environment variables table
8. **API Reference**: if applicable, key interfaces
9. **Contributing**: how to submit PRs
10. **License**: license type and brief statement

Style:
- Active voice, present tense
- Code blocks for all commands
- Consistent heading hierarchy
- No jargon without explanation

Output: complete README.md ready to publish.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Operations Runbooks

**id:** `16-documentation/runbook-writing` · **Difficulty:** intermediate · **Tags:** runbooks, documentation, operations, sre

**Placeholders:** [DATE], [DESCRIBE YOUR SERVICE], [ESTIMATE], [LIST COMMON OPERATIONAL TASKS], [NAME], [OTHER REQUIREMENTS], [SYSTEM], [WHAT SUCCESS LOOKS LIKE]

````text
Write operations runbooks for common tasks.

Service: [DESCRIBE YOUR SERVICE]
Runbooks needed: [LIST COMMON OPERATIONAL TASKS]

Runbook template:

**Title**: [Action-oriented: 'Restart the API server']
**Audience**: On-call engineer
**Time required**: [ESTIMATE]
**Risk level**: Low/Medium/High

**Context**: Why would you need to run this?

**Prerequisites**:
- Access to [SYSTEM]
- [OTHER REQUIREMENTS]

**Steps**:
1. [Specific command or action]
   `$ command here`
   Expected output: [WHAT SUCCESS LOOKS LIKE]

**Verification**: How to confirm success

**Rollback**: How to undo this if needed

**Escalation**: When to escalate and to whom

**Last updated**: [DATE] by [NAME]

Write runbooks for:
1. Restart a service
2. Scale up/down
3. Roll back a deployment
4. Database failover
5. Clear a stuck job queue
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Document UI Components with Storybook

**id:** `16-documentation/storybook-docs` · **Difficulty:** intermediate · **Tags:** storybook, documentation, components, react

**Placeholders:** [LIST YOUR COMPONENTS]

````text
Document my UI components with Storybook.

Components to document: [LIST YOUR COMPONENTS]
Framework: React + TypeScript

1. **Story file structure**: `ComponentName.stories.tsx`
2. **Default export**: meta with title, component, argTypes
3. **Named stories**: each significant state of the component
4. **Args**: control props from Storybook UI
5. **Play function**: interactive stories with user actions
6. **MDX docs**: rich documentation mixing prose + stories

For each component document:
7. Primary story: default/normal use
8. Variants: all different appearances
9. States: loading, error, empty, disabled
10. Size variants: small, medium, large
11. Dark mode: how it looks in dark
12. Mobile: responsive behavior

Storybook addons:
13. Accessibility: a11y panel
14. Viewport: test different screen sizes
15. Background: test on different backgrounds

Output: story files for all my components.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write a Complete OpenAPI Specification

**id:** `16-documentation/swagger-openapi-spec` · **Difficulty:** intermediate · **Tags:** openapi, swagger, api, documentation

**Placeholders:** [DESCRIBE YOUR API], [DETAILED DESCRIPTION], [EACH ENDPOINT], [OPERATIONS], [REUSABLE RESPONSES], [REUSABLE SCHEMAS]

````text
Write a complete OpenAPI 3.1 specification.

API to document: [DESCRIBE YOUR API]

Complete OpenAPI structure:
```yaml
openapi: 3.1.0
info:
  title: My API
  version: 2.0.0
  description: |
    [DETAILED DESCRIPTION]
  contact:
    email: api@example.com
  license:
    name: MIT

servers:
  - url: https://api.example.com/v2
    description: Production
  - url: https://sandbox.api.example.com/v2
    description: Sandbox

security:
  - BearerAuth: []

components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
  schemas:
    [REUSABLE SCHEMAS]
  responses:
    [REUSABLE RESPONSES]

paths:
  /[EACH ENDPOINT]:
    [OPERATIONS]
```

Include:
- All endpoints with full schemas
- 3+ examples per endpoint
- All error responses
- Authentication documentation
- Webhook definitions
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Swagger UI for API Docs

**id:** `16-documentation/swagger-ui-setup` · **Difficulty:** intermediate · **Tags:** swagger, openapi, documentation, api

**Placeholders:** [DESCRIBE YOUR EXPRESS/FASTAPI/OTHER API]

````text
Set up interactive API documentation with Swagger UI.

API: [DESCRIBE YOUR EXPRESS/FASTAPI/OTHER API]

**Option A — Express.js**:
1. Install: `swagger-jsdoc`, `swagger-ui-express`
2. JSDoc annotations on each route:
```javascript
/**
 * @swagger
 * /users/{id}:
 *   get:
 *     summary: Get user by ID
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: User object
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/User'
 */
```
3. Serve UI at `/api-docs`

**Option B — Separate OpenAPI file**:
4. Write `openapi.yaml` manually or generate
5. Serve with Swagger UI standalone

**Best practices**:
6. Examples for every request/response
7. Error responses documented
8. Authentication setup in the UI
9. Protect docs endpoint in production

Output: complete Swagger UI setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Technical Documentation

**id:** `16-documentation/technical-writing` · **Difficulty:** intermediate · **Tags:** technical-writing, docs, guides, markdown

**Placeholders:** [DESCRIBE SKILL LEVEL AND BACKGROUND], [DESCRIBE WHAT YOU'RE DOCUMENTING]

````text
Write clear technical documentation.

Topic: [DESCRIBE WHAT YOU'RE DOCUMENTING]
Audience: [DESCRIBE SKILL LEVEL AND BACKGROUND]

Technical writing principles:
1. **Know your audience**: adjust depth for their expertise
2. **Progressive disclosure**: overview → quick start → deep dive
3. **Consistent structure**: same pattern throughout
4. **Active voice**: 'Click the button' not 'The button should be clicked'
5. **Plain language**: short sentences, common words
6. **Show, don't tell**: screenshots, code examples, demos
7. **Scannable**: headers, bullets, tables, bold key terms
8. **Accurate**: test every instruction before publishing
9. **Versioned**: note which version this applies to
10. **Feedback loop**: 'Was this helpful?' at the bottom

Document types to write:
11. **Tutorial**: teaching-oriented, step by step
12. **How-to guide**: task-oriented, solve a specific problem
13. **Reference**: information-oriented, complete specification
14. **Explanation**: understanding-oriented, why it works this way

Output: complete documentation for my topic.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write a User Guide

**id:** `16-documentation/user-guide` · **Difficulty:** beginner · **Tags:** user-guide, documentation, end-users, help

**Placeholders:** [DESCRIBE WHAT YOUR PRODUCT DOES], [DESCRIBE YOUR TYPICAL USER'S TECHNICAL LEVEL]

````text
Write a comprehensive user guide for my product.

Product: [DESCRIBE WHAT YOUR PRODUCT DOES]
Users: [DESCRIBE YOUR TYPICAL USER'S TECHNICAL LEVEL]

User guide structure:
1. **Introduction**: what this product does and who it's for
2. **Getting started**: set up + first action in 5 steps
3. **Core concepts**: key terms and concepts explained
4. **Feature guides**: one section per major feature
   - What it does
   - When to use it
   - Step-by-step instructions with screenshots
   - Common questions
5. **Troubleshooting**: top 10 issues + solutions
6. **FAQ**: answers to frequently asked questions
7. **Glossary**: define product-specific terms
8. **Index**: searchable list of topics

Writing style:
- Second person ('you')
- Numbered steps for procedures
- Screenshots for complex UI steps
- Warning boxes for destructive actions

Output: complete user guide.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Plan Video Tutorial Content

**id:** `16-documentation/video-tutorials` · **Difficulty:** beginner · **Tags:** tutorials, videos, education, documentation

**Placeholders:** [DESCRIBE WHAT YOU'RE TEACHING], [SHORT CLIPS / SERIES / LIVE CODING], [SKILL LEVEL]

````text
Plan and script a video tutorial series.

Topic: [DESCRIBE WHAT YOU'RE TEACHING]
Audience: [SKILL LEVEL]
Format: [SHORT CLIPS / SERIES / LIVE CODING]

Video series structure:
1. **Hook**: what will they learn? (30 seconds)
2. **Episode outline**: topics in learning order
3. **Prerequisites**: what viewers need to know first
4. **Duration**: 8-15 minutes per episode (ideal for retention)

Script template:
5. **Introduction**: topic + motivation + what they'll build
6. **Demo first**: show the finished thing before explaining
7. **Explanation**: the concept with simple analogies
8. **Live coding**: build it step by step
9. **Common mistakes**: what to watch out for
10. **Summary**: 3 key takeaways
11. **Call to action**: what to try next

For my topic:
- Episode list
- Detailed outline for Episode 1
- Script for Episode 1's introduction
- Exercise: what viewers build after watching
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Generate a complete [DOC_TYPE] for [SUBJECT]

**id:** `16-documentation/generate-a-complete-doc-type-for-subject` · **Difficulty:** beginner/intermediate/advanced · **Tags:** documentation, best-practices, architecture, writing, openapi, contributing, database, engineer, incident

**Variant group** (14 generated prompts collapsed). Pick one value per placeholder:
- `[DOC_TYPE]`: Architecture Decision Records (ADRs) | OpenAPI Swagger specifications | contributing guides | database schema dictionaries | engineer onboarding guides | incident operations runbooks
- `[SUBJECT]`: a database migrations pipeline | a frontend monorepo codebase | a global payment API | a multi-service microservices network | an OAuth2 user signin portal
- `[DOC_SECTION]`: Markdown formatting structures | interactive API mock schemas | reproduction steps guides | troubleshooting FAQ sections

````text
Generate a fully populated [DOC_TYPE] document detailing the architecture, schema, or process for [SUBJECT]. Include [DOC_SECTION].
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** generate-a-complete-architecture-decision-records-adrs-for-a-database-migrations-pipeline, generate-a-complete-architecture-decision-records-adrs-for-a-frontend-monorepo-codebase, generate-a-complete-architecture-decision-records-adrs-for-an-oauth2-user-signin-portal, generate-a-complete-contributing-guides-for-a-database-migrations-pipeline, generate-a-complete-contributing-guides-for-an-oauth2-user-signin-portal, generate-a-complete-database-schema-dictionaries-for-a-database-migrations-pipeline, generate-a-complete-database-schema-dictionaries-for-a-frontend-monorepo-codebase, generate-a-complete-database-schema-dictionaries-for-an-oauth2-user-signin-portal, generate-a-complete-engineer-onboarding-guides-for-a-database-migrations-pipeline, generate-a-complete-engineer-onboarding-guides-for-a-multi-service-microservices-network, generate-a-complete-incident-operations-runbooks-for-a-global-payment-api, generate-a-complete-openapi-swagger-specifications-for-a-frontend-monorepo-codebase, generate-a-complete-openapi-swagger-specifications-for-a-global-payment-api, generate-a-complete-openapi-swagger-specifications-for-a-multi-service-microservices-network


## Write documentation for [SUBJECT] using [DOC_TYPE]

**id:** `16-documentation/write-documentation-for-subject-using-doc-type` · **Difficulty:** beginner/intermediate/advanced · **Tags:** contributing, documentation, best-practices, writing, openapi, engineer, incident, architecture

**Variant group** (14 generated prompts collapsed). Pick one value per placeholder:
- `[DOC_TYPE]`: Architecture Decision Records (ADRs) | OpenAPI Swagger specifications | contributing guides | engineer onboarding guides | incident operations runbooks
- `[SUBJECT]`: a database migrations pipeline | a frontend monorepo codebase | a global payment API | a multi-service microservices network | an OAuth2 user signin portal
- `[DOC_SECTION]`: Markdown formatting structures | interactive API mock schemas | reproduction steps guides | troubleshooting FAQ sections

````text
Write professional documentation for [SUBJECT] using [DOC_TYPE]. Ensure the output contains [DOC_SECTION].
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** write-documentation-for-a-database-migrations-pipeline-using-contributing-guides, write-documentation-for-a-database-migrations-pipeline-using-engineer-onboarding-guides, write-documentation-for-a-database-migrations-pipeline-using-incident-operations-runbooks, write-documentation-for-a-database-migrations-pipeline-using-openapi-swagger-specifications, write-documentation-for-a-frontend-monorepo-codebase-using-architecture-decision-records-adrs, write-documentation-for-a-frontend-monorepo-codebase-using-openapi-swagger-specifications, write-documentation-for-a-global-payment-api-using-contributing-guides, write-documentation-for-a-global-payment-api-using-incident-operations-runbooks, write-documentation-for-a-multi-service-microservices-network-using-architecture-decision-records-adrs, write-documentation-for-a-multi-service-microservices-network-using-contributing-guides, write-documentation-for-a-multi-service-microservices-network-using-incident-operations-runbooks, write-documentation-for-a-multi-service-microservices-network-using-openapi-swagger-specifications, write-documentation-for-an-oauth2-user-signin-portal-using-architecture-decision-records-adrs, write-documentation-for-an-oauth2-user-signin-portal-using-engineer-onboarding-guides

