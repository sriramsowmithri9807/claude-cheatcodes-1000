---
title: "Build App Widgets for iOS and Android"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, widgets, ios, android]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build home screen widgets for my React Native app.

**iOS Widget** (SwiftUI, in Expo managed workflow via config plugin):
1. Create native iOS widget extension
2. Widget sizes: small, medium, large
3. Timeline provider: update widget data on schedule
4. App group: share data between app and widget
5. Widget configuration: user customizable
6. Deep link from widget tap to specific screen

**Android Widget** (Kotlin/Glance, similarly via config plugin):
7. AppWidgetProvider
8. RemoteViews or Jetpack Glance (Compose-based)
9. Update on alarm/broadcast

**Data sharing**:
10. App Group (iOS) / Content Provider (Android) to share data
11. React Native → widget: update when app changes data

Note: widgets require native code → use Expo Dev Client (not Go).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
