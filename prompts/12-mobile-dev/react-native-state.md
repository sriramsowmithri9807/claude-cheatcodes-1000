---
title: "State Management in React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, zustand, state, mobile]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up state management for my React Native app.

App type: [DESCRIBE]
State needs: [DESCRIBE: auth, cart, settings, real-time data, etc.]

**Options**:
1. **React Context**: for simple global state (theme, auth)
2. **Zustand**: most popular, simple, performant
3. **Jotai**: atomic state model
4. **Redux Toolkit**: for complex apps with devtools

**For MY app** (using Zustand):
5. Store setup for each domain (auth store, cart store)
6. Persist to MMKV for offline/restart persistence
7. Async actions in store
8. Selectors to prevent re-renders
9. DevTools: react-native-debugger integration
10. React Query for server state (keep server/client state separate)

Output: complete Zustand stores for my app + TanStack Query setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
