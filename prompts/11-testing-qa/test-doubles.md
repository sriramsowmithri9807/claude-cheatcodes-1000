---
title: "Master Test Doubles"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [mocking, stubs, fakes, testing]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Master test doubles (the proper terminology for mocks).

Code under test: [PASTE CODE WITH DEPENDENCIES]

Test double types:
1. **Dummy**: object passed but never used (fill required params)
2. **Stub**: returns canned answer, no behavior verification
3. **Spy**: records calls, can assert on them later
4. **Mock**: pre-programmed with expectations, verifies behavior
5. **Fake**: working implementation, but simplified (in-memory DB)

When to use each:
6. Dummy: when a dep is required but irrelevant to the test
7. Stub: when you need controlled return values
8. Spy: when you want to verify a function was called
9. Mock: when behavior (call count, args) matters
10. Fake: when real implementation is too slow for tests (DB)

Implement each type for my specific dependencies.
Mistakes to avoid: over-mocking, testing the mock instead of the code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
