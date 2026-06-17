---
title: "Configure Log Retention and Compliance"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [logging, compliance, retention, gdpr]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Configure log retention and management for compliance.

Compliance: [GDPR / HIPAA / SOC2 / none — just best practices]

Log types and retention:
1. Application logs: 90 days hot, 1 year cold storage
2. Access logs: 1 year (security audit trail)
3. Error logs: 1 year with alerting
4. Security events: 2 years
5. Business events: indefinite (anonymized after 1 year)

Implement:
6. Structured logging (JSON, no PII in log messages)
7. Log levels: control verbosity per environment
8. Automatic PII detection and redaction
9. Centralized storage: S3 with lifecycle to Glacier
10. Access controls: who can query logs (SOC2 requirement)
11. Audit log: log who accessed the logs
12. GDPR: ability to delete a user's logs on request
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
