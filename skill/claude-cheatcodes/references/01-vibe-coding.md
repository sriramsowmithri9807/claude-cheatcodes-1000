# 01-vibe-coding

Rapid builds from an idea: scaffolds, landing pages, UI from screenshots, SaaS blueprints, common app features.

56 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Build a ChatGPT-Style Chatbot UI

**id:** `01-vibe-coding/ai-chatbot-ui` · **Difficulty:** intermediate · **Tags:** ai, chat, react, streaming

````text
Build a beautiful ChatGPT-style chatbot UI that connects to an AI API.

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

Tech: React + TypeScript. API: Claude API or OpenAI compatible.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Add AI-Powered Search to Your App

**id:** `01-vibe-coding/ai-powered-search` · **Difficulty:** advanced · **Tags:** search, embeddings, vector-db, ai

**Placeholders:** [DESCRIBE YOUR DATA AND TECH STACK]

````text
Add semantic AI-powered search to my app.

Current setup: [DESCRIBE YOUR DATA AND TECH STACK]

Implement:
1. **Embedding generation** using Claude API (or OpenAI embeddings as fallback)
2. **Vector storage** with pgvector (PostgreSQL) or Pinecone
3. **Indexing pipeline**: ingest documents → chunk → embed → store
4. **Search API**: query → embed → vector similarity search → rerank
5. **Frontend search bar** with debouncing, loading states, highlighted results
6. **Hybrid search**: combine keyword (BM25) + semantic for better results

Performance target: < 500ms search latency for 100k documents.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Micro-Animation System

**id:** `01-vibe-coding/animation-library` · **Difficulty:** intermediate · **Tags:** animations, css, framer-motion, ux

````text
Build a reusable micro-animation system for my React app.

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

Performance: CSS transforms only (no layout-triggering properties). 60fps target.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an Instant Mock API Server

**id:** `01-vibe-coding/api-mockup-server` · **Difficulty:** beginner · **Tags:** api, mock, testing, json-server

**Placeholders:** [DESCRIBE YOUR API NEEDS / PASTE OPENAPI SPEC]

````text
Build me an instant mock API server for my frontend that simulates:

[DESCRIBE YOUR API NEEDS / PASTE OPENAPI SPEC]

Use Express.js + TypeScript. Include:
- All CRUD endpoints with realistic fake data
- Simulated network delay (100–500ms random)
- Error simulation (5% chance of 500 error)
- CORS configured for localhost
- Authentication simulation (any Bearer token accepted)
- Pagination support on list endpoints
- Request/response logging middleware

Also include a `db.json` with 20 realistic seed records per entity.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Full App from One Sentence

**id:** `01-vibe-coding/app-from-one-sentence` · **Difficulty:** intermediate · **Tags:** fullstack, rapid-prototype, mvp

**Placeholders:** [ONE SENTENCE DESCRIPTION]

````text
You are a 10x developer building an MVP in record time. I want to build: [ONE SENTENCE DESCRIPTION].

Produce:
1. A folder structure for this app
2. A tech stack recommendation with reasoning
3. The complete code for the core feature (the ONE thing that makes this app useful)
4. A `README.md` with setup instructions
5. A list of 5 next features to add after the MVP

Keep the code clean, working, and minimal. No over-engineering. Ship it.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Eliminate Boilerplate from Any Codebase

**id:** `01-vibe-coding/boilerplate-eliminator` · **Difficulty:** intermediate · **Tags:** refactor, dry, clean-code, abstraction

**Placeholders:** [PASTE YOUR CODE]

````text
You are a refactoring expert. Analyze this code:

[PASTE YOUR CODE]

Identify and eliminate ALL boilerplate:
1. List every repeated pattern you find (with line numbers)
2. Create reusable abstractions for each (utility functions, hooks, HOCs, base classes)
3. Rewrite the original code using your abstractions
4. Calculate the lines of code reduction
5. Explain why each abstraction improves maintainability

Follow the DRY principle without over-abstracting. The goal is clarity, not cleverness.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Scaffold a Chrome Extension

**id:** `01-vibe-coding/chrome-extension-scaffold` · **Difficulty:** intermediate · **Tags:** chrome-extension, javascript, browser, web

**Placeholders:** [DESCRIBE WHAT IT DOES]

````text
Build a complete Chrome Extension that: [DESCRIBE WHAT IT DOES].

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

Also include: instructions for loading in Chrome developer mode.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Scaffold a CLI Tool

