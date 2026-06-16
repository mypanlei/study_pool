---
title: "AI Agent 工作原理 — 菜鸟教程"
tags:
  - source
  - agent
  - tutorial
  - working-principle
  - react
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/ai-agent-working-principle.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# AI Agent 工作原理

> 用餐厅经营比喻详细解释 AI Agent 的三大核心组成（大脑、工具、记忆），并通过完整的 ReAct 循环示例和 Python 代码实践演示 Agent 的工作流程。

## 核心内容

1. **三大核心组成** — 大脑（LLM）= 决策中心、工具（Tools）= 可执行动作、记忆（Memory）= 经验存储。
2. **Agent 类型** — 反应式、目标导向、实用型、学习型、多智能体系统。
3. **ReAct 循环详解** — 思考(Think)→行动(Act)→观察(Observe)→再思考的迭代机制，通过"查找北京意大利餐厅"示例完整展示。
4. **Python 实现** — 感知模块、决策模块、行动模块、记忆模块、工具模块的分离实现，以及完整的命令行 AI Agent 示例。

## 关键概念

- LLM 只能"说"，Agent 能"做"
- 模块分离：感知/决策/行动/记忆/工具
- 实践练习：构建一个能查天气和做计算的命令行 Agent
