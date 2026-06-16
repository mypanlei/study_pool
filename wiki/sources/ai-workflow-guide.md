---
title: "AI Workflow（AI 工作流） — 菜鸟教程"
tags:
  - source
  - ai-workflow
  - workflow
  - agent
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/ai-workflow.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# AI Workflow（AI 工作流）

> 系统介绍 AI Workflow 的概念、核心组成要素（LLM、工具、记忆、状态、路由、人工介入）、六大常见设计模式（顺序链、条件路由、并行执行、ReAct 循环、Plan & Execute、多智能体协作）、主流框架对比（LangChain/LangGraph/LlamaIndex/Dify/n8n/CrewAI）及框架选型决策树。

## 核心内容

1. **核心组成要素** — LLM（大脑）、工具（接口）、记忆（短期/长期）、状态（信息载体）、路由（条件分支）、人工介入（高风险暂停）。
2. **六大模式** — 顺序链（线性）、条件路由（动态分支）、并行执行（并发子任务）、ReAct 循环（推理+行动循环）、Plan & Execute（先规划再执行）、多 Agent 协作（协调者+专职 Agent）。
3. **主流框架对比** — LangChain（生态最大）、LangGraph（图状有状态）、LlamaIndex（RAG 专精）、Dify（可视化低代码）、n8n（通用自动化）、CrewAI（多 Agent 协作），附框架选型决策树。
4. **代码示例** — LangChain 顺序链（管道操作符）、ReAct Agent 工具调用、LangGraph 有状态工作流、CrewAI 多 Agent 协作、Human-in-the-Loop 人工审核节点。
5. **陷阱与最佳实践** — 幻觉级联、无限循环、上下文爆炸、工具滥用、JSON 解析失败、费用超支、并发冲突。

## 关键概念

- AI Workflow = 将多个 AI 调用、工具使用、数据处理步骤有序组合成自动化流水线
- 单次 LLM 调用如同工匠，AI Workflow 如同整条流水线
- 从中等复杂度程度开始（如 LangChain / CrewAI），非技术背景可选用 Dify / n8n
