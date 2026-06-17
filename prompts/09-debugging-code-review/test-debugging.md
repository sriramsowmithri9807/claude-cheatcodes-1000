---
title: "Debug Failing Tests"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, debugging, jest, vitest]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Debug my failing tests.

Test output:
```
[PASTE FAILING TEST OUTPUT]
```

Test code:
```javascript
[PASTE FAILING TEST]
```

Implementation code:
```javascript
[PASTE IMPLEMENTATION]
```

1. Parse the test failure message — what exactly failed?
2. Is the test wrong or is the implementation wrong?
3. Check: mocking issues? Async test issues? Setup/teardown?
4. Fix whichever is incorrect
5. Identify any related tests that might also be broken
6. How to make these tests less brittle in the future?
7. Run: what command to run just this test for quick iteration?
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
