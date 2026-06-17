---
title: "Implement OAuth 2.0 and OIDC"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [oauth, oidc, auth, security]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement OAuth 2.0 / OpenID Connect from scratch (to understand it deeply).

Implement both sides:
**Authorization Server** (simplified, for learning):
1. Authorization endpoint (redirect with code)
2. Token endpoint (exchange code for access + refresh + ID token)
3. PKCE support (prevent interception attacks)
4. UserInfo endpoint
5. JWKS endpoint (public keys for JWT verification)

**Resource Server**:
1. JWT validation middleware (verify signature, claims, expiry)
2. Scope checking

**Client** (your app):
1. Full OAuth flow implementation
2. Token refresh logic
3. Secure token storage

Show: complete request/response flow with actual HTTP examples.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
