---
title: "LLM 技术基础"
tags:
  - synthesis
  - llm
  - transformer
  - kv-cache
  - rope
  - scaling-laws
  - fitting
created: 2026-06-13
updated: 2026-06-13
aliases:
  - LLM 技术基础全景
---

# LLM 技术基础

> 综合 5 篇 Deep Learning / LLM 技术文章的跨源综合分析，覆盖 Transformer 架构、KV Cache、RoPE 插值、Scaling Laws 和拟合机制。

## 背景

本次综合涵盖：Transformer 架构详解、KV Cache 技术详解、RoPE 插值技术详解、大模型参数量与性能关系详解、拟合机制深度解析。这 5 篇文章构成了 LLM 技术基础的核心拼图。

## 各方观点

### 基石：Transformer 架构
来源：[[wiki/sources/transformer-architecture-detail]]

Transformer 是 LLM 的基石，核心创新是自注意力机制实现完全并行化处理。QKV 机制（Query/Key/Value 三个线性变换）是注意力计算的基础。架构从 Encoder-Decoder 演变为 Decoder-only 主导（GPT/Llama/Claude）。

### 推理优化：KV Cache
来源：[[wiki/sources/kv-cache-technical-detail]]

KV Cache 通过缓存历史 Token 的 K/V 向量避免重复计算，是推理优化的核心技术。架构从 MHA → GQA（Llama 3/Mistral）→ MLA（DeepSeek V2/V3）→ CSA/HCA（序列级压缩）演进。PagedAttention 解决显存碎片。

### 长上下文：RoPE 插值
来源：[[wiki/sources/rope-interpolation-technical-detail]]

RoPE 通过旋转矩阵编码位置信息。扩展上下文时，插值（坐标系压缩）优于外推。方法演进：PI → NTK-Aware → YaRN（工业标准）→ DroPE（百万级）。128k 以上推荐 YaRN，需 FlashAttention 配合。

### 规模定律：Scaling Laws
来源：[[wiki/sources/large-model-parameters-and-performance]]

Kaplan 定律（更多参数更有效）→ Chinchilla 定律（参数与数据等比例）。小模型逆袭源于：超量训练数据（Llama 3-8B/15T Token）+ 高质量数据配比 + 架构改进（RMSNorm/RoPE/SwiGLU）。

### 学习理论：拟合机制
来源：[[wiki/sources/fitting-mechanism-deep-analysis]]

拟合 = 函数逼近。三种状态（欠/恰好/过拟合）。模型容量（LoRA 的 Rank）决定拟合能力上限。LLM 特有拟合问题：知识冲突和灾难性遗忘。插值后需微调补偿（拟合理论实战应用）。

## 对比分析

| 维度 | Transformer | KV Cache | RoPE 插值 | Scaling Laws | 拟合机制 |
|------|------------|---------|-----------|-------------|---------|
| 核心问题 | 如何并行处理序列 | 如何加速推理 | 如何扩展上下文 | 如何分配资源 | 如何学会规律 |
| 关键参数 | 头数/层数/维度 | Cache 大小/Block 大小 | 缩放因子/方法选择 | N/D/C 三者关系 | Rank/Learning Rate |
| 瓶颈 | 计算+显存 | 显存带宽 | 预训练角度范围 | 训练成本 | 模型容量 |
| 当前趋势 | Decoder-only 主导 | GQA/MLA/PagedAttention | YaRN/NTK | Chinchilla 最优 | MoE/端侧小巧模型 |

## 综合结论

5 篇文章构成了一条从"架构理论→推理优化→上下文扩展→规模定律→学习理论"的完整 LLM 技术链条：

1. **Transformer** 提供了并行自注意力的计算范式
2. **KV Cache** 让推理在显存约束下可行
3. **RoPE 插值** 突破了训练长度的上下文限制
4. **Scaling Laws** 指导了参数和数据的分配策略
5. **拟合机制** 解释了模型如何从数据中学习

## 开放问题

- DeepSeek V4 的 CSA/HCA 序列压缩能否真正支撑百万 token 上下文同时保持精度？
- DroPE 脱离式位置编码能否在不损失精度的前提下替代 RoPE？
- MoE 架构是否能同时实现"大容量"和"低推理成本"的长期目标？

## 来源

- [[wiki/sources/transformer-architecture-detail]]
- [[wiki/sources/kv-cache-technical-detail]]
- [[wiki/sources/rope-interpolation-technical-detail]]
- [[wiki/sources/large-model-parameters-and-performance]]
- [[wiki/sources/fitting-mechanism-deep-analysis]]
