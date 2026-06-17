---
title: "Build an API Playground"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, playground, developer-experience, ui]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build an interactive API playground for my API (like Stripe's API explorer).

My API: [DESCRIBE]

Features:
1. Request builder: select method, endpoint, fill params/body
2. Auth: enter API key or use OAuth to get a token
3. Environment selector: sandbox vs production
4. Code generation: copy the request as cURL, JavaScript, Python, Ruby
5. Response viewer: formatted JSON, headers, status code
6. Request history: last 50 requests
7. Saved requests: name and save common requests
8. Schema viewer: explore all available endpoints with docs
9. Example responses: pre-loaded realistic examples
10. Dark mode

Stack: React + Monaco Editor (for JSON body) + fetch API.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
