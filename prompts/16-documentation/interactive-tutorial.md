---
title: "Design an Interactive Tutorial"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [tutorial, learning, education, ux]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design an interactive tutorial for my product or technology.

Learning goal: [WHAT SHOULD THE USER BE ABLE TO DO AFTER COMPLETING]
Technology: [DESCRIBE WHAT YOU'RE TEACHING]

Interactive tutorial design:
1. **Learning objectives**: specific, measurable goals
2. **Prerequisites**: what users need before starting
3. **Chapters**: 5-8 progressive chapters
4. **Each chapter**:
   - Concept explanation (minimal text)
   - Interactive example (user runs code or clicks through UI)
   - Challenge: user applies the concept
   - Feedback: immediate, specific feedback
5. **Progression**: each chapter builds on the last
6. **Aha moments**: design for 1 aha moment per chapter
7. **Completion certificate**: gamification element

Format options:
8. **In-browser coding**: like freeCodeCamp, Codecademy
9. **Guided tour**: Shepherd.js overlay on real app
10. **Sandbox environment**: live environment to experiment

Output: complete chapter outline + Chapter 1 design.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
