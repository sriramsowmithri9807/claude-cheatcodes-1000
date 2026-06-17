---
title: "Process and Analyze Text Data"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [nlp, text-processing, spacy, python]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Process and analyze text data with NLP techniques.

Text data: [DESCRIBE YOUR TEXT: customer reviews, news articles, tweets, documents]
Goal: [DESCRIBE: sentiment, topic, classification, entity extraction]

Processing pipeline:
1. **Cleaning**: lowercase, remove HTML, special chars
2. **Tokenization**: split into words/sentences
3. **Stop word removal**: remove common uninformative words
4. **Stemming/Lemmatization**: reduce to base form

Analysis:
5. **TF-IDF**: term frequency - inverse document frequency
6. **Topic modeling**: LDA for discovering topics
7. **Named Entity Recognition**: extract people, orgs, places
8. **Sentiment analysis**: VADER for lexicon, transformers for ML
9. **Text classification**: train classifier on labeled examples
10. **Word embeddings**: Word2Vec, GloVe, or sentence transformers
11. **Text similarity**: cosine similarity between documents
12. **Summarization**: extractive vs abstractive

Using: spaCy + HuggingFace transformers.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
