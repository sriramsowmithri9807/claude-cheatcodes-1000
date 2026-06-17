---
title: "Design API Before Implementation"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api-first, openapi, design, planning]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design my API before writing any implementation code.

Feature to design: [DESCRIBE FEATURE]
Consumers: [FRONTEND / MOBILE / THIRD-PARTY]

Step 1: Resource modeling
- What are the main resources?
- What are the relationships?
- What operations are needed per resource?

Step 2: OpenAPI spec
- Write the complete spec in OpenAPI 3.1
- Include request/response schemas
- Include error responses
- Include auth requirements

Step 3: Review questions
- Is this API easy to use?
- Does it follow REST conventions?
- Is it consistent with existing API?
- What might change in v2?

Output: complete OpenAPI 3.1 YAML + design decisions document.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
