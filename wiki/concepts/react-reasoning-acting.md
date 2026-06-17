---
title: "ReAct (Reasoning + Acting)"
tags:
  - concept
  - react
  - agent-pattern
  - reasoning
  - agent
created: 2026-06-18
updated: 2026-06-18
aliases:
  - ReAct 模式
  - Reasoning + Acting
  - ReAct 循环
  - Think-Act-Observe
---

# ReAct (Reasoning + Acting)

## 定义

ReAct（Reasoning + Acting）是一种将推理（Reasoning）与行动（Acting）交织在一起的 Agent 行为模式。由 Shunyu Yao 等人于 2022 年提出，核心思想是让 LLM 在**思考（Thought）→ 行动（Act）→ 观察（Observation）**之间循环迭代，每一步推理都基于上一步的观察结果，形成动态的反馈闭环。

ReAct 是目前最广泛使用的 Agent 基础模式，几乎所有主流 Agent 框架（LangGraph、AutoGen、CrewAI、Claude Code 等）都以 ReAct 作为核心循环。

## 核心要点

- **Thought（思考）**：LLM 分析当前状态，决定下一步做什么
- **Act（行动）**：执行一个具体动作（调用工具、查询数据库、搜索网页等）
- **Observe（观察）**：获取行动的结果反馈，更新上下文
- **循环终止**：当 LLM 判断任务已完成或无法继续时，输出最终答案
- **与 CoT 的关系**：ReAct = CoT（推理链）+ 工具调用（行动），CoT 只在"头脑中"推理，ReAct 通过与外部世界交互来验证推理

## 详细阐述

### 背景

传统 LLM 的推理（Chain of Thought）仅在文本空间内进行，无法感知外部环境。而纯行为式的 Agent（如早期的对话机器人）缺乏推理能力，容易陷入错误循环。ReAct 将两者结合，让 Agent 既能思考策略，又能通过行动获取真实世界反馈。

### ReAct 循环

```
用户提问
  │
  ▼
┌─────────────────────────────────┐
│  Thought: "我需要先搜索信息"     │  ← 推理
│  Act: search("关键词")          │  ← 行动
│  Observation: <搜索结果>        │  ← 反馈
│  Thought: "现在我需要分析结果"   │  ← 推理
│  Act: call_analysis_tool()     │  ← 行动
│  Observation: <分析结果>        │  ← 反馈
│  Thought: "任务完成，可以回答"   │  ← 推理
│  Final Answer: <最终答案>       │  ← 输出
└─────────────────────────────────┘
```

### 优缺点

| 优势 | 缺点 |
|------|------|
| 动态适应环境变化 | 上下文易随步骤累积膨胀 |
| 可追踪推理过程（可解释性） | 多步后可能偏离主线 |
| 支持复杂多步任务 | 工具调用失败时可能循环 |
| 灵活组合多种工具 | 需精心设计 System Prompt 约束行为 |

### ReAct 变体

- **标准 ReAct**：Thought → Act → Observe 循环
- **Plan & Execute**：先规划完整步骤，再逐执行（适合确定性任务）
- **Reflexion**：在 ReAct 基础上加入自我反思，回顾历史错误
- **Tree-of-Thoughts ReAct**：多路径并行 ReAct，树状搜索最佳路径

### 在主流框架中的实现

| 框架 | ReAct 实现方式 |
|------|---------------|
| LangGraph | `create_react_agent()` + StateGraph 状态机构建循环 |
| AutoGen | AssistantAgent + UserProxyAgent 的对话式 ReAct |
| CrewAI | 角色化 Agent 内部使用 ReAct 循环 |
| Claude Code | 内置 ReAct 循环（思考→工具调用→观察→再思考） |
| OpenAI Assistants | Function Calling + Run 循环实现 ReAct |

## 相关概念

- [[wiki/concepts/cot-chain-of-thought]] — CoT 纯文本推理，ReAct 在 CoT 基础上增加工具调用
- [[wiki/concepts/mcp-model-context-protocol]] — MCP 提供 ReAct 循环中"行动"步骤所需的工具接口
- [[wiki/concepts/prompt-engineering]] — Prompt Engineering 设计 ReAct 循环的 System Prompt
- [[wiki/concepts/harness-engineering]] — Harness 为 ReAct 循环提供约束和护栏

## 来源

- [[wiki/sources/ai-agent-working-principle]] — 菜鸟教程 ReAct 循环详解与 Python 实现
- [[wiki/sources/reasoning-and-planning]] — 菜鸟教程推理与规划框架对比
- [[wiki/sources/ai-agent-core-components]] — Agent 核心组件中的 ReAct 模式
- [[wiki/sources/agent-architecture-patterns]] — 6 种 Agent 架构中的 ReAct 循环
- [[wiki/sources/langgraph-react-agent-guide]] — LangGraph ReAct Agent 工程化实现
- [[wiki/sources/python-reasoning-planning-implementation]] — ReAct Python 实现代码
