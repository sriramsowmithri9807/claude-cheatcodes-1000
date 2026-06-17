---
title: "Optimize React Application Performance"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, performance, memoization, rendering]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my React application's rendering performance.

App: [DESCRIBE]
Symptoms: [DESCRIBE: slow renders, janky animations, high memory usage]

**Profiling**:
1. React DevTools Profiler: find expensive renders
2. Chrome Performance tab: find long tasks
3. Why-did-you-render: log unnecessary re-renders

**Memoization**:
4. `React.memo()`: prevent re-render if props unchanged
5. `useMemo()`: expensive computations
6. `useCallback()`: stable function references
7. When NOT to memoize: premature optimization

**State management**:
8. Colocate state: don't lift state higher than needed
9. Split contexts: separate frequently-changing state
10. Zustand selectors: re-render only on relevant state change

**Lists**:
11. Virtual lists: TanStack Virtual for large lists
12. Stable keys: avoid index-as-key when order changes

**Data fetching**:
13. TanStack Query: background refresh, no loading flash
14. Suspense: progressive loading

Output: specific optimizations for my app with measurements.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
