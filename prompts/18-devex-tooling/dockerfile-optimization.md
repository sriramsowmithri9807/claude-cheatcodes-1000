---
title: "Optimize Dockerfiles"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [docker, optimization, build-time, image-size]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my Dockerfiles for build time and image size.

Current Dockerfile: [PASTE YOUR DOCKERFILE]
Current image size: [SIZE]
Current build time: [TIME]

Optimization techniques:
1. **Multi-stage build**: separate build stage from runtime stage
2. **Layer ordering**: COPY package files → install → COPY code
   (dependencies change less often than code)
3. **Minimize layers**: combine RUN commands with &&
4. **Minimal base image**: node:20-alpine instead of node:20
5. **Distroless**: no shell, no package manager, smallest attack surface
6. **Cache mount**: `--mount=type=cache,target=/root/.npm`
7. **.dockerignore**: exclude node_modules, .git, .env, test files
8. **Non-root user**: `USER node` before CMD
9. **Specific versions**: pin base image version
10. **HEALTHCHECK**: define health check

Before/after comparison:
- Image size reduction target: 50%+
- Build time reduction: explain caching strategy

Output: optimized Dockerfile.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
