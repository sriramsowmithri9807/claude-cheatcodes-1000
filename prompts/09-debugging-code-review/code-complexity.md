---
title: "Reduce Code Complexity"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [complexity, refactoring, clean-code, cognitive]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Reduce the complexity of this code:

```[LANGUAGE]
[PASTE CODE]
```

Metrics (if available): Cyclomatic complexity: [N], Lines per function: [N]

Techniques to apply:
1. **Extract Method**: break long functions into smaller ones
2. **Replace Conditionals**: strategy pattern, polymorphism, lookup tables
3. **Early returns**: reduce nesting with guard clauses
4. **Replace loop with pipeline**: map/filter/reduce
5. **Introduce Parameter Object**: group related params
6. **Remove dead code**: unreachable branches
7. **Simplify boolean**: `return condition` not `if (x) return true else return false`
8. **Extract constants**: replace magic numbers with named constants

Target: cyclomatic complexity < 10, functions < 20 lines.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
