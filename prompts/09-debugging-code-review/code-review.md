---
title: "Perform a Thorough Code Review"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [code-review, quality, feedback]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
You are a senior engineer with 15 years experience. Perform a thorough code review on this code:

```[LANGUAGE]
[PASTE YOUR CODE]
```

Review for:
1. **Bugs**: logic errors, edge cases not handled, potential exceptions
2. **Security**: injection, auth, data exposure, input validation
3. **Performance**: N+1 queries, unnecessary loops, memory leaks
4. **Readability**: naming, comments, cognitive complexity
5. **Design**: SOLID principles, separation of concerns
6. **Testability**: is this code easy to unit test?
7. **Error handling**: missing try/catch, unhandled promise rejections
8. **TypeScript**: type safety, any usage, type assertions

Format: severity (critical/major/minor) + line reference + explanation + fix
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
