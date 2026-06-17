---
title: "Build a Subscription/Payment System"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [stripe, subscriptions, payments, saas]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
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
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
