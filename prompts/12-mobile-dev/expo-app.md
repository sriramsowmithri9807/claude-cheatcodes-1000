---
title: "Build a React Native App with Expo"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [expo, react-native, mobile, typescript]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a React Native app with Expo for: [DESCRIBE YOUR APP].

Stack: Expo SDK 51+ + TypeScript + NativeWind (Tailwind for RN)

Setup:
1. `npx create-expo-app --template` with TypeScript template
2. Folder structure: app/, components/, hooks/, utils/, constants/
3. Expo Router v3 (file-based routing)

Core features:
4. Navigation: Tab bar + Stack navigation
5. Safe area handling
6. Status bar control
7. Splash screen + app icon
8. Environment variables (EAS Secrets)

Shipping:
9. EAS Build: iOS (.ipa) + Android (.apk / .aab)
10. EAS Update: OTA updates for JS bundle
11. App Store / Play Store submission checklist

Output: complete app with [YOUR FEATURES] implemented.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
