---
title: "Hermes Agent"
tags:
  - entity
  - agent
  - ai
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Hermes
---

# Hermes Agent

> Nous Research 构建的自主 AI 代理，核心特色是「闭环学习系统」— 从经验中创建技能、在使用中自我改进、跨会话持久化记忆。

## 关键信息

- **类型**: 自主 AI Agent
- **开发商**: [[wiki/entities/nous-research]]
- **安装方式**: 一键脚本或 Desktop 安装包
- **后端**: CLI / Docker / SSH / Daytona / Modal / Singularity
- **消息平台**: 20+（CLI、Telegram、Discord、Slack、飞书、钉钉、微信等）

## 核心特色

| 特性 | 描述 |
|------|------|
| 闭环学习 | Agent 自主创建和改进技能 |
| 记忆系统 | 跨会话持久化，FTS5 + LLM 摘要 |
| Skills 系统 | 兼容 agentskills.io 开放标准 |
| MCP 支持 | 可扩展工具能力 |
| 调度自动化 | 内置 cron |
| Voice Mode | 实时语音交互 |

## 与 Claude Code 的对比

| 维度 | Hermes Agent | Claude Code |
|------|-------------|-------------|
| 定位 | 独立自主 Agent | IDE 内嵌编码助手 |
| 技能创建 | 自主创建+改进 | 手动编写 SKILL.md |
| 运行环境 | 任意后端（VPS/Serverless） | 本地 CLI |
| 消息平台 | 20+ 平台 | CLI 为主 |
| 学习能力 | 闭环学习 | 无内置学习 |

## 来源

- [[wiki/sources/hermes-agent-docs]]
- [[wiki/sources/hermes-agent-alicloud-deployment-guide]]
- [[wiki/sources/hermes-agent-alicloud-messaging-guide]]
