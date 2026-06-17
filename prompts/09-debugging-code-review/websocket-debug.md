---
title: "Debug WebSocket Connection Issues"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [websockets, debugging, real-time, network]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Debug WebSocket connection issues.

Setup: [Socket.io / native WebSocket / ws library]
Client: [Browser / React Native / Node.js]
Problem: [DESCRIBE: can't connect, disconnects randomly, messages not received, duplicate messages]

Debugging steps:
1. Open browser DevTools → Network tab → WS filter → inspect frames
2. Server logs: are connections being established?
3. CORS: for Socket.io, is the origin allowed?
4. Proxy: if behind nginx/load balancer, are Upgrade headers passed?
5. Reconnection: client should auto-reconnect — is it?
6. Event name mismatch: server emits 'foo', client listens to 'bar'
7. Room handling: is the user in the right room?
8. Authentication: is the handshake auth token valid?

Fix for my specific issue.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
