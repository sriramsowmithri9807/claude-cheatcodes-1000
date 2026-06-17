---
title: "Debug API Integration Issues"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, debugging, http, integration]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Debug my API integration issue.

I'm calling: [API NAME / URL]
Request I'm sending: [PASTE curl command or request code]
Expected response: [DESCRIBE]
Actual response: [PASTE ERROR OR WRONG RESPONSE]

1. Analyze the request — is it correctly formed?
2. Check auth headers — are they present and correct format?
3. Check request body — content-type, encoding, required fields
4. Check status code — what does this code specifically mean for this API?
5. Parse the error message — what is it actually saying?
6. Check rate limits — am I being throttled?
7. Fix the request
8. How to test it: corrected curl command

Also: how to debug this type of API issue independently in the future.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
