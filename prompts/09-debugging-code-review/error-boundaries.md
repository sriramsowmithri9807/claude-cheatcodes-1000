---
title: "Implement Comprehensive Error Handling"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [error-handling, debugging, resilience, node-js]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement comprehensive error handling for my application.

Current code: [PASTE RELEVANT CODE]
Current problem: [DESCRIBE: unhandled errors, unclear error messages, missing logging]

1. **Error classification**: operational vs programmer errors
2. **Error types**: create domain-specific error classes
3. **Async error handling**: catch all promise rejections
4. **Middleware**: centralized Express error handler
5. **Logging**: structured error logging with context
6. **User messages**: never show stack traces to users
7. **Recovery**: graceful degradation for non-fatal errors
8. **Alerting**: page on-call for critical errors
9. **Error tracking**: Sentry or equivalent integration
10. **Testing**: test that errors are caught and handled correctly

Transform my code with all these patterns applied.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
