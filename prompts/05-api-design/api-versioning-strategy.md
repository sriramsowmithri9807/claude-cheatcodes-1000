---
title: "API Versioning Strategy"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, versioning, rest, strategy]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Define a complete API versioning strategy for my product:

Current API users: [DESCRIBE YOUR CONSUMERS]
Breaking change planned: [DESCRIBE WHAT'S CHANGING]

Cover:
1. URL vs header vs query param — evaluate tradeoffs for my case
2. SemVer for APIs: what constitutes major/minor/patch
3. Backward compatibility rules (what is and isn't a breaking change)
4. Deprecation process: sunset headers, docs notice, timeline
5. Migration guide format for consumers
6. Running multiple versions simultaneously
7. Sunset monitoring: detect when old version traffic → 0
8. Client SDK versioning strategy

Output: versioning policy document + implementation code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
