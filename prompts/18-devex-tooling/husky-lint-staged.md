---
title: "Set Up Pre-Commit Hooks"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [husky, lint-staged, git-hooks, quality]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Set up pre-commit hooks to enforce code quality.

Project: [DESCRIBE YOUR STACK]

1. **Install Husky**: `npx husky init`
2. **Install lint-staged**: `npm install --save-dev lint-staged`

3. **`.husky/pre-commit`**:
```bash
npx lint-staged
```

4. **`.husky/commit-msg`** (Conventional Commits):
```bash
npx --no -- commitlint --edit $1
```

5. **`lint-staged` config** in `package.json`:
```json
{
  'lint-staged': {
    '*.{ts,tsx}': ['eslint --fix', 'prettier --write'],
    '*.{css,scss}': ['stylelint --fix', 'prettier --write'],
    '*.{json,md}': ['prettier --write']
  }
}
```

6. **Commitlint**: enforce Conventional Commits format

7. **Pre-push hook**: run tests before push
```bash
npm test -- --passWithNoTests
```

8. **Bypass**: `git commit --no-verify` for emergencies (document when ok to use)

Output: complete hook setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
