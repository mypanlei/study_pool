---
title: "向量数据库（Vector Database） — 菜鸟教程"
tags:
  - source
  - vector-database
  - embedding
  - rag
  - ann
  - hnsw
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/vector-database.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# 向量数据库（Vector Database）

> 系统介绍向量数据库的原理与实践，涵盖向量与嵌入概念、三种相似度计算方法（余弦相似度/欧氏距离/点积）、索引算法（Flat/IVF/HNSW/ScaNN）、主流数据库对比（Chroma/Qdrant/Weaviate/Milvus/Pinecone/pgvector）、Python 示例和典型应用场景。

## 核心内容

1. **核心概念** — 向量（一组有序数字表示语义特征）、嵌入（将对象转为向量的过程）、语义近则向量近。
2. **相似度计算** — 余弦相似度（文本首选，关注方向）、欧氏距离（图像检索，关注绝对距离）、点积（推荐系统，综合方向长度）。
3. **索引算法** — Flat（精确暴力检索）、IVF（聚类后桶内搜索）、HNSW（分层导航小世界图，最主流，O(log n)）、IVF_PQ（量化压缩节省内存）。
4. **主流数据库对比** — Chroma（入门首选，嵌入式）、Qdrant（生产级 Rust 实现）、Weaviate（多模态+GraphQL）、Milvus（亿级分布式）、Pinecone（全托管 SaaS）、pgvector（PostgreSQL 扩展）。
5. **Python 实战** — Chroma 完整 CRUD 示例（8 个文档的语义搜索系统）、纯本地 SentenceTransformer 离线方案、pgvector SQL 示例。
6. **典型应用场景** — RAG 知识库问答、个性化推荐、以图搜图、异常检测、内容去重、人脸识别。

## 关键概念

- 向量数据库通过相似度查询（"找到和这个最像的"），而非精确匹配
- 嵌入模型必须统一：插入和查询必须用同一个模型
- HNSW 是最主流的 ANN 算法，兼顾速度和精度
