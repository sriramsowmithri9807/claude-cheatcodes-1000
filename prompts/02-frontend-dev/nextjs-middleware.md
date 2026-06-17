---
title: "Master Next.js Middleware"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [nextjs, middleware, auth, edge]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement powerful Next.js Middleware for [MY APP].

Use cases:
1. **Auth protection**: redirect unauthenticated users
2. **A/B testing**: randomly assign variant, persist in cookie
3. **Feature flags**: check flags and redirect or modify response
4. **Geo-blocking**: redirect based on country
5. **Rate limiting**: basic IP-based rate limit at the edge
6. **Localization**: detect language, redirect to locale subdirectory
7. **Bot detection**: block known scrapers
8. **Security headers**: CSP, HSTS, X-Frame-Options

Includes: `middleware.ts` + `matcher` config, performance tips (< 1ms execution budget).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
