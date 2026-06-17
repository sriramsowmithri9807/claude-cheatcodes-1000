---
title: "Set Up Bulletproof Environment Config"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [config, environment, secrets, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up bulletproof environment configuration for my Node.js/Next.js app.

Implement:
1. `env.ts` — typed env validation using Zod (crash on startup if invalid)
2. `.env.example` with all variables documented
3. `.env.local`, `.env.staging`, `.env.production` structure
4. GitHub Actions secrets setup guide
5. Docker environment file handling
6. How to rotate secrets without downtime
7. Which variables are safe to commit vs must be secret

Never let a missing env variable cause a silent bug in production again.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
