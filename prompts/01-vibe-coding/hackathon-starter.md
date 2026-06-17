---
title: "Build a Hackathon Project Starter"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [hackathon, rapid-prototype, fullstack, starter]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
I'm starting a hackathon in 1 hour. My project idea: [IDEA]. Time limit: [X hours].

Give me:
1. The exact tech stack to use (optimized for speed, not perfection)
2. A Next.js + TypeScript starter project with:
   - Auth (Clerk free tier)
   - Database (Supabase free tier)
   - UI (shadcn/ui)
   - Deployment config (Vercel)
3. The 3 pages/routes I need to build
4. The database schema
5. Hour-by-hour timeline
6. The one demo flow that will impress judges

Start with the complete `npx create-next-app` command and all setup steps.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
