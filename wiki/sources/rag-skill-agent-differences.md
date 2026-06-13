---
title: "RAG、Skill、Agent 的区别与联系 — 三层能力体系与组合判断框架"
tags:
  - source
  - rag
  - skill
  - agent
  - methodology
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "internal note"
source_author: "自建知识库笔记"
source_date: 2026-05-29
---

# RAG、Skill、Agent 的区别与联系

> RAG 解决知识获取，Skill 解决方法固化，Agent 解决任务执行。三者不是同一层级的概念，可以独立存在，也可以组合使用。

## 核心论点

1. **RAG** — Retrieval-Augmented Generation，解决「模型如何获得外部知识」的问题。关键组件：文档切分、Embedding、向量检索、Rerank、上下文拼接。
2. **Skill** — Agent 的可复用能力包/流程手册，解决「Agent 如何按固定方法做某类事」的问题。本身不主动执行，由 Agent 在需要时读取。
3. **Agent** — 围绕目标自主完成任务的执行系统，由 Model + Tools + Instructions/Memory/Context 构成，解决「如何围绕目标自主规划并完成任务」。
4. **常见误区** — 有 RAG 不一定是 Agent（可能只是增强问答）；Skill 不是小 Agent（Skill 本身不会思考调用工具）；Agent 不一定需要 RAG（可只依赖代码库和工具结果）。
5. **组合使用** — Agent 执行任务 → Skill 规定流程 → RAG 提供知识 → Tools 执行外部动作 → 最终产出结果。

## 判断框架

- 缺知识 → RAG
- 缺流程 → Skill
- 缺执行闭环 → Agent

## 受影响的 Wiki 页面

- [[wiki/concepts/agent-skills-system]] — 已更新
- [[wiki/concepts/rag-vs-wiki]] — 已关联
