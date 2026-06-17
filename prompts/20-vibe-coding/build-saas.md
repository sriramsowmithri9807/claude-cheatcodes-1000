---
title: "Build a SaaS Product from Scratch"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [saas, product, vibe-coding, monetization]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Help me build a SaaS product from scratch.

SaaS idea: [DESCRIBE WHAT THE SAAS DOES]
Target customer: [DESCRIBE WHO PAYS FOR IT]
Pricing idea: [ESTIMATE WHAT YOU COULD CHARGE]

SaaS foundation to build first:

**Week 1 — Core product**:
1. The one feature that provides the value
2. Make it work well enough to demo

**Week 2 — Auth + user management**:
3. Sign up, login, forgot password
4. User dashboard

**Week 3 — Payments**:
5. Stripe Checkout integration
6. Subscription management
7. Free trial flow

**Week 4 — Polish + launch**:
8. Landing page with pricing
9. Onboarding flow
10. Email notifications (welcome, failed payment)

**Tech stack for speed**:
- Next.js + TypeScript
- Supabase (auth + database)
- Stripe (payments)
- Resend (email)
- Vercel (deployment)
- Posthog (analytics)

Output: tech architecture + implementation plan + starter code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
