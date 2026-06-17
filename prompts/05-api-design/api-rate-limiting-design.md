---
title: "Design API Rate Limiting"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rate-limiting, api, design, backend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive rate limiting strategy for my public API.

My API plans:
- Free: 1,000 req/day
- Pro: 100,000 req/day  
- Enterprise: unlimited (with fair-use)

Design:
1. Algorithm: token bucket vs leaky bucket vs sliding window — which and why
2. Granularity: global vs per-endpoint vs per-resource
3. Cost model: assign cost to expensive operations (search=10x, AI=100x)
4. Burst allowance: short bursts above limit without penalty
5. Response headers: standard headers consumers should read
6. 429 response body: clear message with retry timing
7. Abuse prevention: detect and block abusive patterns
8. Override: enterprise customers with custom limits

Output: rate limiting spec + Redis implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
