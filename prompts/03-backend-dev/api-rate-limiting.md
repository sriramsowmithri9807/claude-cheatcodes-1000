---
title: "Advanced API Rate Limiting"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rate-limiting, redis, api, security]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement sophisticated API rate limiting for a production API.

Requirements:
- Free tier: 100 req/hour
- Pro tier: 10,000 req/hour
- Enterprise: 1,000,000 req/hour

Implement:
1. Token bucket algorithm (smooth bursting)
2. Sliding window log (most accurate)
3. Redis-based distributed limiting (works across multiple API servers)
4. Per-endpoint limits (stricter for expensive operations)
5. Cost-based limiting (read=1 point, write=5 points, AI=100 points)
6. Response headers: X-RateLimit-Limit, Remaining, Reset, Retry-After
7. Graceful limit exceeded: 429 with retry timing
8. Admin API to adjust limits per user
9. Bypass for internal service calls
10. Dashboard showing rate limit usage per API key
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
