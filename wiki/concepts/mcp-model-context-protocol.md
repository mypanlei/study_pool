---
title: "MCP (Model Context Protocol)"
tags:
  - concept
  - mcp
  - protocol
  - anthropic
  - tool-use
  - agent
created: 2026-06-18
updated: 2026-06-18
aliases:
  - Model Context Protocol
  - MCP 协议
  - MCP Server
  - MCP Client
---

# MCP (Model Context Protocol)

## 定义

MCP（Model Context Protocol）是 Anthropic 推出的开放协议，旨在为 AI 模型（尤其是 LLM）提供标准化的外部工具和数据接入方式。MCP 采用 **Host-Client-Server** 三层架构，本质是定义模型与外部资源之间的"连接协议"，使 Agent 可以像 USB 设备一样即插即用地使用各类工具和 API。

MCP 与 A2A 形成互补对等关系：
- **MCP**：Agent ↔ Tool（垂直集成，解决"如何访问数据"）
- **A2A**：Agent ↔ Agent（水平互联，解决"如何协同合作"）

## 核心要点

- **标准化工具接口**：将各种 API、数据库、文件系统统一为 MCP Server 形态
- **三层架构**：Host（宿主应用）→ Client（客户端）→ Server（服务端）
- **关注连接**：MCP 关注"如何接入"，而非"如何执行"（后者是 Agent Skills 的领域）
- **即插即用**：MCP Server 可独立开发、独立部署，Host 应用自动发现和调用
- **开放生态**：已有大量官方和社区 MCP Server（文件系统、数据库、GitHub、Slack 等）

## 详细阐述

### 背景

在 MCP 出现之前，每个 AI 应用都需要为每个外部工具编写自定义集成代码。这种"点对点"的集成模式导致：
- 每个工具需要单独适配不同的 AI 框架
- 工具的切换和复用成本高
- 安全策略难以统一管理

MCP 将工具接口标准化，类比为 AI 领域的 **USB 接口** —— 无论设备内部逻辑如何，只需符合 USB 标准即可即插即用。

### 架构模型

```
Host (Claude Desktop / IDE / CLI)
  │
  ├── Client (MCP Client) ←→ MCP Server A (文件系统)
  │
  └── Client (MCP Client) ←→ MCP Server B (数据库)
```

| 角色 | 描述 | 示例 |
|------|------|------|
| **Host** | 用户直接交互的宿主应用 | Claude Desktop、VS Code、Claude Code |
| **Client** | 与 MCP Server 建立 1:1 连接的客户端 | 每个 Server 对应一个专用 Client |
| **Server** | 提供特定工具/资源/能力的服务端 | 文件系统 Server、GitHub Server |

### MCP vs Agent Skills

| 维度 | MCP | Agent Skills |
|------|-----|--------------|
| 关注点 | **连接** — 如何访问数据和 API | **逻辑** — 如何按流程执行任务 |
| 本质 | 协议层（传输） | 指令层（知识） |
| 是否需要后端 | 需要编码配置和 Server 运行 | 不需要后端，纯文本指令 |
| 复用方式 | HTTP/stdio 连接 | 文件复制 + 加载 |
| 类比 | USB 接口（硬件连接） | 用户手册（操作指南） |

### MCP vs A2A

| 维度 | MCP | A2A |
|------|-----|-----|
| 解决问题 | Agent ↔ Tool 连接（垂直集成） | Agent ↔ Agent 通信（水平互联） |
| Agent 模型 | Agent 主动调用外部工具 | Agent 之间以黑盒方式协作 |
| 类比 | USB（设备连接） | HTTP（Web 通信） |
| 架构 | Host-Client-Server | Client-Remote Agent |
| 发起方 | Host 应用决定调用 | Client Agent 发起任务请求 |

### 常见 MCP Server 示例

- **文件系统** — 读写本地文件、搜索目录
- **数据库** — SQL 查询、Schema 浏览
- **GitHub** — PR 管理、Issue 操作、代码搜索
- **Slack** — 消息发送、频道管理
- **Web 搜索** — 网页抓取、搜索引擎调用
- **Memory** — 持久化存储和检索

## 相关概念

- [[wiki/concepts/a2a-agent-to-agent-protocol]] — A2A（Agent 间通信）与 MCP 互补
- [[wiki/concepts/agent-skills-system]] — Agent Skills（指令层）与 MCP（连接层）对比
- [[wiki/concepts/harness-engineering]] — Harness 工程中工具的集成和管理
- [[wiki/entities/anthropic]] — Anthropic 公司，MCP 协议的提出者

## 来源

- [[wiki/sources/llm-skills-technical-guide]] — LLM Skills 技术全景指南，含 MCP 协议详解
- [[wiki/sources/ai-agent-tools-integration]] — 菜鸟教程 Agent 工具集成，含 MCP 实现
- [[wiki/sources/skills-tutorial]] — Skills 教程，MCP vs Skills 对比
- [[wiki/sources/multi-agent-system]] — A2A vs MCP 对比框架
- [[wiki/sources/ai-agent-glossary]] — Agent 术语词典含 MCP 定义
