---
title: "Build a Full App from One Sentence"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [fullstack, rapid-prototype, mvp]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
You are a 10x developer building an MVP in record time. I want to build: [ONE SENTENCE DESCRIPTION].

Produce:
1. A folder structure for this app
2. A tech stack recommendation with reasoning
3. The complete code for the core feature (the ONE thing that makes this app useful)
4. A `README.md` with setup instructions
5. A list of 5 next features to add after the MVP

Keep the code clean, working, and minimal. No over-engineering. Ship it.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
