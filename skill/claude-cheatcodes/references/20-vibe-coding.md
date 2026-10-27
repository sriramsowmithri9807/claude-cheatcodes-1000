# 20-vibe-coding

Ship fast: MVPs, prototypes, automations, weekend projects, launch checklists, AI-assisted workflows.

22 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Build an AI-Powered App Quickly

**id:** `20-vibe-coding/ai-powered-app` · **Difficulty:** intermediate · **Tags:** ai, vibe-coding, claude, quick-build

**Placeholders:** [DESCRIBE YOUR APP IDEA], [DESCRIBE: text generation, analysis, classification, etc.], [WHO WILL USE THIS]

````text
Help me build an AI-powered app quickly.

App idea: [DESCRIBE YOUR APP IDEA]
AI functionality needed: [DESCRIBE: text generation, analysis, classification, etc.]
Target users: [WHO WILL USE THIS]

Quick build approach:

1. **Tech stack** (for speed):
   - Frontend: Next.js (pages router, fastest to get running)
   - AI: Claude API (Anthropic)
   - Styling: Tailwind CSS
   - Deploy: Vercel (git push → live)
2. **App structure**:
   - One main page
   - Input form
   - AI call with streaming
   - Output display
3. **Claude integration**:
   - API route: /api/generate
   - System prompt for your use case
   - Streaming response to frontend
4. **Minimum lovable UI**:
   - Clean, centered layout
   - Loading state (stream the text)
   - Copy button for output
5. **Ship**:
   - Deploy to Vercel
   - Share with 10 people

Output: complete app code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Turn an Idea into a Spec

**id:** `20-vibe-coding/app-from-idea` · **Difficulty:** beginner · **Tags:** planning, vibe-coding, spec, product

**Placeholders:** [APP NAME], [DO WHAT], [HOW], [WHO]

````text
Turn my app idea into a buildable spec.

Idea: [DESCRIBE YOUR IDEA — even rough is fine]

Let me refine this idea into a clear spec:

**1. Problem statement** (refined):
Who has this problem? How often? How bad?

**2. Solution** (one sentence):
[APP NAME] helps [WHO] to [DO WHAT] by [HOW].

**3. Core features** (MVP only — 3-5 max):
- Feature 1: [description]
- Feature 2: [description]
- Feature 3: [description]

**4. User flow**:
How does a new user go from landing page → registered → first value?

**5. Data model**:
Key entities and their relationships.

**6. Tech stack**:
What to build with (for speed + your skills).

**7. MVP timeline**:
Realistic estimate in days.

**8. What's out of scope** (important!):
What to build in v2, not now.

**9. First step**:
Exact first thing to code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write an Automation Script

**id:** `20-vibe-coding/automation-script` · **Difficulty:** beginner · **Tags:** automation, scripting, productivity, python

**Placeholders:** [DESCRIBE WHAT YOU DO MANUALLY], [HOW LONG IT TAKES MANUALLY], [HOW OFTEN YOU DO IT]

````text
Write an automation script to save me time.

Task to automate: [DESCRIBE WHAT YOU DO MANUALLY]
Current time cost: [HOW LONG IT TAKES MANUALLY]
Frequency: [HOW OFTEN YOU DO IT]

Automation approach:
1. Break down the manual steps
2. Identify the technical approach for each step
3. Write the script
4. Test with a small example first
5. Add error handling
6. Schedule it (cron, GitHub Actions, etc.)

Common automation categories:
- **File processing**: rename, move, convert files
- **Web scraping**: extract data from websites
- **API integration**: connect two services
- **Email/Slack**: send notifications or reports
- **Data transformation**: CSV → database, API → spreadsheet
- **Deployment**: automate repetitive dev tasks

Preferred language: Python (most automation libraries, readable)

Output: complete script that I can run immediately + cron expression if it should be scheduled.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Portfolio-Worthy Project

