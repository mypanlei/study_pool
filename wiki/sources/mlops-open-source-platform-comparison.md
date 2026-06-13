---
title: "常用 MLOps 开源平台对比"
tags:
  - source
  - mlops
  - open-source
  - comparison
  - platform-selection
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-06-02
---

# 常用 MLOps 开源平台对比

> 基于各项目官方文档、GitHub 仓库和权威资料，比较 Kubeflow、MLflow、ZenML、Metaflow、Flyte、Kedro、DVC、ClearML、Feast、BentoML、KServe 的定位、技术指标、生命周期覆盖范围和选型建议。

## 核心论点

1. **不存在单一最优平台**：最通用的是 MLflow（实验追踪+模型注册）+ DVC（数据版本）；最完整 K8s 原生平台是 Kubeflow；生产编排可选 ZenML/Metaflow/Flyte/Kedro。
2. **分层选型框架**：按生命周期能力拆分——全生命周期（Kubeflow/ClearML）、实验追踪（MLflow）、训练编排（ZenML/Metaflow/Flyte/Kedro）、数据版本（DVC）、特征平台（Feast）、模型服务（BentoML/KServe）。
3. **通用程度排序**：MLflow 和 DVC 通用程度最高，不强制 K8s；Kubeflow 适合平台工程团队；ClearML 适合一体化套件需求。
4. **推荐组合**：个人小团队（MLflow+DVC+BentoML）、K8s 企业栈（Kubeflow+KServe+Feast）、LLM 应用（MLflow+BentoML+KServe）。

## 技术指标

截至 2026-06-02，主要项目 GitHub stars：MLflow 26.2k、Kubeflow 15.7k、DVC 15.6k、Kedro 10.9k、Metaflow 10.1k、BentoML 8.7k、Flyte 7.1k、Feast 7.1k、ClearML 6.7k、ZenML 5.4k、KServe 5.5k。

## 与现有知识的关系

- 与 [[wiki/sources/gemini-enterprise-vs-kubeflow-comparison]] 互补
- 被 [[wiki/sources/ai-platform-product-manager-role-framework]] 引用为平台选型知识基础

## 受影响的 Wiki 页面

- [[wiki/concepts/mlops-lifecycle]] — 已更新
- [[wiki/syntheses/mlops-ecosystem-overview]] — 已更新
