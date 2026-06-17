---
title: "Configure Prettier for Consistent Formatting"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [prettier, formatting, code-style, tooling]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Configure Prettier for consistent code formatting.

Project: [DESCRIBE]

1. **Installation**: `npm install --save-dev prettier`
2. **Config file** (`.prettierrc.json`):
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "all",
  "printWidth": 100,
  "bracketSpacing": true,
  "arrowParens": "always",
  "endOfLine": "lf"
}
```

3. **`.prettierignore`**: exclude generated files, build output
4. **Editor integration**: VS Code settings to format on save
5. **ESLint integration**: `eslint-config-prettier` (disable conflicting rules)
6. **Pre-commit hook**: `lint-staged` + `husky` → format on commit
7. **CI check**: `prettier --check .` fails if not formatted
8. **Format all files**: `prettier --write .` to format existing codebase
9. **Plugins**: Prettier plugin for Tailwind, JSON, MDX
10. **Opinionated decision**: stop bikeshedding formatting forever
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
