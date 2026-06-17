---
title: "Apply Color Theory to UI Design"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [color, design, ui, accessibility]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Apply color theory to create a beautiful, accessible color system for my UI.

Context: [DESCRIBE YOUR PRODUCT TYPE AND BRAND FEELING]
Existing brand colors (if any): [HEX CODES]

1. **Color models**: HSL for perceptually uniform adjustments
2. **Color harmony**: complementary, analogous, triadic — which suits my brand
3. **Primary color**: your main brand color → generate 10-shade scale
4. **Secondary color**: complementary for accents
5. **Neutral scale**: warm gray vs cool gray vs pure gray
6. **Semantic colors**: success (green), warning (amber), error (red), info (blue)
7. **Dark mode**: not just inversion — luminance and saturation adjustments
8. **WCAG contrast**: all text meets 4.5:1 AA, large text 3:1
9. **Color blindness**: test with Deuteranopia and Protanopia simulators
10. **CSS output**: complete custom property color system

Output: complete color system as CSS variables.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
