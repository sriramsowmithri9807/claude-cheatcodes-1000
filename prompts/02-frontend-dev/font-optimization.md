---
title: "Optimize Web Fonts for Performance"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [fonts, performance, css, web-vitals]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Optimize web fonts for performance and aesthetics in my project.

Current fonts: [LIST YOUR FONTS]

Implement:
1. Self-hosting fonts (woff2 format, subset to used characters)
2. `@font-face` with `font-display: swap` and correct descriptors
3. Preloading critical fonts in `<head>`
4. Variable fonts: one file for all weights
5. System font fallback stack that minimizes layout shift
6. `size-adjust` to match system font metrics to web font
7. Next.js `next/font` for zero-CLS font loading
8. Subsetting: only include characters you use (pyftsubset)

Target: < 30KB total font payload, CLS = 0.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
