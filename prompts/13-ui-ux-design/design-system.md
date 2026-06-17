---
title: "Build a Complete Design System"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [design-system, components, css, tokens]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a complete design system for my product.

Brand: [DESCRIBE YOUR BRAND PERSONALITY AND VALUES]
Product type: [SaaS / consumer app / e-commerce / etc.]

Design system layers:

**1. Foundation**:
- Color palette: brand, neutral, semantic, dark mode
- Typography: scale, weights, line heights, families
- Spacing: 4px grid, scale from 0 to 96
- Shadows: 5 elevation levels
- Border radius: sm/md/lg/full
- Icons: chose icon library or custom icons

**2. Components**:
- Atoms: Button, Input, Checkbox, Badge, Avatar
- Molecules: Form Field, Card, Dropdown, Toast
- Organisms: Navigation, Data Table, Modal, Sidebar

**3. Patterns**:
- Form patterns, data display, empty states, errors

**4. Documentation**: living style guide

Output: CSS variables + React components + Storybook stories.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
