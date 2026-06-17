---
title: "Google A2A 协议详解 — 掘金社区文章"
tags:
  - source
  - a2a
  - google
  - agent-protocol
  - multi-agent
created: 2026-06-18
updated: 2026-06-18
source_url: "https://juejin.cn/post/7491231635868090394"
source_author: "MervynZ"
source_date: 2025-04-09
---

# Google A2A 协议详解

> 一篇全面介绍 Google Agent-to-Agent（A2A）开放协议的深度文章，涵盖协议的动机、核心架构、通信模型、Agent Card 规范、任务生命周期及 JSON-RPC API 示例。

## 核心论点

1. **A2A 解决 Agent 互操作性问题** — 不同供应商/框架构建的 AI Agent 之间缺乏有效的通信和协作方式，A2A 提供了通用的通信语言让 Agent 可以跨框架协作，而不需要共享记忆、思维或工具。
2. **A2A 与 MCP 互补而非竞争** — A2A 解决 Agent 间通信（发现/协作/同步），MCP 解决 Agent 与外部工具连接；两者可结合使用构建完整的 Agent 生态系统。
3. **企业级安全设计** — A2A 遵循 OpenAPI 认证规范，身份信息通过带外（out-of-band）方式传递，不在协议 payload 中传输身份信息。服务端通过 Agent Card 公开认证要求。

## 架构概述

### 核心参与者
- **用户（User）** — 使用 Agent 系统的终端用户（人类或服务）
- **客户端（Client）** — 代表用户向"黑盒"Agent 发起任务请求的实体
- **远程 Agent/服务器（Remote Agent / Server）** — 黑盒 Agent，A2A 协议的服务端

### 传输层
- **HTTP** — 底层传输协议
- **JSON-RPC 2.0** — 数据交换格式
- **SSE（Server-Sent Events）** — 支持服务器向客户端主动实时推送流式更新
- **Webhook** — 客户端离线时的异步通知机制

### 关键组件

1. **Agent Card** — 每个 Agent 发布在 `/.well-known/agent.json` 的公开文件，描述能力、技能、认证方式和通信端点。客户端据此发现并选择合适的 Agent 合作伙伴。
2. **Task（任务）** — 核心工作单元，有唯一 ID 和生命周期状态。状态包括：`submitted` → `working` → `input-required` / `completed` / `canceled` / `failed`。
3. **Artifact（制品）** — Agent 生成的不可变最终结果（文本、文件、结构化数据），支持流式追加。
4. **Message（消息）** — 非制品内容（思维过程、上下文、指令），角色标记为 `user` 或 `agent`。
5. **Part** — 消息和制品的内容单元，支持 Text/File/Data 三种类型。

### 执行模型

- **即时完成** — 请求后立即返回结果
- **长任务轮询** — 客户端通过 polling 周期性获取状态更新
- **SSE 推送** — 保持连接时实时推送状态和制品更新
- **断线重连** — 通过 `tasks/resubscribe` 重新订阅任务流
- **多轮对话** — 任务进入 `input-required` 状态时请求客户端补充输入，实现多轮交互

## 关键引用/数据

> "A2A 让 Agent 能够在不共享记忆、思维或工具的情况下完成终端用户的任务。取而代之的是，Agent 通过各自相互结合的方式交换上下文、状态、指令和数据。"

> "发现机制是整个 A2A 协议中最基础也是最关键的环节。每个 Agent 公开一个 JSON 文件，称为 Agent Card，位于 `https://<base-url>/.well-known/agent.json`。"

> "A2A 遵循 OpenAPI 的身份验证规范进行认证。值得注意的是，A2A 协议中不会在协议中交换身份信息。"

## 与现有知识的关系

- 补充 [[wiki/sources/multi-agent-system]] 中对 A2A 与 MCP 对比的简要提及，提供了 A2A 协议全貌的技术细节
- 与 [[wiki/concepts/a2a-agent-to-agent-protocol]] 概念页对应，作为其主要来源
- 与 [[wiki/entities/google-adk]] 相关，A2A 是 Google 的 Agent 开放协议

## 个人思考

- A2A 的"黑盒 Agent"假设很重要：Agent 之间不需要共享内部状态，只通过标准接口交换任务和数据，这种解耦设计让不同组织构建的 Agent 可以安全协作
- A2A vs MCP 的分工明确：A2A 管 Agent 之间通信（类似 HTTP），MCP 管 Agent 与工具连接（类似 USB）。这种分层设计降低了互操作性的复杂度
- Agent Card 的发现机制与 DNS 类比很恰当，使得 Agent 生态可以像互联网一样去中心化扩展
- 推送通知机制的设计考虑到了企业安全场景（中央通知服务），说明 Google 主要瞄准企业级生产部署

## 受影响的 Wiki 页面

- [[wiki/entities/google-adk]] — 已更新，添加 A2A 协议说明
- [[wiki/concepts/a2a-agent-to-agent-protocol]] — 新建概念页
