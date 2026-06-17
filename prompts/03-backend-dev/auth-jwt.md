---
title: "Implement JWT Authentication from Scratch"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [jwt, auth, security, nodejs]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement JWT authentication from scratch in Node.js (to deeply understand it).

Don't use passport.js — implement manually.

Implement:
1. User registration (bcrypt password hashing, salt rounds = 12)
2. User login (compare hash, issue access + refresh tokens)
3. Access token: 15 min expiry, sign with RS256 (asymmetric)
4. Refresh token: 7 day expiry, store hash in DB
5. Token refresh endpoint
6. Logout (invalidate refresh token in DB)
7. Auth middleware (verify JWT signature, check expiry)
8. Token rotation (new refresh token on each refresh)
9. Token revocation list (Redis set for logged-out users)
10. Security: httpOnly cookie storage vs Authorization header — show both

Explain every security decision.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
