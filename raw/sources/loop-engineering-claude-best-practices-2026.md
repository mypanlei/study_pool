---
title: "Loop Engineering 使用 Claude 的最佳实践（2026）"
tags:
  - loop-engineering
  - claude
  - best-practices
  - agent
  - workflow
source_urls:
  - "https://developer.aliyun.com/article/1744228"
  - "https://developer.aliyun.com/article/1743448"
  - "https://github.com/maxmilian/loop-engineering"
  - "https://github.com/cobusgreyling/loop-engineering"
  - "https://cloud.tencent.com.cn/developer/article/2689205"
  - "https://www.techspot.com/news/112923-ai-developers-moving-beyond-prompts-loops-take-over.html"
source_date: 2026-06-30
clipped: false
---

# Loop Engineering 使用 Claude 的最佳实践（2026）

> 本文聚合自 2026 年多篇 Loop Engineering 实践文章，涵盖 Claude Code 内置循环命令、Builder/Checker 隔离模式、停止规则、大规模多 Agent 编排以及社区工具生态。

## 一、Loop Engineering 概述

Loop Engineering（循环工程）是 2026 年兴起的一种 AI 编程范式。核心理念是：不再由人向 AI 发送指令，而是设计一套系统让 AI 自动循环运行。

Claude Code 之父 Boris Cherny 的原话：
> "我不再提示 Claude 了。我有一堆循环在运行，它们才是在提示 Claude 并判断接下来该怎么做。我的工作变成了写循环。"

## 二、Claude Code 内置的两种循环命令

### 1. `/goal` 命令

- **机制**：跑到目标达成为止，由独立模型判断是否完成（非执行任务的模型自评）
- **适用场景**：从零搭建项目、批量重构
- **核心优势**：自带验证闭环，Agent 自行判断目标达成条件
- **用法**：`/goal 实现一个用户登录功能，包含 JWT 鉴权`

### 2. `/loop` 命令

- **机制**：按固定时间间隔重复执行
- **适用场景**：持续监控、定时扫描
- **用法**：`/loop 10m 检查 CI 状态`
- **注意事项**：在同一会话中运行，上下文会持续累积

## 三、Builder/Checker 隔离模式（核心设计模式）

这是社区公认的最重要模式。用三个文件搭建完整闭环：

### builder.md
- 专职写代码的 Agent
- **有** Write/Edit 工具权限

### checker.md
- 专职检查代码的 Agent
- **只有读权限**，硬隔离
- 使用独立模型审查，避免"自己写自己查"的盲区

### 循环编排器
- 调度循环的核心
- 通过 `/loop` 命令或外部调度器实现

**关键原则**：验证必须用独立模型，而非执行任务的模型自评。这是最常被忽视的坑。

## 四、停止规则（熔断机制）

防止死循环，应写在 CLAUDE.md 中：

| 规则 | 触发条件 | 动作 |
|------|---------|------|
| ALL GREEN | 所有检查通过 | 循环正常结束 |
| 轮次用尽 | 达到上限（建议 5 轮） | 强制停止，报告未完成项 |
| 连续重复失败 | 同一失败连续出现 2 轮 | 停止，标记为无法自动修复 |
| 回归 | 修复导致之前通过的检查失败 | 停止，回退到稳定版本 |
| 无实质进展 | 连续 2 轮失败项未减少 | 停止，请求人工介入 |
| 超出能力 | 模型自身判断无法解决 | 停止，输出当前状态供人工接手 |

## 五、大规模多 Agent 编排实践

### 300 Agent 协同案例
- Kimi 2.6 Swarm 集群（执行代码生成）
- Claude Opus 4.8（负责验收和质量控制）
- 分工逻辑：执行 Agent 批量产出 → Claude 单点验收 → 不合格回炉 → 自进化

### 关键经验
- 执行层追求速度，验收层追求质量
- 多 Agent 编排需要严格的状态追踪和防冲突机制
- 验收 Agent 使用更强大的模型，执行 Agent 使用更快速的模型

## 六、社区工具生态

### GitHub: maxmilian/loop-engineering
- 可直接安装的 Skill 包
- 设计用于 Claude Code、Codex、Copilot、Gemini 等工具
- 包含完整的设计和审查循环模板

### GitHub: cobusgreyling/loop-engineering
- 包含 CLI 工具：
  - `loop-audit` — 审计现有工作流中的循环机会
  - `loop-init` — 初始化项目循环配置
  - `loop-cost` — 估算循环的 Token 成本

## 七、实践建议总结

| 维度 | 建议 |
|------|------|
| 验证机制 | 用独立模型判断完成，而非执行任务的模型自评 |
| 状态追踪 | 用 PROGRESS.md 记录进度，防止上下文丢失 |
| 熔断机制 | 同问题修复超过 5 次即跳过，防死循环 |
| Token 管理 | 设轮次上限和 Token 预算 |
| 模型选择 | 循环场景需高频调用，优先速度快、可配置推理强度的模型 |
| 学习路径 | 先练提示词 → 学会 CLAUDE.md → /goal 小目标 → 进阶 loop 系统 |
