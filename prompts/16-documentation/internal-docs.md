---
title: "Set Up Internal Documentation System"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [documentation, confluence, notion, wiki]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up an internal documentation system for my engineering team.

Team size: [N engineers]
Current state: [DESCRIBE: no docs / scattered docs / outdated docs]

Documentation system design:
1. **Tool selection**: Notion / Confluence / GitBook / docs-as-code (MDX)
   - Recommendation based on team size and existing tools
2. **Information architecture**: how to organize content
3. **Templates**: one template per document type
4. **Ownership**: every document has an owner
5. **Review cycle**: quarterly review → mark as stale or update

Essential docs to create first:
6. **Onboarding guide**: new engineer day 1-30
7. **Development setup**: how to run everything locally
8. **Architecture overview**: what we've built and why
9. **Runbooks**: common operational procedures
10. **On-call guide**: what to do when paged
11. **Decision log**: major technical decisions and rationale
12. **Team processes**: how we work (standups, PRs, deployments)

Output: documentation system setup guide.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
