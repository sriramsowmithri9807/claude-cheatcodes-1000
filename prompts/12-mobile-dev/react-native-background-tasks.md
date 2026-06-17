---
title: "Run Background Tasks in React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, background, tasks, mobile]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Run background tasks in my React Native app.

Background needs: [DESCRIBE: location tracking, data sync, download, notifications]

**iOS background modes** (must declare in Info.plist):
1. Background fetch: periodically wake app to sync data
2. Remote notifications: wake on push to process
3. Background processing: long tasks when device charging
4. Location updates: always-on GPS tracking

**Android**:
5. WorkManager: deferrable background work (sync, upload)
6. Foreground Service: with persistent notification (location, audio)
7. JobScheduler: periodic tasks

**Expo libraries**:
8. `expo-background-fetch`: cross-platform periodic sync
9. `expo-task-manager`: define and manage background tasks
10. `expo-location`: background location tracking

Limitations: iOS aggressively limits background — understand the constraints.
Battery optimization: efficient background work.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
