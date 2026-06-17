---
title: "Deprecate API Endpoints Gracefully"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, deprecation, versioning, lifecycle]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Plan and execute graceful deprecation of these API endpoints:

[LIST ENDPOINTS TO DEPRECATE AND THEIR REPLACEMENTS]

Deprecation process:
1. Add `Deprecation` and `Sunset` headers (RFC 8594)
2. Update docs with deprecation notice + migration guide
3. Log usage of deprecated endpoints (to track migration progress)
4. Email API consumers who have called the endpoint recently
5. Show deprecation warning in developer dashboard
6. Hard cutoff date announcement (3-6 months notice)
7. Grace period extension process for consumers who need more time
8. Traffic monitoring: graph call volume trending to zero
9. Actual removal + 410 Gone response
10. Post-mortem: how many consumers were impacted
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
