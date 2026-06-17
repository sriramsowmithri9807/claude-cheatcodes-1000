---
title: "Test Infrastructure as Code"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [terraform, testing, inspec, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write tests for my Terraform infrastructure code.

Infrastructure: [DESCRIBE YOUR TERRAFORM RESOURCES]

Testing layers:
1. **Static analysis**: `terraform validate` + `tflint` + `checkov` (security)
2. **Unit tests**: `Terratest` — deploy to real AWS sandbox, verify resources
3. **Policy tests**: OPA (Open Policy Agent) policies for compliance
4. **Drift detection**: `terraform plan` output — alert if diff exists in prod
5. **Integration**: real infrastructure test with smoke tests
6. **Destruction test**: verify `terraform destroy` cleans up cleanly

CI pipeline:
7. On PR: static analysis + security scan
8. On merge to main: deploy to staging + integration tests
9. On tag: deploy to production with manual approval

Output: Terratest Go test file + GitHub Actions workflow.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
