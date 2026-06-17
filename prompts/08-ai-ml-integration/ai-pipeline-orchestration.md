---
title: "Orchestrate AI Pipelines"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [orchestration, pipelines, claude, agents]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a complex AI pipeline that chains multiple Claude calls.

Pipeline goal: [DESCRIBE YOUR MULTI-STEP AI WORKFLOW]

1. **Pipeline definition**: graph of steps with dependencies
2. **Step types**: transform, classify, generate, validate, branch
3. **Data flow**: output of step N → input of step N+1
4. **Parallelism**: run independent steps in parallel
5. **Branching**: different paths based on step output
6. **Validation gates**: validate output before passing to next step
7. **Retry logic**: retry failed steps with different approach
8. **State persistence**: save pipeline state (can resume if interrupted)
9. **Cost tracking**: track tokens per step
10. **Visualization**: diagram of pipeline execution
11. **Testing**: unit test each step independently
12. **Monitoring**: latency and success rate per step

Node.js implementation with a DAG executor.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
