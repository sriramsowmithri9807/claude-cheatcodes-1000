---
title: "Handle AI Errors Gracefully"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [error-handling, claude, reliability, api]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Handle all error scenarios in my Claude API integration gracefully.

Error types to handle:
1. **Rate limit (429)**: exponential backoff: 1s, 2s, 4s, 8s, 16s, give up
2. **Overloaded (529)**: server busy — retry with longer delay
3. **Invalid request (400)**: prompt too long, invalid parameters — don't retry, fix it
4. **Auth error (401)**: invalid API key — alert, don't retry
5. **Timeout**: stream stalls — detect with timeout, abort and retry
6. **Partial response**: stream cut off mid-sentence — detect and complete or retry
7. **Content policy**: Claude refuses the request — graceful fallback message
8. **JSON parsing**: Claude returns malformed JSON — retry with stronger format instruction
9. **Token limit**: response truncated — detect and request continuation
10. **Network errors**: ECONNRESET, etc. — retry with backoff

Reusable retry wrapper for all Claude API calls.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
