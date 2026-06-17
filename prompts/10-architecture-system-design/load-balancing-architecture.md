---
title: "Design Load Balancing Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [load-balancing, architecture, nginx, aws]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive load balancing architecture.

Application: [DESCRIBE]
Scale: [EXPECTED PEAK RPS]

Layers:
1. **DNS level**: Route 53 weighted routing / GeoDNS
2. **Global CDN**: CloudFront / Cloudflare (static assets + API caching)
3. **Layer 4 (TCP)**: AWS NLB for raw TCP throughput
4. **Layer 7 (HTTP)**: AWS ALB or Nginx (path routing, SSL termination)
5. **Application cluster**: stateless app servers (scale horizontally)
6. **Service mesh**: Istio for service-to-service load balancing
7. **Database**: PgBouncer + read replica routing
8. **Cache**: Redis Cluster for distributed caching

Health check strategy at each layer.
Failover behavior at each layer.
Draw the full request path.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
