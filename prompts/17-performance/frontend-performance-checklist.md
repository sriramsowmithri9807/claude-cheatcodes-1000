---
title: "Frontend Performance Checklist"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [performance, frontend, checklist, web]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Apply the complete frontend performance checklist to my web app.

App URL or description: [DESCRIBE YOUR APP]

**Loading performance**:
□ LCP < 2.5 seconds
□ TTFB < 200ms (server response)
□ FCP < 1.8 seconds (first content visible)
□ Total blocking time < 200ms
□ JavaScript bundle < 100KB gzipped (main)
□ CSS < 30KB gzipped
□ No render-blocking scripts in <head>
□ Images in WebP/AVIF format
□ Images have width + height attributes
□ LCP image preloaded
□ Fonts use `font-display: swap`
□ Fonts subsetted to characters used
□ Third-party scripts loaded async/defer
□ HTTP/2 enabled
□ Gzip/Brotli compression enabled
□ CDN for static assets

**Runtime performance**:
□ No layout thrashing (batch reads before writes)
□ List virtualization for 100+ item lists
□ `will-change` only for actual animations
□ CSS animations use transform/opacity only
□ Event listeners removed when not needed

For each failing item: how to fix it.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
