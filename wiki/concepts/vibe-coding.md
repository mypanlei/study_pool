---
title: "Vibe Coding"
tags:
  - concept
  - methodology
  - ai
  - development
created: 2026-06-13
updated: 2026-06-13
aliases:
  - 意图编程
  - 氛围编程
---

# Vibe Coding

> Andrej Karpathy 推广的新型开发范式：开发者通过描述「意图（Intent）」和「感觉（Vibe）」，由 AI Agent 负责具体实现与调试。

## 定义

Vibe Coding 的核心不是「乱写」，而是将关注点从语法细节上移到意图层。开发者描述想要什么（而不是怎么实现），AI Agent 理解意图后自主完成编码、调试和验证。

## 核心心法

### Spec before Vibe

在进入 Vibe 状态前，先完成规范定义：
- **PLANNING.md**: 让 AI 先生成逻辑规划文件，确认无误后再执行
- **README 驱动**: 先定义产品交互逻辑和运行方式，作为 AI 的「北极星指标」

### 原子化交互

一个意图 → 一次修改 → 一次验证的闭环。每次只处理一个逻辑单元。

### 工具链优化

- **Cursor**: `.cursorrules` 定义全局编程规范，是减少 AI 幻觉的最高效手段
- **Windsurf**: 充分利用 Cascade 的自主终端命令能力，开发者角色更多是「审计者」

## 风险控制

| 防线 | 方法 |
|------|------|
| 诊断优先 | 遇到错误先让 AI 解释原因，再执行修复 |
| 测试前置 | 要求 AI 为所有核心逻辑编写自动化测试 |
| Git 频繁回滚 | 警惕「毁灭性循环 (Doom Loop)」，连续三次失败果断 reset |

## 与 SDD 的关系

Vibe Coding 提供了快速原型和探索的范式，Specification-Driven Development (SDD) 可以理解为对 Vibe Coding 的工程化约束和可复现化改造。两者不是互斥，而是适用于不同阶段。

## 来源

- [[wiki/sources/vibe-coding-guide]]
- [[wiki/concepts/spec-driven-development]]
