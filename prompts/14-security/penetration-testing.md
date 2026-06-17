---
title: "Perform Penetration Testing"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pen-testing, security, owasp-zap, burp-suite]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Perform penetration testing on my web application.

App: [DESCRIBE YOUR APP]
Scope: [WHAT IS IN/OUT OF SCOPE]

**OWASP ZAP** (open source):
1. Spider: discover all URLs
2. Active scan: automated vulnerability detection
3. Manual testing: using ZAP as proxy
4. Authentication: configure to test authenticated areas
5. Report: generate HTML report

**Manual testing checklist**:
6. Authentication bypass: try accessing protected pages without login
7. IDOR: change user IDs in requests
8. Parameter tampering: modify prices, quantities, roles
9. File inclusion: path traversal in file parameters
10. XXE: XML input with entity injection
11. CORS: check what origins are allowed
12. Cookie security: httpOnly, Secure, SameSite flags

**Remediation**:
13. Prioritize by CVSS severity score
14. Fix → retest → close finding
15. Report: executive summary + technical findings

Output: pen test checklist for my specific app.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
