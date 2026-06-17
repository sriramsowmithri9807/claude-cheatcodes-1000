---
title: "Build a Rapid Prototype"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [prototype, vibe-coding, validation, mvp]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Help me build a rapid prototype to validate my idea.

Idea: [DESCRIBE WHAT YOU WANT TO TEST]
Hypothesis: [WHAT ASSUMPTION ARE YOU TESTING]
Users to test with: [WHO WILL YOU SHOW THIS TO]

Prototype approach:

**Decide**: code prototype vs design prototype
- If testing if people WANT it: Figma or even paper
- If testing if it WORKS: code prototype

**For a code prototype**:
1. Hardcode everything: no database, no auth
2. One happy path only (no error handling)
3. Static data is fine (JSON file, no API)
4. Ugly is ok: validate the idea, not the design

**Speed techniques**:
5. Use shadcn/ui for instant beautiful components
6. v0.dev to generate UI from description
7. Supabase for instant auth + database
8. Vercel for instant deployment

**Validate**:
9. Show to 5 target users
10. Watch them use it (don't explain)
11. Ask: would you pay for this? How much?
12. Decide: build it or kill it

Output: minimal prototype code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
