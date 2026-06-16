---
title: "菜鸟教程 AI Agent 系列 — 从入门到实战的全景教程体系"
tags:
  - synthesis
  - rookie-tutorial
  - agent
  - tutorial-series
  - runoob
created: 2026-06-17
updated: 2026-06-17
---

# 菜鸟教程 AI Agent 系列

> 综合 30 篇菜鸟教程（Runoob）AI Agent 系列文章，构建从基础概念到高阶实战的完整学习路径。涵盖 Agent 基础、核心组件、架构模式、工具集成、记忆系统、推理规划、多模态、多智能体、RAG、Prompt Engineering、Harness/Loop Engineering、以及 Python 实现等 11 大主题模块。

---

## 一、系列概况

菜鸟教程（runoob.com）于 2026 年 6 月推出的 AI Agent 系列教程，是目前中文互联网上**覆盖最全面的 AI Agent 入门教程体系**。系列共 30 篇文章，从零基础概念讲到生产级工程实践，配有完整的 Python 代码示例。

```
学习路径概览：

第一层：基础认知
  Agent 概述 → 工作原理 → 核心组件 → 术语表

第二层：架构与设计
  底层架构 → 架构模式(6种) → Agent Workflow(6种)

第三层：核心技术
  Token → LLM 基础 → Prompt Engineering → Context Engineering
  RAG → 向量数据库 → 记忆系统 → 推理与规划(CoT/ReAct/ToT/MCTS/Reflexion)

第四层：工程框架
  Harness Engineering → Loop Engineering → Skills 系统

第五层：进阶能力
  多模态 Agent(视觉/语音/视频) → 多智能体系统(AutoGen/A2A/MCP)

第六层：实战落地
  Python 实现 Agent → Python 实现 RAG → Python 实现推理规划
  Hugging Face Transformers → Vibe Coding → OpenClaw → Hermes Agent
```

---

## 二、各模块详解

### 模块 1：Agent 基础概念（4 篇）

| 文章 | 核心定位 | 关键内容 |
|------|----------|----------|
| AI Agent 教程概述 | 系列总纲 | 学习路径、前置知识、目标读者 |
| AI Agent 简介 | Agent 是什么 | 定义、自主性特征、与 LLM 的区别、应用场景 |
| AI Agent 工作原理 | 感知-思考-行动循环 | 感知层/推理层/执行层三层架构、ReAct 循环 |
| AI Agent 术语 | 术语词典 | 30+ 核心术语定义（Agent/工具/记忆/规划/RAG/MCP 等） |

### 模块 2：架构与设计（3 篇）

| 文章 | 核心定位 | 关键内容 |
|------|----------|----------|
| AI Agent 底层架构 | 分层架构全景 | 模型层/记忆层/工具层/规划层/安全层 5 层架构 |
| Agent 架构 6 模式 | 6 种架构选型 | Single Agent / Plan & Execute / Multi-Agent / Reflection / RAG+Agent / DAG |
| AI Workflow 6 模式 | 6 种工作流编排 | Sequential Chain / Conditional Router / Parallel Exec / ReAct Loop / Plan & Exec / Multi-Agent |

### 模块 3：核心技术（9 篇）

| 文章 | 核心定位 | 关键内容 |
|------|----------|----------|
| Token 概念 | 理解 Token | BPE 编码、中英文 Token 差异、上下文窗口 |
| LLM 基础 | 大模型基础 | Transformer、API 调用、Fine-tuning 概念 |
| Prompt Engineering | 提示词工程 | 10 大技术：清晰指令/角色设定/XML 标签/CoT/Few-shot/反幻觉等 |
| Context Engineering | 上下文工程 | Budget 管理、System Prompt、工具描述、历史压缩 |
| RAG 与知识检索 | 检索增强生成 | 离线索引 Pipeline、Advanced RAG、GraphRAG、RAGAS 评估 |
| 向量数据库 | 向量检索 | Cosine/欧氏距离/点积、HNSW/IVF、Chroma/Qdrant/Milvus 对比 |
| 记忆系统设计 | Agent 记忆 | 短期记忆(工作台) vs 长期记忆(向量库)、对话历史管理、压缩策略 |
| 推理与规划 5 框架 | 推理规划 | CoT / ReAct / Plan-and-Execute / ToT+MCTS / Reflexion |
| Skills 教程 | 技能系统 | SKILL.md 结构、渐进披露、MCP vs Skills |

### 模块 4：工程框架（2 篇）

| 文章 | 核心定位 | 关键内容 |
|------|----------|----------|
| Harness Engineering | 运行时工程 | Context/Constraints/Feedback/Entropy 4 护栏、6 行业共识 |
| Loop Engineering | 循环工程 | 6 要素(Automations/Worktrees/Skills/Connectors/Sub-Agents/Memory)、5 循环模式 |

### 模块 5：进阶能力（3 篇）

