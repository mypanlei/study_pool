---
title: "Fine-tuning — 微调"
tags:
  - concept
  - training
  - llm
  - peft
created: 2026-06-17
updated: 2026-06-17
aliases:
  - 微调
  - SFT
  - Supervised Fine-tuning
---

# Fine-tuning（微调）

> 在预训练模型基础上，用特定任务数据继续训练以适应特定场景的方法。从全量微调到高效微调（LoRA/QLoRA），是 LLM 适配落地的核心手段。

## 微调类型

| 类型 | 训练参数量 | 显存 | 适用场景 |
|------|-----------|------|---------|
| **全量微调** | 100% | 极高 | 领域大模型 |
| **LoRA** | 0.1-1% | 低 | 任务适配 |
| **QLoRA** | 0.1-1% | 极低（4bit） | 单 GPU 微调 |
| **Adapter** | 1-5% | 低 | 多任务切换 |

## SFT（Supervised Fine-tuning）

使用人工标注的高质量问答数据对模型进行监督学习，是 RLHF 流程的前置步骤。DeepSeek-R1 的"冷启动"阶段即使用 SFT。

## 与 LoRA 的关系

- LoRA 是高效微调（PEFT）的代表方法
- 详见 [[wiki/concepts/lora-low-rank-adaptation]]

## 来源

- 知识库内 8 处引用
