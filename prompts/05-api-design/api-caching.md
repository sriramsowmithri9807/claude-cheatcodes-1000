---
title: "Design API Caching Strategy"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [caching, api, http, etag]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive caching strategy for my API.

Endpoints: [LIST YOUR ENDPOINTS AND HOW OFTEN DATA CHANGES]

HTTP caching:
1. `Cache-Control` headers for each endpoint type
2. `ETag` implementation (conditional GET, 304 responses)
3. `Last-Modified` header
4. `Vary` header for content negotiation
5. CDN caching: which endpoints to cache at edge
6. Cache invalidation on data change

Server-side caching:
7. Redis cache for expensive queries
8. Cache warming strategy
9. Cache aside vs write-through vs write-behind

Client-side:
10. React Query cache coordination with HTTP cache

Output: cache policy per endpoint type + implementation code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
