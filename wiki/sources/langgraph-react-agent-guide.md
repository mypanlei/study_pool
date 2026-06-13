---
title: "LangGraph ReAct Agent 实战指南 — 状态机驱动的 Agent 工程化"
tags:
  - source
  - langgraph
  - agent
  - react
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://langchain-ai.github.io/langgraph/"
source_author: "自建知识库笔记"
source_date: 2026-03-19
---

# LangGraph ReAct Agent 实战指南

> LangGraph 通过状态机思想将 ReAct 模式工程化，解决了传统 Chain 难以处理的循环（Loop）问题。

## 核心论点

1. **运行逻辑** — Agent Node（思考并决定）→ Tools Node（执行并返回观察结果）→ Agent Node（循环），直到无需工具直接回复。
2. **核心概念** — State（流转数据结构）、Nodes（执行逻辑的函数）、Edges（节点路径）、Conditional Edges（根据状态决策下一步）。
3. **两种实现方案** — 高层封装 `create_react_agent`（推荐，一行代码构建完整 ReAct 图）和底层构建 `StateGraph`（深度定制，精细控制状态更新）。
4. **记忆管理** — 短期记忆通过 Checkpointer 实现（`thread_id` 隔离会话）；长期记忆需设计记忆节点联动向量数据库。
5. **选择 LangGraph 的理由** — 可控性好（每一步可见可修改）、原生持久化（Checkpointer 实现中断恢复）、循环处理工程化（递归边）。

## 受影响的 Wiki 页面

- [[wiki/entities/langgraph]] — 已创建
- [[wiki/concepts/agent-skills-system]] — 已关联
