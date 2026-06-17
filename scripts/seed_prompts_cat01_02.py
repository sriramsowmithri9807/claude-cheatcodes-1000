#!/usr/bin/env python3
"""
Run this script once to generate all 1000 prompt files.
python3 scripts/seed_prompts.py
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
PROMPTS = ROOT / "prompts"

def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n")
    print(f"  ✍️  {path.relative_to(ROOT)}")

# ─────────────────────────────────────────────
# CATEGORY 01 — VIBE CODING & RAPID PROTOTYPING
# ─────────────────────────────────────────────
cat = PROMPTS / "01-vibe-coding"

VIBE_PROMPTS = [
    ("idea-to-landing-page.md", "Turn an Idea into a Landing Page", ["html", "css", "js", "landing-page"], "beginner",
     """You are a creative full-stack developer. I have a startup idea: [INSERT YOUR IDEA].
Turn it into a complete, beautiful single-page landing page with:
- Hero section with a catchy headline and sub-headline
- 3 feature/benefit sections with icons (use emoji icons)
- A pricing section with 3 tiers (Free, Pro, Enterprise)
- A FAQ section with 5 Q&As
- A footer with social links and copyright
Use pure HTML, CSS, and vanilla JS. Make it modern, dark-mode, with gradient accents. No external libraries except Google Fonts (Inter). Make it mobile-responsive."""),

    ("wireframe-to-react.md", "Convert a Text Wireframe to React Components", ["react", "typescript", "components", "ui"], "intermediate",
     """You are an expert React developer. Convert the following text wireframe description into fully functional React + TypeScript components:

[PASTE YOUR WIREFRAME DESCRIPTION HERE]

Requirements:
- Use functional components with hooks
- TypeScript interfaces for all props
- Styled with CSS Modules or inline styles (no Tailwind)
- Responsive layout using CSS Grid and Flexbox
- Include PropTypes / TypeScript types
- Add hover states and smooth transitions
- Export a single `App.tsx` that composes all components together"""),

    ("app-from-one-sentence.md", "Build a Full App from One Sentence", ["fullstack", "rapid-prototype", "mvp"], "intermediate",
     """You are a 10x developer building an MVP in record time. I want to build: [ONE SENTENCE DESCRIPTION].

Produce:
1. A folder structure for this app
2. A tech stack recommendation with reasoning
3. The complete code for the core feature (the ONE thing that makes this app useful)
4. A `README.md` with setup instructions
5. A list of 5 next features to add after the MVP

Keep the code clean, working, and minimal. No over-engineering. Ship it."""),

    ("clone-ui-from-description.md", "Clone a UI from a Description", ["html", "css", "clone", "ui"], "beginner",
     """You are a pixel-perfect front-end engineer. Recreate the following UI from this description:

[DESCRIBE THE UI: colors, layout, components, feel]

Output a single self-contained HTML file with embedded CSS. Make it look as close to the description as possible. Use:
- CSS variables for colors
- Flexbox/Grid for layout
- Smooth hover animations
- Google Fonts for typography
No images needed — use CSS shapes, gradients, or emoji placeholders."""),

    ("vibe-to-api.md", "Turn a Vibe / Feeling into an API", ["api", "design", "creative", "backend"], "intermediate",
     """I want an API that feels like [DESCRIBE THE VIBE — e.g., "a calm productivity tool", "a chaotic creative playground"].

Design and implement:
1. The REST API routes (method, path, request body, response shape)
2. Express.js implementation with TypeScript
3. Meaningful status codes and error messages that match the vibe
4. A sample `.http` or `curl` test file
5. A one-paragraph "API philosophy" doc comment at the top of the file

Make the developer experience match the vibe — from variable names to error messages."""),

    ("ui-component-library-starter.md", "Scaffold a UI Component Library", ["react", "storybook", "design-system", "components"], "advanced",
     """You are a design systems engineer. Scaffold a minimal but production-ready React component library with:
- Button (variants: primary, secondary, ghost, danger; sizes: sm, md, lg)
- Input (text, password, email with validation states)
- Modal (with backdrop, close button, keyboard ESC support)
- Card (with header, body, footer slots)
- Badge / Chip component

Each component must have:
- TypeScript props interface
- CSS Module styles
- Storybook story (CSF3 format)
- Jest + React Testing Library unit test

Also create: `package.json`, `tsconfig.json`, `.storybook/main.ts`, and `index.ts` barrel export."""),

    ("prototype-in-10-minutes.md", "Ship a Working Prototype in 10 Minutes", ["prototype", "mvp", "vibe-coding"], "beginner",
     """I have exactly 10 minutes. Help me ship a working prototype of: [YOUR IDEA].

Rules:
- Single HTML file, no build step
- Works offline (no API calls required)
- Looks decent (not embarrassing to show)
- Actually demonstrates the core value proposition

Give me the complete code I can copy-paste into a file and open in a browser right now. Then give me 3 things I can add in the next 30 minutes to make it impressive."""),

    ("sass-to-css-variables.md", "Modernize Legacy CSS to CSS Variables", ["css", "refactor", "design-tokens"], "beginner",
     """You are a CSS architecture expert. Refactor this legacy CSS/SASS:

[PASTE YOUR CSS HERE]

Convert it to modern CSS with:
- CSS custom properties (variables) for all colors, spacing, typography
- A `:root` block with a complete design token system
- Logical properties where appropriate (margin-inline, padding-block)
- CSS nesting (native, no preprocessor)
- Remove any vendor prefixes that are no longer needed (2024+)
- Add CSS layers (@layer) for specificity management

Output the refactored CSS and a brief explanation of each major change."""),

    ("generate-fake-data.md", "Generate Realistic Fake Data for Your App", ["testing", "mock-data", "faker", "seed"], "beginner",
     """Generate realistic seed data for my app. Here's the data schema:

[PASTE YOUR DATABASE SCHEMA OR TYPESCRIPT TYPES]

Produce:
1. 20 realistic, diverse sample records (not just "John Doe" and "test@test.com")
2. A JavaScript/TypeScript seed file using this data
3. A Faker.js script that can generate unlimited records following these patterns
4. Edge cases to test: empty fields, long strings, special characters, international names/addresses

Make the fake data feel real — realistic names from diverse cultures, real-looking addresses, plausible dates."""),

    ("readme-generator.md", "Generate a Stunning GitHub README", ["documentation", "readme", "github", "open-source"], "beginner",
     """You are a documentation expert. Generate a stunning GitHub README.md for my project:

Project name: [NAME]
What it does: [DESCRIPTION]
Tech stack: [STACK]
Key features: [LIST]

Include:
- Badges (build status, npm version, license, contributors)
- A hero section with an ASCII art logo or emoji branding
- Feature list with emoji bullets
- Quick start (< 5 steps)
- Full installation and configuration docs
- API reference table (if applicable)
- Contributing section
- License

Make it the kind of README that makes developers star the repo immediately."""),

    ("color-palette-generator.md", "Generate a Complete Color Palette from One Color", ["design", "colors", "css", "ui"], "beginner",
     """I have a brand color: [HEX COLOR].

Generate a complete design system color palette:
1. Primary scale (50–950, 10 shades)
2. Neutral/gray scale (50–950)
3. Semantic colors: success, warning, error, info (each with light/default/dark)
4. Dark mode equivalents for each semantic color

Output as:
- CSS custom properties
- JavaScript/TypeScript object
- Tailwind CSS config extension

Also provide WCAG contrast ratios for text-on-background combinations and flag any accessibility issues."""),

    ("cli-tool-scaffold.md", "Scaffold a CLI Tool", ["cli", "node", "typescript", "tooling"], "intermediate",
     """Build a Node.js CLI tool called `[TOOL-NAME]` that does: [DESCRIPTION].

Implement:
- `commander.js` for argument parsing
- Subcommands: `init`, `run`, `config`, `--help`, `--version`
- Colorized output with `chalk`
- Interactive prompts with `inquirer`
- Configuration file support (~/.toolname/config.json)
- Progress indicators with `ora`
- Proper exit codes

Include: `package.json` (with `bin` field), `tsconfig.json`, entry point, and a `README.md` with usage examples."""),

    ("convert-design-to-code.md", "Convert Figma-Style Design Spec to Code", ["figma", "design-to-code", "react", "css"], "intermediate",
     """You are an expert at converting design specifications to pixel-perfect code. Here is the design spec:

[PASTE FIGMA SPECS / DESIGN TOKENS / DESIGN DESCRIPTION]

Convert to:
- React + TypeScript functional components
- CSS Modules with exact spacing, colors, and typography from the spec
- Responsive breakpoints: mobile (< 768px), tablet (768–1024px), desktop (> 1024px)
- Smooth transitions for interactive states (hover, focus, active, disabled)
- Accessibility: proper ARIA roles, focus indicators, keyboard navigation"""),

    ("boilerplate-eliminator.md", "Eliminate Boilerplate from Any Codebase", ["refactor", "dry", "clean-code", "abstraction"], "intermediate",
     """You are a refactoring expert. Analyze this code:

[PASTE YOUR CODE]

Identify and eliminate ALL boilerplate:
1. List every repeated pattern you find (with line numbers)
2. Create reusable abstractions for each (utility functions, hooks, HOCs, base classes)
3. Rewrite the original code using your abstractions
4. Calculate the lines of code reduction
5. Explain why each abstraction improves maintainability

Follow the DRY principle without over-abstracting. The goal is clarity, not cleverness."""),

    ("state-machine-designer.md", "Design a State Machine for Any Feature", ["state-machine", "xstate", "logic", "architecture"], "advanced",
     """You are an expert in finite state machines. I need a state machine for: [FEATURE DESCRIPTION].

