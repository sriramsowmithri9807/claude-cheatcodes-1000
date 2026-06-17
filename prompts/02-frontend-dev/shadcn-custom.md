---
title: "Customize and Extend shadcn/ui"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [shadcn, radix, react, design-system]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Extend shadcn/ui with custom components and theme customization.

My app's design: [DESCRIBE BRAND: colors, roundness, feel]

Implement:
1. Custom CSS variables for your brand in `globals.css`
2. Custom `tailwind.config.ts` theme extension
3. New component variants for existing shadcn components
4. 3 completely new components built in the shadcn pattern:
   - [Component 1]
   - [Component 2]
   - [Component 3]
5. Custom command palette (extend shadcn Command)
6. Data table (extend shadcn Table + TanStack Table)
7. Charts (extend shadcn Chart + Recharts)

Output: drop-in components ready for your `components/ui/` folder.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
