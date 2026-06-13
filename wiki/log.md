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
