---
title: "A2A 官方公告与协议规范 — Google / Linux Foundation"
tags:
  - source
  - a2a
  - google
  - linux-foundation
  - protocol
  - official
created: 2026-06-19
updated: 2026-06-19
source_url: "https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/"
source_author: "Google Developers Blog / Linux Foundation / a2aproject"
source_date: 2025-04-09
---

# A2A 官方公告与协议规范

> Google 官方发布的 A2A 协议公告 + Linux Foundation 托管的官方协议规范 + GitHub a2aproject 开源仓库。涵盖协议的设计定位、企业生态、治理结构、与 MCP 的关系、SDK 支持（6 种语言）等官方权威信息。

## 核心论点

1. **A2A 由 Google 开发并捐赠给 Linux Foundation** — 由 AWS/Cisco/Google/IBM/Microsoft/Salesforce/SAP/ServiceNow 组成的 TSC 共同治理
2. **A2A 与 MCP 非竞争而是互补** — MCP 管 Agent↔Tool，A2A 管 Agent↔Agent，两者可结合使用
3. **A2A 不是 Agent 开发框架** — 不替代 LangGraph/CrewAI/ADK，而是 Agent 间的通信层
4. **50+ 企业伙伴支持** — 包括 Atlassian、Box、Cohere、Intuit、LangChain、MongoDB、PayPal、Salesforce 等
5. **官方 SDK 覆盖 6 种语言** — Python、JavaScript、Java、C#/.NET、Golang、Rust

## 核心内容

### 官方定位

| A2A 是 | A2A 不是 |
|--------|----------|
| Agent 间通信协议 | Agent 开发框架（不替代 LangGraph/CrewAI/ADK） |
| 开放标准（Linux Foundation） | 子 Agent 或工具调用协议 |
| 企业级互操作方案 | MCP 的替代品 |
| 机器对机器协议 | 聊天应用（Slack/Discord） |

### 治理结构
- **托管组织**：Linux Foundation
- **技术指导委员会**: AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, ServiceNow
- **许可证**: Apache 2.0
- **官方资源**: 协议规范 (a2a-protocol.org)、GitHub 样例代码、DeepLearning.AI 课程

## 与现有知识的关系

- 本文是 [[wiki/sources/google-a2a-protocol]]（掘金社区文章）的官方权威来源补充
- 与 [[wiki/concepts/a2a-agent-to-agent-protocol]] 概念页对应，提供了治理和生态方面的官方信息
- 与 [[wiki/concepts/mcp-model-context-protocol]] 中 A2A vs MCP 对比的官方依据

## 受影响的 Wiki 页面

- [[wiki/concepts/a2a-agent-to-agent-protocol]] — 已补充官方来源引用
- [[wiki/entities/google-adk]] — 已补充 A2A Linux Foundation 治理信息