**id:** `20-vibe-coding/build-portfolio-project` · **Difficulty:** intermediate · **Tags:** portfolio, project, career, vibe-coding

**Placeholders:** [AI SUGGESTS SPECIFIC PROJECT], [DESCRIBE: frontend developer, full-stack, etc.], [LIST], [WEEKS], [WHAT TO EMPHASIZE IN INTERVIEWS]

````text
Help me build a portfolio-worthy project.

Target job: [DESCRIBE: frontend developer, full-stack, etc.]
Current skills: [LIST]
Time available: [WEEKS]

Portfolio project criteria:
1. **Solves a real problem**: not another todo app
2. **End-to-end**: frontend + backend + deployed
3. **Technical depth**: at least 2-3 interesting technical challenges
4. **Good code**: readable, typed, tested
5. **Good README**: explains the project and your decisions

Project idea for my target role:
[AI SUGGESTS SPECIFIC PROJECT]

Features to include:
- Core features: [LIST]
- Technical highlights: [WHAT TO EMPHASIZE IN INTERVIEWS]

What to avoid:
- Copying tutorials exactly
- Too simple (no technical challenge)
- Too complex (never finish)

GitHub presentation:
- README with: what, why, how, demo link, setup instructions
- Live demo on Vercel/Railway
- Clean commit history

Output: project spec + implementation plan.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a SaaS Product from Scratch

**id:** `20-vibe-coding/build-saas` · **Difficulty:** advanced · **Tags:** saas, product, vibe-coding, monetization

**Placeholders:** [DESCRIBE WHAT THE SAAS DOES], [DESCRIBE WHO PAYS FOR IT], [ESTIMATE WHAT YOU COULD CHARGE]

````text
Help me build a SaaS product from scratch.

SaaS idea: [DESCRIBE WHAT THE SAAS DOES]
Target customer: [DESCRIBE WHO PAYS FOR IT]
Pricing idea: [ESTIMATE WHAT YOU COULD CHARGE]

SaaS foundation to build first:

**Week 1 — Core product**:
1. The one feature that provides the value
2. Make it work well enough to demo

**Week 2 — Auth + user management**:
3. Sign up, login, forgot password
4. User dashboard

**Week 3 — Payments**:
5. Stripe Checkout integration
6. Subscription management
7. Free trial flow

**Week 4 — Polish + launch**:
8. Landing page with pricing
9. Onboarding flow
10. Email notifications (welcome, failed payment)

**Tech stack for speed**:
- Next.js + TypeScript
- Supabase (auth + database)
- Stripe (payments)
- Resend (email)
- Vercel (deployment)
- Posthog (analytics)

Output: tech architecture + implementation plan + starter code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Clone an Existing App to Learn

**id:** `20-vibe-coding/clone-this-app` · **Difficulty:** intermediate · **Tags:** clone, learning, vibe-coding, project

**Placeholders:** [APP NAME], [APP], [DESCRIBE YOUR EXPERIENCE], [LEARNING / PORTFOLIO / STARTING POINT FOR MY IDEA]

````text
Help me clone [APP NAME] to learn from it.

App to clone: [e.g., Twitter, Trello, Notion, Airbnb, etc.]
Purpose: [LEARNING / PORTFOLIO / STARTING POINT FOR MY IDEA]
Skill level: [DESCRIBE YOUR EXPERIENCE]

Cloning strategy:

1. **Scope**: which features to clone (not everything)
   - Core loop: the 2-3 features that define the app
   - Skip: social features, search, notifications (add later)

2. **Design**: don't copy — make it yours
   - Different color palette
   - Your name + branding
   - One twist: one feature your version has that theirs doesn't

3. **Tech stack**: choose for learning, not production scale
   - Next.js + Prisma + PostgreSQL + Tailwind
   - Auth: Clerk (2 lines of code)

