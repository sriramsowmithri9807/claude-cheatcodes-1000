---
title: "Build a Design Tokens Pipeline"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [design-tokens, style-dictionary, theming, build]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a design tokens pipeline from Figma to code.

Using: Style Dictionary

Source tokens (JSON format):
- Colors, typography, spacing, shadows, border radius, breakpoints

Output targets:
1. CSS custom properties file
2. JavaScript/TypeScript ES module
3. SCSS variables
4. iOS Swift color extensions
5. Android XML resources
6. Figma plugin JSON format

Build pipeline:
- Token transformation (snake_case → camelCase, px → rem)
- Theme support (light/dark/brand themes)
- Documentation auto-generation
- CI integration: fail if tokens are invalid

Include: the Style Dictionary config and npm build script.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
