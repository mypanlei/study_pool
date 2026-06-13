---
title: "RAG 系统常见问题与全链路优化指南"
tags:
  - source
  - rag
  - retrieval-augmented-generation
  - llm
  - optimization
  - vector-database
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-04-10
---

# RAG 系统常见问题与全链路优化指南

> RAG 落地中"检索不准"和"生成幻觉"两大难题的避坑经验，覆盖从朴素 RAG 向高级/模块化 RAG 进阶的全链路优化。

## 核心论点

1. **检索端优化**：
   - 语义失准 → Hybrid Search（Dense + BM25）+ BGE/Rerank 重排序
   - 问题模糊 → HyDE（伪答案检索）+ Query Rewrite（代词还原）
2. **生成端优化**：
   - 幻觉与过度外推 → Strict Guardrails + Citation 引用溯源
   - 信息过载与 Lost in Middle → Context Filtering + 关键信息放 Prompt 首尾
3. **评估体系**：RAGAS 三元组——Faithfulness（忠实度）、Answer Relevancy（相关性）、Context Precision（检索精度）。
4. **进阶架构 GraphRAG**：实体提取 + 社区检测，解决跨文档关联复杂查询。

## 与现有知识的关系

- 与 [[wiki/sources/ragas-evaluation-metrics]] 构成 RAG 评估体系
- 与 [[wiki/sources/rag-vs-semantic-cache-comparison]] 互补（RAG 优化 vs RAG 与缓存对比）
- 与 [[wiki/concepts/rag-optimization]] 关联

## 受影响的 Wiki 页面

- [[wiki/concepts/rag-optimization]] — 已创建
- [[wiki/syntheses/rag-optimization-guide]] — 已更新
- [[wiki/concepts/rag-vs-wiki]] — 已更新
