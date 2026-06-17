---
title: "Master React Context Patterns"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, context, state-management, typescript]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement production-quality React Context patterns for [APP TYPE].

Build context for: [LIST YOUR GLOBAL STATE NEEDS]

Implement:
1. **Typed context** with TypeScript generics
2. **Null safety**: custom hook that throws if used outside provider
3. **Performance optimization**: split context to avoid unnecessary re-renders
4. **Compound component pattern**: context + parent/child composition
5. **Context with useReducer**: for complex state (like Redux but built-in)
6. **Lazy initialization**: expensive state init only runs once
7. **Context selector pattern**: subscribe to slices only

Show: when to use Context vs Zustand vs Jotai vs Redux — and why.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
