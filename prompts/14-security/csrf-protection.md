---
title: "Implement CSRF Protection"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [csrf, security, web, tokens]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement CSRF (Cross-Site Request Forgery) protection.

App: [DESCRIBE YOUR AUTHENTICATION METHOD]

1. **What is CSRF**: malicious site makes authenticated requests on behalf of user
2. **When you're vulnerable**: session cookies, no Origin/Referer check
3. **SameSite cookies**: `SameSite=Lax` or `Strict` — primary defense
4. **CSRF token**: synchronizer token pattern
   - Generate per-session random token
   - Include in every form as hidden field
   - Validate on backend
5. **Double submit cookie**: stateless CSRF prevention
6. **Origin/Referer check**: server validates request origin
7. **Custom header**: `X-Requested-With` for AJAX requests
8. **Framework built-in**: Express CSRF middleware, Django CSRF, Rails authenticity token
9. **SPA/JWT**: cookie-less → no CSRF risk
10. **Testing**: use Burp Suite to verify protection

Implement CSRF protection for my specific setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
