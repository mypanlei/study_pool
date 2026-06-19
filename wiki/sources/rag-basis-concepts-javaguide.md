---
title: "万字详解 RAG 基础概念 — JavaGuide"
tags:
  - source
  - rag
  - retrieval-augmented-generation
  - javaguide
created: 2026-06-19
updated: 2026-06-19
aliases:
  - RAG 基础概念
  - RAG 万字详解
source: "https://javaguide.cn/ai/rag/rag-basis.html"
author: "Guide (JavaGuide)"
---

# 万字详解 RAG 基础概念 — JavaGuide

> JavaGuide 出品的 RAG 基础概念深度解析，2026-05-25 发布。文章约 6200 字，从 RAG 定义出发，系统覆盖 Embedding、相似度度量、RAG vs 微调、RAG vs 长上下文、RAG vs 传统搜索、RAG 演化阶段、核心优势与局限性等高频面试考点。

## 核心贡献

### 1. RAG 定义与核心价值
- **RAG** = Retrieval-Augmented Generation = 检索 + 增强 + 生成
- 解决 LLM 三大核心挑战：知识时效性、私有数据访问、幻觉问题
- 不是让模型"更神"，而是把回答拉回到可检索、可引用、可审计的证据上

### 2. RAG vs 传统搜索
- **传统搜索** → 排序器（给文档列表，用户点开自己判断）
- **RAG** → 信息综合器（跨文档归纳整合，生成直接可读答案）
- 选型判断：用户想要"帮我找到材料"还是"帮我读完材料并给出结论"
- 最佳实践：**简单查找走搜索，复杂问答走 RAG** — 两套入口并行

### 3. RAG vs 微调
- **RAG** → 解决"模型不知道新知识/私有知识"（知识库更新成本低）
- **微调** → 解决"模型不会按你的方式说话做事"（风格/格式/术语对齐）
- 两者可结合：微调定领域表达 + RAG 提供实时知识
- 务实建议：资源有限时先把 RAG 做稳，再考虑引入微调

### 4. RAG vs 长上下文
- 长上下文 ≠ 可以取代 RAG
- 长上下文适合：单篇长文档深度分析、长对话总结
- 长上下文不适合：海量知识库（百万级文档片段）、权限隔离、"Lost in the Middle"问题、可追溯性要求

### 5. Embedding 与相似度度量
- **Embedding**：将文本映射到高维稠密向量空间，语义接近 → 向量距离近
- **常见模型**：OpenAI text-embedding-3-small (1536维)、BGE、GTE、E5 系列
- **三种度量方式**：余弦相似度（最常用，对长度不敏感）、内积（L2归一化后等价于余弦）、欧氏距离（对幅度敏感）

### 6. RAG 演进三阶段
| 阶段 | 典型链路 | 特点 |
|------|---------|------|
| **Naive RAG** | 文档切块 → Embedding → Top-K 检索 → LLM 生成 | 最基础，适合 Demo |
| **Advanced RAG** | Query Rewrite/HyDE → 混合检索 → Rerank → 上下文压缩 → LLM 生成 | 解决召回不准和噪声 |
| **Modular RAG** | 检索器/重排器/压缩器/路由器/生成器可插拔组合 | 生产系统和复杂 Agent |

### 7. RAG 优势与局限

**优势**:
- 知识更新成本低（换索引即可，无需重新训练）
- 减少幻觉 + 可追溯来源
- 数据隔离易做（检索层 ACL）
- 换领域成本低

**局限**:
- 检索质量决定上限（GIGO 原则）
- 上下文噪声稀释注意力
- 延迟高（完整链路多个步骤）
- 工程复杂度高（向量库/增量索引/权限/评测闭环）
- Token 成本（每次请求带上下文）

## 关键洞察

- **Demo ≠ 生产可用**：RAG 最难的部分不是接一个向量库，而是持续评估和优化召回质量
- **面试常考点**：RAG 定义、与传统搜索区别、与微调的选型、Embedding 选择、相似度度量选择、幻觉问题、"Lost in the Middle"、长上下文 vs RAG、评估指标、优势与局限
- 文章最后推荐了实战项目：**interview-guide**（Spring Boot 4.0 + Spring AI + pgvector 的 RAG 面试平台）

## 相关页面

- [[wiki/concepts/embedding]] — Embedding 嵌入与向量化
- [[wiki/concepts/rag-optimization]] — RAG 全链路优化
- [[wiki/concepts/fine-tuning]] — 微调
- [[wiki/concepts/rag-vs-wiki]] — RAG vs Wiki 对比
- [[wiki/concepts/rerank]] — Rerank 重排序
- [[wiki/concepts/graphrag]] — GraphRAG
- [[wiki/syntheses/rag-optimization-guide]] — RAG 优化指南
