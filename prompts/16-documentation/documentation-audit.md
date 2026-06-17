---
title: "Audit and Improve Existing Documentation"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [documentation, audit, improvement, quality]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Audit and improve my existing documentation.

Documentation to audit: [DESCRIBE YOUR DOCS / PASTE SAMPLE]
Complaints you've received: [DESCRIBE USER PAIN POINTS]

Audit dimensions:
1. **Accuracy**: is it still correct?
2. **Completeness**: are there obvious gaps?
3. **Discoverability**: can users find what they need?
4. **Clarity**: is it clear to the target audience?
5. **Examples**: are there enough concrete examples?
6. **Freshness**: when was it last updated?
7. **Structure**: logical flow and hierarchy?
8. **Search**: can users find via search?

For each piece of documentation:
9. Current state assessment
10. Specific improvements needed
11. Priority (critical/important/nice-to-have)

Improvements to make:
12. Add missing sections
13. Rewrite unclear explanations
14. Add code examples
15. Fix outdated information

Output: audit report + prioritized improvement list.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
