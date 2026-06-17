---
title: "Configure CORS Correctly"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cors, security, web, api]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Configure CORS (Cross-Origin Resource Sharing) correctly for my API.

My origins:
- Production frontend: https://myapp.com
- Staging: https://staging.myapp.com
- Development: http://localhost:3000

Node.js/Express setup:
1. Allow specific origins (NOT `*` for authenticated endpoints)
2. Allow specific methods: GET, POST, PUT, PATCH, DELETE
3. Allow specific headers: Content-Type, Authorization
4. `credentials: true` for cookies (requires specific origin, not *)
5. Preflight caching: `maxAge: 86400` (24h cache for OPTIONS requests)
6. Error response for rejected origins

Config:
7. Different origins per environment (env variable)
8. Dynamic origin validation (regex for subdomains)

Common mistakes:
9. Using `*` with `credentials: true` (doesn't work, AND is insecure)
10. Forgetting preflight: OPTIONS requests must also pass CORS

Output: complete CORS configuration for Express + Nginx.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
