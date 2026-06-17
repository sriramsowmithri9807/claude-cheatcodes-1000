---
title: "Implement Blue-Green Deployment"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [blue-green, deployment, zero-downtime, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement blue-green deployment for zero-downtime releases.

Current setup: [DESCRIBE YOUR DEPLOYMENT INFRASTRUCTURE]

Blue-green strategy:
1. Blue: current production version (100% traffic)
2. Green: new version (deployed but no traffic)
3. Smoke test green environment
4. Switch traffic: blue → green (instant or gradual)
5. Keep blue running for 30 minutes (rollback window)
6. Tear down blue

Implementation options:
- **AWS ECS**: blue/green with CodeDeploy
- **Kubernetes**: two Deployments, update Service selector
- **Nginx**: upstream groups, reload config without downtime
- **Feature flags**: code-level blue/green

For MY stack: complete implementation with rollback procedure.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
