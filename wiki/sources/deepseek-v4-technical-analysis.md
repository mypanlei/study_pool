---
title: "DeepSeek-V4 技术分析：长文本与高缓存命中率"
tags:
  - source
  - deepseek
  - llm
  - kv-cache
  - csa
  - hca
  - prefix-caching
created: 2026-06-13
updated: 2026-06-13
aliases:
  - DeepSeek-V4 技术分析
---

# DeepSeek-V4 技术分析：长文本与高缓存命中率的秘诀

> 本文解析 DeepSeek-V4 (2026-04 发布) 的核心架构演进 CSA/HCA、KV Cache 极致压缩技术以及高缓存命中率的商业与工程实现。

## 核心贡献

1. **CSA (Compressed Sparse Attention)**：序列维度压缩 4 倍，将每 4 个连续 Token 聚合为一个压缩条目，配合 Lightning Indexer 动态决定关注哪些压缩块。
2. **HCA (Heavily Compressed Attention)**：模型前几层使用，序列维度压缩 128 倍，提供全局上下文的"极简草图"，大幅降低初始处理长文本计算量。
3. **KV Cache 极致压缩**：1M 上下文仅需约 9.6 GB (V3 约为 84 GB)，缓存使用 FP8 精度。V3 压头维度 (MLA)，V4 压序列维度 (CSA/HCA)。
4. **前缀缓存策略**：自动哈希分块识别重复 System Prompt 或历史对话，多轮对话/Agent 任务缓存命中率 80%+，V4-Flash 实测平均 97%。
5. **阶梯定价闭环**：缓存命中 Token 价格降至非命中 1/10，倒逼开发者将静态内容放在 Prompt 前部，人为提升全局命中率。

## 关联页面

- [[wiki/entities/deepseek]] — DeepSeek AI 公司实体
- [[wiki/concepts/kv-cache]] — KV Cache 概念与 CSA/HCA 扩展
- [[wiki/syntheses/deepseek-technical-analysis]] — DeepSeek 技术综合分析

## 参考链接

- [[KV-Cache-技术详解]]
