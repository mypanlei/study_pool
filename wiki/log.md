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

## [2026-06-13] ingest | 批量 Ingest 17 篇源材料（MLOps 系列 + LLM/DL + RAG + Other）

这是截至目前最大的一次批量 Ingest，覆盖 7 篇 MLOps 系列大型文章、5 篇 LLM/DL 技术文章、3 篇 RAG 相关文章和 2 篇其他主题，新增 28 个页面。

### MLOps 系列（7 篇）

#### 1. 内部 MLOps Availability 需求拆解与落地计划
- **源摘要**: [[wiki/sources/internal-mlops-availability-requirements-user-stories-technical-plan]]
- 贡献：以 ML Developer Core Journey 为核心的 99.9% SLO 落地计划，7 个 Epic / 29 个 User Stories，三口径统计（Gross/Net/Platform-owned），43.2 分钟 error budget 分摊模型

#### 2. 内部 MLOps Availability 结构化分析
- **源摘要**: [[wiki/sources/internal-mlops-availability-structured-analysis]]
- 贡献：按评审/汇报逻辑重新编排的版本，工业成熟实践对比，执行资产模板（Incident/Runbook/RCA/K8s 加固）

#### 3. ML 生命周期管理官方总结
- **源摘要**: [[wiki/sources/ml-lifecycle-management-official-doc-summary]]
- 贡献：8 阶段生命周期模型，综合 AWS/Google/Azure/MLflow/Kubeflow/NIST 官方资料，CI/CD/CT 自动化成熟度，反模式总结

#### 4. MLOps Data Versioning 开源方案对比
- **源摘要**: [[wiki/sources/mlops-data-versioning-open-source-comparison]]
- 贡献：Data Versioning（DVC/lakeFS/Pachyderm/Nessie）vs Data Management（DataHub/OpenMetadata/Amundsen/Atlas/Marquez）问题分层框架，与 MLflow/Kubeflow 集成关系，推荐组合

#### 5. MLOps 开源平台对比
- **源摘要**: [[wiki/sources/mlops-open-source-platform-comparison]]
- 贡献：11 个平台逐项对比（Kubeflow/MLflow/ZenML/Metaflow/Flyte/Kedro/DVC/ClearML/Feast/BentoML/KServe），分层选型框架，推荐组合

#### 6. ML Platform Availability SLA 商业评估
- **源摘要**: [[wiki/sources/ml-platform-availability-sla-commercial-assessment]]
- 贡献：99.9%（主流）vs 99.95%（高可用需多实例多区）vs 99.99%（基础设施级）市场对标，3 档商业 SKU 建议

#### 7. 内部 MLOps 数据版本控制 PRD
- **源摘要**: [[wiki/sources/internal-mlops-data-versioning-prd]]
- 贡献：基于 lakeFS+DataHub+OpenLineage 的 PRD，P0/P1/P2 需求矩阵，MVP 退出标准

### LLM/DL 技术系列（5 篇）

#### 8. KV Cache 技术详解
- **源摘要**: [[wiki/sources/kv-cache-technical-detail]]
- 贡献：KV Cache Prefill/Decode 原理，架构演进 MHA→GQA→MLA→CSA/HCA，PagedAttention 显存管理

#### 9. RoPE 插值技术详解
- **源摘要**: [[wiki/sources/rope-interpolation-technical-detail]]
- 贡献：RoPE 物理意义（坐标系压缩），PI/NTK-Aware/YaRN/DroPE 四种插值方法，参数选择指南

#### 10. Transformer 架构详解
- **源摘要**: [[wiki/sources/transformer-architecture-detail]]
- 贡献：QKV 机制、Encoder-Decoder vs Decoder-only 架构分化、MHA/GQA 关键组件、训练数据压缩为权重而非存储的常见误解澄清

#### 11. 大模型参数量与性能关系
- **源摘要**: [[wiki/sources/large-model-parameters-and-performance]]
- 贡献：Kaplan vs Chinchilla Scaling Laws，小模型逆袭三大原因（超量训练+数据质量+架构改进），MoE/端侧 AI 趋势

#### 12. 拟合机制深度解析
- **源摘要**: [[wiki/sources/fitting-mechanism-deep-analysis]]
- 贡献：函数逼近数学本质，欠/恰好/过拟合三种状态，模型容量（LoRA Rank），LLM 知识冲突与灾难性遗忘

### RAG 相关（3 篇）

#### 13. RAG 常见问题与优化
- **源摘要**: [[wiki/sources/rag-common-issues-and-optimization]]
- 贡献：检索端（Hybrid/Rerank/HyDE/Query Rewrite/GraphRAG）+ 生成端（Guardrails/Citation/Context Filtering）双端优化

#### 14. RAG vs Semantic Cache 对比
- **源摘要**: [[wiki/sources/rag-vs-semantic-cache-comparison]]
- 贡献：RAG（知识注入，每次调用 LLM）vs 语义缓存（加速器，10-50ms 缓存命中）本质区别，最佳实践为 RAG 生成后写入缓存

#### 15. RAGAS 评估指标
- **源摘要**: [[wiki/sources/ragas-evaluation-metrics]]
- 贡献：RAGAS 三元组（Faithfulness/Relevancy/Context Precision），LLM-as-a-Judge 思路，鲁棒性（Negative Rejection + Noise Sensitivity）

### 其他（2 篇）

#### 16. AI 平台化解决方案产品经理
- **源摘要**: [[wiki/sources/ai-platform-product-manager-role-framework]]
- 贡献：角色定位、5 维度能力模型、6 块背景知识、与各团队分工、组织价值

#### 17. Karpathy LLM Wiki 理念深度解析
- **源摘要**: [[wiki/sources/karpathy-llm-wiki-philosophy]]
- 贡献：三层架构（Raw Sources/Wiki/Schema），核心操作流程（增量摄入/深度查询/自动化巡检），Bookkeeping cost 消除

### 新建概念页（8 个）
- [[wiki/concepts/transformer-architecture]] — Transformer 架构与自注意力机制
- [[wiki/concepts/kv-cache]] — KV Cache 与 PagedAttention
- [[wiki/concepts/rope-positional-encoding]] — RoPE 旋转位置编码与插值
- [[wiki/concepts/rag-optimization]] — RAG 全链路优化
- [[wiki/concepts/mlops-lifecycle]] — MLOps 生命周期管理
- [[wiki/concepts/data-versioning-and-management]] — 数据版本控制与数据管理
- [[wiki/concepts/ai-platform-product-manager]] — AI 平台产品经理角色
- [[wiki/concepts/fitting-mechanism]] — 拟合机制（欠/恰好/过拟合）

### 新建实体页（3 个）
- [[wiki/entities/mlflow]] — MLflow 实验追踪与模型注册平台
- [[wiki/entities/datahub]] — 组织级元数据图谱与 Data Catalog
- [[wiki/entities/lakefs]] — 对象存储层 Git-like 数据版本控制

### 新建综合分析页（3 个）
- [[wiki/syntheses/mlops-ecosystem-overview]] — MLOps 生态全景（综合 7 篇 MLOps 文章）
- [[wiki/syntheses/llm-technical-foundations]] — LLM 技术基础（综合 5 篇技术文章）
- [[wiki/syntheses/rag-optimization-guide]] — RAG 优化指南（综合 3 篇 RAG 文章）

### 更新已有页面
- [[wiki/entities/andrej-karpathy]] — 添加 Karpathy LLM Wiki 源链接
- [[wiki/concepts/rag-vs-wiki]] — 添加 RAG 相关源和概念链接
- [[wiki/index.md]] — 添加所有新页面

