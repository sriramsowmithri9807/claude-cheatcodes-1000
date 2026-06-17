---
title: "Master Responsive Design"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [responsive, css, mobile-first, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement perfect responsive design for my application.

App type: [DESCRIBE: dashboard, marketing site, e-commerce, etc.]
Breakpoints: mobile (< 640px), tablet (640-1024px), desktop (> 1024px)

1. **Mobile-first**: start with mobile styles, add complexity for larger screens
2. **Fluid typography**: `clamp(min, preferred, max)` for responsive font sizes
3. **Fluid spacing**: `clamp()` for padding and margins too
4. **Container queries**: component-level responsive instead of viewport
5. **Flexible images**: `width: 100%; max-width: X` and `object-fit`
6. **Grid system**: CSS Grid with `auto-fill + minmax`
7. **Navigation**: hamburger menu on mobile, full nav on desktop
8. **Tables**: horizontal scroll on mobile, or transform to card layout
9. **Touch targets**: 44px minimum on mobile
10. **Viewport units**: use `svh` (small viewport height) on mobile

For each component in my app: mobile + desktop design decisions.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
