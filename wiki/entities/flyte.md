---
title: "Flyte"
tags:
  - entity
  - mlops
  - orchestration
  - workflow
created: 2026-06-15
updated: 2026-06-15
aliases:
  - Flyte 工作流引擎
---

# Flyte

> Lyft/Union.ai 开源的 **ML 工作流编排引擎**。它不是完整 MLOps 平台，而是专注做好「Pipeline 编排」这一层的工具。

## ⚠️ 关键澄清：Flyte 不是完整 MLOps 平台

**Flyte 和 Kubeflow 不是一个层面的解决方案。**

- **Kubeflow** = 完整 MLOps 平台（Notebooks + Pipelines + Katib + Training + Model Registry + KServe 等）
- **Flyte** = 只做 **Pipeline/Workflow 编排** 这一件事

所谓 "Flyte vs Kubeflow" 的对比，实际是 **Flyte vs Kubeflow Pipelines**（Kubeflow 的一个子组件）。拿 Flyte 和整个 Kubeflow 比，就像拿「MySQL 和 AWS 比」。

## 层级定位

```
                    ┌──────────────────────┐
                    │  Model Serving        │ ← KServe / BentoML
                    ├──────────────────────┤
                    │  Model Registry       │ ← MLflow Model Registry
                    ├──────────────────────┤
                    │  Hyperparameter Tuning│ ← Katib / Optuna
                    ├──────────────────────┤
  Flyte 在这里 →    │  Pipeline 编排        │ ← Kubeflow Pipelines / Flyte / Airflow
                    ├──────────────────────┤
                    │  Experiment Tracking  │ ← MLflow Tracking / W&B
                    ├──────────────────────┤
                    │  Data Versioning      │ ← DVC / lakeFS
                    └──────────────────────┘
```

## Flyte 不包含什么

对比 Kubeflow 完整平台，Flyte **没有**：

| 能力 | Kubeflow | Flyte |
|------|----------|-------|
| 模型服务 (Serving) | ✅ KServe / Triton | ❌ 需另接 BentoML/FastAPI |
| 超参调优 | ✅ Katib | ❌ 需另接 Optuna |
| 实验追踪 | ✅ 可接 MLflow | ❌ 需另接 |
| 模型注册表 | ✅ Model Registry | ❌ 需另接 |
| Notebook 环境 | ✅ Jupyter | ❌ |
| 特征平台 | ✅ + Feast | ❌ |

## Flyte 真正专注什么

Flyte 专注的是 **Pipeline 编排层**的最佳体验：

1. **纯 Python DX** — `@task` `@workflow` decorator，数据科学家不需要知道 K8s
2. **强类型系统** — torch/numpy/pandas/Spark 类型原生支持，编译期检查
3. **Fast Registration** — Python 修改无需 rebuild Docker，秒级迭代
4. **动态 DAG** — 运行时动态生成图，适合条件/循环/自适应流程
5. **多租户一等公民** — RBAC、配额、命名空间隔离
6. **内置 Checkpoint** — 故障恢复从中断点继续，而非从头重跑

## 所以你应该这样理解

> Flyte 竞争的不是 Kubeflow 整体，而是 **Kubeflow Pipelines** 这一个组件。它在编排层做得比 KFP 更好（DX、类型系统、动态图），但你要自己补齐 Serving、Registry、Tuning 等其他层。

## 来源

- [[wiki/sources/mlops-open-source-platform-comparison]]
- [[wiki/syntheses/mlops-ecosystem-overview]]
