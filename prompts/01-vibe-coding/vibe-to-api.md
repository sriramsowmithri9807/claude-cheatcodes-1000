---
title: "Turn a Vibe / Feeling into an API"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, design, creative, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
I want an API that feels like [DESCRIBE THE VIBE — e.g., "a calm productivity tool", "a chaotic creative playground"].

Design and implement:
1. The REST API routes (method, path, request body, response shape)
2. Express.js implementation with TypeScript
3. Meaningful status codes and error messages that match the vibe
4. A sample `.http` or `curl` test file
5. A one-paragraph "API philosophy" doc comment at the top of the file

Make the developer experience match the vibe — from variable names to error messages.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
