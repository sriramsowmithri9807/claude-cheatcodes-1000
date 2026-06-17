---
title: "Build an Internal Developer Platform"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [idp, platform, devops, developer-experience]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design an Internal Developer Platform (IDP) for my engineering team.

Team size: [N engineers]
Current pain points: [DESCRIBE: long deploy times, environment parity, etc.]

Platform components:
1. **Self-service infrastructure**: create environments with one command
2. **Backstage**: service catalog, documentation, runbooks
3. **Golden paths**: opinionated templates for new services
4. **Secrets management**: self-service secret storage
5. **Observability portal**: logs, metrics, traces in one place
6. **Deployment portal**: see deploy status, trigger deploys, roll back
7. **Cost portal**: per-team cloud spend visibility
8. **Runbook automation**: common operations as self-service buttons
9. **DORA metrics dashboard**: track engineering effectiveness
10. **On-call scheduler**: PagerDuty integration, fair rotation

Start small: what to build in week 1 vs month 6.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
