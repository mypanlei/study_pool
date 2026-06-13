---
title: "KV Cache"
tags:
  - concept
  - llm
  - inference
  - optimization
  - transformer
  - memory
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Key-Value Cache
  - PagedAttention
---

# KV Cache (Key-Value Cache)

> LLM 推理优化的核心技术，通过缓存注意力机制中前文 Token 的 K 和 V 向量，避免自回归逐 Token 生成中的重复计算。

## 定义

KV Cache 是 Transformer 推理时的一种空间换时间优化技术。在自回归生成中，每生成一个新 Token 都需要计算注意力，通过缓存历史 Token 的 K 和 V 向量，将每步计算量从 O(N^2) 降至 O(N)。

## 核心要点

1. **推理阶段划分**：Prefill（预填充，计算所有输入 Token 的 KV 并缓存）和 Decode（解码，每步仅算当前 Token KV，从缓存读取历史）。
2. **架构演进**：MHA（标准多头，显存压力大）→ MQA（共享 KV 极致压缩）→ GQA（分组共享，Llama 3）→ MLA（低秩投影，DeepSeek V2/V3）→ **CSA/HCA（序列维度压缩，DeepSeek V4）**。
3. **PagedAttention**：vLLM 的核心创新，借鉴操作系统分页机制将 KV Cache 离散化存储在 Block 中，提升显存利用率至 96%+（传统预分配 60%+ 碎片浪费）。

## 详细阐述

### 与 FlashAttention 的区别
- KV Cache：算法层空间换时间，解决重复计算
- FlashAttention：硬件层 IO 优化，解决 GPU 显存读写瓶颈
两者互补，可同时使用

### 长上下文挑战
KV Cache 随序列长度和头数线性增长。处理 128k 上下文时，KV Cache 可能占用数十 GB 显存。GQA、PagedAttention 和 CSA/HCA 是缓解这一问题的关键技术。

### CSA/HCA (DeepSeek-V4 序列压缩)

DeepSeek-V4 在 MLA 的基础上引入了序列维度的压缩：

- **CSA (Compressed Sparse Attention)**：序列维度压缩 **4 倍**，每 4 个连续 Token 聚合为一个压缩条目，配合 Lightning Indexer 动态决定关注哪些压缩块。MLA 压注意力头维度，CSA 压序列长度维度，两者正交叠加。
- **HCA (Heavily Compressed Attention)**：模型前几层使用，序列维度压缩 **128 倍**，提供全局上下文"极简草图"，大幅降低初始处理长文本计算量。
- **效果**：1M 上下文 KV Cache 从 V3 的 ~84 GB 降至 V4 的 ~9.6 GB，推理 FLOPs 下降约 70%。
- **前缀缓存**：自动哈希分块识别重复 System Prompt 或历史对话，实测缓存命中率可达 97%（V4-Flash 长上下文 Agent 任务）。

详细分析见 [[wiki/syntheses/deepseek-technical-analysis]]。

## 相关概念

- [[wiki/concepts/transformer-architecture]] — 注意力机制基础
- [[wiki/concepts/transformer-architecture]] — 位置编码与 RoPE

## 来源

- [[wiki/sources/kv-cache-technical-detail]]
- [[wiki/sources/transformer-architecture-detail]]
- [[wiki/sources/rope-interpolation-technical-detail]]
