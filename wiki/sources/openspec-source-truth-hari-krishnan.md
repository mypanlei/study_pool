---
title: "OpenSpec Source-of-Truth Specification — Hari Krishnan"
tags:
  - source
  - spec-driven
  - openspec
  - comparison
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://intent-driven.dev/blog/2025/11/09/spec-driven-development-openspec-source-truth/"
source_author: "Hari Krishnan"
source_date: 2025-11-09
aliases:
  - OpenSpec Source of Truth
  - Spec-Kit vs OpenSpec vs Kiro
---

# OpenSpec Source-of-Truth Specification — Hari Krishnan

> Hari Krishnan 深入解析 OpenSpec 的"单一权威规范"（Source of Truth）方案，将其与 Spec-Kit 的碎片化规范方案和 Kiro 进行对比，提出了"一致性层次"框架（Spec-First / Spec-Anchored / Spec-as-Source）。

## 核心论点

1. **碎片化规范的问题**（Spec-Kit / Kiro 方式）：功能级规范分散在子文件夹中 → 理解分散（系统总体意图难以把握）、规范演变（多文件累积导致验证困难）、意外交互（无统一验证视图）。

2. **OpenSpec 的"权威规范"方案**：维护一个持续代表实时系统的顶层规范文档。所有增量变更最终合并到单一文档，可随时根据统一的真实来源规范进行验证。

3. **一致性层次**（引用 Birgitta Böckeler）：
   - **Spec-First**：规范指导初始设计，但实现偏离后可靠性降低
   - **Spec-Anchored**：规范持续与实现同步（OpenSpec 通过权威规范在此层次运作）
   - **Spec-as-Source**：规范即源码

4. **碎片化规范的局限**：随功能弃用/演进，相关规范部分失效 → 本质上仍停留在 Spec-First 范畴。OpenSpec 通过维护权威规范成为 Spec-Anchored 工具。

5. **OpenSpec 实践观察**：快速迭代（提案周期明显快于 Spec-Kit）、心流状态（上下文切换少）、1-N/现有项目定位精准。作者同时是 OpenSpec 和 Spec-Kit 的活跃贡献者。

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — 新增 OpenSpec 权威规范概念、一致性层次框架、碎片化 vs 统一规范对比
