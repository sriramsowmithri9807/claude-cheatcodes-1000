# 04-fullstack-projects

End-to-end apps: SaaS, dashboards, marketplaces, scaffolds on Next.js/SvelteKit/Nuxt/MERN stacks.

43 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Build an Analytics Dashboard

**id:** `04-fullstack-projects/analytics-dashboard` · **Difficulty:** advanced · **Tags:** analytics, charts, react, fullstack

````text
Build a web analytics dashboard (like a lightweight Plausible or Fathom).

Stack: Next.js + ClickHouse (time-series DB) + React

Metrics to track:
1. Pageviews, unique visitors, sessions
2. Traffic sources (direct, search, social, referral)
3. Top pages by views
4. Countries and cities
5. Devices (desktop/mobile/tablet), browsers, OS
6. Bounce rate, session duration
7. Goal conversions

Dashboard features:
- Date range picker (today, 7d, 30d, custom)
- Real-time visitors (WebSocket)
- Comparison to previous period
- Charts: line, bar, donut

Data collection: lightweight JS snippet (< 1KB, no cookies, GDPR-friendly)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Medical Appointment Booking System

**id:** `04-fullstack-projects/appointment-booking` · **Difficulty:** advanced · **Tags:** appointments, healthcare, fullstack, calendar

````text
Build a medical appointment booking system.

Stack: Next.js + PostgreSQL + Twilio (SMS) + Stripe

Roles: Admin, Doctor, Patient

Features:
1. Doctors: set weekly availability, blocked dates, appointment types
2. Patients: find doctor, view calendar, book appointment
3. Appointment types: consultation (30min), follow-up (15min), procedure (60min)
4. Confirmation: email + SMS to patient and doctor
5. Reminders: 24h and 2h before (SMS + email)
6. Telemedicine: virtual appointments with video link
7. Medical records: doctor adds notes after appointment (patient can view)
8. Insurance: collect insurance info at booking
9. Cancellation: with configurable advance notice requirement
10. Waitlist: patient joins if slot becomes available
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Modern Blog Platform

**id:** `04-fullstack-projects/blog-platform` · **Difficulty:** intermediate · **Tags:** blog, nextjs, mdx, cms

````text
Build a developer blog platform like Hashnode or Dev.to.

Stack: Next.js 14 + MDX + PostgreSQL + Prisma + Cloudinary

Features:
1. Write posts in MDX (Markdown + React components)
2. Syntax highlighted code blocks
3. Tag system with exploration
4. Reactions (like, unicorn, bookmark)
5. Comments with nested replies
6. Reading progress bar
7. Related posts
8. Author profiles
9. RSS feed
10. Newsletter integration (subscribe to author)
11. SEO: OG images, sitemap, structured data
12. Admin: unpublished drafts, scheduled publishing
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Booking/Scheduling System

**id:** `04-fullstack-projects/booking-system` · **Difficulty:** advanced · **Tags:** booking, calendar, fullstack, stripe

````text
Build a Calendly-style booking and scheduling system.

Stack: Next.js + PostgreSQL + Stripe + SendGrid

Features:
1. User creates event types (30 min meeting, 1 hour call, etc.)
2. User sets availability windows per day of week
3. Buffer time between bookings
4. Booking page: calendar picker showing available slots
5. Booking confirmation: form (name, email, reason)
6. Invitee gets confirmation email + calendar invite (.ics)
7. Host gets notification + can reschedule/cancel
8. Time zone handling (IANA tz, no ambiguity)
9. Google Calendar integration (check conflicts, add events)
10. Stripe: charge for premium event types
11. Reminders: email 24h and 1h before
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Real-Time Chat App

**id:** `04-fullstack-projects/chat-application` · **Difficulty:** advanced · **Tags:** chat, websockets, react, fullstack

````text
Build a Slack-style real-time chat application.

Stack: React + Node.js + Socket.io + PostgreSQL + Redis

Features:
1. Workspaces and channels
2. Direct messages (1:1 and group DMs)
3. Real-time messaging with delivery receipts
4. Typing indicators
5. Message reactions (emoji)
6. Thread replies
7. File attachments (images auto-preview)
8. User presence (online/offline/away)
9. Message search
10. Notifications: desktop push, unread counts, mention alerts
11. Mobile responsive

Architecture: Socket.io rooms for channels, Redis adapter for scaling.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Code Snippet Manager

**id:** `04-fullstack-projects/code-snippet-manager` · **Difficulty:** intermediate · **Tags:** snippets, developer-tools, fullstack, search

````text
Build a developer code snippet manager (like Carbon or Ray.so but with search and sharing).

