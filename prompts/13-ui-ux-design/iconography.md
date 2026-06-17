---
title: "Create an Iconography System"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [icons, design, svg, system]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create a consistent iconography system for my product.

Brand personality: [DESCRIBE: minimal/geometric, rounded/friendly, sharp/technical]

1. **Icon library selection** (or custom):
   - Heroicons: clean, MIT license
   - Phosphor Icons: 6 weights, very flexible
   - Lucide: community fork of Feather
   - Custom SVG for brand-critical icons

2. **Sizing**: standard sizes: 16, 20, 24, 32px
3. **Stroke weight**: consistent 1.5 or 2px across all icons
4. **Corner radius**: square or rounded corners (match your UI roundness)
5. **Color**: inherit from text color (`currentColor`)
6. **Variants**: outlined (default), filled (active state), duotone (decorative)
7. **React component**: `<Icon name="arrow-right" size={20} />`
8. **Sprite sheet**: optimize for performance (SVG sprite)
9. **Accessibility**: title + aria-hidden for decorative icons
10. **Dark mode**: icons that work on both backgrounds

Output: icon component + usage guidelines.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
