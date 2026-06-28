---
title: "AI 辅助编程与 AI Specs 实战 — 腾讯云"
tags:
  - source
  - spec-driven
  - comparison
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://cloud.tencent.com/developer/article/2656315"
source_author: "腾讯云开发者社区"
source_date: 2026-04-17
aliases:
  - Tencent Cloud SDD Guide
  - OpenSpec vs SpecKit vs Kiro
---

# AI 辅助编程与 AI Specs 实战 — 腾讯云

> 腾讯云开发者社区发布的 SDD 框架深度对比文章，系统介绍 OpenSpec、GitHub Spec Kit 和 Kiro 三大框架的设计哲学、工作流与适用场景，并探讨 Agentic IDE 和智能体编程趋势。

## 核心论点

1. **范式迁移**：2026 年 AI 编程从"氛围编程"（Vibe Coding）向"规范驱动开发"（SDD）全面迁移。下个瓶颈不再是模型能力，而是人机协作的工程方法论。

2. **三大框架对比**：

| 维度 | OpenSpec | GitHub Spec Kit | Kiro |
|------|----------|-----------------|------|
| 团队 | Fission-AI | GitHub (官方) | AWS |
| 哲学 | 轻量、灵活、增量友好 | 标准化、严谨、宪法先行 | 一体化、Agentic、云原生 |
| 形态 | CLI + 工作流规范 | CLI + 规范模板 | Agentic IDE |
| 学习曲线 | 平缓 | 较陡 | 中等 |
| 场景 | 棕地项目 | 绿地项目/企业合规 | AI Agent 开发/AWS 生态 |
| TDD | 需自行配置 | 内置强制 TDD | 专用 Agent 保障 |

3. **OpenSpec 亮点**：零 API 密钥、棕地优先、三步工作流（New→Apply→Archive）、`.specs/` 目录作为知识库、斜杠命令（`/opsx:propose`）直接集成 IDE。

4. **Spec Kit 亮点**：宪法先行（CONSTITUTION.md）、强制 TDD、四阶段验证流（Specify→Plan→Tasks→Implement）、MIT 开源。

5. **Kiro 亮点**：AWS 出品的 Agentic IDE、双模交互（代码编辑 + 对话规划）、原子化回滚、Specs & Hooks、Security Agent/Performance Agent 等多专业 Agent 协作、云原生集成。

6. **趋势**：开发者从"写代码的实施者"转向"AI 指挥官"，Agentic IDE 崛起、"对话即工程"（Conversation as Engineering）、安全与治理成为核心战场。

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — 新增 OpenSpec/Spec Kit/Kiro 三框架深度对比