Stack: Next.js + PostgreSQL + Prism.js (syntax highlighting)

Features:
1. Create snippets: title, description, code, language, tags
2. Syntax highlighting for 50+ languages
3. Collections / folders
4. Full-text search (content + title + tags)
5. Public snippets: shareable URL with beautiful code rendering
6. Private snippets: only visible to owner
7. Embed code: `<iframe>` embed for blogs/docs
8. VS Code extension: save snippet from editor, search from command palette
9. Copy to clipboard with one click
10. Import from GitHub Gist
11. AI: explain snippet, generate similar snippet (Claude API)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a CRM System

**id:** `04-fullstack-projects/crm-system` · **Difficulty:** advanced · **Tags:** crm, nextjs, fullstack, business

````text
Build a lightweight CRM for a small sales team.

Stack: Next.js + PostgreSQL + Prisma

Features:
1. **Contacts**: name, company, email, phone, custom fields, tags
2. **Companies**: associated contacts, deals
3. **Deals/Pipeline**: kanban view by stage (Lead → Qualified → Proposal → Won/Lost)
4. **Activities**: log calls, emails, meetings against a contact/deal
5. **Tasks**: follow-up reminders with due dates
6. **Notes**: rich text notes on any record
7. **Email integration**: log emails from Gmail/Outlook
8. **Reports**: win rate, pipeline value, activity by rep
9. **Import**: bulk import from CSV
10. **Team**: assign contacts/deals to sales reps

DB schema + complete API + key UI components.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Crowdfunding Platform

**id:** `04-fullstack-projects/crowdfunding-platform` · **Difficulty:** advanced · **Tags:** crowdfunding, stripe, fullstack, community

````text
Build a Kickstarter-style crowdfunding platform.

Stack: Next.js + PostgreSQL + Stripe + Cloudinary

Features:
1. Project creation: title, story (rich text), goal, deadline, rewards
2. Rewards: backer tiers with perks and quantity limits
3. Funding: pledge (Stripe Payment Intent, charged only if goal met)
4. Progress: funding bar, % funded, backers count, days left
5. Comments and updates from creator
6. Backer dashboard: all pledges, downloadable rewards
7. Creator dashboard: funding stats, backer export, send updates
8. Refund: auto-refund if goal not reached by deadline
9. Discovery: categories, trending, ending soon
10. Social: share buttons, embed widget

Stripe hold → capture on success / cancel on failure is the key flow.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Customer Support Ticketing System

**id:** `04-fullstack-projects/customer-support` · **Difficulty:** advanced · **Tags:** support, helpdesk, fullstack, email

````text
Build a Zendesk-style customer support system.

Stack: Next.js + Node.js + PostgreSQL + SendGrid

Roles: Customer, Agent, Admin

Features:
1. Customers: submit ticket via web form or email
2. Email ingestion: support@company.com → creates ticket automatically
3. Ticket lifecycle: Open → In Progress → Resolved → Closed
4. Assignment: route to agent by category/round-robin
5. Internal notes: agents communicate privately
6. SLA: first response < 4h, resolution < 24h — track and alert
7. CSAT: post-resolution survey
8. Knowledge base: articles that auto-suggest when customer types ticket
9. AI first response: Claude drafts suggested reply for agent review
10. Reporting: ticket volume, response times, CSAT scores
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Matching/Dating App

**id:** `04-fullstack-projects/dating-app` · **Difficulty:** advanced · **Tags:** matching, swipe, fullstack, real-time

````text
Build a dating/matching app (Tinder-style).

Stack: React Native (Expo) + Node.js + PostgreSQL + Redis + Socket.io

Core features:
1. Profile: photos, bio, age, location, preferences
2. Discovery: swipe right (like), left (pass), super-like
3. Matching algorithm: only match if both swipe right
4. Chat: real-time messages with Socket.io
5. Photo upload: multiple photos, drag to reorder
6. Geolocation: show profiles within X km
7. Filters: age range, distance, interests
8. Push notifications: new match, new message
9. Boost: increase visibility temporarily
10. Report/block: safety features

Privacy: hide last active time, control who sees your profile.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Collaborative Document Editor

**id:** `04-fullstack-projects/document-editor` · **Difficulty:** advanced · **Tags:** editor, collaboration, yjs, fullstack

````text
Build a Google Docs-style collaborative document editor.

Stack: Next.js + Node.js + Yjs + y-websocket + Tiptap + PostgreSQL

