---
title: "Build AI Agents with Claude"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [agents, tools, claude, ai]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an AI agent system using Claude with tool use.

Agent purpose: [DESCRIBE: research agent, coding agent, data analysis agent, customer service]

Implement:
1. **Tool definition**: define tools as JSON schema (Claude understands these)
2. **Tool examples**:
   - `search_web(query)` → results
   - `execute_code(code)` → output
   - `read_file(path)` → content
   - `query_database(sql)` → results
3. **Agentic loop**: Claude → tool call → result → Claude → ... → final answer
4. **Multi-agent**: orchestrator agent + specialist sub-agents
5. **Memory**: short-term (conversation), long-term (vector DB)
6. **Error handling**: tool failures, retries, fallbacks
7. **Safety guardrails**: what agents are NOT allowed to do
8. **Observation and logging**: trace every action for debugging

Node.js implementation with the Anthropic SDK.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
