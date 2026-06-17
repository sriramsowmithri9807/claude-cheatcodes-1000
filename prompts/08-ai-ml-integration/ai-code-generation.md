---
title: "Build an AI Code Generation Tool"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [code-generation, claude, developer-tools, ai]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an AI code generation and explanation tool.

Use case: [DESCRIBE: generate boilerplate, explain code, convert between languages, refactor]
Language focus: [PROGRAMMING LANGUAGES]

1. **Code generation**: from natural language description → working code
2. **Multi-file generation**: generate an entire feature spanning multiple files
3. **Code explanation**: explain what this code does, line by line
4. **Code refactoring**: improve readability, performance, patterns
5. **Language conversion**: Python → TypeScript, SQL → code, etc.
6. **Test generation**: generate unit tests for existing code
7. **Documentation**: generate JSDoc/docstrings for functions
8. **Debugging help**: identify bugs and suggest fixes
9. **Code review**: review for security, performance, style issues
10. **Interactive REPL**: user iterates on generated code in conversation

UI with Monaco editor (VS Code in browser).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
