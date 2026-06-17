---
title: "Prepare Design Handoff for Developers"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [design-handoff, figma, specifications, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Prepare a comprehensive design handoff for developers.

Feature designed: [DESCRIBE]
Design tool: Figma
Developers receiving: [DESCRIBE THEIR EXPERIENCE LEVEL]

**What developers need from handoff**:
1. **Specs**: exact measurements (px/rem), colors (hex/CSS var), fonts
2. **Component states**: default, hover, active, disabled, loading, error
3. **Responsive behavior**: how it adapts at each breakpoint
4. **Animations**: duration, easing, what triggers them
5. **Interactions**: what happens on each user action
6. **Edge cases**: long text, empty state, error state
7. **Assets**: exported SVGs, images at correct sizes
8. **Design tokens**: which token variables to use

**Figma handoff checklist**:
9. Auto layout on all components (no absolute positioning)
10. Consistent naming (developers use these names in code)
11. Annotated with units and behavior notes
12. Dev mode enabled for automatic CSS output

Output: handoff specification document + Figma annotation guide.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
