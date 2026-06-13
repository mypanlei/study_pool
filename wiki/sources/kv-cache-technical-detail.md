---
title: "KV Cache 技术详解"
tags:
  - source
  - llm
  - inference
  - optimization
  - transformer
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-05-11
---

# KV Cache 技术详解

> LLM 推理优化的核心技术，通过缓存注意力机制中前文 Token 的 K 和 V 向量，避免自回归过程中的重复计算。

## 核心论点

1. **工作原理**：推理阶段分为 Prefill（计算所有输入 KV 并存入缓存）和 Decode（每步仅计算当前 Token KV，从缓存读取历史数据）。无缓存时计算量随序列长度平方级增长。
2. **架构演进**：MHA（标准多头，显存压力大）→ MQA（多查询共享，极致压缩有精度损耗）→ GQA（分组查询共享，推荐选择，如 Llama 3）→ MLA（低秩投影压缩"头维度"，DeepSeek V2/V3）→ CSA/HCA（序列维度压缩 4x-128x，支撑百万级上下文）。
3. **显存管理——PagedAttention**：传统预分配导致 60%+ 碎片浪费；vLLM PagedAttention 借鉴操作系统分页机制，提升显存利用率至 96%+。
4. **与 FlashAttention 的区别**：KV Cache 是算法层"空间换时间"解决重复计算；FlashAttention 是硬件层 IO 优化解决 GPU 显存读写瓶颈。

## 与现有知识的关系

- 与 [[wiki/sources/transformer-architecture-detail]] 构成理解 Transformer 推理优化的基础
- 与 [[wiki/sources/rope-interpolation-technical-detail]] 共同支撑长上下文推理
- 支撑 [[wiki/concepts/kv-cache]] 和 [[wiki/concepts/transformer-architecture]]

## 受影响的 Wiki 页面

- [[wiki/concepts/kv-cache]] — 已创建
- [[wiki/concepts/transformer-architecture]] — 已更新
- [[wiki/syntheses/llm-technical-foundations]] — 已更新
