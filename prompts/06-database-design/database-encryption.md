---
title: "Implement Database Encryption"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [encryption, security, postgresql, compliance]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement encryption for sensitive data in my database.

Sensitive fields: [LIST: SSN, credit cards, health data, etc.]
Compliance: [HIPAA / PCI-DSS / GDPR]

Layers:
1. **Encryption at rest**: disk-level (transparent, OS/DB handles)
2. **Encryption in transit**: SSL/TLS for DB connections (verify, don't just encrypt)
3. **Column-level encryption**: pgcrypto for specific sensitive fields
4. **Application-level encryption**: encrypt before insert, decrypt on read
5. **Key management**: AWS KMS / HashiCorp Vault (don't store keys in DB)
6. **Searchable encryption**: how to search encrypted fields
7. **Tokenization**: replace sensitive data with non-sensitive token
8. **Data masking**: return masked value to non-privileged users

For each compliance framework: what is required vs nice-to-have.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
