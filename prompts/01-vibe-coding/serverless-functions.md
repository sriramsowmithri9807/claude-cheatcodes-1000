---
title: "Build Serverless Functions for Your App"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [serverless, aws-lambda, vercel-functions, edge]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build serverless functions for my app. I need to handle:

[LIST YOUR BACKEND OPERATIONS]

For each function:
1. Implementation (TypeScript, compatible with Vercel/AWS Lambda/Cloudflare Workers)
2. Input validation with Zod
3. Error handling with proper HTTP status codes
4. Cold start optimization
5. Environment variable usage
6. Local testing with Vitest
7. Deployment config

Also include: a shared middleware pattern for auth, logging, and CORS.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
