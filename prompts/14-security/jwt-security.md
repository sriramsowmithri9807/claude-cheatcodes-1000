---
title: "Implement Secure JWT Authentication"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [jwt, auth, security, tokens]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement JWT authentication with all security best practices.

1. **Algorithm**: use RS256 (asymmetric), NOT HS256 for distributed systems
   - Private key: sign on auth server
   - Public key: verify on resource servers
2. **Payload**: minimal claims (sub, iat, exp, jti)
   - Never put sensitive data in JWT payload (it's base64-decodable)
3. **Expiry**: access token 15 minutes, refresh token 7 days
4. **JTI**: JWT ID for replay prevention
5. **Refresh token rotation**: new refresh token on each use
6. **Token revocation**: Redis blocklist for logged-out tokens
7. **Storage**: httpOnly secure cookie (not localStorage)
8. **CSRF protection**: if using cookies
9. **Algorithm confusion attack**: explicitly verify algorithm
10. **Key rotation**: rotate signing keys without downtime

Node.js implementation with `jose` or `jsonwebtoken` library.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
