---
title: "Fix OWASP Top 10 Vulnerabilities"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [owasp, security, vulnerabilities, web]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Audit and fix OWASP Top 10 vulnerabilities in my application.

App: [DESCRIBE YOUR STACK AND WHAT IT DOES]

For each vulnerability: explain, find in my code, and fix:

1. **A01 Broken Access Control**: check every endpoint for authorization
2. **A02 Cryptographic Failures**: find plaintext storage of secrets
3. **A03 Injection**: SQL, command, LDAP injection points
4. **A04 Insecure Design**: missing rate limiting, missing business logic guards
5. **A05 Security Misconfiguration**: debug mode, default creds, exposed admin
6. **A06 Vulnerable Components**: npm audit, outdated dependencies
7. **A07 Auth Failures**: brute force, weak session management
8. **A08 Integrity Failures**: unsigned updates, deserialization
9. **A09 Logging Failures**: not logging security events
10. **A10 SSRF**: user-controlled URLs in server-side requests

For each: code example of the vulnerability + the fix + test to verify.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
