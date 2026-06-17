---
title: "Add a Keyboard Shortcuts System"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [accessibility, keyboard, ux, productivity]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add a comprehensive keyboard shortcut system to my React app.

Implement:
1. Global shortcut registry with conflict detection
2. Context-aware shortcuts (active only in certain components)
3. `useKeyboardShortcut(keys, handler, options)` hook
4. Shortcuts help modal (triggered by `?` key) showing all active shortcuts
5. Customizable shortcuts saved to user preferences
6. Visual shortcut hints on buttons/menu items (like Notion/Linear)
7. Sequential shortcuts (Vim-style: `g` then `h` = go home)
8. Platform-aware: show ⌘ on Mac, Ctrl on Windows

Include: escape hatch for when user is typing in an input.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
