---
title: "Manage Storage in React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, storage, async-storage, sqlite]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement data persistence in my React Native app.

Data to persist: [DESCRIBE: user preferences, offline data, cache, etc.]

Storage options:
1. **AsyncStorage**: key-value for simple preferences
   - When to use: settings, auth tokens, simple state
   - Limitation: strings only, 6MB limit

2. **MMKV** (recommended over AsyncStorage):
   - 10x faster than AsyncStorage
   - Synchronous API
   - Use via react-native-mmkv

3. **SQLite** (expo-sqlite):
   - Full relational database
   - For complex offline-first data
   - DrizzleORM for SQLite in React Native

4. **Secure Storage** (expo-secure-store):
   - Keychain (iOS) / Keystore (Android)
   - For sensitive data: auth tokens, encryption keys

For my use case: which to use and implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
