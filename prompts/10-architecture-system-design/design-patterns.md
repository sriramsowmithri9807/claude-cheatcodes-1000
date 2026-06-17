---
title: "Apply Gang of Four Design Patterns"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [design-patterns, gof, architecture, oop]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply relevant design patterns to my codebase.

Code/System: [DESCRIBE]
Problems to solve: [DESCRIBE WHAT'S AWKWARD OR HARD TO EXTEND]

Suggest and implement the right patterns:

**Creational**: Factory, Abstract Factory, Builder, Singleton, Prototype
**Structural**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
**Behavioral**: Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor

For each suggested pattern:
1. Which pattern to use here
2. Why it solves the problem
3. TypeScript/Python implementation
4. Before and after code comparison
5. When NOT to use this pattern (overengineering warning)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
