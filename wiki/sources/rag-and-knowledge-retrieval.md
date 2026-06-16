---
title: "RAG 与知识检索 — 菜鸟教程"
tags:
  - source
  - rag
  - retrieval
  - knowledge-base
  - llm
  - vector-database
  - graphrag
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/retrieval-augmented-generation.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# RAG 与知识检索

> 系统介绍 RAG 技术的原理和实践，涵盖离线索引流水线（文档切分/Embedding/向量化存储）和在线查询流水线（查询向量化/相似度检索/Prompt 拼接/LLM 生成），以及 Advanced RAG、GraphRAG、数据库选型和 RAGAS 评估框架。

## 核心内容

1. **RAG 基础流程** — 离线索引（文档→Chunking→Embedding→向量库）和在线查询（问题→向量化→检索→Prompt 拼接→生成）。
2. **文档切分策略** — 固定大小切分、递归字符切分、语义切分、父子文档检索（Small-to-Big），含 overlap 重叠配置。
3. **Advanced RAG** — 查询改写、HyDE 假设文档嵌入、混合检索（向量+BM25）、重排序（Cross-Encoder 精排）、Self-RAG/CRAG 自我修正检索。
4. **GraphRAG** — 知识图谱构建（三元组提取→Neo4j 存储）、双路检索（向量检索+图遍历）、图文融合生成，解决多跳推理问题。
5. **Embedding 模型对比** — text-embedding-3-small/large、BAAI/bge-m3、all-MiniLM-L6-v2，维度与精度权衡。
6. **数据库选型** — Pinecone（全托管）、Qdrant（高性能 Rust）、Weaviate/ES（混合检索）、Milvus（超大规模）、Chroma/FAISS（轻量本地）。
7. **RAGAS 评估** — Context Recall、Context Precision、Faithfulness、Answer Relevance 四个自动化量化指标。

## 关键概念

- RAG 解决 LLM 的两个核心痛点：知识截止日期和幻觉问题
- ANN 近似最近邻算法（HNSW）是百万级向量毫秒级检索的关键
- GraphRAG 通过实体关系图支持跨文档多跳推理
