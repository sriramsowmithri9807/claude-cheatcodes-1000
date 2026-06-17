---
title: "Scaffold a UI Component Library"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, storybook, design-system, components]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
You are a design systems engineer. Scaffold a minimal but production-ready React component library with:
- Button (variants: primary, secondary, ghost, danger; sizes: sm, md, lg)
- Input (text, password, email with validation states)
- Modal (with backdrop, close button, keyboard ESC support)
- Card (with header, body, footer slots)
- Badge / Chip component

Each component must have:
- TypeScript props interface
- CSS Module styles
- Storybook story (CSF3 format)
- Jest + React Testing Library unit test

Also create: `package.json`, `tsconfig.json`, `.storybook/main.ts`, and `index.ts` barrel export.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
