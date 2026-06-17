---
title: "Optimize JavaScript Bundle Size"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [bundle, webpack, vite, performance]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my JavaScript bundle size.

Current bundle size: [DESCRIBE]
Build tool: [Webpack / Vite / Next.js]

Analysis:
1. **Bundle analyzer**: `webpack-bundle-analyzer` or `rollup-plugin-visualizer`
2. Identify: large libraries, duplicates, unused code

Optimizations:
3. **Code splitting**: dynamic `import()` for route-level splitting
4. **Tree shaking**: ensure proper ES modules (not CommonJS)
5. **Replace large libraries**:
   - moment.js → date-fns (tree-shakeable)
   - lodash → lodash-es or just use native JS
6. **Lazy load**: non-critical components with React.lazy()
7. **Image optimization**: WebP, AVIF, responsive srcset
8. **Font subsetting**: only include characters you use
9. **Third-party scripts**: load async, defer non-critical
10. **Source maps**: production source maps sent to Sentry, not end user

Target: < 100KB main bundle (gzipped), < 200KB per route chunk.
Output: specific changes for my bundle.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
