---
title: "A2A (Agent-to-Agent) 协议"
tags:
  - concept
  - a2a
  - agent-protocol
  - google
  - multi-agent
  - interoperability
created: 2026-06-18
updated: 2026-06-18
aliases:
  - Agent-to-Agent
  - A2A 协议
  - Agent2Agent
---

# A2A (Agent-to-Agent) 协议

## 定义

A2A（Agent-to-Agent）是 Google 于 2025 年 4 月 9 日开源的开放协议，旨在为不同框架和供应商构建的 AI Agent 提供标准化的通信与协作方式，实现跨平台、跨框架的 Agent 互操作性。A2A 将 Agent 视为"黑盒"，通过标准接口交换上下文、状态、指令和数据，而不需要 Agent 之间共享内部记忆、思维或工具。

## 核心要点

- **开放标准**：基于 HTTP + JSON-RPC 2.0 构建，复用现有 Web 标准
- **黑盒模型**：Agent 不暴露内部实现、记忆或工具，仅通过标准 API 交换任务级信息
- **发现机制**：通过 `/.well-known/agent.json`（Agent Card）实现类似 DNS 的 Agent 服务发现
- **任务中心**：以 Task 为协作核心单元，支持即时/长任务/流式/多轮等多种执行模式
- **企业安全**：遵循 OpenAPI 认证规范，身份信息通过带外方式（HTTP Header）传递
- **A2A ≠ MCP**：A2A 解决 Agent 间通信（水平互联），MCP 解决 Agent 与工具连接（垂直集成），两者互补

## 详细阐述

### 背景

随着 AI Agent 技术的快速发展，不同供应商和框架（LangGraph、CrewAI、AutoGen、ADK 等）构建的 Agent 之间缺乏标准化的通信方式，限制了它们在复杂多步骤任务中的应用。Google 于 2025 年 4 月 9 日推出 A2A 协议，旨在建立类似 USB 或蓝牙的通用"连接标准"。

A2A 的设计原则：
- **简洁**：复用现有标准（HTTP、JSON-RPC、SSE）
- **企业就绪**：支持身份认证、安全、隐私、审计追踪
- **异步优先**：支持长时间运行任务和人工参与的流程
- **多模态**：支持文本、音频、视频、表单、iframe 等多种交互
- **黑盒执行**：Agent 无需共享内部思考过程、计划或工具

### 架构模型

A2A 定义了三个核心参与者：

```
用户 (User) → 客户端 (Client) ↔ 远程 Agent (Server)
```

- **用户**：发起任务的终端用户（人类或服务）
- **客户端**：代表用户向远程 Agent 发起任务请求（服务、Agent 或应用）
- **远程 Agent**：黑盒执行任务的服务器端

### 发现机制

每个支持 A2A 的 Agent 在 `https://<base-url>/.well-known/agent.json` 发布 Agent Card（JSON 格式），包含：

| 字段 | 描述 |
|------|------|
| `name` | Agent 可读名称 |
| `description` | Agent 功能描述 |
| `url` | 服务地址 |
| `version` | Agent 版本 |
| `capabilities` | 支持的能力（流式、推送通知、状态历史） |
| `authentication` | 认证需求（schemes + credentials） |
| `defaultInputModes` | 默认输入 MIME 类型 |
| `defaultOutputModes` | 默认输出 MIME 类型 |
| `skills[]` | Agent 技能列表（id、name、description、tags、examples） |

客户端通过 Agent Card 判断 Agent 能力是否匹配任务需求，获取认证方式，建立通信。

### 任务生命周期

Task 是 A2A 协议的核心工作单元，生命周期状态机：

```
submitted → working → completed
                    → canceled
                    → failed
                    → input-required → (等待用户输入后回到 working)
```

任务核心对象：
- **Task**：唯一 ID、sessionId、状态、消息历史、制品集合
- **Artifact**：Agent 生成的不可变结果（支持流式追加）
- **Message**：角色化的内容交换（role: "user" | "agent"）
- **Part**：内容单元（Text/File/Data 三种类型）

### API 方法

| 方法 | 用途 |
|------|------|
| `tasks/send` | 创建/恢复/重开任务 |
| `tasks/get` | 查询任务状态和制品 |
| `tasks/cancel` | 取消任务 |
| `tasks/sendSubscribe` | 创建任务并订阅流式更新（SSE） |
| `tasks/resubscribe` | 断线重连，重新订阅任务更新 |
| `tasks/pushNotification/set` | 设置推送通知配置 |
| `tasks/pushNotification/get` | 查询推送通知配置 |

### 错误处理

使用 JSON-RPC 标准错误码 + 自定义扩展：

| 错误码 | 含义 |
|--------|------|
| -32700 | JSON 解析错误 |
| -32600 | 无效请求 |
| -32601 | 方法未找到 |
| -32602 | 无效参数 |
| -32603 | 内部错误 |
| -32001 | 任务未找到 |
| -32002 | 任务无法取消 |
| -32003 | 不支持推送通知 |
| -32004 | 不支持的操作 |
| -32005 | 不兼容的内容类型 |

## 相关概念

- [[wiki/sources/multi-agent-system]] — 菜鸟教程多智能体系统（含 A2A vs MCP 对比），A2A 是多 Agent 系统的重要通信协议
- [[wiki/entities/google-adk]] — Google ADK 是 Google 的 Agent 开发工具包，可集成 A2A 协议
- [[wiki/sources/google-a2a-protocol]] — 掘金社区 A2A 协议详解（主要来源）
- [[wiki/sources/a2a-official-spec-linux-foundation]] — A2A 官方公告与 Linux Foundation 协议规范，补充治理/生态/SDK 信息

### A2A vs MCP 与 FC/Agent 完整分层

MCP、FC (Function Calling)、Agent 三者是不同层级的组件，A2A 与 MCP 的关系需要放在这个分层中理解：

| 层次 | 协议/机制 | 解决问题 |
|------|-----------|----------|
| **Agent 层** | Agent 规划框架 | 任务怎么一步步做完（ReAct/Plan-and-Execute） |
| **Agent ↔ Agent** | **A2A** | Agent 间水平互联与协作 |
| **Agent ↔ Tool** | **MCP** | 工具发现、连接与执行 |
| **模型表达层** | **Function Calling** | 模型怎么输出结构化调用意图 |

| 维度 | A2A | MCP |
|------|-----|-----|
| 解决问题 | Agent ↔ Agent 通信（水平互联） | Agent ↔ Tool 连接（垂直集成） |
| 类比 | HTTP（Web 通信） | USB（设备连接） |
| Agent 模型 | 黑盒（不共享内部状态） | Agent 主动调用工具 |
| 通信方式 | 任务驱动 + JSON-RPC + SSE | Client-Server 模式 |
| 协作方式 | 客户端-远程 Agent | Host-Client-Server |

## 来源

- [[wiki/sources/google-a2a-protocol]] — Google A2A 协议详解（掘金社区文章）
- [[wiki/sources/multi-agent-system]] — 菜鸟教程多智能体系统（含 A2A vs MCP 对比）
- [[wiki/sources/mcp-deep-dive-javaguide]] — JavaGuide MCP 深度解析（含 FC/MCP/Agent 三层关系，完善 A2A vs MCP 对比框架）
