---
title: "KServe"
tags:
  - entity
  - mlops
  - serving
  - kubeflow
created: 2026-06-17
updated: 2026-06-17
aliases:
  - KServe 模型服务
---

# KServe

> Kubeflow 生态中的模型推理服务组件，前身为 KFServing。提供 Kubernetes-native 的模型 serving，支持多种推理框架和自动伸缩。

## 关键信息

- **类型**: 开源模型推理服务框架
- **前身**: KFServing
- **生态**: Kubeflow, Knative, Istio
- **定位**: 生产级模型 inference 的 Kubernetes 标准方案

## 支持的推理框架

| 框架 | 说明 |
|------|------|
| **Triton Inference Server** | NVIDIA 高性能推理 |
| **vLLM** | LLM 推理加速 |
| **TFServing** | TensorFlow 模型 |
| **TorchServe** | PyTorch 模型 |
| **ONNX Runtime** | 跨平台推理 |
| **MLServer** | Seldon 的通用框架 |

## 核心特性

- Serverless 自动伸缩（缩零）
- 金丝雀/蓝绿部署
- 请求级自动缩放（InferenceGraph）
- Prometheus 监控集成
- 多模型服务（ModelMesh）

## 来源

- [[wiki/sources/mlops-open-source-platform-comparison]] — MLOps 开源平台对比，涵盖 KServe 定位
- [[wiki/sources/flyte-vs-kubeflow-comparison]] — Kubeflow 生态组件比较
- [[wiki/entities/kubeflow]]
