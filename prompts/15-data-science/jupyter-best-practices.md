---
title: "Write Better Jupyter Notebooks"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [jupyter, notebooks, data-science, best-practices]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Apply best practices to my Jupyter notebooks.

Current notebook: [DESCRIBE WHAT YOUR NOTEBOOK DOES]

Notebook quality improvements:
1. **Structure**: introduction → data → analysis → conclusions
2. **Markdown**: rich text cells explaining the story (not just code)
3. **Cell size**: one logical step per cell
4. **Reproducibility**: set random seeds, specify package versions
5. **Dependencies**: requirements.txt or conda environment.yml
6. **Data paths**: use relative paths, document where data comes from
7. **Function extraction**: move reusable code to .py files
8. **Output management**: clear outputs before committing to git
9. **nbstripout**: git hook to strip outputs automatically
10. **Parameterization**: Papermill for parameterized notebook runs

Conversion to production:
11. Extract core logic to Python module
12. Keep notebook as documentation/analysis only
13. Schedule with Airflow using PapermillOperator

Output: refactored notebook following all best practices.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
