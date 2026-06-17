---
title: "Conduct a Security Audit"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security-audit, review, checklist, security]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Conduct a comprehensive security audit of my application.

App: [DESCRIBE]
Audit scope: [WHAT'S INCLUDED]

**Audit checklist**:

Authentication:
□ Password hashing (bcrypt/argon2, not MD5/SHA1)
□ Brute force protection
□ MFA availability
□ Session fixation protection
□ Secure password reset

Authorization:
□ Every endpoint checks authentication
□ Every operation checks ownership (IDOR)
□ Admin functions separately protected

Data:
□ Sensitive data encrypted at rest
□ PII minimization
□ Secure deletion

Infrastructure:
□ Secrets not in code
□ HTTPS everywhere
□ Security headers set
□ Dependencies up to date

Code:
□ Input validation
□ Output encoding
□ No eval(), no innerHTML with user data

Output: findings report with severity ratings + remediation plan.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
