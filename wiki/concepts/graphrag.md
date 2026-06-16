---
title: "GraphRAG — 知识图谱增强 RAG"
tags:
  - concept
  - rag
  - knowledge-graph
created: 2026-06-17
updated: 2026-06-17
aliases:
  - 知识图谱 RAG
  - Graph Retrieval Augmented Generation
---

# GraphRAG

> 微软推出的知识图谱增强 RAG 方法。在传统 RAG 的向量检索之上，额外构建实体关系图谱，实现跨文档的全局性推理。

## 核心思想

- 从文档中提取实体和关系 → 构建知识图谱
- 查询时，同时进行：向量检索 + 图谱遍历
- 答案综合两者的结果，实现全局性理解

## 与传统 RAG 对比

| 维度 | 传统 RAG | GraphRAG |
|------|---------|-----------|
| 检索单位 | 文档块（chunk） | 实体 + 关系 + 块 |
| 结构保持 | 丢失文档间关系 | 保留实体关系网络 |
| 全局查询 | 弱（各 chunk 独立） | 强（图谱遍历） |
| 实现成本 | 低 | 高 |
| 适合场景 | FAQ/单文档问答 | 多文档/跨文档综合分析 |

## 来源

- [[wiki/concepts/rag-optimization]]
- [[wiki/syntheses/rag-optimization-guide]]
- 知识库内 19 处引用
