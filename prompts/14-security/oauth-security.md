---
title: "Implement OAuth 2.0 Securely"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [oauth, oidc, security, auth]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement OAuth 2.0 security best practices.

OAuth flow: Authorization Code + PKCE (for web/mobile apps)

**Authorization Code + PKCE**:
1. Generate `code_verifier`: 32 random bytes, base64url encoded
2. `code_challenge`: SHA-256 hash of code_verifier, base64url
3. Include in authorization request
4. Server verifies challenge on token exchange

**State parameter**:
5. Generate random state, store in session
6. Verify state matches on callback (prevent CSRF)

**Token handling**:
7. Access tokens: short-lived (15 min)
8. Refresh tokens: rotate on each use
9. Store in httpOnly cookies or secure storage
10. Never in localStorage

**Authorization server choices**:
11. Auth0 / Clerk / AWS Cognito (managed)
12. Keycloak (self-hosted)

**Threats to protect against**:
13. Authorization code interception (solved by PKCE)
14. Token leakage in URL (use POST for token endpoint)
15. Open redirect (validate redirect_uri strictly)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
