---
title: "Monetize Your App"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [monetization, saas, stripe, vibe-coding]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Help me monetize my app.

App: [DESCRIBE]
Current users: [NUMBER AND TYPE OF USERS]
Value delivered: [DESCRIBE WHAT VALUE IT PROVIDES]

Monetization options:

**Subscriptions** (best for SaaS):
1. Free tier: limited features/usage
2. Pro: $X/month for full access
3. Team: $X/user/month
4. Enterprise: annual contract

**One-time payment**:
5. Lifetime access deal
6. Pay-per-use credits

**Freemium ladder**:
7. Free: enough to get hooked
8. Paid: more of what they love

**Pricing strategies**:
9. Value-based: what is it worth to them?
10. Competitor anchoring: vs alternatives
11. Per-seat: grows with their team

**Implementation** (Stripe):
12. Stripe Checkout: 15 minutes to live payments
13. Stripe Customer Portal: self-service subscription management
14. Webhooks: `customer.subscription.deleted` → downgrade

For my app:
- Which model fits best
- Suggested pricing tiers
- Stripe implementation code
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
