---
title: "Create a Typography System"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [typography, design, css, fonts]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create a comprehensive typography system for my web application.

Brand feeling: [DESCRIBE: modern, classic, playful, serious, technical]

1. **Font pairing**:
   - Heading font: [suggestions based on brand]
   - Body font: [readable, comfortable for long text]
   - Mono font: [for code, data]
2. **Type scale**: 8 sizes from xs to 5xl (following modular scale ratio)
3. **Font weights**: which weights you actually use (reduce to 2-3)
4. **Line height**: heading (1.2), body (1.5), UI labels (1.0)
5. **Letter spacing**: heading (-0.02em), body (0), uppercase (0.08em)
6. **Measure**: optimal line length (60-75 characters)
7. **Responsive**: slightly smaller on mobile
8. **Loading**: self-host or `next/font`, no FOUT
9. **Dark mode**: same fonts, slightly lighter weight
10. **Accessibility**: minimum 16px body, high contrast text

Output: CSS custom properties + utility classes.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