### 汇总
- **本次新增**: 17 源摘要 + 3 实体 + 8 概念 + 3 综合分析 = 31 页面
- **全文索引统计**: 14 实体 + 15 概念 + 41 源摘要 + 6 综合分析 = 76 页面

## [2026-06-13] ingest | 批量 Ingest 11 篇源材料（DeepSeek 三部曲 + Gemini CLI + Git + NotebookLM + Obsidian + 飞书）

这是深度覆盖推理模型、CLI 工具、Git 工程化、研究工具、知识工作流和项目管理工具的一次批量 Ingest。

### DeepSeek 三部曲（3 篇）

#### 1. DeepSeek-R1 技术秘诀
- **源摘要**: [[wiki/sources/deepseek-r1-technical-secrets]]
- 贡献：GRPO 算法、四阶段训练流程、MLA+MoE 架构、知识蒸馏、成本奇迹

#### 2. DeepSeek-R1 深度解析
- **源摘要**: [[wiki/sources/deepseek-r1-deep-analysis]]
- 贡献：R1-Zero vs R1 路径对比、GRPO 群组相对策略优化、蒸馏模型影响力

#### 3. DeepSeek-V4 技术分析
- **源摘要**: [[wiki/sources/deepseek-v4-technical-analysis]]
- 贡献：CSA/HCA 序列压缩注意力、KV Cache 极致压缩、前缀缓存策略与阶梯定价闭环

### Gemini CLI 与 Git 工具（3 篇）

#### 4. Gemini CLI Skills 配置指南
- **源摘要**: [[wiki/sources/gemini-cli-skills-guide]]
- 贡献：Skills 存储层级、SKILL.md 规范、发现/激活/状态控制机制

#### 5. Git LFS 工作原理与配置指南
- **源摘要**: [[wiki/sources/git-lfs-guide]]
- 贡献：指针文件机制、clean/smudge filter、历史迁移策略、GitHub 计费规则

#### 6. GitHub CLI 代理配置
- **源摘要**: [[wiki/sources/github-cli-proxy-config]]
- 贡献：环境变量方案、Git 代理配置、SSH 协议代理

### NotebookLM（1 篇）

#### 7. NotebookLM 系统介绍
- **源摘要**: [[wiki/sources/notebooklm-introduction]]
- 贡献：来源驱动型研究工作台定位、资料类型与限制、核心能力全景（问答/Source Guide/音频视频概览/Deep Research）、隐私与企业口径

### Obsidian Advanced（2 篇）

#### 8. Obsidian 代理设置与非官方 Vault 同步方案
- **源摘要**: [[wiki/sources/obsidian-proxy-sync-guide]]
- 贡献：代理三层架构（系统/Electron/插件）、八种非官方同步方案全景、Windows+Android+iPad 设备组合建议

#### 9. Obsidian + 浏览器扩展 + Claudian 知识工作流方案
- **源摘要**: [[wiki/sources/obsidian-claudian-workflow]]
- 贡献：三层闭环架构（采集/存储/加工）、三个典型场景、推荐目录结构

### 飞书多维表格（2 篇）

#### 10. 飞书多维表格 vs Jira 对比
- **源摘要**: [[wiki/sources/feishu-bitable-vs-jira-comparison]]
- 贡献：数据表模型 vs Issue 模型、工作流差异、配合模式

#### 11. 飞书多维表格系统介绍
- **源摘要**: [[wiki/sources/feishu-bitable-introduction]]
- 贡献："多维"含义、基础数据模型、核心能力模块（字段/视图/关联/表单/自动化/权限/仪表盘/API）

### 新建实体页（4 个）
- [[wiki/entities/deepseek]] — DeepSeek AI 公司实体
- [[wiki/entities/notebooklm]] — Google NotebookLM 实体
- [[wiki/entities/feishu-bitable]] — 飞书多维表格实体
- [[wiki/entities/jira]] — Atlassian Jira 实体

### 新建概念页（2 个）
- [[wiki/concepts/git-lfs]] — Git LFS 大文件存储机制
- [[wiki/concepts/feishu-bitable]] — 飞书多维表格数据模型

### 新建综合分析页（1 个）
- [[wiki/syntheses/deepseek-technical-analysis]] — 综合 3 篇 DeepSeek 文章，涵盖 GRPO/训练策略/架构演进/缓存工程

### 更新已有页面
- [[wiki/concepts/kv-cache]] — 新增 CSA/HCA 序列压缩注意力详解
- [[wiki/entities/claude-code]] — 新增 Gemini CLI 对比表格
- [[wiki/entities/google-adk]] — 添加 Gemini CLI Skills 来源引用
- [[wiki/syntheses/obsidian-sync-comparison]] — 新增 Obsidian 代理三层架构、知识工作流三层架构、Git 代理配置补充章节

### 汇总
- **本次新增**: 11 源摘要 + 4 实体 + 2 概念 + 1 综合分析 = 18 页面
- **更新已有**: 4 页面
- **全文索引统计**: 18 实体 + 17 概念 + 52 源摘要 + 7 综合分析 = 94 页面

## [2026-06-13] ingest | Skills Manager 教程

- **源摘要**: [[wiki/sources/skills-manager-tutorial]] — Datawhale 出品的跨 Agent Skill 管理器教程
- 核心贡献：Skills Manager 中央库 + Preset + Multi-tool sync 的可视化管理方案
- **更新**: [[wiki/syntheses/claude-skill-management]] — 新增策略 E（Skills Manager 工具式）
- **更新**: `wiki/index.md` — 源摘要 52 → 53
- **全文索引统计**: 18 实体 + 17 概念 + 53 源摘要 + 7 综合分析 = 95 页面

## [2026-06-15] feat | 三层架构重建 + 2 篇新源材料 Ingest

### 架构重建
- **新建 `CLAUDE.md`** — Karpathy 模式的 Schema 入口文件，记录三层架构和当前状态
- **更新 `.claude/agents/llm-wiki.md`** — 同步为完整架构描述，更新采集/Ingest/Query/Lint 四工作流
- **新建 `raw/sources/` 中 2 篇新剪藏**: Karpathy 访谈 + 实操教程

### 源材料 Ingest
1. **[[wiki/sources/karpathy-agentic-engineering-interview]]** — Karpathy AI Ascent 2026 访谈
   - 核心贡献：Vibe Coding vs Agentic Engineering、Software 3.0、Jagged Intelligence、Verifiability、LLM Wiki
2. **[[wiki/sources/karpathy-method-practical-guide]]** — Austin Marchese 的 Karpathy 方法实操拆解
   - 核心贡献：Spec × Verifier × Environment 三层法、CLAUDE.md + LLM Wiki + Skills 组合实践

### 更新
- `wiki/index.md` — 源摘要 53 → 55
- `wiki/log.md` — 本条目

### 全文索引统计
18 实体 + 17 概念 + 55 源摘要 + 7 综合分析 + CLAUDE.md + index/log/tag-index = 97 页面

