---
title: "Optimize Your JavaScript Bundle"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [performance, webpack, vite, bundle-size]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Analyze and optimize my JavaScript bundle.

Current setup: [VITE/WEBPACK/NEXT.JS] with these dependencies: [LIST HEAVY DEPS]

Optimization strategies:
1. **Code splitting**: route-level, component-level lazy loading
2. **Tree shaking**: identify and fix failed tree shaking
3. **Dynamic imports**: heavy libraries (charts, PDFs, maps) loaded on demand
4. **Bundle analyzer**: setup and interpret `rollup-plugin-visualizer` output
5. **Compression**: gzip vs Brotli, when each applies
6. **Module deduplication**: fix multiple React versions
7. **Replace heavy packages**: suggest lighter alternatives
8. **CSS splitting**: per-route CSS bundles

Target: main bundle < 100KB gzipped.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
