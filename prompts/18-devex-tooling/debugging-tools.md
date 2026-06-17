---
title: "Set Up Debugging Tools"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [debugging, devtools, node-js, chrome]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up comprehensive debugging tools for my stack.

Stack: [NODE.JS / BROWSER / REACT]

**Node.js debugging**:
1. VS Code debugger: `.vscode/launch.json` configuration
2. `--inspect` flag: `node --inspect server.js`
3. Chrome DevTools: `chrome://inspect`
4. `debugger` statement: pause execution in debugger
5. `console.trace()`: print stack trace
6. Logging: structured logging with pino

**Browser debugging**:
7. Chrome DevTools: Elements, Network, Console, Sources
8. `console.table()`: visualize arrays of objects
9. `$0` in console: last selected element
10. Network conditions: throttle to simulate slow connection
11. Breakpoints: conditional, XHR, event listener

**React debugging**:
12. React DevTools: component tree, props, state
13. Why Did You Render: log unnecessary re-renders
14. Redux/Zustand DevTools: state inspection

**Remote debugging**:
15. ngrok: expose localhost to webhook services

Output: VS Code launch.json + debugging tips.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
