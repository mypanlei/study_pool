---
title: "Gemini Enterprise Agent Platform vs Kubeflow — 分层对比与企业选型框架"
tags:
  - source
  - gemini
  - kubeflow
  - agent
  - mlops
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://adk.dev/"
source_author: "自建知识库笔记"
source_date: 2026-06-12
---

# Gemini Enterprise Agent Platform vs Kubeflow 对比

> Gemini Enterprise Agent Platform 偏「Agent 产品工程栈」，Kubeflow 偏「AI 平台工程栈」。两者不是同层竞争，而是分层互补。

## 核心论点

1. **设计中心不同** — ADK 核心抽象是 Agent、Tool、Session、Memory、Runner、Evaluation；Kubeflow 核心抽象是 Notebook、Pipeline、TrainJob、Registry、Serving。
2. **生命周期覆盖不同** — Kubeflow 覆盖数据准备→训练→优化→注册→服务的完整 AI lifecycle；Gemini 栈更强在交互式推理、多 Agent 协作、会话状态与长期记忆。
3. **部署模式不同** — Gemini 栈托管能力强，运维复杂度中低；Kubeflow 需自建 Kubernetes 平台，运维复杂度中高到高。
4. **模型策略不同** — Gemini 栈在 Google Cloud 语义内开放；Kubeflow 不预设模型厂商，可接 vLLM/Triton/KServe。
5. **记忆与 RAG** — ADK 中 Memory 是一等公民（MemoryService、Memory Bank、RAG Memory）；Kubeflow 需自行拼装。

## 最佳组合

- **Kubeflow 在下层**：数据准备、训练、微调、模型注册、私有 serving
- **Gemini/ADK 在上层**：Agent 应用层、工具编排、记忆、交互体验

## 受影响的 Wiki 页面

- [[wiki/entities/google-adk]] — 已创建
- [[wiki/entities/kubeflow]] — 已创建
- [[wiki/syntheses/ai-agent-ecosystem-comparison]] — 已更新
