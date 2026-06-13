---
title: "RAG 优化"
tags:
  - concept
  - rag
  - retrieval-augmented-generation
  - optimization
  - llm
created: 2026-06-13
updated: 2026-06-13
aliases:
  - RAG 全链路优化
  - 检索增强生成优化
---

# RAG 优化

> RAG（检索增强生成）系统从朴素实现向高级/模块化架构演进的全链路优化方法论，覆盖检索端、生成端和评估端。

## 定义

RAG 优化是一套系统性地提升检索增强生成系统准确性、相关性和效率的技术集合，包括检索质量改进、生成质量控制和量化评估三个核心维度。

## 核心要点

### 检索端优化
- **语义失准**：Hybrid Search（Dense + BM25 结合语义与关键词）+ BGE/Rerank 重排序（100→Top 5）
- **问题模糊**：HyDE（伪答案检索）+ Query Rewrite（多轮代词还原）
- **GraphRAG**：实体提取+社区检测，解决跨文档关联查询

### 生成端优化
- **幻觉与过度外推**：Strict Guardrails + Citation 引用溯源
- **信息过载 / Lost in Middle**：Context Filtering（仅相关片段）+ 关键信息放 Prompt 首尾

### 评估体系：RAGAS 三元组
1. Faithfulness（忠实度）：Claims 均可从 Context 找到依据
2. Answer Relevancy（回答相关性）：回答匹配问题意图
3. Context Precision（检索精度）：排序靠前的结果更有用

## 与 Semantic Cache 的关系

语义缓存是 RAG 的加速器：RAG 负责知识注入，语义缓存负责高频问题的秒级响应。最佳实践是 RAG 生成回答后写入语义缓存。

## 相关概念

- [[wiki/concepts/rag-vs-wiki]] — RAG 与持久化 Wiki 的对比
- [[wiki/concepts/llm-wiki-pattern]] — LLM Wiki 作为 RAG 的替代/补充

## 来源

- [[wiki/sources/rag-common-issues-and-optimization]]
- [[wiki/sources/rag-vs-semantic-cache-comparison]]
- [[wiki/sources/ragas-evaluation-metrics]]
- [[wiki/sources/karpathy-llm-wiki-philosophy]]
