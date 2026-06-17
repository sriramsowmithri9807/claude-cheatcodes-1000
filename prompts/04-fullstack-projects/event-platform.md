---
title: "Build an Event Management Platform"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [events, ticketing, stripe, fullstack]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
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
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
