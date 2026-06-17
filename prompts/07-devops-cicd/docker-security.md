---
title: "Harden Docker Containers for Production"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [docker, security, containers, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Harden my Docker containers for production security.

Current Dockerfile: [PASTE OR DESCRIBE]

Security improvements:
1. **Non-root user**: run process as non-root inside container
2. **Read-only filesystem**: `--read-only`, writable mounts only where needed
3. **Minimal base image**: distroless or alpine (reduce attack surface)
4. **Multi-stage build**: no build tools in final image
5. **No secrets in image**: use runtime env vars or secrets manager
6. **Pinned versions**: specific tags, not `latest`
7. **Layer ordering**: cache dependencies layer separately from code
8. **Image scanning**: Trivy or Snyk in CI pipeline
9. **COPY vs ADD**: use COPY, never ADD
10. **HEALTHCHECK**: define health check in Dockerfile
11. **Capabilities**: drop all, add back only what's needed
12. `.dockerignore`: exclude .git, .env, node_modules
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