**id:** `01-vibe-coding/cli-tool-scaffold` · **Difficulty:** intermediate · **Tags:** cli, node, typescript, tooling

**Placeholders:** [DESCRIPTION], [TOOL-NAME]

````text
Build a Node.js CLI tool called `[TOOL-NAME]` that does: [DESCRIPTION].

Implement:
- `commander.js` for argument parsing
- Subcommands: `init`, `run`, `config`, `--help`, `--version`
- Colorized output with `chalk`
- Interactive prompts with `inquirer`
- Configuration file support (~/.toolname/config.json)
- Progress indicators with `ora`
- Proper exit codes

Include: `package.json` (with `bin` field), `tsconfig.json`, entry point, and a `README.md` with usage examples.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Clone a UI from a Description

**id:** `01-vibe-coding/clone-ui-from-description` · **Difficulty:** beginner · **Tags:** html, css, clone, ui

**Placeholders:** [DESCRIBE THE UI: colors, layout, components, feel]

````text
You are a pixel-perfect front-end engineer. Recreate the following UI from this description:

[DESCRIBE THE UI: colors, layout, components, feel]

Output a single self-contained HTML file with embedded CSS. Make it look as close to the description as possible. Use:
- CSS variables for colors
- Flexbox/Grid for layout
- Smooth hover animations
- Google Fonts for typography
No images needed — use CSS shapes, gradients, or emoji placeholders.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Solve Coding Challenges with Explanation

**id:** `01-vibe-coding/code-challenge-solver` · **Difficulty:** intermediate · **Tags:** algorithms, leetcode, interviews, problem-solving

**Placeholders:** [PASTE THE PROBLEM STATEMENT]

````text
You are an expert competitive programmer and technical interviewer. Solve this problem:

[PASTE THE PROBLEM STATEMENT]

Provide:
1. **Brute force solution** with time/space complexity
2. **Optimal solution** with explanation of the key insight
3. **Step-by-step walkthrough** on the example inputs
4. **Edge cases** to handle and why
5. **TypeScript/Python code** (clean, commented)
6. **Follow-up questions** an interviewer might ask and how to answer them

Don't just give code — teach me to think about this type of problem.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Intelligently Split a Large File

**id:** `01-vibe-coding/code-splitter` · **Difficulty:** intermediate · **Tags:** refactor, architecture, clean-code, modules

**Placeholders:** [PASTE FILE OR DESCRIBE IT]

````text
This file has grown too large: [PASTE FILE OR DESCRIBE IT].

Refactor it by:
1. Identifying all distinct concerns/responsibilities in this file
2. Proposing a new folder structure with one file per concern
3. Writing each split file with proper imports/exports
4. Updating the original file to import from the new modules
5. Identifying any circular dependencies to watch for

Follow: Single Responsibility Principle. Each file should have exactly one reason to change.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Generate a Complete Color Palette from One Color

**id:** `01-vibe-coding/color-palette-generator` · **Difficulty:** beginner · **Tags:** design, colors, css, ui

**Placeholders:** [HEX COLOR]

````text
I have a brand color: [HEX COLOR].

Generate a complete design system color palette:
1. Primary scale (50–950, 10 shades)
2. Neutral/gray scale (50–950)
3. Semantic colors: success, warning, error, info (each with light/default/dark)
4. Dark mode equivalents for each semantic color

Output as:
- CSS custom properties
- JavaScript/TypeScript object
- Tailwind CSS config extension

Also provide WCAG contrast ratios for text-on-background combinations and flag any accessibility issues.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Reverse-Engineer a Component from Description

**id:** `01-vibe-coding/component-from-screenshot` · **Difficulty:** intermediate · **Tags:** react, components, reverse-engineer, ui

**Placeholders:** [DESCRIBE THE COMPONENT IN DETAIL: layout, colors, interactions, animations]

````text
Reverse-engineer this UI component from my description:

[DESCRIBE THE COMPONENT IN DETAIL: layout, colors, interactions, animations]

Build it as:
- React + TypeScript functional component
- Self-contained (no external UI library dependencies)
- CSS Module for styles
- Full keyboard accessibility (ARIA, focus management)
- Responsive
- Storybook story showing all states
- Props with sensible defaults

Name the component `[ComponentName]` and export it from `index.ts`.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Convert Figma-Style Design Spec to Code

**id:** `01-vibe-coding/convert-design-to-code` · **Difficulty:** intermediate · **Tags:** figma, design-to-code, react, css