| 文章 | 核心定位 | 关键内容 |
|------|----------|----------|
| 多模态 Agent | 多模态感知 | 图像(GPT-4V/VQA)、语音(ASR→NLU→DM→TTS)、视频理解 |
| 多智能体系统 | 多 Agent 协作 | 层次/平级架构、AutoGen、A2A vs MCP、Orchestrator-Subagent |
| Hugging Face Transformers | HF 生态入门 | Pipeline/Tokenizer/Fine-tuning/LoRA/推理加速 |

### 模块 6：实战落地（5 篇）

| 文章 | 核心定位 | 关键内容 |
|------|----------|----------|
| Python 实现 AI Agent | Agent 编码 | AgentBrain/AgentTools/SimpleAgent 实现 |
| Python 实现 RAG | RAG 编码 | SimpleRAG/AdvancedRAG(reranking+hybrid)/GraphRAG |
| Python 实现推理与规划 | 推理编码 | ReActAgent/ToTAgent/MCTS/ReflexionAgent/PlanAndExecuteAgent |
| Vibe Coding | 编程新范式 | Karpathy 概念、12 工具对比、最佳实践 |
| OpenClaw 教程 | 开源 Agent 部署 | 安装/配置/Skills 系统/Workspace |
| Hermes Agent 教程 | 闭环 Agent 部署 | 安装/模型配置/消息网关 15+ 平台 |

---

## 三、系列特色与亮点

### 3.1 代码优先
系列中大量使用 Python 类实现核心概念，每个 Agent 模式都有可运行的代码示例：
- `ReActAgent` — Thought/Action/Observation 循环
- `SimpleRAG` / `AdvancedRAG` — 检索增强生成
- `AgentBrain` / `AgentTools` — Agent 大脑与工具系统
- `VectorMemory` — 基于 ChromaDB 的记忆系统
- `ShortTermMemory` / `LongTermMemory` — 双记忆架构

### 3.2 横向对比
系列在多处提供工具/框架的横向对比：

| 对比主题 | 涉及工具 |
|----------|----------|
| Workflow 框架 7 选 | LangChain / LangGraph / CrewAI / AutoGen / Dify / Coze / ByteDance |
| 向量数据库 6 选 | Chroma / Qdrant / Weaviate / Milvus / Pinecone / pgvector |
| 推理规划 5 框架 | CoT / ReAct / Plan-and-Execute / ToT+MCTS / Reflexion |
| Vibe Coding 12 工具 | Cursor / Claude Code / Copilot / Windsurf / Trae / Qoder / Bolt.new 等 |

### 3.3 从概念到代码
系列遵循「概念 → 原理 → 架构 → 代码 → 部署」的递进结构，适合自学和教学场景。

---

## 四、外部关联

### 4.1 与 wiki 中其他生态对比的关系

本系列是菜鸟教程的入门教材，而 [[wiki/syntheses/ai-agent-ecosystem-comparison]] 提供的是工具/平台层面的选型框架。两者互补：
- **本系列**：学 AI Agent 是什么、怎么工作、怎么实现
- **生态对比**：选什么工具、平台、框架落地

### 4.2 与 MLOps 生态的关系

系列覆盖的 RAG、向量数据库、Hugging Face 等内容与 [[wiki/syntheses/mlops-ecosystem-overview]] 中的 MLOps 实践有交叉，特别是模型部署和 Pipeline 编排部分。

---

## 五、来源

- [[wiki/sources/ai-agent-tutorial-overview]]
- [[wiki/sources/ai-agent-introduction]]
- [[wiki/sources/ai-agent-working-principle]]
- [[wiki/sources/ai-agent-core-components]]
- [[wiki/sources/ai-agent-glossary]]
- [[wiki/sources/ai-agent-tools-integration]]
- [[wiki/sources/ai-agent-architecture-layers]]
- [[wiki/sources/agent-architecture-patterns]]
- [[wiki/sources/agent-context-engineering]]
- [[wiki/sources/agent-evaluation-safety-alignment]]
- [[wiki/sources/agent-memory-system-design]]
- [[wiki/sources/llm-basics]]
- [[wiki/sources/prompt-engineering-guide]]
- [[wiki/sources/ai-workflow-guide]]
- [[wiki/sources/rookie-harness-engineering]]
- [[wiki/sources/huggingface-transformers-guide]]
- [[wiki/sources/loop-engineering-guide]]
- [[wiki/sources/openclaw-rookie-tutorial]]
- [[wiki/sources/python-ai-agent-implementation]]
- [[wiki/sources/python-rag-implementation]]
- [[wiki/sources/python-reasoning-planning-implementation]]
- [[wiki/sources/rag-and-knowledge-retrieval]]
- [[wiki/sources/skills-tutorial]]
- [[wiki/sources/token-concepts]]
- [[wiki/sources/vibe-coding-rookie-tutorial]]
- [[wiki/sources/vector-database-introduction]]
- [[wiki/sources/multi-agent-system]]
- [[wiki/sources/multimodal-agent]]
- [[wiki/sources/reasoning-and-planning]]
- [[wiki/sources/hermes-agent-rookie-guide]]

## 相关页面

- [[wiki/syntheses/ai-agent-ecosystem-comparison]]
- [[wiki/concepts/harness-engineering]]
- [[wiki/syntheses/claude-skill-management]]
