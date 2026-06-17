---
title: "Design API Authentication Systems"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [auth, api, jwt, oauth]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design the authentication system for my public API:

Consumers: [3rd-party developers / mobile apps / other services]
Security requirements: [DESCRIBE]

Design:
1. API Key authentication: generation, storage (hashed), rotation
2. JWT Bearer: access tokens, refresh, expiry
3. OAuth 2.0: authorization code + PKCE for third-party apps
4. HMAC request signing: for server-to-server (like AWS Signature)
5. Rate limiting per auth method (API keys get higher limits)
6. Scopes: define permission model for your API
7. Token revocation
8. Audit log: who accessed what and when

Output: auth spec document + implementation code for each method.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