**Placeholders:** [PASTE FIGMA SPECS / DESIGN TOKENS / DESIGN DESCRIPTION]

````text
You are an expert at converting design specifications to pixel-perfect code. Here is the design spec:

[PASTE FIGMA SPECS / DESIGN TOKENS / DESIGN DESCRIPTION]

Convert to:
- React + TypeScript functional components
- CSS Modules with exact spacing, colors, and typography from the spec
- Responsive breakpoints: mobile (< 768px), tablet (768–1024px), desktop (> 1024px)
- Smooth transitions for interactive states (hover, focus, active, disabled)
- Accessibility: proper ARIA roles, focus indicators, keyboard navigation
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Perfect Dark Mode

**id:** `01-vibe-coding/dark-mode-implementation` · **Difficulty:** intermediate · **Tags:** dark-mode, theming, css, react

````text
Implement a perfect dark mode system for my [React/Next.js/Vue] app.

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

Include the Next.js specific FOUC prevention script.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Create a Complete Design Token System

**id:** `01-vibe-coding/design-system-tokens` · **Difficulty:** intermediate · **Tags:** design-tokens, css, design-system, theming

**Placeholders:** [TYPE OF APP: SaaS/e-commerce/dashboard/marketing]

````text
Create a production-grade design token system for a [TYPE OF APP: SaaS/e-commerce/dashboard/marketing].

Include all categories:
- **Colors**: brand, neutral, semantic (success/warning/error/info), dark mode variants
- **Typography**: font families, sizes (scale), weights, line heights, letter spacing
- **Spacing**: 4px base grid, scale from 0 to 96
- **Border radius**: sm/md/lg/full
- **Shadows**: 5 levels
- **Breakpoints**: xs/sm/md/lg/xl/2xl
- **Z-index**: named layers (modal, tooltip, dropdown, sticky)
- **Animation**: duration, easing curves

Output as: CSS custom properties, JavaScript ES module, and Figma-ready JSON (Style Dictionary format).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Up Bulletproof Environment Config

**id:** `01-vibe-coding/env-config-management` · **Difficulty:** intermediate · **Tags:** config, environment, secrets, devops

````text
Set up bulletproof environment configuration for my Node.js/Next.js app.

Implement:
1. `env.ts` — typed env validation using Zod (crash on startup if invalid)
2. `.env.example` with all variables documented
3. `.env.local`, `.env.staging`, `.env.production` structure
4. GitHub Actions secrets setup guide
5. Docker environment file handling
6. How to rotate secrets without downtime
7. Which variables are safe to commit vs must be secret

Never let a missing env variable cause a silent bug in production again.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Production Error Boundary System

**id:** `01-vibe-coding/error-boundary-system` · **Difficulty:** intermediate · **Tags:** react, error-handling, reliability, monitoring

````text
Build a comprehensive error boundary system for a React app.

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

TypeScript, works with React 18+ (concurrent mode safe).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Simple Feature Flag System

**id:** `01-vibe-coding/feature-flag-system` · **Difficulty:** intermediate · **Tags:** feature-flags, backend, typescript, devops

````text
Build a lightweight feature flag system for my Node.js app.

Requirements:
- Store flags in a JSON file (for simplicity) with live reload
- Types: boolean, percentage rollout, user-segment targeting
- SDK: `isEnabled(flagName, userId?)` function
- Admin API: GET/POST/PATCH flags
- React hook: `useFeatureFlag(name)` for frontend
- Audit log: who changed what flag and when

Keep it simple enough to understand in 10 minutes, powerful enough to use in production.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Generate Realistic Fake Data for Your App

**id:** `01-vibe-coding/generate-fake-data` · **Difficulty:** beginner · **Tags:** testing, mock-data, faker, seed

**Placeholders:** [PASTE YOUR DATABASE SCHEMA OR TYPESCRIPT TYPES]

````text
Generate realistic seed data for my app. Here's the data schema:

[PASTE YOUR DATABASE SCHEMA OR TYPESCRIPT TYPES]

Produce:
1. 20 realistic, diverse sample records (not just "John Doe" and "test@test.com")
2. A JavaScript/TypeScript seed file using this data
3. A Faker.js script that can generate unlimited records following these patterns
4. Edge cases to test: empty fields, long strings, special characters, international names/addresses

Make the fake data feel real — realistic names from diverse cultures, real-looking addresses, plausible dates.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Up a Professional Git Workflow

