---
title: "Deploy to Fly.io"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [fly-io, deployment, containers, devops]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Deploy my application to Fly.io.

App: [DESCRIBE: what it is, what port it listens on, any databases/redis needed]

1. **fly.toml**: complete config file
   - app name, region selection
   - HTTP service with internal port
   - health check configuration
   - environment variables
   - volume mounts for persistent data
2. **Dockerfile**: optimized for Fly.io
3. **PostgreSQL**: provision Fly Postgres cluster
4. **Redis**: Upstash Redis integration
5. **Secrets**: `fly secrets set KEY=VALUE`
6. **Scaling**: `fly scale count 2` for zero-downtime deploys
7. **GitHub Actions**: auto-deploy on push to main
8. **Custom domain**: add and configure SSL
9. **Monitoring**: Fly metrics integration
10. **Connecting locally**: fly proxy for local DB access
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
