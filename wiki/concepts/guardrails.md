---
title: "Guardrails (Agent 安全护栏)"
tags:
  - concept
  - guardrails
  - safety
  - security
  - agent
  - alignment
created: 2026-06-18
updated: 2026-06-18
aliases:
  - 安全护栏
  - Guardrails
  - AI 安全
  - Agent 防护
  - 输出护栏
---

# Guardrails (Agent 安全护栏)

## 定义

Guardrails（安全护栏）是一套用于控制、约束和监控 AI Agent 行为的防护机制，覆盖**输入验证、行为约束、输出过滤**三个环节。Guardrails 的核心目的是确保 Agent 在自主执行任务时不会产生有害、违规或不可预期的结果，同时保持用户对 Agent 行为的可控性。

在 Agent 工程中，Guardrails 是 Harness Engineering 四道护栏（Context/Constraints/Feedback/Entropy）的重要组成部分。

## 核心要点

- **多层防护**：输入验证 → 注入检测 → 执行约束 → 输出过滤的层层递进
- **不是万能的**：安全是一个持续的过程，没有万无一失的方案
- **可观测性配合**：Guardrails + 日志/追踪/指标形成完整的安全闭环
- **结构性 vs 内容性**：结构性护栏限制行为范围，内容性护栏过滤有害输出
- **HITL 融合**：高风险场景下 Guardrails 触发人工审核（Human-in-the-Loop）

## 详细阐述

### 四层安全架构

```
输入层 → 注入检测层 → 执行层 → 输出过滤层
  │          │            │         │
  ▼          ▼            ▼         ▼
格式验证    Prompt      权限检查    PII 脱敏
长度限制    Injection   工具白名单  内容审核
类型检查    越狱检测    速率限制    合规检查
            恶意输入    资源限制    格式约束
```

### Guardrails 的类型

| 类型 | 描述 | 示例 |
|------|------|------|
| **输入 Guardrails** | 在 User Prompt 进入 LLM 之前过滤 | 长度限制、格式校验、敏感词检测 |
| **注入检测** | 检测并阻止 Prompt Injection / Jailbreaking | 语义分析、模式匹配、异常检测 |
| **行为约束** | 限制 Agent 可执行的操作范围 | 工具白名单、权限控制、操作频率限制 |
| **输出 Guardrails** | 在 LLM 输出返回给用户前过滤 | PII 脱敏、内容审核、格式合规 |
| **流程 Guardrails** | 在 Agent 决策流程中插入检查点 | HITL 审批、二次确认、回滚能力 |

### 常见攻击与防御

| 威胁 | 描述 | 防御措施 |
|------|------|----------|
| **Prompt Injection** | 用户输入中包含恶意指令覆盖 System Prompt | 输入分隔（XML 标签）、指令检测 |
| **Jailbreaking** | 精心构造的提示绕过模型安全对齐 | 多层检测、行为白名单 |
| **工具滥用** | Agent 在授权范围外使用工具 | 细粒度权限控制、操作审计 |
| **数据泄露** | Agent 在输出中暴露敏感信息 | PII 检测、输出过滤 |

### Harness 中的 Guardrails 定位

在 Harness Engineering 四道护栏中：
- **Context**：提供正确的决策上下文（上限）
- **Constraints**：设定明确的约束边界（下限）
- **Feedback**：持续的反馈循环（纠偏）
- **Entropy**：异常检测和熔断机制（应急）

Guardrails 主要对应 Constraints 和 Entropy 两个维度。

## 相关概念

- [[wiki/concepts/harness-engineering]] — Harness 工程中的四道护栏，Guardrails 的理论框架
- [[wiki/concepts/rag-optimization]] — RAG 生成端的 Guardrails（Citation/Context Filtering）
- [[wiki/concepts/prompt-engineering]] — Prompt Engineering 中的防幻觉和注入防御技术

## 来源

- [[wiki/sources/agent-evaluation-safety-alignment]] — 菜鸟教程 Agent 安全防护，含 Guardrails 详解
- [[wiki/sources/rag-common-issues-and-optimization]] — RAG 生成端 Guardrails 实践
- [[wiki/sources/harness-engineering-deep-dive]] — Harness 工程四道护栏架构
