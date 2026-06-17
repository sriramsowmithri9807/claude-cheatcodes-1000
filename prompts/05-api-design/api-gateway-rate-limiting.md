---
title: "Implement Advanced API Gateway Rate Limiting"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api-gateway, rate-limiting, kong, nginx]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement sophisticated rate limiting at the API gateway level.

Gateway: [Kong / Nginx / Cloudflare Workers]

Rate limiting tiers:
- Anonymous: 100 req/min per IP
- Free account: 1,000 req/hour
- Pro account: 50,000 req/hour
- Enterprise: custom

Advanced features:
1. Cost-based limiting (not just request count)
2. Endpoint-specific limits (POST /ai-generate = 10x cost)
3. Global vs per-region limits
4. DDoS protection: detect and block attack patterns
5. Whitelisting: internal services bypass limits
6. Rate limit sharing across microservices
7. Graceful degradation: partial service when near limit

Redis cluster configuration for distributed state.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
