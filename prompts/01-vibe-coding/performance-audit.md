---
title: "Audit and Fix App Performance"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [performance, optimization, lighthouse, web-vitals]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
You are a web performance expert. Here is my app's performance data:

[PASTE: Lighthouse report, Web Vitals, bundle size report, or description of slowness]

Provide:
1. **Diagnosis**: Root cause of each performance issue
2. **Quick wins** (fixes taking < 1 hour each)
3. **Code changes** with before/after examples for the top 3 issues
4. **Bundle optimization**: code splitting, lazy loading, tree shaking
5. **Image optimization** strategy
6. **Caching strategy** (HTTP headers, service worker, CDN)
7. **Target metrics**: LCP < 2.5s, FID < 100ms, CLS < 0.1
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
