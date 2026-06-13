---
title: "大模型参数量与性能关系详解"
tags:
  - source
  - llm
  - scaling-laws
  - deep-learning
  - model-optimization
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-02-05
---

# 大模型参数量与性能关系详解

> 分析 LLM 参数量与性能的关系，解释 Scaling Laws 以及"小模型"逆袭的底层逻辑。

## 核心论点

1. **参数量的本质**：决定模型容量（拟合复杂函数能力）和知识压缩率（参数量越大，保留信息越精确）。
2. **Scaling Laws 演进**：Kaplan 定律（OpenAI 2020，增加参数最显著）→ Chinchilla 定律（DeepMind 2022，N 和 D 应等比例增加，每增 1 倍参数至少增 20 倍训练 Token）。
3. **小模型逆袭原因**：大数据量训练小模型（如 Llama 3-8B 用 15T Token 训练）+ 数据质量提升（代码/数学/论文配比和合成数据）+ 架构改进（RMSNorm/RoPE/SwiGLU）。
4. **未来趋势**：MoE 稀疏激活实现"大容量低计算量"；端侧 1B-10B 参数高效模型主导本地终端。

## 与现有知识的关系

- 与 [[wiki/sources/transformer-architecture-detail]] 共同理解 LLM 架构设计
- 与 [[wiki/sources/fitting-mechanism-deep-analysis]] 中的模型容量概念呼应

## 受影响的 Wiki 页面

- [[wiki/concepts/transformer-architecture]] — 已更新
- [[wiki/syntheses/llm-technical-foundations]] — 已更新
