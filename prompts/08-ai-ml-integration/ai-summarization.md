---
title: "Build Text Summarization Features"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [summarization, claude, nlp, content]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add AI summarization to my application.

Content to summarize: [DESCRIBE: articles, meeting transcripts, reports, emails]
Summary format: [BULLET POINTS / PARAGRAPH / STRUCTURED SECTIONS]
Audience: [WHO WILL READ THE SUMMARY]

1. **Summary types**:
   - Executive summary: 3 bullet points for busy readers
   - Detailed summary: preserves all key points
   - Meeting minutes: action items, decisions, attendees
   - Abstractive: new sentences (not copied from original)
2. **Long document handling**: chunk → summarize each → meta-summarize
3. **Key points extraction**: numbered list of most important points
4. **Action items**: extract TODO items from meeting notes
5. **Sentiment**: add overall tone (positive/negative/neutral)
6. **Multilingual**: summarize in a different language
7. **Custom length**: user controls word count
8. **Citation**: which part of original supports each summary point

React component + backend API.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
