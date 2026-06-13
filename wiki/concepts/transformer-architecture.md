---
title: "Transformer 架构"
tags:
  - concept
  - llm
  - deep-learning
  - architecture
  - attention
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Transformer
  - Attention Is All You Need
  - 自注意力机制
---

# Transformer 架构

> 现代 LLM 的基石架构，2017 年由 Google 在《Attention Is All You Need》中提出。核心贡献是完全并行化的自注意力机制。

## 定义

Transformer 是一种基于自注意力机制（Self-Attention）的神经网络架构，通过一次性输入整个序列实现了完全并行计算，解决了 RNN 无法并行和长距离依赖丢失的问题。

## 核心要点

1. **自注意力机制**：Q（Query，当前词找什么）、K（Key，其他词有什么特征）、V（Value，匹配后提供什么内容）三个向量的点积+Softmax+加权求和。
2. **多头注意力 MHA**：多个注意力头从不同视角关注序列（语法、语义等），但 KV Cache 随头数线性增长。
3. **GQA 分组查询注意力**：Llama 3/Mistral 采用，对 Q 头分组共享 KV 头，减少显存占用，平衡效率与精度。
4. **位置编码**：因为并行处理，需要 RoPE 等位置编码注入位置信息。
5. **架构分化**：Encoder-Decoder（原始，T5/FLAN）vs Decoder-only（主流，GPT/Llama/Claude）。

## 详细阐述

### 背景
在 Transformer 之前，RNN/LSTM 必须按顺序处理序列，无法利用 GPU 并行能力且长距离依赖困难。Transformer 通过自注意力机制一次性处理整个序列，使长距离词之间的依赖可以直接捕获。

### 机制
每个 token 的输入向量 x' 分别乘以三个学习得到的权重矩阵 W_Q, W_K, W_V 得到 Q/K/V。注意力得分 = softmax(Q @ K^T / sqrt(d_k)) @ V。整个过程完全可并行。

### 演进
原始 MHA → MQA（多查询共享，极致压缩）→ GQA（分组共享，平衡方案，Llama 3）→ MLA（低秩投影，DeepSeek V2/V3）→ CSA/HCA（序列维度压缩，DeepSeek V4）。

## 相关概念

- [[wiki/concepts/kv-cache]] — 推理时缓存 K/V 避免重复计算
- [[wiki/concepts/transformer-architecture]] — 位置编码与 RoPE 插值
- [[wiki/concepts/fitting-mechanism]] — 模型容量与拟合能力

## 来源

- [[wiki/sources/transformer-architecture-detail]]
- [[wiki/sources/kv-cache-technical-detail]]
- [[wiki/sources/rope-interpolation-technical-detail]]
- [[wiki/sources/large-model-parameters-and-performance]]
