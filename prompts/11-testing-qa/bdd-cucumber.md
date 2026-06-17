---
title: "Set Up Cucumber for BDD Testing"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cucumber, bdd, gherkin, testing]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up Cucumber.js for BDD testing in my Node.js project.

Features to test: [DESCRIBE IN BUSINESS TERMS]

1. **Installation**: `@cucumber/cucumber`, `@playwright/test` or Supertest
2. **Feature files**: write in Gherkin syntax
3. **Step definitions**: implement each Given/When/Then step
4. **World**: shared context between steps
5. **Hooks**: Before/After for setup and teardown
6. **Tags**: @slow, @smoke, @regression — run subsets
7. **Parameterized scenarios**: Scenario Outline with Examples table
8. **Background**: common steps for all scenarios in a feature
9. **Reports**: cucumber-html-reporter for stakeholders
10. **Page objects**: for UI scenarios

Feature to implement end-to-end:
```gherkin
[YOUR FEATURE IN GHERKIN]
```

Output: feature file + step definitions + cucumber config.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
