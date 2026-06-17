---
title: "Critique and Improve an Existing REST API"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rest, api, critique, refactoring]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Review and critique this REST API design:

[PASTE YOUR API ROUTES AND SCHEMAS]

Analyze:
1. URL design issues (verbs in URLs, inconsistent naming)
2. HTTP method misuse (GET with side effects, POST for everything)
3. Status code problems (200 for errors, 500 for everything)
4. Response shape inconsistencies
5. Missing pagination, filtering, sorting
6. Auth vulnerabilities
7. Missing error details
8. Performance issues (no caching headers, N+1 in related data)
9. Breaking change risks in current design
10. Security gaps

For each issue: severity (critical/major/minor), explanation, and the fix.
Output: improved API spec.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
