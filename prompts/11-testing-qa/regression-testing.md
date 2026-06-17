---
title: "Set Up Regression Testing"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [regression, testing, automation, ci-cd]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up a regression testing process to prevent old bugs from returning.

Application: [DESCRIBE]
Past bugs: [DESCRIBE NOTABLE BUGS THAT OCCURRED]

1. **Bug-driven tests**: for every bug fixed, write a test that proves it's fixed
2. **Regression test suite**: dedicated suite of known-to-have-broken scenarios
3. **Run on every PR**: catch regressions before they merge
4. **Snapshot tests**: UI components don't visually regress
5. **API contract tests**: API responses don't regress
6. **Performance benchmarks**: latency doesn't regress (k6 + assertions)
7. **Database queries**: query counts don't regress (N+1 guard)
8. **Dependency updates**: test before merging Dependabot PRs

For my past bugs, write specific regression tests that would have caught them.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
