---
title: "Integrate Payments in React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, stripe, payments, mobile]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Integrate payment processing in my React Native app.

Using: Stripe React Native SDK

1. **Installation**: `@stripe/stripe-react-native`
2. **Setup**: StripeProvider with publishable key
3. **Payment Sheet**: prebuilt UI (easiest, most conversions)
   - Create PaymentIntent on backend
   - Initialize and present payment sheet
   - Confirm result
4. **Card field**: manual card entry form
5. **Apple Pay**: `ApplePayButton`, Works in iOS only
6. **Google Pay**: `GooglePayButton`, Android only
7. **Link (Stripe Link)**: save payment methods across merchants
8. **Subscriptions**: create subscription via backend + Stripe
9. **3D Secure**: automatically handled by Payment Sheet
10. **Receipts**: send email receipt from backend webhook
11. **Testing**: Stripe test cards (4242 4242...)

Output: complete payment integration with backend.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