Features:
1. Rich text editor: headings, bold/italic, lists, tables, images, code blocks
2. Real-time collaboration: multiple users edit simultaneously (CRDT-powered)
3. Cursor presence: see other users' cursors with name labels
4. Comments: highlight text → add comment → reply thread
5. Version history: restore to any past version
6. Share: private, view-only link, public
7. Export: PDF, Word (.docx), Markdown
8. Templates: start from pre-made document templates
9. Table of contents: auto-generated from headings
10. Word count, reading time stats
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an E-Commerce Platform

**id:** `04-fullstack-projects/ecommerce-platform` · **Difficulty:** advanced · **Tags:** ecommerce, nextjs, stripe, fullstack

````text
Build a full e-commerce platform from scratch.

Stack: Next.js 14 + TypeScript + PostgreSQL + Stripe + Cloudinary

Features:
1. **Product catalog**: list, search, filter, categories
2. **Product page**: images, description, variants (size/color), stock
3. **Cart**: add/remove, quantity, persist in localStorage or session
4. **Checkout**: Stripe Payment Element, address, shipping options
5. **Orders**: order history, order detail, status tracking
6. **Auth**: customer accounts, guest checkout
7. **Admin**: add/edit products, manage orders, inventory
8. **Email**: order confirmation, shipping notification

Database schema + all API routes + key UI components included.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an Event Management Platform

**id:** `04-fullstack-projects/event-platform` · **Difficulty:** advanced · **Tags:** events, ticketing, stripe, fullstack

````text
Build an Eventbrite-style event management platform.

Stack: Next.js + PostgreSQL + Stripe + SendGrid + MapBox

Features:
1. Create events: title, description, date/time, location (map), category
2. Ticket types: free, paid, donation; quantity limits; early bird pricing
3. Registration flow: select tickets → Stripe checkout → confirmation email
4. QR code tickets: generate per attendee, scan at door
5. Event dashboard: attendee list, revenue, check-in stats
6. Discovery: map view of nearby events, category browse
7. Calendar: add to Google/Apple Calendar
8. Virtual events: embed Zoom/Meet link (shown only to registered)
9. Recurring events
10. Waitlist: when sold out, notify on cancellations
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Personal Finance Tracker

**id:** `04-fullstack-projects/expense-tracker` · **Difficulty:** intermediate · **Tags:** finance, fullstack, charts, react

````text
Build a personal finance and expense tracker app.

Stack: Next.js + PostgreSQL + Plaid API

Features:
1. Manual transaction entry: amount, category, date, note
2. Bank account connection via Plaid (automatic import)
3. Category management: custom categories with budgets
4. Budget tracking: progress bars, overspend alerts
5. Monthly summary: income vs expenses, savings rate
6. Charts: spending by category (donut), trend over time (line)
7. Recurring transactions: detect and label subscriptions
8. Net worth tracker: assets vs liabilities
9. Export to CSV for taxes
10. Multi-currency support

Full implementation with Plaid integration or CSV import fallback.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Fitness Tracking App

**id:** `04-fullstack-projects/fitness-tracker` · **Difficulty:** intermediate · **Tags:** fitness, health, react-native, fullstack

````text
Build a fitness tracking app.

Stack: React Native (Expo) + Node.js + PostgreSQL

Features:
1. Workout templates: create routines with exercises, sets, reps, weight
2. Workout logging: log today's workout, track personal bests
3. Exercise library: 200+ exercises with instructions and muscle groups
4. Progress charts: weight lifted over time, volume per muscle group
5. Body measurements: weight, body fat %, measurements log
6. Calendar: view past workouts, streaks
7. Rest timer: countdown between sets
8. HealthKit / Google Fit integration: import steps, heart rate
9. Share workout: generate image summary
10. AI coach: suggest next workout based on history (Claude API)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Forum Platform

**id:** `04-fullstack-projects/forum-platform` · **Difficulty:** intermediate · **Tags:** forum, community, nextjs, fullstack

````text
Build a Reddit-style forum platform.

Stack: Next.js + PostgreSQL + Redis

Features:
1. Communities (subreddits) with moderation
2. Posts: link, text, image, video
3. Voting: upvote/downvote, Reddit-style karma
4. Comments: nested, collapsible, sorted by best/new/top
5. User profiles: karma, post/comment history
6. Moderation: remove posts, ban users, mod queue
7. Trending: hot algorithm (score + time decay)
8. Search: across posts and communities
9. Flair: user and post flair
10. Cross-posting
11. Markdown in posts and comments
12. Email digest of top posts
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Habit Tracker App

**id:** `04-fullstack-projects/habit-tracker` · **Difficulty:** intermediate · **Tags:** habits, react, fullstack, gamification

````text
Build a habit tracking app with gamification.

