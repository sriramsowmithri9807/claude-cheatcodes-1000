---
title: "Implement Progressive Loading Patterns"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [performance, loading, ux, react]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement progressive loading to make my app feel instant.

Current slow points: [DESCRIBE WHAT'S SLOW]

Patterns to implement:
1. **Skeleton screens**: anatomically correct placeholder for each section
2. **Optimistic UI**: show result before server confirms
3. **Suspense boundaries**: granular loading states per section
4. **Streaming SSR** (Next.js): progressive HTML from server
5. **Prefetching**: hover to preload next page data
6. **Stale-while-revalidate**: show old data while fetching new
7. **Critical CSS inlining**: above-the-fold CSS in `<head>`
8. **Resource hints**: `<link rel="prefetch|preload|preconnect">`

Each pattern with before (jarring UX) and after (smooth UX) code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
