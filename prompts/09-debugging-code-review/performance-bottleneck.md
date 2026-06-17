---
title: "Find and Fix Performance Bottlenecks"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [performance, profiling, optimization]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Help me find and fix the performance bottleneck in this code.

Code: [PASTE CODE]
Performance symptoms: [DESCRIBE: slow API, high CPU, memory growing, etc.]
Profiling data (if available): [PASTE FLAME GRAPH / METRICS]

Analyze:
1. What is the most expensive operation?
2. What is the algorithmic complexity? Can it be improved?
3. Are there unnecessary computations in loops?
4. Are there memory allocations that could be avoided?
5. Is there blocking I/O that should be async?
6. Is there N+1 query pattern?
7. Can results be cached or memoized?

Output: fixed code with explanation of each optimization and expected improvement.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
