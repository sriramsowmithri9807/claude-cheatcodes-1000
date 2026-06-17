---
title: "Identify and Fix Code Smells"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [code-smells, refactoring, clean-code, quality]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Identify and fix code smells in this codebase:

```[LANGUAGE]
[PASTE CODE]
```

Scan for all 22 classic code smells:
1. Long Method
2. Large Class
3. Primitive Obsession
4. Long Parameter List
5. Divergent Change
6. Shotgun Surgery
7. Feature Envy
8. Data Clumps
9. Switch Statements
10. Parallel Inheritance Hierarchies
11. Lazy Class
12. Speculative Generality
13. Temporary Field
14. Message Chains
15. Middle Man
16. Inappropriate Intimacy
17. Alternative Classes with Different Interfaces
18. Incomplete Library Class
19. Data Class
20. Refused Bequest
21. Comments (that explain bad code instead of fixing it)
22. Duplicate Code

For each found: location + explanation + refactoring.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
