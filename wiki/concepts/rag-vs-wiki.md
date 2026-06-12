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

## 来源

- [[wiki/sources/llm-wiki-pattern]]
