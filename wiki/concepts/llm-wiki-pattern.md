---
title: "LLM Wiki Pattern"
tags:
  - concept
  - methodology
  - active
created: 2026-06-13
updated: 2026-06-13
aliases:
  - LLM 维基模式
  - LLM Wiki
---

# LLM Wiki Pattern

> 由 Andrej Karpathy 提出的知识管理模式：让 LLM 增量构建和维护持久的、结构化的 Markdown 维基，而非每次查询从零合成知识。

## 定义

LLM Wiki 是一种知识管理架构，核心思路是将知识「编译」到持久维基中并持续维护，而不是每次查询时从原始文档重新检索和合成。它通过三层架构（原始资料 → 维基 → Schema）实现知识复利效应。

## 核心原则

1. **持久化积累** — 知识被一次编译、持续维护，而非每次重新发现
2. **三层分离** — 原始资料（不可变）↔ 维基（LLM 维护）↔ Schema（人类定规则）
3. **人机分工** — 人类策展 + 引导，LLM 执行 + 维护
4. **答案即知识** — 有价值的查询回答被归档为 Wiki 新页面
5. **零边际维护成本** — LLM 处理所有书签工作（交叉引用、一致性检查）

## 与 RAG 的对比

| 维度 | 传统 RAG | LLM Wiki |
|------|----------|----------|
| 知识存储 | 无状态，每次查询重新检索 | 有状态，持久化维基 |
| 综合能力 | 每次重新合成，可能遗漏 | 持续累积，综合随每次 Ingest 深化 |
| 维护负担 | 低（无需维护） | 中（LLM 自动维护） |
| 回答速度 | 慢（需检索+合成） | 快（知识已在维基中） |
| 可浏览性 | 差（无法直接浏览知识结构） | 好（可读 Markdown + Graph View） |

## 三工作流

- **Ingest**：源材料 → 阅读 → 讨论 → 写摘要 → 更新相关页 → 更新索引 → 日志
- **Query**：读索引 → 定位页面 → 综合回答 → 可选的答案归档
- **Lint**：周期性健康检查（矛盾、过时、孤儿页、缺口）

## 推荐工具栈

- **Obsidian** — 作为维基 IDE
- **Claude Code / Codex** — 作为维基维护者（LLM Agent）
- **qmd** — 本地搜索引擎（可选，规模大时引入）
- **Git** — 版本控制
- **Dataview** — Obsidian 插件，动态查询 YAML frontmatter

## 来源

- [[wiki/sources/llm-wiki-pattern]]
