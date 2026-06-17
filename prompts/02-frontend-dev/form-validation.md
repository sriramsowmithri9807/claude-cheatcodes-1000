---
title: "Master Form Validation Patterns"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [forms, react-hook-form, zod, typescript]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement comprehensive form validation for [FORM TYPE].

Using: react-hook-form + Zod

Patterns to cover:
1. Basic field validation (required, minLength, pattern)
2. Custom validators (async: check if email exists in DB)
3. Cross-field validation (confirm password, date ranges)
4. Dynamic field arrays (add/remove items)
5. Conditional fields (show field B only if field A = X)
6. File upload validation (type, size, dimensions)
7. Validation on blur vs on submit (when to use each)
8. Server-side error integration (map API errors to fields)
9. Form reset and dirty state tracking
10. Accessible error messages (aria-describedby)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
