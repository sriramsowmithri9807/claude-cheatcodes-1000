---
title: "Track Code Quality Metrics"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [code-quality, metrics, sonarqube, tooling]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Track and improve code quality metrics.

Project: [DESCRIBE]

**Metrics to track**:
1. **Test coverage**: line, branch, function coverage
2. **Cyclomatic complexity**: cognitive load of functions
3. **Code duplication**: DRY violations
4. **Technical debt**: estimated fix time
5. **Dependency vulnerabilities**: known CVEs
6. **Bundle size**: JS bundle weight over time
7. **TypeScript strictness**: any usage, untyped imports

**Tools**:
8. **SonarQube** (self-hosted) / **SonarCloud** (cloud):
   - Connect to GitHub
   - Gate: block PRs below quality threshold
9. **CodeClimate**: maintainability grade
10. **Codecov**: coverage reports with PR comments

**Local tools**:
11. `complexity-report`: cyclomatic complexity
12. `jscpd`: copy-paste detection
13. `ts-prune`: find unused TypeScript exports
14. `depcheck`: find unused dependencies

GitHub Actions integration:
15. PR comment with quality summary
16. Fail PR on threshold breach

Output: complete quality pipeline setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
