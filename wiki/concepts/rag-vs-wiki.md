---
title: "RAG vs Wiki"
tags:
  - concept
  - comparison
created: 2026-06-13
updated: 2026-06-13
aliases:
  - RAG 与维基对比
---

# RAG vs Wiki

> Karpathy LLM Wiki 模式中提出的核心对比：无状态的检索-生成 vs 有状态的持久化积累。

## RAG（传统方案）

- 上传文档集合 → 向量化 → 查询时检索相关块 → LLM 合成答案
- ✅ 无需维护
- ❌ 每次查询重新发现知识，没有积累
- ❌ 综合问题需要从多文档中寻找碎片，容易遗漏
- ❌ 知识结构不可浏览

## LLM Wiki（持久方案）

- 源材料 → LLM 读取、提取、整合到维基 → 从维基回答问题
- ✅ 知识持续积累，产生复利效应
- ✅ 合成结果反映所有已读内容
- ✅ 可浏览（Markdown + Graph View）
- ❌ 需要初始设置成本
- ❌ 对源材料质量敏感

## 关键洞察

两者并非互斥。在 LLM Wiki 中，如果维基规模过大，index.md 检索可能不够用，此时可在维基层之上叠加轻量级搜索（如 qmd 的 BM25/向量混合搜索）。RAG 是工具，Wiki 是架构。

## RAG vs 传统搜索

RAG 和传统搜索都在"找信息"，但拿到信息之后做的事不一样：

| 维度 | 传统搜索 | RAG |
|------|---------|-----|
| **检索机制** | 倒排索引 + 关键词匹配 (BM25) | 向量检索/BM25/混合检索均可 |
| **结果形态** | 文档列表，用户二次阅读 | 直接可读答案 + 引用来源 |
| **数据范围** | 全网爬虫和大规模索引 | 企业内部知识库和垂直领域 |
| **成本和延迟** | 快，成本可控 | 多了 LLM 推理，延迟和成本上升 |
| **本质** | 排序器 | 信息综合器 |

> 选型判断：用户想要"找到材料"走搜索，想要"读完材料给出结论"走 RAG。实际落地中很多企业两套入口并行。

## 相关 RAG 资源

RAG 相关优化技术与 LLM Wiki 形成互补：

- [[wiki/sources/rag-basis-concepts-javaguide]] — 万字详解 RAG 基础概念 (JavaGuide)
- [[wiki/sources/rag-common-issues-and-optimization]] — RAG 全链路优化指南
- [[wiki/sources/rag-vs-semantic-cache-comparison]] — 语义缓存 vs RAG 对比
- [[wiki/sources/ragas-evaluation-metrics]] — RAGAS 评估体系
- [[wiki/concepts/rag-optimization]] — RAG 优化概念页

更多综合：[[wiki/syntheses/rag-optimization-guide]]

## 来源

- [[wiki/sources/llm-wiki-pattern]]
- [[wiki/sources/karpathy-llm-wiki-philosophy]]
