# 02-frontend-dev

React/Next.js, TypeScript, CSS, animations, forms, data tables, state management, frontend performance.

51 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Build Fully Accessible UI Components

**id:** `02-frontend-dev/accessible-components` · **Difficulty:** advanced · **Tags:** accessibility, aria, wcag, react

````text
Build these UI components with perfect accessibility (WCAG 2.1 AA):

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
- Testing with axe-core
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Complete Auth Context in React

**id:** `02-frontend-dev/auth-context` · **Difficulty:** intermediate · **Tags:** react, auth, context, typescript

````text
Build a complete authentication context for a React SPA.

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

TypeScript throughout with proper typing of user object.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Optimize Your JavaScript Bundle

**id:** `02-frontend-dev/bundle-optimization` · **Difficulty:** advanced · **Tags:** performance, webpack, vite, bundle-size

**Placeholders:** [LIST HEAVY DEPS], [VITE/WEBPACK/NEXT.JS]

````text
Analyze and optimize my JavaScript bundle.

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

Target: main bundle < 100KB gzipped.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Charts and Analytics Dashboard

**id:** `02-frontend-dev/chart-dashboard` · **Difficulty:** intermediate · **Tags:** react, charts, recharts, analytics

**Placeholders:** [LIST YOUR METRICS]

````text
Build a beautiful analytics dashboard with interactive charts.

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

Dark mode support included.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Write Tests for React Components

**id:** `02-frontend-dev/component-testing` · **Difficulty:** intermediate · **Tags:** testing, react-testing-library, jest, vitest

**Placeholders:** [LIST YOUR COMPONENTS]

````text
Write comprehensive tests for my React components.

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

Test organization: describe blocks, arrange-act-assert pattern.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## CSS Animation Masterclass

**id:** `02-frontend-dev/css-animation-masterclass` · **Difficulty:** intermediate · **Tags:** css, animations, keyframes, ux

````text
Create a complete animation system using pure CSS (no JavaScript).

Implement:
1. **Entrance animations**: fadeIn, slideUp, slideLeft, scaleIn, bounceIn
2. **Attention seekers**: shake, pulse, swing, tada
3. **Exits**: fadeOut, slideDown, scaleOut
4. **Continuous**: spin, ping, blink, wave
5. **Scroll-triggered**: using `@keyframes` + Intersection Observer via CSS only (animation-play-state)
6. **Stagger pattern**: `nth-child` animation delays for lists
7. **Reduced motion**: `@media (prefers-reduced-motion: reduce)` fallbacks

Each animation as a reusable CSS class.
Timing functions: use `cubic-bezier()` for natural motion, not just ease-in-out.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master CSS Custom Properties

**id:** `02-frontend-dev/css-custom-properties` · **Difficulty:** intermediate · **Tags:** css, variables, theming, modern

````text
Master CSS custom properties for building a robust theming system.

Implement:
1. **Design tokens**: color, spacing, typography as custom properties
2. **Component-level overrides**: scoped custom properties
3. **Theme switching**: class-based light/dark/custom themes
4. **JavaScript integration**: read/write custom properties from JS
5. **Fallback values**: `var(--color, #fallback)` patterns
6. **@property rule**: typed custom properties with animation support
7. **Inheritance tricks**: cascade manipulation
8. **Media query integration**: responsive design token overrides

Build a complete theming system for a SaaS dashboard with these techniques.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build Complex Layouts with CSS Grid

**id:** `02-frontend-dev/css-grid-mastery` · **Difficulty:** advanced · **Tags:** css, grid, layout, advanced

````text
Build these complex real-world layouts using pure CSS Grid (no flexbox fallbacks):

1. **Magazine layout**: multi-column article with featured image spanning rows
2. **Dashboard layout**: collapsible sidebar + header + main + widget grid
3. **Holy grail layout**: header, footer, 3 columns, all full-height
4. **Masonry grid**: Pinterest-style variable height cards
5. **Calendar grid**: month view with events spanning multiple days
6. **Timeline**: alternating left-right with center line
7. **Pricing cards**: equal height, aligned features

For each: the HTML structure, the CSS Grid code, and an explanation of the non-obvious parts.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Create Scroll-Driven Animations

**id:** `02-frontend-dev/css-scroll-animations` · **Difficulty:** intermediate · **Tags:** css, scroll, animations, modern

````text
Create scroll-driven animations using the modern CSS Scroll-driven Animations API.

