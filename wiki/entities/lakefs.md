---
title: "lakeFS"
tags:
  - entity
  - mlops
  - open-source
  - data-versioning
  - data-lake
created: 2026-06-13
updated: 2026-06-13
aliases:
  - lakeFS
  - Git for Data
---

# lakeFS

> 对象存储层的 Git-like 数据版本控制平台。支持 branch、commit、merge，不复制数据即可获得隔离的数据环境，适配 Spark、Hive、Athena、DuckDB、Presto 等现代数据框架。

## 关键信息

- **类型**: 开源项目
- **License**: Apache-2.0
- **定位**: 对象存储数据湖版本控制层
- **部署复杂度**: 中到中高
- **版本控制粒度**: bucket/prefix/object 集合
- **核心语义**: branch、commit、merge 明确

## 核心能力

- 数据湖 dev/test/prod 数据分支
- write-audit-publish 流程
- 不复制数据回溯、审计、回滚和重放
- 适配 S3/Azure Blob/GCS

## 在 MLOps 生态中的角色

- 主要解决存储层版本隔离，不负责完整目录治理（需 DataHub/OpenMetadata 补上层）
- 与 MLflow 强互补：lakeFS 管数据版本，MLflow 管实验和模型注册
- 与 Kubeflow 强互补：Kubeflow 是执行平面，lakeFS 是数据控制平面
- 推荐组合：lakeFS + Spark + OpenMetadata

## 来源

- [[wiki/sources/mlops-data-versioning-open-source-comparison]]
- [[wiki/sources/internal-mlops-data-versioning-prd]]
