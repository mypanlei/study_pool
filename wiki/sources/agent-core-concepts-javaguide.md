---
title: "AI Agent 核心概念全景 — JavaGuide"
tags:
  - source
  - agent
  - javaguide
  - react
  - plan-execute
  - a2a
  - agentic-workflows
created: 2026-06-19
updated: 2026-06-19
source_url: "https://javaguide.cn/ai/agent/agent-basis.html"
source_author: "JavaGuide (Guide)"
source_date: 2026-06-07
---

# AI Agent 核心概念全景

> JavaGuide 出品的 AI Agent 核心概念深度文章（~7000 字），系统梳理 Agent 从聊天机器人到常驻自治系统的演进历程，对比 Agent/传统编程/Workflow 的区别，详解 Agent Loop、ReAct、Plan-and-Execute、Reflection、Multi-Agent、A2A 及 Agentic Workflows 等核心范式。

## 核心论点

1. **Agent 演进四阶段** — 2022 对话式 → 2023 Function Calling + RAG → 2024 标准化(MCP) + 多模态 → 2025-2026 长任务执行 + Skills + Harness Engineering
2. **Agent = LLM + Planning + Memory + Tools** — 四个核心组件缺一不可，缺少 Tools 停留在"给建议"，缺少 Memory 长任务会失忆
3. **Agent 三层能力栈** — LLM Call（模型调用）、Tools Call（Function Calling / MCP / Skills）、Context Engineering（上下文管理），Context Engineering 最容易被低估
4. **Agent vs Workflow 选型标准** — 执行路径能确定用 Workflow，不能确定用 Agent，两者混合用 Agentic Workflows

## 核心内容

### Agent 核心范式对比

| 范式 | 适用场景 | 代价 |
|------|----------|------|
| **AI Workflow (Graph)** | 执行路径可提前确定 | 稳定可观测，前期设计成本高 |
| **ReAct** | 路径不确定，需动态规划 | 灵活，Token 消耗高，调试难 |
| **Plan-and-Execute** | 长任务步骤多但结构清晰 | 不易迷路，动态调整弱 |
| **Reflection** | 输出质量要求高 | 和 ReAct/P&E 配合使用 |
| **Multi-Agent** | 任务可拆成多个专业角色 | 通信和调试成本翻倍 |
| **Agentic Workflows** | 长任务 + 部分子任务不可预测 | 全局 Workflow + 局部 ReAct 嵌套 |

### Tools 注册与调用

- **数据格式**：OpenAI Function Calling Schema（JSON Schema 描述）
- **通信接入**：MCP 协议（基于 JSON-RPC 2.0）
- **进阶封装**：Agent Skills（SKILL.md 渐进披露 + 延迟加载）
- **关键细节**：工具描述写得好不好直接影响 Agent 判断

### A2A 协议定位

A2A 是 Agent 之间的接口契约，类比后端微服务的 RESTful/RPC。Agent 之间用结构化数据交互而非自然语言，降低 Token 消耗和解析错误。

## 与现有知识的关系

- 与 [[wiki/sources/ai-agent-architecture-overview]] 互为补充，本文侧重演进与选型决策
- 与 [[wiki/sources/ai-agent-working-principle]] 的 ReAct 循环描述一致
- 与 [[wiki/concepts/react-reasoning-acting]] 和 [[wiki/concepts/mcp-model-context-protocol]] 概念内容一致

## 受影响的 Wiki 页面

- [[wiki/concepts/react-reasoning-acting]] — 已补充新来源引用
- [[wiki/concepts/mcp-model-context-protocol]] — 已补充新来源引用
