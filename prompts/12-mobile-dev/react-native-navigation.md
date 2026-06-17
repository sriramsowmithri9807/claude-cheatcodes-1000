---
title: "Master React Native Navigation"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, navigation, expo-router, mobile]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement navigation in my React Native app.

App structure: [DESCRIBE YOUR SCREENS AND NAVIGATION FLOW]

Using: Expo Router v3 (file-based, like Next.js for mobile)

1. **File-based routing**: app/(tabs)/, app/(auth)/, app/[id].tsx
2. **Tab navigation**: bottom tab bar with icons and badges
3. **Stack navigation**: push/pop with header customization
4. **Modal screens**: bottom sheet style modals
5. **Deep links**: handle URL scheme (myapp://post/123)
6. **Auth gates**: redirect to login if not authenticated
7. **Type-safe navigation**: typed route params
8. **Transitions**: custom animations between screens
9. **Drawer navigation**: side menu for settings
10. **Dynamic routes**: `app/posts/[id].tsx`

Output: complete navigation setup for my app structure.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
