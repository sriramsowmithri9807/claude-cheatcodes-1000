---
title: "Design Idempotent API Operations"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [idempotency, api, reliability, payments]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design idempotent API operations for my payment-critical system.

Critical operations: [LIST YOUR OPERATIONS]

Implement:
1. `Idempotency-Key` header specification (UUID format, required for mutations)
2. Key storage: Redis with TTL (24h) + database for permanent record
3. Response caching: first successful response cached and returned on retry
4. In-flight protection: Redis lock during processing
5. Key fingerprinting: cache key = idempotency-key + request body hash
6. What to do if same key but different body (reject with 422)
7. Conditional requests: ETag + If-Match for read-modify-write
8. Testing: how to simulate retry scenarios
9. Client retry logic: when to retry and when not to
10. Documentation: how to communicate this to API consumers
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
