---
title: "Build a Booking/Scheduling System"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [booking, calendar, fullstack, stripe]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
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
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
