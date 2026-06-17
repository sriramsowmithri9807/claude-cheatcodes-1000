---
title: "Create and Manage Design Tokens"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [design-tokens, css, theming, style-dictionary]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Create a comprehensive design token system.

Brand: [DESCRIBE]
Platforms: Web (CSS) + iOS (Swift) + Android (XML) [choose which apply]

**Token hierarchy**:
1. **Primitive tokens**: raw values (colors, sizes)
   - `color-blue-500: #3b82f6`
2. **Semantic tokens**: meaning (reference primitives)
   - `color-action-primary: {color-blue-500}`
3. **Component tokens**: specific usage
   - `button-background-primary: {color-action-primary}`

**Token categories**:
4. Colors (full palette + semantic)
5. Typography (family, size, weight, line-height)
6. Spacing (4px grid)
7. Border (width, radius)
8. Shadow (elevation)
9. Animation (duration, easing)
10. Z-index (layers)

Using Style Dictionary:
11. Token JSON files
12. Transform to CSS, Swift, Android XML
13. CI: regenerate on token change

Output: complete token set + Style Dictionary config.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
