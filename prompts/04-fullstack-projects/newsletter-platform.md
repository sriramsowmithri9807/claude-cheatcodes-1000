---
title: "Build a Newsletter Platform"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [newsletter, email, fullstack, stripe]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
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
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
