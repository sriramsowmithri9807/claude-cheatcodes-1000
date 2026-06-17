---
title: "Master Next.js Image Optimization"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [nextjs, images, performance, web-vitals]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Optimize all images in my Next.js app for maximum performance.

Current situation: [DESCRIBE YOUR IMAGE USAGE]

Implement:
1. `next/image` for all images with correct `sizes` prop
2. Blur placeholder generation during build
3. Art direction: different crops for mobile vs desktop
4. Lazy loading with custom placeholder
5. Priority loading for above-the-fold images
6. CDN configuration for remote images
7. SVG handling (don't put SVGs through Image component)
8. Background images with CSS (when `next/image` doesn't fit)

Target: Largest Contentful Paint < 2.5s, zero layout shift from images.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
