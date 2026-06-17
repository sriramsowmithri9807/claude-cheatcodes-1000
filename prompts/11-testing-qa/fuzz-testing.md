---
title: "Apply Fuzzing to Find Security Bugs"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [fuzzing, security, testing, bugs]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply fuzzing to find security vulnerabilities and bugs in my code.

Code to fuzz: [DESCRIBE YOUR PARSER / API / FUNCTION]

Fuzzing types:
1. **Mutation fuzzing**: take valid input, randomly mutate
2. **Generation fuzzing**: generate inputs from grammar
3. **Coverage-guided fuzzing**: find inputs that cover new code paths

Tools:
4. **Node.js**: `@jazzer.js/core` (coverage-guided)
5. **Python**: `atheris` (coverage-guided fuzzer from Google)
6. **API fuzzing**: OWASP ZAP API scan
7. **Property-based**: fast-check with arbitrary generators

Targets to fuzz:
8. Parsers: JSON, XML, CSV, image formats
9. API inputs: all endpoint parameters
10. Cryptographic functions: key/message combinations

For my code: fuzz harness setup + initial seed corpus + how to interpret crashes.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
