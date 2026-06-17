---
title: "CI/CD Best Practices for Production"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ci-cd, devops, best-practices, pipelines]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement CI/CD best practices for my team's deployment pipeline.

Current setup: [DESCRIBE YOUR CURRENT CI/CD SITUATION]

Best practices to implement:
1. **Fail fast**: run fastest checks first (lint before tests)
2. **Parallelism**: run independent jobs in parallel
3. **Caching**: dependency cache, Docker layer cache
4. **Artifact storage**: pass build artifacts between jobs
5. **Environment parity**: staging = production config
6. **Rollback**: one-click rollback to previous version
7. **Feature flags**: deploy code without enabling feature
8. **Canary deployment**: route 1% traffic to new version first
9. **Smoke tests**: post-deploy verification
10. **Secrets rotation**: no long-lived secrets
11. **Dependency updates**: Dependabot or Renovate bot
12. **DORA metrics**: track deployment frequency, lead time, MTTR, change failure rate
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
