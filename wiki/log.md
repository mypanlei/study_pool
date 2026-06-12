---
title: "Wiki 操作日志"
tags:
  - meta
created: 2026-06-13
updated: 2026-06-13
---

# Wiki 操作日志

> 仅追加的 Chronological 日志，记录所有 Ingest、Query 和 Lint 操作。

---

## [2026-06-13] init | 初始化 LLM Wiki

- 创建三层架构目录结构
- 编写 Schema 配置文档 `.claude/agents/llm-wiki.md`
- 初始化 `wiki/index.md` 和 `wiki/log.md`
- 创建页面模板（entity, concept, source, synthesis）
- 状态：空知识库，待首次 Ingest

## [2026-06-13] ingest | LLM Wiki Pattern (Karpathy)

- 将 5 篇现有 Clippings 复制到 `raw/sources/`
- **完成 Ingest**: `llm-wiki.md` — Karpathy 关于 LLM Wiki 模式的原始文章
- **新建源摘要**: [[wiki/sources/llm-wiki-pattern]]
- **新建概念页**: [[wiki/concepts/llm-wiki-pattern]], [[wiki/concepts/rag-vs-wiki]], [[wiki/concepts/memex]]
- **新建实体页**: [[wiki/entities/andrej-karpathy]]
- **更新**: `wiki/index.md`
- **待处理源材料**: 4 篇在 `raw/sources/` 中等待 Ingest

## [2026-06-13] ingest | Skill 的管理方法（知乎）

- **完成 Ingest**: 知乎文章《Skill 的管理方法》（130+ Skill 的跨设备管理方案）
- **新建源摘要**: [[wiki/sources/skill-management-zhihu]]
- 文章核心贡献：全局目录 (`~/.claude/skills/`) 作为 Single Source of Truth、跨设备同步方案（GitHub + NAS/rsync）、分类公开仓库、元 Skill 概念
- **更新**: [[wiki/syntheses/claude-skill-management]] — 新增策略 D（全局目录式）、跨设备同步、元 Skill 章节

## [2026-06-13] synthesis | Claude Code Skill Management 指南

- **新建综合分析页**: [[wiki/syntheses/claude-skill-management]]
- 盘点全盘技能生态：1 个 Agent (llm-wiki)、1 个 Skill (tailored-resume-generator)、9 个工作区 Repo、35+ 官方 Marketplace 插件
- 记录三种技能管理策略（内嵌 / Symlink / 独立仓库）
- 推荐新建 `my-skills` 集中仓库 + Symlink 方案
- **更新**: `wiki/index.md`

## [2026-06-13] ingest | 批量处理剩余 4 篇源材料

### 1. Claudian 安装教程
- **源摘要**: [[wiki/sources/claudian-setup-guide]]
- **新实体**: [[wiki/entities/claudian]], [[wiki/entities/claude-code]]

### 2. Obsidian 同步方案 (2 篇)
- **源摘要**: [[wiki/sources/obsidian-sync-7-solutions]], [[wiki/sources/obsidian-sync-6-solutions]]
- **综合分析**: [[wiki/syntheses/obsidian-sync-comparison]] — 合并两篇内容并与你当前方案做对照

### 3. Hermes Agent 文档
- **源摘要**: [[wiki/sources/hermes-agent-docs]]
- **新实体**: [[wiki/entities/hermes-agent]], [[wiki/entities/nous-research]]
- **新概念**: [[wiki/concepts/agent-skills-system]]

### 汇总
- **本次新增**: 4 源摘要 + 4 实体 + 1 概念 + 1 综合分析 = 10 页面
- **更新**: `wiki/index.md`
- **状态**: `raw/sources/` 全部 6 篇源材料已全部 Ingest 完成
