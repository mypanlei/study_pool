---
title: "规范驱动开发（SDD）简介 — Jimmy Song AI Handbook"
tags:
  - source
  - spec-driven
  - methodology
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://jimmysong.io/zh/book/ai-handbook/sdd/overview/"
source_author: "Jimmy Song"
source_date: 2025-11-03
aliases:
  - Jimmy Song SDD Overview
  - AI Handbook SDD
---

# 规范驱动开发（SDD）简介 — Jimmy Song AI Handbook

> Jimmy Song《AI Handbook》中的 SDD 章节。从 Vibe Coding 到 SDD 的范式迁移视角出发，详细阐述了 AI 编程协议栈（MCP/A2A/AG-UI）、五大核心能力、SDD 工具全景（Kiro/Spec-kit/Tessl/Qoder/AgentScript/CodePlan）及其对 AI Agent 规划可控性的支撑。

## 核心论点

1. **范式迁移三阶段**：IDE 时代（工具辅助）→ AI 编程时代（协作式创造）→ Vibe Coding 时代（流体化共创）。SDD 是 Vibe Coding 的工程化约束。

2. **AI 编程协议栈三层模型**：
   - MCP（Model-Context Protocol）：定义 AI 与工具的交互方式
   - A2A（Agent-to-Agent Protocol）：多智能体协作
   - AG-UI（Agent-User Interaction）：用户与 Agent 的实时可视交互

3. **五大核心能力**：结构化任务分解、智能上下文工程、标准化交付体系、测试驱动的自愈式开发（Self-Healing TDD）、质量驱动的持续优化。

4. **SDD 落地工具全景**（超越主流三大框架）：Kiro（VS Code 插件）、Spec-kit（GitHub CLI）、Tessl Framework（代码反推规范、`@generate`/`@test` 标签）、Qoder（规范即代码编程助手）、AgentScript（计划代码 AST 可审查执行）、CodePlan（学术框架，规划图+验证反馈）。

5. **准确率框架**：成功率 ≥90%、可部署率 ≥85%、返工率 ≤10%——当某类任务稳定在 90% 以上时 AI 才从实验变为生产力。

6. **哲学转变**：从"自由生成"到"规范生成"。开发者角色转向"设计系统语义的人"——定义 Prompt 模板、上下文结构、评测指标与协作协议。

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — 新增 AI 编程协议栈三层模型、工具全景（Tessl/AgentScript/CodePlan/Qoder）、准确率框架
