---
title: "Implement Security Rate Limiting"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rate-limiting, security, brute-force, ddos]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement rate limiting to prevent brute force and DDoS attacks.

Endpoints to protect:
- Login: strict (5 attempts per 15 minutes per IP)
- Registration: moderate (10 per hour per IP)
- Password reset: strict (3 per hour per email)
- API: per-key limits
- Static: generous (1000/min per IP)

Implement:
1. Express rate limiting middleware (express-rate-limit)
2. Redis backend for distributed limiting
3. Sliding window algorithm
4. IP-based limiting (with proxy header handling)
5. User-based limiting (authenticated endpoints)
6. Account lockout after N failed logins
7. Exponential backoff message (don't reveal exact limit)
8. Bypass for monitoring/health checks
9. DDoS mitigation at CDN level (Cloudflare)
10. 429 response with Retry-After header

Output: complete middleware implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
