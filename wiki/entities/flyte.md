---
title: "Flyte"
tags:
  - entity
  - mlops
  - platform
  - orchestration
created: 2026-06-15
updated: 2026-06-15
aliases:
  - Flyte Platform
  - Flyte 工作流引擎
---

# Flyte

> Lyft/Union.ai 开源的 ML 工作流编排平台。核心哲学：把 Kubernetes 抽象掉，提供纯 Python 开发者体验。在 2025-2026 年被广泛视为"Kubeflow 的更轻量替代"。

## 关键信息

- **类型**: ML Pipeline 编排平台
- **开发商**: Lyft → Union.ai（开源 + 托管）
- **核心定位**: 生产级数据与 ML 工作流编排，强调开发者体验
- **Python SDK**: `flytekit` — 原生 Python decorator（`@task`、`@workflow`）
- **GitHub Stars**: ~7.1k（截至 2026-06）

## 与 Kubeflow 核心差异

| 维度 | Kubeflow | Flyte |
|------|----------|-------|
| 设计哲学 | K8s-native，薄层封装 K8s | **抽象掉 K8s**，纯 Python 体验 |
| 目标用户 | ML 工程师 + DevOps | 数据科学家、ML 工程师（Ops 负担低） |
| 资源占用 | ~40 pods / 12GB RAM idle | **~3-4 pods / 2.5GB RAM**（少 90%） |
| 本地开发 | 需 Kind/Minikube | 两命令启动：`flytectl demo start` |
| 迭代速度 | 每次改代码需重新 build 容器 | **Fast Registration**，无需 Docker rebuild |
| 动态 DAG | 有限（v2 不原生支持） | **原生 `@dynamic`**，纯 Python 动态图 |
| 强类型系统 | 基础类型 | 丰富 ML 类型（torch/numpy/pandas/Spark） |
| 多租户 | 有限 | **一等公民**（RBAC/配额/命名空间隔离） |
| Checkpoint/恢复 | ❌ | ✅ 内置 intra-task checkpoint |
| 模型服务 | ✅ KServe/Triton/Seldon | ❌ 非原生（需 UnionML/外部集成） |
| 通知 | ❌ 需 Argo/自定义 | ✅ 原生 Email/Slack/PagerDuty |
| TCO | ~2-3x **更高**（基础架构+人力） | **更低**，多家迁移后降 40-67% 成本 |

## 核心特色

1. **纯 Python DX** — `@task` `@workflow` decorator，数据科学家不需要知道 K8s
2. **Fast Registration** — Python-only 修改无需 rebuild Docker，调试秒级 vs Kubeflow 10-15 分钟
3. **动态工作流** — 运行时动态生成 DAG，适合 AI Agent 和复合 AI 系统
4. **强类型系统** — 原生支持 ML 数据类型，编译期类型检查
5. **Flyte 2.0**（2025-09）— 明确面向"后静态 DAG 时代"：纯 Python、崩溃恢复、资源感知伸缩

## 市场趋势

- AI 编排市场 ~25% CAGR
- Flyte 是增长更快的替代方案，尤其重视开发者速度和成本控制的团队
- 复合 AI 系统（多模型/多工具编排）更偏向 Flyte 的动态工作流模型

## 来源

- [[wiki/sources/mlops-open-source-platform-comparison]]
- [[wiki/syntheses/mlops-ecosystem-overview]]
