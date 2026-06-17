---
title: "Build Offline-First React Native App"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, offline, sync, mobile]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build offline-first functionality for my React Native app.

Data that needs to work offline: [DESCRIBE]

1. **Local database**: SQLite via expo-sqlite + DrizzleORM
2. **Data sync**: sync when connection is restored
3. **Conflict resolution**: last-write-wins or user choice
4. **Optimistic updates**: show result immediately, sync in background
5. **Network detection**: `@react-native-community/netinfo`
6. **Offline UI**: show offline banner, disable online-only features
7. **Background sync**: sync when app comes to foreground
8. **Retry queue**: queue failed requests, retry on reconnect
9. **Partial sync**: only sync changed records (delta sync)
10. **File sync**: cache media files for offline viewing

Pattern: TanStack Query with persistQueryClient for offline caching.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
