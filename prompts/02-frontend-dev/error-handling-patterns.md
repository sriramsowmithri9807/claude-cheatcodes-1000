---
title: "Master Frontend Error Handling"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [error-handling, react, typescript, reliability]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement comprehensive error handling for a React + TypeScript app.

Types of errors to handle:
1. **Network errors**: API down, timeout, no internet
2. **API errors**: 4xx responses with error details from server
3. **Validation errors**: map server validation to form fields
4. **JavaScript errors**: Error Boundary for unexpected crashes
5. **Async errors**: unhandled promise rejections
6. **Missing data**: null/undefined guards with fallbacks

For each:
- How to catch it
- What to show the user
- What to log (and how much detail)
- How to recover without page refresh

Include: a centralized error reporting service (Sentry or custom).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
