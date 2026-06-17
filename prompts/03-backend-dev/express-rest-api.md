---
title: "Build a Production Express.js REST API"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [express, nodejs, typescript, rest]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a production-ready REST API with Express.js + TypeScript for: [APP DESCRIPTION].

Include:
- Folder structure: routes/, controllers/, services/, middleware/, models/
- JWT authentication middleware
- Request validation with Zod
- Error handling middleware (centralized)
- Rate limiting (express-rate-limit)
- Helmet.js security headers
- Morgan request logging
- CORS configuration
- Health check endpoint: GET /health
- Environment config with dotenv-safe
- Swagger/OpenAPI docs with swagger-ui-express
- Graceful shutdown handling
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