Animations to build:
1. Progress bar that fills as user scrolls the page
2. Elements that fade/slide in as they enter the viewport
3. Parallax scrolling effect on hero image
4. Sticky header that shrinks/changes on scroll
5. Horizontal scroll carousel
6. Number counter that animates when scrolled into view
7. Reading time indicator

Using: `animation-timeline: scroll()` and `view()` — no JavaScript!
Include graceful degradation for unsupported browsers (Intersection Observer fallback).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Feature-Rich Data Table

**id:** `02-frontend-dev/data-table` · **Difficulty:** advanced · **Tags:** react, table, tanstack-table, ui

**Placeholders:** [DESCRIBE YOUR DATA COLUMNS AND TYPES]

````text
Build a production-grade data table component.

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

TypeScript with inferred column types.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Design Tokens Pipeline

**id:** `02-frontend-dev/design-tokens-pipeline` · **Difficulty:** advanced · **Tags:** design-tokens, style-dictionary, theming, build

````text
Build a design tokens pipeline from Figma to code.

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

Include: the Style Dictionary config and npm build script.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Drag-and-Drop Kanban Board

**id:** `02-frontend-dev/drag-and-drop-kanban` · **Difficulty:** advanced · **Tags:** react, dnd, kanban, ui

````text
Build a fully-featured Kanban board with drag and drop.

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

TypeScript, no CSS framework dependency.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Frontend Error Handling

**id:** `02-frontend-dev/error-handling-patterns` · **Difficulty:** intermediate · **Tags:** error-handling, react, typescript, reliability

````text
Implement comprehensive error handling for a React + TypeScript app.

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

Include: a centralized error reporting service (Sentry or custom).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Optimize Web Fonts for Performance

**id:** `02-frontend-dev/font-optimization` · **Difficulty:** intermediate · **Tags:** fonts, performance, css, web-vitals

**Placeholders:** [LIST YOUR FONTS]

````text
Optimize web fonts for performance and aesthetics in my project.

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

Target: < 30KB total font payload, CLS = 0.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Form Validation Patterns

**id:** `02-frontend-dev/form-validation` · **Difficulty:** intermediate · **Tags:** forms, react-hook-form, zod, typescript

**Placeholders:** [FORM TYPE]

````text
Implement comprehensive form validation for [FORM TYPE].

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
10. Accessible error messages (aria-describedby)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build Headless Components with Radix UI

**id:** `02-frontend-dev/headless-components` · **Difficulty:** intermediate · **Tags:** radix-ui, headless, accessibility, react

````text
Build a design system using Radix UI primitives (headless, fully accessible components).

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
- Storybook story with all variants
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Next.js Image Optimization

**id:** `02-frontend-dev/image-optimization` · **Difficulty:** intermediate · **Tags:** nextjs, images, performance, web-vitals

**Placeholders:** [DESCRIBE YOUR IMAGE USAGE]

````text
Optimize all images in my Next.js app for maximum performance.

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

Target: Largest Contentful Paint < 2.5s, zero layout shift from images.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Rich Markdown Editor

**id:** `02-frontend-dev/markdown-editor` · **Difficulty:** advanced · **Tags:** editor, markdown, react, ui

````text
Build a rich Markdown editor like Notion or Hashnode's editor.

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
10. Auto-save with debounce
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Up Micro-Frontend Architecture

**id:** `02-frontend-dev/micro-frontend` · **Difficulty:** advanced · **Tags:** micro-frontend, module-federation, webpack, architecture

**Placeholders:** [DESCRIPTION], [MY APP], [TEAM NAME]

````text
Set up a Micro-Frontend architecture for [MY APP].

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

Show: how to share auth state between microfrontends.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Next.js App Router Patterns

**id:** `02-frontend-dev/nextjs-app-router` · **Difficulty:** advanced · **Tags:** nextjs, app-router, react, typescript

**Placeholders:** [MY APP]

````text
Implement these Next.js 14+ App Router patterns for [MY APP]:

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

Show before/after for each pattern migrating from Pages Router.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Authentication in Next.js

**id:** `02-frontend-dev/nextjs-auth` · **Difficulty:** advanced · **Tags:** nextjs, auth, next-auth, security

````text
Implement complete authentication for Next.js 14 App Router.

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
10. Role-based access control (user, admin, moderator)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Next.js Middleware

