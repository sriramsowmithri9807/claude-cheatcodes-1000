---
title: "Implement Comprehensive Input Validation"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [validation, security, sanitization, web]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement comprehensive input validation for my application.

Inputs to validate: [LIST YOUR API INPUTS]

**Principles**:
1. **Allow-list**: define what IS allowed, reject everything else
2. **Server-side**: always validate on server (client validation is UX, not security)
3. **Sanitization**: sanitize for output context (HTML, SQL, shell)
4. **Length limits**: set max length for all string inputs

**Implement validation for**:
5. Email: format + MX record check
6. URLs: protocol allow-list (http/https only)
7. File uploads: MIME type (magic bytes), size, name
8. Numbers: range, type
9. Dates: valid date, reasonable range
10. Enums: only allow defined values
11. HTML content: sanitize with DOMPurify
12. JSON: schema validation before processing

Using: Zod for TypeScript, Pydantic for Python.
Output: validation schema for each of my inputs.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
