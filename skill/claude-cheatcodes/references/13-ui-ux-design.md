# 13-ui-ux-design

UI components, design systems, accessibility, Tailwind/CSS/Framer Motion, UX writing, wireframes.

25 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Apply Animation Principles to UI

**id:** `13-ui-ux-design/animation-principles` · **Difficulty:** intermediate · **Tags:** animation, ux, motion, design

**Placeholders:** [DESCRIBE]

````text
Apply the 12 principles of animation to my UI.

App: [DESCRIBE]

**Disney's 12 principles applied to UI**:
1. **Squash and stretch**: buttons compress on press (scale 0.95)
2. **Anticipation**: loading indicator before action starts
3. **Staging**: most important element animates first
4. **Straight ahead vs pose to pose**: CSS transitions vs keyframes
5. **Follow through**: elements overshoot then settle (spring)
6. **Slow in, slow out**: ease-in-out (never linear for UI)
7. **Arcs**: natural curved motion paths (not straight lines)
8. **Secondary action**: smaller elements react to main animation
9. **Timing**: duration = perceived weight (heavy = slower)
10. **Exaggeration**: slightly overdo for delightful feel
11. **Solid drawing**: 3D-aware scale and perspective
12. **Appeal**: animations should feel alive

**UI-specific additions**:
- Duration: 100ms (micro), 200-300ms (standard), 400-600ms (large)
- Easing: spring for physical, ease-out for entrances

Apply to my app's key interactions.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Audit Color Accessibility

**id:** `13-ui-ux-design/color-accessibility` · **Difficulty:** intermediate · **Tags:** accessibility, color, wcag, design

**Placeholders:** [DESCRIBE], [PASTE HEX VALUES]

````text
Audit and fix color accessibility in my design.

Current color palette: [PASTE HEX VALUES]
UI elements using these colors: [DESCRIBE]

WCAG 2.1 requirements:
- **AA**: normal text 4.5:1, large text 3:1, UI components 3:1
- **AAA**: normal text 7:1, large text 4.5:1

Audit:
1. Calculate contrast ratio for every text/background combination
2. Flag all failures with their current ratio
3. Suggest adjusted colors that pass while staying on-brand
4. Check: colored icons on colored backgrounds
5. Check: focus indicators (3:1 against adjacent colors)
6. Check: placeholder text (often too light)
7. Check: disabled state (often too light)
8. Color blindness: can everything be understood without color alone?

Fix:
9. Adjusted color values for all failures
10. Add pattern/icon to supplement color-only information

Output: audit table + fixed color values.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Color Theory to UI Design

**id:** `13-ui-ux-design/color-theory` · **Difficulty:** intermediate · **Tags:** color, design, ui, accessibility

**Placeholders:** [DESCRIBE YOUR PRODUCT TYPE AND BRAND FEELING], [HEX CODES]

````text
Apply color theory to create a beautiful, accessible color system for my UI.

Context: [DESCRIBE YOUR PRODUCT TYPE AND BRAND FEELING]
Existing brand colors (if any): [HEX CODES]

1. **Color models**: HSL for perceptually uniform adjustments
2. **Color harmony**: complementary, analogous, triadic — which suits my brand
3. **Primary color**: your main brand color → generate 10-shade scale
4. **Secondary color**: complementary for accents
5. **Neutral scale**: warm gray vs cool gray vs pure gray
6. **Semantic colors**: success (green), warning (amber), error (red), info (blue)
7. **Dark mode**: not just inversion — luminance and saturation adjustments
8. **WCAG contrast**: all text meets 4.5:1 AA, large text 3:1
9. **Color blindness**: test with Deuteranopia and Protanopia simulators
10. **CSS output**: complete custom property color system

Output: complete color system as CSS variables.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Beautiful Dark Mode

**id:** `13-ui-ux-design/dark-mode-design` · **Difficulty:** intermediate · **Tags:** dark-mode, design, css, theming

**Placeholders:** [PASTE YOUR COLOR PALETTE]

````text
Design a beautiful, professional dark mode for my application.

Current light mode colors: [PASTE YOUR COLOR PALETTE]

