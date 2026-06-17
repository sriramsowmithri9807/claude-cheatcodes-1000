---
title: "Secure Your AI Application"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, ai, prompt-injection, claude]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Secure my AI application against prompt injection and abuse.

App: [DESCRIBE YOUR AI FEATURE]

Threats:
1. **Prompt injection**: user input overrides system prompt
   - Defense: XML tags around user input, clear delimiters
   - Defense: validate Claude's output before acting on it
2. **Jailbreaking**: bypass safety guidelines
   - Defense: Claude's built-in safety is strong, add extra layer
3. **Data exfiltration**: get Claude to reveal system prompt or training data
   - Defense: never put secrets in system prompt
4. **Resource exhaustion**: max_tokens abuse
   - Defense: output length limits per user tier
5. **Content policy violations**: generate harmful content
   - Defense: output scanning before displaying
6. **Cost attacks**: trigger expensive requests
   - Defense: rate limiting, cost per user limit
7. **Indirect injection**: malicious content in RAG documents injected into prompt
   - Defense: sanitize retrieved content

Implement all defenses in code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
