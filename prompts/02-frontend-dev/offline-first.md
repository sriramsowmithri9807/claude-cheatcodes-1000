---
title: "Build an Offline-First Web App"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pwa, offline, service-worker, indexeddb]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an offline-first version of my web app.

App type: [DESCRIBE YOUR APP AND ITS DATA]

Implement:
1. **Service Worker**: cache strategies per resource type
2. **IndexedDB**: local database for app data (using Dexie.js for nice API)
3. **Sync**: queue actions while offline, sync when reconnected (Background Sync API)
4. **Conflict resolution**: last-write-wins vs user choice
5. **Offline UI**: banner indicating offline status, disabled features that need network
6. **Optimistic offline mutations**: update local DB → sync to server
7. **Cache management**: storage quota handling, cache invalidation

Test with Chrome DevTools: offline mode + throttling.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
