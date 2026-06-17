---
title: "Add Real-Time Features to Any App"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [websockets, socket-io, real-time, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add real-time features to my [TYPE] app.

Features to add:
- [FEATURE 1: e.g., live chat]
- [FEATURE 2: e.g., real-time notifications]
- [FEATURE 3: e.g., collaborative editing indicator]

Implement using Socket.IO + Node.js:
1. Server setup with rooms and namespaces
2. Client SDK (React hook: `useSocket`)
3. Reconnection handling
4. Presence system (who's online)
5. Optimistic updates on the client
6. Scaling notes for when you need multiple servers (Redis adapter)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
