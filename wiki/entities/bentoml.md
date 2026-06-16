---
title: "BentoML"
tags:
  - entity
  - mlops
  - serving
created: 2026-06-17
updated: 2026-06-17
aliases:
  - BentoML 模型服务
---

# BentoML

> 开源模型服务框架，将模型打包为标准 Bento（可部署单元），支持 Python-native 的 serving 和多种云部署目标。

## 关键信息

- **类型**: 开源模型服务框架
- **GitHub Stars**: ~8.7k（截至 2026-06）
- **定位**: 从训练到生产的模型服务桥梁
- **核心概念**: Bento（标准可部署单元）

## 核心能力

| 能力 | 说明 |
|------|------|
| **Bento 打包** | 模型 + 代码 + 依赖 + 配置 → 标准构件 |
| **Python-native** | `@bentoml.service` decorator 定义 API |
| **多框架支持** | PyTorch/TensorFlow/Scikit-learn/XGBoost |
| **云部署** | Docker/K8s/SageMaker/Vertex AI/Lambda |

## 推荐组合

个人小团队：MLflow + DVC + BentoML
K8s 企业：Kubeflow + KServe + BentoML

## 来源

- [[wiki/sources/mlops-open-source-platform-comparison]]
