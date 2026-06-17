---
title: "Apply Test-Driven Development"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [tdd, red-green-refactor, testing, methodology]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Apply TDD to implement this feature:

[DESCRIBE THE FEATURE TO IMPLEMENT]

TDD workflow (Red → Green → Refactor):

**Red phase** — write failing tests first:
1. Write a test for the simplest case that doesn't work yet
2. Run it, confirm it fails for the right reason
3. Write tests for all known cases (don't implement yet)

**Green phase** — minimum code to pass:
4. Write the minimum code to make the first test pass
5. Don't optimize, just make it work
6. Repeat for each test

**Refactor phase** — improve while tests stay green:
7. Improve naming, structure, eliminate duplication
8. Tests must remain passing

Output: complete test file + implementation file, built test by test.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
