---
title: "Design a Streaming API"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [streaming, api, sse, ndjson]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a streaming API for: [USE CASE — AI responses / data export / live events].

Options to evaluate:
1. **Server-Sent Events**: unidirectional, browser-native, auto-reconnect
2. **WebSocket**: bidirectional, lower overhead
3. **gRPC streaming**: binary, typed, low latency
4. **NDJSON over HTTP**: newline-delimited JSON, simple
5. **HTTP chunked transfer**: progressive loading

For MY use case, implement:
- Server implementation
- Client (browser + Node.js) SDK
- Backpressure handling
- Error recovery
- Authentication
- Progress reporting
- Cancellation

With concrete code examples for each layer.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
