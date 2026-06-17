---
title: "Write Better Code Comments"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [comments, documentation, code-quality, best-practices]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Improve code comments and documentation in my codebase.

Code: [PASTE YOUR CODE]

Comment principles:
1. **Why, not what**: code shows what, comments explain why
2. **Don't state the obvious**: `i++ // increment i` is useless
3. **Business context**: why this specific algorithm? Why this value?
4. **Gotchas**: warn about non-obvious behavior, performance implications
5. **TODO format**: `// TODO(username): description` with actionable notes

Docstring standards:
6. **JSDoc** (JavaScript): @param, @returns, @throws, @example
7. **Python docstrings**: Google style or NumPy style
8. **Class docs**: purpose, invariants, usage example
9. **Function docs**: what it does, params, return, side effects

For each function/class in my code:
- Remove misleading comments
- Add missing why-comments
- Add complete JSDoc/docstrings

Output: fully documented code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
