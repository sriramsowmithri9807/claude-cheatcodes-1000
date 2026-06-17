---
title: "Secure Your CI/CD Pipeline"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, ci-cd, supply-chain, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Harden my CI/CD pipeline against supply chain attacks.

Current pipeline: GitHub Actions

Threats:
1. Compromised dependencies (supply chain attack)
2. Stolen secrets from CI logs
3. Untrusted code in pull requests
4. Malicious GitHub Actions

Hardening:
1. **Pin action versions**: use SHA hash, not tags
2. **Minimal permissions**: `permissions: read-all` by default, grant write only where needed
3. **OIDC for cloud auth**: no long-lived AWS/GCP credentials
4. **Secret masking**: secrets never in logs
5. **Dependency lock files**: commit package-lock.json, poetry.lock
6. **Verify downloads**: checksum verification for any downloaded tools
7. **Code signing**: sign your container images (cosign)
8. **SBOM generation**: Software Bill of Materials on every build
9. **OpenSSF Scorecard**: measure and improve supply chain security
10. **Third-party action audit**: review all actions in use
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
