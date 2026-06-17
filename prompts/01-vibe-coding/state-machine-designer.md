---
title: "Design a State Machine for Any Feature"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [state-machine, xstate, logic, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
You are an expert in finite state machines. I need a state machine for: [FEATURE DESCRIPTION].

Design:
1. All possible states (draw as an ASCII diagram)
2. All transitions and the events that trigger them
3. Guard conditions for conditional transitions
4. Entry/exit actions for each state
5. Implementation using XState v5 (TypeScript)
6. React integration with `useMachine` hook
7. Unit tests for each state transition

Make the state machine impossible to get into an invalid state.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
