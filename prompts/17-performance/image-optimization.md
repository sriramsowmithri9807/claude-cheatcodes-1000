---
title: "Optimize Images for Web"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [images, webp, performance, cdn]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Optimize all images in my web application.

Current state: [DESCRIBE: image formats, sizes, how they're served]

1. **Format selection**:
   - Photos: WebP (30-35% smaller than JPEG) or AVIF (50% smaller)
   - Graphics: SVG (infinitely scalable) or WebP-lossless
   - Animations: WebP animation or AVIF animation (not GIF)
2. **Responsive images**: `srcset` + `sizes` for different viewports
3. **Lazy loading**: `loading='lazy'` for below-fold images
4. **Dimensions**: always specify width + height to prevent CLS
5. **Priority loading**: `fetchpriority='high'` for LCP image
6. **Compression**: 85% quality for WebP (imperceptible quality loss)
7. **CDN delivery**: Cloudflare Images, Cloudinary, or imgproxy
8. **Preload**: `<link rel='preload'>` for critical above-fold images
9. **Sprite sheets**: for many small icons
10. **Blur-up placeholder**: low-res placeholder → full image

Next.js: use `<Image>` component (handles all of the above automatically).
Output: specific optimizations for my images.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
