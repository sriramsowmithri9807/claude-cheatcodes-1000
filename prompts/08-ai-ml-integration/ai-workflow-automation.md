---
title: "Build AI-Powered Workflow Automation"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [workflow, automation, claude, agents]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an AI-powered workflow automation system.

Workflows to automate: [DESCRIBE: data processing, content moderation, report generation, etc.]

1. **Workflow definition**: define steps, triggers, conditions
2. **Claude as orchestrator**: plan the workflow steps dynamically
3. **Tool integrations**: connect Claude to: database, APIs, email, Slack, calendar
4. **Human-in-the-loop**: pause for human review when confidence is low
5. **Error recovery**: Claude handles errors, tries alternative approaches
6. **State management**: persist workflow state across multiple Claude calls
7. **Parallel execution**: run independent workflow steps simultaneously
8. **Logging and observability**: trace every decision and action
9. **Approval gates**: require human approval for high-impact actions
10. **Testing**: replay recorded workflows to test changes

Node.js + LangChain or custom implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