**id:** `01-vibe-coding/git-workflow-setup` · **Difficulty:** beginner · **Tags:** git, workflow, branching, ci

**Placeholders:** [PROJECT TYPE]

````text
Set up a professional Git workflow for my team working on [PROJECT TYPE].

Provide:
1. Branching strategy (GitFlow vs trunk-based, with justification for my team size)
2. Commit message convention (Conventional Commits) with examples
3. Pre-commit hooks (`.husky/` + `lint-staged` config)
4. PR/MR template (`.github/pull_request_template.md`)
5. Branch protection rules to configure on GitHub
6. `commitlint.config.js` configuration
7. `CHANGELOG.md` automation with `standard-version`
8. Git aliases cheat sheet for the team
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Design a GraphQL API Schema-First

**id:** `01-vibe-coding/graphql-schema-first` · **Difficulty:** advanced · **Tags:** graphql, api, schema, typescript

**Placeholders:** [YOUR APP]

````text
You are a GraphQL expert. Design a GraphQL API for: [YOUR APP].

Schema-first approach:
1. Complete GraphQL SDL schema (all types, queries, mutations, subscriptions)
2. TypeScript codegen config (using GraphQL Code Generator)
3. Resolvers implementation (Node.js + Apollo Server)
4. DataLoader setup for N+1 prevention
5. Authentication/authorization in resolvers
6. Error handling with custom error types
7. Example queries in GraphQL Playground format
8. Performance considerations for each resolver
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Hackathon Project Starter

**id:** `01-vibe-coding/hackathon-starter` · **Difficulty:** intermediate · **Tags:** hackathon, rapid-prototype, fullstack, starter

**Placeholders:** [IDEA]

````text
I'm starting a hackathon in 1 hour. My project idea: [IDEA]. Time limit: [X hours].

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

Start with the complete `npx create-next-app` command and all setup steps.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Up Internationalization (i18n)

**id:** `01-vibe-coding/i18n-setup` · **Difficulty:** intermediate · **Tags:** i18n, localization, next-intl, react-i18next

**Placeholders:** [ADD MORE]

````text
Set up complete internationalization for my [React/Next.js] app.

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

Provide 50 sample translation strings across 3 languages.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Turn an Idea into a Landing Page

**id:** `01-vibe-coding/idea-to-landing-page` · **Difficulty:** beginner · **Tags:** html, css, js, landing-page

**Placeholders:** [INSERT YOUR IDEA]

````text
You are a creative full-stack developer. I have a startup idea: [INSERT YOUR IDEA].
Turn it into a complete, beautiful single-page landing page with:
- Hero section with a catchy headline and sub-headline
- 3 feature/benefit sections with icons (use emoji icons)
- A pricing section with 3 tiers (Free, Pro, Enterprise)
- A FAQ section with 5 Q&As
- A footer with social links and copyright
Use pure HTML, CSS, and vanilla JS. Make it modern, dark-mode, with gradient accents. No external libraries except Google Fonts (Inter). Make it mobile-responsive.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Validate a Product Idea with Claude

**id:** `01-vibe-coding/idea-validator` · **Difficulty:** beginner · **Tags:** product, validation, startup, research

**Placeholders:** [YOUR IDEA]

````text
Act as an experienced product manager and startup advisor. Validate this idea: [YOUR IDEA].

Provide:
1. **Market size estimate** (TAM/SAM/SOM)
2. **3 strongest reasons this could work**
3. **3 biggest risks that could kill it**
4. **Competitor landscape** (direct and indirect)
5. **The riskiest assumption** to test first
6. **A 2-week validation experiment** I can run with no code
7. **Verdict**: Build it / Don't build it / Build something adjacent

Be brutally honest. Don't sugarcoat.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Complete Image Upload System

**id:** `01-vibe-coding/image-upload-system` · **Difficulty:** intermediate · **Tags:** uploads, storage, react, backend

**Placeholders:** [YOUR STACK]

````text
Build a complete image upload and management system.

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

Include: TypeScript types, error states, and loading UX.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Write a Production Incident Postmortem

**id:** `01-vibe-coding/incident-postmortem` · **Difficulty:** intermediate · **Tags:** postmortem, devops, reliability, documentation

**Placeholders:** [PASTE: incident timeline, affected systems, errors, metrics]

````text
You are an SRE writing a blameless postmortem. Here are the incident details:

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