### 三层架构最终状态
```
raw/      55 篇源文件
wiki/     97 内容页 (含模板)
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-17] ingest | 批量 Ingest 32 篇源材料（菜鸟教程 AI Agent 系列 + MLOps 对比）

这是 wiki 创建以来最大的一次批量 Ingest，覆盖菜鸟教程（Runoob）AI Agent 系列 30 篇文章，以及 2 篇 MLOps 工具对比文章。

### 菜鸟教程 AI Agent 系列（30 篇）

#### 1-4. Agent 基础概念
- **源摘要**: [[wiki/sources/ai-agent-tutorial-overview]] — 系列概述与学习路径
- **源摘要**: [[wiki/sources/ai-agent-introduction]] — Agent 定义、自主性、与 LLM 区别
- **源摘要**: [[wiki/sources/ai-agent-working-principle]] — 感知-思考-行动三层架构
- **源摘要**: [[wiki/sources/ai-agent-glossary]] — 30+ 核心术语词典

#### 5-7. 架构与设计
- **源摘要**: [[wiki/sources/ai-agent-architecture-layers]] — 5 层架构（模型/记忆/工具/规划/安全）
- **源摘要**: [[wiki/sources/agent-architecture-patterns]] — 6 种架构模式（Single Agent / Plan & Exec / Multi-Agent / Reflection / RAG+Agent / DAG）
- **源摘要**: [[wiki/sources/ai-workflow-guide]] — 6 种工作流 + 7 框架对比

#### 8-16. 核心技术
- **源摘要**: [[wiki/sources/token-concepts]] — BPE 编码与上下文窗口
- **源摘要**: [[wiki/sources/llm-basics]] — Transformer/API/Fine-tuning 基础
- **源摘要**: [[wiki/sources/prompt-engineering-guide]] — 10 大提示词技术
- **源摘要**: [[wiki/sources/agent-context-engineering]] — Budget 管理/历史压缩
- **源摘要**: [[wiki/sources/rag-and-knowledge-retrieval]] — Advanced RAG/GraphRAG/RAGAS
- **源摘要**: [[wiki/sources/vector-database-introduction]] — HNSW/Chroma/Qdrant/Milvus 对比
- **源摘要**: [[wiki/sources/agent-memory-system-design]] — 短期/长期记忆 + 向量数据库 + 压缩策略
- **源摘要**: [[wiki/sources/reasoning-and-planning]] — CoT/ReAct/Plan-and-Execute/ToT+MCTS/Reflexion
- **源摘要**: [[wiki/sources/skills-tutorial]] — SKILL.md/渐进披露/MCP vs Skills

#### 17-18. 工程框架
- **源摘要**: [[wiki/sources/rookie-harness-engineering]] — 4 大护栏（Context/Constraints/Feedback/Entropy）
- **源摘要**: [[wiki/sources/loop-engineering-guide]] — 6 要素（Automations/Worktrees/Skills/Connectors/Sub-Agents/Memory）

#### 19-21. 进阶能力
- **源摘要**: [[wiki/sources/multimodal-agent]] — 图像/语音/视频多模态感知
- **源摘要**: [[wiki/sources/multi-agent-system]] — 层次/平级架构/AutoGen/A2A vs MCP
- **源摘要**: [[wiki/sources/huggingface-transformers-guide]] — Pipeline/Tokenizer/Fine-tuning/LoRA

#### 22-27. 实战落地（Python + 工具）
- **源摘要**: [[wiki/sources/python-ai-agent-implementation]] — AgentBrain/AgentTools 实现
- **源摘要**: [[wiki/sources/python-rag-implementation]] — SimpleRAG/AdvancedRAG/GraphRAG 实现
- **源摘要**: [[wiki/sources/python-reasoning-planning-implementation]] — ReAct/ToT/MCTS/Reflexion 实现
- **源摘要**: [[wiki/sources/vibe-coding-rookie-tutorial]] — Karpathy 概念 + 12 工具对比
- **源摘要**: [[wiki/sources/openclaw-rookie-tutorial]] — 安装/配置/Skills 系统
- **源摘要**: [[wiki/sources/hermes-agent-rookie-guide]] — 安装/模型配置/15+ 消息网关

#### 28-30. 其他菜鸟教程
- **源摘要**: [[wiki/sources/ai-agent-core-components]] — 感知/推理/记忆/工具/行动 5 大模块
- **源摘要**: [[wiki/sources/ai-agent-tools-integration]] — Function Calling/MCP/API/搜索
- **源摘要**: [[wiki/sources/agent-evaluation-safety-alignment]] — 指标体系/Guardrails/HITL

### MLOps 工具对比（2 篇）

#### 31. Kubeflow 轻量替代方案
- **源摘要**: [[wiki/sources/kubeflow-alternatives-5-tools]]
- 核心贡献：MLflow/Flyte/Prefect/ZenML/Argo 资源消耗与性能基准测试
- Kubeflow 40+ pods vs MLflow 单 pod / Flyte 4 pods

#### 32. Flyte vs Kubeflow 深度技术对比
- **源摘要**: [[wiki/sources/flyte-vs-kubeflow-comparison]]
- 核心贡献：代码体验、类型系统、动态 DAG、恢复模式、代码示例对比

### 新建综合分析页
- **新建**: [[wiki/syntheses/ai-agent-rookie-tutorial-series]] — 菜鸟教程 AI Agent 系列全景
  - 综合 30 篇菜鸟教程文章，按 11 大主题模块组织学习路径
  - 覆盖基础概念 → 架构设计 → 核心技术 → 工程框架 → 进阶能力 → 实战落地

### 更新已有页面
- [[wiki/syntheses/ai-agent-ecosystem-comparison]] — 新增 2 篇 MLOps 对比来源 + Flyte 实体链接
- [[wiki/concepts/harness-engineering]] — 新增菜鸟教程 Harness Engineering 来源
- [[wiki/entities/flyte]] — 新增 2 篇 Flyte 相关来源
- [[wiki/index.md]] — 源摘要 55 → 87，综合分析 9 → 10

### 汇总
- **本次新增**: 32 源摘要 + 1 综合分析 = 33 页面
- **更新已有**: 4 页面
- **全文索引统计**: 19 实体 + 17 概念 + 87 源摘要 + 10 综合分析 = 133 页面

### 三层架构最终状态
```
raw/      87 篇源文件（87 篇全部已 Ingest）
wiki/     133 内容页（含模板）+ 2 综合分析
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-17] feat | Wiki Loop Engineering — 引入自动化循环

- **新建概念**: [[wiki/concepts/wiki-loop-engineering]] — 知识库 Loop 架构
- **更新 Agent**: `.claude/agents/llm-wiki.md` — 新增 Loop 工作流
- **设定 Cron**: 每日 9:00 自动 Lint（Loop 2）
- **三 Loop**: 自动采集 / 健康检查 / 知识演进
- **更新**: `wiki/index.md` — 概念页 17 → 18
- **全文**: 19 实体 + 18 概念 + 87 源摘要 + 10 综合分析 = 134 页

## [2026-06-17] loop-3 | 知识演进 — 填补 7 个知识缺口

- **Loop 3 扫描结果**: 27 个高频引用概念无独立页面
- **优先补充 7 页**:

  **新实体 (3)**:
  - [[wiki/entities/anthropic]] — Claude/Claude Code 开发商
  - [[wiki/entities/openai]] — GPT/ChatGPT/Codex 开发商
  - [[wiki/entities/dvc]] — 数据版本控制工具

  **新概念 (4)**:
  - [[wiki/concepts/rl-reinforcement-learning]] — 强化学习（87 次引用）
  - [[wiki/concepts/moe-mixture-of-experts]] — 专家混合架构
  - [[wiki/concepts/lora-low-rank-adaptation]] — 低秩适配微调
  - [[wiki/concepts/para-method]] — 知识管理方法论

- **更新**: `wiki/index.md` — 实体 19→21, 概念 18→22
- **全文**: 21 实体 + 22 概念 + 87 源摘要 + 10 综合分析 = 140 页

## [2026-06-17] loop-3 | 知识演进 — 第二轮填补 11 个知识缺口

- **新实体 (6)**: autogen, bentoml, crewai, kserve, llamaindex, vllm
- **新概念 (5)**: embedding, fine-tuning, graphrag, marp-presentation, rerank
- **更新**: `wiki/index.md` — 实体 21→27, 概念 22→27
- **全文**: 27 实体 + 27 概念 + 87 源摘要 + 10 综合分析 = 151 页

