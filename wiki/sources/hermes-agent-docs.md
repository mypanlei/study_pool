---
title: "Hermes Agent — Nous Research 的自我进化 AI 代理"
tags:
  - source
  - agent
  - ai
created: 2026-06-13
updated: 2026-06-13
source_url: "https://hermes-agent.nousresearch.com/docs/"
source_author: "Nous Research"
source_date: 2026
---

# Hermes Agent Documentation

> Nous Research 构建的自主 AI 代理。核心特色是「闭环学习系统」— 从经验中创建技能、在使用中自我改进、跨会话持久化记忆。

## 核心特性

1. **闭环学习 (Closed Learning Loop)** — Agent 自主管理记忆、自动创建技能、在使用中自我改进技能、FTS5 跨会话召回 + LLM 摘要
2. **随处运行** — 6 种终端后端：local / Docker / SSH / Daytona / Modal / Singularity，不绑定在笔记本上
3. **多平台** — CLI + 20+ 消息平台（Telegram、Discord、Slack、WhatsApp、飞书、钉钉、微信等）
4. **Skills 系统** — 可移植/可共享的技能，兼容 agentskills.io 标准，社区贡献的 Skills Hub
5. **MCP 支持** — 可连接任何 MCP 服务器扩展工具能力
6. **调度自动化** — 内置 cron + 任意消息平台投递

## 与 Claude Code / LLM Wiki 的关系

- Hermes Agent 的 **Skills 系统** 与 Claude Code 的 Skills 类似，但更强调「自主创建和自我改进」— Agent 在运行时自动生成和优化技能
- 兼容 agentskills.io 开放标准，这意味着 Skills 是跨平台可移植的
- Hermes 的 Memory System 与 LLM Wiki 的持久化维基有异曲同工之妙：都是在构建跨会话的知识积累
- 但 Hermes 更 Agent 导向（自主行动），而 LLM Wiki 更知识库导向（人类引导 + LLM 维护）

## 关键实体

- **Nous Research** — 背后的研究实验室（也是 Hermes、Nomos、Psyche 模型的创造者）
- **Nous Portal** — 一站式 OAuth 认证 + 工具网关（Web 搜索、图像生成、TTS、浏览器）
- **agentskills.io** — 开放技能标准/市场

## 个人思考

- Hermes 的「技能自我改进」机制很有意思 — Skill 不只是静态指令，而是在使用中动态优化。这比 Claude Code 的静态 SKILL.md 更进一步
- 如果 LLM Wiki 的 Agent（如当前这个）也能在运行中动态优化自己的工作流，那就接近 Hermes 的闭环学习理念了
- 「不绑定在 IDE 上」是 Hermes 与 Claude Code 的定位差异：前者是独立 Agent，后者是 IDE 内嵌的编码助手

## 受影响的 Wiki 页面

- [[wiki/entities/hermes-agent]] — 已创建
- [[wiki/entities/nous-research]] — 已创建
- [[wiki/concepts/agent-skills-system]] — 已创建