Stack: React Native (Expo) or Next.js PWA + PostgreSQL

Features:
1. Create habits: name, icon, target frequency (daily/weekly/specific days)
2. Log completion: mark habit as done for today
3. Streak tracking: current streak and longest streak
4. Visualizations: GitHub-style contribution heatmap, weekly bar chart
5. Statistics: completion rate, best streak, total completions
6. Reminders: push notifications at set time
7. Gamification: XP, level up, badges for milestones
8. Categories: health, fitness, learning, creativity
9. Notes: add context when logging
10. Social: share progress (opt-in), follow friends' habits

Full DB schema + API + UI with beautiful animations.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Point of Sale System

**id:** `04-fullstack-projects/inventory-pos` · **Difficulty:** advanced · **Tags:** pos, retail, stripe, fullstack

````text
Build a Point of Sale (POS) system for a retail store.

Stack: React + Node.js + PostgreSQL + Stripe Terminal

Features:
1. Product lookup: barcode scan or search by name
2. Cart: add items, quantity, discounts, remove
3. Payment: card via Stripe Terminal, cash, split payment
4. Receipt: print (ESC/POS) or email
5. Refunds: partial or full, back to payment method
6. Customer: create/find customer account, loyalty points
7. End-of-day report: sales summary, by payment method
8. Inventory sync: sales auto-decrement stock
9. Offline mode: queue sales when internet drops, sync when reconnected
10. Multi-register: multiple terminals in same store
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an Inventory Management System

**id:** `04-fullstack-projects/inventory-system` · **Difficulty:** intermediate · **Tags:** inventory, react, fullstack, business

````text
Build a small business inventory management system.

Stack: React + Node.js + PostgreSQL

Features:
1. Product catalog with variants (SKU, price, cost, barcode)
2. Stock levels with low-stock alerts
3. Receive stock: purchase orders, supplier management
4. Sales: record sales, update stock automatically
5. Multi-location: manage stock across multiple stores/warehouses
6. Transfers between locations
7. Reports: inventory value, top sellers, stock history
8. Barcode scanner support (camera or USB scanner)
9. CSV import/export
10. Role-based access: manager vs staff

DB schema + API + key UI screens.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an IoT Data Dashboard

**id:** `04-fullstack-projects/iot-dashboard` · **Difficulty:** advanced · **Tags:** iot, mqtt, websockets, fullstack

````text
Build an IoT data collection and visualization dashboard.

Stack: Node.js + MQTT + InfluxDB (time-series) + React + WebSocket

Architecture:
1. **MQTT broker**: receive telemetry from IoT devices
2. **Ingestion service**: subscribe to MQTT, validate, write to InfluxDB
3. **REST API**: query historical data, manage devices
4. **WebSocket**: push live sensor data to dashboard
5. **Dashboard**: real-time gauges, time-series charts, device map
6. **Alerting**: threshold alerts (temperature > 80°C → notify)
7. **Device management**: register devices, see status, last seen
8. **Data retention**: auto-delete data older than 90 days

Example devices: temperature sensors, energy monitors, GPS trackers.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Job Board

**id:** `04-fullstack-projects/job-board` · **Difficulty:** intermediate · **Tags:** job-board, nextjs, fullstack, search

````text
Build a job board like Hacker News: Who is hiring.

Stack: Next.js + TypeScript + PostgreSQL + Stripe

Features:
1. Job listings: title, company, location, salary range, tags, description
2. Search: full-text + filter by category/location/remote/salary
3. Job detail page with apply button
4. Employer dashboard: post jobs, view applications
5. Job seeker: save jobs, apply, track applications
6. Email alerts for new matching jobs
7. Company profiles
8. Pricing: free (1 listing) vs paid (featured, unlimited)
9. Admin: approve/reject listings
10. SEO: each listing is a public indexed page

Full implementation with DB schema and key routes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Learning Management System

**id:** `04-fullstack-projects/learning-management` · **Difficulty:** advanced · **Tags:** lms, education, video, fullstack

````text
Build a Udemy-style Learning Management System (LMS).

Stack: Next.js + PostgreSQL + S3 + Stripe

Features:
1. **Course catalog**: browse, search, filter by category/price/rating
2. **Course detail**: description, curriculum, instructor, reviews, preview video
3. **Video player**: custom player with progress tracking
4. **Enrollment**: Stripe one-time payment or subscription
5. **Course player**: lesson navigation, completion tracking, notes
6. **Quiz/Assessment**: at the end of sections
7. **Certificate**: auto-generate PDF on course completion
8. **Instructor dashboard**: create courses, upload videos, view analytics
9. **Student dashboard**: enrolled courses, progress
10. **Reviews and ratings system**