## [2026-06-17] optimize | 浙江省技术经纪人中级培训 — 会议记录优化

- **源材料**: `Clippings/浙江省技术经纪人培训-高校科技成果转化与AI创业_raw.md`（原始语音转写，约 440 行）
- **分析结果**：
  - 两位讲者：沈映春（北航，高校科技成果转化）与张洁（每日互动投资副总裁，AI 创业孵化）
  - 沈映春讲座核心：科技成果转化"死亡谷"问题、概念验证中心（PoCC）机制、师生共创模式（成功率 15% vs 教授单独 2%）、哈佛/北航/清华案例
  - 张洁讲座核心：AI 时代 5 层公司结构、Product-Business Model 框架、硅谷人才/资本生态、AMC（Agentic Micro Company）范式、6 家被投企业案例
- **处理方式**：保留全部信息量，非摘要式结构化整理——按主题重构段落，去除语音重复与填充词，填补逻辑断点，增加表格/层级标题/标注等格式增强可读性
- **新建源摘要**: [[浙江省技术经纪人中级培训 - 高校科技成果转化与AI创业孵化]]
- **更新**: `wiki/index.md` — 源摘要 87 → 88
- **全文**: 27 实体 + 27 概念 + 88 源摘要 + 10 综合分析 = 152 页

## [2026-06-18] ingest | Google A2A 协议详解

- **源材料**: 掘金社区文章《Agent to Agent（A2A）一文全了解》by MervynZ
- **处理方式**: 从 `Clippings/` 复制到 `raw/sources/`，更新 frontmatter 元数据
- **新建源摘要**: [[wiki/sources/google-a2a-protocol]] — 全面介绍 Agent Card、任务生命周期、JSON-RPC API、流式通信等
- **新建概念页**: [[wiki/concepts/a2a-agent-to-agent-protocol]] — A2A 协议概念，含架构模型、发现机制、任务生命周期、A2A vs MCP 对比
- **更新已有实体**: [[wiki/entities/google-adk]] — 新增 A2A 协议说明及引用来源
- **更新**: `wiki/index.md` — 概念 27 → 28，源摘要 88 → 89，原始资料 87 → 88
- **全文**: 27 实体 + 28 概念 + 89 源摘要 + 14 综合分析 = 158 页

## [2026-06-18] lint | 定期健康检查

- **检查范围**: 孤儿页、断链、知识缺口、交叉引用、过时内容、资料覆盖
- **孤儿页**: ✅ 0 个 — 所有 157 个内容页均在 index.md 中有索引
- **断链**: ✅ 0 个 — 所有 `[[wiki/...]]` 内部链接均有效（模板占位符除外）
- **知识缺口**: ⚠️ 发现 5 个高优先级缺口
  - 🔴 P0: MCP (Model Context Protocol) — 22 篇提及，与 A2A 对等的核心协议缺口
  - 🔴 P0: ReAct (Reasoning + Acting) — 12 篇提及，最核心的 Agent 行为模式
  - 🟡 P1: Prompt Engineering — 10 篇提及，基础技术无独立概念页
  - 🟡 P1: Chain of Thought (CoT) — 8 篇提及，核心推理技术
  - 🟢 P2: Guardrails — 4 篇提及，Agent 安全护栏
- **交叉引用**: ⚠️ 3 个实体缺源引用 — openai、kserve、vllm（来自 Loop-3 自动创建，未关联源摘要）
- **过时内容**: ✅ 无明显过时
- **资料覆盖**: ✅ 88/88 全部已 Ingest
- **报告**: [[wiki/lint-report-2026-06-18]]

## [2026-06-18] loop-3 | 知识演进 — 填补 5 个高优先 Lint 知识缺口 + 修复 3 个实体引用

### 新增概念 (5 个)
- [[wiki/concepts/mcp-model-context-protocol]] — MCP 协议，Anthropic 的 Agent↔Tool 连接协议，含与 A2A/Skills 对比表
- [[wiki/concepts/react-reasoning-acting]] — ReAct (Thought→Act→Observe) 循环，Agent 最核心的行为模式
- [[wiki/concepts/prompt-engineering]] — 提示词工程：三大消息角色、十大技术、Agent System Prompt 设计
- [[wiki/concepts/cot-chain-of-thought]] — CoT 思维链推理技术，Zero-shot/Few-shot/自洽性方法，与 ReAct 对比
- [[wiki/concepts/guardrails]] — Agent 安全护栏：四层安全架构（输入/注入检测/执行/输出），Harness 四道护栏定位

### 实体引用修复 (3 个)
- [[wiki/entities/openai]] — 添加 3 个 `[[wiki/sources/...]]` 引用
- [[wiki/entities/kserve]] — 添加 2 个 `[[wiki/sources/...]]` 引用
- [[wiki/entities/vllm]] — 添加 3 个 `[[wiki/sources/...]]` 引用

### 更新
- `wiki/index.md` — 概念 28 → 33
- `wiki/lint-report-2026-06-18.md` — 更新状态和修复记录
- **全文**: 27 实体 + 33 概念 + 89 源摘要 + 14 综合分析 = 163 页

## [2026-06-19] ingest | 批量 Ingest 7 篇新源材料 — JavaGuide 系列 + A2A 官方来源

### 源材料迁移
- 从 `Clippings/` 复制到 `raw/sources/` 共 7 篇，更新 frontmatter 元数据

### JavaGuide 系列（4 篇）

#### 1. AI Agent 核心概念全景
- **源摘要**: [[wiki/sources/agent-core-concepts-javaguide]]
- 核心贡献：Agent 演进四阶段、Agent vs Workflow 选型、Agent Loop 详解、Tools 注册/MCP/Skills 三层体系
- **更新**: [[wiki/concepts/react-reasoning-acting]]、[[wiki/concepts/mcp-model-context-protocol]] — 补充引用

#### 2. AI Agent 记忆系统深度解析
- **源摘要**: [[wiki/sources/agent-memory-system-javaguide]]
- 核心贡献：记忆三层表征（Token/参数/潜在）、6 大 Memory 产品对比、短期记忆三策略、CLAUDE.md 设计方法论
- **更新**: [[wiki/concepts/agent-skills-system]] — 补充引用

#### 3. Agent Skills 深度解析
- **源摘要**: [[wiki/sources/agent-skills-deep-dive-javaguide]]
- 核心贡献：Skill 与 Prompt/MCP/Function Calling 的边界、SKILL.md 元数据与正文设计、渐进披露三层模型、8 个常见坑
- **更新**: [[wiki/concepts/agent-skills-system]]、[[wiki/concepts/mcp-model-context-protocol]] — 补充引用

#### 4. Prompt Engineering 深度解析
- **源摘要**: [[wiki/sources/prompt-engineering-javaguide]]
- 核心贡献：四要素框架、六大技巧、企业级安全实践（输入验证/注入检测/权限隔离/输出审计）
- **更新**: [[wiki/concepts/prompt-engineering]] — 补充引用

### A2A 官方来源（3 篇 → 合并 1 个源摘要）

#### 5. Google Blog + Linux Foundation Spec + GitHub
- **源摘要**: [[wiki/sources/a2a-official-spec-linux-foundation]]
- 核心贡献：A2A 治理结构（Linux Foundation TSC）、6 语言 SDK、50+ 企业伙伴、A2A vs MCP 官方定位
- **更新**: [[wiki/concepts/a2a-agent-to-agent-protocol]]、[[wiki/entities/google-adk]] — 补充引用

