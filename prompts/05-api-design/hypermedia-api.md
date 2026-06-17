---
title: "Build a Hypermedia (HATEOAS) API"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [hateoas, rest, hypermedia, api]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement HATEOAS for my REST API to make it truly discoverable.

Resources: [LIST YOUR MAIN RESOURCES]

Implement:
1. `_links` in every response (self, related resources, actions)
2. Link relations using IANA-registered names (collection, item, edit, etc.)
3. `_actions` for available operations on this resource based on current state
4. Embedded resources (avoid extra round trips)
5. API root: GET / returns all available resources
6. HAL (Hypertext Application Language) format
7. Link templates (RFC 6570) for parameterized links
8. Siren or JSON:API as alternatives — compare

Example: Order resource with links to: payment, shipment, cancel (only if cancellable), invoice.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
