---
title: "Secure a Node.js Application"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, nodejs, express, owasp]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Perform a security audit and harden my Node.js/Express application.

Current codebase: [DESCRIBE YOUR APP]

Fix these OWASP Top 10 issues:
1. **Injection**: parameterized queries, input sanitization
2. **Broken Auth**: JWT best practices, secure session management
3. **Sensitive Data**: encrypt PII, HTTPS everywhere, no secrets in logs
4. **XXE**: disable XML entity expansion
5. **Broken Access Control**: check authorization on every route
6. **Security Misconfiguration**: Helmet.js, remove X-Powered-By, CSP
7. **XSS**: output encoding, CSP headers
8. **Insecure Deserialization**: validate all deserialized data
9. **Known Vulnerabilities**: npm audit fix
10. **Insufficient Logging**: structured logging of security events

Output: security-hardened version of each vulnerable code section.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
