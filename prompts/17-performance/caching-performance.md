---
title: "Implement Aggressive Caching for Performance"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [caching, cdn, performance, http]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement aggressive caching to improve performance.

Assets to cache: [DESCRIBE YOUR ASSETS AND API RESPONSES]

HTTP caching strategy:
1. **Immutable assets** (hashed filenames): `Cache-Control: public, max-age=31536000, immutable`
2. **Static HTML**: `Cache-Control: no-cache` (revalidate always)
3. **API responses** (public): `Cache-Control: public, max-age=60, s-maxage=300`
4. **User-specific API**: `Cache-Control: private, max-age=30`
5. **ETags**: conditional GET (304 Not Modified)

Service Worker caching:
6. Cache-first for static assets
7. Network-first for API calls
8. Stale-while-revalidate for non-critical
9. Offline fallback page

CDN strategy:
10. Push static assets to CDN on deploy
11. CDN API cache with purge on data change
12. Edge functions for dynamic caching logic

Redis caching:
13. Cache expensive DB queries
14. Cache third-party API responses

Output: caching strategy implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
