---
title: "Secure Webhook Endpoints"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [webhooks, security, api, hmac]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Secure my webhook-receiving endpoints against abuse and spoofing.

Webhooks I receive from: [LIST: Stripe, GitHub, Twilio, etc.]

For each webhook provider:
1. Signature verification (HMAC-SHA256, provider-specific header)
2. Timestamp validation (reject webhooks > 5 minutes old)
3. Raw body parsing (not parsed JSON — signature is over raw bytes)
4. Idempotency: deduplicate events using event ID
5. Async processing: immediately return 200, process in queue
6. Retry handling: idempotent handlers for safe retries
7. Error handling: return 4xx only if payload is invalid (causes retries)
8. Monitoring: alert on missing expected webhooks
9. Testing: replay webhooks from provider dashboard
10. Webhook signing secret rotation procedure
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