Key technical challenge: video streaming with resume from where left off.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Two-Sided Marketplace

**id:** `04-fullstack-projects/marketplace` · **Difficulty:** advanced · **Tags:** marketplace, stripe-connect, fullstack, payments

````text
Build a two-sided marketplace (like Airbnb, Etsy, Fiverr).

Stack: Next.js + PostgreSQL + Stripe Connect

Core features:
1. **Sellers**: create listings, manage inventory, view orders, payouts
2. **Buyers**: browse, search, filter, buy, review
3. **Payments**: Stripe Connect (marketplace payments with platform fee)
4. **Escrow**: hold payment until buyer confirms delivery
5. **Reviews**: two-way reviews (buyer reviews seller and vice versa)
6. **Disputes**: flag orders, admin resolution
7. **Messaging**: buyer ↔ seller chat
8. **Categories and SEO**: each listing indexed by Google
9. **Search**: full-text + faceted filters
10. **Admin panel**: approve listings, manage disputes, see revenue

Stripe Connect onboarding flow is the most complex part — show fully.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Newsletter Platform

**id:** `04-fullstack-projects/newsletter-platform` · **Difficulty:** advanced · **Tags:** newsletter, email, fullstack, stripe

````text
Build a Substack-style newsletter platform.

Stack: Next.js + PostgreSQL + Resend + Stripe

Features:
1. Writer: create newsletter, publish posts (markdown editor)
2. Subscribers: free and paid tiers
3. Subscription management: Stripe for paid subscriptions
4. Send: trigger email delivery to all subscribers on publish
5. Archive: public archive of all posts
6. Subscribe widget: embeddable `<iframe>` for other websites
7. Unsubscribe: one-click, respect immediately
8. Analytics per post: opens, clicks, unsubscribes
9. Comments on posts
10. Writer dashboard: subscriber count, revenue, post performance

Email delivery must handle thousands of recipients (queue-based).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Note-Taking App

**id:** `04-fullstack-projects/note-taking-app` · **Difficulty:** intermediate · **Tags:** notes, editor, react, fullstack

````text
Build a Notion-lite note-taking app.

Stack: Next.js + PostgreSQL + Tiptap editor

Features:
1. Block-based editor: text, heading, bullet list, numbered list, code, image, divider
2. Slash command: / to insert blocks
3. Drag to reorder blocks
4. Nested pages (tree structure in sidebar)
5. Full-text search across all notes
6. Tags and favorites
7. Share note: public read-only URL
8. Real-time autosave (debounced, no manual save needed)
9. Markdown import/export
10. Dark mode

Optional: real-time collaboration with Yjs
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Podcast Hosting Platform

**id:** `04-fullstack-projects/podcast-platform` · **Difficulty:** advanced · **Tags:** podcast, audio, streaming, fullstack

````text
Build a podcast hosting and discovery platform.

Stack: Next.js + Node.js + S3 + PostgreSQL

Features:
1. Upload episodes: MP3/M4A, title, description, show notes, episode number
2. RSS feed generation (valid podcast RSS with all required tags)
3. Web player: custom HTML5 audio player with chapters support
4. Auto-submit to Apple Podcasts, Spotify (show RSS URL)
5. Transcription: auto-transcribe with Whisper API
6. Show notes: rich text editor with timestamps
7. Analytics: downloads per episode, listener geography (private feed tokens)
8. Embeddable player widget
9. Subscription: email list of listeners
10. Monetization: supporter donations (Stripe)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Project Management App

**id:** `04-fullstack-projects/project-management-app` · **Difficulty:** advanced · **Tags:** project-management, react, fullstack, kanban

````text
Build a Linear/Jira-style project management app.

Stack: React + Node.js + PostgreSQL + Socket.io

Features:
1. Projects and workspaces
2. Issues: create, assign, priority, status, labels
3. Kanban board with drag-and-drop
4. List view with sorting/filtering
5. Roadmap/timeline view
6. Comments on issues (with mentions)
7. Activity feed per issue
8. Team members and permissions
9. Real-time updates (collaborator sees your changes instantly)
10. Keyboard shortcuts (Linear-style)

Full schema, API design, and component architecture.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an Online Quiz Platform

**id:** `04-fullstack-projects/quiz-platform` · **Difficulty:** intermediate · **Tags:** quiz, education, fullstack, gamification

````text
Build an online quiz and assessment platform.

Stack: Next.js + PostgreSQL + Socket.io

