---
title: "Implement Secure Session Management"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sessions, security, auth, web]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement secure session management.

App: [DESCRIBE YOUR AUTH APPROACH]

1. **Session ID generation**: `crypto.randomBytes(32)` — cryptographically random
2. **Storage**: server-side (Redis) — not stateful client-side (JWT for stateless)
3. **Cookie flags**: `httpOnly; Secure; SameSite=Lax; Path=/`
4. **Session expiry**: idle timeout (30 min) + absolute timeout (8 hours)
5. **Session fixation**: regenerate session ID on login
6. **Concurrent sessions**: detect and limit (optional)
7. **Session revocation**: ability to invalidate specific sessions
8. **Log all sessions**: device, IP, created time — show to user
9. **Logout**: invalidate server-side immediately
10. **"Remember me"**: separate long-lived token, not just longer session

Node.js with Express + `express-session` + Redis store:
11. Configuration code
12. Middleware setup
13. Login/logout handlers
14. Admin: view and terminate user sessions
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
