---
title: "Implement Clean Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [clean-architecture, solid, architecture, layers]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement Clean Architecture for my application.

Application type: [DESCRIBE]

Layers (inner → outer, dependencies point inward):

1. **Entities**: business objects, no framework deps
2. **Use Cases**: application-specific business rules
3. **Interface Adapters**: controllers, presenters, gateways
4. **Frameworks & Drivers**: web, DB, UI

Implement:
- Folder structure with layer separation
- Dependency rule: nothing in inner circle knows about outer
- Dependency injection at the edges
- Repository pattern for data access
- Use case per feature
- Controller → Use Case → Entity → Repository

Example: implement user registration end-to-end
- Entity: User with validation
- Use Case: RegisterUser
- Repository interface + PostgreSQL implementation
- HTTP Controller
- Dependency injection wiring
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
