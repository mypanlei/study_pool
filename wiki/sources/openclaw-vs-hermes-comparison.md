---
title: "OpenClaw vs Hermes Agent 详细对比 — 个人助理平台 vs 自改进 Agent 框架"
tags:
  - source
  - openclaw
  - hermes
  - comparison
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://openclaw.ai/"
source_author: "自建知识库笔记"
source_date: 2026-06-11
---

# OpenClaw vs Hermes Agent 详细对比

> OpenClaw 更像 personal AI assistant platform（个人助理平台），Hermes Agent 更像 self-improving agent operating system（自改进 Agent 操作系统）。

## 核心论点

1. **设计中心差异** — OpenClaw 以「个人助理体验 + chat-native + always-on」为中心；Hermes 以「agent runtime + learning loop + provider abstraction」为中心。
2. **入口模型** — OpenClaw 以 chat app 为第一入口，从消息入口延展到系统执行；Hermes 同时强调 CLI 和消息平台是同一 runtime 的两个操作面。
3. **记忆与技能** — OpenClaw 偏产品化的持久上下文（越来越懂你的助理）；Hermes 偏 agent runtime 的闭环学习（越来越会做事的 agent runtime），支持自主技能创建和自我改进。
4. **Provider 策略** — OpenClaw 多模型但 provider abstraction 不是最强卖点；Hermes 明确 20+ providers，provider-agnostic 是核心能力。
5. **部署模型** — OpenClaw 偏「这就是我的 agent 机器」；Hermes 偏「agent runtime 与执行环境解耦」，支持 local/Docker/SSH/Daytona 等多种 backend。

## 最终判断

- 想要个人助理 + 聊天入口优先 → OpenClaw
- 想要长期积累技能 + 可换 provider + 可工程化扩展 → Hermes Agent

## 受影响的 Wiki 页面

- [[wiki/entities/openclaw]] — 已创建
- [[wiki/entities/hermes-agent]] — 已更新
- [[wiki/syntheses/ai-agent-ecosystem-comparison]] — 已更新