Dark mode design principles:
1. **Not just color inversion**: dark mode is a different design
2. **Elevation model**: dark surfaces get lighter, not darker (Material Design)
3. **Reduced saturation**: colors look different on dark backgrounds, adjust saturation
4. **True black avoidance**: #121212 or #1a1a1a, not #000000 (except OLED)
5. **Text contrast**: avoid pure white (#ffffff) → use #e8e8e8
6. **Shadows**: don't show well on dark → use glow effects instead
7. **Images**: darken bright images slightly, lighten dark ones
8. **Icons**: use outlined in dark, filled in light
9. **Transitions**: smooth 200ms transition between modes
10. **System preference**: respect prefers-color-scheme

Output: complete CSS variable system for both modes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Critique and Improve a UI Design

**id:** `13-ui-ux-design/design-critique` · **Difficulty:** intermediate · **Tags:** design-critique, ux, feedback, improvement

**Placeholders:** [DESCRIBE OR PASTE SCREENSHOT DESCRIPTION], [WHAT THE APP DOES], [WHO USES IT]

````text
Critique and improve this UI design.

Current design: [DESCRIBE OR PASTE SCREENSHOT DESCRIPTION]
App purpose: [WHAT THE APP DOES]
Target users: [WHO USES IT]

Critique across dimensions:
1. **Visual hierarchy**: does the eye go to the right place first?
2. **Consistency**: same patterns used for same actions throughout?
3. **Feedback**: does the user know what's happening?
4. **Error prevention**: are common mistakes prevented?
5. **Cognitive load**: is there too much information at once?
6. **Affordance**: do interactive elements look interactive?
7. **Accessibility**: contrast, font size, touch targets
8. **Mobile**: does it work on small screens?
9. **Empty states**: what does the user see with no data?
10. **Performance perception**: does it feel fast?

For each issue:
- Severity: critical / major / minor
- Specific element affected
- Recommended fix with reasoning
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Prepare Design Handoff for Developers

**id:** `13-ui-ux-design/design-handoff` · **Difficulty:** intermediate · **Tags:** design-handoff, figma, specifications, design

**Placeholders:** [DESCRIBE THEIR EXPERIENCE LEVEL], [DESCRIBE]

````text
Prepare a comprehensive design handoff for developers.

Feature designed: [DESCRIBE]
Design tool: Figma
Developers receiving: [DESCRIBE THEIR EXPERIENCE LEVEL]

**What developers need from handoff**:
1. **Specs**: exact measurements (px/rem), colors (hex/CSS var), fonts
2. **Component states**: default, hover, active, disabled, loading, error
3. **Responsive behavior**: how it adapts at each breakpoint
4. **Animations**: duration, easing, what triggers them
5. **Interactions**: what happens on each user action
6. **Edge cases**: long text, empty state, error state
7. **Assets**: exported SVGs, images at correct sizes
8. **Design tokens**: which token variables to use

**Figma handoff checklist**:
9. Auto layout on all components (no absolute positioning)
10. Consistent naming (developers use these names in code)
11. Annotated with units and behavior notes
12. Dev mode enabled for automatic CSS output

Output: handoff specification document + Figma annotation guide.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Complete Design System

**id:** `13-ui-ux-design/design-system` · **Difficulty:** advanced · **Tags:** design-system, components, css, tokens

**Placeholders:** [DESCRIBE YOUR BRAND PERSONALITY AND VALUES]

````text
Build a complete design system for my product.

Brand: [DESCRIBE YOUR BRAND PERSONALITY AND VALUES]
Product type: [SaaS / consumer app / e-commerce / etc.]

Design system layers:

**1. Foundation**:
- Color palette: brand, neutral, semantic, dark mode
- Typography: scale, weights, line heights, families
- Spacing: 4px grid, scale from 0 to 96
- Shadows: 5 elevation levels
- Border radius: sm/md/lg/full
- Icons: chose icon library or custom icons

**2. Components**:
- Atoms: Button, Input, Checkbox, Badge, Avatar
- Molecules: Form Field, Card, Dropdown, Toast
- Organisms: Navigation, Data Table, Modal, Sidebar

**3. Patterns**:
- Form patterns, data display, empty states, errors

**4. Documentation**: living style guide

Output: CSS variables + React components + Storybook stories.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create and Manage Design Tokens

**id:** `13-ui-ux-design/design-tokens` · **Difficulty:** advanced · **Tags:** design-tokens, css, theming, style-dictionary

**Placeholders:** [DESCRIBE]

````text
Create a comprehensive design token system.

Brand: [DESCRIBE]
Platforms: Web (CSS) + iOS (Swift) + Android (XML) [choose which apply]

**Token hierarchy**:
1. **Primitive tokens**: raw values (colors, sizes)
   - `color-blue-500: #3b82f6`
2. **Semantic tokens**: meaning (reference primitives)
   - `color-action-primary: {color-blue-500}`
3. **Component tokens**: specific usage
   - `button-background-primary: {color-action-primary}`

**Token categories**:
4. Colors (full palette + semantic)
5. Typography (family, size, weight, line-height)
6. Spacing (4px grid)
7. Border (width, radius)
8. Shadow (elevation)
9. Animation (duration, easing)
10. Z-index (layers)

Using Style Dictionary:
11. Token JSON files
12. Transform to CSS, Swift, Android XML
13. CI: regenerate on token change

Output: complete token set + Style Dictionary config.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Error States and Empty States

**id:** `13-ui-ux-design/error-states` · **Difficulty:** intermediate · **Tags:** errors, empty-states, ux, design

**Placeholders:** [DESCRIBE]

````text
Design informative, helpful error states and empty states.

My app: [DESCRIBE]

**Error states**:
1. **404 Page**: friendly + helpful navigation back
2. **500 Error**: apologetic + retry button + status page link
3. **No internet**: offline icon + retry + what still works
4. **API error**: specific message + what user can do
5. **Permission denied**: explain why + request permission
6. **Session expired**: auto-save user's work + re-login prompt

**Empty states** (first-time user or no results):
7. **First visit**: illustrative empty state + primary CTA (don't show empty table)
8. **No search results**: show what was searched + suggestions
9. **Filtered to nothing**: show active filters + clear filter CTA
10. **No notifications**: reassuring (not broken) message

For each: copy + illustration description + CTA button copy.
Illustrations: use SVG blob or emoji-based illustrations.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design High-Converting Forms

**id:** `13-ui-ux-design/form-ux` · **Difficulty:** intermediate · **Tags:** forms, ux, conversion, design

**Placeholders:** [DESCRIBE YOUR MAIN FORMS]

````text
Design high-converting, user-friendly forms.

Forms in my app: [DESCRIBE YOUR MAIN FORMS]

Conversion optimization:
1. **Single column**: never use two columns for forms (unless desktop)
2. **Labels above**: not inside (inside labels disappear)
3. **Placeholder**: show example value, not label
4. **Input width**: match expected content width
5. **Keyboard type**: show number pad for phone numbers
6. **Autocomplete**: `autocomplete` attribute for browser assist
7. **Real-time validation**: validate on blur, not on change (less jarring)
8. **Error placement**: below the field, never just red border
9. **Success state**: green checkmark on valid field
10. **Progress indicator**: show step X of Y for multi-step
11. **Smart defaults**: pre-fill what you know
12. **Submit button**: active only when required fields complete

Specific improvements for each of my forms.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create an Iconography System

**id:** `13-ui-ux-design/iconography` · **Difficulty:** intermediate · **Tags:** icons, design, svg, system

**Placeholders:** [DESCRIBE: minimal/geometric, rounded/friendly, sharp/technical]

````text
Create a consistent iconography system for my product.

Brand personality: [DESCRIBE: minimal/geometric, rounded/friendly, sharp/technical]

1. **Icon library selection** (or custom):
   - Heroicons: clean, MIT license
   - Phosphor Icons: 6 weights, very flexible
   - Lucide: community fork of Feather
   - Custom SVG for brand-critical icons

2. **Sizing**: standard sizes: 16, 20, 24, 32px
3. **Stroke weight**: consistent 1.5 or 2px across all icons
4. **Corner radius**: square or rounded corners (match your UI roundness)
5. **Color**: inherit from text color (`currentColor`)
6. **Variants**: outlined (default), filled (active state), duotone (decorative)
7. **React component**: `<Icon name="arrow-right" size={20} />`
8. **Sprite sheet**: optimize for performance (SVG sprite)
9. **Accessibility**: title + aria-hidden for decorative icons
10. **Dark mode**: icons that work on both backgrounds

Output: icon component + usage guidelines.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Information Architecture

**id:** `13-ui-ux-design/information-architecture` · **Difficulty:** advanced · **Tags:** ia, navigation, ux, structure

**Placeholders:** [DESCRIBE YOUR APP AND ITS MAIN FEATURES], [DESCRIBE YOUR USER TYPES AND THEIR GOALS]

````text
Design the information architecture for my application.

App: [DESCRIBE YOUR APP AND ITS MAIN FEATURES]
Users: [DESCRIBE YOUR USER TYPES AND THEIR GOALS]

1. **Card sorting** (mental model):
   - List all features/content in your app
   - Group them as a user would
   - Identify naming conventions users expect
2. **Hierarchy**: organize content into logical tree
3. **Navigation patterns**:
   - Primary: top bar / sidebar / bottom tabs
   - Secondary: breadcrumbs, tabs, sub-navigation
   - Utility: search, profile, settings
4. **Labeling**: names that match user mental models
5. **Progressive disclosure**: hide complexity until needed
6. **Search**: when navigation alone isn't enough
7. **Cross-linking**: related content links between sections
8. **Mobile vs desktop**: different IA for different contexts
9. **Sitemap**: visual map of all pages and relationships
10. **Navigation test**: can users find key items in < 3 clicks?

Output: sitemap + navigation design.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Beautiful Loading States

**id:** `13-ui-ux-design/loading-states` · **Difficulty:** intermediate · **Tags:** loading, ux, skeleton, design

**Placeholders:** [DESCRIBE]

````text
Design comprehensive loading states for my application.

App type: [DESCRIBE]

Loading patterns:
1. **Skeleton screens**: anatomically correct placeholder matching real content shape
2. **Spinner**: when content area is small or duration unknown
3. **Progress bar**: when % known (file upload, multi-step)
4. **Optimistic UI**: show result immediately, then confirm
5. **Blur-up**: load low-res placeholder, fade in full image
6. **Progressive loading**: load critical content first
7. **Stale-while-revalidate**: show old data while fetching new

For each state:
8. Initial load: skeleton the whole page
9. Partial refresh: show spinner in specific section
10. Action feedback: button shows spinner, disables during submit
11. Background refresh: subtle indicator, don't block UI
12. Infinite scroll: spinner at bottom, not full page

Output: React components for each loading state.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Micro-Interactions

**id:** `13-ui-ux-design/micro-interactions` · **Difficulty:** intermediate · **Tags:** animations, micro-interactions, ux, design

**Placeholders:** [DESCRIBE YOUR APP]

````text
Design delightful micro-interactions for my application.

App context: [DESCRIBE YOUR APP]

Micro-interactions to design:
1. **Button press**: scale down + color darken (tactile feel)
2. **Toggle switch**: slide + color change with spring physics
3. **Checkbox**: scale in checkmark with bounce
4. **Form validation**: success → green check, error → red shake
5. **Loading states**: skeleton → skeleton fade → content fade in
6. **Navigation**: smooth page transition (slide/fade)
7. **Hover effects**: lift (shadow + translateY), color shift
8. **Toast notifications**: slide up + auto-dismiss with animation
9. **Delete**: swipe or fade out with confirmation
10. **Pull to refresh**: elastic overscroll
11. **Long press**: subtle haptic feedback pattern
12. **Upload progress**: radial or linear with completion burst

For each: CSS/Framer Motion implementation + timing spec.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Responsive Design

**id:** `13-ui-ux-design/responsive-design` · **Difficulty:** intermediate · **Tags:** responsive, css, mobile-first, design

**Placeholders:** [DESCRIBE: dashboard, marketing site, e-commerce, etc.]

````text
Implement perfect responsive design for my application.

App type: [DESCRIBE: dashboard, marketing site, e-commerce, etc.]
Breakpoints: mobile (< 640px), tablet (640-1024px), desktop (> 1024px)

1. **Mobile-first**: start with mobile styles, add complexity for larger screens
2. **Fluid typography**: `clamp(min, preferred, max)` for responsive font sizes
3. **Fluid spacing**: `clamp()` for padding and margins too
4. **Container queries**: component-level responsive instead of viewport
5. **Flexible images**: `width: 100%; max-width: X` and `object-fit`
6. **Grid system**: CSS Grid with `auto-fill + minmax`
7. **Navigation**: hamburger menu on mobile, full nav on desktop
8. **Tables**: horizontal scroll on mobile, or transform to card layout
9. **Touch targets**: 44px minimum on mobile
10. **Viewport units**: use `svh` (small viewport height) on mobile

For each component in my app: mobile + desktop design decisions.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create a Typography System

**id:** `13-ui-ux-design/typography-system` · **Difficulty:** intermediate · **Tags:** typography, design, css, fonts

**Placeholders:** [DESCRIBE: modern, classic, playful, serious, technical]

````text
Create a comprehensive typography system for my web application.

Brand feeling: [DESCRIBE: modern, classic, playful, serious, technical]

1. **Font pairing**:
   - Heading font: [suggestions based on brand]
   - Body font: [readable, comfortable for long text]
   - Mono font: [for code, data]
2. **Type scale**: 8 sizes from xs to 5xl (following modular scale ratio)
3. **Font weights**: which weights you actually use (reduce to 2-3)
4. **Line height**: heading (1.2), body (1.5), UI labels (1.0)
5. **Letter spacing**: heading (-0.02em), body (0), uppercase (0.08em)
6. **Measure**: optimal line length (60-75 characters)
7. **Responsive**: slightly smaller on mobile
8. **Loading**: self-host or `next/font`, no FOUT
9. **Dark mode**: same fonts, slightly lighter weight
10. **Accessibility**: minimum 16px body, high contrast text

Output: CSS custom properties + utility classes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a UI Patterns Library

**id:** `13-ui-ux-design/ui-patterns-library` · **Difficulty:** intermediate · **Tags:** ui-patterns, documentation, design, components

**Placeholders:** [DESCRIBE]

````text
Build a UI patterns library documenting when and how to use each pattern.

App type: [DESCRIBE]

**Pattern documentation format**:
- Name and description
- When to use
- When NOT to use
- Example usage (code + visual)
- Variations
- Accessibility considerations

**Patterns to document**:
1. **Buttons**: primary, secondary, ghost, danger — when each
2. **Modals**: when modal vs page vs slide-over
3. **Toasts**: success, error, info, warning — auto vs manual dismiss
4. **Tables**: sortable, filterable, selectable, expandable rows
5. **Forms**: single column, inline, multi-step
6. **Navigation**: tabs, breadcrumbs, pagination
7. **Empty states**: first use, no results, error
8. **Loading**: skeleton, spinner, progress
9. **Cards**: media card, stats card, action card
10. **Lists**: simple, with actions, with checkboxes

Output: patterns library in Markdown format.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design User Onboarding Flow

**id:** `13-ui-ux-design/user-onboarding` · **Difficulty:** intermediate · **Tags:** onboarding, ux, retention, design

**Placeholders:** [DESCRIBE], [THE MOMENT A USER FIRST GETS VALUE]

````text
Design an effective user onboarding flow for my application.

Product: [DESCRIBE]
Aha moment: [THE MOMENT A USER FIRST GETS VALUE]

Onboarding principles:
1. **Get to value FAST**: time-to-aha is your most important metric
2. **Progressive disclosure**: don't show everything on day 1
3. **Empty states with actions**: first-time empty state guides the first action
4. **Checklist**: small wins → engagement (like Notion, Linear)
5. **Skip option**: power users hate hand-holding
6. **Contextual tooltips**: teach in context, not upfront
7. **Personalization question**: 1-2 questions to customize experience
8. **Success moment**: celebrate when they complete key action
9. **Email drip**: day 1, 3, 7 onboarding emails
10. **Completion tracking**: % of users reaching the aha moment

Design:
- Welcome screen (value prop in 10 words)
- 2-3 step setup flow
- Empty state with primary action
- First-run checklist
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Define and Track UX Metrics

**id:** `13-ui-ux-design/ux-metrics` · **Difficulty:** intermediate · **Tags:** ux-metrics, analytics, design, measurement

**Placeholders:** [DESCRIBE YOUR ANALYTICS SETUP], [DESCRIBE]

````text
Define UX metrics to measure and improve my product's user experience.

Product: [DESCRIBE]
Current data available: [DESCRIBE YOUR ANALYTICS SETUP]

**HEART Framework** (Google's UX metrics):
1. **Happiness**: user satisfaction (NPS, CSAT, App Store rating)
2. **Engagement**: usage frequency, session length, features used
3. **Adoption**: new users completing onboarding, feature adoption rate
4. **Retention**: D1, D7, D30 retention, churn rate
5. **Task success**: completion rate, time-on-task, error rate

**Specific metrics for my app**:
6. Onboarding completion rate
7. Time-to-first-value (minutes to aha moment)
8. Feature activation rate (% users who use each feature)
9. Support ticket rate (proxy for UX confusion)
10. Rage clicks (users clicking in frustration)

**Implementation**:
- Events to track in analytics
- Dashboard to visualize
- Improvement targets and timeline

Output: metrics plan + implementation guide.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Common UX Patterns

**id:** `13-ui-ux-design/ux-patterns` · **Difficulty:** intermediate · **Tags:** ux-patterns, design, interaction, ui

**Placeholders:** [DESCRIBE YOUR FEATURES AND SCREENS]

````text
Apply the right UX patterns to my application.

App: [DESCRIBE YOUR FEATURES AND SCREENS]

**Navigation patterns**:
1. Hub and spoke: central home → features → back
2. Flat navigation: bottom tabs for main areas
3. Pyramid: hierarchical drill-down

**Form patterns**:
4. Progressive disclosure: show fields as needed
5. One thing per page: reduce cognitive load
6. Inline editing: edit in place without separate form

**Data display patterns**:
7. Card layout: scannable content pieces
8. Master-detail: list + detail panel (email app)
9. Timeline: chronological events

**Action patterns**:
10. Confirmation: destructive actions need confirm
11. Undo: allow undoing recent actions
12. Optimistic update: show change before server confirms

For each screen in my app: which pattern to apply and why.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a UX Research Plan

**id:** `13-ui-ux-design/ux-research` · **Difficulty:** intermediate · **Tags:** ux-research, user-testing, interviews, design

**Placeholders:** [DESCRIBE], [WHAT DO YOU WANT TO LEARN]

````text
Design a UX research plan for my product.

Product: [DESCRIBE]
Research questions: [WHAT DO YOU WANT TO LEARN]

**Research methods**:
1. **User interviews**: 5-8 qualitative sessions
   - Recruiting criteria
   - Discussion guide (10-15 questions)
   - Not leading questions
2. **Usability testing**: test specific flows
   - Tasks to complete
   - Think-aloud protocol
   - Metrics: task completion, time, errors
3. **Surveys**: quantitative at scale
   - NPS, SUS (System Usability Scale)
4. **Analytics**: behavioral data
   - Heatmaps (Hotjar), session recording
   - Funnel analysis
5. **A/B testing**: test design variants

**Research planning**:
6. Define research questions clearly
7. Choose methods that answer your questions
8. Recruit the right participants
9. Synthesize findings → insights
10. Communicate findings → design decisions

Output: research plan document.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Better UX Copy

**id:** `13-ui-ux-design/ux-writing` · **Difficulty:** beginner · **Tags:** ux-writing, copy, microcopy, design

**Placeholders:** [PASTE YOUR CURRENT UI TEXT, LABELS, ERROR MESSAGES, TOOLTIPS, BUTTONS]

````text
Improve the UX writing in my application.

Current copy that needs improvement:
```
[PASTE YOUR CURRENT UI TEXT, LABELS, ERROR MESSAGES, TOOLTIPS, BUTTONS]
```

Principles of great UX writing:
1. **Clear**: say what it does, not what it is
2. **Concise**: cut words that don't add meaning
3. **Useful**: answer the user's question before they ask it
4. **Appropriate**: match the tone to the context
5. **Human**: conversational, not corporate

Specifically improve:
6. **Button labels**: action verbs ("Delete account" not "OK")
7. **Error messages**: what happened + how to fix it
8. **Empty states**: explain why + guide to action
9. **Tooltips**: answer "why would I do this?"
10. **Confirmation dialogs**: specific consequence + reversibility

Output: before/after for every piece of copy.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create Wireframes for a New Feature

**id:** `13-ui-ux-design/wireframing` · **Difficulty:** beginner · **Tags:** wireframing, design, planning, ux

**Placeholders:** [DESCRIBE THE FEATURE], [DESCRIBE YOUR APP AND ITS PATTERNS]

````text
Create wireframes for a new feature in my application.

Feature to design: [DESCRIBE THE FEATURE]
Existing app context: [DESCRIBE YOUR APP AND ITS PATTERNS]

Outputin ASCII wireframe format:

```
┌─────────────────────────────────┐
│  Header / Navigation            │
├─────────────────────────────────┤
│  [Wireframe content here]       │
│                                 │
└─────────────────────────────────┘
```

Wireframes needed:
1. Main view (desktop + mobile)
2. Empty state (no data)
3. Loading state
4. Error state
5. Key interaction states (expanded, selected, etc.)

For each wireframe:
- What the user sees
- Interactive elements
- What happens on each action
- Edge cases addressed

Also: user flow diagram showing navigation between screens.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an accessible [COMPONENT] with [STYLING]

**id:** `13-ui-ux-design/build-an-accessible-component-with-styling` · **Difficulty:** beginner/intermediate/advanced · **Tags:** accessible, native, css, ui-ux, tailwind, design-system, framer, command, styled, dark/light, drag-and-drop, multi-step, paginated

**Variant group** (13 generated prompts collapsed). Pick one value per placeholder:
- `[STYLING]`: CSS Modules | Framer Motion animations | Styled Components | Tailwind CSS | native CSS variables
- `[COMPONENT]`: accessible modal dialogs | command palette bars | dark/light theme config panels | drag-and-drop kanban boards | multi-step wizard checkouts | paginated data tables
- `[UX_REQUIREMENT]`: fully responsive viewports | inline form validation helpers | loading skeleton blocks | smooth interface micro-animations

````text
Build a highly polished, interactive [COMPONENT] using [STYLING]. Ensure design contains [UX_REQUIREMENT] and premium aesthetics.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** build-an-accessible-accessible-modal-dialogs-with-native-css-variables, build-an-accessible-command-palette-bars-with-framer-motion-animations, build-an-accessible-command-palette-bars-with-styled-components, build-an-accessible-darklight-theme-config-panels-with-css-modules, build-an-accessible-darklight-theme-config-panels-with-native-css-variables, build-an-accessible-drag-and-drop-kanban-boards-with-css-modules, build-an-accessible-multi-step-wizard-checkouts-with-framer-motion-animations, build-an-accessible-multi-step-wizard-checkouts-with-native-css-variables, build-an-accessible-multi-step-wizard-checkouts-with-styled-components, build-an-accessible-multi-step-wizard-checkouts-with-tailwind-css, build-an-accessible-paginated-data-tables-with-native-css-variables, build-an-accessible-paginated-data-tables-with-styled-components, build-an-accessible-paginated-data-tables-with-tailwind-css


## Design a dashboard component for [COMPONENT] using [STYLING]

**id:** `13-ui-ux-design/design-a-dashboard-component-for-component-using-styling` · **Difficulty:** beginner/intermediate/advanced · **Tags:** accessible, framer, css, ui-ux, tailwind, design-system, native, styled, command, dark/light, drag-and-drop, multi-step, paginated

**Variant group** (14 generated prompts collapsed). Pick one value per placeholder:
- `[STYLING]`: CSS Modules | Framer Motion animations | Styled Components | Tailwind CSS | native CSS variables
- `[COMPONENT]`: accessible modal dialogs | command palette bars | dark/light theme config panels | drag-and-drop kanban boards | multi-step wizard checkouts | paginated data tables
- `[UX_REQUIREMENT]`: fully responsive viewports | inline form validation helpers | keyboard WAI-ARIA focus rules | loading skeleton blocks | smooth interface micro-animations

````text
Design a custom frontend component for [COMPONENT] utilizing [STYLING]. Ensure the layout scales cleanly and supports [UX_REQUIREMENT].
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** design-a-dashboard-component-for-accessible-modal-dialogs-using-framer-motion-animations, design-a-dashboard-component-for-accessible-modal-dialogs-using-native-css-variables, design-a-dashboard-component-for-accessible-modal-dialogs-using-styled-components, design-a-dashboard-component-for-accessible-modal-dialogs-using-tailwind-css, design-a-dashboard-component-for-command-palette-bars-using-css-modules, design-a-dashboard-component-for-command-palette-bars-using-framer-motion-animations, design-a-dashboard-component-for-darklight-theme-config-panels-using-framer-motion-animations, design-a-dashboard-component-for-darklight-theme-config-panels-using-native-css-variables, design-a-dashboard-component-for-darklight-theme-config-panels-using-tailwind-css, design-a-dashboard-component-for-drag-and-drop-kanban-boards-using-native-css-variables, design-a-dashboard-component-for-drag-and-drop-kanban-boards-using-styled-components, design-a-dashboard-component-for-multi-step-wizard-checkouts-using-native-css-variables, design-a-dashboard-component-for-paginated-data-tables-using-framer-motion-animations, design-a-dashboard-component-for-paginated-data-tables-using-native-css-variables

