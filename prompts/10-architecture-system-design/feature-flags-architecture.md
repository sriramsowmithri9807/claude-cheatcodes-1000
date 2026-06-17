---
title: "Design Feature Flag System Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [feature-flags, architecture, gradual-rollout, experimentation]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a feature flag system for my engineering team.

Team size: [N], services: [N]

Requirements:
- Toggle features without deployment
- Gradual rollout (1% → 10% → 100%)
- User/segment targeting
- A/B testing experiments
- Kill switch for emergencies

Architecture:
1. **Flag store**: database schema for flags + rules
2. **Evaluation engine**: rules engine (user in segment? rollout %?)
3. **SDK**: client library (JavaScript + Python) with local caching
4. **Admin UI**: create/edit flags, set rollout %
5. **Streaming updates**: SSE/WebSocket to push flag changes
6. **Analytics**: track exposure and conversion per variant
7. **Audit log**: who changed what flag and when
8. **Emergency mode**: fast disable all flags if eval service fails

Build vs buy: LaunchDarkly vs Unleash vs custom.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
