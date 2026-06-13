---
title: "数据版本控制与数据管理"
tags:
  - concept
  - mlops
  - data-versioning
  - data-management
  - lineage
  - governance
created: 2026-06-13
updated: 2026-06-13
aliases:
  - 数据版本控制
  - 数据管理
  - Data Versioning
  - Data Management
---

# 数据版本控制与数据管理

> MLOps 中数据层的两大核心问题：Data Versioning（数据版本、隔离、回滚、可复现）和 Data Management（发现、血缘、治理、上下文、可观测）。

## 定义

数据版本控制解决"某个训练集在某个时间点是什么"的问题；数据管理解决"团队如何找到可用数据、知道谁负责、变更影响谁"的问题。两者是 MLOps 数据层的不同维度，互为补充。

## 核心要点

### 4 层数据管理能力
1. **数据版本控制**：训练集、特征集、表快照的时间点快照
2. **数据发现与目录**：搜索、owner、schema、用途和可信度
3. **血缘与影响分析**：表/字段/特征变更影响哪些 pipeline、报表或模型
4. **治理与质量**：权限、分类、敏感标签、质量检查、审计

### Data Versioning 工具
- **DVC**：项目级 Git 邻接数据版本，适合单团队可复现实验
- **lakeFS**：对象存储级 Git-like 版本控制，适合多团队共享数据湖
- **Pachyderm**：K8s 原生版本化数据流水线平台
- **Nessie**：Iceberg 湖仓 catalog 事务版本控制

### Data Management 工具
- **DataHub**：组织级元数据图谱中枢
- **OpenMetadata**：语义上下文+质量+血缘统一层
- **Amundsen**：数据发现和搜索
- **OpenLineage/Marquez**：血缘标准与基础设施

## 推荐组合

- 项目级：DVC + MLflow + DataHub
- 数据湖：lakeFS + Spark + OpenMetadata
- Lakehouse：Nessie + Iceberg + OpenLineage + Marquez

## 相关概念

- [[wiki/concepts/mlops-lifecycle]] — MLOps 生命周期中的数据阶段
- [[wiki/entities/lakefs]] — 数据版本控制实现
- [[wiki/entities/datahub]] — 元数据治理实现

## 来源

- [[wiki/sources/mlops-data-versioning-open-source-comparison]]
- [[wiki/sources/internal-mlops-data-versioning-prd]]
- [[wiki/sources/mlops-open-source-platform-comparison]]
