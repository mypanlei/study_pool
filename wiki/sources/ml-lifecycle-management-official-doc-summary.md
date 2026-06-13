---
title: "ML 生命周期管理官方文档总结"
tags:
  - source
  - mlops
  - lifecycle-management
  - model-governance
  - ml-platforms
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队（基于 AWS/Google Cloud/Azure/MLflow/Kubeflow/NIST 官方文档整理）"
source_date: 2026-06-01
---

# ML 生命周期管理官方文档总结

> 综合 Google Cloud、AWS、Azure、MLflow、Kubeflow、NIST 等官方资料的 ML 生命周期管理笔记。核心观点：ML 生命周期管理是把业务目标、数据、实验、模型、部署、监控、治理和持续改进连接成可追踪、可复现、可审计、可自动化的闭环。

## 核心论点

1. **生命周期 8 阶段**：业务目标识别 → ML 问题定义 → 数据处理 → 实验与模型开发 → 模型评估与上线门禁 → 模型注册 → 部署与发布 → 生产监控（含反馈与再训练闭环）→ AI 风险治理。
2. **MLOps 不是 DevOps 复制**：MLOps = DevOps + DataOps + Model Governance，多了数据版本、模型漂移、实验管理、模型注册与审批等独特挑战。
3. **CI/CD/CT 三层自动化**：Google Cloud 成熟度模型（Level 0 手动 → Level 1 自动化 pipeline → Level 2 CI/CD pipeline），CT（持续训练）是 ML 特有的自动化维度。
4. **反模式总结**：Notebook 即生产、只保存模型文件不保存上下文、只有离线指标没有线上监控、自动化部署没有门禁、MLOps 被误解为工具采购。

## 关键平台映射

- AWS：SageMaker Pipelines + Model Registry + Model Monitor + Clarify
- Google Cloud：Vertex AI Pipelines + CI/CD/CT + TFX
- Azure：Azure ML + Model Registry + Event Grid + Endpoints
- MLflow：Tracking + Model Registry + Aliases
- Kubeflow：Pipelines + Katib + KServe + Notebooks
- NIST AI RMF：GOVERN/MAP/MEASURE/MANAGE 四函数贯穿生命周期

## 与现有知识的关系

- 为 [[wiki/syntheses/mlops-ecosystem-overview]] 提供生命周期理论基础
- 被 [[wiki/sources/ai-platform-product-manager-role-framework]] 引用为 AI 工作流理解的基础

## 受影响的 Wiki 页面

- [[wiki/concepts/mlops-lifecycle]] — 已更新
- [[wiki/syntheses/mlops-ecosystem-overview]] — 已更新