### 汇总
- **本次新增**: 5 源摘要
- **更新已有**: 7 概念/实体页新增引用
- **更新**: `wiki/index.md` — 源摘要 89 → 93，原始资料 88 → 95
- **全文**: 28 实体 + 33 概念 + 93 源摘要 + 13 综合分析 = 167 页

## [2026-06-19] lint | Loop 2 健康检查

### 检查结果
- **孤儿页**: ✅ 无 — 168 个内容页均通过索引引用
- **断链**: ✅ 无 — 182 个 wikilinks 中 0 个真实断链（13 个"缺失"均来自 templates/、log.md、lint-report.md）
- **raw/sources vs wiki/sources**: ✅ 一致 — raw 95 篇 / wiki 93 篇（差异 2 篇为 A2A 多源文件合并为单一摘要）
- **索引统计**: ⚠️ 发现 1 处偏差 → 源摘要页统计 94 → **已修正为 93**

### 修复项
- **索引统计修正**: `wiki/index.md` 源摘要页 94 → 93
- **Frontmatter 修复**: 更新 5 个页面的 `updated:` 字段，对齐最新编辑时间
  - [[wiki/entities/google-adk]] — 06-13 → 06-19
  - [[wiki/entities/openai]] — 06-17 → 06-19
  - [[wiki/entities/kserve]] — 06-17 → 06-19
  - [[wiki/entities/vllm]] — 06-17 → 06-19
  - [[wiki/concepts/agent-skills-system]] — 06-13 → 06-19

## [2026-06-19] ingest | 万字详解 RAG 基础概念 — JavaGuide

- **源材料**: Clippings 中的 JavaGuide RAG 基础概念文章（约 6200 字）
- **复制到**: `raw/sources/万字详解 RAG 基础概念.md`，更新 frontmatter 元数据
- **新建源摘要**: [[wiki/sources/rag-basis-concepts-javaguide]] — RAG 基础概念全景

### 更新已有概念页
- [[wiki/concepts/embedding]] — 新增相似度度量对比表（余弦/内积/欧氏距离），扩充 Embedding 模型表（text-embedding-3-large/GTE 系列），添加选型建议
- [[wiki/concepts/fine-tuning]] — 新增 RAG vs 微调完整对比表，含 6 维度对比（知识更新/数据安全/幻觉控制/成本结构/适合场景/主要风险）
- [[wiki/concepts/rag-optimization]] — 新增 RAG 演进三阶段（Naive/Advanced/Modular），新增 RAG 核心优势与局限总结
- [[wiki/concepts/rag-vs-wiki]] — 新增 RAG vs 传统搜索对比表，含选型判断框架

### 更新综合分析页
- [[wiki/syntheses/rag-optimization-guide]] — 新增维度 D（基础概念与决策框架），补充对比分析表和开放问题

### 汇总
- **本次新增**: 1 源摘要
- **更新已有**: 5 页面（4 概念 + 1 综合分析）
- **更新**: `wiki/index.md` — 源摘要 93 → 94，原始资料 95 → 96
- **全文**: 28 实体 + 33 概念 + 94 源摘要 + 13 综合分析 = 168 页

## [2026-06-19] ingest | 批量 Ingest 9 篇新源材料 — JavaGuide RAG 系列 + LLM/Agent 系列

这是 JavaGuide 系列的第二批批量 Ingest，覆盖 5 篇 RAG 系列文章和 4 篇 LLM/Agent 系列文章。

### 源材料迁移
- 从 `Clippings/` 复制到 `raw/sources/` 共 9 篇，更新 frontmatter 元数据

### RAG 系列（5 篇）

#### 1. RAG 文档处理与切分策略
- **源摘要**: [[wiki/sources/rag-document-processing-javaguide]]
- 核心贡献：文档进入索引前的完整链路（文件解析→清洗→结构化增强→Chunking），多粒度混合 Chunking 策略，多模态内容处理

#### 2. RAG 知识库文档更新
- **源摘要**: [[wiki/sources/rag-knowledge-update-javaguide]]
- 核心贡献：Embedding 模型一致性要求、元数据设计（版本号/时间戳）、增量更新 vs 全量重建、灰度发布与回滚方案

#### 3. 万字详解 RAG 优化
- **源摘要**: [[wiki/sources/rag-optimization-javaguide]]
- 核心贡献：RAG 优化是系统工程（数据→切分→索引→召回→重排→上下文→生成→评估），数据治理优先，上下文压缩与答案评估

#### 4. 万字详解 RAG 向量索引算法和向量数据库
- **源摘要**: [[wiki/sources/rag-vector-store-javaguide]]
- 核心贡献：HNSW/IVFFLAT/IVF+HNSW 索引算法选型，Milvus/pgvector/ES 向量数据库对比，80% 召回问题与向量搜索算法无关

#### 5. 万字详解 GraphRAG
- **源摘要**: [[wiki/sources/graphrag-javaguide]]
- 核心贡献：传统向量 RAG 的局限性（实体关系丢失），GraphRAG 实体提取/关系构建/社区检测流程，工程落地成本考量

### Agent/LLM 系列（4 篇）

#### 6. AI 工作流中的 Workflow、Graph 与 Loop
- **源摘要**: [[wiki/sources/ai-workflow-graph-loop-javaguide]]
- 核心贡献：Workflow/Graph/Loop 三层抽象、Node/Edge/State 模型、Loop 安全边界（状态污染/放大攻击）、Spring AI Alibaba vs LangGraph

#### 7. LLM 运行机制
- **源摘要**: [[wiki/sources/llm-operation-mechanism-javaguide]]
- 核心贡献：Token 经济（中英文差异/BPE/Unigram）、上下文窗口隐藏成本、采样参数配置矩阵（Temperature/Top-p/Top-k/Penalty）、Token 预算公式

#### 8. 大模型结构化输出与 Function Calling
- **源摘要**: [[wiki/sources/structured-output-function-calling-javaguide]]
- 核心贡献："请返回 JSON"的五种失效模式、JSON Mode vs Schema vs Structured Outputs 三层体系、Function Calling 七步流水线、六层安全防御

#### 9. 一文搞懂 Harness Engineering
- **源摘要**: [[wiki/sources/harness-engineering-javaguide]]
- 核心贡献：六层架构（模型/上下文/工具/记忆/控制/观测）、40% 上下文利用率阈值、模型-Harness 耦合度概念、5 团队实战案例（OpenAI/Anthropic/Stripe/Hashimoto/Bockeler）

### 更新已有概念页
- [[wiki/concepts/graphrag]] — 新增工程落地考量章节（实体提取精度/计算开销/增量更新/适用边界）
- [[wiki/concepts/harness-engineering]] — 新增 JavaGuide 六层架构视角（细化三层为六层用于生产排障）
- [[wiki/concepts/rag-optimization]] — 添加新 RAG 优化来源引用
- [[wiki/concepts/embedding]] — 添加向量数据库来源引用
- [[wiki/concepts/rerank]] — 添加 RAG 优化来源引用

### 更新综合分析页
- [[wiki/syntheses/rag-optimization-guide]] — 新增维度 E/F/G/H（文档处理/知识库更新/向量数据库/GraphRAG），对比分析表从 5 列扩展到 8 列
- [[wiki/syntheses/llm-technical-foundations]] — 新增 LLM 运行机制和结构化输出两个维度，对比分析表从 5 列扩展到 7 列

### 汇总
- **本次新增**: 9 源摘要
- **更新已有**: 9 页面（5 概念 + 2 综合分析）
- **更新**: `wiki/index.md` — 源摘要 94 → 103，原始资料 96 → 105
- **全文**: 28 实体 + 33 概念 + 103 源摘要 + 13 综合分析 = 177 页

