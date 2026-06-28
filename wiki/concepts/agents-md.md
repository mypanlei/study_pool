---
title: "AGENTS.md 规范"
tags:
  - concept
  - agent
  - methodology
  - spec-driven
created: 2026-06-29
updated: 2026-06-29
aliases:
  - AGENTS.md Specification
  - 智能体规范文件
  - Agent Contract
---

# AGENTS.md 规范

> AGENTS.md 不是提示词，而是 Contract——不是表达模型应该如何思考，而是规定它如何工作、如何输出、如何被审计、如何被回滚。

## 定义

AGENTS.md 是用于智能体定义"角色、能力、工具、边界、工作流"的工程化规范文档，由 Jimmy Song 在《AI Handbook》中系统化提出。它是可执行的操作手册，确保智能体行为可控、可复现、可测试。

## 六大工程要素

一个高质量的 AGENTS.md 必须覆盖六个工程要素：

1. **Commands（可执行命令）** — 智能体可运行的命令，如 `npm test --silent`、`pytest -v`、`npm run build` 等
2. **Testing（测试能力）** — 测试框架与运行方式的定义
3. **Project Structure（项目结构）** — 目录约定（src/tests/docs/scripts/config）及读写权限
4. **Code Style（代码示例）** — 真实格式化示例，确保输出一致性
5. **Git Workflow（版本与提交规范）** — 分支命名（`feature/docs-xxx`、`test/fix-xxx`）、原子提交、PR 流程
6. **Boundaries（操作边界）** — 三层边界模型

## 三层边界模型

| 层级 | 含义 | 示例 |
|------|------|------|
| ✅ **必须执行**（Always do） | 智能体可自主执行的操作 | 写入 docs/tests、用命令验证输出、严格格式化 |
| ⚠️ **需先询问**（Ask first） | 需要人工确认后方可执行 | 增加依赖、修改配置、重写大段内容 |
| 🚫 **禁止操作**（Never do） | 任何情况下都不得执行 | 修改 src（非开发 Agent）、删除失败测试、修改 CI/CD、提交 secrets |

## 完整结构

```
AGENTS.md
├── Identity（身份定义）— 名称、角色、专长、技术栈、服务对象
├── Commands（可执行命令）— 测试/构建/检查等命令
├── Project Knowledge（项目知识）
│   ├── File Structure（文件结构）
│   └── Framework & Versions（框架与版本）
├── Responsibilities（职责范围）— 阅读/生成/校验/优化
├── Output Style（输出风格）— 代码和文档格式示例
├── Boundaries（三层边界模型）
├── Error Handling（错误处理）— 不确定则最小安全行动
└── Git Workflow（版本控制规范）
```

## AGENTS.md vs CLAUDE.md

| 维度 | AGENTS.md | CLAUDE.md |
|------|-----------|-----------|
| 粒度 | Agent 粒度的操作手册 | 项目粒度的全局规范 |
| 焦点 | 角色、边界、可执行命令 | 项目约定、技术栈、代码风格 |
| 适用对象 | 单个 Agent/Sub-agent | 整个项目所有 AI 交互 |
| 变化频率 | 随 Agent 角色变化 | 随项目演进变化 |

两者互补：CLAUDE.md 定义项目的全局上下文和约束，AGENTS.md 定义特定 Agent 在项目内的角色和操作边界。

## 与 SDD 的关系

AGENTS.md 是 [[wiki/concepts/spec-driven-development|SDD]] 体系中"约束与假设"要素的落地工具之一。结合 AGENTS.md 可以为 AI Agent 提供持久的项目上下文，与任务特定的 Spec 互补。

## 相关概念

- [[wiki/concepts/agent-skills-system]] — AGENTS.md 是 Agent Skills 的一种结构化交付形式，将 Skill 的操作知识以工程化文件形式表达
- [[wiki/concepts/spec-driven-development]] — AGENTS.md 作为 Spec 体系的持久上下文层
- [[wiki/concepts/guardrails]] — 三层边界模型是 Guardrails 的一种具体实现

## 来源

- [[wiki/sources/agents-md-specification-jimmysong]] — Jimmy Song AI Handbook AGENTS.md 规范章节：六大工程要素、三层边界模型
