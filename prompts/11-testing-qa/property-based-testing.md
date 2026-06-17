---
title: "Apply Property-Based Testing"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [property-based, fast-check, testing, generative]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply property-based testing to find edge cases I'd never think of.

Code to test: [PASTE YOUR FUNCTIONS]
Framework: fast-check (JavaScript)

Property-based testing:
- Instead of `expect(add(1, 2)).toBe(3)`, you define PROPERTIES
- Properties: things that should ALWAYS be true
- fast-check generates hundreds of random inputs
- Shrinks failing input to the simplest case

Examples of properties:
- `sort(arr)` should always return same length as `arr`
- `add(a, b) === add(b, a)` (commutativity)
- `parse(serialize(data))` equals `data` (roundtrip)
- `encode` then `decode` returns original string

For my code:
1. Identify properties that should always hold
2. Write fast-check tests for each property
3. Run and interpret failures
4. Add any found edge cases to unit tests as regression tests
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
