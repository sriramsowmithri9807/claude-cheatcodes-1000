---
title: "Implement Two-Factor Authentication"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [2fa, totp, auth, security]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement two-factor authentication (2FA) for my application.

App: [DESCRIBE YOUR AUTH SYSTEM]

**TOTP (Time-based One-Time Password)**:
1. Generate secret: `speakeasy.generateSecret()`
2. QR code: encode otpauth URI as QR code (qrcode library)
3. Show to user for Google Authenticator / Authy
4. Verify code: `speakeasy.totp.verify()` with 1-window tolerance
5. Backup codes: generate 10 single-use codes on setup
6. Store: secret encrypted in database

**2FA enrollment flow**:
7. User enables 2FA in settings
8. Show QR code + manual entry code
9. Verify user scanned correctly (enter code to confirm)
10. Show backup codes once (require user to save them)

**2FA login flow**:
11. After password → if 2FA enabled → prompt for TOTP
12. "Remember this device" option (30 day cookie)
13. Rate limit TOTP attempts (3 per minute)
14. Backup code flow when TOTP not available

Output: complete 2FA implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
