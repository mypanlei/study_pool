---
title: "Loop Engineering（循环工程） — 菜鸟教程"
tags:
  - source
  - loop-engineering
  - agent
  - prompt-engineering
  - context-engineering
  - harness-engineering
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/loop-engineering.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Loop Engineering（循环工程）

> 介绍 Loop Engineering（循环工程）的概念、起源和六大要素。由 Addy Osmani 系统整理，Boris Cherny 和 Peter Steinberger 推动，代表 AI 编程从 Prompt→Context→Harness→Loop 的第四次范式跃迁。

## 核心内容

1. **工程范式演进** — Prompt Engineering（怎么问）→ Context Engineering（给什么信息）→ Harness Engineering（如何组织能力）→ Loop Engineering（如何让 AI 持续创造结果）。
2. **Loop 核心循环** — 意图（Intent）→ 上下文（Context）→ 行动（Action）→ 观察（Observation）→ 调整（Adjustment）。
3. **六大要素** — 自动触发器（Automations/定时调度）、并行隔离（Worktrees）、技能文件（Skills/SKILL.md）、连接器（Connectors/MCP）、子 Agent（Sub-Agents/制作者-检查者模式）、持久记忆（Memory/文件状态）。
4. **五种 Loop 模式** — 测试驱动（Test-driven）、编译器驱动（Type-driven）、Review 驱动、运行时调试（Runtime-debug）、产品迭代（UI-driven）。
5. **Loop 构建四步法** — 窄任务开始→明确验证方式→设置保险机制→逐步提升自主程度。
6. **三大风险** — 验证仍是你的责任、理解债积累更快、认知投降。

## 关键概念

- "你不应该再手动提示 AI 编程助手了，你应该设计让 Agent 自己提示自己的 Loop"
- Loop Engineering 在外循环层工作（你设计的系统），Agent 内循环负责（感知→推理→行动→观察）
- 从只读 Loop 开始（只写 TODO.md，不碰源码），逐步提升自主程度
