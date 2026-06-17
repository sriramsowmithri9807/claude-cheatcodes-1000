---
title: "Clone an Existing App to Learn"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [clone, learning, vibe-coding, project]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Help me clone [APP NAME] to learn from it.

App to clone: [e.g., Twitter, Trello, Notion, Airbnb, etc.]
Purpose: [LEARNING / PORTFOLIO / STARTING POINT FOR MY IDEA]
Skill level: [DESCRIBE YOUR EXPERIENCE]

Cloning strategy:

1. **Scope**: which features to clone (not everything)
   - Core loop: the 2-3 features that define the app
   - Skip: social features, search, notifications (add later)

2. **Design**: don't copy — make it yours
   - Different color palette
   - Your name + branding
   - One twist: one feature your version has that theirs doesn't

3. **Tech stack**: choose for learning, not production scale
   - Next.js + Prisma + PostgreSQL + Tailwind
   - Auth: Clerk (2 lines of code)

4. **Build order**:
   - Data model first
   - Backend API second
   - UI third
   - Auth last (so auth doesn't block learning core features)

Output: feature list + data model + implementation plan for [APP].
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
