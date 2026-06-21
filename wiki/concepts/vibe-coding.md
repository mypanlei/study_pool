---
title: "Vibe Coding"
tags:
  - concept
  - methodology
  - ai
  - development
created: 2026-06-13
updated: 2026-06-21
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

Specification-Driven Development (SDD) 可以理解为对 Vibe Coding 的工程化约束和可复现化改造。两者不是互斥，而是适用于不同阶段。

### 适用场景判断

Vibe Coding 适合：2 天就扔的脚本、一次性 Demo、内部小工具、有完整测试兜底且不直接暴露给外部用户。
Spec Coding 适合：超过一周的代码、多人协作项目、涉及数据持久化和外部接口的系统。

### 轻量 Spec 策略

3-5 天的中间地带可以写轻量 Spec——不用展开完整设计，只写关键约束和验收标准。轻量 Spec 可以简单到："目标+关键约束+验收标准"三段式。

## 核心技巧

### 多模型分工
- 第一步让顶级模型出方案（只讨论方案不写代码）
- 第二步把 Task 丢给低价模型按任务实现
- 第三步让顶级模型 Review diff
- 这样既控制成本又不牺牲质量

### 上下文管理
- 一个会话只处理一个任务
- 长任务及时用 `/compact` 压缩
- 关键进展落到 `NOTES.md` 或 handoff 文档
- 3000-8000 tokens 的高质量上下文通常比几十万 tokens 的杂乱对话更可靠

### Git 工作流
- 开工前 `git status --short` 确认工作区干净
- 开单独分支隔离任务
- 改完后 `git diff --stat` 看影响面再分块提交
- 并行任务用 `git worktree` 隔离

### 权限控制
- AI Coding 不能只靠 Prompt 约束，需用工具强制
- Claude Code: `/permissions` 配置 allow/ask/deny
- 加 Hooks (PreToolUse) 拦截危险命令
- 加 Sandbox 执行环境隔离

## 来源

- [[wiki/sources/vibe-coding-guide]]
- [[wiki/sources/vibe-coding-tips-javaguide]] — Vibe Coding 实用技巧总结：Git/Spec/上下文管理/多 Agent
- [[wiki/sources/spec-coding-javaguide]] — Spec Coding 规范驱动编程，含 Vibe vs Spec 适用边界
- [[wiki/concepts/spec-driven-development]]
