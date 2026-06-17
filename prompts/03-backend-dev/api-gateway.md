---
title: "Build an API Gateway"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api-gateway, nginx, nodejs, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an API Gateway for my microservices.

Services behind the gateway: [LIST SERVICES AND THEIR PORTS]

Using: Express.js gateway (or recommend nginx/Kong if more appropriate)

Implement:
1. Route proxying to upstream services
2. JWT authentication (verify at gateway, forward user info)
3. Rate limiting per user/IP
4. Request/response transformation
5. Aggregation endpoint (combine multiple service calls)
6. Circuit breaker for each upstream
7. Request timeout handling
8. Access logging (structured JSON)
9. Health aggregation endpoint
10. Graceful degradation (serve cached response when upstream is down)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
