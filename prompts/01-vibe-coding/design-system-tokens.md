---
title: "Create a Complete Design Token System"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [design-tokens, css, design-system, theming]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create a production-grade design token system for a [TYPE OF APP: SaaS/e-commerce/dashboard/marketing].

Include all categories:
- **Colors**: brand, neutral, semantic (success/warning/error/info), dark mode variants
- **Typography**: font families, sizes (scale), weights, line heights, letter spacing
- **Spacing**: 4px base grid, scale from 0 to 96
- **Border radius**: sm/md/lg/full
- **Shadows**: 5 levels
- **Breakpoints**: xs/sm/md/lg/xl/2xl
- **Z-index**: named layers (modal, tooltip, dropdown, sticky)
- **Animation**: duration, easing curves

Output as: CSS custom properties, JavaScript ES module, and Figma-ready JSON (Style Dictionary format).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
