---
title: "Implement Resilience Patterns"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [resilience, circuit-breaker, retry, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement resilience patterns to make my services fault-tolerant.

Services that can fail: [LIST EXTERNAL DEPENDENCIES]

1. **Circuit Breaker**: open circuit when error rate > 50% for 60s
   - States: Closed → Open → Half-Open
   - Node.js: opossum library
2. **Retry with backoff**: retry transient failures
   - Exponential backoff: 1s, 2s, 4s, 8s
   - Jitter: add random ±20% to prevent thundering herd
   - Don't retry: 4xx responses (except 429)
3. **Bulkhead**: isolate failures (separate thread pools / queues)
4. **Timeout**: fail fast, don't wait indefinitely
5. **Fallback**: return cached data when primary fails
6. **Health check**: monitor dependency health
7. **Chaos engineering**: randomly fail dependencies in staging

Implement all patterns in Node.js with Axios and opossum.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
