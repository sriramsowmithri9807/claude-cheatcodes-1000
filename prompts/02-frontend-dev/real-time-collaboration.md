---
title: "Build Real-Time Collaboration Features"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [websockets, yjs, crdt, collaboration]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Add Google Docs-style real-time collaboration to my app.

Feature: [DESCRIBE: collaborative text editing / whiteboard / spreadsheet / other]

Using: Yjs (CRDT library) + y-websocket

Implement:
1. Yjs document setup with your data type (Y.Text, Y.Map, Y.Array)
2. WebSocket provider setup with y-websocket
3. Awareness (cursor positions, user presence)
4. Undo/redo with collaborative history
5. Offline support (sync when reconnected)
6. Conflict resolution (automatic with CRDTs)
7. UI: show collaborator cursors/selections
8. Persistence: store Yjs document in database

Include the server setup (Node.js y-websocket server).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
