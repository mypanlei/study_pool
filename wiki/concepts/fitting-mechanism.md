---
title: "拟合机制"
tags:
  - concept
  - machine-learning
  - fitting
  - model-capacity
  - deep-learning
created: 2026-06-13
updated: 2026-06-13
aliases:
  - 拟合
  - 欠拟合
  - 过拟合
  - 模型容量
  - Fitting
---

# 拟合机制

> 机器学习模型学习能力与数据规律之间匹配程度的核心概念。拟合的三种状态（欠拟合/恰好拟合/过拟合）直接影响模型性能和泛化能力。

## 定义

拟合（Fitting）是通过调整模型参数 theta，使模型输出 f(x;theta) 尽可能准确地模拟客观世界中复杂规律（标签 y）的函数逼近过程。数学目标是最小化损失函数 L。

## 核心要点

1. **三种拟合状态**：
   - 欠拟合（Underfitting）：模型容量不足，无法捕捉基本规律。表现为训练/测试准确率均低。
   - 恰好拟合（Good Fitting）：模型成功捕捉潜在规律，具备好泛化能力。
   - 过拟合（Overfitting）：模型把随机噪声也当成规律学进去，表现为训练集准确率高但测试集极差。
2. **模型容量**：LoRA 中 Rank(r) 直接决定容量（r=8 低容量，r=128 高容量）。
3. **LLM 微调特有拟合问题**：
   - 知识冲突：微调数据与预训练常识矛盾导致拟合阻力（特殊的"语义欠拟合"）
   - 灾难性遗忘：过度拟合新任务破坏原有泛化结构

## 详细阐述

### 调优策略
欠拟合时：增加 Rank、开启 all-linear、调高学习率、增加 Epochs、数据纯化
过拟合时：增加 Dropout、减少 Epochs、数据清洗/增强

### 拟合与插值的关系
RoPE 插值后需微调补偿（5%-10% 长文本语料），这是拟合理论在 LLM 长上下文扩展中的实战应用。

## 相关概念

- [[wiki/concepts/transformer-architecture]] — Transformer 作为拟合的模型基础
- [[wiki/concepts/rope-positional-encoding]] — 插值后拟合补偿

## 来源

- [[wiki/sources/fitting-mechanism-deep-analysis]]
- [[wiki/sources/large-model-parameters-and-performance]]
- [[wiki/sources/rope-interpolation-technical-detail]]
