---
title: "Build a Micro-Animation System"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [animations, css, framer-motion, ux]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a reusable micro-animation system for my React app.

Create:
1. **CSS animation primitives** in a global stylesheet:
   - fadeIn, slideIn (4 directions), scaleIn, bounceIn
   - Exit animations: fadeOut, slideOut, scaleOut
2. **React components**: `<AnimateIn>`, `<AnimateOut>`, `<AnimatePresence>`
3. **Framer Motion variants** for complex sequences
4. **Page transitions** between routes
5. **Stagger animations** for lists (items animate in one by one)
6. **Skeleton loading** animations
7. **Reduced motion** support (prefers-reduced-motion media query)

Performance: CSS transforms only (no layout-triggering properties). 60fps target.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
