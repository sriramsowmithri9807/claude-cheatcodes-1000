---
title: "Audit and Secure Dependencies"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [dependencies, security, supply-chain, npm]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Audit and secure my application's dependencies.

Package manager: [npm / yarn / pnpm / pip / go mod]

Vulnerability scanning:
1. `npm audit` — find known vulnerabilities
2. Snyk: `snyk test` — more comprehensive scan
3. GitHub Dependabot: automated PRs for security updates
4. OWASP Dependency-Check: for Java/Python

Fix strategy:
5. Critical: update immediately
6. High: update within 1 week
7. Medium: update within 1 month
8. Low: add to tech debt backlog

Prevention:
9. `npm audit` in CI — fail build on high+ severity
10. Renovate bot: auto-update minor/patch versions
11. Lock files: commit `package-lock.json`
12. Pin exact versions for security-critical packages

Supply chain:
13. Only use packages with active maintainers
14. Verify package signatures (npm provenance)
15. Prefer `--ignore-scripts` for untrusted packages

Output: audit results + remediation plan.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
