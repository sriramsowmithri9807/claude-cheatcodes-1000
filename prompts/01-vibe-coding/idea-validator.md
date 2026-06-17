---
title: "Validate a Product Idea with Claude"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [product, validation, startup, research]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Act as an experienced product manager and startup advisor. Validate this idea: [YOUR IDEA].

Provide:
1. **Market size estimate** (TAM/SAM/SOM)
2. **3 strongest reasons this could work**
3. **3 biggest risks that could kill it**
4. **Competitor landscape** (direct and indirect)
5. **The riskiest assumption** to test first
6. **A 2-week validation experiment** I can run with no code
7. **Verdict**: Build it / Don't build it / Build something adjacent

Be brutally honest. Don't sugarcoat.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
