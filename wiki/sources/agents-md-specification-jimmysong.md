---
title: "AGENTS.md 规范 — Jimmy Song AI Handbook"
tags:
  - source
  - spec-driven
  - agent
  - methodology
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://jimmysong.io/zh/book/ai-handbook/sdd/agents/"
source_author: "Jimmy Song"
source_date: 2025-11-02
aliases:
  - AGENTS.md Specification
  - Jimmy Song AGENTS.md
---

# AGENTS.md 规范 — Jimmy Song AI Handbook

> Jimmy Song《AI Handbook》中的 AGENTS.md 规范章节。AGENTS.md 不是提示词，而是 Contract——不是表达模型应该如何思考，而是规定它如何工作、如何输出、如何被审计、如何被回滚。

## 核心论点

1. **AGENTS.md 定位**：用于智能体定义"角色、能力、工具、边界、工作流"的工程化规范文档。是可执行的操作手册，确保智能体行为可控、可复现、可测试。

2. **六大工程要素**：
   - **Commands（可执行命令）**：`npm test`、`pytest -v`、`npm run build` 等
   - **Testing（测试能力）**：测试框架与运行方式
   - **Project Structure（项目结构）**：目录约定与读写权限
   - **Code Style（代码示例）**：真实格式示例
   - **Git Workflow（版本与提交规范）**：分支命名、commit 粒度
   - **Boundaries（操作边界）**：三层边界模型

3. **三层边界模型**：
   - ✅ **必须执行**（Always do）：写入 docs/tests、用命令验证输出、严格格式化
   - ⚠️ **需先询问**（Ask first）：增加依赖、修改配置、重写大段内容
   - 🚫 **禁止操作**（Never do）：修改 src、删除失败测试、修改 CI/CD、提交 secrets

4. **完整结构**：身份定义 → 可执行命令 → 项目知识（文件结构+框架版本）→ 职责范围 → 输出风格（代码示例）→ 三层边界 → 错误处理 → Git 工作流 → 质量标准检查清单。

5. **AGENTS.md vs CLAUDE.md**：AGENTS.md 更聚焦于 Agent 的角色、边界和可执行命令，相当于 Agent 粒度的操作手册；CLAUDE.md 是项目粒度的全局规范。

## 受影响的 Wiki 页面

- [[wiki/concepts/agent-skills-system]] — AGENTS.md 作为 Agent Skills 的一种结构化交付形式
