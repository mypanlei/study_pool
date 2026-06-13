---
title: "Cursor Agent vs Skill 使用决策指南 — Agent、Skill、Subagent 的完整分工体系"
tags:
  - source
  - cursor
  - agent
  - workflow
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://cursor.com/docs/agent/overview.md"
source_author: "Cursor 官方文档"
source_date: 2026-05-21
---

# Cursor Agent vs Skill 使用决策指南

> Agent 是执行者，Skill 是能力说明书，Subagent 是被主 Agent 委派出去的专门助手。三者构成 Cursor 的完整 AI 工作流体系。

## 核心论点

1. **Agent 的核心** — 理解目标、搜索代码、读写文件、运行终端、调用工具并完成任务，由 Instructions + Tools + Model 三部分组成。
2. **Skill 的核心** — 可复用能力包，包含 SOP、脚本、模板和参考资料，Agent 在合适时机读取使用，本身不主动执行。
3. **Subagent 的核心** — 在独立上下文中处理复杂、并行、长时间或需要专门角色的任务，然后将结果交回主 Agent。
4. **四种工作模式** — Agent Mode（直接执行）、Plan Mode（先规划再执行）、Debug Mode（诊断定位）、Multitask（并行多任务）。
5. **与 Rules/MCP 的关系** — Rules 约束行为、Skill 提供流程、MCP 连接外部系统、Subagent 委派任务、Agent 完成目标。

## 决策树

- 一次性任务 → Agent
- 反复出现的固定流程 → Skill
- 需要独立上下文的复杂任务 → Subagent
- 约束 Agent 行为 → Rules
- 连接外部系统 → MCP

## 受影响的 Wiki 页面

- [[wiki/concepts/agent-skills-system]] — 已更新
- [[wiki/entities/claude-code]] — 已关联
