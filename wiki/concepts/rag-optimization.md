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

## RAG 演进阶段

RAG 历经三个阶段逐步走向成熟：

| 阶段 | 典型链路 | 特点 |
|------|---------|------|
| **Naive RAG** | 文档切块 → Embedding → Top-K 检索 → LLM 生成 | 最基础，适合 Demo |
| **Advanced RAG** | Query Rewrite/HyDE → 混合检索 → Rerank → 上下文压缩 → LLM 生成 | 解决召回不准和噪声 |
| **Modular RAG** | 检索器/重排器/压缩器/路由器/生成器可插拔组合 | 生产系统和复杂 Agent |

> Naive RAG 能跑通 Demo 但离生产通常还有距离。Advanced RAG 是生产最低要求，Modular RAG 适合复杂 Agent 场景。

## RAG 核心优势与局限

**优势**:
- 知识更新成本低（换索引即可，无需重新训练）
- 减少幻觉 + 可追溯来源（回答可挂到具体文档片段）
- 数据隔离易做（检索层 ACL / 多租户隔离）
- 换领域成本低（重建知识库即可）

**局限**:
- 检索质量决定上限（GIGO 原则：Embedding 不准或分块策略丢信息则无法挽回）
- 上下文噪声干扰（"Lost in the Middle"问题）
- 延迟高（查询改写 → 向量化 → 检索 → 重排 → 上下文构建 → LLM 生成）
- 工程复杂度高（向量库/增量索引/权限过滤/引用溯源/评测闭环）
- Token 成本（每次请求带上下文，输入 Token 远高于普通对话）

## 相关概念

- [[wiki/concepts/rag-vs-wiki]] — RAG 与持久化 Wiki 的对比
- [[wiki/concepts/llm-wiki-pattern]] — LLM Wiki 作为 RAG 的替代/补充
- [[wiki/concepts/embedding]] — Embedding 嵌入与向量化
- [[wiki/concepts/fine-tuning]] — RAG vs 微调

## 来源

- [[wiki/sources/rag-basis-concepts-javaguide]] — 万字详解 RAG 基础概念 (JavaGuide)
- [[wiki/sources/rag-common-issues-and-optimization]]
- [[wiki/sources/rag-vs-semantic-cache-comparison]]
- [[wiki/sources/ragas-evaluation-metrics]]
- [[wiki/sources/karpathy-llm-wiki-philosophy]]
