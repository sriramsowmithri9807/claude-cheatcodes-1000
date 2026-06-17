---
title: "Manage Secrets in Production"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [secrets, security, vault, aws-secrets-manager]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up secure secrets management for my production environment.

Secrets to manage: [LIST TYPES: DB passwords, API keys, JWT secrets, etc.]

Options:
**AWS Secrets Manager**:
1. Store secrets with automatic rotation
2. IAM policy: EC2/ECS can read specific secrets
3. SDK integration (Node.js, Python)
4. Rotation lambda for database passwords

**HashiCorp Vault**:
5. Dynamic secrets: Vault generates short-lived DB credentials
6. App role authentication
7. Kubernetes integration (vault-agent-injector)

**GitHub Actions**:
8. Environment secrets for CI/CD
9. OIDC federation: GitHub → AWS without long-lived keys

Never again:
- Hardcode secrets in code
- Store secrets in environment files committed to git
- Share secrets via Slack/email
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
