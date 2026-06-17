---
title: "Build a UI Patterns Library"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ui-patterns, documentation, design, components]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a UI patterns library documenting when and how to use each pattern.

App type: [DESCRIBE]

**Pattern documentation format**:
- Name and description
- When to use
- When NOT to use
- Example usage (code + visual)
- Variations
- Accessibility considerations

**Patterns to document**:
1. **Buttons**: primary, secondary, ghost, danger — when each
2. **Modals**: when modal vs page vs slide-over
3. **Toasts**: success, error, info, warning — auto vs manual dismiss
4. **Tables**: sortable, filterable, selectable, expandable rows
5. **Forms**: single column, inline, multi-step
6. **Navigation**: tabs, breadcrumbs, pagination
7. **Empty states**: first use, no results, error
8. **Loading**: skeleton, spinner, progress
9. **Cards**: media card, stats card, action card
10. **Lists**: simple, with actions, with checkboxes

Output: patterns library in Markdown format.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