Features:
1. Question types: multiple choice, true/false, short answer, code challenge
2. Quiz builder: add questions, set time limit, configure scoring
3. Taking a quiz: countdown timer, progress indicator
4. Live quiz mode: host shares code → participants join → play in real-time
5. Leaderboard: live standings during quiz
6. Results: score, correct answers, explanations
7. Analytics: per-question performance, average score
8. Import questions from CSV
9. Public quiz library: share your quizzes
10. Certificates on completion (PDF)
11. AI question generator: paste topic → generate 10 questions (Claude API)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Real Estate Listing Platform

**id:** `04-fullstack-projects/real-estate-platform` · **Difficulty:** advanced · **Tags:** real-estate, maps, search, fullstack

````text
Build a real estate listing platform (like Zillow).

Stack: Next.js + PostgreSQL + MapBox + Cloudinary

Features:
1. Listings: address, price, beds, baths, sqft, photos, description
2. Map view: cluster pins by area, click to see listing
3. List view: grid of cards with key details
4. Search: by address/city/zip, filter by price/beds/type
5. Saved searches: alert on new matching listings
6. Favorite properties
7. Property detail: full gallery, map, neighborhood stats, similar homes
8. Mortgage calculator
9. Request viewing: contact agent form
10. Agent profiles: their listings, contact info

SEO: each listing is a public page indexed by Google.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Recipe Sharing Platform

**id:** `04-fullstack-projects/recipe-platform` · **Difficulty:** intermediate · **Tags:** recipe, community, nextjs, fullstack

````text
Build a recipe sharing platform (like AllRecipes).

Stack: Next.js + PostgreSQL + Cloudinary

Features:
1. Recipe: title, description, ingredients (with amounts), instructions (steps)
2. Media: multiple photos, optional video
3. Tags: cuisine, diet (vegan/gluten-free), meal type, difficulty
4. Servings scaling: user changes servings → amounts scale automatically
5. Save / bookmark recipes
6. Rating and reviews
7. User profiles with collection of recipes
8. Search: full-text + filter by dietary restrictions
9. Meal planner: drag recipes to weekly calendar
10. Shopping list: combine ingredients from planned meals (deduplicate)
11. AI ingredient substitutions (Claude API)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Resume Builder

**id:** `04-fullstack-projects/resume-builder` · **Difficulty:** intermediate · **Tags:** resume, pdf, react, fullstack

````text
Build an online resume builder that generates beautiful PDFs.

Stack: Next.js + PostgreSQL + react-pdf

Features:
1. Sections: contact, summary, experience, education, skills, projects, certifications
2. Multiple templates: modern, classic, minimal, creative
3. Live preview: see changes in real-time
4. Export: PDF + ATS-friendly plain text
5. AI enhancement: improve bullet points (Claude API)
6. ATS score: analyze against a job description
7. Shareable URL: public resume page
8. Version history: save multiple versions
9. Import from LinkedIn
10. Cover letter generator (AI)

React PDF renders the exact same layout in both preview and export.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Review and Rating Platform

**id:** `04-fullstack-projects/review-platform` · **Difficulty:** intermediate · **Tags:** reviews, ratings, fullstack, community

````text
Build a product/business review platform (like Trustpilot or G2).

Stack: Next.js + PostgreSQL + Algolia (search)

Features:
1. Businesses claim their profile
2. Customers write reviews: rating (1-5 stars), text, pros/cons, verified purchase badge
3. Business response to reviews
4. Helpful votes on reviews
5. Fake review detection: velocity checks, account age requirements
6. Review widgets: embeddable badge for business websites
7. Search: find businesses by name or category
8. Compare: side-by-side comparison of 2-3 businesses
9. Featured reviews: AI summary of sentiment (Claude API)
10. Report inappropriate reviews
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a SaaS Admin Panel

**id:** `04-fullstack-projects/saas-admin-panel` · **Difficulty:** intermediate · **Tags:** admin, saas, fullstack, dashboard

````text
Build a complete admin panel for a SaaS application.

Stack: React + Node.js + PostgreSQL

Sections:
1. **Dashboard**: total users, MRR, churn, signups this month, active now
2. **Users**: search, filter by plan, view profile, impersonate, ban, delete
3. **Subscriptions**: all subs, by plan, revenue per plan, churned subs
4. **Feature flags**: enable/disable features per user or globally
5. **Announcements**: send in-app banner to all users
6. **Email campaigns**: send one-off email to user segments
7. **Audit log**: all admin actions logged
8. **Database explorer**: safe read-only SQL queries
9. **API keys**: view all API keys, revoke
10. **System health**: uptime, queue depth, error rate

