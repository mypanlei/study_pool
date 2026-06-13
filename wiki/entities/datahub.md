---
title: "DataHub"
tags:
  - entity
  - mlops
  - open-source
  - metadata
  - data-catalog
  - governance
created: 2026-06-13
updated: 2026-06-13
aliases:
  - DataHub
  - 数据中枢
---

# DataHub

> LinkedIn 开源的组织级元数据图谱与 AI data catalog 平台。覆盖 discovery、governance、observability、real-time metadata graph，支持 80+ connectors。

## 关键信息

- **类型**: 开源项目（元数据平台）
- **License**: Apache-2.0
- **定位**: 组织级 metadata graph 中枢
- **生态集成**: MLflow、Kubeflow、Feast、SageMaker、dbt、Airflow 等
- **部署复杂度**: 中高

## 核心能力

- 数据资产发现与搜索
- Schema、owner、lineage、治理、质量、影响分析
- 实时元数据图谱
- AI agents / MCP 集成

## 在 MLOps 生态中的角色

- 不对实际数据做 branch/commit/version（与 lakeFS/DVC 互补）
- 与 MLflow/Kubeflow 为强互补关系：MLflow 负责实验和 registry，DataHub 负责资产发现、owner、lineage、影响分析、治理
- 常与 lakeFS（数据版本）+ MLflow（实验追踪）组合

## 来源

- [[wiki/sources/mlops-data-versioning-open-source-comparison]]
- [[wiki/sources/internal-mlops-data-versioning-prd]]
