---
title: "Optimize Web Application Performance"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [web-performance, lighthouse, optimization, frontend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my web application's performance to achieve Core Web Vitals targets.

App: [DESCRIBE YOUR APP AND CURRENT SCORES]
Targets: LCP < 2.5s, FID < 100ms, CLS < 0.1, INP < 200ms

**LCP optimization** (Largest Contentful Paint):
1. Preload LCP image: `<link rel='preload' as='image'>`
2. Server-push or preconnect to image server
3. Optimize image: WebP, correct size, lazy load below-fold
4. Eliminate render-blocking resources
5. Server response time < 200ms (TTFB)

**INP optimization** (Interaction to Next Paint):
6. Move heavy work off main thread (Web Workers)
7. Break up long tasks (> 50ms) with `setTimeout(fn, 0)`
8. Use `startTransition` for non-urgent state updates (React)

**CLS optimization** (Cumulative Layout Shift):
9. Always define width/height on images and videos
10. Font loading: `font-display: swap` or subset fonts
11. Reserve space for ads and embeds

Output: Lighthouse audit + specific fixes.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
