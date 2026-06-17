---
title: "Convert Figma-Style Design Spec to Code"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [figma, design-to-code, react, css]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
You are an expert at converting design specifications to pixel-perfect code. Here is the design spec:

[PASTE FIGMA SPECS / DESIGN TOKENS / DESIGN DESCRIPTION]

Convert to:
- React + TypeScript functional components
- CSS Modules with exact spacing, colors, and typography from the spec
- Responsive breakpoints: mobile (< 768px), tablet (768–1024px), desktop (> 1024px)
- Smooth transitions for interactive states (hover, focus, active, disabled)
- Accessibility: proper ARIA roles, focus indicators, keyboard navigation
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
