---
title: "Implement Server-Sent Events (SSE)"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sse, streaming, real-time, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement Server-Sent Events (SSE) for real-time one-way streaming.

Use case: [DESCRIBE: live notifications / log streaming / AI response streaming / dashboard updates]

Backend (Express.js):
1. SSE endpoint with proper headers (Content-Type: text/event-stream)
2. Event types: named events, data, id, retry
3. Heartbeat to keep connection alive (comment every 30s)
4. Authentication (validate token before streaming)
5. Client disconnect detection and cleanup
6. Broadcasting to multiple clients

Frontend (React):
1. `useEventSource` hook with reconnection
2. Handle multiple event types
3. Connection status indicator

Compare with WebSockets: when SSE is the better choice.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
