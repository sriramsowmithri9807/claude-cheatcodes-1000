---
title: "Build a Document Analysis System"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [documents, pdf, analysis, claude]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a system to analyze and extract information from documents.

Document types: [PDFs, Word docs, Excel, emails, etc.]
Extraction goal: [DESCRIBE: extract key data points, summarize, classify, compare]

Implement:
1. **Document loading**: PDF parsing (pdf-parse), DOCX (mammoth), Excel (xlsx)
2. **Text extraction**: preserve structure (headings, tables, lists)
3. **Claude analysis prompt**: extract specific structured data
4. **Structured output**: force JSON output with schema validation
5. **Table extraction**: extract tables as structured data
6. **Multi-document comparison**: compare N documents for differences
7. **Citation extraction**: identify and validate citations
8. **PII detection**: find and flag personal information
9. **Batch processing**: process hundreds of documents efficiently
10. **Output formats**: JSON, CSV, structured database records

Node.js + TypeScript with Zod validation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
