---
title: "Write a Production Incident Postmortem"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [postmortem, devops, reliability, documentation]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
You are an SRE writing a blameless postmortem. Here are the incident details:

[PASTE: incident timeline, affected systems, errors, metrics]

Write a professional postmortem including:
1. **Incident summary** (1 paragraph, suitable for stakeholders)
2. **Timeline** (minute-by-minute from detection to resolution)
3. **Root cause** (5 Whys analysis)
4. **Contributing factors** (not blame — systemic issues)
5. **Impact** (users affected, duration, data loss if any)
6. **Resolution steps** taken
7. **Action items** to prevent recurrence (with owners and due dates)
8. **Lessons learned**

Blameless tone throughout.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
