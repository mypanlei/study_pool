---
title: "Loop Engineering（循环工程）"
tags:
  - concept
  - loop-engineering
  - agent
  - automation
created: 2026-06-30
updated: 2026-06-30
aliases:
  - 循环工程
  - Agent Loop
  - 工程师循环
---

# Loop Engineering（循环工程）

> 设计让 AI Agent **自己提示自己、自动完成整个工作循环**的工程方法论。代表 AI 编程从 Prompt → Context → Harness → Loop 的第四次范式跃迁。

## 定义

Loop Engineering 是 2026 年兴起的一种 AI 编程范式，核心理念是：**不再由人向 AI 发送指令，而是设计一套系统让 AI 自动循环运行**。它在外循环层工作（你设计的系统），Agent 的内循环负责（感知→推理→行动→观察）。

## 核心要点

- **第四次范式跃迁**：Prompt Engineering（怎么问）→ Context Engineering（给什么信息）→ Harness Engineering（如何组织能力）→ Loop Engineering（如何让 AI 持续创造结果）
- **六大要素**：Automations（自动触发器）+ Worktrees（并行隔离工作空间）+ Skills（SKILL.md）+ Connectors（MCP 连接器）+ Sub-Agents（制作者-检查者模式）+ Memory（持久化文件状态）
- **五种循环模式**：测试驱动 / 类型驱动 / Review 驱动 / 运行时调试 / 聚合循环
- **Loop ≠ Harness**：Harness = 跑得稳（可靠运行），Loop = 跑不停（持续创造结果）
- **停止规则是安全底线**：必须设置 ALL GREEN、轮次上限、重复失败、回归检测、无进展熔断和超出能力检测

## 详细阐述

### 背景

2025-2026 年，AI 编程工具（Claude Code、Codex、Cursor 等）的能力大幅提升，从「辅助写代码」进化为「自主完成编程任务」。人们发现：

1. 手动提示 AI 的边际效益递减 — 重复性提示占用大量时间
2. Agent 能力足够承接完整工作流 — 从写代码到测试到部署
3. 关键在于设计系统而非写指令 — 让 Agent 自行决策和迭代

Boris Cherny（Claude Code 之父）率先提出：「我不再提示 Claude 了，我有一堆循环在运行。」Addy Osmani（Google）系统整理了 Loop Engineering 的理论框架。

### 六大要素详解

| 要素 | 作用 | Claude Code 实现 |
|------|------|-----------------|
| **Automations** | 循环的心跳，设定频率和触发条件 | `/loop` 命令, CronCreate 定时任务 |
| **Worktrees** | 支持并行执行，防止文件冲突 | `EnterWorktree(name="...")` 命令 |
| **Skills** | 持久化项目知识，避免每次从零推导 | `.claude/skills/*` + SKILL.md |
| **Connectors** | 基于 MCP 连接真实工具 | MCP 服务器配置 (`claude.json`) |
| **Sub-Agents** | 将写代码的和检查代码的分开 | `/agent create` 命令 |
| **Memory** | 持久化状态，记录"什么完成了、什么接下来" | PROGRESS.md + Auto Memory |

### Builder/Checker 隔离模式

这是社区公认最重要的设计模式：

- **builder.md**：专职写代码的 Agent，有 Write/Edit 工具权限
- **checker.md**：专职检查代码的 Agent，只有读权限（硬隔离），使用 **独立模型** 审查
- **循环编排器**：通过 `/loop` 命令或外部调度器实现

**关键原则**：验证必须用独立模型，而非执行任务的模型自评 — 这是最容易被忽略的坑。

### 停止规则体系

Loop 的安全底线，应写入 CLAUDE.md：

| 规则 | 触发条件 | 动作 |
|------|---------|------|
| ALL GREEN | 所有检查通过 | 循环正常结束 |
| 轮次用尽 | 达到上限（建议 5 轮） | 强制停止，报告未完成项 |
| 连续重复失败 | 同一失败连续出现 2 轮 | 停止，标记为无法自动修复 |
| 回归 | 修复导致之前通过的检查失败 | 停止，回退到稳定版本 |
| 无实质进展 | 连续 2 轮失败项未减少 | 停止，请求人工介入 |
| 超出能力 | 模型自身判断无法解决 | 停止，输出当前状态供人工接手 |

### 成熟度模型

| Level | 状态 | 特征 |
|-------|------|------|
| **L0** | 纯手动 | 所有操作人工触发，无自动化循环 |
| **L1** | 单 Loop | 一个自动化循环（如自动 Lint），只读报告 |
| **L2** | 多 Loop | 多个并行 Loop，各自独立运行 |
| **L3** | 联动 Loop | Loop 间有依赖关系，一个 Loop 的输出触发另一个 |
| **L4** | 自进化 | Loop 能检测自身效果，自动调整参数和频率 |

### 构建四步法

1. **窄任务开始** — 先跑通一个最简单的 Loop（如自动 Lint）
2. **明确验证方式** — 每个 Loop 必须有明确的成功/失败标准
3. **设置保险机制** — 永远不要让 Loop 在无人确认的情况下修改重要内容
4. **逐步提升自主程度** — 从只读报告 → 建议 → 自动执行

## 与 Harness Engineering 的关系

| 维度 | Harness Engineering | Loop Engineering |
|------|-------------------|-----------------|
| 核心问题 | 如何让 Agent **可靠运行**？ | 如何让 Agent **持续创造结果**？ |
| 关注点 | 基础设施、安全护栏、权限控制 | 自动化循环、触发机制、迭代节奏 |
| 典型组件 | CLAUDE.md, MCP, Hooks, Permissions | `/loop`, CronCreate, Worktree, Auto Memory |
| 设计目标 | 让 Agent 不犯错、不越权、不崩溃 | 让 Agent 自我驱动、持续迭代、渐进改进 |
| 关系 | **基础层** — Agent 的操作系统内核 | **应用层** — Agent 的定时任务调度器 |

## 相关概念

- [[wiki/concepts/harness-engineering]] — 让 Agent 跑得稳的基础设施层
- [[wiki/concepts/wiki-loop-engineering]] — Loop Engineering 在 LLM Wiki 知识库中的具体应用
- [[wiki/concepts/spec-driven-development]] — 与 Loop 配合的规格驱动开发方法论
- [[wiki/concepts/vibe-coding]] — 前一个范式（意图编程）
- [[wiki/concepts/prompt-engineering]] — 更早期的范式

## 来源

- [[wiki/sources/loop-engineering-guide]] — 菜鸟教程：六大要素 + 五种模式
- [[wiki/sources/loop-engineering-claude-best-practices-2026]] — 本文对应的原始资料聚合
- [[wiki/syntheses/loop-engineering-with-claude-code]] — Claude Code 实操指南
- [[wiki/syntheses/harness-engineering-with-claude-code]] — 互补的 Harness 实操指南
