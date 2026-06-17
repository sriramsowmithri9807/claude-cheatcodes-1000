---
title: "Design Beautiful Loading States"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [loading, ux, skeleton, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design comprehensive loading states for my application.

App type: [DESCRIBE]

Loading patterns:
1. **Skeleton screens**: anatomically correct placeholder matching real content shape
2. **Spinner**: when content area is small or duration unknown
3. **Progress bar**: when % known (file upload, multi-step)
4. **Optimistic UI**: show result immediately, then confirm
5. **Blur-up**: load low-res placeholder, fade in full image
6. **Progressive loading**: load critical content first
7. **Stale-while-revalidate**: show old data while fetching new

For each state:
8. Initial load: skeleton the whole page
9. Partial refresh: show spinner in specific section
10. Action feedback: button shows spinner, disables during submit
11. Background refresh: subtle indicator, don't block UI
12. Infinite scroll: spinner at bottom, not full page

Output: React components for each loading state.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
