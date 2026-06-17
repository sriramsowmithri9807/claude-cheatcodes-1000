---
title: "Design a Beautiful Dark Mode"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [dark-mode, design, css, theming]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design a beautiful, professional dark mode for my application.

Current light mode colors: [PASTE YOUR COLOR PALETTE]

Dark mode design principles:
1. **Not just color inversion**: dark mode is a different design
2. **Elevation model**: dark surfaces get lighter, not darker (Material Design)
3. **Reduced saturation**: colors look different on dark backgrounds, adjust saturation
4. **True black avoidance**: #121212 or #1a1a1a, not #000000 (except OLED)
5. **Text contrast**: avoid pure white (#ffffff) → use #e8e8e8
6. **Shadows**: don't show well on dark → use glow effects instead
7. **Images**: darken bright images slightly, lighten dark ones
8. **Icons**: use outlined in dark, filled in light
9. **Transitions**: smooth 200ms transition between modes
10. **System preference**: respect prefers-color-scheme

Output: complete CSS variable system for both modes.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
