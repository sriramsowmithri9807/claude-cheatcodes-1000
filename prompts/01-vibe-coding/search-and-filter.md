---
title: "Build Advanced Search and Filter UI"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [search, filter, react, ux]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build an advanced search and filter UI component for a [TYPE: table/list/gallery].

Data shape: [DESCRIBE YOUR DATA]

Features:
- Full-text search with debouncing (300ms)
- Multi-select filters per field
- Date range picker
- Sort by multiple columns
- URL state sync (filters persist in URL params)
- Active filter chips with remove buttons
- Clear all filters button
- Loading skeleton while fetching
- Empty state with helpful message
- Result count display

React + TypeScript, no UI library dependencies.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
