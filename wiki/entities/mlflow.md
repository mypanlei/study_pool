---
title: "MLflow"
tags:
  - entity
  - mlops
  - open-source
  - experiment-tracking
  - model-registry
created: 2026-06-13
updated: 2026-06-13
aliases:
  - MLflow
  - MLflow Tracking
  - MLflow Model Registry
---

# MLflow

> 开源 AI/ML 生命周期管理平台，核心能力覆盖 experiment tracking、model registry、model packaging 和 deployment workflow。GitHub stars ~26.2k，是实验追踪和模型注册领域的事实标准之一。

## 关键信息

- **类型**: 开源项目
- **创建时间**: 2018-06
- **License**: Apache-2.0
- **主语言**: Python
- **GitHub**: [mlflow/mlflow](https://github.com/mlflow/mlflow)
- **定位**: 实验追踪与模型注册基础设施，非完整 pipeline orchestrator

## 核心能力

- **MLflow Tracking**: 记录 parameters、metrics、models、artifacts
- **MLflow Models**: 模型打包格式
- **MLflow Model Registry**: 模型注册、版本、alias、tag、annotation
- **MLflow Deployments**: 部署和推理接口
- **MLflow Evaluation**: 传统 ML 和 GenAI evaluation

## 在 MLOps 生态中的角色

- 通用程度极高，可与 PyTorch、TensorFlow、Scikit-learn、Spark 等生态兼容
- 常与 DVC（数据版本）、Kubeflow（pipeline）、DataHub（metadata graph）组合使用
- Databricks 提供托管版 MLflow，补全企业级治理

## 来源

- [[wiki/sources/mlops-open-source-platform-comparison]]
- [[wiki/sources/ml-lifecycle-management-official-doc-summary]]
- [[wiki/sources/internal-mlops-data-versioning-prd]]