Blameless tone throughout.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Add a Keyboard Shortcuts System

**id:** `01-vibe-coding/keyboard-shortcuts` · **Difficulty:** intermediate · **Tags:** accessibility, keyboard, ux, productivity

````text
Add a comprehensive keyboard shortcut system to my React app.

Implement:
1. Global shortcut registry with conflict detection
2. Context-aware shortcuts (active only in certain components)
3. `useKeyboardShortcut(keys, handler, options)` hook
4. Shortcuts help modal (triggered by `?` key) showing all active shortcuts
5. Customizable shortcuts saved to user preferences
6. Visual shortcut hints on buttons/menu items (like Notion/Linear)
7. Sequential shortcuts (Vim-style: `g` then `h` = go home)
8. Platform-aware: show ⌘ on Mac, Ctrl on Windows

Include: escape hatch for when user is typing in an input.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Blueprint a Micro-SaaS in a Weekend

**id:** `01-vibe-coding/micro-saas-blueprint` · **Difficulty:** intermediate · **Tags:** saas, startup, monetization, product

**Placeholders:** [YOUR IDEA]

````text
Design a complete Micro-SaaS blueprint for: [YOUR IDEA].

Include:
1. **Landing page copy** (headline, subheadline, 3 features, CTA)
2. **Pricing strategy** with 3 tiers and justification
3. **Tech stack** (keep it boring and proven)
4. **Database schema** for the core entities
5. **Auth flow** (use Clerk/Auth0/Supabase Auth)
6. **Payment integration** (Stripe checkout + webhooks)
7. **Week 1 launch checklist** (what to build, what to skip)
8. **First 10 customers acquisition strategy**

Budget: $0 infra cost at launch. Target: profitable within 30 days.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Up a Professional Monorepo

**id:** `01-vibe-coding/monorepo-setup` · **Difficulty:** advanced · **Tags:** monorepo, turborepo, pnpm, nx, architecture

**Placeholders:** [LIST YOUR APPS AND PACKAGES]

````text
Set up a professional monorepo for a project with: [LIST YOUR APPS AND PACKAGES].

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
- CI pipeline that only runs affected packages
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Design an n8n Automation Workflow

**id:** `01-vibe-coding/n8n-automation-workflow` · **Difficulty:** beginner · **Tags:** automation, n8n, no-code, workflow

**Placeholders:** [DESCRIBE YOUR AUTOMATION]

````text
Design a complete n8n automation workflow for: [DESCRIBE YOUR AUTOMATION].

Provide:
1. The complete workflow as a JSON export (importable into n8n)
2. Step-by-step explanation of each node
3. Error handling nodes and what they do
4. Webhook triggers and their configuration
5. Environment variables to configure
6. Testing instructions

If n8n can't do part of it, suggest a custom Code node solution.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an In-App Notification System

**id:** `01-vibe-coding/notification-system` · **Difficulty:** advanced · **Tags:** notifications, react, backend, real-time

````text
Build a complete in-app notification system.

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

Include database migration and the complete API + UI code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Generate an OpenAPI 3.1 Spec for Your API

**id:** `01-vibe-coding/open-api-spec` · **Difficulty:** intermediate · **Tags:** openapi, swagger, api-docs, rest

**Placeholders:** [DESCRIBE YOUR API: endpoints, auth method, main entities]

````text
Generate a complete OpenAPI 3.1 specification for my API:

[DESCRIBE YOUR API: endpoints, auth method, main entities]

Include:
- All paths with GET/POST/PUT/PATCH/DELETE where appropriate
- Request bodies with JSON Schema validation
- Response schemas for 200, 400, 401, 403, 404, 500
- Security schemes (Bearer JWT or API Key)
- Tags for grouping
- Examples for every endpoint
- Reusable components ($ref schemas)

Output as valid YAML that can be imported into Swagger UI or Postman.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Audit and Fix App Performance

**id:** `01-vibe-coding/performance-audit` · **Difficulty:** advanced · **Tags:** performance, optimization, lighthouse, web-vitals

**Placeholders:** [PASTE: Lighthouse report, Web Vitals, bundle size report, or description of slowness]

````text
You are a web performance expert. Here is my app's performance data:

[PASTE: Lighthouse report, Web Vitals, bundle size report, or description of slowness]

