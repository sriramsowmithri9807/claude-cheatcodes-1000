---
title: "Scaffold a CLI Tool"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cli, node, typescript, tooling]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a Node.js CLI tool called `[TOOL-NAME]` that does: [DESCRIPTION].

Implement:
- `commander.js` for argument parsing
- Subcommands: `init`, `run`, `config`, `--help`, `--version`
- Colorized output with `chalk`
- Interactive prompts with `inquirer`
- Configuration file support (~/.toolname/config.json)
- Progress indicators with `ora`
- Proper exit codes

Include: `package.json` (with `bin` field), `tsconfig.json`, entry point, and a `README.md` with usage examples.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
