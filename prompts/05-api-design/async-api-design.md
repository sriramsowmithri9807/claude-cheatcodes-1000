---
title: "Design Asynchronous API Operations"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [async, api, webhooks, polling]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design async operation handling for my API.

Operations that are slow (> 5 seconds): [LIST]

Pattern 1 — Polling:
1. POST /export → 202 Accepted + `{job_id, status_url}`
2. GET /jobs/{id} → {status: pending|processing|done|failed, result_url}
3. Client polls with exponential backoff
4. Result available for 24h then deleted

Pattern 2 — Webhooks:
5. Client registers webhook URL
6. On completion: POST to webhook with result

Pattern 3 — WebSocket / SSE:
7. Connect before starting job
8. Receive real-time progress events

For MY specific operations: which pattern to use and why.
Implementation for each.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
