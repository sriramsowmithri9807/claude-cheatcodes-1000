---
title: "Master Responsive Images"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [images, responsive, performance, html]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement responsive images correctly for [MY WEBSITE/APP].

Use cases: [LIST: hero images / product photos / avatars / blog thumbnails]

Implement:
1. `srcset` + `sizes` for resolution switching
2. `<picture>` element for art direction (different crops at different sizes)
3. WebP + AVIF with JPEG fallback using `<source type>`
4. Lazy loading with `loading="lazy"` + blurred placeholder
5. `fetchpriority="high"` for LCP image
6. Aspect ratio boxes to prevent layout shift
7. Next.js Image component equivalent for pure HTML
8. CSS background images: use `image-set()` for responsive backgrounds

Show: the generated HTML for each scenario.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
