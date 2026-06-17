---
title: "Generate a Complete Color Palette from One Color"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [design, colors, css, ui]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
I have a brand color: [HEX COLOR].

Generate a complete design system color palette:
1. Primary scale (50–950, 10 shades)
2. Neutral/gray scale (50–950)
3. Semantic colors: success, warning, error, info (each with light/default/dark)
4. Dark mode equivalents for each semantic color

Output as:
- CSS custom properties
- JavaScript/TypeScript object
- Tailwind CSS config extension

Also provide WCAG contrast ratios for text-on-background combinations and flag any accessibility issues.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
