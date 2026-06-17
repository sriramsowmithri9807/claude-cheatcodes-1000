---
title: "Set Security Headers on Every API Response"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, headers, express, backend]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Set proper HTTP security headers on every API response.

Using: Helmet.js for Express.js

Explain and configure:
1. `Content-Security-Policy`: prevent XSS (show the directives)
2. `X-Content-Type-Options: nosniff`: prevent MIME sniffing
3. `X-Frame-Options: DENY`: prevent clickjacking
4. `Strict-Transport-Security`: enforce HTTPS
5. `Referrer-Policy: strict-origin`: control referer
6. `Permissions-Policy`: disable unused browser features
7. `X-XSS-Protection: 0`: (paradoxically, disable the old filter)
8. `Cache-Control`: prevent caching of sensitive data
9. CORS headers: restrict origins, methods, headers
10. Remove: `X-Powered-By: Express` (stop advertising your stack)

Show the Helmet.js config and test with securityheaders.com.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
