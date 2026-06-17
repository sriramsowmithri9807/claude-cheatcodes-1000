---
title: "Configure Load Balancing"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [load-balancing, nginx, haproxy, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up load balancing for my application.

Architecture: [N app servers, what protocol, session requirements]

Options to evaluate:

**Nginx upstream**:
- round_robin (default)
- least_conn
- ip_hash (sticky sessions)
- weight distribution

**HAProxy** (more features):
- ACL-based routing
- Health checks (active and passive)
- SSL termination
- Connection rate limiting
- Stats page

**AWS ALB**:
- Target groups + rules
- Path-based routing
- Weighted routing (canary)
- Sticky sessions

For MY setup: which to use and why.
Output: complete config + health check setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
