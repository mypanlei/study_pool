---
title: "AI Agent 核心组件 — 菜鸟教程"
tags:
  - source
  - agent
  - architecture
  - components
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/ai-agent-core.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# AI Agent 核心组件

> 以"智能餐厅"类比系统介绍 AI Agent 的五大核心组件：感知层、大脑、工具、记忆、规划，以及 Agent Loop 的完整运行机制。

## 核心内容

1. **感知层 (Perception)** — 多模态输入接收（文本、图像、结构化数据、环境状态、工具返回结果）。
2. **大脑 (Brain/LLM)** — 意图理解、推理决策、工具调用判断。
3. **工具 (Tools)** — 四大类：信息获取、计算执行、内容生成、系统交互。
4. **记忆 (Memory)** — 短期记忆（In-Context）、长期记忆（向量数据库）、情节记忆、语义记忆 + RAG。
5. **规划 (Planning)** — CoT、ReAct、ToT、Reflection 四种主流策略。
6. **Agent Loop** — 感知→思考→行动→观察的持续迭代闭环。

## 关键概念

- 函数调用（Function Calling）机制
- RAG 作为最主流的长期记忆实现方案
- 五大组件一览表（类比、职责、关键技术）
