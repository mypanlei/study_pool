---
title: "Google ADK / Gemini Enterprise Agent Platform"
tags:
  - entity
  - gemini
  - agent
  - platform
  - google
created: 2026-06-13
updated: 2026-06-13
aliases:
  - ADK
  - Agent Development Kit
  - Gemini Enterprise Agent Platform
---

# Google ADK / Gemini Enterprise Agent Platform

> Google 的开源 Agent Development Kit（ADK）加上 Google Cloud 托管服务（Vertex AI、Agent Platform、Memory Bank）构成的完整企业级 Agent 开发与运行栈。

## 关键信息

- **类型**: 托管型企业 Agent 栈
- **开发商**: Google
- **核心定位**: 企业 Agent 应用层开发与运行
- **默认交付模式**: Google Cloud managed services + ADK
- **开发方式**: 代码优先，结合托管云服务
- **主要抽象**: Agent, Tool, Session, State, Memory, Workflow, Runtime

## 核心组件

| 组件 | 描述 |
|------|------|
| ADK | 开源 Agent Development Kit |
| Agent Platform / Vertex AI | 托管模型与 Agent 运行时 |
| Memory Bank / Knowledge Engine | 长期记忆与 RAG memory 能力 |
| Cloud Run / GKE | 托管与半托管部署路径 |
| Google Cloud 观测/IAM | 生产落地基础设施 |

## 核心特色

- **Memory 是一等公民**: MemoryService, Memory Bank, RAG Memory
- **多 Agent 协作**: 图工作流、工具调用、会话驱动；提出 A2A 开放协议实现跨框架 Agent 互操作
- **企业治理**: 继承 Google Cloud IAM、Logging、Metrics
- **模型灵活**: 支持 Gemini、Vertex endpoint、Claude、开源模型

## 开放协议

Google 于 2025 年 4 月 9 日发布了 A2A（Agent-to-Agent）开放协议，实现 Agent 间的标准化通信。与 ADK 等 Google 内部 Agent 工具不同，A2A 是框架无关的协议标准，旨在让不同供应商的 Agent 能够互相协作。参见 [[wiki/concepts/a2a-agent-to-agent-protocol]] 了解详情。

## 来源

- [[wiki/sources/gemini-enterprise-vs-kubeflow-comparison]]
- [[wiki/sources/gemini-kubeflow-dify-langgraph-comparison]]
- [[wiki/sources/gemini-cli-skills-guide]] — Gemini CLI Skills 机制（ADK 生态中的 CLI 层工具）
- [[wiki/sources/google-a2a-protocol]] — Google A2A 协议详解
