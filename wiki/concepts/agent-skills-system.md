---
title: "Agent Skills System"
tags:
  - concept
  - agent
  - ai
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Agent 技能系统
  - 可移植技能
---

# Agent Skills System

> AI Agent 的「程序性记忆」— 可复用、可共享、可自我改进的任务指令单元。

## 定义

Agent Skills 是 AI Agent 的可复用行为模块，相当于 Agent 的「程序性记忆」（知道「怎么做」），区别于「陈述性记忆」（知道「是什么」）。

## 当前生态中的 Skill 系统对比

| 维度 | Claude Code Skills | Hermes Agent Skills | agentskills.io |
|------|-------------------|-------------------|----------------|
| 格式 | SKILL.md（Markdown） | SKILL.md（Markdown） | 开放标准 |
| 创建方式 | 手动编写 | 自动+手动 | 社区贡献 |
| 自我改进 | ❌ 静态 | ✅ 运行时自动优化 | — |
| 可移植性 | 项目内 `.claude/skills/` | 跨平台 | 跨 Agent |

## 关键洞察

- Hermes Agent 的「闭环学习」代表了 Skill 的未来方向：**Skill 不应该是静态的指令文件，而应该在使用中动态进化**
- agentskills.io 作为开放标准，有可能成为 Agent Skill 的「npm」— 一个跨平台的技能市场
- Claude Code 的 SKILL.md 是 1.0 版本，Hermes 的自我改进技能是 2.0

## 来源

- [[wiki/sources/hermes-agent-docs]]
- [[wiki/syntheses/claude-skill-management]]
