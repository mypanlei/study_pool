---
title: "OpenClaw、Hermes、Pi、Claude Code、Codex、Copilot 区别与选型指南"
tags:
  - source
  - comparison
  - agent
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "internal note"
source_author: "自建知识库笔记"
source_date: 2026-06-11
---

# OpenClaw、Hermes、Pi、Claude Code、Codex、Copilot 区别与选型指南

> 这 6 个名字分属不同层级：从个人 AI 助手到编码 agent 产品，从开源框架到云端执行系统。

## 核心论点

1. **OpenClaw** — 个人/团队 AI 助手平台，chat-app native，偏 personal assistant，不是 coding-first。
2. **Hermes Agent** — 自我改进的开源 agent 框架，技能学习闭环、provider 抽象、跨终端与消息平台。
3. **Pi** — 开源 coding-agent harness，多 provider、本地 CLI、可扩展 runtime，默认安全边界较弱。
4. **Claude Code** — 成熟的一体化 coding agent 产品，本地代码库上下文理解，多入口统一体验。
5. **Codex** — 云端软件工程 agent，每个任务在独立云 sandbox 中执行，异步委派和可审计交付。
6. **GitHub Copilot** — 以 GitHub 和 IDE 工作流为中心的 AI 编程协作层，正扩展到 cloud agent 和第三方 agent 编排。

## 选型框架

- 个人 AI 助理 → OpenClaw 或 Hermes
- 本地高频编程 → Claude Code 或 Copilot
- 远程并行派工 → Codex
- 可控可自建长期演化 → Hermes 或 OpenClaw

## 受影响的 Wiki 页面

- [[wiki/entities/openclaw]] — 已创建
- [[wiki/entities/pi-agent]] — 已创建
- [[wiki/entities/hermes-agent]] — 已更新
- [[wiki/entities/claude-code]] — 已更新
- [[wiki/syntheses/ai-agent-ecosystem-comparison]] — 已更新
