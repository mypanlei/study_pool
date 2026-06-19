---
title: "Agent Harness Engineering"
tags:
  - concept
  - agent
  - architecture
  - engineering
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Harness Engineering
  - 装具工程
  - Agent 运行时工程
---

# Agent Harness Engineering

> 工程化设计「模型在怎样的运行时里完成任务」的学科，通过一套确定性的基础设施（Scaffolding）包裹概率性的模型，将 LLM 从不稳定的「对话者」转化为可靠的「执行者」。

## 定义

Harness Engineering 的核心对象是**模型所在的执行运行时**。它关注 LLM 如何调用工具、多步任务如何编排暂停重试、哪些动作需要权限校验或人工审批、如何记录轨迹和监控成本。

它与 Prompt Engineering（指令层）和 Content Engineering（知识层）共同构成生产级 AI 系统的三层分工：
- **Prompt Engineering**: 怎么告诉模型做事
- **Content Engineering**: 给模型什么知识和上下文
- **Harness Engineering**: 整个系统如何可靠运行

## 三层架构深度解构

### 1. 工具层 (Tool Layer)
- MCP Server：标准化协议接口
- API Proxy：身份验证与审计
- 运行时资源发现

### 2. 智能层 (Intelligence Layer)
- 知识图谱（Knowledge Graph）：长期记忆，四层数据模型
- 向量数据库：短期相关性检索
- 推理记录：历史决策与经验

### 3. 执行运行时 (Execution Runtime)
- Pipeline Engine：任务编排/自愈流
- Sandbox：WASM/Container 隔离环境
- OPA Kernel：确定性护栏拦截

## OPA 治理模式

OPA (Open Policy Agent) 作为 Agent 运行时的决策中枢，实现：
- **保存时强制 (Save-time Enforcement)**：静态分析，拦截不合规的逻辑定义
- **运行时评估 (Run-time Evaluation)**：Agent 执行有副作用操作前必须向 OPA Kernel 发起准入请求

## 自愈闭环

感知 → 根因初查 → 方案生成 → 策略校验 → 审批挂起 → 执行与验证

## 硬件隐喻参考模型

| Harness 组件 | 硬件隐喻 | 功能 |
|-------------|---------|------|
| LLM | CPU | 原始推理与意图理解 |
| Context Window | RAM | 易失性工作内存 |
| Knowledge Graph | Hard Drive | 长期结构化组织记忆 |
| OPA Kernel | OS Kernel | 权限控制与安全护栏 |
| MCP | Syscalls | 与外部世界交互的标准接口 |
| Pipeline | System Bus | 数据流动与任务调度 |

## JavaGuide 六层架构视角

JavaGuide 的 Harness Engineering 文章提出了六层架构视角，将 Harness 拆解为更细粒度的分层：

1. **模型层** — 模型选择、量化、推理优化
2. **上下文层** — Context Window 管理、Token 预算、历史压缩、动态注入
3. **工具层** — Function Calling、MCP 协议、工具注册与动态发现
4. **记忆层** — 短期记忆（对话历史）、长期记忆（知识图谱/向量库）
5. **控制层** — 路由策略、权限校验、人工审批（HITL）、重试与回退
6. **观测层** — 轨迹记录、成本监控、评估回测、告警与自愈

> 六层架构是三层架构的细化版本，适用于工程落地时逐层排查和优化。三层适合概念理解，六层适合生产排障。

## 来源

- [[wiki/sources/harness-engineering-deep-dive]]
- [[wiki/sources/harness-content-prompt-engineering]]
- [[wiki/sources/rookie-harness-engineering]]
- [[wiki/sources/harness-engineering-javaguide]] — 一文搞懂 Harness Engineering (JavaGuide)
