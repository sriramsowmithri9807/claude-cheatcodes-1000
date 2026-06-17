---
title: "Secure REST APIs"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, security, auth, rest]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement comprehensive security for my REST API.

API: [DESCRIBE]

**Authentication**:
1. JWT with RS256 (not HS256)
2. Short expiry access tokens (15 min)
3. Secure refresh token rotation

**Authorization**:
4. Check on every endpoint (not just middleware)
5. Resource ownership check (IDOR prevention)
6. Role validation for admin operations

**Input validation**:
7. Validate all inputs with Zod
8. Sanitize strings (trim, max length)
9. Validate file uploads (type, size, magic bytes)

**Output security**:
10. Never expose internal IDs if sequential (use UUID)
11. Filter response fields (don't return password hash)
12. Rate limiting per endpoint

**Infrastructure**:
13. HTTPS only (HSTS header)
14. Security headers (Helmet.js)
15. Request logging for audit
16. Secrets in environment variables

Output: security middleware stack for Express.js.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
