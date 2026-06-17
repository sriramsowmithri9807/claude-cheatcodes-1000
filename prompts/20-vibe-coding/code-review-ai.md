---
title: "Get Your Code Reviewed by AI"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [code-review, ai, claude, quality]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Get a comprehensive AI code review.

Code to review:
```[LANGUAGE]
[PASTE YOUR CODE]
```

Review my code from these perspectives:

1. **Does it work?**
   - Logic errors
   - Edge cases not handled
   - Missing error handling

2. **Is it secure?**
   - Input validation
   - Authentication/authorization
   - Data exposure

3. **Is it performant?**
   - Unnecessary loops or computations
   - Database query efficiency
   - Memory usage

4. **Is it readable?**
   - Variable/function naming
   - Code complexity
   - Comments where needed

5. **Can it be simplified?**
   - Duplicate code
   - Overcomplicated solutions
   - Modern language features not used

6. **Will it scale?**
   - Bottlenecks at 10x scale
   - Design limitations

For each issue: severity + specific fix + explanation of why.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
