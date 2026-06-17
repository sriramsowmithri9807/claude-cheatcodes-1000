---
title: "Design a Security Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, architecture, zero-trust, defense-in-depth]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive security architecture for my application.

Application type: [DESCRIBE]
Data sensitivity: [PUBLIC / SENSITIVE / HIGHLY CONFIDENTIAL]

Defense in depth layers:
1. **Network**: VPC, private subnets, security groups, WAF
2. **Edge**: Cloudflare WAF, DDoS protection, bot detection
3. **Authentication**: MFA, SSO, session management
4. **Authorization**: RBAC + ABAC, least privilege
5. **Application**: OWASP Top 10 mitigations, input validation
6. **Data**: encryption at rest, in transit, key management
7. **Secrets**: Vault or AWS Secrets Manager, rotation
8. **Audit logging**: immutable audit trail for sensitive operations
9. **Vulnerability management**: dependency scanning, SAST, DAST
10. **Incident response**: detection, containment, recovery playbook
11. **Compliance**: SOC2, ISO 27001, GDPR controls mapping

Threat model: identify top 5 threats and how each is mitigated.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
