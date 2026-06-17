---
title: "Modernize Legacy CSS to CSS Variables"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [css, refactor, design-tokens]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
You are a CSS architecture expert. Refactor this legacy CSS/SASS:

[PASTE YOUR CSS HERE]

Convert it to modern CSS with:
- CSS custom properties (variables) for all colors, spacing, typography
- A `:root` block with a complete design token system
- Logical properties where appropriate (margin-inline, padding-block)
- CSS nesting (native, no preprocessor)
- Remove any vendor prefixes that are no longer needed (2024+)
- Add CSS layers (@layer) for specificity management

Output the refactored CSS and a brief explanation of each major change.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
