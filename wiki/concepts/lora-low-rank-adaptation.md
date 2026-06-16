---
title: "LoRA (Low-Rank Adaptation) — 低秩适配"
tags:
  - concept
  - fine-tuning
  - efficiency
  - peft
created: 2026-06-17
updated: 2026-06-17
aliases:
  - 低秩适配
  - Low-Rank Adaptation
  - LoRA 微调
---

# LoRA（低秩适配）

> 高效微调（PEFT）的代表方法。冻结原始模型权重，插入少量可训练的低秩矩阵，大幅降低微调成本。

## 核心原理

- 冻结预训练权重，不修改
- 在 Transformer 层旁插入低秩矩阵 A × B（rank r ≪ d）
- 推理时可将 LoRA 权重合并回原模型，无额外推理延迟

## 优势

| 维度 | 全量微调 | LoRA |
|------|---------|------|
| 可训练参数量 | 100% | ~0.1-1% |
| 显存需求 | 高 | 低 |
| 训练时间 | 长 | 短 |
| 多任务切换 | 需保存完整副本 | 仅保存几 MB 权重文件 |

## 常见变体

- **QLoRA** — 4-bit 量化 + LoRA，单 GPU 可微调 65B 模型
- **DoRA** — 权重分解低秩适配
- **rsLoRA** — 秩值缩放改进

## 来源

- 知识库内 11 处引用
