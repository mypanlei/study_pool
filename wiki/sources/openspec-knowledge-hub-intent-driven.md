---
title: "OpenSpec Knowledge Hub — Hari Krishnan"
tags:
  - source
  - spec-driven
  - openspec
  - methodology
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://intent-driven.dev/knowledge/openspec/"
source_author: "Hari Krishnan"
source_date: 2025-11-20
aliases:
  - OpenSpec Knowledge Base
  - intent-driven.dev OpenSpec
---

# OpenSpec Knowledge Hub — Hari Krishnan

> Hari Krishnan 维护的 OpenSpec 知识中心，涵盖 OpenSpec 工作流、自定义 schema、与其他 SDD 工具的对比，以及 Git Worktrees 并行开发等高级模式。

## 核心论点

1. **OpenSpec 工作流三工件**：
   - **变更规范（增量规范）**：代表拟议修改的临时文档，章节标记为"新增/修改/删除"
   - **真实性来源规范**：代表系统实际状态的主规范。所有增量变更最终通过归档合并至此
   - **已存档规范**：保留早期增量规范的历史沿革，维护演进审计追踪

2. **Git Worktrees 并行开发**：结合 OpenCode 的子代理，在主分支提出更改 → 子代理在隔离 worktree 应用 → 合并 → 归档。每个子代理在合并前运行验证。

3. **架构决策记录（ADR）集成**：自定义 `spec-driven-with-adr` schema 将 ADR 作为持久工件与权威规范并存。规范记录功能状态，ADR 记录架构状态。

4. **主要优势**：基于规范的对齐（支持在任何阶段根据当前权威规范验证）、更快的迭代周期、棕地支持、特征交互检测、持续验证。

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — OpenSpec 工作流详解、三工件模型、ADR 集成
