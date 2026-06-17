---
title: "Design Zero-Downtime Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [zero-downtime, high-availability, deployment, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design an architecture for zero-downtime deployments and operations.

Current situation: [DESCRIBE CURRENT DEPLOY PROCESS AND DOWNTIME]

Components:
1. **Load balancer health checks**: remove unhealthy instances immediately
2. **Rolling deployment**: update N instances at a time
3. **Blue/green deployment**: full parallel environment switch
4. **Canary deployment**: route 1% → 10% → 100% gradually
5. **Database migrations**: backward-compatible schema changes only
6. **Feature flags**: deploy code before enabling it
7. **Connection draining**: finish in-flight requests before shutdown
8. **Graceful shutdown**: SIGTERM → drain → exit
9. **Readiness probe**: don't send traffic until app is ready
10. **Rollback**: immediate automated rollback on error rate spike

Make every production deployment invisible to users.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
