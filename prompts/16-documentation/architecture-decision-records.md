---
title: "Write Architecture Decision Records"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [adr, architecture, documentation, decisions]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write Architecture Decision Records (ADRs) for my team.

Decisions to document: [LIST KEY TECHNICAL DECISIONS YOUR TEAM HAS MADE]

ADR format (Nygard style):
```markdown
# ADR-001: Use PostgreSQL as the Primary Database

Status: Accepted
Date: 2024-01-15
Deciders: Engineering team

## Context
[What is the issue that motivates this decision?]

## Decision Drivers
* [Driver 1]
* [Driver 2]

## Considered Options
* [Option A]
* [Option B]

## Decision Outcome
Chosen option: [OPTION]

Because: [JUSTIFICATION]

## Consequences
* Good: [POSITIVE OUTCOMES]
* Bad: [TRADEOFFS AND RISKS]

## Options Comparison
| Criteria | Option A | Option B |
```

Write ADRs for my decisions covering:
1. Database choice
2. API style (REST vs GraphQL)
3. Authentication method
4. Deployment platform
5. Testing strategy
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
