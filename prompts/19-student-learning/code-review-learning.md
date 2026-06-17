---
title: "Learn to Do Code Reviews"
category: student-learning
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [code-review, learning, team, quality]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Teach me how to do effective code reviews.

Context: [NEW TO REVIEWING / RECEIVING BAD REVIEWS / WANT TO IMPROVE]

**What code review is for**:
1. Find bugs before production
2. Knowledge sharing across the team
3. Maintain code quality and consistency
4. NOT: gatekeeping, showing off, nitpicking

**What to look for**:
5. **Correctness**: does it do what it says?
6. **Security**: any obvious vulnerabilities?
7. **Performance**: O(n²) where O(n) would work?
8. **Readability**: clear naming, not too complex?
9. **Tests**: are edge cases covered?
10. **Design**: is this the right approach?

**How to give feedback**:
11. Ask questions instead of making demands
12. Explain WHY, not just WHAT to change
13. Distinguish critical from optional ('nit:')
14. Approve when good enough (not perfect)

**How to receive feedback**:
15. Don't take it personally — it's about the code
16. Ask for clarification if unclear
17. Respond to every comment

Output: code review guidelines + practice on [SAMPLE CODE].
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
