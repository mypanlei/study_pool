---
title: "语义缓存 (Semantic Cache) 与 RAG 的深度对比"
tags:
  - source
  - rag
  - semantic-cache
  - architecture
  - comparison
  - llm
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-04-10
---

# 语义缓存 (Semantic Cache) 与 RAG 的深度对比

> 虽都使用向量搜索，但语义缓存和 RAG 在角色、目标和存储内容上完全不同。语义缓存是"加速器"；RAG 是"知识注入器"。

## 核心论点

1. **核心目标不同**：语义缓存追求极速响应和降本；RAG 追求消除幻觉和注入最新知识。
2. **存储内容不同**：语义缓存存 QA 对（问题向量+最终答案）；RAG 存知识切片（文档向量+原始分块）。
3. **是否调用 LLM**：语义缓存仅未命中时调用 LLM；RAG 每次请求都必须调用 LLM。
4. **最佳实践**：RAG 是知识源头；语义缓存是加速器。LLM 根据 RAG 生成回答后再存进语义缓存供后续相似问题直接使用。
5. **向量代表意义不同**：语义缓存向量代表"问题意图"；RAG 向量代表"知识内容"。

## 关键对比

| 维度 | 语义缓存 | RAG |
|---|---|---|
| 核心目标 | 极速响应、降本 | 消除幻觉、注入最新知识 |
| 存储内容 | QA 对 | 知识切片 |
| 是否调用 LLM | 仅未命中时 | 每次都调用 |
| 响应延迟 | 10-50ms | 1-5s |
| 知识时效性 | 较差 | 极强 |

## 与现有知识的关系

- 与 [[wiki/sources/rag-common-issues-and-optimization]] 共同构成 RAG 知识体系
- 支撑 [[wiki/syntheses/rag-optimization-guide]]

## 受影响的 Wiki 页面

- [[wiki/concepts/rag-optimization]] — 已更新
- [[wiki/syntheses/rag-optimization-guide]] — 已更新
- [[wiki/concepts/rag-vs-wiki]] — 已更新
