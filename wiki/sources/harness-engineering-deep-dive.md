---
title: "Agent Harness Engineering 深度解析 — 三层架构、知识图谱与 OPA 治理"
tags:
  - source
  - harness
  - agent
  - architecture
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://www.harness.io/products/ai-development"
source_author: "自建知识库笔记"
source_date: 2026-05-12
---

# Agent Harness Engineering 深度解析

> Harness Engineering 已超越 Prompt Engineering，成为构建生产级 AI 系统的主流学科。其核心是将 LLM 从不稳定的「对话者」转化为可靠的「执行者」。

## 核心论点

1. **范式转移** — 从 Oracle-based（LLM 是全知全能的先知）到 Component-based（LLM 是 CPU/推理单元），可靠性来源从更好的 Prompt 转向确定性的运行时与护栏。
2. **三层架构** — 工具层（MCP 标准化接口 + API 审计）、智能层（知识图谱 + 向量数据库 + 推理记录）、执行运行时（Pipeline Engine + Sandbox + OPA Kernel）。
3. **四层数据模型** — Modeled（HQL+图数据库）、Semi-modeled（结构化日志）、Managed（外部集成映射）、External（原始 API 数据），知识图谱实现因果链追踪。
4. **OPA 治理模式** — OPA Kernel 作为 Agent 运行时的决策中枢，实现保存时强制（静态分析）和运行时评估（副作用操作准入），支持上下文感知策略。
5. **自愈闭环** — 感知→根因初查→方案生成→策略校验→审批挂起→执行与验证，构建能自我感知的闭环系统。

## 硬件隐喻参考模型

- LLM = CPU, Context Window = RAM, Knowledge Graph = Hard Drive
- OPA Kernel = OS Kernel, MCP = Syscalls, Pipeline = System Bus

## 受影响的 Wiki 页面

- [[wiki/concepts/harness-engineering]] — 已创建
- [[wiki/concepts/agent-skills-system]] — 已关联
