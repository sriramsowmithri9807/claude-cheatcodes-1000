---
title: "Perform Security Testing"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, testing, owasp, penetration]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Perform security testing on my application.

App: [DESCRIBE YOUR APP]
Auth type: [JWT / session / OAuth]

Security tests to run:

**Authentication**:
1. Brute force: rate limiting works?
2. JWT manipulation: tampered token rejected?
3. Session fixation: session ID changes on login?

**Authorization (IDOR)**:
4. Access other user's resources by changing ID in URL
5. Horizontal privilege escalation
6. Vertical privilege escalation (regular → admin)

**Injection**:
7. SQL injection: special chars in all inputs
8. XSS: script tags in all text inputs
9. Command injection: shell metacharacters

**Logic**:
10. Price manipulation: modify amount in request
11. Race conditions: parallel requests

Tool: OWASP ZAP or manual testing with Burp Suite.
Output: test scripts + found vulnerabilities + fixes.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
