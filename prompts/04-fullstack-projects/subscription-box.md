---
title: "Build a Subscription Box Business Platform"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [subscription, ecommerce, stripe, fullstack]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
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
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
