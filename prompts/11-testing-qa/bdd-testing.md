---
title: "Write BDD-Style Tests"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [bdd, cucumber, gherkin, testing]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write Behavior-Driven Development (BDD) tests for my features.

Features to test: [DESCRIBE FEATURES IN BUSINESS TERMS]
Framework: Cucumber.js (or Vitest with BDD syntax)

Gherkin feature files:
```gherkin
Feature: [FEATURE NAME]
  As a [USER TYPE]
  I want to [GOAL]
  So that [BUSINESS VALUE]

  Scenario: [SCENARIO NAME]
    Given [INITIAL STATE]
    When [ACTION]
    Then [EXPECTED OUTCOME]
    And [ADDITIONAL ASSERTION]
```

Step definitions:
- Given steps: set up state
- When steps: perform action
- Then steps: assert outcome

Best practices:
- Write scenarios with product owner, not after
- Scenarios describe behavior, not implementation
- Living documentation: scenarios are always up to date

Output: feature files + step definitions for my use cases.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