Provide:
1. **Diagnosis**: Root cause of each performance issue
2. **Quick wins** (fixes taking < 1 hour each)
3. **Code changes** with before/after examples for the top 3 issues
4. **Bundle optimization**: code splitting, lazy loading, tree shaking
5. **Image optimization** strategy
6. **Caching strategy** (HTTP headers, service worker, CDN)
7. **Target metrics**: LCP < 2.5s, FID < 100ms, CLS < 0.1
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Scaffold a Portfolio-Worthy Project

**id:** `01-vibe-coding/portfolio-project-scaffold` · **Difficulty:** intermediate · **Tags:** portfolio, career, project, showcase

**Placeholders:** [TOPIC]

````text
I'm a developer trying to impress employers. Build a complete scaffold for a portfolio project about: [TOPIC].

Include:
- Professional folder structure
- Complete `README.md` with badges and screenshots section
- Environment configuration (.env.example)
- Docker Compose for local development
- GitHub Actions CI pipeline
- Pre-commit hooks (eslint, prettier, commitlint)
- The core feature implemented end-to-end
- Deployment instructions for Railway/Vercel/Render

Make this look like it was built by someone who takes their craft seriously.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Convert a Website to a PWA

**id:** `01-vibe-coding/progressive-web-app` · **Difficulty:** intermediate · **Tags:** pwa, service-worker, offline, mobile

**Placeholders:** [DESCRIBE YOUR CURRENT APP]

````text
Convert my existing web app into a Progressive Web App (PWA).

[DESCRIBE YOUR CURRENT APP]

Implement:
1. Web App Manifest (`manifest.json`) with all required fields
2. Service Worker with: cache-first strategy, network-first for API calls, offline fallback page
3. App install prompt (beforeinstallprompt handling)
4. Push notifications setup (with permission flow)
5. Background sync for offline form submissions
6. Update notification when new version is available

Lighthouse PWA score target: 100.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Generate 10 Buildable Project Ideas

**id:** `01-vibe-coding/project-ideas-generator` · **Difficulty:** beginner · **Tags:** ideas, projects, learning, portfolio

**Placeholders:** [SKILL LEVEL], [SKILLS YOU WANT TO DEMONSTRATE], [TECH STACK], [TIME FRAME]

````text
I am a [SKILL LEVEL] developer who knows [TECH STACK]. I want to build something impressive for my portfolio.

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
- The single hardest technical challenge to solve
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Run an AI-Powered Project Retrospective

**id:** `01-vibe-coding/project-retrospective` · **Difficulty:** beginner · **Tags:** retrospective, agile, productivity, team

**Placeholders:** [PASTE YOUR SPRINT NOTES, INCIDENTS, METRICS, FEEDBACK]

````text
Act as an experienced engineering manager facilitating a retrospective. Here are notes from our last sprint/project:

[PASTE YOUR SPRINT NOTES, INCIDENTS, METRICS, FEEDBACK]

Facilitate a retrospective:
1. **What went well** (celebrate these)
2. **What didn't go well** (be specific, no blame)
3. **Root cause analysis** for the top 2 problems
4. **Actionable improvements** (with owners and deadlines)
5. **Team health check** based on the data
6. **One process change** to implement immediately

Output as a formatted retrospective report suitable for sharing with the team.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Ship a Working Prototype in 10 Minutes

**id:** `01-vibe-coding/prototype-in-10-minutes` · **Difficulty:** beginner · **Tags:** prototype, mvp, vibe-coding

**Placeholders:** [YOUR IDEA]

````text
I have exactly 10 minutes. Help me ship a working prototype of: [YOUR IDEA].

Rules:
- Single HTML file, no build step
- Works offline (no API calls required)
- Looks decent (not embarrassing to show)
- Actually demonstrates the core value proposition

Give me the complete code I can copy-paste into a file and open in a browser right now. Then give me 3 things I can add in the next 30 minutes to make it impressive.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Rate Limiting for Your API

**id:** `01-vibe-coding/rate-limiter` · **Difficulty:** intermediate · **Tags:** rate-limiting, redis, api, security

````text
Implement production-grade rate limiting for my Express.js API.

Requirements:
- Sliding window algorithm (fairer than fixed window)
- Per-user rate limits (authenticated) and per-IP (anonymous)
- Different limits per route: strict for auth, generous for reads
- Redis backend for distributed rate limiting
- Graceful response with `Retry-After` header
- Rate limit headers in every response (X-RateLimit-Limit, Remaining, Reset)
- Admin bypass capability
- Rate limit exceeded webhook/alert

