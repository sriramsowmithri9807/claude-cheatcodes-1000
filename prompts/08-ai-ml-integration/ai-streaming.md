---
title: "Stream AI Responses in Real-Time"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [streaming, claude, ux, real-time]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement real-time streaming of Claude responses for great UX.

UI framework: [React / Next.js / Vue]

Backend (Node.js):
1. Claude streaming API: `stream: true`
2. Event types: `message_start`, `content_block_delta`, `message_stop`
3. SSE endpoint: forward Claude stream to frontend
4. Error handling mid-stream
5. Abort: cancel stream when user clicks stop button

Frontend (React):
6. Fetch with ReadableStream
7. Append tokens to state as they arrive
8. Show typing indicator while waiting for first token
9. Auto-scroll to bottom
10. Stop button: abort fetch, stop stream

Edge deployment:
11. Vercel Edge Functions for minimal latency
12. OpenAI-compatible streaming format for compatibility

Full implementation with beautiful streaming chat UI.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
