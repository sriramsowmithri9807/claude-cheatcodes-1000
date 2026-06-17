---
title: "Build Fully Accessible UI Components"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [accessibility, aria, wcag, react]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build these UI components with perfect accessibility (WCAG 2.1 AA):

1. **Modal/Dialog**: focus trap, ESC to close, aria-modal, return focus on close
2. **Dropdown Menu**: arrow key navigation, type-ahead search
3. **Combobox/Autocomplete**: ARIA 1.2 combobox pattern
4. **Toast notifications**: aria-live region, auto-dismiss with warning
5. **Tabs**: roving tabindex pattern
6. **Accordion**: ARIA expanded state, keyboard support
7. **Date Picker**: calendar grid with keyboard navigation
8. **Data Table**: sortable columns with aria-sort

For each:
- Screen reader announcements
- Keyboard interaction pattern
- Focus management
- ARIA roles, states, properties
- Testing with axe-core
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
