---
title: "Implement GraphQL Subscriptions"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [graphql, subscriptions, websockets, real-time]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement GraphQL subscriptions for real-time features.

Real-time features needed: [DESCRIBE]

Using: Apollo Server + graphql-ws

1. Subscription schema definition
2. PubSub setup (in-memory for single server, Redis for multiple)
3. Resolver: publish events + subscribe to topics
4. Authentication: verify JWT on WebSocket connection
5. Authorization: filter subscription events per user
6. Connection lifecycle: onConnect, onSubscribe, onDisconnect
7. Error handling: close connection on auth failure
8. Reconnection: client auto-reconnects with same subscription
9. Scaling: Redis PubSub adapter for horizontal scaling
10. Testing: subscription tests with graphql-ws client

Client implementation: React hook with Apollo Client.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
