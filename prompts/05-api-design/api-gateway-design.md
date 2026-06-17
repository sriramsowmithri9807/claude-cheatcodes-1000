---
title: "Design an API Gateway"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api-gateway, kong, nginx, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design an API gateway for my microservices architecture.

Services: [LIST YOUR SERVICES]
Clients: [Web app, Mobile app, Third-party]

Gateway responsibilities:
1. **Routing**: path-based and header-based routing rules
2. **Auth**: JWT validation, API key management
3. **Rate limiting**: per client, per service, per endpoint
4. **Load balancing**: round-robin, weighted, least-connections
5. **Circuit breaker**: fail fast when upstream is unhealthy
6. **Caching**: cache GET responses at edge
7. **Transformation**: request/response manipulation
8. **Observability**: request tracing, access logs, metrics
9. **TLS termination**: HTTPS → HTTP to services
10. **DDoS protection**: IP blocking, challenge-based

Tool: Kong (open source) or Nginx + Lua, with config files.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
