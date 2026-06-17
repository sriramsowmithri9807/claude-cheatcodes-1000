---
title: "Build a Simple Feature Flag System"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [feature-flags, backend, typescript, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a lightweight feature flag system for my Node.js app.

Requirements:
- Store flags in a JSON file (for simplicity) with live reload
- Types: boolean, percentage rollout, user-segment targeting
- SDK: `isEnabled(flagName, userId?)` function
- Admin API: GET/POST/PATCH flags
- React hook: `useFeatureFlag(name)` for frontend
- Audit log: who changed what flag and when

Keep it simple enough to understand in 10 minutes, powerful enough to use in production.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
