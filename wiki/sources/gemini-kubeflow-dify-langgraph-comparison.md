---
title: "Gemini、Kubeflow、Dify、LangGraph 四方对比 — 分层定位与选型指南"
tags:
  - source
  - gemini
  - kubeflow
  - dify
  - langgraph
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "internal note"
source_author: "自建知识库笔记"
source_date: 2026-06-12
---

# Gemini、Kubeflow、Dify、LangGraph 四方对比

> 四者分属不同层级：Gemini 和 Dify 在应用交付层，LangGraph 在编排与 runtime 层，Kubeflow 在模型平台与基础设施层。

## 核心论点

1. **分层定位** — Gemini Enterprise Agent Platform = Google Cloud 托管型企业 Agent 栈；Kubeflow = Kubernetes AI 平台底座；Dify = 开源低代码 AI 应用平台；LangGraph = 低层 Agent 编排框架。
2. **Gemini vs Dify** — Gemini 偏托管/代码优先/GCP 深集成；Dify 偏开源/自托管/低代码/业务交付效率。
3. **Gemini vs LangGraph** — Gemini 强在完整托管生态与企业交付闭环；LangGraph 强在自行掌控 orchestration runtime。
4. **Dify vs LangGraph** — 低代码平台与低层框架的典型对比：Dify 快交付、可视化；LangGraph 深控制、长状态。
5. **Kubeflow 与三者** — Kubeflow 不是其他三者的替代品，而是下层基础设施候选。

## 典型组合

- Kubeflow + Gemini：训练/模型平台 + 上层 Agent
- Kubeflow + LangGraph：模型平台 + 复杂 Agent runtime
- Dify + 自有模型：快速交付 + 自托管

## 受影响的 Wiki 页面

- [[wiki/entities/dify]] — 已创建
- [[wiki/entities/langgraph]] — 已创建
- [[wiki/entities/google-adk]] — 已创建
- [[wiki/entities/kubeflow]] — 已创建
- [[wiki/syntheses/ai-agent-ecosystem-comparison]] — 已更新
