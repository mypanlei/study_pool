---
title: "RAG 优化指南"
tags:
  - synthesis
  - rag
  - optimization
  - retrieval-augmented-generation
  - ragas
  - semantic-cache
  - evaluation
created: 2026-06-13
updated: 2026-06-13
aliases:
  - RAG 全链路优化全景
---

# RAG 优化指南

> 综合 3 篇 RAG 相关文章的跨源综合分析，覆盖 RAG 常见问题与优化、RAG vs Semantic Cache 对比、RAGAS 评估体系。

## 背景

RAG（检索增强生成）是 LLM 应用的事实标准架构，但在落地中面临"检索不准"和"生成幻觉"两大难题。本次综合涵盖 3 篇文章：RAG 常见问题与全链路优化指南、语义缓存与 RAG 深度对比、RAGAS 评估指标深度解析。

## 各方观点

### 维度 A：全链路优化
来源：[[wiki/sources/rag-common-issues-and-optimization]]

RAG 优化需同时覆盖检索端和生成端。检索端：Hybrid Search + Rerank + HyDE + Query Rewrite + GraphRAG。生成端：Strict Guardrails + Citation + Context Filtering。进阶建议引入 GraphRAG 解决跨文档综合查询。

### 维度 B：RAG vs Semantic Cache
来源：[[wiki/sources/rag-vs-semantic-cache-comparison]]

语义缓存和 RAG 是互补而非互斥方案。RAG 负责知识注入（每次都调用 LLM 重新生成），语义缓存负责高频问题的秒级响应（10-50ms 缓存命中）。最佳实践：RAG 生成回答后写入语义缓存。

### 维度 C：评估体系
来源：[[wiki/sources/ragas-evaluation-metrics]]

RAGAS 三元组是量化评估的基础：Faithfulness（忠实度，回答是否完全来自 Context）、Answer Relevancy（回答相关性，是否答非所问）、Context Precision（检索精度，排序质量）。加上鲁棒性（Negative Rejection + Noise Sensitivity）。

## 对比分析

| 维度 | 检索端优化 | 生成端优化 | 语义缓存 | RAGAS 评估 |
|------|-----------|-----------|---------|-----------|
| 核心问题 | 检索不准 | 生成幻觉 | 延迟/成本 | 可靠性量化 |
| 关键技术 | Hybrid/Rerank/HyDE | Guardrails/Citation | 语义相似度匹配 | LLM-as-a-Judge |
| 推荐工具 | BGE/BAAI Reranker | - | 自建 | GPT-4/Qwen-Max |
| 复杂度 | 中 | 低-中 | 中 | 低-中 |

## 综合结论

一个高可靠的 RAG 系统需要 3 层能力的协同：

1. **检索质量层**：Hybrid Search + Rerank + Query Rewrite 确保检索到的文档高度相关
2. **生成控制层**：Strict Guardrails + Citation + Context Filtering 确保回答忠实于检索内容
3. **评估闭环层**：RAGAS 三元组量化评估 + 鲁棒性测试，驱动迭代改进

**加速层（可选）**：RAG 生成回答后写入语义缓存，高频问题实现 10-50ms 响应。

## 开放问题

- Karpathy 的 LLM Wiki 模式（持久化维基）与传统 RAG（无状态检索）如何选择/组合？
- GraphRAG 在实际生产中的计算开销和维护成本是否可控？
- LLM-as-a-Judge 评估的偏差问题和替代方案（如人工评估集）如何权衡？

## 来源

- [[wiki/sources/rag-common-issues-and-optimization]]
- [[wiki/sources/rag-vs-semantic-cache-comparison]]
- [[wiki/sources/ragas-evaluation-metrics]]
- [[wiki/sources/karpathy-llm-wiki-philosophy]]