Design:
1. All possible states (draw as an ASCII diagram)
2. All transitions and the events that trigger them
3. Guard conditions for conditional transitions
4. Entry/exit actions for each state
5. Implementation using XState v5 (TypeScript)
6. React integration with `useMachine` hook
7. Unit tests for each state transition

Make the state machine impossible to get into an invalid state."""),

    ("project-ideas-generator.md", "Generate 10 Buildable Project Ideas", ["ideas", "projects", "learning", "portfolio"], "beginner",
     """I am a [SKILL LEVEL] developer who knows [TECH STACK]. I want to build something impressive for my portfolio.

Generate 10 unique, buildable project ideas that:
- Are original (not the 1000th todo app)
- Solve a real problem or are genuinely fun
- Are completable in [TIME FRAME]
- Showcase [SKILLS YOU WANT TO DEMONSTRATE]

For each idea:
- Name and one-sentence description
- Core features (MVP vs stretch goals)
- Tech stack recommendation
- Why it's impressive to employers/the community
- The single hardest technical challenge to solve"""),

    ("weekend-project-planner.md", "Plan a Weekend Coding Project", ["planning", "project-management", "mvp"], "beginner",
     """I have this weekend (Sat + Sun, ~12 hours total) to build: [PROJECT IDEA].

Create a detailed hour-by-hour plan:
- Saturday morning (3h): [Foundation]
- Saturday afternoon (3h): [Core features]  
- Sunday morning (3h): [Polish & edge cases]
- Sunday afternoon (3h): [Deploy & share]

For each block:
- Specific tasks with checkboxes
- Files to create/edit
- Potential blockers and how to avoid them

Also: What to cut if I'm running behind, and what's the absolute minimum I need for a deployable v1."""),

    ("user-story-to-code.md", "Convert User Stories to Working Code", ["agile", "user-stories", "tdd", "features"], "intermediate",
     """Convert these user stories into working code using TDD:

[PASTE USER STORIES IN GIVEN/WHEN/THEN FORMAT]

For each user story:
1. Write the failing test first (Jest)
2. Implement the minimum code to pass the test
3. Refactor for clarity

Tech stack: [YOUR STACK]

Output the complete test file and implementation file. Group tests by user story with `describe` blocks."""),

    ("api-mockup-server.md", "Build an Instant Mock API Server", ["api", "mock", "testing", "json-server"], "beginner",
     """Build me an instant mock API server for my frontend that simulates:

[DESCRIBE YOUR API NEEDS / PASTE OPENAPI SPEC]

Use Express.js + TypeScript. Include:
- All CRUD endpoints with realistic fake data
- Simulated network delay (100–500ms random)
- Error simulation (5% chance of 500 error)
- CORS configured for localhost
- Authentication simulation (any Bearer token accepted)
- Pagination support on list endpoints
- Request/response logging middleware

Also include a `db.json` with 20 realistic seed records per entity."""),

    ("portfolio-project-scaffold.md", "Scaffold a Portfolio-Worthy Project", ["portfolio", "career", "project", "showcase"], "intermediate",
     """I'm a developer trying to impress employers. Build a complete scaffold for a portfolio project about: [TOPIC].

Include:
- Professional folder structure
- Complete `README.md` with badges and screenshots section
- Environment configuration (.env.example)
- Docker Compose for local development
- GitHub Actions CI pipeline
- Pre-commit hooks (eslint, prettier, commitlint)
- The core feature implemented end-to-end
- Deployment instructions for Railway/Vercel/Render

Make this look like it was built by someone who takes their craft seriously."""),

    ("idea-validator.md", "Validate a Product Idea with Claude", ["product", "validation", "startup", "research"], "beginner",
     """Act as an experienced product manager and startup advisor. Validate this idea: [YOUR IDEA].

Provide:
1. **Market size estimate** (TAM/SAM/SOM)
2. **3 strongest reasons this could work**
3. **3 biggest risks that could kill it**
4. **Competitor landscape** (direct and indirect)
5. **The riskiest assumption** to test first
6. **A 2-week validation experiment** I can run with no code
7. **Verdict**: Build it / Don't build it / Build something adjacent