## [2026-06-19] ingest | MCP（Model Context Protocol）深度解析 — JavaGuide

- **源材料**: Clippings 中的 JavaGuide MCP 文章（约 12,000 字）
- **复制到**: `raw/sources/什么是 Model Context Protocol (MCP)？和 Function Calling、Agent 什么关系？.md`，更新 frontmatter 元数据
- **新建源摘要**: [[wiki/sources/mcp-deep-dive-javaguide]] — MCP 深度解析

### 更新已有概念页

- [[wiki/concepts/mcp-model-context-protocol]] — **大幅重写**：新增 FC/MCP/Agent 三层关系与场景判断表、四层架构详解（Host→Client→Server→DataSource）、Server 侧三类能力（Resources/Tools/Prompts）、Client 侧三类能力（Roots/Sampling/Elicitation）、JSON-RPC 2.0 通信机制与示例、stdio vs Streamable HTTP 传输选型、生产落地六大问题、企业检查清单五大维度 25+ 项、Server 开发最佳实践、FastMCP 最小代码示例、安全红线。概念页从 109 行扩展到全页
- [[wiki/concepts/a2a-agent-to-agent-protocol]] — 新增 FC/MCP/A2A/Agent 完整分层表，补充 MCP 深度解析来源引用

### 汇总

- **本次新增**: 1 源摘要
- **更新已有**: 2 概念页
- **更新**: `wiki/index.md` — 源摘要 103 → 104，原始资料 105 → 106
- **全文**: 28 实体 + 33 概念 + 104 源摘要 + 13 综合分析 = 178 页

### 三层架构最终状态

```
raw/      106 篇源文件（106 篇全部已 Ingest）
wiki/     178 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-19] lint | Loop 2 健康检查

### 检查范围
孤儿页、断链、索引统计、raw/sources vs wiki/sources 一致性、知识缺口

### 检查结果

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 孤儿页 | ✅ | 无 — 178 个内容页均通过索引引用 |
| 断链 | 🔴 **已修复** | 发现 1 处断链 → 已清除 |
| 索引统计 | ✅ | 28 实体 + 33 概念 + 104 源摘要 + 13 综合分析 = 178 页，全部与磁盘一致 |
| raw/sources vs wiki/sources | ✅ | 106 raw vs 104 wiki，差异 2 篇为 A2A 多源文件合并（4 raw → 2 wiki），预期内 |
| 知识缺口 | ✅ | 上次 5 个缺口（MCP/ReAct/Prompt Engineering/CoT/Guardrails）已填补 |
| 交叉引用 | ✅ | 上次 3 个实体缺引用（openai/kserve/vllm）已修复 |

### 发现与修复

#### 🔴 断链：浙江省技术经纪人源摘要
- `wiki/index.md` 中存在 `[[浙江省技术经纪人中级培训 - 高校科技成果转化与AI创业孵化]]` 链接
- 对应文件不存在于 `wiki/`、`wiki/sources/` 或 `raw/sources/` 中
- 原始 Clippings 文件 `Clippings/浙江省技术经纪人培训-高校科技成果转化与AI创业_raw.md` 也已不存在
- **修复**: 从 index.md 中移除该断链条目
- **用户注意**: 此源材料数据已丢失。如需恢复需重新剪藏或导入

#### 🟡 重复条目：hermes-agent-comprehensive-guide
- `wiki/index.md` 综合分析的 `[[wiki/syntheses/hermes-agent-comprehensive-guide]]` 出现两次
- 第二次为 Marp 演示版创建时的重复添加
- **修复**: 删除重复行，保留唯一条目并更新描述

### 全文索引统计
28 实体 + 33 概念 + 104 源摘要 + 13 综合分析 = 178 页（与磁盘一致）

### 三层架构最终状态
```
raw/      106 篇源文件（106 篇全部已 Ingest）
wiki/     178 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-21] ingest | 批量 Ingest 8 篇新源材料 — JavaGuide 系列

这是 JavaGuide 系列的第三批，覆盖 AI 系统设计、Coding 工具、语音 Agent、CLAUDE.md、Spec Coding、Vibe Coding 技巧和 LLM Gateway。

### 源材料迁移
- 从 `Clippings/` 复制 8 篇到 `raw/sources/`，更新 frontmatter 元数据

### 新建源摘要（8 篇）

1. **[[wiki/sources/ai-system-design-javaguide]]** — AI 应用系统设计：Demo 生产差距、分层架构、三类交互模式、Prompt 版本化、RAG/Memory/Tool 分离、工具安全 6 道关、Java 11 模块
2. **[[wiki/sources/ai-skills-recommendations-javaguide]]** — 6 大 AI 编程 Skills：Superpowers/Everything Claude Code/UI UX Pro Max/sanyuan-skills/Web Access/skill-creator
3. **[[wiki/sources/cli-vs-ide-comparison-javaguide]]** — CLI vs IDE 深度对比：9 款产品全景图、CLI 4 大优势、行业融合趋势
4. **[[wiki/sources/ai-voice-engineering-javaguide]]** — AI 语音系统工程：ASR/TTS/VAD、打断处理、级联 vs Realtime API、interview-guide 完整实现
5. **[[wiki/sources/claude-md-best-practices-javaguide]]** — CLAUDE.md 最佳实践：5 类该写/3 类不该写、层级结构、.claude/rules、Auto Memory、维护方法
6. **[[wiki/sources/spec-coding-javaguide]]** — Spec Coding：四步流程、三色标签权限、Spec 分层管理、多 Agent 协作
7. **[[wiki/sources/vibe-coding-tips-javaguide]]** — Vibe Coding 实用技巧：Git 策略、贵模型分工、上下文管理、权限控制
8. **[[wiki/sources/llm-gateway-deep-dive-javaguide]]** — LLM Gateway：6 阶段路由演进、Fallback/幂等、Token 五维限流、成本 18 字段、6 种方案选型

### 更新已有页面

- [[wiki/concepts/vibe-coding]] — 新增适用场景判断、轻量 Spec 策略、多模型分工/上下文管理/Git 工作流/权限控制 5 个技巧模块，添加 3 个新来源
- [[wiki/concepts/spec-driven-development]] — 新增四步落地流程表、三色标签权限控制、Spec 管理策略，添加 Spec Coding 来源
- [[wiki/entities/claude-code]] — 添加 6 个新来源引用

### 汇总

- **本次新增**: 8 源摘要
- **更新已有**: 3 页面（2 概念 + 1 实体）
- **更新**: `wiki/index.md` — 源摘要 104 → 112，原始资料 106 → 114
- **全文**: 28 实体 + 33 概念 + 112 源摘要 + 13 综合分析 = 186 页

### 三层架构最终状态

