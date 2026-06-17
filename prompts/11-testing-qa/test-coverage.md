---
title: "Achieve High Test Coverage"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [coverage, testing, quality, metrics]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Help me achieve and maintain high test coverage for my codebase.

Current coverage: [CURRENT %]
Target: [TARGET %]
Uncovered code: [PASTE COVERAGE REPORT OR DESCRIBE]

1. **Identify gaps**: which files/functions have low coverage?
2. **Prioritize**: cover critical paths first (auth, payments, data mutations)
3. **Write tests for each gap**: generate tests for uncovered code
4. **Branch coverage**: test all if/else branches
5. **Edge case coverage**: empty arrays, null values, error paths
6. **Integration coverage**: tests that cover multiple units together
7. **Coverage thresholds**: fail CI if coverage drops below threshold
8. **Coverage reports**: HTML report + PR comment showing change
9. **Mutation testing**: does changing code make tests fail? (Stryker)
10. **What to not test**: 3rd party code, generated code, trivial getters

Output: specific tests for my coverage gaps.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
