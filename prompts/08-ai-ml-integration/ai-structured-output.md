---
title: "Get Reliable Structured Output from Claude"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [structured-output, json, validation, claude]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Get reliable structured JSON output from Claude every time.

Data structure needed: [DESCRIBE YOUR TARGET JSON SCHEMA]

Techniques (from fragile to reliable):

1. **Basic**: ask for JSON in the prompt
2. **Schema in prompt**: include your JSON schema with descriptions
3. **Few-shot examples**: show 2-3 examples of correct JSON output
4. **XML wrapping**: ask Claude to wrap JSON in `<json>` tags (parse easily)
5. **Validation + retry**: if Zod validation fails, send error back to Claude
6. **Format reminder**: end prompt with "Remember: respond ONLY with valid JSON"
7. **Temperature 0**: for consistency in structured tasks
8. **Output type in system prompt**: tell Claude its output type from the start
9. **Anthropic beta JSON mode**: if available, use tool_use with defined schema
10. **Post-processing**: fix common JSON mistakes (trailing commas, unquoted keys)

Reusable TypeScript function for each approach.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
