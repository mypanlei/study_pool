---
title: "Vibe Coding 实战指南 — AI 驱动的意图编程范式"
tags:
  - source
  - vibe-coding
  - methodology
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "internal note"
source_author: "自建知识库笔记（基于 Andrej Karpathy 理念）"
source_date: 2026-05-12
---

# Vibe Coding 实战指南

> Vibe Coding 是由 Andrej Karpathy 推广的新型开发范式：通过描述「意图」和「感觉」，由 AI Agent 负责具体实现与调试。

## 核心论点

1. **Spec before Vibe** — Vibe Coding 不等于乱写。核心心法是先有 PLANNING.md（逻辑规划）和 README 驱动（定义交互逻辑）作为 AI 的「北极星指标」。
2. **工具链优化** — Cursor 中使用 `.cursorrules` 定义全局编程规范是减少幻觉的最高效手段；Windsurf 中充分利用 Cascade 的自主终端命令能力。
3. **实战沟通范式** — 原子化交互（一个意图→一次修改→一次验证）、语音输入高吞吐量、对比法（「风格类似 Apple/Stripe」）利用 AI 的审美迁移能力。
4. **风险控制** — 诊断优先（遇到错误先让 AI 解释原因）、测试前置（为所有核心逻辑编写自动化测试）、Git 频繁回滚（警惕 Doom Loop，连续三次失败果断 reset）。
5. **Vibe Coding 与 SDD 的关系** — SDD 可以理解为对 Vibe Coding 的工程化约束和可复现化改造。

## 受影响的 Wiki 页面

- [[wiki/concepts/vibe-coding]] — 已创建
- [[wiki/concepts/spec-driven-development]] — 已关联
