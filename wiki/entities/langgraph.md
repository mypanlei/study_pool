---
title: "LangGraph"
tags:
  - entity
  - agent
  - framework
  - ai
created: 2026-06-13
updated: 2026-06-13
aliases:
  - LangGraph Framework
---

# LangGraph

> LangChain 推出的低层 Agent 编排框架，通过状态机（State Machine）思想工程化 ReAct 模式，适合长运行、强状态、复杂控制的 Agent 系统。

## 关键信息

- **类型**: 低层 Agent 编排框架（orchestration framework and runtime）
- **开发商**: LangChain
- **核心定位**: 构建、管理和部署长运行、有状态 Agent
- **语言**: Python / JavaScript
- **开源**: 是

## 核心特色

| 特性 | 描述 |
|------|------|
| 状态机架构 | State + Nodes + Edges + Conditional Edges |
| 持久化 | Checkpointer 机制，原生支持会话中断恢复 |
| 记忆管理 | 短期（thread-level）和长期（cross-thread）记忆 |
| Human-in-the-loop | 人工介入节点 |
| 多 Agent 协作 | 支持图工作流编排 |

## 实现方式

- **高层封装**: `create_react_agent` — 一行代码构建标准 ReAct 循环
- **底层构建**: `StateGraph` — 精细控制状态更新和多 Agent 协作

## 在 Agent 平台生态中的位置

LangGraph 位于 **编排与 runtime 层**。比 Gemini/Dify（应用交付层）更低层，比 Kubeflow（基础设施层）更高层。适合精细编排长流程、长状态、多 Agent runtime 的团队。

## 来源

- [[wiki/sources/langgraph-react-agent-guide]]
- [[wiki/sources/gemini-kubeflow-dify-langgraph-comparison]]
- [[wiki/sources/ai-agent-architecture-overview]]
