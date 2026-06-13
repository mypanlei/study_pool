---
title: "内部 MLOps 数据版本控制与数据管理平台 PRD"
tags:
  - source
  - mlops
  - prd
  - data-versioning
  - data-management
  - lakefs
  - datahub
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-06-05
---

# 内部 MLOps 数据版本控制与数据管理平台 PRD

> 面向内部平台团队、数据团队和模型开发团队的 PRD，解决 MLOps 中 4 类痛点：训练数据不可复现、数据资产不可发现、数据变更影响不可见、数据治理责任不清晰。

## 核心论点

1. **产品愿景**：建立"数据控制平面 + 元数据平面"，让模型开发团队能回答 5 个问题——用哪版数据、owner 是谁、从哪里来、变更影响谁、是否满足治理要求。
2. **推荐技术栈**：lakeFS（平台级数据版本控制）+ DataHub（组织级 metadata graph）+ OpenLineage/Marquez（统一 lineage 事件模型）+ MLflow + Kubeflow。
3. **MVP 范围**：对象存储训练数据版本化 → 数据资产注册与搜索 → 训练 run 与数据版本关联 → 基础 lineage → owner/标签/状态元数据。
4. **非目标**：不做通用企业级全域数据治理平台、不做全量历史资产一次性治理、不做完整数据质量平台。

## 关键框架

- **产品原则**：平台分层、共享平台优先对象存储语义、本地项目工作流不被破坏、元数据先于自动化治理、MVP 优先 80% 高频痛点。
- **P0/P1/P2 需求矩阵**：5 项 P0（版本控制+数据版本绑定+资产注册+核心 lineage+MLflow 打通），5 项 P1（Kubeflow 集成+治理元数据+审计+权限+运营机制）。
- **MVP 退出标准**：以业务闭环是否成立为准，而非工具部署完成。

## 与现有知识的关系

- 基于 [[wiki/sources/mlops-data-versioning-open-source-comparison]] 的技术选型结论
- 基于 [[wiki/sources/ml-lifecycle-management-official-doc-summary]] 的生命周期框架
- 与 [[wiki/syntheses/mlops-ecosystem-overview]] 中的平台建设部分一致

## 受影响的 Wiki 页面

- [[wiki/concepts/data-versioning-and-management]] — 已更新
- [[wiki/syntheses/mlops-ecosystem-overview]] — 已更新
