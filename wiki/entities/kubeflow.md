---
title: "Kubeflow"
tags:
  - entity
  - mlops
  - platform
  - kubernetes
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Kubeflow Platform
---

# Kubeflow

> Kubernetes 上的 AI / MLOps reference platform，覆盖训练、Pipeline、模型注册、模型服务的完整 AI 平台底座。

## 关键信息

- **类型**: Kubernetes 上的 AI / MLOps reference platform
- **开发商**: Kubeflow 社区（CNCF 生态）
- **核心定位**: 企业自己的 AI 平台底座
- **默认交付模式**: 自建 / 自运维 Kubernetes 平台
- **主要抽象**: Notebook, Pipeline, TrainJob, Katib, Registry, Serving, KServe

## 核心组件

| 组件 | 描述 |
|------|------|
| Notebooks | Jupyter 开发环境 |
| Pipelines | ML 工作流编排 |
| Trainer | 训练作业管理 |
| Katib | 超参数调优 |
| Model Registry | 模型版本管理 |
| KServe | 模型服务与推理 |

## 核心特色

- **AI 全生命周期**: 数据准备→训练→优化→注册→服务→反馈
- **模型中立**: 不预设模型厂商，可接 vLLM/Triton/KServe
- **高控制权**: 多云/私有化/混合云
- **开源自托管**: Kubernetes-native，跨云可移植性强

## 对比 ADK/Gemini 栈

| 维度 | Kubeflow | Gemini 栈 |
|------|----------|-----------|
| 设计中心 | 训练/模型生命周期 | Agent 应用/推理编排 |
| 记忆/RAG | 需自建或外接 | 一等公民能力 |
| 运维复杂度 | 高 | 中低 |
| 可移植性 | 高（Kubernetes-native） | 中（GCP 依赖） |

## 来源

- [[wiki/sources/gemini-enterprise-vs-kubeflow-comparison]]
- [[wiki/sources/gemini-kubeflow-dify-langgraph-comparison]]
