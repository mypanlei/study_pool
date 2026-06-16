---
title: "DVC (Data Version Control)"
tags:
  - entity
  - mlops
  - data
  - versioning
created: 2026-06-17
updated: 2026-06-17
aliases:
  - DVC 数据版本控制
---

# DVC (Data Version Control)

> ML 领域最广泛使用的数据版本控制工具。基于 Git 的「存储不可变、逻辑可版本」理念，将大文件/数据集存储在外部存储（S3/GCS/本地），Git 仓库仅保存 DVC 指针文件。

## 关键信息

- **类型**: 开源数据版本控制工具
- **GitHub**: iterative/dvc
- **Stars**: ~15.6k（截至 2026-06）
- **核心理念**: `git + cloud storage` 的数据版本管理

## 核心能力

| 能力 | 说明 |
|------|------|
| 数据集版本管理 | `dvc add/commit/push/pull` 类似 Git |
| Pipeline 编排 | `dvc.yaml` 定义多步流水线 |
| 指标追踪 | `dvc metrics diff` 对比实验结果 |
| 云存储集成 | S3/GCS/Azure/SSH/MinIO |

## 推荐定位

- 个人/小团队 MLOps 最佳数据版本工具
- 与 MLflow（实验追踪）+ BentoML（模型服务）组合使用
- 比 lakeFS/Pachyderm/Nessie 更轻量，不强制 K8s

## 来源

- [[wiki/sources/mlops-open-source-platform-comparison]]
- [[wiki/concepts/data-versioning-and-management]]
- 知识库内 24 处引用