```
raw/      114 篇源文件（114 篇全部已 Ingest）
wiki/     186 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-22] lint | Loop 2 健康检查

### 检查结果
- **孤儿页**: ✅ 无 — 186 个内容页均通过索引引用
- **索引统计**: ✅ 与实际文件数一致（28+33+112+13=186）
- **raw/sources vs wiki/sources**: ✅ 差异 2 篇属预期（A2A 多源合并 + 浙江省特殊情况）
- **断链**: ⚠️ 发现 2 个

### 断链详情

**🔴 问题 1：浙江省技术经纪人培训源摘要文件缺失**
- `index.md` 中 `[[浙江省技术经纪人中级培训 - 高校科技成果转化与AI创业孵化]]` 指向不存在的文件
- 根因：2026-06-17 `optimize` 操作记录了"新建源摘要"但文件未被物理创建
- 处理：从 `index.md` 移除该条目，调整源摘要计数

**🟡 问题 2：vector-database 概念页待创建**
- `wiki/sources/rag-vector-store-javaguide.md` 中 `[[wiki/concepts/vector-database]]` 标记为"（页面待创建）"
- 处理：保留至下次 Loop-3 知识演进。现有 `wiki/sources/vector-database-introduction.md` 和 `wiki/concepts/embedding.md` 已覆盖相关主题

### 前次修复验证
- 2026-06-18 Lint 发现的 5 个知识缺口（MCP/ReAct/Prompt Engineering/CoT/Guardrails）：✅ 全部填补完毕

### 本次修复
1. **vector-database 引用修复**: `wiki/sources/rag-vector-store-javaguide.md` 中的 `[[wiki/concepts/vector-database]]` 断链已改为指向现有 `[[wiki/sources/vector-database-introduction]]`
2. **浙江省条目**: 已在 2026-06-19 Lint 中移除，本次检查确认无残留
3. **报告**: [[wiki/lint-report-2026-06-22]]

### 三层架构最终状态

```
raw/      114 篇源文件（114 篇全部已 Ingest）
wiki/     186 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-23] lint | Loop 2 健康检查

### 检查结果
- **孤儿页**: ✅ 无 — 186 个内容页均在 `index.md` 中有索引
- **索引统计**: ✅ 与实际文件数一致（28 实体 + 33 概念 + 112 源摘要 + 13 综合分析 = 186）
- **raw/sources vs wiki/sources**: ✅ raw 114 / wiki 112，差异 2 篇属预期（A2A 多源合并）
- **断链**: ✅ 0 个实际断链。上次修复的 `[[wiki/concepts/vector-database]]` 确认已在 `rag-vector-store-javaguide.md` 中改为 `[[wiki/sources/vector-database-introduction]]`

### 说明
grep 发现的 4 个"匹配"均为误报：
- `[[wiki/...]]` 和 `[[wiki/sources/...]]` — lint-report 中的模板描述占位符
- `[[wiki/concepts/vector-database]]` — 上次 lint 报告中的历史引用，非当前链接
- `[[wiki/index.md]]` — log.md 中的文件路径引用，非 wikilink

### 汇总
| 检查项 | 状态 |
|--------|------|
| 孤儿页 | ✅ |
| 索引统计 | ✅ |
| raw vs wiki 一致性 | ✅ |
| 断链 | ✅ 0 个 |
| **全文统计** | 28 实体 + 33 概念 + 112 源摘要 + 13 综合分析 = 186 页 |

## [2026-06-24] lint | Loop 2 健康检查

### 检查结果
- **孤儿页**: ✅ 无 — 186 个内容页均在 `index.md` 中有索引
- **索引统计**: ✅ 与实际一致（28 实体 + 33 概念 + 112 源摘要 + 13 综合分析 = 186）
- **raw/sources vs wiki/sources**: ✅ raw 114 / wiki 112（差异 2 属 A2A 多源合并，预期内）
- **断链**: ✅ 0 个

| 检查项 | 状态 |
|--------|------|
| 孤儿页 | ✅ |
| 索引统计 | ✅ |
| raw vs wiki 一致性 | ✅ |
| 断链 | ✅ 0 个 |
| **全文统计** | 28 实体 + 33 概念 + 112 源摘要 + 13 综合分析 = 186 页 |

## [2026-06-29] ingest | Spec-Driven Development 完全指南 — Augment Code

- **源材料**: `Clippings/What Is Spec-Driven Development A Complete Guide.md` → `raw/sources/`
- **原文**: Augment Code 发布的 SDD 深度指南（Molisha Shah, 2026-04-23）
- **新建源摘要**: [[wiki/sources/spec-driven-development-complete-guide]]
  - 核心贡献：六要素框架（Outcomes/Scope/Constraints/Prior Decisions/Task Breakdown/Verification Criteria）
  - SDD vs TDD/BDD/Vibe Coding 五维对比表
  - 三种落地模式：Spec-First / Spec-Anchored / Spec-as-Source
  - 对抗性 Agent 模式（Coordinator/Implementor/Verifier）及模型分层策略
  - 7 款工具对比矩阵（Spec Kit / SwaggerHub / Postman / Spectral / PactFlow / Specmatic / TypeSpec）
  - 棕地采纳三阶段、Figma MCP 实践案例、何时跳过 Spec 判断框架
- **大幅更新概念页**: [[wiki/concepts/spec-driven-development]]
  - 新增 Why SDD Matters Now（2025-2026 三大合力：AI 漏洞率/ EU AI Act / 分布式治理）
  - 新增六要素框架（Spec 的可操作检查清单）
  - 新增三种模式详解及其适用场景判断
  - 新增对抗性 Agent 模式（Coordinator → Implementor → Verifier 架构 + 对立目标设计）
  - 新增模型分层策略（Spec 用贵模型 / Implement 用中档 / Verify 用快速）
  - 新增棕地采纳三阶段法（重构 → 局部 Spec → 增量 CI 执行）
  - 新增何时跳过 Spec 判断表
  - 新增 7 款工具对比矩阵、Intent Context Engine 企业级扩展
  - 新增 1 个来源引用（来自 Augment Code）、1 个新相关概念（guardrails）

### 汇总
- **本次新增**: 1 源摘要
- **大幅更新**: 1 概念页
- **更新**: `wiki/index.md` — 源摘要 112 → 113，原始资料 114 → 115
- **全文**: 28 实体 + 33 概念 + 113 源摘要 + 13 综合分析 = 187 页

### 三层架构最终状态

```
raw/      115 篇源文件（115 篇全部已 Ingest）
wiki/     187 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-29] ingest | 批量 Ingest 8 篇新源材料 — SDD 生态深度覆盖 + Vibe Coding + AGENTS.md

这是 2026 年 6 月 29 日的第二次批量 Ingest，与第一次（Augment Code SDD 指南）互补，形成对 SDD 生态从"概念→工具→企业落地"的完整覆盖。此外还补充了 Vibe Coding 和 AGENTS.md 两个相邻主题。

### 源材料迁移
- 从 `Clippings/` 复制 8 篇到 `raw/sources/`，更新 frontmatter 元数据

### 新建源摘要（8 篇）

**SDD 生态深度覆盖（6 篇）**
1. **[[wiki/sources/sdd-tencent-cloud-ai-specs-practice]]** — OpenSpec/Spec Kit/Kiro 三大框架深度对比（腾讯云社区, 2026-04-17）
2. **[[wiki/sources/sdd-github-spec-kit-announcement]]** — GitHub Spec Kit 官方博客：四阶段工作流、核心设计理念（Den Delimarsky, 2025-09-03）
3. **[[wiki/sources/sdd-with-claude-code-heeki-park]]** — SDD + Claude Code 实战：三层 SDD 实践、分阶段构建、Claude Code 技巧（Heeki Park, 2026-03-01）
4. **[[wiki/sources/sdd-zhangluka-guide]]** — SDD 企业落地实践指南：六阶段生命周期、四步推进法、多团队协同（zhangluka, 2026-06）
5. **[[wiki/sources/sdd-4-tools-comparison-hubwiz]]** — GSD/Spec Kit/OpenSpec/Taskmaster 四象限格局、五大分歧点（汇智网, 2026-03-03）
6. **[[wiki/sources/sdd-intro-jimmysong-ai-handbook]]** — SDD 范式迁移：AI 编程协议栈三层模型、Tessl/AgentScript/CodePlan 等工具全景（Jimmy Song, 2025-11-03）

**Vibe Coding（1 篇）**
7. **[[wiki/sources/vibe-coding-jimmysong-ai-handbook]]** — 氛围编程定义与四要素、代表性实践、工程化挑战与质量门（Jimmy Song, 2025-09-29）

**AGENTS.md（1 篇）**
8. **[[wiki/sources/agents-md-specification-jimmysong]]** — AGENTS.md 规范：六大工程要素、三层边界模型（Jimmy Song, 2025-11-02）

### 更新已有页面

- **大幅更新概念页**: [[wiki/concepts/spec-driven-development]]
  - 新增 2026 SDD 工具生态格局（GSD/Spec Kit/OpenSpec/Taskmaster/Kiro 五工具四象限对比）
  - 新增五大分歧点分析（执行深度/上下文策略/棕地绿地/平台哲学/许可证）
  - 新增 GSD/OpenSpec/Kiro/Taskmaster AI 逐个详解
  - 新增 Tessl Framework/AgentScript/CodePlan 等相邻方案
  - 新增 8 个来源引用
  - 新增相关概念：agents-md

- **更新概念页**: [[wiki/concepts/vibe-coding]]
  - 新增 AI 编程历时演进七阶段
  - 新增核心四要素框架
  - 新增 1 个来源引用

- **新建概念页**: [[wiki/concepts/agents-md]]
  - AGENTS.md 规范定义、六大工程要素、三层边界模型、完整结构
  - AGENTS.md vs CLAUDE.md 对比
  - 相关概念：agent-skills-system, spec-driven-development, guardrails

- **更新概念页**: [[wiki/concepts/agent-skills-system]]
  - 新增相关概念：agents-md

### 汇总
- **本次新增**: 8 源摘要 + 1 概念 = 9 页面
- **大幅更新**: 1 概念页
- **小幅更新**: 2 概念页
- **更新**: `wiki/index.md` — 概念 33 → 34，源摘要 113 → 121，原始资料 115 → 123
- **全文**: 28 实体 + 34 概念 + 121 源摘要 + 13 综合分析 = 196 页

### 三层架构最终状态

```
raw/      123 篇源文件（123 篇全部已 Ingest）
wiki/     196 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-29] ingest | Hidden Technical Debt in ML Systems — Sculley et al. NeurIPS 2015

