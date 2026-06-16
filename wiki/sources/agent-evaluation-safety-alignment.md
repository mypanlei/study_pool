---
title: "Agent 评估、安全与对齐 — 菜鸟教程"
tags:
  - source
  - agent
  - evaluation
  - safety
  - alignment
  - security
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/evaluation-safety-alignment.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Agent 评估、安全与对齐

> 系统介绍 Agent 的评测体系（指标、Benchmark、评估框架）、安全威胁（提示注入、越狱、数据污染）、防护策略（多层安全检查、Guardrails）、可观测性（日志/Tracing/指标）和人机协同（HITL）。

## 核心内容

1. **评测维度** — 任务完成度、效率指标、质量指标、鲁棒性。
2. **常用 Benchmark** — GAIA、MMLU、HumanEval、HotpotQA、AgentBench。
3. **安全威胁** — 提示注入（Prompt Injection）、越狱（Jailbreaking）、数据污染、敏感信息泄露。
4. **防护策略** — 四层安全架构：输入验证→注入检测→执行核心逻辑→输出过滤。
5. **可观测性** — 日志（Logging）、追踪（Tracing）、指标（Metrics）三大支柱，含 OpenTelemetry 集成示例。
6. **人机协同** — HITL（Human-in-the-Loop）的高/中/低三档风险分级审批模型。

## 关键概念

- 安全是一个持续的过程，没有万无一失的方案
- Guardrails 侧重于输出质量和合规性
- HITL 在高风险场景中引入人工审核