Be brutally honest. Don't sugarcoat."""),

    ("code-challenge-solver.md", "Solve Coding Challenges with Explanation", ["algorithms", "leetcode", "interviews", "problem-solving"], "intermediate",
     """You are an expert competitive programmer and technical interviewer. Solve this problem:

[PASTE THE PROBLEM STATEMENT]

Provide:
1. **Brute force solution** with time/space complexity
2. **Optimal solution** with explanation of the key insight
3. **Step-by-step walkthrough** on the example inputs
4. **Edge cases** to handle and why
5. **TypeScript/Python code** (clean, commented)
6. **Follow-up questions** an interviewer might ask and how to answer them

Don't just give code — teach me to think about this type of problem."""),

    ("micro-saas-blueprint.md", "Blueprint a Micro-SaaS in a Weekend", ["saas", "startup", "monetization", "product"], "intermediate",
     """Design a complete Micro-SaaS blueprint for: [YOUR IDEA].

Include:
1. **Landing page copy** (headline, subheadline, 3 features, CTA)
2. **Pricing strategy** with 3 tiers and justification
3. **Tech stack** (keep it boring and proven)
4. **Database schema** for the core entities
5. **Auth flow** (use Clerk/Auth0/Supabase Auth)
6. **Payment integration** (Stripe checkout + webhooks)
7. **Week 1 launch checklist** (what to build, what to skip)
8. **First 10 customers acquisition strategy**

Budget: $0 infra cost at launch. Target: profitable within 30 days."""),

    ("design-system-tokens.md", "Create a Complete Design Token System", ["design-tokens", "css", "design-system", "theming"], "intermediate",
     """Create a production-grade design token system for a [TYPE OF APP: SaaS/e-commerce/dashboard/marketing].

Include all categories:
- **Colors**: brand, neutral, semantic (success/warning/error/info), dark mode variants
- **Typography**: font families, sizes (scale), weights, line heights, letter spacing
- **Spacing**: 4px base grid, scale from 0 to 96
- **Border radius**: sm/md/lg/full
- **Shadows**: 5 levels
- **Breakpoints**: xs/sm/md/lg/xl/2xl
- **Z-index**: named layers (modal, tooltip, dropdown, sticky)
- **Animation**: duration, easing curves

Output as: CSS custom properties, JavaScript ES module, and Figma-ready JSON (Style Dictionary format)."""),

    ("component-from-screenshot.md", "Reverse-Engineer a Component from Description", ["react", "components", "reverse-engineer", "ui"], "intermediate",
     """Reverse-engineer this UI component from my description:

[DESCRIBE THE COMPONENT IN DETAIL: layout, colors, interactions, animations]

Build it as:
- React + TypeScript functional component
- Self-contained (no external UI library dependencies)
- CSS Module for styles
- Full keyboard accessibility (ARIA, focus management)
- Responsive
- Storybook story showing all states
- Props with sensible defaults

Name the component `[ComponentName]` and export it from `index.ts`."""),

    ("hackathon-starter.md", "Build a Hackathon Project Starter", ["hackathon", "rapid-prototype", "fullstack", "starter"], "intermediate",
     """I'm starting a hackathon in 1 hour. My project idea: [IDEA]. Time limit: [X hours].

Give me:
1. The exact tech stack to use (optimized for speed, not perfection)
2. A Next.js + TypeScript starter project with:
   - Auth (Clerk free tier)
   - Database (Supabase free tier)
   - UI (shadcn/ui)
   - Deployment config (Vercel)
3. The 3 pages/routes I need to build
4. The database schema
5. Hour-by-hour timeline
6. The one demo flow that will impress judges

Start with the complete `npx create-next-app` command and all setup steps."""),

    ("side-project-automator.md", "Automate Your Side Project's Boring Parts", ["automation", "scripts", "productivity", "devops"], "intermediate",
     """I'm building [PROJECT] and I keep doing these repetitive tasks manually: [LIST TASKS].

Automate everything with:
1. **Shell scripts** for each task
2. **npm scripts** in package.json
3. **GitHub Actions** for any CI/CD tasks
4. **Makefile** with a help target listing all commands
5. A **pre-commit hook** that runs relevant checks

For each automation:
- The script code
- How to invoke it
- What it does and why it saves time"""),

    ("feature-flag-system.md", "Build a Simple Feature Flag System", ["feature-flags", "backend", "typescript", "devops"], "intermediate",
     """Build a lightweight feature flag system for my Node.js app.

Requirements:
- Store flags in a JSON file (for simplicity) with live reload
- Types: boolean, percentage rollout, user-segment targeting
- SDK: `isEnabled(flagName, userId?)` function
- Admin API: GET/POST/PATCH flags
- React hook: `useFeatureFlag(name)` for frontend
- Audit log: who changed what flag and when

Keep it simple enough to understand in 10 minutes, powerful enough to use in production."""),

    ("project-retrospective.md", "Run an AI-Powered Project Retrospective", ["retrospective", "agile", "productivity", "team"], "beginner",
     """Act as an experienced engineering manager facilitating a retrospective. Here are notes from our last sprint/project:

[PASTE YOUR SPRINT NOTES, INCIDENTS, METRICS, FEEDBACK]

Facilitate a retrospective:
1. **What went well** (celebrate these)
2. **What didn't go well** (be specific, no blame)
3. **Root cause analysis** for the top 2 problems
4. **Actionable improvements** (with owners and deadlines)
5. **Team health check** based on the data
6. **One process change** to implement immediately

Output as a formatted retrospective report suitable for sharing with the team."""),

    ("chrome-extension-scaffold.md", "Scaffold a Chrome Extension", ["chrome-extension", "javascript", "browser", "web"], "intermediate",
     """Build a complete Chrome Extension that: [DESCRIBE WHAT IT DOES].

Include all required files:
- `manifest.json` (Manifest V3)
- `popup.html` + `popup.js` (extension popup UI)
- `background.js` (service worker)
- `content.js` (page injection script if needed)
- `options.html` (settings page)
- CSS styles

Features:
- Storage sync for settings
- Message passing between popup ↔ background ↔ content
- Context menu integration
- Keyboard shortcut

Also include: instructions for loading in Chrome developer mode."""),

    ("n8n-automation-workflow.md", "Design an n8n Automation Workflow", ["automation", "n8n", "no-code", "workflow"], "beginner",
     """Design a complete n8n automation workflow for: [DESCRIBE YOUR AUTOMATION].

Provide:
1. The complete workflow as a JSON export (importable into n8n)
2. Step-by-step explanation of each node
3. Error handling nodes and what they do
4. Webhook triggers and their configuration
5. Environment variables to configure
6. Testing instructions

If n8n can't do part of it, suggest a custom Code node solution."""),

    ("supabase-backend.md", "Build a Complete Backend with Supabase", ["supabase", "postgresql", "backend", "auth"], "intermediate",
     """Build a complete backend for [APP TYPE] using Supabase.

Include:
1. Database schema with all tables, columns, types, and constraints
2. Row Level Security (RLS) policies for each table
3. PostgreSQL functions and triggers
4. TypeScript types generated from schema
5. Supabase client setup with proper TypeScript generics
6. Auth configuration (email/password + OAuth)
7. Storage bucket setup for file uploads
8. Edge Functions for any custom logic

Output as: SQL migration files + TypeScript client code."""),

    ("graphql-schema-first.md", "Design a GraphQL API Schema-First", ["graphql", "api", "schema", "typescript"], "advanced",
     """You are a GraphQL expert. Design a GraphQL API for: [YOUR APP].

Schema-first approach:
1. Complete GraphQL SDL schema (all types, queries, mutations, subscriptions)
2. TypeScript codegen config (using GraphQL Code Generator)
3. Resolvers implementation (Node.js + Apollo Server)
4. DataLoader setup for N+1 prevention
5. Authentication/authorization in resolvers
6. Error handling with custom error types
7. Example queries in GraphQL Playground format
8. Performance considerations for each resolver"""),

    ("progressive-web-app.md", "Convert a Website to a PWA", ["pwa", "service-worker", "offline", "mobile"], "intermediate",
     """Convert my existing web app into a Progressive Web App (PWA).

[DESCRIBE YOUR CURRENT APP]

Implement:
1. Web App Manifest (`manifest.json`) with all required fields
2. Service Worker with: cache-first strategy, network-first for API calls, offline fallback page
3. App install prompt (beforeinstallprompt handling)
4. Push notifications setup (with permission flow)
5. Background sync for offline form submissions
6. Update notification when new version is available

Lighthouse PWA score target: 100."""),

    ("monorepo-setup.md", "Set Up a Professional Monorepo", ["monorepo", "turborepo", "pnpm", "nx", "architecture"], "advanced",
     """Set up a professional monorepo for a project with: [LIST YOUR APPS AND PACKAGES].

Use: pnpm workspaces + Turborepo

Structure:
```
apps/
  web/        (Next.js)
  api/        (Node.js/Express)
  mobile/     (React Native or Expo)
packages/
  ui/         (shared React components)
  utils/      (shared utilities)
  types/      (shared TypeScript types)
  config/     (shared configs: eslint, tsconfig, prettier)
```

Provide:
- Root `package.json` and `turbo.json` config
- Each `package.json` with proper workspace references
- Shared TypeScript config inheritance
- Build and dev pipeline
- CI pipeline that only runs affected packages"""),

    ("real-time-feature.md", "Add Real-Time Features to Any App", ["websockets", "socket-io", "real-time", "backend"], "intermediate",
     """Add real-time features to my [TYPE] app.

Features to add:
- [FEATURE 1: e.g., live chat]
- [FEATURE 2: e.g., real-time notifications]
- [FEATURE 3: e.g., collaborative editing indicator]

Implement using Socket.IO + Node.js:
1. Server setup with rooms and namespaces
2. Client SDK (React hook: `useSocket`)
3. Reconnection handling
4. Presence system (who's online)
5. Optimistic updates on the client
6. Scaling notes for when you need multiple servers (Redis adapter)"""),

    ("performance-audit.md", "Audit and Fix App Performance", ["performance", "optimization", "lighthouse", "web-vitals"], "advanced",
     """You are a web performance expert. Here is my app's performance data:

[PASTE: Lighthouse report, Web Vitals, bundle size report, or description of slowness]

Provide:
1. **Diagnosis**: Root cause of each performance issue
2. **Quick wins** (fixes taking < 1 hour each)
3. **Code changes** with before/after examples for the top 3 issues
4. **Bundle optimization**: code splitting, lazy loading, tree shaking
5. **Image optimization** strategy
6. **Caching strategy** (HTTP headers, service worker, CDN)
7. **Target metrics**: LCP < 2.5s, FID < 100ms, CLS < 0.1"""),

    ("ai-powered-search.md", "Add AI-Powered Search to Your App", ["search", "embeddings", "vector-db", "ai"], "advanced",
     """Add semantic AI-powered search to my app.

Current setup: [DESCRIBE YOUR DATA AND TECH STACK]

Implement:
1. **Embedding generation** using Claude API (or OpenAI embeddings as fallback)
2. **Vector storage** with pgvector (PostgreSQL) or Pinecone
3. **Indexing pipeline**: ingest documents → chunk → embed → store
4. **Search API**: query → embed → vector similarity search → rerank
5. **Frontend search bar** with debouncing, loading states, highlighted results
6. **Hybrid search**: combine keyword (BM25) + semantic for better results

Performance target: < 500ms search latency for 100k documents."""),

    ("serverless-functions.md", "Build Serverless Functions for Your App", ["serverless", "aws-lambda", "vercel-functions", "edge"], "intermediate",
     """Build serverless functions for my app. I need to handle:

[LIST YOUR BACKEND OPERATIONS]

For each function:
1. Implementation (TypeScript, compatible with Vercel/AWS Lambda/Cloudflare Workers)
2. Input validation with Zod
3. Error handling with proper HTTP status codes
4. Cold start optimization
5. Environment variable usage
6. Local testing with Vitest
7. Deployment config

Also include: a shared middleware pattern for auth, logging, and CORS."""),

    ("open-api-spec.md", "Generate an OpenAPI 3.1 Spec for Your API", ["openapi", "swagger", "api-docs", "rest"], "intermediate",
     """Generate a complete OpenAPI 3.1 specification for my API:

[DESCRIBE YOUR API: endpoints, auth method, main entities]

Include:
- All paths with GET/POST/PUT/PATCH/DELETE where appropriate
- Request bodies with JSON Schema validation
- Response schemas for 200, 400, 401, 403, 404, 500
- Security schemes (Bearer JWT or API Key)
- Tags for grouping
- Examples for every endpoint
- Reusable components ($ref schemas)

Output as valid YAML that can be imported into Swagger UI or Postman."""),

    ("git-workflow-setup.md", "Set Up a Professional Git Workflow", ["git", "workflow", "branching", "ci"], "beginner",
     """Set up a professional Git workflow for my team working on [PROJECT TYPE].

Provide:
1. Branching strategy (GitFlow vs trunk-based, with justification for my team size)
2. Commit message convention (Conventional Commits) with examples
3. Pre-commit hooks (`.husky/` + `lint-staged` config)
4. PR/MR template (`.github/pull_request_template.md`)
5. Branch protection rules to configure on GitHub
6. `commitlint.config.js` configuration
7. `CHANGELOG.md` automation with `standard-version`
8. Git aliases cheat sheet for the team"""),

    ("env-config-management.md", "Set Up Bulletproof Environment Config", ["config", "environment", "secrets", "devops"], "intermediate",
     """Set up bulletproof environment configuration for my Node.js/Next.js app.

Implement:
1. `env.ts` — typed env validation using Zod (crash on startup if invalid)
2. `.env.example` with all variables documented
3. `.env.local`, `.env.staging`, `.env.production` structure
4. GitHub Actions secrets setup guide
5. Docker environment file handling
6. How to rotate secrets without downtime
7. Which variables are safe to commit vs must be secret

Never let a missing env variable cause a silent bug in production again."""),

    ("code-splitter.md", "Intelligently Split a Large File", ["refactor", "architecture", "clean-code", "modules"], "intermediate",
     """This file has grown too large: [PASTE FILE OR DESCRIBE IT].

Refactor it by:
1. Identifying all distinct concerns/responsibilities in this file
2. Proposing a new folder structure with one file per concern
3. Writing each split file with proper imports/exports
4. Updating the original file to import from the new modules
5. Identifying any circular dependencies to watch for

Follow: Single Responsibility Principle. Each file should have exactly one reason to change."""),

    ("incident-postmortem.md", "Write a Production Incident Postmortem", ["postmortem", "devops", "reliability", "documentation"], "intermediate",
     """You are an SRE writing a blameless postmortem. Here are the incident details:

[PASTE: incident timeline, affected systems, errors, metrics]

Write a professional postmortem including:
1. **Incident summary** (1 paragraph, suitable for stakeholders)
2. **Timeline** (minute-by-minute from detection to resolution)
3. **Root cause** (5 Whys analysis)
4. **Contributing factors** (not blame — systemic issues)
5. **Impact** (users affected, duration, data loss if any)
6. **Resolution steps** taken
7. **Action items** to prevent recurrence (with owners and due dates)
8. **Lessons learned**

Blameless tone throughout."""),

    ("test-data-factory.md", "Build a Test Data Factory", ["testing", "factories", "typescript", "jest"], "intermediate",
     """Build a test data factory system for my TypeScript project.

Models to build factories for:
[PASTE YOUR TYPESCRIPT INTERFACES/TYPES]

Implement:
1. Factory function for each model with sensible defaults
2. Override capability: `createUser({ email: 'test@test.com' })`
3. Trait support: `createUser('admin')`, `createUser('suspended')`
4. Relationship factories: `createPost({ author: createUser() })`
5. Sequence numbers for unique fields
6. Faker.js integration for realistic data
7. Database factory that actually creates records (Prisma/Drizzle)

Pattern: inspired by factory_bot (Ruby) or fishery (TypeScript)."""),

    ("rate-limiter.md", "Implement Rate Limiting for Your API", ["rate-limiting", "redis", "api", "security"], "intermediate",
     """Implement production-grade rate limiting for my Express.js API.

Requirements:
- Sliding window algorithm (fairer than fixed window)
- Per-user rate limits (authenticated) and per-IP (anonymous)
- Different limits per route: strict for auth, generous for reads
- Redis backend for distributed rate limiting
- Graceful response with `Retry-After` header
- Rate limit headers in every response (X-RateLimit-Limit, Remaining, Reset)
- Admin bypass capability
- Rate limit exceeded webhook/alert

Include unit tests for the rate limiter logic."""),

    ("subscription-system.md", "Build a Subscription/Payment System", ["stripe", "subscriptions", "payments", "saas"], "advanced",
     """Build a complete subscription system using Stripe.

App type: [YOUR APP TYPE]
Plans: [LIST YOUR PLANS AND PRICES]

Implement:
1. Stripe Products and Prices setup
2. Checkout session creation
3. Customer portal for subscription management
4. Webhook handler for all critical events:
   - payment_intent.succeeded
   - customer.subscription.updated/deleted
   - invoice.payment_failed
5. Database schema for subscriptions
6. Middleware to check subscription status on protected routes
7. Usage-based billing if applicable
8. Dunning: what happens when payment fails

Production-ready with idempotency keys and webhook signature verification."""),

    ("search-and-filter.md", "Build Advanced Search and Filter UI", ["search", "filter", "react", "ux"], "intermediate",
     """Build an advanced search and filter UI component for a [TYPE: table/list/gallery].

Data shape: [DESCRIBE YOUR DATA]

Features:
- Full-text search with debouncing (300ms)
- Multi-select filters per field
- Date range picker
- Sort by multiple columns
- URL state sync (filters persist in URL params)
- Active filter chips with remove buttons
- Clear all filters button
- Loading skeleton while fetching
- Empty state with helpful message
- Result count display

React + TypeScript, no UI library dependencies."""),

    ("error-boundary-system.md", "Build a Production Error Boundary System", ["react", "error-handling", "reliability", "monitoring"], "intermediate",
     """Build a comprehensive error boundary system for a React app.

Implement:
1. Generic `ErrorBoundary` component with fallback UI
2. Route-level error boundaries (one per major section)
3. Component-level granular error boundaries
4. Error reporting to Sentry (or a generic reporter interface)
5. Error recovery (retry button)
6. Different fallback UIs: page-level (full page) vs component-level (inline)
7. Development mode: detailed error info + stack trace
8. Production mode: user-friendly message only
9. Error ID for user to report to support

TypeScript, works with React 18+ (concurrent mode safe)."""),

    ("animation-library.md", "Build a Micro-Animation System", ["animations", "css", "framer-motion", "ux"], "intermediate",
     """Build a reusable micro-animation system for my React app.

Create:
1. **CSS animation primitives** in a global stylesheet:
   - fadeIn, slideIn (4 directions), scaleIn, bounceIn
   - Exit animations: fadeOut, slideOut, scaleOut
2. **React components**: `<AnimateIn>`, `<AnimateOut>`, `<AnimatePresence>`
3. **Framer Motion variants** for complex sequences
4. **Page transitions** between routes
5. **Stagger animations** for lists (items animate in one by one)
6. **Skeleton loading** animations
7. **Reduced motion** support (prefers-reduced-motion media query)

Performance: CSS transforms only (no layout-triggering properties). 60fps target."""),

    ("dark-mode-implementation.md", "Implement Perfect Dark Mode", ["dark-mode", "theming", "css", "react"], "intermediate",
     """Implement a perfect dark mode system for my [React/Next.js/Vue] app.

Requirements:
- Respect OS preference on first visit
- User override with persistent preference (localStorage)
- No flash of unstyled content (FOUC) on page load
- Smooth transition between modes (CSS transition)
- CSS custom properties for all color tokens
- `useTheme()` React hook
- Theme toggle component with animation
- System → Light → Dark cycling

Bonus:
- Per-component theme override
- High contrast mode support
- Auto switch at sunrise/sunset (geolocation)

Include the Next.js specific FOUC prevention script."""),

    ("ai-chatbot-ui.md", "Build a ChatGPT-Style Chatbot UI", ["ai", "chat", "react", "streaming"], "intermediate",
     """Build a beautiful ChatGPT-style chatbot UI that connects to an AI API.

Features:
- Message thread with user/assistant bubbles
- Streaming response (character by character using SSE/ReadableStream)
- Markdown rendering in assistant messages (code blocks, lists, bold)
- Code block with syntax highlighting + copy button
- Auto-scroll to latest message
- Stop generation button
- Conversation history sidebar
- New chat button
- Model selector dropdown
- Message timestamps
- Regenerate response button

Tech: React + TypeScript. API: Claude API or OpenAI compatible."""),

    ("keyboard-shortcuts.md", "Add a Keyboard Shortcuts System", ["accessibility", "keyboard", "ux", "productivity"], "intermediate",
     """Add a comprehensive keyboard shortcut system to my React app.

Implement:
1. Global shortcut registry with conflict detection
2. Context-aware shortcuts (active only in certain components)
3. `useKeyboardShortcut(keys, handler, options)` hook
4. Shortcuts help modal (triggered by `?` key) showing all active shortcuts
5. Customizable shortcuts saved to user preferences
6. Visual shortcut hints on buttons/menu items (like Notion/Linear)
7. Sequential shortcuts (Vim-style: `g` then `h` = go home)
8. Platform-aware: show ⌘ on Mac, Ctrl on Windows

Include: escape hatch for when user is typing in an input."""),

    ("notification-system.md", "Build an In-App Notification System", ["notifications", "react", "backend", "real-time"], "advanced",
     """Build a complete in-app notification system.

Backend (Node.js):
- Notification model with: type, title, body, read status, userId, createdAt
- Polymorphic target (comment notification vs system alert vs mention)
- Bulk create API for fan-out to many users
- Mark read/unread, mark all read
- Real-time delivery via WebSocket

Frontend (React):
- Bell icon with unread count badge
- Dropdown panel with notification list
- Notification item with icon, text, time ago, read indicator
- Infinite scroll for history
- Sound + browser push notifications (with permission)
- Toast for new notifications while browsing

Include database migration and the complete API + UI code."""),

    ("i18n-setup.md", "Set Up Internationalization (i18n)", ["i18n", "localization", "next-intl", "react-i18next"], "intermediate",
     """Set up complete internationalization for my [React/Next.js] app.

Target languages: English, Spanish, French, [ADD MORE]

Implement:
1. `next-intl` or `react-i18next` configuration
2. Translation file structure with namespaces
3. `useTranslation()` hook usage patterns
4. Pluralization rules
5. Date, number, and currency formatting per locale
6. RTL support for Arabic/Hebrew
7. Language switcher component
8. Lazy loading translation bundles
9. Missing translation detection in development
10. SEO: `hreflang` tags, locale-aware routing

Provide 50 sample translation strings across 3 languages."""),

    ("image-upload-system.md", "Build a Complete Image Upload System", ["uploads", "storage", "react", "backend"], "intermediate",
     """Build a complete image upload and management system.

Stack: [YOUR STACK]
Storage: S3 (or Cloudflare R2 / Supabase Storage)

Features:
1. **Frontend**: Drag-and-drop upload zone with progress bar
2. **Validation**: file type, size limit, dimension constraints
3. **Preview**: instant preview before upload
4. **Processing**: server-side resizing with Sharp (thumbnail, medium, full)
5. **Upload**: presigned S3 URL (client uploads directly to S3)
6. **Database**: store file metadata (URL, size, dimensions, user)
7. **CDN**: serve via CloudFront/CDN URL
8. **Deletion**: cleanup S3 when record is deleted

Include: TypeScript types, error states, and loading UX."""),
]

