---
title: "Build a gRPC Service"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [grpc, protobuf, nodejs, backend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a gRPC service for: [DESCRIPTION].

Define the proto file:
- Service definition with all RPCs
- Message types with proper field numbers
- Use: unary, server streaming, client streaming, bidirectional streaming where appropriate

Implement in Node.js (@grpc/grpc-js):
1. Server implementation
2. Client SDK (reusable wrapper)
3. Authentication via metadata
4. Interceptors for logging and error handling
5. Health checking (grpc-health-probe)
6. Reflection (for grpcui/grpcurl debugging)
7. Load balancing client-side
8. Proto-generated TypeScript types
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
