---
title: "Optimize React Performance"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, performance, memo, optimization]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Profile and optimize the performance of my React app.

Current issues: [DESCRIBE: slow renders, jank, high memory usage]

Optimization techniques:
1. **React.memo**: when it helps vs when it's counterproductive
2. **useMemo and useCallback**: common mistakes and correct usage
3. **React DevTools Profiler**: how to read the flame chart
4. **Context optimization**: prevent unnecessary re-renders
5. **Virtualization**: react-virtual for long lists
6. **Code splitting**: lazy() + Suspense for routes and heavy components
7. **React 18 features**: startTransition, useDeferredValue
8. **Avoid reconciliation**: stable keys, stable references

Show: before/after examples with render count measurements.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