Include unit tests for the rate limiter logic.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Generate a Stunning GitHub README

**id:** `01-vibe-coding/readme-generator` · **Difficulty:** beginner · **Tags:** documentation, readme, github, open-source

**Placeholders:** [DESCRIPTION], [LIST], [NAME], [STACK]

````text
You are a documentation expert. Generate a stunning GitHub README.md for my project:

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

Make it the kind of README that makes developers star the repo immediately.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Add Real-Time Features to Any App

**id:** `01-vibe-coding/real-time-feature` · **Difficulty:** intermediate · **Tags:** websockets, socket-io, real-time, backend

**Placeholders:** [FEATURE 1: e.g., live chat], [FEATURE 2: e.g., real-time notifications], [FEATURE 3: e.g., collaborative editing indicator], [TYPE]

````text
Add real-time features to my [TYPE] app.

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
6. Scaling notes for when you need multiple servers (Redis adapter)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Modernize Legacy CSS to CSS Variables

**id:** `01-vibe-coding/sass-to-css-variables` · **Difficulty:** beginner · **Tags:** css, refactor, design-tokens

**Placeholders:** [PASTE YOUR CSS HERE]

````text
You are a CSS architecture expert. Refactor this legacy CSS/SASS:

[PASTE YOUR CSS HERE]

Convert it to modern CSS with:
- CSS custom properties (variables) for all colors, spacing, typography
- A `:root` block with a complete design token system
- Logical properties where appropriate (margin-inline, padding-block)
- CSS nesting (native, no preprocessor)
- Remove any vendor prefixes that are no longer needed (2024+)
- Add CSS layers (@layer) for specificity management

Output the refactored CSS and a brief explanation of each major change.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build Advanced Search and Filter UI

**id:** `01-vibe-coding/search-and-filter` · **Difficulty:** intermediate · **Tags:** search, filter, react, ux

**Placeholders:** [DESCRIBE YOUR DATA], [TYPE: table/list/gallery]

````text
Build an advanced search and filter UI component for a [TYPE: table/list/gallery].

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

React + TypeScript, no UI library dependencies.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build Serverless Functions for Your App

**id:** `01-vibe-coding/serverless-functions` · **Difficulty:** intermediate · **Tags:** serverless, aws-lambda, vercel-functions, edge

**Placeholders:** [LIST YOUR BACKEND OPERATIONS]

````text
Build serverless functions for my app. I need to handle:

[LIST YOUR BACKEND OPERATIONS]

For each function:
1. Implementation (TypeScript, compatible with Vercel/AWS Lambda/Cloudflare Workers)
2. Input validation with Zod
3. Error handling with proper HTTP status codes
4. Cold start optimization
5. Environment variable usage
6. Local testing with Vitest
7. Deployment config

Also include: a shared middleware pattern for auth, logging, and CORS.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Automate Your Side Project's Boring Parts

**id:** `01-vibe-coding/side-project-automator` · **Difficulty:** intermediate · **Tags:** automation, scripts, productivity, devops

**Placeholders:** [LIST TASKS], [PROJECT]

````text
I'm building [PROJECT] and I keep doing these repetitive tasks manually: [LIST TASKS].

Automate everything with:
1. **Shell scripts** for each task
2. **npm scripts** in package.json
3. **GitHub Actions** for any CI/CD tasks
4. **Makefile** with a help target listing all commands
5. A **pre-commit hook** that runs relevant checks

For each automation:
- The script code
- How to invoke it
- What it does and why it saves time
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Design a State Machine for Any Feature

**id:** `01-vibe-coding/state-machine-designer` · **Difficulty:** advanced · **Tags:** state-machine, xstate, logic, architecture

**Placeholders:** [FEATURE DESCRIPTION]

````text
You are an expert in finite state machines. I need a state machine for: [FEATURE DESCRIPTION].

Design:
1. All possible states (draw as an ASCII diagram)
2. All transitions and the events that trigger them
3. Guard conditions for conditional transitions
4. Entry/exit actions for each state
5. Implementation using XState v5 (TypeScript)
6. React integration with `useMachine` hook
7. Unit tests for each state transition

Make the state machine impossible to get into an invalid state.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Subscription/Payment System

**id:** `01-vibe-coding/subscription-system` · **Difficulty:** advanced · **Tags:** stripe, subscriptions, payments, saas

**Placeholders:** [LIST YOUR PLANS AND PRICES], [YOUR APP TYPE]

