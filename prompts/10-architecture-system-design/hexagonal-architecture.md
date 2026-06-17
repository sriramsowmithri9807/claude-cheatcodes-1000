---
title: "Implement Hexagonal Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [hexagonal, ports-adapters, architecture, clean]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement Hexagonal Architecture (Ports and Adapters) for my application.

Application: [DESCRIBE]

Structure:
```
src/
  core/              # Pure domain logic, no framework deps
    domain/
      entities/
      value-objects/
      services/
    ports/
      in/              # Driving ports (use cases)
      out/             # Driven ports (interfaces)
  adapters/
    in/
      http/            # REST API controllers
      graphql/         # GraphQL resolvers
      cli/             # CLI commands
    out/
      persistence/     # Database implementations
      messaging/       # Event bus
      external-api/    # Third-party services
```

Implement:
1. A complete use case end-to-end
2. Dependency injection setup
3. Testing without infrastructure (mock ports)
4. Adding a new adapter without changing core
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
