---
title: "Debug and Write Regular Expressions"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [regex, debugging, patterns, parsing]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Help me write and debug a regular expression.

What I need to match: [DESCRIBE OR GIVE EXAMPLES]
Examples that should match:
- [EXAMPLE 1]
- [EXAMPLE 2]

Examples that should NOT match:
- [COUNTER-EXAMPLE 1]

My current regex (if any): [YOUR REGEX]
What's wrong with it: [DESCRIBE]

1. Write the correct regex
2. Explain each part of the regex
3. Test against all my examples
4. Handle edge cases I might have missed
5. Performance considerations for large inputs
6. Language-specific notes: [JavaScript / Python / Java]
7. Online regex tester link for further experimentation
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
