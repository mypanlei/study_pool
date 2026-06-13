---
title: "拟合机制深度解析"
tags:
  - source
  - machine-learning
  - fitting
  - underfitting
  - overfitting
  - deep-learning
  - model-capacity
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-05-13
---

# 拟合机制深度解析：机器学习与 LLM 微调的底层逻辑

> 系统解析拟合的数学本质、三种状态（欠拟合/恰好拟合/过拟合）、模型容量概念及 LLM 微调中的特有拟合问题。

## 核心论点

1. **拟合的数学本质**：函数逼近——通过调整参数 theta 使模型输出尽可能准确模拟客观规律。最优 theta = argmin E[Loss(f(x;theta), y)]。
2. **拟合三种状态**：欠拟合（Low Capacity，无法捕捉基本规律）→ 恰好拟合（好泛化）→ 过拟合（把噪声当规律学进去，死记硬背）。
3. **模型容量核心概念**：LoRA 中 Rank(r) 直接决定容量。r=8 低容量，r=128 高容量。简单逻辑低容量即可，复杂逻辑需要高容量。
4. **LLM 微调特有拟合问题**：知识冲突（微调数据与预训练常识矛盾）和灾难性遗忘（过度拟合新任务破坏原有泛化结构）。
5. **调优路径**：欠拟合时增加 Rank、开启 all-linear、调高学习率、增加训练轮数、数据纯化。

## 与现有知识的关系

- 与 [[wiki/sources/large-model-parameters-and-performance]] 中的 Scaling Laws 和模型容量概念互补
- 与 [[wiki/sources/rope-interpolation-technical-detail]] 中的微调权衡呼应

## 受影响的 Wiki 页面

- [[wiki/concepts/fitting-mechanism]] — 已创建
- [[wiki/syntheses/llm-technical-foundations]] — 已更新
