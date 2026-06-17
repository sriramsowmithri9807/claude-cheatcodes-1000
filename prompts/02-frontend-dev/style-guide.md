---
title: "Create a Living Style Guide"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [style-guide, components, documentation, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create a living style guide (in-app) for my component library.

Build a `/style-guide` route with sections:
1. **Colors**: all design tokens with hex values and usage guidance
2. **Typography**: all type scales, weights, with live examples
3. **Spacing**: visual spacing scale
4. **Icons**: all available icons with copy-name-to-clipboard
5. **Components**: interactive demos of every component
   - Button (all variants + sizes + states)
   - Form elements
   - Cards, modals, tooltips, etc.
6. **Do/Don't**: design rules with visual examples

Self-contained page that works without any routing library.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
