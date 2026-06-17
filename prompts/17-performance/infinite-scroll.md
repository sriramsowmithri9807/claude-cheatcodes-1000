---
title: "Implement High-Performance Infinite Scroll"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [infinite-scroll, performance, react, virtual]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement high-performance infinite scroll.

Data: [DESCRIBE: posts, products, messages, etc.]
Expected list size: [MAX ITEMS]

**Naive infinite scroll problems**:
- DOM grows unboundedly (thousands of nodes → slow render)
- Memory leak from non-virtualized list

**Solution: Virtual list**:
1. Only render visible items (+ a small buffer)
2. Use TanStack Virtual (React) or react-window

Implementation:
3. **TanStack Query infinite query**: `useInfiniteQuery`
4. **Intersection Observer**: detect when user reaches bottom
5. **TanStack Virtual**: virtualize the list items
6. **Loading states**: spinner at bottom, skeleton items
7. **Error recovery**: retry button on load failure
8. **Scroll restoration**: preserve scroll position on back-navigate
9. **Performance**: `memo` on list items, stable key
10. **Accessibility**: announce new items to screen reader

Output: complete infinite scroll component.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
