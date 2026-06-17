---
title: "Implement Data Encryption"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [encryption, security, crypto, data-protection]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement encryption for sensitive data in my application.

Sensitive data to encrypt: [LIST: PII, health data, financial, etc.]

**Encryption at rest**:
1. **Disk-level**: cloud provider disk encryption (baseline, not sufficient alone)
2. **Column-level**: encrypt specific sensitive DB columns
   - AES-256-GCM (authenticated encryption)
   - Node.js: `crypto.createCipheriv`
3. **Key management**: AWS KMS or HashiCorp Vault (NEVER store key with data)
4. **Key rotation**: rotate without re-encrypting everything (envelope encryption)

**Encryption in transit**:
5. TLS 1.3 for all external communication
6. TLS for internal service communication (mTLS)
7. Certificate pinning in mobile apps

**Specific implementations**:
8. Password hashing: bcrypt (cost=12) or argon2id
9. Tokenization: replace PAN/SSN with non-sensitive token
10. Searchable encryption: how to search encrypted fields

Output: encryption implementation for my specific data.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
