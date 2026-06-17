---
title: "Implement GDPR Compliance"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [gdpr, privacy, compliance, data]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement GDPR compliance for my application.

App: [DESCRIBE]
Data processed: [LIST PERSONAL DATA TYPES]

**User rights implementation**:
1. **Right to access**: endpoint to export all user data as JSON/CSV
2. **Right to erasure**: delete account → delete all PII (or anonymize)
3. **Right to portability**: machine-readable format
4. **Right to rectification**: update any personal data
5. **Right to object**: opt out of marketing, profiling

**Consent**:
6. Cookie consent banner (necessary vs analytics vs marketing)
7. Granular consent per purpose
8. Store consent with timestamp and version
9. Easy withdrawal of consent

**Data protection**:
10. Data minimization: collect only what you need
11. Retention policy: auto-delete after X months
12. Third-party processor agreements (DPA)
13. Breach notification: 72-hour window to DPA
14. DPO: designate if required

Output: GDPR compliance checklist + implementation code for user rights.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
