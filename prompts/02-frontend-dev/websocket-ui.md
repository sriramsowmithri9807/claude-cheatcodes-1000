---
title: "Build a WebSocket-Powered Real-Time UI"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [websockets, react, real-time, ui]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a real-time dashboard UI using WebSockets.

Data to display in real-time: [DESCRIBE YOUR DATA: stock prices / server metrics / chat messages / etc.]

React implementation:
1. `useWebSocket` custom hook with reconnection logic
2. Connection status indicator (connecting/connected/disconnected)
3. Message queue for messages received while UI is updating
4. Throttle incoming messages (max 60fps updates)
5. Optimistic local updates
6. Reconnect with exponential backoff
7. Heartbeat/ping-pong keepalive

UI components: animated number counters, live charts, real-time feed.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
