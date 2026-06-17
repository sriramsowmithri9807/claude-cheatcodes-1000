---
title: "Implement Password Security Best Practices"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [passwords, security, hashing, auth]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement password security best practices.

**Hashing** (NOT encryption):
1. **Algorithm**: Argon2id (preferred) or bcrypt (cost=12+)
2. **Salt**: automatic per-password (done by argon2/bcrypt library)
3. **Node.js**: `argon2` npm package
4. Never: MD5, SHA1, SHA256 for passwords (too fast)

**Password policy**:
5. Minimum 8 characters (12+ encouraged)
6. Check against HaveIBeenPwned breached password list
7. Allow spaces and all special characters
8. Don't force regular rotation (causes weaker passwords)
9. Strength meter feedback (zxcvbn library)

**Password reset**:
10. Random token, not predictable
11. Short expiry: 15 minutes
12. Single-use: invalidate after use
13. Email to registered address only
14. Rate limit: 3 reset requests per hour

**Account protection**:
15. Failed attempt lockout (with alert to user)
16. Password change → invalidate all other sessions

Output: complete password management implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
