---
title: "Apply Mutation Testing"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [mutation-testing, stryker, quality, testing]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply mutation testing to measure real test quality.

Code to mutate: [PASTE OR DESCRIBE YOUR CODE AND TESTS]
Framework: Stryker (JavaScript/TypeScript)

What mutation testing does:
- Automatically introduces bugs (mutations) into your code
- Runs tests against each mutation
- If tests PASS with a bug → tests are not catching this case
- Mutation score = killed mutations / total mutations

Setting up Stryker:
1. Install: `npm install --save-dev @stryker-mutator/core`
2. Configure: stryker.config.json
3. Run: `npx stryker run`
4. Interpret: HTML report showing survived mutations

For each survived mutation:
5. What bug wasn't caught?
6. Write a test that kills it
7. Target: > 80% mutation score

Output: Stryker config + analysis of gaps + new tests to kill survivors.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
