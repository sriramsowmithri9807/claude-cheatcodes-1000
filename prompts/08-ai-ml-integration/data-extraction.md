---
title: "Extract Structured Data from Unstructured Text"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [extraction, nlp, structured-data, claude]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Extract structured data from unstructured text using Claude.

Input text type: [DESCRIBE: receipts, resumes, medical notes, legal contracts, emails]
Data to extract: [LIST FIELDS TO EXTRACT]

1. **Define output schema** (TypeScript interface or Zod schema)
2. **Extraction prompt**: precise instructions for each field
3. **JSON mode**: force structured JSON output
4. **Validation**: Zod validate the extracted data
5. **Handling missing data**: null vs "not mentioned" vs inferred
6. **Tables extraction**: extract tabular data from text
7. **Multiple records**: extract list of items from one document
8. **Accuracy**: handle typos, abbreviations, different formats
9. **Normalization**: dates → ISO 8601, currencies → decimal
10. **Confidence**: flag fields where extraction is uncertain

Batch processing for high volume.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
