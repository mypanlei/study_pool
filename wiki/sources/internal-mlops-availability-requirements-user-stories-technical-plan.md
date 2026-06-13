---
title: "内部 MLOps 平台 Availability 提升需求拆解与落地计划"
tags:
  - source
  - mlops
  - availability
  - sla
  - sre
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-06-02
---

# 内部 MLOps 平台 Availability 提升需求拆解与落地计划

> 基于 SRE 方法论，将 99.9% availability 目标拆解为 user stories、SLI/SLO、技术分析和分阶段执行计划。面向 ML developer 真实体验，而非仅 Pod 级健康检查。

## 核心论点

1. **ML Developer Core Journey 优先**：availability 应从 ML developer 能否完成关键工作出发（登录、实验查询、pipeline 提交、MLflow 读写、model registry、artifact 上传下载），而非仅看底层 Pod 存活。
2. **三口径统计**：Gross user-facing availability（真实体验）、Net SLA availability（正式承诺）、Platform-owned controllable availability（内部改进）三套口径区分责任边界。
3. **上游依赖治理**：Azure 鉴权、Gerrit/Git、Jenkins、Kubernetes cloud、GPU/CPU/memory 等上游依赖必须纳入 error budget 分摊和 OLA 治理，避免端到端 99.9% 被不可控依赖拖垮。
4. **升级维护计入口径**：K8s/Kubeflow/MLflow 等工具集升级造成的 planned break 计入 gross availability，合规 scheduled maintenance 可从 net SLA 中排除。
5. **分阶段执行路线**：阶段 0（需求冻结）→ 阶段 1（可观测性建立）→ 阶段 2（止血治理）→ 阶段 3（HA 改造）→ 阶段 4（SLO 运营），90 天路线图。

## 关键框架

- **43.2 分钟** error budget（30 天 99.9%）
- **5 类 stakeholder**：Customer、ML developers、MLOps team、IT team、Business owners
- **7 个 Epic**，29 个 User Stories
- **Go/No-Go 条件**：连续 2-3 个月 core journey >= 99.9% 方可正式承诺 SLA

## 与现有知识的关系

- 与 [[wiki/sources/internal-mlops-availability-structured-analysis]] 互为补充（本文为详细技术计划版）
- 与 [[wiki/sources/ml-platform-availability-sla-commercial-assessment]] 构成商业-SLA 对照
- 支撑 [[wiki/concepts/mlops-lifecycle]] 中的生产运维闭环

## 受影响的 Wiki 页面

- [[wiki/concepts/mlops-lifecycle]] — 已更新
- [[wiki/syntheses/mlops-ecosystem-overview]] — 已更新
