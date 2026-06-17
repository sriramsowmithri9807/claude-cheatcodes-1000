---
title: "Implement Perfect Dark Mode"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [dark-mode, theming, css, react]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement a perfect dark mode system for my [React/Next.js/Vue] app.

Requirements:
- Respect OS preference on first visit
- User override with persistent preference (localStorage)
- No flash of unstyled content (FOUC) on page load
- Smooth transition between modes (CSS transition)
- CSS custom properties for all color tokens
- `useTheme()` React hook
- Theme toggle component with animation
- System → Light → Dark cycling

Bonus:
- Per-component theme override
- High contrast mode support
- Auto switch at sunrise/sunset (geolocation)

Include the Next.js specific FOUC prevention script.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
