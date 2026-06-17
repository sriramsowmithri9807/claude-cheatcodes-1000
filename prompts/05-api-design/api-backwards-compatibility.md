---
title: "Maintain API Backwards Compatibility"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, compatibility, versioning, design]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Define rules for maintaining backwards compatibility in my API.

Current consumers: [DESCRIBE]

Non-breaking changes (safe to ship):
1. Add new optional fields to responses
2. Add new optional request fields
3. Add new endpoints
4. Add new enum values (caution)
5. Increase rate limits

Breaking changes (require versioning or careful migration):
6. Remove/rename fields
7. Change field types
8. Change auth requirements
9. Change response codes
10. Make optional fields required

For each potential breaking change in my API:
- Is it actually breaking?
- If yes: expand-contract migration pattern
- Testing: contract tests to detect regressions

Output: compatibility policy + API change checklist.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
