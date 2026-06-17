---
title: "Reverse-Engineer a Component from Description"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, components, reverse-engineer, ui]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Reverse-engineer this UI component from my description:

[DESCRIBE THE COMPONENT IN DETAIL: layout, colors, interactions, animations]

Build it as:
- React + TypeScript functional component
- Self-contained (no external UI library dependencies)
- CSS Module for styles
- Full keyboard accessibility (ARIA, focus management)
- Responsive
- Storybook story showing all states
- Props with sensible defaults

Name the component `[ComponentName]` and export it from `index.ts`.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
