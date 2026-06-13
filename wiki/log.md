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

## [2026-06-13] ingest | 批量 Ingest 剩余 18 篇源材料

这是截至目前最大的一次批量 Ingest，覆盖 AI Agent 架构、平台对比、Harness Engineering、SDD、Vibe Coding 等主题。

### 1. AI Agent 架构与框架全景指南
- **源摘要**: [[wiki/sources/ai-agent-architecture-overview]]
- 贡献：ReAct/Plan-and-Execute/混合架构模式梳理，2025 主流框架对比（LangGraph/CrewAI/LlamaIndex/AutoGen/Pydantic AI/Mastra）

### 2. Claude Code 自定义 Agent 配置指南
- **源摘要**: [[wiki/sources/claude-code-custom-agent-guide]]
- 贡献：Subagent 创建方法、frontmatter 字段详解、工具权限最小化原则、常见 Agent 模板

### 3. Cursor Agent vs Skill 使用决策指南
- **源摘要**: [[wiki/sources/cursor-agent-vs-skill-guide]]
- 贡献：Agent/Skill/Subagent 完整分工体系、四种工作模式（Agent/Plan/Debug/Multitask）、决策树

### 4. Gemini Enterprise Agent Platform vs Kubeflow 对比
- **源摘要**: [[wiki/sources/gemini-enterprise-vs-kubeflow-comparison]]
- **新实体**: [[wiki/entities/google-adk]], [[wiki/entities/kubeflow]]
- 贡献：两层分层对比框架、误区澄清、组合推荐

### 5. Gemini/Kubeflow/Dify/LangGraph 四方对比
- **源摘要**: [[wiki/sources/gemini-kubeflow-dify-langgraph-comparison]]
- **新实体**: [[wiki/entities/dify]], [[wiki/entities/langgraph]]
- 贡献：四层分层框架、核心对比矩阵、典型组合方式

### 6. Harness/Content/Prompt Engineering 区别与联系
- **源摘要**: [[wiki/sources/harness-content-prompt-engineering]]
- **新概念**: [[wiki/concepts/harness-engineering]]
- 贡献：三层工程体系的理论框架、分层判断方法

### 7. Harness Engineering 深度解析
- **源摘要**: [[wiki/sources/harness-engineering-deep-dive]]
- 贡献：三层架构深度解构、四层数据模型、OPA 治理模式、自愈闭环、硬件隐喻模型

### 8. Hermes Agent 阿里云消息入口实操
- **源摘要**: [[wiki/sources/hermes-agent-alicloud-messaging-guide]]
- 贡献：飞书 WebSocket vs Webhook、微信 iLink 限制、落地顺序建议

### 9. Hermes Agent 阿里云部署指南
- **源摘要**: [[wiki/sources/hermes-agent-alicloud-deployment-guide]]
- 贡献：ECS + Docker + systemd 全流程、安全规范、Provider 选择

### 10. LLM Skills 技术全景指南
- **源摘要**: [[wiki/sources/llm-skills-technical-guide]]
- 贡献：调度员模式、MCP 协议详解、Agent Skills 三级渐进披露机制、Function Calling 原理

### 11. LangGraph ReAct Agent 实战指南
- **源摘要**: [[wiki/sources/langgraph-react-agent-guide]]
- 贡献：状态机工程化、`create_react_agent` vs `StateGraph` 双方案、Checkpointer 记忆管理

### 12. OpenClaw/Hermes/Pi/Claude Code/Codex/Copilot 区别
- **源摘要**: [[wiki/sources/openclaw-hermes-pi-codex-copilot-comparison]]
- **新实体**: [[wiki/entities/openclaw]], [[wiki/entities/pi-agent]]
- 贡献：6 大平台/工具的定位分层、选型框架

### 13. OpenClaw vs Hermes Agent 详细对比
- **源摘要**: [[wiki/sources/openclaw-vs-hermes-comparison]]
- 贡献：设计中心差异、入口模型对比、记忆与技能系统差异、Provider 策略对比

### 14. Pi/Claude Code/Codex 区别
- **源摘要**: [[wiki/sources/pi-claude-codex-comparison]]
- 贡献：三种编码 Agent 的执行模型差异、常见误区澄清

### 15. Pi vs Claude Code vs Codex English Presentation
- **源摘要**: [[wiki/sources/pi-claude-codex-english-presentation]]
- 贡献：英文版企业演示材料

### 16. RAG/Skill/Agent 区别与联系
- **源摘要**: [[wiki/sources/rag-skill-agent-differences]]
- 贡献：三层能力体系理论、组合使用模式、常见误区澄清、判断框架

### 17. Specification-Driven AI Development 综述
- **源摘要**: [[wiki/sources/spec-driven-development-overview]]
- **新概念**: [[wiki/concepts/spec-driven-development]]
- 贡献：SDD 开源生态全景（Spec Kit/OpenSpec/LeanSpec/specs.md/Shotgun）、三层落地架构

### 18. Vibe Coding 实战指南
- **源摘要**: [[wiki/sources/vibe-coding-guide]]
- **新概念**: [[wiki/concepts/vibe-coding]]
- 贡献：Spec before Vibe 心法、风险控制四道防线、与 SDD 的关系

### 综合分析
- **新建综合分析页**: [[wiki/syntheses/ai-agent-ecosystem-comparison]]
- 综合 4 组对比分析文章，构建三层分层框架（应用交付层/编排层/平台层）
- 覆盖企业平台、编程 Agent、Personal AI Agent 三大子生态
- 提供全局选型决策树

### 汇总
- **本次新增**: 18 源摘要 + 6 实体 + 3 概念 + 1 综合分析 = 28 页面
- **更新**: `wiki/index.md`, `wiki/log.md`
- **状态**: `raw/sources/` 全部 24 篇源材料已全部 Ingest 完成

## [2026-06-13] feature | Dataview 标签索引页

- **新建**: [[wiki/tag-index]] — 使用 Dataview 动态查询生成的标签导航页
- 安装 Dataview 社区插件（加入 community-plugins.json）
- 索引覆盖 11 个标签分组（agent, ai, claude, obsidian, hermes, comparison, methodology, gemini/kubeflow, openclaw/pi, sync, harness）
- 包含标签云（按频率排序）和最近更新列表
- **更新**: `wiki/index.md` — 添加标签索引入口链接
- **全文索引统计**: 11 实体 + 7 概念 + 24 源摘要 + 3 综合分析 = 45 页面
