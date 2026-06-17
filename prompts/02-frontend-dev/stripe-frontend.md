---
title: "Integrate Stripe Payment UI"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [stripe, payments, react, frontend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build the frontend payment UI for a Stripe integration.

Using: @stripe/react-stripe-js + @stripe/stripe-js

Implement:
1. **Payment form**: Card Element with custom styling to match brand
2. **Address collection**: Address Element
3. **Payment Request Button**: Apple Pay / Google Pay
4. **3D Secure handling**: redirect flow
5. **Error messages**: Stripe error code → user-friendly message
6. **Loading states**: during payment processing
7. **Success page**: order confirmation with details
8. **Subscription UI**: plan selection, current plan, upgrade/downgrade

Include: the backend API routes needed to create Payment Intents.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
