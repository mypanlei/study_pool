---
title: "多 AI 协同 + SDD 编程实践：一个 AI 全流程交付实录"
tags:
  - source
  - sdd
  - spec-driven-development
  - multi-agent
  - openspec
  - practice
created: 2026-06-30
updated: 2026-06-30
source_url: "https://zhuanlan.zhihu.com/p/2000568085258712069"
source_author: "千问云"
source_date: 2026-02-03
aliases:
  - SDD 多 AI 协同实践
  - 千问云 SDD 实践
  - Claude Codex Gemini 协作
---

# 多 AI 协同 + SDD 编程实践：一个 AI 全流程交付实录

> 基于 OpenSpec 构建由 Claude Code、CodeX 与 Gemini 协同驱动的 SDD 编程工作流，并从零交付一个跨境保险产品的全流程实践记录。核心思路：通过 MCP 协议将 Codex 和 Gemini 作为工具注入 Claude，实现"Claude 统筹 + Codex 实现 + Gemini 分析"的铁三角协作模式。

## 核心论点

1. **从 Vibe Coding 到 SDD 是必然演进** — AI 编码已深度融入研发流程，但仅靠"写得快"远远不够，关键在于"写得对"。SDD 的规范先行、分阶段验证、多 AI 协同三大核心理念是从 Vibe Coding 到可靠交付的核心转型路径。

2. **多 AI 模型协作是复杂任务的必然选择** — 任务越复杂，越需要多个 AI 模型的能力互补（Claude 的推理、Codex 的编码、Gemini 的大文本分析），但手动切换工具的成本抵消了 AI 的提效红利。解决方案是通过 MCP 协议将多模型注入同一入口。

3. **OpenSpec 适合棕地工程落地** — 相比 BMAD 和 Spec Kit，OpenSpec 的轻量可嵌入、多 AI 友好、变更可管理三大特性使其最适合实际工程场景。

4. **标准化工作流程是协作质量的保障** — 通过 CLAUDE.md/AGENTS.md 的强制规则 + 标准化 4 步循环（理解→实现→分析→撰写）+ 职责清晰的角色分工，确保多模型协作不失控。

## 架构设计

### 多 AI 角色分工

| 模型 | 角色 | 核心职责 | 配置文件 |
|------|------|----------|----------|
| **Claude** | 协调者 (Orchestrator) | 理解目标、拆分工作、决定何时调用其他模型、应用最终代码、撰写最终文本 | CLAUDE.md |
| **Codex** | 高级工程师 | 非平凡代码/实验任务：设计、实现、调试、重构、实验 Pipeline | AGENTS.md |
| **Gemini** | 大文本分析师 | 多论文/长文档/大代码库分析：全局视图、模式发现 | AGENTS.md |

### 关键的强制规则

CLAUDE.md 中的核心指令：
> "For any task that is more than a trivial edit, you MUST ask: 'Can Codex help with code here? Can Gemini help with large-context analysis here?'"

这意味着工具调用是默认行为，而非可选项。

### 4 步标准化工作流

1. **理解与规划 (Understand & Plan)** — Claude 澄清目标 → 调用 Codex 细化方案 → 调用 Gemini 获取全局视图
2. **实现与运行 (Implement & Run)** — 向 Codex 请求 unified diff 原型 → Claude 审查改进后应用
3. **审查与分析 (Review & Analyze)** — Codex 做代码审查 → Gemini 分析测试日志/异常模式 → 冲突时 Claude 仲裁
4. **撰写 (Write)** — Gemini 总结法规要点 → Codex 校验代码与文档一致性

### 三文件保障体系

- **CLAUDE.md** — 主控面板，定义 Claude 作为协调者的决策框架和标准工作流
- **AGENTS.md (Codex)** — Codex 的行为规范，定义工作目录、沟通方式、验证标准
- **AGENTS.md (Gemini)** — Gemini 的行为规范，定义 read-only 分析师角色边界

## 实践六阶段

1. **Spec-PRD 生成** — 将原始 PRD 结构化重写为 Spec-PRD，明确变更内容与代码库的映射关系
2. **系统架构总结** — 通过系统架构专家 SubAgent 分析现有代码库，输出架构文档
3. **技术方案生成** — 基于 Spec-PRD + 架构文档，调用技术方案专家 SubAgent 自动生成可执行方案
4. **OpenSpec 变更提案** — 通过 `/openspec:proposal` 创建变更提案（含 specs/ 和 tasks.md）
5. **分阶段变更实现** — 通过 `/openspec:apply` 触发编码，关键约束：每完成一个阶段必须暂停等待人工 Review，降低"错上加错"风险
6. **提案归档** — 验证通过后通过 `/openspec-archive` 归档

## 关键设计决策

- **Gemini 默认为 read-only 分析师**：所有实现与最终决策由 Claude（人类监督下）完成，确保安全可控
- **分阶段交互式开发**：限制 AI 一口气生成全部代码，每阶段结束后必须总结变更并等待人工 Review
- **工具无关性**：当 Claude 服务不可用时（如 CloudFlare 故障），可无缝切换至其他 AI Coding CLI（如 iflow），OpenSpec 的"工具无关，规范驱动"理念得到验证

## 关键引用

> "AI 模型的输出天然带有概率性与模糊性——无论是单 AI 还是多 AI 协作，若放任其自由发挥，看似高效的'全自动编码'反而会引入难以追溯的隐性风险。"

> "SDD 通过规范对齐，让 AI 的'概率输出'最终汇聚为'确定交付'。"

> "这不是试图消除 AI 的不确定性，而是将其引导至一个可预测、可验证、可干预的轨道上。"

## 与现有知识的关系

- 补充 [[wiki/concepts/spec-driven-development]] 中 OpenSpec 部分，提供完整的端到端六阶段实践案例
- 与 [[wiki/sources/openspec-knowledge-hub-intent-driven]] 和 [[wiki/sources/openspec-source-truth-hari-krishnan]] 互补，从工具介绍层面延伸到实际工程落地
- 与 [[wiki/sources/sdd-with-claude-code-heeki-park]] 互补，提供"多 AI 协同"这一新的实践维度
- 与 [[wiki/concepts/agents-md]] 相关，文中展示了 AGENTS.md 在多模型协作中的实际配置

## 个人思考

- 本文最大的价值在于提出了"多 AI 协作"的可行工程架构：通过 MCP 协议将多个模型的能力注入单一入口，而不是让用户在不同工具间手动切换
- CLAUDE.md 的强制规则设计是保障协作质量的关键——不是建议而是 MUST，工具调用是默认而非可选项
- "分阶段 + 人工 Review"是降低 AI 犯错成本的关键实践，与 SDD 概念页中的"Spec-Anchored"模式一致
- 文中 Claude 服务故障时无缝切换至 iflow 的经历，验证了 OpenSpec "工具无关，规范驱动"理念的实际价值
