---
title: "AI Agent 架构与框架全景指南 — 核心模式与选型框架"
tags:
  - source
  - agent
  - architecture
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "internal note"
source_author: "自建知识库笔记"
source_date: 2026-04-11
---

# AI Agent 架构与框架全景指南

> 从 ReAct、Plan-and-Execute 到混合架构，系统梳理 Agent 核心模式，并横向对比 2025-2026 年主流开发框架。

## 核心论点

1. **ReAct (Reasoning + Acting)** — 将推理和行动合并到一个循环中，模型生成 Thought → Action → Observation，自适应强但易陷入无限循环。
2. **Plan-and-Execute** — 将高层目标分解为原子化步骤列表，由 Planner 规划和 Re-planner 动态调整，逻辑严密但响应延迟较高。
3. **混合架构 (P&E + ReAct)** — Plan-and-Execute 做宏观调度，ReAct 做局部执行器，兼具鲁棒性、可解释性和 Token 优化。
4. **2025 主流框架对比** — LangGraph（状态机/图架构）、CrewAI（角色驱动协作）、LlamaIndex（RAG 增强）、AutoGen（对话式多 Agent）、Pydantic AI（类型安全）、Mastra（TS 原生）各有侧重。

## 关键概念

- **Reflexion**：执行后自我反思，根据失败经验修正策略
- **Tree of Thoughts**：探索多条推理分支并评分择优
- **Prompt Chaining**：固定的线性多步 Prompt 传递
- **Routing**：预分类意图后路由到专门 Agent

## 选型建议

- 需要严密逻辑控制 → LangGraph
- 快速搭建多角色团队 → CrewAI
- 核心场景是查文档 RAG → LlamaIndex
- 构建高度确定性 Pipeline → Prompt Chaining 或 Routing

## 受影响的 Wiki 页面

- [[wiki/entities/langgraph]] — 已创建
- [[wiki/concepts/agent-skills-system]] — 已关联
