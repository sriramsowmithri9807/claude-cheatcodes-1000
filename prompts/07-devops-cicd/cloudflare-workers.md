---
title: "Deploy with Cloudflare Workers"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cloudflare, workers, edge, deployment]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Deploy my application to Cloudflare Workers (edge computing).

App type: [API / static site / SSR / proxy]

Implement:
1. **Worker script** in TypeScript using Hono framework
2. **KV storage**: for caching, session state, feature flags
3. **D1 database**: SQLite at the edge for small datasets
4. **R2 storage**: S3-compatible object storage
5. **Durable Objects**: stateful edge (real-time collaboration, rate limiting)
6. **Queue**: Cloudflare Queues for background processing
7. **Cron triggers**: scheduled jobs
8. **Wrangler config**: `wrangler.toml` with environments
9. **CI/CD**: GitHub Actions → `wrangler deploy`
10. **Custom domain**: bind to your domain with Cloudflare DNS
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
