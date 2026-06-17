---
title: "Secure Your API Against Common Attacks"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, api, owasp, backend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Harden my API against the OWASP API Security Top 10.

My API: [DESCRIBE]

1. **Broken Object Level Auth (BOLA)**: verify ownership on every request
2. **Broken Auth**: JWT best practices, no weak secrets
3. **Broken Object Property Level Auth**: never expose more fields than needed
4. **Unrestricted Resource Consumption**: rate limiting, pagination limits
5. **Broken Function Level Auth**: re-verify role on admin operations
6. **Unrestricted Access to Sensitive Business Flows**: apply stricter limits
7. **Server Side Request Forgery**: validate and allowlist URLs
8. **Security Misconfiguration**: headers, CORS, debug endpoints
9. **Improper Inventory Management**: disable unused endpoints
10. **Unsafe Consumption of APIs**: validate third-party API responses

For each: code example of the vulnerability + the fix.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
