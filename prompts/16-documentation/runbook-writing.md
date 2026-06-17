---
title: "Write Operations Runbooks"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [runbooks, documentation, operations, sre]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write operations runbooks for common tasks.

Service: [DESCRIBE YOUR SERVICE]
Runbooks needed: [LIST COMMON OPERATIONAL TASKS]

Runbook template:

**Title**: [Action-oriented: 'Restart the API server']
**Audience**: On-call engineer
**Time required**: [ESTIMATE]
**Risk level**: Low/Medium/High

**Context**: Why would you need to run this?

**Prerequisites**:
- Access to [SYSTEM]
- [OTHER REQUIREMENTS]

**Steps**:
1. [Specific command or action]
   `$ command here`
   Expected output: [WHAT SUCCESS LOOKS LIKE]

**Verification**: How to confirm success

**Rollback**: How to undo this if needed

**Escalation**: When to escalate and to whom

**Last updated**: [DATE] by [NAME]

Write runbooks for:
1. Restart a service
2. Scale up/down
3. Roll back a deployment
4. Database failover
5. Clear a stuck job queue
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
