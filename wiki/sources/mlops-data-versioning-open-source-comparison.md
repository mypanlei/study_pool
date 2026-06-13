---
title: "MLOps 中 Data Versioning 与 Data Management 开源方案对比"
tags:
  - source
  - mlops
  - data-versioning
  - data-management
  - open-source
  - comparison
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-06-04
---

# MLOps 中 Data Versioning 与 Data Management 开源方案对比

> 结论先行：Data Versioning 和 Data Management 不是同一个问题域。DVC/lakeFS/Pachyderm/Nessie 解决"数据版本、隔离、回滚、可复现"；DataHub/OpenMetadata/Amundsen/Atlas/Marquez 解决"发现、血缘、治理、上下文、可观测"。

## 核心论点

1. **问题分层**：数据管理至少包含 4 层能力——数据版本控制、数据发现与目录、血缘与影响分析、治理与质量。
2. **Data Versioning 方案对比**：DVC（项目级 Git 邻接）、lakeFS（对象存储层 Git-like）、Pachyderm（K8s 原生版本化数据流水线）、Project Nessie（Iceberg 湖仓 catalog 事务）。
3. **Data Management 方案对比**：DataHub（元数据图谱中枢）、OpenMetadata（语义上下文平台）、Amundsen（数据发现）、Apache Atlas（传统强治理）、OpenLineage/Marquez（血缘标准）。
4. **与 MLflow/Kubeflow 的集成关系**：DVC+MLflow 最佳项目级组合；lakeFS+Kubeflow 最佳对象存储数据湖组合；DataHub+MLflow/Kubeflow 最佳组织级 metadata 组合。

## 关键推荐组合

- 小团队：MLflow + DVC + DataHub
- 对象存储数据湖：lakeFS + Spark + OpenMetadata
- Iceberg/Lakehouse：Nessie + Iceberg + OpenLineage + Marquez
- K8s 原生数据平台：Pachyderm + MLflow + DataHub

## 与现有知识的关系

- 被 [[wiki/sources/internal-mlops-data-versioning-prd]] 引用为技术选型基础
- 与 [[wiki/sources/mlops-open-source-platform-comparison]] 互补（数据层 vs 平台层）

## 受影响的 Wiki 页面

- [[wiki/concepts/data-versioning-and-management]] — 已更新
- [[wiki/syntheses/mlops-ecosystem-overview]] — 已更新
