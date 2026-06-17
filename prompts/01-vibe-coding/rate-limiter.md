---
title: "Implement Rate Limiting for Your API"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rate-limiting, redis, api, security]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement production-grade rate limiting for my Express.js API.

Requirements:
- Sliding window algorithm (fairer than fixed window)
- Per-user rate limits (authenticated) and per-IP (anonymous)
- Different limits per route: strict for auth, generous for reads
- Redis backend for distributed rate limiting
- Graceful response with `Retry-After` header
- Rate limit headers in every response (X-RateLimit-Limit, Remaining, Reset)
- Admin bypass capability
- Rate limit exceeded webhook/alert

Include unit tests for the rate limiter logic.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
