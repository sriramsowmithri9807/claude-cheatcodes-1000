---
title: "Set Up Perfect Development Environment"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [dev-environment, dotfiles, tooling, productivity]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up a perfect development environment for [LANGUAGE/STACK].

OS: [Mac / Linux / Windows]
Stack: [DESCRIBE]

**Terminal setup**:
1. iTerm2 (Mac) or Warp — better than default terminal
2. Zsh + Oh My Zsh or Starship prompt
3. Plugins: zsh-autosuggestions, zsh-syntax-highlighting, fzf
4. Aliases: shortcuts for common commands

**Package management**:
5. Homebrew (Mac) — install everything
6. `mise` or `nvm` — manage Node.js versions
7. `pyenv` — manage Python versions

**Essential tools**:
8. `git` configuration: user, aliases, delta for diffs
9. `gh` — GitHub CLI
10. `jq` — JSON processor
11. `httpie` or `curl` — API testing
12. `k9s` — Kubernetes dashboard in terminal

**Dotfiles**:
13. Track in git repo
14. `stow` or `chezmoi` for symlinks
15. Bootstrap script: new machine ready in 10 minutes

Output: complete setup script + dotfiles for my stack.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
