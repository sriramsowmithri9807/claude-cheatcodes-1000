---
title: "Manage Environment Variables"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [environment, secrets, config, tooling]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Manage environment variables across development, staging, and production.

Project: [DESCRIBE]

**Local development**:
1. `.env` file: local secrets (git-ignored)
2. `.env.example`: template with fake values (committed)
3. `dotenv`: load .env automatically
4. Validation: check required vars on startup

**Multiple environments**:
5. `.env.local` > `.env.development` > `.env` (priority)
6. `.env.test` for test environment
7. Never commit `.env` with real values

**Validation with Zod**:
```typescript
const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  PORT: z.coerce.number().default(3000),
});
export const env = envSchema.parse(process.env);
```

**Production**:
8. Platform secrets: Vercel, Railway, EAS
9. Secrets manager: AWS Secrets Manager or Vault
10. Inject at deploy time, not stored in codebase

**CI/CD**:
11. GitHub Secrets for CI
12. Environment-specific secrets

Output: env validation schema + .env.example.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
