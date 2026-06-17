---
title: "Choose and Implement State Management"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [redux, zustand, jotai, state]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
My app needs state management for: [DESCRIBE YOUR STATE NEEDS].

Compare and implement with the RIGHT tool:
- **Local state**: useState/useReducer — when and how
- **Zustand**: global state for most apps — show full setup
- **Jotai**: atomic state — show atoms + derived atoms
- **Redux Toolkit**: when you need time-travel and devtools

For each, implement:
- Your specific state shape
- Actions/mutations
- Async operations (thunks/queries)
- React DevTools integration
- TypeScript types throughout

Recommendation: Which one fits my use case and why.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
