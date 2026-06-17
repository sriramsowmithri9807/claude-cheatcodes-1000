---
title: "Build a Two-Sided Marketplace"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [marketplace, stripe-connect, fullstack, payments]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
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
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