Secure: admin-only routes with 2FA requirement.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Complete SaaS Starter Kit

**id:** `04-fullstack-projects/saas-starter` · **Difficulty:** advanced · **Tags:** saas, nextjs, stripe, auth

````text
Build a complete, production-ready SaaS starter kit.

Tech stack:
- Frontend: Next.js 14 App Router + TypeScript
- Auth: Auth.js v5
- Database: PostgreSQL + Prisma ORM
- Payments: Stripe subscriptions
- Email: Resend
- UI: shadcn/ui
- Deployment: Vercel + Supabase

Features to include:
1. Auth: signup, login, OAuth (Google/GitHub), email verify, password reset
2. Stripe: checkout, webhooks, customer portal, subscription status
3. Dashboard: overview, settings, billing page
4. Team/org support: invite members, roles (owner/admin/member)
5. API: public API with API key generation
6. Admin: user management panel

Output: complete folder structure + all core files.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Social Media App

**id:** `04-fullstack-projects/social-media-app` · **Difficulty:** advanced · **Tags:** social, nextjs, fullstack, real-time

````text
Build a Twitter/X-style social media app.

Stack: Next.js + TypeScript + Prisma + PostgreSQL + Socket.io

Core features:
1. Posts: create, like, repost, quote, delete
2. Media: attach images/videos to posts
3. Feed: following timeline + explore tab
4. Follow/unfollow users
5. Notifications: likes, follows, mentions (real-time)
6. Search: users and posts
7. DMs: real-time direct messages
8. User profile: bio, avatar, follower/following counts
9. Hashtags: trending, click to explore
10. Auth: signup with username selection

Full database schema + API routes + React components.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Subscription Box Business Platform

**id:** `04-fullstack-projects/subscription-box` · **Difficulty:** advanced · **Tags:** subscription, ecommerce, stripe, fullstack

````text
Build a complete platform for a subscription box business.

Stack: Next.js + PostgreSQL + Stripe + Shippo

Features:
1. **Landing page**: product imagery, what's in the box, testimonials, subscribe CTA
2. **Subscribe flow**: choose plan (monthly/quarterly/annual), Stripe, shipping address
3. **Subscriber portal**: manage subscription, skip month, cancel, change address
4. **Box management**: admin creates box contents per cycle
5. **Fulfillment**: generate packing slips, create shipments via Shippo API
6. **Tracking**: send tracking emails, customers track in portal
7. **Referral program**: unique referral link, credit for successful referrals
8. **Churn prevention**: cancel flow with pause option + discount offer
9. **Analytics**: MRR, churn rate, active subscribers
10. **Inventory**: track stock per item, alert when low
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a No-Code Task Automation Platform

**id:** `04-fullstack-projects/task-automation` · **Difficulty:** advanced · **Tags:** automation, workflows, fullstack, no-code

````text
Build a simple Zapier-style automation platform.

Stack: Next.js + Node.js + BullMQ + PostgreSQL

Concepts:
- **Triggers**: events that start a workflow (webhook, schedule, form submission)
- **Actions**: things that happen (send email, HTTP request, DB insert, Slack message)
- **Workflows**: chain of trigger + multiple actions

Implement:
1. Workflow builder UI (visual flow editor)
2. Trigger types: Webhook, Schedule (cron), Manual
3. Action types: HTTP Request, Send Email, Slack Webhook, Database Insert
4. Data mapping: pass data between trigger and actions
5. Workflow runs history: success/failure/payload
6. Error handling: retry failed actions
7. Webhook URL generation per workflow
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an AI Travel Planner

**id:** `04-fullstack-projects/travel-planner` · **Difficulty:** intermediate · **Tags:** travel, ai, fullstack, maps

````text
Build an AI-powered travel itinerary planner.

Stack: Next.js + Claude API + PostgreSQL + MapBox

Features:
1. Input: destination, dates, number of travelers, budget, interests
2. AI generation: Claude generates day-by-day itinerary
3. Itinerary display: timeline view with activities, restaurants, hotels
4. Map integration: plot all locations on interactive map
5. Save itinerary to account
6. Edit: add/remove/reorder activities
7. Collaboration: share with travel companions (they can suggest edits)
8. Export: PDF itinerary + calendar events (.ics)
9. Packing list: AI-generated based on destination + activities
10. Budget breakdown: estimated costs per day

Claude prompt engineering: get structured JSON itinerary.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a URL Shortener Service

**id:** `04-fullstack-projects/url-shortener` · **Difficulty:** intermediate · **Tags:** url-shortener, redis, analytics, fullstack

````text
Build a URL shortener with analytics (like Bit.ly).

