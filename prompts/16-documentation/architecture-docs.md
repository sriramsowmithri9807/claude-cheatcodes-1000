---
title: "Document System Architecture"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [architecture, documentation, diagrams, adr]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Document my system architecture.

System: [DESCRIBE YOUR SYSTEM]

1. **Architecture overview**: high-level description in plain English
2. **Diagram**: C4 model diagram (Context → Container → Component)
   - Context: how your system fits in the world
   - Container: main deployable units
   - Component: major components within each container
3. **Technology choices**: what and why for key decisions
4. **Data flow**: how data moves through the system
5. **Security architecture**: auth, network, data protection overview
6. **Scaling strategy**: how it handles growth
7. **Failure modes**: what happens when X fails
8. **External dependencies**: third-party services and their criticality

ADRs (Architecture Decision Records):
9. One ADR per significant decision
10. Format: Status, Context, Decision, Consequences

Output: architecture document + 3 example ADRs.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
