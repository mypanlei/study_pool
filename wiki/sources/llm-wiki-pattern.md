---
title: "LLM Wiki Pattern — 用 LLM 构建个人知识库"
tags:
  - source
  - methodology
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
source_author: "Andrej Karpathy"
source_date: 2026
---

# LLM Wiki Pattern — 用 LLM 构建个人知识库

> 核心洞见：不要用 LLM 做传统 RAG（每次查询重新发现知识），而是让 LLM **增量构建和维护一个持久的维基** — 结构化的、互相链接的 Markdown 文件集合，作为用户与原始资料之间的中间层。

## 核心论点

1. **持久知识积累** — 传统 RAG 每次查询都从零合成，没有积累。LLM Wiki 将知识「编译」一次后持续维护，综合结果会随每次 Ingest 不断丰富。
2. **三层架构** — 原始资料层（不可变）→ 维基层（LLM 全权维护）→ Schema 层（定义结构和约定），层次清晰，职责分离。
3. **人机分工** — 人类负责策展来源、引导分析、提出好问题；LLM 负责所有「苦力活」— 总结、交叉引用、归档、维护一致性。
4. **答案也是知识** — 好的查询回答可以归档回维基成为新页面，让探索成果也沉淀到知识库中。
5. **零维护成本** — 维基维护（更新交叉引用、保持摘要更新、标记矛盾）是人工维基最大的负担，但对 LLM 来说成本几乎为零。

## 关键概念

- **RAG vs Wiki**：RAG 是无状态的检索-生成；Wiki 是有状态的持久化积累
- **Memex (1945)**：Vannevar Bush 设想的人个知识存储设备，LLM Wiki 是其现代实现 — 解决了「谁来维护」的问题
- **Schema 驱动**：通过 CLAUDE.md / AGENTS.md 等配置文件让 LLM 成为有纪律的维基维护者

## 工作流三件套

| 操作 | 触发条件 | 内容 |
|------|----------|------|
| **Ingest** | 添加新源材料 | 阅读→讨论→写摘要→更新相关页面→更新索引→记录日志 |
| **Query** | 用户提问 | 读索引→深入阅读→综合回答→归档好答案 |
| **Lint** | 定期/按需 | 检查矛盾、过时内容、孤儿页、缺口、交叉引用 |

## 推荐工具栈

- **Obsidian**：作为维基的 IDE（Graph View, Dataview, Marp, Web Clipper）
- **qmd**：本地 Markdown 搜索引擎，支持 BM25/向量混合搜索 + LLM 重排序
- **Git**：版本历史、分支、协作能力免费获得

## 个人思考

- 这个模式的关键不在于「用 LLM 写笔记」— 而在于**让知识积累产生复利效应**。每篇新文章都在已有基础上建设，而不是每次重新开始。
- 与 Zettelkasten 理念有相通之处：原子化笔记、强调链接、从下到上的知识涌现。但 LLM Wiki 通过 LLM 消除了维护成本。
- 需要警惕的是「垃圾进垃圾出」— 如果源材料质量不高，LLM 可能会强化错误的主张。人类对来源的策展至关重要。

## 受影响的 Wiki 页面

- [[wiki/concepts/llm-wiki-pattern]] — 已创建
- [[wiki/entities/andrej-karpathy]] — 已创建
- [[wiki/concepts/memex]] — 已创建
- [[wiki/concepts/rag-vs-wiki]] — 已创建
