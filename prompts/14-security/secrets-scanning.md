---
title: "Prevent Secrets in Source Code"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [secrets, security, git, scanning]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Prevent and detect secrets committed to source code.

**Prevention** (pre-commit):
1. `git-secrets`: detect AWS keys, passwords before commit
2. `detect-secrets`: Yelp's pre-commit hook
3. `trufflehog`: scan git history for secrets
4. Pre-commit hook: `.husky/pre-commit` → run detection

**Detection in existing repo**:
5. `gitleaks`: scan entire git history
6. `trufflehog git`: entropy-based secret detection
7. GitHub Advanced Security: automatic secret scanning

**Remediation when secrets are found**:
8. Rotate the secret IMMEDIATELY (before fixing code)
9. Remove from git history: `git filter-repo --invert-paths --path secrets.txt`
10. Force push (coordinate with team)
11. Add `.gitignore` entry
12. Use environment variables instead

**Process**:
- `.env.example` with placeholder values (never real values)
- All secrets via environment variables
- Secrets manager for production

Output: pre-commit hook setup + scan report.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
