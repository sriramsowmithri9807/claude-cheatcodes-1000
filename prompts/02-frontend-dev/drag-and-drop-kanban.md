---
title: "Build a Drag-and-Drop Kanban Board"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, dnd, kanban, ui]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a fully-featured Kanban board with drag and drop.

Using: @dnd-kit/core (modern, accessible alternative to react-beautiful-dnd)

Features:
- Drag cards between columns
- Drag columns to reorder
- Add/edit/delete cards (inline editing)
- Card colors and labels
- Due dates on cards
- Smooth drop animations
- Touch support (mobile drag and drop)
- Keyboard-accessible drag and drop
- Optimistic updates with rollback on error
- Persist order to backend (PATCH API call on drop)

TypeScript, no CSS framework dependency.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
