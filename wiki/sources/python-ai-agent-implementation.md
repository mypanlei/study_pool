---
title: "Python 实现 AI Agent — 菜鸟教程"
tags:
  - source
  - python
  - agent
  - implementation
  - tutorial
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/python-ai-agent.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Python 实现 AI Agent

> Python 从零实现 AI Agent 的实战教程。涵盖 Agent 核心架构（大脑/感知/行动/目标）、极简 Agent 原型（含 LLM 抽象/记忆/工具注册/规划器/执行器）、以及任务规划助手的完整构建过程。

## 核心内容

1. **Agent 核心架构** — 大脑（LLM 推理决策）、感知（输入获取）、行动（工具调用）、目标（任务驱动）。
2. **极简 Agent 原型** — Memory（短期/长期记忆）、LLMInterface（可替换的 LLM 抽象）、ToolRegistry（工具注册与调用）、SimplePlanner（任务分解）、Executor（步骤执行）。
3. **任务规划助手实战** — AgentBrain（OpenAI/DeepSeek API 封装）、AgentTools（搜索/计划/时间/计算工具）、SimpleAgent（感知-思考-行动循环）。
4. **核心工作流程** — 解析意图 → 规划步骤 → 选择工具 → 执行行动 → 观察结果 → 生成最终回复。
5. **实践练习** — 增加记忆功能、实现自动工具选择（JSON 格式解析）、添加新工具（待办事项）。

## 关键概念

- Agent = 大脑（LLM）+ 感知 + 行动 + 目标
- 感知-思考-行动循环是 Agent 最基础的工作模式
- LLM 抽象层是可替换点，可对接 OpenAI/Claude/DeepSeek/本地模型
