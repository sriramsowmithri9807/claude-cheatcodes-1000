---
title: "Build a WebSocket Server"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [websockets, nodejs, real-time, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a production WebSocket server for: [USE CASE — chat / notifications / live data].

Using: Node.js + ws library (or uWebSockets.js for max performance)

Implement:
- Connection management (track all connected clients)
- Authentication (validate JWT on upgrade request)
- Rooms/channels (subscribe to specific topics)
- Message protocol: define JSON message types
- Heartbeat (ping/pong to detect dead connections)
- Reconnection handling (client-side)
- Horizontal scaling with Redis pub/sub (sticky sessions or stateless)
- Rate limiting per connection
- Message history (last N messages on join)
- Graceful shutdown (drain connections)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
