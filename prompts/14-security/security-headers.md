---
title: "Implement HTTP Security Headers"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, headers, http, web]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Implement all necessary HTTP security headers.

Server: [Nginx / Express / Next.js / Cloudflare]

Required headers:
1. **Content-Security-Policy**: strict policy preventing XSS
   - `default-src 'self'; script-src 'self'; ...`
   - Start with Report-Only mode, then enforce
2. **Strict-Transport-Security**: `max-age=31536000; includeSubDomains; preload`
3. **X-Content-Type-Options**: `nosniff`
4. **X-Frame-Options**: `DENY` (use CSP frame-ancestors instead for flexibility)
5. **Referrer-Policy**: `strict-origin-when-cross-origin`
6. **Permissions-Policy**: disable unused APIs: camera, microphone, geolocation
7. **Cross-Origin-Opener-Policy**: `same-origin`
8. **Cross-Origin-Resource-Policy**: `same-origin`

Remove:
9. `X-Powered-By` header (reveals stack)
10. `Server` header (reveals server software)

Test: securityheaders.com (target: A+).
Output: Nginx config / Express Helmet.js config / Next.js headers config.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
