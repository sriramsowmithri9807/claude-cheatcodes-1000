---
title: "Manage the Full API Lifecycle"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, lifecycle, devops, strategy]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Manage my API's full lifecycle from design to sunset.

My API: [DESCRIBE]

Phases:
1. **Design**: API-first — spec before code, review with stakeholders
2. **Mock**: generate mock server from spec for parallel dev
3. **Develop**: implement against spec, linting to verify conformance
4. **Test**: contract testing, integration tests, security scan
5. **Document**: auto-generate from spec + hand-written guides
6. **Release**: semantic versioning, changelog, consumer notification
7. **Monitor**: uptime, latency, error rates, usage analytics
8. **Iterate**: gather consumer feedback, add features without breaking
9. **Deprecate**: announce sunset, provide migration path
10. **Sunset**: remove old version, redirect to new

Tool recommendations for each phase.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
