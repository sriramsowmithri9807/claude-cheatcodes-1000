---
title: "Build a Virtualized Infinite List"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, virtualization, performance, ui]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a high-performance virtualized infinite scroll list for [DATA TYPE].

Using: react-virtual or tanstack-virtual

Features:
- Renders only visible items (handles 100k+ items)
- Dynamic row heights
- Sticky headers for groups
- Infinite scroll (fetch next page when near bottom)
- Skeleton loading for initial and page loads
- Pull-to-refresh (mobile)
- Keyboard navigation (up/down arrows, page up/down)
- Jump to item by index API
- Empty, loading, error, and end-of-list states

Include the React Query integration for data fetching.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
