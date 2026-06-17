---
title: "Implement API Key Management"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api-keys, security, authentication, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement a secure API key management system.

My API: [DESCRIBE]
Key consumers: [DEVELOPERS / INTERNAL SERVICES]

1. **Key generation**: cryptographically random, 32 bytes, base64-encoded
2. **Key format**: prefix for identification (e.g., `sk_live_` or `key_`)
3. **Storage**: store HASH of key (not plaintext), using SHA-256
4. **First display**: show key only once after creation, then never again
5. **Key scopes**: read-only, write, admin — principle of least privilege
6. **Expiration**: optional expiry date
7. **Rate limiting**: per-key rate limits
8. **Usage tracking**: log every request with key ID (not full key)
9. **Key rotation**: create new → test → revoke old
10. **Revocation**: instant revocation, check blocklist in auth middleware
11. **Multi-key**: users can have multiple keys (dev vs production)
12. **Dashboard**: users view/manage/revoke their own keys

Output: complete implementation with all endpoints.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