**id:** `02-frontend-dev/nextjs-middleware` · **Difficulty:** advanced · **Tags:** nextjs, middleware, auth, edge

**Placeholders:** [MY APP]

````text
Implement powerful Next.js Middleware for [MY APP].

Use cases:
1. **Auth protection**: redirect unauthenticated users
2. **A/B testing**: randomly assign variant, persist in cookie
3. **Feature flags**: check flags and redirect or modify response
4. **Geo-blocking**: redirect based on country
5. **Rate limiting**: basic IP-based rate limit at the edge
6. **Localization**: detect language, redirect to locale subdirectory
7. **Bot detection**: block known scrapers
8. **Security headers**: CSP, HSTS, X-Frame-Options

Includes: `middleware.ts` + `matcher` config, performance tips (< 1ms execution budget).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an Offline-First Web App

**id:** `02-frontend-dev/offline-first` · **Difficulty:** advanced · **Tags:** pwa, offline, service-worker, indexeddb

**Placeholders:** [DESCRIBE YOUR APP AND ITS DATA]

````text
Build an offline-first version of my web app.

App type: [DESCRIBE YOUR APP AND ITS DATA]

Implement:
1. **Service Worker**: cache strategies per resource type
2. **IndexedDB**: local database for app data (using Dexie.js for nice API)
3. **Sync**: queue actions while offline, sync when reconnected (Background Sync API)
4. **Conflict resolution**: last-write-wins vs user choice
5. **Offline UI**: banner indicating offline status, disabled features that need network
6. **Optimistic offline mutations**: update local DB → sync to server
7. **Cache management**: storage quota handling, cache invalidation

Test with Chrome DevTools: offline mode + throttling.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Progressive Loading Patterns

**id:** `02-frontend-dev/progressive-loading` · **Difficulty:** intermediate · **Tags:** performance, loading, ux, react

