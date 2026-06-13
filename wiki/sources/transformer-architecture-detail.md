---
title: "Transformer 架构详解"
tags:
  - source
  - llm
  - deep-learning
  - transformer
  - architecture
  - nlp
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-02-04
---

# Transformer 架构详解

> 现代 LLM 的基石，Google 2017 年《Attention Is All You Need》提出。彻底改变 NLP 领域的并行化自注意力架构。

## 核心论点

1. **核心突破**：自注意力机制让模型能直接计算任意距离词之间的关联，解决 RNN 并行化不足和长距离依赖问题。
2. **QKV 机制**：Query（当前词找什么信息）、Key（其他词含什么特征）、Value（匹配后提供的内容）。通过训练学习的权重矩阵 W_Q/W_K/W_V 生成。
3. **架构分化**：原始 Encoder-Decoder → Decoder-only 成为主流（GPT/Llama/Claude，扩展性好）；Encoder-Decoder 仍在翻译/摘要等任务有用（T5/FLAN）。
4. **关键组件**：多头注意力 MHA（多视角但显存高）→ GQA（分组共享 KV，Llama 3/Mistral 核心）→ 位置编码 → FFN → 残差连接与层归一化。
5. **常见误解澄清**：训练数据被压缩进权重（并非像数据库一样存储），推理时 QKV 是临时生成的当前上下文表示（即 KV Cache）。

## 与现有知识的关系

- 为 [[wiki/sources/kv-cache-technical-detail]] 提供注意力机制基础
- 为 [[wiki/sources/rope-interpolation-technical-detail]] 提供位置编码基础
- 为 [[wiki/sources/large-model-parameters-and-performance]] 提供 Scaling Laws 理解基础

## 受影响的 Wiki 页面

- [[wiki/concepts/transformer-architecture]] — 已创建
- [[wiki/concepts/kv-cache]] — 已更新
- [[wiki/syntheses/llm-technical-foundations]] — 已更新