for filename, title, tags, difficulty, prompt_text in VIBE_PROMPTS:
    models = ["claude-haiku-3-5", "claude-sonnet-4", "claude-opus-4", "claude-fable-5"]
    content = f"""---
title: "{title}"
category: vibe-coding
models: [{', '.join(models)}]
tags: [{', '.join(tags)}]
difficulty: {difficulty}
author: community
tested: true
---

## 🎯 Prompt

```
{prompt_text.strip()}
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
"""
    write(cat / filename, content)

# ─────────────────────────────────────────────
# CATEGORY 02 — FRONTEND DEVELOPMENT
# ─────────────────────────────────────────────
cat = PROMPTS / "02-frontend-dev"

FRONTEND_PROMPTS = [
    ("react-custom-hooks.md", "Build 10 Essential Custom React Hooks", ["react", "hooks", "typescript"], "intermediate",
     """Build 10 production-ready custom React hooks that every app needs:

1. `useLocalStorage<T>(key, initialValue)` — persistent state with type safety
2. `useDebounce<T>(value, delay)` — debounce any value
3. `useIntersectionObserver(options)` — lazy loading, infinite scroll
4. `useMediaQuery(query)` — responsive logic in JS
5. `useClickOutside(ref, handler)` — close dropdowns/modals
6. `usePrevious<T>(value)` — access previous render value
7. `useAsync<T>(asyncFn)` — async operations with loading/error state
8. `useCopyToClipboard()` — copy text with success feedback
9. `useKeyPress(key)` — keyboard shortcut detection
10. `useWindowSize()` — responsive dimensions

For each hook:
- TypeScript implementation
- JSDoc comments
- Usage example
- Edge cases handled"""),

    ("react-form-wizard.md", "Build a Multi-Step Form Wizard", ["react", "forms", "validation", "typescript"], "intermediate",
     """Build a production-ready multi-step form wizard in React + TypeScript.

Steps: [DESCRIBE YOUR FORM STEPS AND FIELDS]

Features:
- Progress indicator (step dots or bar)
- Validation per step before advancing (react-hook-form + Zod)
- Back button with state preservation
- Data persists in localStorage (survive page refresh)
- Review step showing all inputs before submit
- Loading state during submission
- Success/error states
- Accessible (ARIA live regions for step changes)
- Smooth step transition animations

No UI library — pure React + CSS Modules."""),

    ("virtualized-list.md", "Build a Virtualized Infinite List", ["react", "virtualization", "performance", "ui"], "advanced",
     """Build a high-performance virtualized infinite scroll list for [DATA TYPE].

Using: react-virtual or tanstack-virtual

Features:
- Renders only visible items (handles 100k+ items)
- Dynamic row heights
- Sticky headers for groups
- Infinite scroll (fetch next page when near bottom)
- Skeleton loading for initial and page loads
- Pull-to-refresh (mobile)
- Keyboard navigation (up/down arrows, page up/down)
- Jump to item by index API
- Empty, loading, error, and end-of-list states

Include the React Query integration for data fetching."""),

    ("drag-and-drop-kanban.md", "Build a Drag-and-Drop Kanban Board", ["react", "dnd", "kanban", "ui"], "advanced",
     """Build a fully-featured Kanban board with drag and drop.

Using: @dnd-kit/core (modern, accessible alternative to react-beautiful-dnd)

Features:
- Drag cards between columns
- Drag columns to reorder
- Add/edit/delete cards (inline editing)
- Card colors and labels
- Due dates on cards
- Smooth drop animations
- Touch support (mobile drag and drop)
- Keyboard-accessible drag and drop
- Optimistic updates with rollback on error
- Persist order to backend (PATCH API call on drop)

TypeScript, no CSS framework dependency."""),

    ("data-table.md", "Build a Feature-Rich Data Table", ["react", "table", "tanstack-table", "ui"], "advanced",
     """Build a production-grade data table component.

Data: [DESCRIBE YOUR DATA COLUMNS AND TYPES]
Using: TanStack Table v8 (formerly react-table)

Features:
- Column sorting (single and multi-column)
- Column filtering (text, select, date range)
- Global search
- Pagination with page size selector
- Column visibility toggle
- Column resizing
- Row selection with select-all
- Bulk actions on selected rows
- Export to CSV/Excel
- Row expansion for details
- Pinned columns (first and last)
- Sticky header
- Loading skeleton
- Empty state

TypeScript with inferred column types."""),

    ("chart-dashboard.md", "Build a Charts and Analytics Dashboard", ["react", "charts", "recharts", "analytics"], "intermediate",
     """Build a beautiful analytics dashboard with interactive charts.

Metrics to display: [LIST YOUR METRICS]
Library: Recharts (or Visx for more control)

Include:
1. Area chart for time series (with brushing for date range selection)
2. Bar chart for comparisons (horizontal and vertical)
3. Pie/Donut chart for distribution
4. Metric cards with trend indicators (↑↓)
5. Data table with sort for detailed view
6. Date range picker to filter all charts simultaneously
7. Responsive grid layout
8. Loading skeletons for each chart
9. Tooltip with formatted numbers
10. Color theme consistent with brand

Dark mode support included."""),

    ("nextjs-app-router.md", "Master Next.js App Router Patterns", ["nextjs", "app-router", "react", "typescript"], "advanced",
     """Implement these Next.js 14+ App Router patterns for [MY APP]:

1. **Layouts**: Root layout, nested layouts, parallel routes
2. **Loading UI**: `loading.tsx` with Suspense boundaries
3. **Error handling**: `error.tsx` with reset functionality
4. **Server Components**: data fetching without `useEffect`
5. **Client Components**: minimal client JS, proper `'use client'` usage
6. **Server Actions**: form handling without API routes
7. **Route Handlers**: API endpoints in `app/api/`
8. **Metadata API**: dynamic SEO metadata per page
9. **Streaming**: `<Suspense>` for progressive loading
10. **Caching**: `fetch` with revalidation, `unstable_cache`

Show before/after for each pattern migrating from Pages Router."""),

    ("css-animation-masterclass.md", "CSS Animation Masterclass", ["css", "animations", "keyframes", "ux"], "intermediate",
     """Create a complete animation system using pure CSS (no JavaScript).

Implement:
1. **Entrance animations**: fadeIn, slideUp, slideLeft, scaleIn, bounceIn
2. **Attention seekers**: shake, pulse, swing, tada
3. **Exits**: fadeOut, slideDown, scaleOut
4. **Continuous**: spin, ping, blink, wave
5. **Scroll-triggered**: using `@keyframes` + Intersection Observer via CSS only (animation-play-state)
6. **Stagger pattern**: `nth-child` animation delays for lists
7. **Reduced motion**: `@media (prefers-reduced-motion: reduce)` fallbacks

Each animation as a reusable CSS class.
Timing functions: use `cubic-bezier()` for natural motion, not just ease-in-out."""),

    ("react-context-patterns.md", "Master React Context Patterns", ["react", "context", "state-management", "typescript"], "intermediate",
     """Implement production-quality React Context patterns for [APP TYPE].

Build context for: [LIST YOUR GLOBAL STATE NEEDS]

Implement:
1. **Typed context** with TypeScript generics
2. **Null safety**: custom hook that throws if used outside provider
3. **Performance optimization**: split context to avoid unnecessary re-renders
4. **Compound component pattern**: context + parent/child composition
5. **Context with useReducer**: for complex state (like Redux but built-in)
6. **Lazy initialization**: expensive state init only runs once
7. **Context selector pattern**: subscribe to slices only

Show: when to use Context vs Zustand vs Jotai vs Redux — and why."""),

    ("accessible-components.md", "Build Fully Accessible UI Components", ["accessibility", "aria", "wcag", "react"], "advanced",
     """Build these UI components with perfect accessibility (WCAG 2.1 AA):

1. **Modal/Dialog**: focus trap, ESC to close, aria-modal, return focus on close
2. **Dropdown Menu**: arrow key navigation, type-ahead search
3. **Combobox/Autocomplete**: ARIA 1.2 combobox pattern
4. **Toast notifications**: aria-live region, auto-dismiss with warning
5. **Tabs**: roving tabindex pattern
6. **Accordion**: ARIA expanded state, keyboard support
7. **Date Picker**: calendar grid with keyboard navigation
8. **Data Table**: sortable columns with aria-sort

For each:
- Screen reader announcements
- Keyboard interaction pattern
- Focus management
- ARIA roles, states, properties
- Testing with axe-core"""),

    ("responsive-grid-system.md", "Build a Custom Responsive Grid System", ["css", "grid", "layout", "responsive"], "intermediate",
     """Build a custom CSS Grid system from scratch (no Bootstrap/Tailwind).

Implement:
1. 12-column grid with gutters (CSS custom properties for easy config)
2. Named grid areas for semantic layouts
3. Auto-responsive: `auto-fill` and `minmax()` patterns
4. Nested grids
5. Full-page layouts: sidebar, header, footer, main content
6. Card grid: masonry-style and equal-height
7. Subgrid (CSS Subgrid) for aligned children
8. Grid debugging: overlay helper

Breakpoints: 5 levels (xs/sm/md/lg/xl)
Output: a CSS file usable via `<link>` or importable in React."""),

    ("form-validation.md", "Master Form Validation Patterns", ["forms", "react-hook-form", "zod", "typescript"], "intermediate",
     """Implement comprehensive form validation for [FORM TYPE].

Using: react-hook-form + Zod

Patterns to cover:
1. Basic field validation (required, minLength, pattern)
2. Custom validators (async: check if email exists in DB)
3. Cross-field validation (confirm password, date ranges)
4. Dynamic field arrays (add/remove items)
5. Conditional fields (show field B only if field A = X)
6. File upload validation (type, size, dimensions)
7. Validation on blur vs on submit (when to use each)
8. Server-side error integration (map API errors to fields)
9. Form reset and dirty state tracking
10. Accessible error messages (aria-describedby)"""),

    ("react-query-patterns.md", "Master React Query / TanStack Query", ["react-query", "tanstack", "data-fetching", "cache"], "intermediate",
     """Master TanStack Query v5 (React Query) for [MY APP].

Implement these patterns:
1. Basic `useQuery` with TypeScript generics
2. `useMutation` with optimistic updates + rollback
3. Infinite queries for pagination/infinite scroll
4. Prefetching: hover prefetch, SSR prefetch (Next.js)
5. Dependent queries (query B runs after query A)
6. Query invalidation strategies
7. Polling: refetch every N seconds
8. Offline support: `networkMode: 'offlineFirst'`
9. Global error handling with `QueryErrorBoundary`
10. DevTools integration

Include: a `queryClient` singleton setup and provider configuration."""),

    ("svg-animations.md", "Create Advanced SVG Animations", ["svg", "animations", "css", "gsap"], "advanced",
     """Create stunning SVG animations for:

[DESCRIBE: icons, logos, illustrations, charts, or data viz you want to animate]

Implement:
1. SVG path drawing animation (stroke-dasharray/dashoffset technique)
2. Morphing between shapes
3. Animated SVG icons (menu → close, play → pause)
4. Particle/wave animation
5. Loading spinner (custom, branded)
6. Chart reveal animations
7. GSAP integration for timeline-based sequences
8. Accessibility: `prefers-reduced-motion` + `aria-hidden` on decorative SVGs

Export each as a React component with controllable animation state."""),

    ("image-optimization.md", "Master Next.js Image Optimization", ["nextjs", "images", "performance", "web-vitals"], "intermediate",
     """Optimize all images in my Next.js app for maximum performance.

Current situation: [DESCRIBE YOUR IMAGE USAGE]

Implement:
1. `next/image` for all images with correct `sizes` prop
2. Blur placeholder generation during build
3. Art direction: different crops for mobile vs desktop
4. Lazy loading with custom placeholder
5. Priority loading for above-the-fold images
6. CDN configuration for remote images
7. SVG handling (don't put SVGs through Image component)
8. Background images with CSS (when `next/image` doesn't fit)

Target: Largest Contentful Paint < 2.5s, zero layout shift from images."""),

    ("state-management-comparison.md", "Choose and Implement State Management", ["redux", "zustand", "jotai", "state"], "advanced",
     """My app needs state management for: [DESCRIBE YOUR STATE NEEDS].

Compare and implement with the RIGHT tool:
- **Local state**: useState/useReducer — when and how
- **Zustand**: global state for most apps — show full setup
- **Jotai**: atomic state — show atoms + derived atoms
- **Redux Toolkit**: when you need time-travel and devtools

For each, implement:
- Your specific state shape
- Actions/mutations
- Async operations (thunks/queries)
- React DevTools integration
- TypeScript types throughout

Recommendation: Which one fits my use case and why."""),

    ("css-grid-mastery.md", "Build Complex Layouts with CSS Grid", ["css", "grid", "layout", "advanced"], "advanced",
     """Build these complex real-world layouts using pure CSS Grid (no flexbox fallbacks):

1. **Magazine layout**: multi-column article with featured image spanning rows
2. **Dashboard layout**: collapsible sidebar + header + main + widget grid
3. **Holy grail layout**: header, footer, 3 columns, all full-height
4. **Masonry grid**: Pinterest-style variable height cards
5. **Calendar grid**: month view with events spanning multiple days
6. **Timeline**: alternating left-right with center line
7. **Pricing cards**: equal height, aligned features

For each: the HTML structure, the CSS Grid code, and an explanation of the non-obvious parts."""),

    ("component-testing.md", "Write Tests for React Components", ["testing", "react-testing-library", "jest", "vitest"], "intermediate",
     """Write comprehensive tests for my React components.

Components to test: [LIST YOUR COMPONENTS]

Testing patterns:
1. **Rendering**: does it render without crashing
2. **Props**: test all prop variations
3. **User interactions**: click, type, select using `userEvent`
4. **Async behavior**: loading states, data fetching (msw mocking)
5. **Accessibility**: axe-core integration
6. **Snapshots**: when they're useful vs harmful
7. **Custom hooks**: `renderHook` from RTL
8. **Context providers**: wrapping with providers in tests

Test organization: describe blocks, arrange-act-assert pattern."""),

    ("nextjs-middleware.md", "Master Next.js Middleware", ["nextjs", "middleware", "auth", "edge"], "advanced",
     """Implement powerful Next.js Middleware for [MY APP].

Use cases:
1. **Auth protection**: redirect unauthenticated users
2. **A/B testing**: randomly assign variant, persist in cookie
3. **Feature flags**: check flags and redirect or modify response
4. **Geo-blocking**: redirect based on country
5. **Rate limiting**: basic IP-based rate limit at the edge
6. **Localization**: detect language, redirect to locale subdirectory
7. **Bot detection**: block known scrapers
8. **Security headers**: CSP, HSTS, X-Frame-Options

Includes: `middleware.ts` + `matcher` config, performance tips (< 1ms execution budget)."""),

    ("real-time-collaboration.md", "Build Real-Time Collaboration Features", ["websockets", "yjs", "crdt", "collaboration"], "advanced",
     """Add Google Docs-style real-time collaboration to my app.

Feature: [DESCRIBE: collaborative text editing / whiteboard / spreadsheet / other]

Using: Yjs (CRDT library) + y-websocket

Implement:
1. Yjs document setup with your data type (Y.Text, Y.Map, Y.Array)
2. WebSocket provider setup with y-websocket
3. Awareness (cursor positions, user presence)
4. Undo/redo with collaborative history
5. Offline support (sync when reconnected)
6. Conflict resolution (automatic with CRDTs)
7. UI: show collaborator cursors/selections
8. Persistence: store Yjs document in database

Include the server setup (Node.js y-websocket server)."""),

    ("micro-frontend.md", "Set Up Micro-Frontend Architecture", ["micro-frontend", "module-federation", "webpack", "architecture"], "advanced",
     """Set up a Micro-Frontend architecture for [MY APP].

Using: Webpack Module Federation (or Vite equivalent)

Teams/domains:
- Host app (shell): [DESCRIPTION]
- Remote 1 ([TEAM NAME]): [DESCRIPTION]
- Remote 2 ([TEAM NAME]): [DESCRIPTION]

Implement:
1. Host app that dynamically loads remote modules
2. Shared dependencies configuration (React, ReactDOM)
3. Typed remote module loading with TypeScript
4. Error boundary for failed remote loads
5. Versioning strategy
6. Local development setup (all remotes running locally)
7. Deployment: each remote deployed independently

Show: how to share auth state between microfrontends."""),

    ("web-workers.md", "Offload Heavy Work to Web Workers", ["web-workers", "performance", "javascript", "concurrency"], "advanced",
     """Offload these CPU-intensive tasks to Web Workers:

Tasks: [DESCRIBE: image processing / data parsing / complex calculations / etc.]

Implement:
1. Worker setup with TypeScript (using Comlink for RPC-style API)
2. Main thread ↔ worker communication (with TypeScript types)
3. Transferable objects for large data (avoid copying)
4. Worker pool for parallel processing
5. Progress reporting from worker to main thread
6. Worker error handling and recovery
7. SharedArrayBuffer + Atomics for advanced use case
8. React integration: `useWorker` hook

Benchmark: show the before (main thread blocking) vs after."""),

    ("css-scroll-animations.md", "Create Scroll-Driven Animations", ["css", "scroll", "animations", "modern"], "intermediate",
     """Create scroll-driven animations using the modern CSS Scroll-driven Animations API.

Animations to build:
1. Progress bar that fills as user scrolls the page
2. Elements that fade/slide in as they enter the viewport
3. Parallax scrolling effect on hero image
4. Sticky header that shrinks/changes on scroll
5. Horizontal scroll carousel
6. Number counter that animates when scrolled into view
7. Reading time indicator

Using: `animation-timeline: scroll()` and `view()` — no JavaScript!
Include graceful degradation for unsupported browsers (Intersection Observer fallback)."""),

    ("typescript-generics.md", "Master TypeScript Generics for React", ["typescript", "generics", "react", "types"], "advanced",
     """Master TypeScript generics in the context of React development.

Build these generic utilities and components:

1. **Generic API hook**: `useApi<TData, TError>(url)` → `{data, error, loading}`
2. **Generic form**: `<Form<TValues>` with typed fields and typed submit handler
3. **Generic table**: `<DataTable<TRow>` with typed columns
4. **Generic select**: `<Select<TOption>` with typed options and onChange
5. **Generic context**: `createContext<TState>()` with typed provider
6. **Conditional types**: `DeepPartial<T>`, `DeepReadonly<T>`, `Nullable<T>`
7. **Mapped types**: transform any model for API vs UI vs form
8. **Template literal types**: typed route params

Each with TypeScript playground-ready examples."""),

    ("web-components.md", "Build Native Web Components", ["web-components", "custom-elements", "shadow-dom", "javascript"], "advanced",
     """Build production-ready Web Components (framework-agnostic).

Components to build:
1. `<my-button>` — accessible button with variants
2. `<my-modal>` — dialog with focus trap and backdrop
3. `<my-toast>` — notification system
4. `<my-tabs>` — accessible tab interface
5. `<my-accordion>` — expand/collapse sections

Each component must:
- Use Shadow DOM for style encapsulation
- Define a clean attribute/property API
- Fire custom events for parent communication
- Work in React, Vue, Angular, and vanilla HTML
- Be tree-shakeable when used in bundles
- Pass all ARIA requirements

Include TypeScript type declarations (.d.ts) for IDE support."""),

    ("react-native-components.md", "Build Cross-Platform React Native Components", ["react-native", "expo", "mobile", "cross-platform"], "intermediate",
     """Build these cross-platform React Native components using Expo.

Components:
1. Bottom Sheet modal (with gesture handling)
2. Pull-to-refresh list
3. Swipe-to-delete list item
4. Custom tab bar with animations
5. Image picker with camera + library options
6. Skeleton loading component

Each component must:
- Work on iOS and Android (handle platform differences)
- Use React Native Reanimated 3 for animations
- Support dark mode (useColorScheme)
- Have TypeScript props
- Not crash when permissions are denied"""),

    ("seo-optimization.md", "Implement Complete SEO for Next.js", ["seo", "nextjs", "metadata", "structured-data"], "intermediate",
     """Implement complete SEO for my Next.js 14 app.

App type: [DESCRIBE YOUR APP]
Key pages: [LIST IMPORTANT PAGES]

Implement:
1. Root metadata in `layout.tsx`
2. Dynamic metadata in each `page.tsx` using `generateMetadata`
3. Open Graph tags for social sharing
4. Twitter Card metadata
5. JSON-LD structured data (Organization, Article, Product, BreadcrumbList)
6. Sitemap generation (`app/sitemap.ts`)
7. Robots.txt (`app/robots.ts`)
8. Canonical URLs
9. Dynamic OG images using `next/og`
10. Internationalized SEO with `hreflang` for [LANGUAGES]"""),

    ("error-handling-patterns.md", "Master Frontend Error Handling", ["error-handling", "react", "typescript", "reliability"], "intermediate",
     """Implement comprehensive error handling for a React + TypeScript app.

Types of errors to handle:
1. **Network errors**: API down, timeout, no internet
2. **API errors**: 4xx responses with error details from server
3. **Validation errors**: map server validation to form fields
4. **JavaScript errors**: Error Boundary for unexpected crashes
5. **Async errors**: unhandled promise rejections
6. **Missing data**: null/undefined guards with fallbacks

For each:
- How to catch it
- What to show the user
- What to log (and how much detail)
- How to recover without page refresh

Include: a centralized error reporting service (Sentry or custom)."""),

    ("nextjs-auth.md", "Implement Authentication in Next.js", ["nextjs", "auth", "next-auth", "security"], "advanced",
     """Implement complete authentication for Next.js 14 App Router.

Using: Auth.js v5 (next-auth)

Providers: Email/Password + Google + GitHub

Implement:
1. Auth.js configuration with all providers
2. Database adapter (Prisma or Drizzle)
3. Session handling in Server Components
4. Protected routes with Middleware
5. Client-side auth state with `useSession`
6. Sign in / Sign up pages with beautiful UI
7. Email verification flow
8. Password reset flow
9. Account settings (change email, password, connect social)
10. Role-based access control (user, admin, moderator)"""),

    ("bundle-optimization.md", "Optimize Your JavaScript Bundle", ["performance", "webpack", "vite", "bundle-size"], "advanced",
     """Analyze and optimize my JavaScript bundle.

Current setup: [VITE/WEBPACK/NEXT.JS] with these dependencies: [LIST HEAVY DEPS]

Optimization strategies:
1. **Code splitting**: route-level, component-level lazy loading
2. **Tree shaking**: identify and fix failed tree shaking
3. **Dynamic imports**: heavy libraries (charts, PDFs, maps) loaded on demand
4. **Bundle analyzer**: setup and interpret `rollup-plugin-visualizer` output
5. **Compression**: gzip vs Brotli, when each applies
6. **Module deduplication**: fix multiple React versions
7. **Replace heavy packages**: suggest lighter alternatives
8. **CSS splitting**: per-route CSS bundles

Target: main bundle < 100KB gzipped."""),

    ("storybook-setup.md", "Set Up Storybook for Your Component Library", ["storybook", "components", "documentation", "testing"], "intermediate",
     """Set up Storybook 8 for my [React/Vue/Web Components] project.

Include:
1. Installation and initial config (`.storybook/main.ts`, `preview.ts`)
2. A story for each component variant (CSF3 format)
3. Controls (args) for interactive prop editing
4. Actions for event logging
5. Docs: auto-generated component documentation from TypeScript types
6. Dark mode addon
7. Accessibility addon (axe-core integration)
8. Viewport addon for responsive testing
9. Chromatic setup for visual regression testing
10. Deploy to GitHub Pages

Also: best practices for story organization and naming."""),

    ("react-performance.md", "Optimize React Performance", ["react", "performance", "memo", "optimization"], "advanced",
     """Profile and optimize the performance of my React app.

Current issues: [DESCRIBE: slow renders, jank, high memory usage]

Optimization techniques:
1. **React.memo**: when it helps vs when it's counterproductive
2. **useMemo and useCallback**: common mistakes and correct usage
3. **React DevTools Profiler**: how to read the flame chart
4. **Context optimization**: prevent unnecessary re-renders
5. **Virtualization**: react-virtual for long lists
6. **Code splitting**: lazy() + Suspense for routes and heavy components
7. **React 18 features**: startTransition, useDeferredValue
8. **Avoid reconciliation**: stable keys, stable references

Show: before/after examples with render count measurements."""),

    ("tanstack-router.md", "Set Up TanStack Router", ["tanstack-router", "routing", "typescript", "react"], "intermediate",
     """Set up TanStack Router v1 for my React app.

Routes needed: [LIST YOUR ROUTES AND THEIR PARAMS]

Implement:
1. File-based routing setup with code generation
2. Type-safe navigation (`Link` and `useNavigate` with typed params)
3. Nested routes and layouts
4. Route loaders (data fetching before rendering)
5. Route actions (form submissions)
6. Search params (typed with Zod validation)
7. Protected routes with `beforeLoad`
8. 404 and error pages
9. Route transitions
10. Devtools integration

Show the complete router setup and 3 example routes."""),

    ("css-custom-properties.md", "Master CSS Custom Properties", ["css", "variables", "theming", "modern"], "intermediate",
     """Master CSS custom properties for building a robust theming system.

Implement:
1. **Design tokens**: color, spacing, typography as custom properties
2. **Component-level overrides**: scoped custom properties
3. **Theme switching**: class-based light/dark/custom themes
4. **JavaScript integration**: read/write custom properties from JS
5. **Fallback values**: `var(--color, #fallback)` patterns
6. **@property rule**: typed custom properties with animation support
7. **Inheritance tricks**: cascade manipulation
8. **Media query integration**: responsive design token overrides

Build a complete theming system for a SaaS dashboard with these techniques."""),

    ("websocket-ui.md", "Build a WebSocket-Powered Real-Time UI", ["websockets", "react", "real-time", "ui"], "intermediate",
     """Build a real-time dashboard UI using WebSockets.

Data to display in real-time: [DESCRIBE YOUR DATA: stock prices / server metrics / chat messages / etc.]

React implementation:
1. `useWebSocket` custom hook with reconnection logic
2. Connection status indicator (connecting/connected/disconnected)
3. Message queue for messages received while UI is updating
4. Throttle incoming messages (max 60fps updates)
5. Optimistic local updates
6. Reconnect with exponential backoff
7. Heartbeat/ping-pong keepalive

UI components: animated number counters, live charts, real-time feed."""),

    ("stripe-frontend.md", "Integrate Stripe Payment UI", ["stripe", "payments", "react", "frontend"], "intermediate",
     """Build the frontend payment UI for a Stripe integration.

Using: @stripe/react-stripe-js + @stripe/stripe-js

Implement:
1. **Payment form**: Card Element with custom styling to match brand
2. **Address collection**: Address Element
3. **Payment Request Button**: Apple Pay / Google Pay
4. **3D Secure handling**: redirect flow
5. **Error messages**: Stripe error code → user-friendly message
6. **Loading states**: during payment processing
7. **Success page**: order confirmation with details
8. **Subscription UI**: plan selection, current plan, upgrade/downgrade

Include: the backend API routes needed to create Payment Intents."""),

    ("three-js-scene.md", "Build a 3D Scene with Three.js and React", ["three-js", "react-three-fiber", "3d", "graphics"], "advanced",
     """Build a 3D interactive scene using React Three Fiber (Three.js for React).

Scene: [DESCRIBE WHAT YOU WANT: product viewer / animated logo / data viz / game-like scene]

Implement:
1. Scene setup: canvas, camera, lighting (ambient + directional + point)
2. 3D models: either primitive geometry or GLTF model loading
3. Materials: PBR materials with metalness/roughness
4. Animations: useFrame loop, GSAP timeline
5. Interactivity: onClick, onHover, raycasting
6. Post-processing: bloom, depth of field (using @react-three/postprocessing)
7. Performance: instancing, LOD, frustum culling
8. Responsive canvas

Include: Leva controls for tweaking parameters in development."""),

    ("react-pdf.md", "Generate PDFs from React Components", ["pdf", "react", "react-pdf", "documents"], "intermediate",
     """Generate professional PDFs from React components.

Document to generate: [DESCRIBE: invoice / report / certificate / contract]

Using: @react-pdf/renderer

Implement:
1. PDF document with pages, header, footer
2. Tables with borders and alternating row colors
3. Images and logos
4. Typography with custom fonts (load from URL)
5. Page numbers and total pages
6. Dynamic content from data
7. Download button that triggers PDF generation
8. Preview the PDF in a modal before downloading

Also: email delivery option using the PDF as a Buffer attachment."""),

    ("progressive-loading.md", "Implement Progressive Loading Patterns", ["performance", "loading", "ux", "react"], "intermediate",
     """Implement progressive loading to make my app feel instant.

Current slow points: [DESCRIBE WHAT'S SLOW]

Patterns to implement:
1. **Skeleton screens**: anatomically correct placeholder for each section
2. **Optimistic UI**: show result before server confirms
3. **Suspense boundaries**: granular loading states per section
4. **Streaming SSR** (Next.js): progressive HTML from server
5. **Prefetching**: hover to preload next page data
6. **Stale-while-revalidate**: show old data while fetching new
7. **Critical CSS inlining**: above-the-fold CSS in `<head>`
8. **Resource hints**: `<link rel="prefetch|preload|preconnect">`

Each pattern with before (jarring UX) and after (smooth UX) code."""),

    ("markdown-editor.md", "Build a Rich Markdown Editor", ["editor", "markdown", "react", "ui"], "advanced",
     """Build a rich Markdown editor like Notion or Hashnode's editor.

Using: Tiptap (or ProseMirror directly for maximum control)

Features:
1. Toolbar: bold, italic, code, headings, lists, blockquote, link, image
2. Keyboard shortcuts: ⌘B for bold, ⌘K for link, etc.
3. Slash commands: type `/` to insert blocks
4. Drag and drop blocks to reorder
5. Auto-link: paste URL → detect and convert
6. Code blocks with syntax highlighting
7. Real-time Markdown preview (split view)
8. Export to HTML and raw Markdown
9. Mention system: @username autocomplete
10. Auto-save with debounce"""),

    ("auth-context.md", "Build a Complete Auth Context in React", ["react", "auth", "context", "typescript"], "intermediate",
     """Build a complete authentication context for a React SPA.

Backend: [REST API / GraphQL / Supabase / Firebase]

Implement:
1. `AuthContext` with: user, isAuthenticated, isLoading, error
2. `useAuth()` hook
3. `AuthProvider` that persists session (localStorage + refresh token)
4. Protected Route component
5. `login()`, `logout()`, `register()`, `refreshToken()` functions
6. Auto-refresh tokens before expiry
7. Handle 401 errors globally → redirect to login
8. Role checking: `usePermission('admin')` hook
9. Redirect to original URL after login

TypeScript throughout with proper typing of user object."""),

    ("responsive-images.md", "Master Responsive Images", ["images", "responsive", "performance", "html"], "intermediate",
     """Implement responsive images correctly for [MY WEBSITE/APP].

Use cases: [LIST: hero images / product photos / avatars / blog thumbnails]

Implement:
1. `srcset` + `sizes` for resolution switching
2. `<picture>` element for art direction (different crops at different sizes)
3. WebP + AVIF with JPEG fallback using `<source type>`
4. Lazy loading with `loading="lazy"` + blurred placeholder
5. `fetchpriority="high"` for LCP image
6. Aspect ratio boxes to prevent layout shift
7. Next.js Image component equivalent for pure HTML
8. CSS background images: use `image-set()` for responsive backgrounds

Show: the generated HTML for each scenario."""),

    ("offline-first.md", "Build an Offline-First Web App", ["pwa", "offline", "service-worker", "indexeddb"], "advanced",
     """Build an offline-first version of my web app.

App type: [DESCRIBE YOUR APP AND ITS DATA]

Implement:
1. **Service Worker**: cache strategies per resource type
2. **IndexedDB**: local database for app data (using Dexie.js for nice API)
3. **Sync**: queue actions while offline, sync when reconnected (Background Sync API)
4. **Conflict resolution**: last-write-wins vs user choice
5. **Offline UI**: banner indicating offline status, disabled features that need network
6. **Optimistic offline mutations**: update local DB → sync to server
7. **Cache management**: storage quota handling, cache invalidation

Test with Chrome DevTools: offline mode + throttling."""),

    ("font-optimization.md", "Optimize Web Fonts for Performance", ["fonts", "performance", "css", "web-vitals"], "intermediate",
     """Optimize web fonts for performance and aesthetics in my project.

Current fonts: [LIST YOUR FONTS]

Implement:
1. Self-hosting fonts (woff2 format, subset to used characters)
2. `@font-face` with `font-display: swap` and correct descriptors
3. Preloading critical fonts in `<head>`
4. Variable fonts: one file for all weights
5. System font fallback stack that minimizes layout shift
6. `size-adjust` to match system font metrics to web font
7. Next.js `next/font` for zero-CLS font loading
8. Subsetting: only include characters you use (pyftsubset)

Target: < 30KB total font payload, CLS = 0."""),

    ("headless-components.md", "Build Headless Components with Radix UI", ["radix-ui", "headless", "accessibility", "react"], "intermediate",
     """Build a design system using Radix UI primitives (headless, fully accessible components).

Components to build styled versions of:
1. Dialog / Modal
2. Dropdown Menu
3. Select
4. Checkbox + Radio
5. Slider
6. Switch / Toggle
7. Tooltip
8. Popover
9. Toast (using Radix Toast)
10. Navigation Menu

For each:
- Custom CSS styling (no Tailwind)
- All accessibility built-in from Radix
- TypeScript props extending Radix primitives
- Storybook story with all variants"""),

    ("web-animation-api.md", "Master the Web Animations API", ["waapi", "animations", "javascript", "performance"], "advanced",
     """Master the Web Animations API (WAAPI) — the native browser animation engine.

Build:
1. Basic animations: `element.animate(keyframes, options)`
2. Playback controls: play, pause, reverse, finish, cancel
3. Animation groups: parallel vs sequential
4. Spring physics: custom easing with `linear()` function
5. Scroll-linked animations using WAAPI
6. Reusable animation functions: `fadeIn(el, options)`, `slideIn(el, options)`
7. React integration: `useAnimation()` hook wrapping WAAPI
8. Performance: animate on compositor thread only (transform, opacity)
9. Debugging with Chrome DevTools Animation panel

Migrate: show how to replace a GSAP animation with WAAPI."""),

    ("typescript-utility-types.md", "Build a TypeScript Utility Type Library", ["typescript", "utility-types", "generics", "types"], "advanced",
     """Build a comprehensive TypeScript utility type library for frontend development.

Implement these utility types with explanations:

**Object manipulation**:
- `DeepPartial<T>`, `DeepRequired<T>`, `DeepReadonly<T>`
- `Flatten<T>`, `Merge<T, U>`, `Overwrite<T, U>`
- `OmitNever<T>`, `PickByValue<T, V>`

**Function types**:
- `AsyncReturnType<F>`, `PromiseType<P>`
- `Parameters<F>`, `ReturnType<F>` (built-in, but show composition)

**String types**:
- `CamelCase<S>`, `KebabCase<S>`, `SnakeCase<S>`
- `Split<S, D>`, `Join<T, D>`

**React-specific**:
- `PropsWithChildren`, `ComponentProps`, `ElementType`
- `StrictOmit<T, K>` (preserves discriminated unions)

Each type with 2 usage examples."""),

    ("design-tokens-pipeline.md", "Build a Design Tokens Pipeline", ["design-tokens", "style-dictionary", "theming", "build"], "advanced",
     """Build a design tokens pipeline from Figma to code.

Using: Style Dictionary

Source tokens (JSON format):
- Colors, typography, spacing, shadows, border radius, breakpoints

Output targets:
1. CSS custom properties file
2. JavaScript/TypeScript ES module
3. SCSS variables
4. iOS Swift color extensions
5. Android XML resources
6. Figma plugin JSON format

Build pipeline:
- Token transformation (snake_case → camelCase, px → rem)
- Theme support (light/dark/brand themes)
- Documentation auto-generation
- CI integration: fail if tokens are invalid

Include: the Style Dictionary config and npm build script."""),

    ("shadcn-custom.md", "Customize and Extend shadcn/ui", ["shadcn", "radix", "react", "design-system"], "intermediate",
     """Extend shadcn/ui with custom components and theme customization.

My app's design: [DESCRIBE BRAND: colors, roundness, feel]

Implement:
1. Custom CSS variables for your brand in `globals.css`
2. Custom `tailwind.config.ts` theme extension
3. New component variants for existing shadcn components
4. 3 completely new components built in the shadcn pattern:
   - [Component 1]
   - [Component 2]
   - [Component 3]
5. Custom command palette (extend shadcn Command)
6. Data table (extend shadcn Table + TanStack Table)
7. Charts (extend shadcn Chart + Recharts)

Output: drop-in components ready for your `components/ui/` folder."""),

    ("react-18-features.md", "Master React 18 Features", ["react-18", "concurrent", "suspense", "transitions"], "advanced",
     """Master React 18 features for better performance and UX.

Features to implement:
1. **`startTransition`**: mark state updates as non-urgent (keep UI responsive)
2. **`useDeferredValue`**: defer expensive renders (search results)
3. **Concurrent Suspense**: show old content while loading new
4. **`useId`**: stable IDs for accessibility across server/client
5. **Automatic batching**: understand when React 18 batches vs not
6. **Selective hydration**: SSR streaming with Suspense boundaries
7. **`use()` hook** (experimental): unwrap promises and context
8. **React Server Components**: server-only component tree

Show: real-world examples where each feature meaningfully improves UX."""),

    ("style-guide.md", "Create a Living Style Guide", ["style-guide", "components", "documentation", "design"], "intermediate",
     """Create a living style guide (in-app) for my component library.

Build a `/style-guide` route with sections:
1. **Colors**: all design tokens with hex values and usage guidance
2. **Typography**: all type scales, weights, with live examples
3. **Spacing**: visual spacing scale
4. **Icons**: all available icons with copy-name-to-clipboard
5. **Components**: interactive demos of every component
   - Button (all variants + sizes + states)
   - Form elements
   - Cards, modals, tooltips, etc.
6. **Do/Don't**: design rules with visual examples

Self-contained page that works without any routing library."""),
]

for filename, title, tags, difficulty, prompt_text in FRONTEND_PROMPTS:
    models = ["claude-haiku-3-5", "claude-sonnet-4", "claude-opus-4", "claude-fable-5"]
    content = f"""---
title: "{title}"
category: frontend-dev
models: [{', '.join(models)}]
tags: [{', '.join(tags)}]
difficulty: {difficulty}
author: community
tested: true
---

## 🎯 Prompt

```
{prompt_text.strip()}
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
"""
    write(cat / filename, content)

print(f"\n🎉 Done writing prompts for Categories 01 and 02!")
print(f"Run this script again after adding more categories to the PROMPTS dict.")
