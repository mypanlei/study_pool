---
title: "记忆系统设计 — 菜鸟教程"
tags:
  - source
  - memory
  - short-term-memory
  - long-term-memory
  - vector-database
  - history-management
  - compression
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/ai-agent-memory-system-design.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# 记忆系统设计

> 系统介绍 AI Agent 记忆系统设计，涵盖短期记忆（工作台/对话上下文）、长期记忆（向量数据库持久化）、对话历史管理（时间衰减/相关性选择/混合策略）、历史压缩（LLM 摘要/增量总结）、以及记忆生命周期管理（重要性评估/聚类压缩/定期清理）。

## 核心内容

1. **短期记忆（ShortTermMemory）** — 存储当前对话上下文和临时信息，容量有限（通常 10-20 轮），对话结束后清除或压缩，含 Python 类实现。
2. **长期记忆（LongTermMemory）** — 基于向量数据库（ChromaDB + SentenceTransformer）持久化存储，通过语义相似度检索，含 VectorMemory 类和 AgentWithMemory 完整示例。
3. **对话历史管理** — 上下文长度限制挑战，智能历史选择策略：时间衰减、相关性选择（embedding 相似度）、混合选择策略、SmartHistorySelector 实现。
4. **历史压缩（HistoryCompressor）** — 使用 LLM 生成对话摘要，保留核心信息，配合最近 1-2 轮对话保持连贯性。
5. **记忆压缩策略** — 基于重要性压缩（ImportanceBasedCompressor）、基于聚类压缩（ClusterBasedCompressor + KMeans）、增量总结（IncrementalSummarizer 每 N 轮总结一次）。
6. **记忆生命周期管理** — MemoryLifecycleManager 统一管理短期→长期→压缩→清理全流程，重要性评估决定存储策略，定期维护清理旧的低重要性记忆。

## 关键概念

- 短期记忆 = Agent 的工作台（顺序访问），长期记忆 = Agent 的档案室（检索式访问）
- 向量数据库（ChromaDB） + Embedding 模型（paraphrase-multilingual-MiniLM-L12-v2）实现语义检索
- 混合搜索结合向量相似度和关键词匹配，提高检索精度
