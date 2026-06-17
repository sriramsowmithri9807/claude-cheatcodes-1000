---
title: "Use Web Workers for Performance"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [web-workers, performance, javascript, concurrency]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Use Web Workers to move heavy computation off the main thread.

Heavy operations: [DESCRIBE: data processing, parsing, encryption, image manipulation]

1. **When to use Web Workers**:
   - JS > 50ms → user feels janky
   - Data processing, parsing large JSON
   - Image/video processing
   - Crypto operations
   - Compression/decompression

2. **Basic Worker setup**:
   ```javascript
   const worker = new Worker(new URL('./worker.ts', import.meta.url));
   worker.postMessage({ data });
   worker.onmessage = (e) => setResult(e.data);
   ```

3. **Comlink**: simplify worker communication
   - Call worker functions like async functions

4. **Transferable objects**: zero-copy for ArrayBuffers

5. **Worker thread pool**: reuse workers (don't create/destroy)

6. **React integration**: `useWorker` hook

7. **Vite/webpack**: import worker with `?worker` suffix

8. **Testing**: jsdom doesn't support workers → mock in tests

Output: Web Worker implementation for my heavy operation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
