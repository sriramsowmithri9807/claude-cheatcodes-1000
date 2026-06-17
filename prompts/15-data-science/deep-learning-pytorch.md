---
title: "Build Deep Learning Models with PyTorch"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pytorch, deep-learning, neural-networks, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a deep learning model with PyTorch.

Task: [DESCRIBE: image classification, NLP, tabular, custom architecture]
Dataset: [DESCRIBE]

Implementation:
1. **Dataset class**: `torch.utils.data.Dataset` for your data
2. **DataLoader**: batching, shuffling, num_workers
3. **Model architecture**: `nn.Module` subclass
4. **Loss function**: CrossEntropyLoss, MSELoss, etc.
5. **Optimizer**: Adam with weight decay, learning rate scheduler
6. **Training loop**:
   - Forward pass
   - Loss computation
   - Backward pass
   - Optimizer step
   - Gradient clipping
7. **Validation loop**: no_grad, eval mode
8. **Checkpointing**: save/load best model
9. **Metrics**: accuracy, AUC, etc. per epoch
10. **TensorBoard**: log loss and metrics
11. **GPU**: `.to(device)`, CUDA availability check
12. **Mixed precision**: `torch.autocast` for speed

Output: complete training script for my task.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
