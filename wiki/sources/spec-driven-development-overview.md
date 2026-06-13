---
title: "Specification-Driven AI Development 开源方案综述 — SDD 生态全景"
tags:
  - source
  - spec-driven
  - methodology
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "internal note"
source_author: "自建知识库笔记"
source_date: 2026-06-09
---

# Specification-Driven AI Development 开源方案综述

> SDD 开源方案到 2025-2026 年已形成较完整生态，主流方案包括 GitHub Spec Kit、OpenSpec、LeanSpec、specs.md、Shotgun 五类。

## 核心论点

1. **SDD 解决的问题** — AI 编码助手在小改动上很好用，但任务跨文件、涉及架构决策时容易偏离目标。共同思路是把需求/设计/任务持久化，让 AI 围绕同一套工件工作。
2. **五个关键特征** — 持久化工件（requirements/spec/design/tasks）、阶段化流程（先 what 再 how）、可重复上下文（新会话可加载工件）、可审查可追踪。
3. **五类方案对比** — Spec Kit（组织级标准化）、OpenSpec（轻量 brownfield）、LeanSpec（兼容现有 issue 体系）、specs.md（严格度可调）、Shotgun（代码库感知的 spec planner）。
4. **行业共识** — 需求/设计/任务必须持久化、AI 需分阶段工作、brownfield 是主战场、文档须是 agent 可消费的上下文资产。
5. **三层落地架构** — 规格层（Spec Kit/OpenSpec）→ 规划层（Shotgun/MetaGPT）→ 执行层（OpenHands/Cursor/Claude Code）。

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — 已创建
- [[wiki/concepts/harness-engineering]] — 已关联
- [[wiki/concepts/vibe-coding]] — 已关联
