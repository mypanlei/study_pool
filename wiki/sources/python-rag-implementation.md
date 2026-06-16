---
title: "Python 实现 RAG 与知识检索 — 菜鸟教程"
tags:
  - source
  - python
  - rag
  - retrieval
  - implementation
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/python-rag.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Python 实现 RAG 与知识检索

> Python 从零实现 RAG 系统的实战教程，覆盖基础 RAG（检索器/向量库/生成器三组件）、Advanced RAG（重排序/混合检索/查询改写/CRAG）、向量数据库选型对比、以及 GraphRAG（知识图谱+向量检索融合）。

## 核心内容

1. **基础 RAG 实现** — SimpleRAG 类：文档切分（chunk_size/overlap）、Embedding 向量化、向量相似度检索、上下文增强生成。
2. **Advanced RAG** — 重排序（Cross-Encoder 精排）、混合检索（稠密+稀疏/BM25+RRF 融合）、查询改写/HyDE、CRAG（修正式检索+Web Search 兜底）。
3. **向量数据库** — Pinecone/Weaviate/Milvus/Chroma/Qdrant 对比选型，余弦相似度/欧氏距离/点积三种度量方式。
4. **GraphRAG** — 知识图谱构建（NER 实体提取+关系抽取）、双路检索（向量+图谱遍历）、图文融合生成，适用于多跳推理场景。
5. **评估指标** — RAGAS 框架：Context Recall/Precision、Faithfulness、Answer Relevance。

## 关键概念

- RAG = 检索增强生成，让 LLM 从外部知识库检索相关内容再生成回答
- Advanced RAG 三段式：预检索优化（查询改写）→ 检索融合（混合检索）→ 后检索优化（重排序）
- GraphRAG 解决传统 RAG 无法处理跨文档多跳推理的问题
