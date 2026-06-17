---
title: "Run AI Models Locally"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [local-ai, ollama, llama, offline]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Run AI models locally for development and privacy.

Use case: [DESCRIBE: development, privacy-sensitive data, offline use, cost reduction]

Using: Ollama

1. **Installation**: `curl -fsSL https://ollama.ai/install.sh | sh`
2. **Pull models**: `ollama pull llama3.1:8b`, `ollama pull mistral`, `ollama pull codellama`
3. **Ollama API**: OpenAI-compatible REST API at localhost:11434
4. **Integration**: drop-in replacement for OpenAI SDK
5. **Model selection guide**: which model for which task
6. **GPU acceleration**: NVIDIA CUDA, Apple Metal (M1/M2)
7. **Context length**: manage smaller context windows
8. **Quantization**: Q4_K_M (smallest), Q8_0 (quality), F16 (full)
9. **Modelfile**: customize system prompt, temperature
10. **LM Studio**: GUI alternative to Ollama

Compare: local vs Claude API — when each makes sense.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