4. **Build order**:
   - Data model first
   - Backend API second
   - UI third
   - Auth last (so auth doesn't block learning core features)

Output: feature list + data model + implementation plan for [APP].
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Get Your Code Reviewed by AI

**id:** `20-vibe-coding/code-review-ai` · **Difficulty:** beginner · **Tags:** code-review, ai, claude, quality

**Placeholders:** [LANGUAGE], [PASTE YOUR CODE]

````text
Get a comprehensive AI code review.

Code to review:
```[LANGUAGE]
[PASTE YOUR CODE]
```

Review my code from these perspectives:

1. **Does it work?**
   - Logic errors
   - Edge cases not handled
   - Missing error handling

2. **Is it secure?**
   - Input validation
   - Authentication/authorization
   - Data exposure

3. **Is it performant?**
   - Unnecessary loops or computations
   - Database query efficiency
   - Memory usage

4. **Is it readable?**
   - Variable/function naming
   - Code complexity
   - Comments where needed

5. **Can it be simplified?**
   - Duplicate code
   - Overcomplicated solutions
   - Modern language features not used

6. **Will it scale?**
   - Bottlenecks at 10x scale
   - Design limitations

For each issue: severity + specific fix + explanation of why.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Daily Coding Habit

**id:** `20-vibe-coding/daily-coding-habit` · **Difficulty:** beginner · **Tags:** habits, learning, productivity, consistency

**Placeholders:** [DESCRIBE: learn to code, improve skills, build projects], [MINUTES PER DAY]

````text
Help me build a consistent daily coding habit.

Goal: [DESCRIBE: learn to code, improve skills, build projects]
Available time: [MINUTES PER DAY]
Current streak: [0 / SOME / USED TO HAVE ONE]

Habit building strategy:

1. **Start tiny**: 20 minutes is enough to maintain momentum
2. **Same time every day**: attach to existing habit (after coffee, before bed)
3. **Lower the barrier**: have your editor already open

Daily coding structure:
4. **Warmup** (5 min): review yesterday's code
5. **Learn** (10 min): one new concept or one LeetCode problem
6. **Build** (remaining time): your current project
7. **Commit**: always end with a git commit

Tracking:
8. GitHub contribution graph: visual streak tracker
9. Coding journal: 2 sentences daily (what I did, what I'll do next)
10. Weekly review: what did I learn this week?

When you miss a day:
11. Never miss twice in a row
12. Return at any time (even 5 minutes)
13. Shame-free restart

Output: personalized habit plan for my schedule.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Use Claude as Your Pair Programmer

**id:** `20-vibe-coding/debug-with-claude` · **Difficulty:** beginner · **Tags:** claude, pair-programming, vibe-coding, debugging

**Placeholders:** [CODE], [DESCRIBE WHAT YOU'RE BUILDING OR STUCK ON], [ERROR], [FEATURE], [PROJECT], [STACK]

````text
Use Claude effectively as your AI pair programmer.

Current coding challenge: [DESCRIBE WHAT YOU'RE BUILDING OR STUCK ON]

Best prompts for different situations:

**When starting a feature**:
'I'm building [FEATURE] in [STACK]. What's the best approach? Show me the implementation.'

**When stuck on a bug**:
'Here's my code: [CODE]. Here's the error: [ERROR]. What's wrong and how do I fix it?'

**When you want a code review**:
'Review this code for bugs, performance, and best practices: [CODE]'

**When you need to understand code**:
'Explain this code line by line: [CODE]'

**When building step by step**:
'I'm building [PROJECT]. So far I have: [CODE]. Next I need to add [FEATURE]. How?'

**Tips for better results with Claude**:
1. Share ALL relevant context (stack, framework versions, constraints)
2. Share the actual error message (not 'it doesn't work')
3. Tell Claude what you've already tried
4. Ask for explanations, not just code
5. Iterate: 'That worked but now I have this problem...'

Apply to my current challenge.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deploy Your App Today

**id:** `20-vibe-coding/deploy-today` · **Difficulty:** beginner · **Tags:** deployment, vibe-coding, launch, hosting

**Placeholders:** [DESCRIBE YOUR APP AND TECH STACK], [FREE / SMALL BUDGET], [RUNS LOCALLY / MOSTLY DONE / NEEDS CLEANUP]

````text
Help me deploy my app today.

App: [DESCRIBE YOUR APP AND TECH STACK]
Current state: [RUNS LOCALLY / MOSTLY DONE / NEEDS CLEANUP]
Budget: [FREE / SMALL BUDGET]

Fastest deployment paths:

**Frontend** (React/Next.js/Vue):
1. Vercel: `vercel --prod` (literally 1 command)
2. Netlify: drag and drop build folder
3. Cloudflare Pages: free + fast CDN

**Backend** (Node.js/Python):
4. Railway: `railway up` (easiest)
5. Render: free tier, auto-deploy from GitHub
6. Fly.io: Docker-based, great free tier

**Database**:
7. Supabase: PostgreSQL free tier
8. PlanetScale: MySQL serverless free tier
9. Neon: PostgreSQL serverless free

**Full-stack**:
10. Railway: deploy frontend + backend + database together
11. Vercel: frontend + serverless functions + Neon PostgreSQL

For my stack:
- Specific platform recommendation
- Step-by-step deployment commands
- Environment variables to set
- First URL to test after deploy

Deploy before you sleep tonight.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Feature Fast

**id:** `20-vibe-coding/feature-builder` · **Difficulty:** intermediate · **Tags:** feature, vibe-coding, productivity, coding

**Placeholders:** [DESCRIBE THE FEATURE], [DESCRIBE YOUR CURRENT APP AND STACK], [HOW CRITICAL IS THIS]

````text
Help me build this feature quickly.

Existing app: [DESCRIBE YOUR CURRENT APP AND STACK]
Feature to add: [DESCRIBE THE FEATURE]
Priority: [HOW CRITICAL IS THIS]

Fast feature development approach:

1. **Clarify requirements** (15 min):
   - What is the minimum version of this feature?
   - What are the edge cases I can defer?
   - What existing code can I reuse?

2. **Plan the changes** (15 min):
   - Files to create
   - Files to modify
   - API changes needed
   - Database changes (if any)

3. **Build** (focus mode):
   - Database/schema first
   - API/backend second
   - UI third
   - Tests last (or in parallel)

4. **Ship fast**:
   - Feature flag: hide from users until ready
   - Deploy to staging first
   - Quick smoke test
   - Deploy to production

Output: implementation plan + the code for this specific feature.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Launch Your App with Confidence

**id:** `20-vibe-coding/launch-checklist` · **Difficulty:** intermediate · **Tags:** launch, checklist, vibe-coding, production

**Placeholders:** [DATE], [DESCRIBE YOUR APP AND STACK]

````text
Launch my app with confidence.

App: [DESCRIBE YOUR APP AND STACK]
Launch target: [DATE]

Pre-launch checklist:

**Technical**:
□ All critical user paths tested manually
□ No console errors in production
□ Mobile responsive (tested on real device)
□ Fast enough (< 3s load time)
□ SSL certificate active
□ Environment variables set correctly
□ Database backed up
□ Error monitoring (Sentry) configured
□ Analytics (PostHog/Plausible) installed
□ Deployment pipeline works
□ Domain connected

**User experience**:
□ Sign up and first action works
□ Error messages are friendly, not technical
□ Loading states on all async actions
□ Empty states are helpful
□ 404 page is friendly

**Business**:
□ Pricing page (if monetized)
□ Terms of service and privacy policy
□ Contact email works
□ Social media handles claimed

**Launch**:
□ Product Hunt draft ready
□ Twitter/X post drafted
□ Personal network notified
□ Relevant communities identified

For my specific app: which items need attention.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Make Your App Look Beautiful

**id:** `20-vibe-coding/make-it-beautiful` · **Difficulty:** beginner · **Tags:** design, ui, vibe-coding, css

**Placeholders:** [DESCRIBE: ugly bootstrap, default browser styles, etc.], [DESCRIBE]

````text
Help me make my app look beautiful.

App type: [DESCRIBE]
Current state: [DESCRIBE: ugly bootstrap, default browser styles, etc.]
Time to polish: [1 HOUR / HALF DAY / FULL DAY]

Quickest path to beautiful:

**If you have 1 hour**:
1. Add shadcn/ui: instant professional components
2. Pick a neutral font: Inter from Google Fonts
3. Fix spacing: consistent padding (p-4, p-8)
4. Fix colors: one primary color, use gray scale for rest
5. Add subtle hover effects

**If you have half a day**:
6. Design system: CSS variables for colors, spacing, fonts
7. Dark mode: it's expected, not optional
8. Responsive: looks good on mobile
9. Loading states: skeleton screens
10. Smooth transitions: 200ms for all interactive elements

**If you have a full day**:
11. Custom illustrations with Figma or AI-generated
12. Micro-animations with Framer Motion
13. 3D elements with Three.js or Spline
14. Gradient backgrounds and glassmorphism cards

For my app: 5 specific improvements to make right now.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Monetize Your App

**id:** `20-vibe-coding/monetize-app` · **Difficulty:** intermediate · **Tags:** monetization, saas, stripe, vibe-coding

**Placeholders:** [DESCRIBE WHAT VALUE IT PROVIDES], [DESCRIBE], [NUMBER AND TYPE OF USERS]

````text
Help me monetize my app.

App: [DESCRIBE]
Current users: [NUMBER AND TYPE OF USERS]
Value delivered: [DESCRIBE WHAT VALUE IT PROVIDES]

Monetization options:

**Subscriptions** (best for SaaS):
1. Free tier: limited features/usage
2. Pro: $X/month for full access
3. Team: $X/user/month
4. Enterprise: annual contract

**One-time payment**:
5. Lifetime access deal
6. Pay-per-use credits

**Freemium ladder**:
7. Free: enough to get hooked
8. Paid: more of what they love

**Pricing strategies**:
9. Value-based: what is it worth to them?
10. Competitor anchoring: vs alternatives
11. Per-seat: grows with their team

**Implementation** (Stripe):
12. Stripe Checkout: 15 minutes to live payments
13. Stripe Customer Portal: self-service subscription management
14. Webhooks: `customer.subscription.deleted` → downgrade

For my app:
- Which model fits best
- Suggested pricing tiers
- Stripe implementation code
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Ship an MVP in a Weekend

**id:** `20-vibe-coding/mvp-builder` · **Difficulty:** beginner · **Tags:** mvp, vibe-coding, quick-build, launch

**Placeholders:** [DESCRIBE YOUR IDEA IN 1-2 SENTENCES], [LIST YOUR SKILLS], [WHO HAS THIS PROBLEM AND HOW BADLY]

````text
Help me ship an MVP in a weekend.

Idea: [DESCRIBE YOUR IDEA IN 1-2 SENTENCES]
Problem it solves: [WHO HAS THIS PROBLEM AND HOW BADLY]
Technology I know: [LIST YOUR SKILLS]

Weekend MVP plan:

**Saturday morning** (planning):
1. Define the one core feature that proves the idea
2. Design the simplest possible UX (pen and paper)
3. Choose the fastest tech stack for me

**Saturday afternoon + evening** (build core):
4. Set up project structure
5. Build the core feature ONLY
6. Make it work end-to-end (ugly is fine)

**Sunday morning** (polish enough to ship):
7. Make it look presentable (not perfect)
8. Handle the main error cases
9. Deploy it

**Sunday afternoon** (share):
10. Write a landing page or Product Hunt post
11. Share in relevant communities
12. Get the first 5 users

Strict rules:
- No perfectionism
- No features not in the core loop
- Ship before Sunday midnight
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Without Writing Code

**id:** `20-vibe-coding/no-code-low-code` · **Difficulty:** beginner · **Tags:** no-code, low-code, tools, vibe-coding

**Placeholders:** [DESCRIBE YOUR IDEA], [FREE / SOME BUDGET], [NO CODE EXPERIENCE / BASIC HTML / SOME PROGRAMMING]

````text
Help me decide what to build without (or with minimal) code.

What I want to build: [DESCRIBE YOUR IDEA]
My technical level: [NO CODE EXPERIENCE / BASIC HTML / SOME PROGRAMMING]
Budget: [FREE / SOME BUDGET]

No-code/low-code tool recommendations:

**Website/Landing page**:
- Webflow: design-focused, most flexible
- Framer: motion-heavy, modern
- Squarespace: simple, all-in-one

**Web app**:
- Bubble.io: complex apps without code
- Glide: apps from spreadsheets
- Softr: apps from Airtable

**Internal tools**:
- Retool: dashboards and admin panels
- AppSmith: open-source Retool
- Forest Admin: instant admin for existing DB

**Automation**:
- Zapier / Make: connect any two apps
- n8n: self-hosted automation (free)

**Database + Backend**:
- Airtable: spreadsheet + database hybrid
- Supabase: Firebase alternative
- PocketBase: single file backend

For MY idea: which tool(s) to use + how to connect them.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Rapid Prototype

**id:** `20-vibe-coding/rapid-prototyping` · **Difficulty:** beginner · **Tags:** prototype, vibe-coding, validation, mvp

**Placeholders:** [DESCRIBE WHAT YOU WANT TO TEST], [WHAT ASSUMPTION ARE YOU TESTING], [WHO WILL YOU SHOW THIS TO]

````text
Help me build a rapid prototype to validate my idea.

Idea: [DESCRIBE WHAT YOU WANT TO TEST]
Hypothesis: [WHAT ASSUMPTION ARE YOU TESTING]
Users to test with: [WHO WILL YOU SHOW THIS TO]

Prototype approach:

**Decide**: code prototype vs design prototype
- If testing if people WANT it: Figma or even paper
- If testing if it WORKS: code prototype

**For a code prototype**:
1. Hardcode everything: no database, no auth
2. One happy path only (no error handling)
3. Static data is fine (JSON file, no API)
4. Ugly is ok: validate the idea, not the design

**Speed techniques**:
5. Use shadcn/ui for instant beautiful components
6. v0.dev to generate UI from description
7. Supabase for instant auth + database
8. Vercel for instant deployment

**Validate**:
9. Show to 5 target users
10. Watch them use it (don't explain)
11. Ask: would you pay for this? How much?
12. Decide: build it or kill it

Output: minimal prototype code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Generate Side Project Ideas

**id:** `20-vibe-coding/side-project-idea` · **Difficulty:** beginner · **Tags:** ideas, projects, vibe-coding, creativity

**Placeholders:** [DESCRIBE YOUR INTERESTS AND HOBBIES], [HOURS PER WEEK], [LEARN / MAKE MONEY / PORTFOLIO / FUN], [LIST YOUR TECHNICAL SKILLS]

````text
Generate side project ideas for me to build.

My skills: [LIST YOUR TECHNICAL SKILLS]
Interests: [DESCRIBE YOUR INTERESTS AND HOBBIES]
Time available: [HOURS PER WEEK]
Goal: [LEARN / MAKE MONEY / PORTFOLIO / FUN]

Generate 10 project ideas that:
1. Use my existing skills (so I can ship fast)
2. Solve a real problem I or others have
3. Can be built in 1-4 weeks
4. Could become something bigger

For each idea:
- Problem it solves and who has it
- Core feature set for MVP
- Potential monetization if any
- Learning opportunity
- Effort estimate (days to MVP)

Then:
- Which 3 are best given my goals?
- Which one should I start with and why?
- What's the first 3 things to build?
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master the Vibe Coding Workflow

**id:** `20-vibe-coding/vibe-coding-workflow` · **Difficulty:** beginner · **Tags:** vibe-coding, ai, workflow, productivity

**Placeholders:** [DESCRIBE]

````text
Teach me the vibe coding workflow with AI assistance.

My coding level: [DESCRIBE]
Project I'm building: [DESCRIBE]

Vibe coding = build fast with AI as your co-pilot.

The workflow:

1. **Describe, don't write**:
   - Tell Claude what you want, let it write the first draft
   - 'Build me a user authentication system with JWT'

2. **Iterate, don't perfect**:
   - First version: working, not pretty
   - Second version: handle edge cases
   - Third version: make it clean

3. **Understand what you ship**:
   - Always understand the code Claude writes
   - Ask: 'Explain this line by line'
   - Never ship code you don't understand

4. **Debug with AI**:
   - Share the error + the code
   - Ask why it failed, not just how to fix

5. **Speed techniques**:
   - Start with templates/starters (don't start from scratch)
   - Use shadcn/ui for instant UI components
   - Use Supabase for instant backend

6. **When to stop AI-assist**:
   - Core business logic: understand this yourself
   - Security code: review especially carefully

Apply to my project.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Plan a Weekend Coding Project

**id:** `20-vibe-coding/weekend-project` · **Difficulty:** beginner · **Tags:** weekend, project, vibe-coding, planning

**Placeholders:** [BEST ONE FOR MY GOALS], [DESCRIBE], [IDEA 1], [IDEA 2], [IDEA 3], [LEARN SOMETHING / BUILD SOMETHING USEFUL / HAVE FUN], [SKILL], [THINGS THAT WOULD TAKE TOO LONG], [TIME ESTIMATE], [WHAT DO YOU LIKE BUILDING]

````text
Plan a weekend coding project.

Skill level: [DESCRIBE]
Interests: [WHAT DO YOU LIKE BUILDING]
Goal: [LEARN SOMETHING / BUILD SOMETHING USEFUL / HAVE FUN]
Time: [SATURDAY + SUNDAY, ~12-16 hours]

Weekend project criteria:
- Completeable in a weekend
- Produces a working, shareable result
- Teaches at least one new skill
- Something you'll be proud of

Project ideas based on my profile:
1. [IDEA 1]: builds [SKILL], takes [TIME ESTIMATE]
2. [IDEA 2]: builds [SKILL], takes [TIME ESTIMATE]
3. [IDEA 3]: builds [SKILL], takes [TIME ESTIMATE]

**Recommended project**: [BEST ONE FOR MY GOALS]

Hour-by-hour plan:
- Hour 1-2: Setup + planning
- Hour 3-6: Core feature
- Hour 7-8: Polish
- Hour 9-10: Deploy + share

What to skip (out of scope):
- [THINGS THAT WOULD TAKE TOO LONG]

First command to run to get started:
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an automated utility for [PROJECT_TYPE] with [INTEGRATION]

**id:** `20-vibe-coding/build-an-automated-utility-for-project-type-with-integration` · **Difficulty:** beginner/intermediate/advanced · **Tags:** rapid-prototyping, automation, mvp, vibe-coding, api, shadcn/ui, automated, instant, supabase, minimal, rapid, single-page, web

**Variant group** (24 generated prompts collapsed). Pick one value per placeholder:
- `[PROJECT_TYPE]`: API workflow pipelines | automated email alerting scripts | minimal MVP webapp scaffold | rapid interactive prototype designs | single-page landing page deployment | web scraping data extraction utilities
- `[INTEGRATION]`: Supabase authentication databases | automation scheduling tasks | instant Vercel web deployments | shadcn/ui layout packages | v0 UI designs prompts
- `[APPROACH]`: launching under 2 hours | leveraging AI pair programming | rapid validation loops | zero complex configurations

````text
Build a rapid, functional script that creates [PROJECT_TYPE] integrating [INTEGRATION]. Ensure [APPROACH] is highlighted for quick deployment.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** build-an-automated-utility-for-api-workflow-pipelines-with-automation-scheduling-tasks, build-an-automated-utility-for-api-workflow-pipelines-with-shadcnui-layout-packages, build-an-automated-utility-for-api-workflow-pipelines-with-v0-ui-designs-prompts, build-an-automated-utility-for-automated-email-alerting-scripts-with-automation-scheduling-tasks, build-an-automated-utility-for-automated-email-alerting-scripts-with-instant-vercel-web-deployments, build-an-automated-utility-for-automated-email-alerting-scripts-with-shadcnui-layout-packages, build-an-automated-utility-for-automated-email-alerting-scripts-with-supabase-authentication-databases, build-an-automated-utility-for-automated-email-alerting-scripts-with-v0-ui-designs-prompts, build-an-automated-utility-for-minimal-mvp-webapp-scaffold-with-automation-scheduling-tasks, build-an-automated-utility-for-minimal-mvp-webapp-scaffold-with-instant-vercel-web-deployments, build-an-automated-utility-for-minimal-mvp-webapp-scaffold-with-supabase-authentication-databases, build-an-automated-utility-for-minimal-mvp-webapp-scaffold-with-v0-ui-designs-prompts, build-an-automated-utility-for-rapid-interactive-prototype-designs-with-automation-scheduling-tasks, build-an-automated-utility-for-rapid-interactive-prototype-designs-with-shadcnui-layout-packages, build-an-automated-utility-for-rapid-interactive-prototype-designs-with-supabase-authentication-databases, build-an-automated-utility-for-rapid-interactive-prototype-designs-with-v0-ui-designs-prompts, build-an-automated-utility-for-single-page-landing-page-deployment-with-automation-scheduling-tasks, build-an-automated-utility-for-single-page-landing-page-deployment-with-instant-vercel-web-deployments, build-an-automated-utility-for-single-page-landing-page-deployment-with-supabase-authentication-databases, build-an-automated-utility-for-single-page-landing-page-deployment-with-v0-ui-designs-prompts, build-an-automated-utility-for-web-scraping-data-extraction-utilities-with-instant-vercel-web-deployments, build-an-automated-utility-for-web-scraping-data-extraction-utilities-with-shadcnui-layout-packages, build-an-automated-utility-for-web-scraping-data-extraction-utilities-with-supabase-authentication-databases, build-an-automated-utility-for-web-scraping-data-extraction-utilities-with-v0-ui-designs-prompts


## Ship a [PROJECT_TYPE] in under 2 hours

**id:** `20-vibe-coding/ship-a-project-type-in-under-2-hours` · **Difficulty:** beginner/advanced · **Tags:** rapid-prototyping, automation, mvp, vibe-coding, api, automated, instant, minimal, rapid, single-page, supabase, web

**Variant group** (6 generated prompts collapsed). Pick one value per placeholder:
- `[PROJECT_TYPE]`: API workflow pipelines | automated email alerting scripts | minimal MVP webapp scaffold | rapid interactive prototype designs | single-page landing page deployment | web scraping data extraction utilities
- `[INTEGRATION]`: Supabase authentication databases | instant Vercel web deployments | v0 UI designs prompts
- `[APPROACH]`: launching under 2 hours | leveraging AI pair programming | rapid validation loops | zero complex configurations

````text
Design and build a [PROJECT_TYPE] utilizing [INTEGRATION]. Focus on speed, minimal setup, and applying [APPROACH] to launch rapidly.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** ship-a-api-workflow-pipelines-in-under-2-hours, ship-a-automated-email-alerting-scripts-in-under-2-hours, ship-a-minimal-mvp-webapp-scaffold-in-under-2-hours, ship-a-rapid-interactive-prototype-designs-in-under-2-hours, ship-a-single-page-landing-page-deployment-in-under-2-hours, ship-a-web-scraping-data-extraction-utilities-in-under-2-hours