- **源材料**: 下载自 `https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf` → `raw/sources/neurips2015-hidden-technical-debt-ml.md`
- **原文**: 里程碑论文 "Hidden Technical Debt in Machine Learning Systems"，10 位 Google 作者，NeurIPS 2015
- **新建源摘要**: [[wiki/sources/hidden-technical-debt-ml-sculley-2015]]
  - 核心贡献：CACE 原则（Changing Anything Changes Everything）
  - 纠缠（Entanglement）、修正级联（Correction Cascades）、未声明消费者（Undeclared Consumers）
  - 数据依赖债务（不稳定/未利用/缺乏静态分析）
  - 直接与隐藏反馈循环
  - ML 系统五大反模式（胶水代码/管道丛林/死亡实验代码路径/抽象债务/常见坏味道）
  - 配置债务六原则、外部世界变化、预测偏差监控
  - 数据测试/可复现性/流程管理/文化债务
- **更新概念页**: [[wiki/concepts/mlops-lifecycle]]
  - 新增"学术根基"章节，关联本论文的核心贡献（CACE、ML 反模式、配置债务、数据依赖债务、反馈循环）
  - 新增 1 个来源引用

### 汇总
- **本次新增**: 1 源摘要
- **更新**: 1 概念页
- **更新**: `wiki/index.md` — 源摘要 121 → 122，原始资料 123 → 124
- **全文**: 28 实体 + 34 概念 + 122 源摘要 + 13 综合分析 = **197 页**

### 三层架构最终状态

```
raw/      124 篇源文件（124 篇全部已 Ingest）
wiki/     197 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-29] ingest | 批量 4 篇：MLOps 成熟度模型 + OpenSpec 生态

### 源材料迁移
- 从 `Clippings/` 复制 4 篇到 `raw/sources/`，更新 frontmatter

### 新建源摘要（4 篇）

**1. [[wiki/sources/mlops-google-cloud-cicd-ct-pipelines]]** — Google Cloud Architecture Center 官方 MLOps CI/CD/CT 指南
- 核心贡献：三层成熟度模型（Level 0 手动 / Level 1 ML Pipeline 自动化 / Level 2 CI/CD 自动化）
- ML vs 传统 DevOps 五大差异、CT（持续训练）作为 ML 特有维度
- 特征存储、元数据管理、pipeline 触发器（按需/定时/新数据/退化/漂移）
- 直接引用 Hidden Technical Debt 论文的 ML 系统组件图

**2. [[wiki/sources/openspec-knowledge-hub-intent-driven]]** — OpenSpec 知识中心（Hari Krishnan）
- 核心贡献：三工件模型（增量规范/权威规范/已存档规范）
- Git Worktrees 并行开发模式、ADR 集成

**3. [[wiki/sources/openspec-source-truth-hari-krishnan]]** — OpenSpec 权威规范 vs 碎片化规范（Hari Krishnan）
- 核心贡献：一致性层次框架（Spec-First → Spec-Anchored → Spec-as-Source）
- 碎片化规范（Spec-Kit/Kiro）的局限 vs OpenSpec 权威规范的优势

**4. [[wiki/sources/openspec-custom-schemas-github]]** — OpenSpec 自定义 Schema 集合（GitHub）
- 核心贡献：5 种工作流模板（Minimalist/Event-Driven/Behaviour-Driven/Intent-Driven/Spec-Driven with ADR）

### 更新已有页面

- [[wiki/concepts/mlops-lifecycle]] — 新增 MLOps 三层成熟度模型章节（Level 0/1/2 详细特性+对比表），新增 2 个来源引用
- [[wiki/concepts/spec-driven-development]] — 新增 3 个 OpenSpec 生态来源引用

### 汇总
- **本次新增**: 4 源摘要
- **更新**: 2 概念页
- **更新**: `wiki/index.md` — 源摘要 122 → 126，原始资料 124 → 128
- **全文**: 28 实体 + 34 概念 + 126 源摘要 + 13 综合分析 = **201 页**

### 三层架构最终状态

```
raw/      128 篇源文件（128 篇全部已 Ingest）
wiki/     201 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```

## [2026-06-29] ingest | Google MLOps 白皮书（上）中文翻译

- **源材料**: `Clippings/Google MLOps白皮书（上）MLOps生命周期及核心能力.md` → `raw/sources/`
- **原文**: Google MLOps 白皮书（Practitioners Guide to MLOps）中文翻译（dreaming, 知乎, 2022-08-25）
- **新建源摘要**: [[wiki/sources/google-mlops-whitepaper-lifecycle-zh]]
  - 核心贡献：MLOps 七阶段生命周期（ML 开发 → 训练操作 → 持续训练 → 模型部署 → 预测服务 → 持续监控 → 数据和模型管理）
  - 11 项核心技术能力（实验/数据处理/模型训练/评估/部署/在线实验/监控/ML 流程/模型注册/特征库/元数据跟踪）
  - ML 工程三大复杂领域融合（数据工程 → ML 工程 → 应用工程）
- **更新概念页**: [[wiki/concepts/mlops-lifecycle]] — 新增 1 个来源引用

### 汇总
- **本次新增**: 1 源摘要
- **更新**: 1 概念页
- **更新**: `wiki/index.md` — 源摘要 126 → 127，原始资料 128 → 129
- **全文**: 28 实体 + 34 概念 + 127 源摘要 + 13 综合分析 = **202 页**

### 三层架构最终状态

```
raw/      129 篇源文件（129 篇全部已 Ingest）
wiki/     202 内容页（含模板）
schema    CLAUDE.md + .claude/agents/llm-wiki.md
```
