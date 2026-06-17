---
title: "Master Claude Tool Use (Function Calling)"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [tool-use, function-calling, claude, agents]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Master Claude's tool use (function calling) feature.

Tools to implement: [DESCRIBE WHAT TOOLS YOUR AGENT NEEDS]

1. **Tool definition**: name, description, input_schema (JSON Schema)
2. **Tool examples**:
   ```
   get_weather(city: string) → temperature, conditions
   search_database(query: string, table: string) → results
   send_email(to: string, subject: string, body: string) → success
   create_calendar_event(title, start, end, attendees) → event_id
   ```
3. **Parallel tool use**: Claude calls multiple tools simultaneously
4. **Tool error handling**: tool fails → inform Claude → it adapts
5. **Confirmation pattern**: ask user before executing irreversible tools
6. **Tool result formatting**: how to structure results for Claude
7. **Chain of tools**: multi-step tasks using multiple tools
8. **Safety**: validate tool inputs before executing
9. **Logging**: audit trail of every tool call
10. **Streaming with tool use**: handle streaming when tools are involved

Node.js SDK implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
