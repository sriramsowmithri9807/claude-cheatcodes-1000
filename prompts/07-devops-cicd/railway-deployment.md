---
title: "Deploy to Railway"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [railway, deployment, devops, beginner]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Deploy my full-stack app to Railway.

App: [DESCRIBE: frontend, backend, database]

Step-by-step:
1. `railway init` and `railway link` for existing project
2. **Environment variables**: set via dashboard or CLI
3. **PostgreSQL plugin**: provision and link to your app (DATABASE_URL auto-set)
4. **Redis plugin**: add for caching/queues
5. **Build command**: override if not auto-detected
6. **Start command**: override if needed
7. **Health checks**: configure for zero-downtime deploys
8. **Custom domain**: CNAME setup
9. **GitHub integration**: auto-deploy on push
10. **Deploy environments**: production + staging environments
11. **Monorepo**: deploy specific service from monorepo
12. **Viewing logs**: `railway logs`
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
