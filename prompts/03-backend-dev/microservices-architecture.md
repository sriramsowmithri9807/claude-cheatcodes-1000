---
title: "Design a Microservices Architecture"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [microservices, docker, kubernetes, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a microservices architecture for: [MONOLITH TO DECOMPOSE / NEW SYSTEM].

Services to create:
- [Service 1]: responsibility
- [Service 2]: responsibility
- [Service 3]: responsibility

For each service:
1. Technology choice and justification
2. API contract (REST or gRPC proto definition)
3. Data store (each service owns its data)
4. Docker container setup
5. Health check endpoint

Cross-cutting concerns:
- API Gateway (Kong or Nginx)
- Service discovery
- Distributed tracing (OpenTelemetry)
- Centralized logging (ELK stack)
- Circuit breaker (Resilience4j or polly)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
