---
title: "Agent 架构 — 菜鸟教程"
tags:
  - source
  - agent
  - architecture
  - patterns
  - multi-agent
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/agent-architecture.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Agent 架构

> 系统介绍六种主流 Agent 架构：单 Agent 循环、规划+执行、多 Agent 协作、反思与自我修正、RAG+Agent、工作流编排（DAG），含图解、代码示例和选型指南。

## 核心内容

1. **单 Agent 循环 (Single Agent Loop)** — 最基础的 ReAct 模式，实现简单但上下文窗口容易溢满。
2. **规划+执行 (Plan & Execute)** — 先规划再执行，支持静态/动态两种变体，可人工审查计划。
3. **多 Agent 协作 (Multi-Agent)** — Orchestrator + Subagent 模式，天然支持并行，上下文隔离。
4. **反思与自我修正 (Reflection)** — 执行器 + 评判者 + 修正器，自我/独立 Critic 两种实现。
5. **RAG + Agent** — Agent 自主判断检索时机和内容，检索增强推理。
6. **工作流编排 (Workflow/DAG)** — 预定义有向无环图，高可预测性但灵活性低。

## 选型指导

- 架构越简单越好（从单 Agent 循环开始）
- 上下文不够时考虑多 Agent，质量不够时加入反思
- 流程稳定后重构为 DAG 提升可靠性
- 常见组合：DAG + 多 Agent、多 Agent + RAG、规划执行 + 反思
