---
title: "多智能体系统（Multi-Agent System） — 菜鸟教程"
tags:
  - source
  - multi-agent
  - autogen
  - a2a
  - mcp
  - orchestration
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/multi-agent-system.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# 多智能体系统（Multi-Agent System）

> 系统介绍多智能体系统的架构与实现，涵盖层次架构和平级架构两种基本模式、角色分工（规划者/执行者/审核者/协调者）、AutoGen 框架使用（AssistantAgent/UserProxyAgent/GroupChat）、A2A 与 MCP 协议对比、主从 Agent 模式（Orchestrator+Subagent）。

## 核心内容

1. **基本架构模式** — 层次架构（Orchestrator+Subagent 树状调度）和平级架构（Peer-to-Peer 对等协作）。
2. **角色分工** — 规划者（分解任务）、执行者（调用工具）、审核者（评估结果）、协调者（通信与分配）。
3. **AutoGen 框架** — 微软多 Agent 框架：AssistantAgent（智能助手）、UserProxyAgent（用户代理）、GroupChat（群聊协作）、GroupChatManager（交互管理），含工具注册示例。
4. **A2A vs MCP** — A2A 解决 Agent 间通信（发现/协作/同步），MCP 解决 Agent 与外部工具连接（Host/Client/Server 架构）。
5. **主从模式** — Orchestrator（任务分解/并行调度/结果整合）+ Subagent（具体执行），适合层次分明任务，附完整并行执行代码。

## 关键概念

- 多 Agent 系统三大挑战：分工、通信、协调
- A2A 和 MCP 解决的问题不同，可结合使用构建完整系统
- 简单场景单 Agent 即可，复杂场景根据任务特点选择架构
