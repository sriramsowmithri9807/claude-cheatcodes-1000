---
title: "Implement Idempotent APIs"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [idempotency, api, payments, backend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement idempotent API endpoints (critical for payments and financial operations).

Why: if a client retries a request (network timeout), the operation must not execute twice.

Implement:
1. `Idempotency-Key` header (UUID, client-provided)
2. Store keys in Redis with 24h TTL
3. On first request: process and cache response
4. On duplicate request (same key): return cached response immediately
5. In-flight protection: lock key while processing (prevent concurrent duplicates)
6. Database: store idempotency key with request fingerprint + response
7. Test: simulate retry scenarios

Apply to: POST /payments, POST /orders, POST /subscriptions
Show the complete middleware implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