**Placeholders:** [DESCRIBE WHAT'S SLOW]

````text
Implement progressive loading to make my app feel instant.

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

Each pattern with before (jarring UX) and after (smooth UX) code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master React 18 Features

**id:** `02-frontend-dev/react-18-features` · **Difficulty:** advanced · **Tags:** react-18, concurrent, suspense, transitions

````text
Master React 18 features for better performance and UX.

Features to implement:
1. **`startTransition`**: mark state updates as non-urgent (keep UI responsive)
2. **`useDeferredValue`**: defer expensive renders (search results)
3. **Concurrent Suspense**: show old content while loading new
4. **`useId`**: stable IDs for accessibility across server/client
5. **Automatic batching**: understand when React 18 batches vs not
6. **Selective hydration**: SSR streaming with Suspense boundaries
7. **`use()` hook** (experimental): unwrap promises and context
8. **React Server Components**: server-only component tree

Show: real-world examples where each feature meaningfully improves UX.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master React Context Patterns

**id:** `02-frontend-dev/react-context-patterns` · **Difficulty:** intermediate · **Tags:** react, context, state-management, typescript

**Placeholders:** [APP TYPE], [LIST YOUR GLOBAL STATE NEEDS]

````text
Implement production-quality React Context patterns for [APP TYPE].

Build context for: [LIST YOUR GLOBAL STATE NEEDS]

Implement:
1. **Typed context** with TypeScript generics
2. **Null safety**: custom hook that throws if used outside provider
3. **Performance optimization**: split context to avoid unnecessary re-renders
4. **Compound component pattern**: context + parent/child composition
5. **Context with useReducer**: for complex state (like Redux but built-in)
6. **Lazy initialization**: expensive state init only runs once
7. **Context selector pattern**: subscribe to slices only

Show: when to use Context vs Zustand vs Jotai vs Redux — and why.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build 10 Essential Custom React Hooks

**id:** `02-frontend-dev/react-custom-hooks` · **Difficulty:** intermediate · **Tags:** react, hooks, typescript

````text
Build 10 production-ready custom React hooks that every app needs:

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
- Edge cases handled
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Multi-Step Form Wizard

**id:** `02-frontend-dev/react-form-wizard` · **Difficulty:** intermediate · **Tags:** react, forms, validation, typescript

**Placeholders:** [DESCRIBE YOUR FORM STEPS AND FIELDS]

````text
Build a production-ready multi-step form wizard in React + TypeScript.

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

No UI library — pure React + CSS Modules.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build Cross-Platform React Native Components

**id:** `02-frontend-dev/react-native-components` · **Difficulty:** intermediate · **Tags:** react-native, expo, mobile, cross-platform

````text
Build these cross-platform React Native components using Expo.

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
- Not crash when permissions are denied
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Generate PDFs from React Components

**id:** `02-frontend-dev/react-pdf` · **Difficulty:** intermediate · **Tags:** pdf, react, react-pdf, documents

**Placeholders:** [DESCRIBE: invoice / report / certificate / contract]

````text
Generate professional PDFs from React components.

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

Also: email delivery option using the PDF as a Buffer attachment.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Optimize React Performance

**id:** `02-frontend-dev/react-performance` · **Difficulty:** advanced · **Tags:** react, performance, memo, optimization

**Placeholders:** [DESCRIBE: slow renders, jank, high memory usage]

````text
Profile and optimize the performance of my React app.

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

Show: before/after examples with render count measurements.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master React Query / TanStack Query

**id:** `02-frontend-dev/react-query-patterns` · **Difficulty:** intermediate · **Tags:** react-query, tanstack, data-fetching, cache

**Placeholders:** [MY APP]

````text
Master TanStack Query v5 (React Query) for [MY APP].

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

Include: a `queryClient` singleton setup and provider configuration.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build Real-Time Collaboration Features

**id:** `02-frontend-dev/real-time-collaboration` · **Difficulty:** advanced · **Tags:** websockets, yjs, crdt, collaboration

**Placeholders:** [DESCRIBE: collaborative text editing / whiteboard / spreadsheet / other]

````text
Add Google Docs-style real-time collaboration to my app.

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

Include the server setup (Node.js y-websocket server).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Custom Responsive Grid System

**id:** `02-frontend-dev/responsive-grid-system` · **Difficulty:** intermediate · **Tags:** css, grid, layout, responsive

````text
Build a custom CSS Grid system from scratch (no Bootstrap/Tailwind).

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
Output: a CSS file usable via `<link>` or importable in React.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Responsive Images

**id:** `02-frontend-dev/responsive-images` · **Difficulty:** intermediate · **Tags:** images, responsive, performance, html

**Placeholders:** [LIST: hero images / product photos / avatars / blog thumbnails], [MY WEBSITE/APP]

````text
Implement responsive images correctly for [MY WEBSITE/APP].

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

Show: the generated HTML for each scenario.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Complete SEO for Next.js

**id:** `02-frontend-dev/seo-optimization` · **Difficulty:** intermediate · **Tags:** seo, nextjs, metadata, structured-data

**Placeholders:** [DESCRIBE YOUR APP], [LANGUAGES], [LIST IMPORTANT PAGES]

````text
Implement complete SEO for my Next.js 14 app.

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
10. Internationalized SEO with `hreflang` for [LANGUAGES]
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Customize and Extend shadcn/ui

**id:** `02-frontend-dev/shadcn-custom` · **Difficulty:** intermediate · **Tags:** shadcn, radix, react, design-system

**Placeholders:** [DESCRIBE BRAND: colors, roundness, feel]

````text
Extend shadcn/ui with custom components and theme customization.

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

Output: drop-in components ready for your `components/ui/` folder.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Choose and Implement State Management

**id:** `02-frontend-dev/state-management-comparison` · **Difficulty:** advanced · **Tags:** redux, zustand, jotai, state

**Placeholders:** [DESCRIBE YOUR STATE NEEDS]

````text
My app needs state management for: [DESCRIBE YOUR STATE NEEDS].

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

Recommendation: Which one fits my use case and why.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Up Storybook for Your Component Library

**id:** `02-frontend-dev/storybook-setup` · **Difficulty:** intermediate · **Tags:** storybook, components, documentation, testing

````text
Set up Storybook 8 for my [React/Vue/Web Components] project.

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

Also: best practices for story organization and naming.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Integrate Stripe Payment UI

**id:** `02-frontend-dev/stripe-frontend` · **Difficulty:** intermediate · **Tags:** stripe, payments, react, frontend

````text
Build the frontend payment UI for a Stripe integration.

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

Include: the backend API routes needed to create Payment Intents.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Create a Living Style Guide

**id:** `02-frontend-dev/style-guide` · **Difficulty:** intermediate · **Tags:** style-guide, components, documentation, design

````text
Create a living style guide (in-app) for my component library.

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

Self-contained page that works without any routing library.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Create Advanced SVG Animations

**id:** `02-frontend-dev/svg-animations` · **Difficulty:** advanced · **Tags:** svg, animations, css, gsap

**Placeholders:** [DESCRIBE: icons, logos, illustrations, charts, or data viz you want to animate]

````text
Create stunning SVG animations for:

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

Export each as a React component with controllable animation state.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Up TanStack Router

**id:** `02-frontend-dev/tanstack-router` · **Difficulty:** intermediate · **Tags:** tanstack-router, routing, typescript, react

**Placeholders:** [LIST YOUR ROUTES AND THEIR PARAMS]

````text
Set up TanStack Router v1 for my React app.

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

Show the complete router setup and 3 example routes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a 3D Scene with Three.js and React

**id:** `02-frontend-dev/three-js-scene` · **Difficulty:** advanced · **Tags:** three-js, react-three-fiber, 3d, graphics

**Placeholders:** [DESCRIBE WHAT YOU WANT: product viewer / animated logo / data viz / game-like scene]

````text
Build a 3D interactive scene using React Three Fiber (Three.js for React).

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

Include: Leva controls for tweaking parameters in development.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master TypeScript Generics for React

**id:** `02-frontend-dev/typescript-generics` · **Difficulty:** advanced · **Tags:** typescript, generics, react, types

````text
Master TypeScript generics in the context of React development.

Build these generic utilities and components:

1. **Generic API hook**: `useApi<TData, TError>(url)` → `{data, error, loading}`
2. **Generic form**: `<Form<TValues>` with typed fields and typed submit handler
3. **Generic table**: `<DataTable<TRow>` with typed columns
4. **Generic select**: `<Select<TOption>` with typed options and onChange
5. **Generic context**: `createContext<TState>()` with typed provider
6. **Conditional types**: `DeepPartial<T>`, `DeepReadonly<T>`, `Nullable<T>`
7. **Mapped types**: transform any model for API vs UI vs form
8. **Template literal types**: typed route params

Each with TypeScript playground-ready examples.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a TypeScript Utility Type Library

**id:** `02-frontend-dev/typescript-utility-types` · **Difficulty:** advanced · **Tags:** typescript, utility-types, generics, types

````text
Build a comprehensive TypeScript utility type library for frontend development.

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

Each type with 2 usage examples.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Virtualized Infinite List

**id:** `02-frontend-dev/virtualized-list` · **Difficulty:** advanced · **Tags:** react, virtualization, performance, ui

**Placeholders:** [DATA TYPE]

````text
Build a high-performance virtualized infinite scroll list for [DATA TYPE].

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

Include the React Query integration for data fetching.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master the Web Animations API

**id:** `02-frontend-dev/web-animation-api` · **Difficulty:** advanced · **Tags:** waapi, animations, javascript, performance

````text
Master the Web Animations API (WAAPI) — the native browser animation engine.

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

Migrate: show how to replace a GSAP animation with WAAPI.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build Native Web Components

**id:** `02-frontend-dev/web-components` · **Difficulty:** advanced · **Tags:** web-components, custom-elements, shadow-dom, javascript

````text
Build production-ready Web Components (framework-agnostic).

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

Include TypeScript type declarations (.d.ts) for IDE support.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Offload Heavy Work to Web Workers

**id:** `02-frontend-dev/web-workers` · **Difficulty:** advanced · **Tags:** web-workers, performance, javascript, concurrency

**Placeholders:** [DESCRIBE: image processing / data parsing / complex calculations / etc.]

````text
Offload these CPU-intensive tasks to Web Workers:

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

Benchmark: show the before (main thread blocking) vs after.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a WebSocket-Powered Real-Time UI

**id:** `02-frontend-dev/websocket-ui` · **Difficulty:** intermediate · **Tags:** websockets, react, real-time, ui

**Placeholders:** [DESCRIBE YOUR DATA: stock prices / server metrics / chat messages / etc.]

````text
Build a real-time dashboard UI using WebSockets.

Data to display in real-time: [DESCRIBE YOUR DATA: stock prices / server metrics / chat messages / etc.]

React implementation:
1. `useWebSocket` custom hook with reconnection logic
2. Connection status indicator (connecting/connected/disconnected)
3. Message queue for messages received while UI is updating
4. Throttle incoming messages (max 60fps updates)
5. Optimistic local updates
6. Reconnect with exponential backoff
7. Heartbeat/ping-pong keepalive

UI components: animated number counters, live charts, real-time feed.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

