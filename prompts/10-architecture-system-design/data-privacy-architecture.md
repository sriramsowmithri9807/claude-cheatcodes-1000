---
title: "Design a Privacy-First Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [privacy, gdpr, architecture, security]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a privacy-first architecture compliant with GDPR and CCPA.

Application: [DESCRIBE YOUR APP AND DATA]

1. **Data inventory**: catalog all personal data collected
2. **Data minimization**: collect only what's needed
3. **Consent management**: granular consent, stored and auditable
4. **Data access layer**: all PII access goes through one service (log it)
5. **Encryption**: PII encrypted at rest (column-level with key rotation)
6. **Anonymization**: aggregate reporting uses anonymized data
7. **Right to erasure**: delete user → cascade delete all personal data
8. **Right to access**: export all user data as JSON/CSV
9. **Data retention**: auto-delete data after [N] months
10. **Breach detection**: alert on unusual bulk data access
11. **Third parties**: data sharing agreements, limited to necessary
12. **DPO tools**: privacy impact assessment, audit logs

Output: architecture diagram + data flow with privacy controls.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
