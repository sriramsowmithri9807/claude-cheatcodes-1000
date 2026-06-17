---
title: "Write Comprehensive Unit Tests"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, unit-tests, jest, vitest]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write comprehensive unit tests for this code:

```[LANGUAGE]
[PASTE YOUR CODE]
```

Requirements:
1. **Test every function** — not just the happy path
2. **Edge cases**: empty input, null, undefined, zero, negative numbers, max values
3. **Error cases**: test that errors are thrown correctly
4. **Boundaries**: values at the edge of acceptable ranges
5. **Integration points**: mock external dependencies (DB, API, time)
6. **Arrange-Act-Assert**: clean test structure
7. **Descriptive names**: `it('should return empty array when no users exist')`
8. **No test duplication**: parameterized tests where appropriate
9. **Coverage**: target 100% for this module
10. **Fast**: all tests run in < 100ms (mock I/O)

Framework: Vitest (Jest compatible).
Output: complete test file with all tests passing.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
