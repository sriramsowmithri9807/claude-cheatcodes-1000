---
title: "Design a Webhook Delivery System"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [webhooks, api, events, reliability]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design and implement a production webhook system.

My service sends events when: [LIST YOUR EVENTS]

Consumers register endpoints to receive these events.

Implement:
1. Webhook registration API (URL, events to subscribe, secret)
2. Signature generation: HMAC-SHA256 of payload + timestamp
3. Delivery: HTTP POST to consumer endpoint
4. Retry: exponential backoff (1s, 5s, 30s, 5min, 30min, 2h, 12h, 24h)
5. Dead letter: mark webhook as failed after all retries
6. Delivery log: per-webhook history (status, response, attempts)
7. Dashboard: consumer can view delivery log, replay events
8. Verification guide: how consumers should verify signatures
9. Event catalog: document every event type with example payload
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