````text
Build a complete subscription system using Stripe.

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

Production-ready with idempotency keys and webhook signature verification.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Complete Backend with Supabase

**id:** `01-vibe-coding/supabase-backend` · **Difficulty:** intermediate · **Tags:** supabase, postgresql, backend, auth

**Placeholders:** [APP TYPE]

````text
Build a complete backend for [APP TYPE] using Supabase.

Include:
1. Database schema with all tables, columns, types, and constraints
2. Row Level Security (RLS) policies for each table
3. PostgreSQL functions and triggers
4. TypeScript types generated from schema
5. Supabase client setup with proper TypeScript generics
6. Auth configuration (email/password + OAuth)
7. Storage bucket setup for file uploads
8. Edge Functions for any custom logic

Output as: SQL migration files + TypeScript client code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Test Data Factory

**id:** `01-vibe-coding/test-data-factory` · **Difficulty:** intermediate · **Tags:** testing, factories, typescript, jest

**Placeholders:** [PASTE YOUR TYPESCRIPT INTERFACES/TYPES]

````text
Build a test data factory system for my TypeScript project.

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

Pattern: inspired by factory_bot (Ruby) or fishery (TypeScript).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Scaffold a UI Component Library

**id:** `01-vibe-coding/ui-component-library-starter` · **Difficulty:** advanced · **Tags:** react, storybook, design-system, components

````text
You are a design systems engineer. Scaffold a minimal but production-ready React component library with:
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

Also create: `package.json`, `tsconfig.json`, `.storybook/main.ts`, and `index.ts` barrel export.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Convert User Stories to Working Code

**id:** `01-vibe-coding/user-story-to-code` · **Difficulty:** intermediate · **Tags:** agile, user-stories, tdd, features

**Placeholders:** [PASTE USER STORIES IN GIVEN/WHEN/THEN FORMAT], [YOUR STACK]

````text
Convert these user stories into working code using TDD:

[PASTE USER STORIES IN GIVEN/WHEN/THEN FORMAT]

For each user story:
1. Write the failing test first (Jest)
2. Implement the minimum code to pass the test
3. Refactor for clarity

Tech stack: [YOUR STACK]

Output the complete test file and implementation file. Group tests by user story with `describe` blocks.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Turn a Vibe / Feeling into an API

**id:** `01-vibe-coding/vibe-to-api` · **Difficulty:** intermediate · **Tags:** api, design, creative, backend

````text
I want an API that feels like [DESCRIBE THE VIBE — e.g., "a calm productivity tool", "a chaotic creative playground"].

Design and implement:
1. The REST API routes (method, path, request body, response shape)
2. Express.js implementation with TypeScript
3. Meaningful status codes and error messages that match the vibe
4. A sample `.http` or `curl` test file
5. A one-paragraph "API philosophy" doc comment at the top of the file

Make the developer experience match the vibe — from variable names to error messages.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Plan a Weekend Coding Project

**id:** `01-vibe-coding/weekend-project-planner` · **Difficulty:** beginner · **Tags:** planning, project-management, mvp

**Placeholders:** [PROJECT IDEA]

````text
I have this weekend (Sat + Sun, ~12 hours total) to build: [PROJECT IDEA].

Create a detailed hour-by-hour plan:
- Saturday morning (3h): [Foundation]
- Saturday afternoon (3h): [Core features]  
- Sunday morning (3h): [Polish & edge cases]
- Sunday afternoon (3h): [Deploy & share]

For each block:
- Specific tasks with checkboxes
- Files to create/edit
- Potential blockers and how to avoid them

Also: What to cut if I'm running behind, and what's the absolute minimum I need for a deployable v1.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Convert a Text Wireframe to React Components

**id:** `01-vibe-coding/wireframe-to-react` · **Difficulty:** intermediate · **Tags:** react, typescript, components, ui

**Placeholders:** [PASTE YOUR WIREFRAME DESCRIPTION HERE]

````text
You are an expert React developer. Convert the following text wireframe description into fully functional React + TypeScript components:

[PASTE YOUR WIREFRAME DESCRIPTION HERE]

Requirements:
- Use functional components with hooks
- TypeScript interfaces for all props
- Styled with CSS Modules or inline styles (no Tailwind)
- Responsive layout using CSS Grid and Flexbox
- Include PropTypes / TypeScript types
- Add hover states and smooth transitions
- Export a single `App.tsx` that composes all components together
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

