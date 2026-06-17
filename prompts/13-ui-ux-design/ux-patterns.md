---
title: "Apply Common UX Patterns"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ux-patterns, design, interaction, ui]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Apply the right UX patterns to my application.

App: [DESCRIBE YOUR FEATURES AND SCREENS]

**Navigation patterns**:
1. Hub and spoke: central home → features → back
2. Flat navigation: bottom tabs for main areas
3. Pyramid: hierarchical drill-down

**Form patterns**:
4. Progressive disclosure: show fields as needed
5. One thing per page: reduce cognitive load
6. Inline editing: edit in place without separate form

**Data display patterns**:
7. Card layout: scannable content pieces
8. Master-detail: list + detail panel (email app)
9. Timeline: chronological events

**Action patterns**:
10. Confirmation: destructive actions need confirm
11. Undo: allow undoing recent actions
12. Optimistic update: show change before server confirms

For each screen in my app: which pattern to apply and why.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
