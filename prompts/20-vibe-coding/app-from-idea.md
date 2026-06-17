---
title: "Turn an Idea into a Spec"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [planning, vibe-coding, spec, product]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Turn my app idea into a buildable spec.

Idea: [DESCRIBE YOUR IDEA — even rough is fine]

Let me refine this idea into a clear spec:

**1. Problem statement** (refined):
Who has this problem? How often? How bad?

**2. Solution** (one sentence):
[APP NAME] helps [WHO] to [DO WHAT] by [HOW].

**3. Core features** (MVP only — 3-5 max):
- Feature 1: [description]
- Feature 2: [description]
- Feature 3: [description]

**4. User flow**:
How does a new user go from landing page → registered → first value?

**5. Data model**:
Key entities and their relationships.

**6. Tech stack**:
What to build with (for speed + your skills).

**7. MVP timeline**:
Realistic estimate in days.

**8. What's out of scope** (important!):
What to build in v2, not now.

**9. First step**:
Exact first thing to code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
