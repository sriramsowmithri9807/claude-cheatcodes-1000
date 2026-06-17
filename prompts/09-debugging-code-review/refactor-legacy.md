---
title: "Refactor Legacy Code"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [refactoring, legacy, clean-code, modernization]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Refactor this legacy code to modern standards:

```[LANGUAGE]
[PASTE LEGACY CODE]
```

Refactoring goals:
1. **Readability**: meaningful names, small functions, clear intent
2. **Modern syntax**: arrow functions, destructuring, optional chaining, nullish coalescing
3. **Error handling**: proper try/catch, typed errors
4. **Type safety**: add TypeScript types if applicable
5. **DRY**: eliminate code duplication
6. **SOLID principles**: single responsibility, open/closed
7. **Remove dead code**: unused variables, unreachable branches
8. **Test coverage**: make it testable (dependency injection)

Show: diff-style before/after for each change, with explanation of why.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
