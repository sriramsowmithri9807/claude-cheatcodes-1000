---
title: "Design and Analyze A/B Tests"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ab-testing, statistics, experiments, data-science]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design and analyze A/B tests rigorously.

Feature to test: [DESCRIBE WHAT YOU'RE TESTING]
Metric: [PRIMARY METRIC + GUARDRAIL METRICS]

**Experiment design**:
1. **Hypothesis**: null hypothesis + alternative hypothesis
2. **Sample size**: power analysis (80% power, α=0.05)
   - `scipy.stats.t`: compute minimum sample size
3. **Randomization unit**: user, session, device
4. **Duration**: run for minimum N weeks (capture weekly seasonality)
5. **Segments**: check if effect varies by user segment

**Analysis**:
6. **SRM check**: sample ratio mismatch (control/treatment equal?)
7. **Statistical test**: t-test, Mann-Whitney, z-test for proportions
8. **p-value and CI**: report both (CI is more informative)
9. **Effect size**: Cohen's d or relative lift
10. **Multiple testing**: Bonferroni correction for multiple metrics

**Decision**:
11. Did it win? Statistical + practical significance
12. Ship, iterate, or stop?
13. Post-ship monitoring: sustain the lift?

Output: Python analysis notebook.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
