---
title: "Implement Zero Trust Security"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [zero-trust, security, architecture, network]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement Zero Trust security architecture for my system.

Current setup: [DESCRIBE YOUR INFRASTRUCTURE]

**Zero Trust principles**:
1. **Never trust, always verify**: every request authenticated and authorized
2. **Least privilege**: minimal permissions for every identity
3. **Assume breach**: design for breach containment

**Implementation**:
4. **Identity**: strong MFA for all users and services
5. **Device trust**: verify device health before access
6. **Micro-segmentation**: network isolation, no implicit east-west trust
7. **Service mesh**: mTLS between all services (Istio)
8. **API gateway**: every API call authenticated
9. **Just-in-time access**: temporary elevated permissions
10. **Continuous verification**: re-auth on sensitive operations

**Monitoring**:
11. All access logged
12. Behavioral analytics: anomaly detection
13. Automated response: block suspicious activity

For my infrastructure: specific implementation plan.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
