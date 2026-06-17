---
title: "Implement the Backend-for-Frontend Pattern"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [bff, api-gateway, architecture, fullstack]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement the Backend-for-Frontend (BFF) pattern.

My frontends:
- Web app (Next.js)
- Mobile app (React Native)
- Third-party API consumers

Problem: Each frontend needs different data shapes and auth methods.

Design BFF for each:
1. **Web BFF**: session-based auth, server-side rendering optimized responses
2. **Mobile BFF**: JWT auth, mobile-optimized payloads (smaller, compressed)
3. **Public API**: API key auth, rate-limited, versioned

Each BFF:
- Aggregates calls to microservices
- Transforms responses
- Handles auth for its client type
- Caches aggressively for its usage pattern
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
