---
title: "CSS Animation Masterclass"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [css, animations, keyframes, ux]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create a complete animation system using pure CSS (no JavaScript).

Implement:
1. **Entrance animations**: fadeIn, slideUp, slideLeft, scaleIn, bounceIn
2. **Attention seekers**: shake, pulse, swing, tada
3. **Exits**: fadeOut, slideDown, scaleOut
4. **Continuous**: spin, ping, blink, wave
5. **Scroll-triggered**: using `@keyframes` + Intersection Observer via CSS only (animation-play-state)
6. **Stagger pattern**: `nth-child` animation delays for lists
7. **Reduced motion**: `@media (prefers-reduced-motion: reduce)` fallbacks

Each animation as a reusable CSS class.
Timing functions: use `cubic-bezier()` for natural motion, not just ease-in-out.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
