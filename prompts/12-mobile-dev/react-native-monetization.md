---
title: "Add In-App Purchases to React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, iap, monetization, expo]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Add in-app purchases to my React Native app.

Using: `react-native-iap` or Expo In-App Purchases

Product types:
1. **Consumable**: one-time purchase (coin pack)
2. **Non-consumable**: permanent unlock (remove ads)
3. **Auto-renewable subscription**: monthly/annual plan

Implementation:
4. Set up products in App Store Connect + Google Play Console
5. Initialize IAP connection
6. Fetch available products
7. Purchase flow: purchase → validate receipt → unlock
8. **Receipt validation** (critical): validate on YOUR backend, not client
9. **Subscription status**: check on app launch
10. **Restore purchases**: restore button for non-consumables
11. **Error handling**: purchase cancelled, payment declined
12. **RevenueCat SDK**: simplifies all of the above (recommended)

Output: complete IAP integration with RevenueCat.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