Stack: Node.js + Redis + PostgreSQL + Next.js

Features:
1. Shorten any URL: generate 6-char base62 code
2. Custom aliases: user picks their own slug
3. QR code generation
4. Redirect: GET /:code → 301 redirect (cache in Redis, 1ms response)
5. Analytics per link: clicks, unique visitors, countries, referrers, devices
6. Click tracking: async (don't slow the redirect)
7. Link expiry: optional TTL
8. Password-protected links
9. API: programmatic shortening with API key
10. Dashboard: all links, stats, delete, edit

Performance target: redirect in < 5ms (Redis-first lookup).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Video Streaming Platform

**id:** `04-fullstack-projects/video-platform` · **Difficulty:** advanced · **Tags:** video, streaming, fullstack, s3

````text
Build a YouTube-style video platform.

Stack: Next.js + Node.js + PostgreSQL + AWS S3 + CloudFront + FFmpeg

Features:
1. **Upload**: multipart upload to S3, show progress
2. **Processing**: FFmpeg transcoding (1080p, 720p, 480p HLS)
3. **Player**: HLS.js player with quality selector, playback speed, captions
4. **Thumbnails**: auto-generate at 25%, 50%, 75% + user-set custom thumbnail
5. **Metadata**: title, description, tags, category, visibility
6. **Engagement**: likes, comments, subscribe
7. **Recommendations**: related videos
8. **Search**: title + description full-text
9. **Analytics**: views, watch time, traffic sources (for creators)
10. **Monetization**: tip button or membership (Stripe)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Pre-Launch Waitlist System

**id:** `04-fullstack-projects/waitlist-system` · **Difficulty:** intermediate · **Tags:** waitlist, viral, marketing, fullstack

````text
Build a viral pre-launch waitlist system.

Stack: Next.js + PostgreSQL + Resend

Features:
1. Landing page with email capture
2. Thank you page: shows referral link immediately
3. Referral tracking: get N spots higher for each referral
4. Leaderboard: top referrers (public)
5. Email confirmation with referral link
6. Progress email: "You've moved up X spots!"
7. Social share buttons: Twitter, WhatsApp, copy link
8. Admin: view all signups, approve in batches
9. Launch email: notify approved users
10. Analytics: conversion rate, referral source, viral coefficient

Make the referral mechanic feel gamified and exciting.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Add [FEATURE] to a [STACK] application

**id:** `04-fullstack-projects/add-feature-to-a-stack-application` · **Difficulty:** intermediate/advanced · **Tags:** web-app, fullstack, next.js, nextjs, angular, react

**Variant group** (3 generated prompts collapsed). Pick one value per placeholder:
- `[STACK]`: Angular + NestJS + MongoDB | Next.js + Supabase | React + Express + PostgreSQL
- `[APP]`: a project task manager | a social network MVP
- `[FEATURE]`: Auth0 social login | Stripe billing and subscription flow | role-based access control (RBAC)

````text
Implement [FEATURE] in a full-stack [APP] built on [STACK]. Ensure end-to-end security and clean forms validation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** add-auth0-social-login-to-a-nextjs-supabase-application, add-role-based-access-control-rbac-to-a-angular-nestjs-mongodb-application, add-stripe-billing-and-subscription-flow-to-a-react-express-postgresql-application


## Scaffold [APP] with [STACK]

**id:** `04-fullstack-projects/scaffold-app-with-stack` · **Difficulty:** beginner/intermediate · **Tags:** web-app, fullstack, vue, nextjs, react, angular, sveltekit

**Variant group** (6 generated prompts collapsed). Pick one value per placeholder:
- `[STACK]`: Angular + NestJS + MongoDB | React + Express + PostgreSQL | SvelteKit + Prisma | Vue 3 (Nuxt.js) + Go
- `[APP]`: a booking and scheduling system | a client onboarding portal | a project task manager | a real-time dashboard | a social network MVP
- `[FEATURE]`: Resend automated email notifications | Stripe billing and subscription flow | Tailwind CSS responsive layout | WebSockets real-time sync

````text
Scaffold [APP] using [STACK]. Include [FEATURE], state management, and a clean folder layout.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** scaffold-a-booking-and-scheduling-system-with-vue-3-nuxtjs-go, scaffold-a-client-onboarding-portal-with-react-express-postgresql, scaffold-a-project-task-manager-with-react-express-postgresql, scaffold-a-real-time-dashboard-with-angular-nestjs-mongodb, scaffold-a-real-time-dashboard-with-sveltekit-prisma, scaffold-a-social-network-mvp-with-vue-3-nuxtjs-go

