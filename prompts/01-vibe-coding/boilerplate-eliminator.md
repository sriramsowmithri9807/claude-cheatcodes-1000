---
title: "Eliminate Boilerplate from Any Codebase"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [refactor, dry, clean-code, abstraction]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
You are a refactoring expert. Analyze this code:

[PASTE YOUR CODE]

Identify and eliminate ALL boilerplate:
1. List every repeated pattern you find (with line numbers)
2. Create reusable abstractions for each (utility functions, hooks, HOCs, base classes)
3. Rewrite the original code using your abstractions
4. Calculate the lines of code reduction
5. Explain why each abstraction improves maintainability

Follow the DRY principle without over-abstracting. The goal is clarity, not cleverness.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
