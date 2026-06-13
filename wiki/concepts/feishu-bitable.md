---
title: "飞书多维表格数据模型"
tags:
  - concept
  - feishu
  - bitable
  - data-model
  - low-code
  - database
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Bitable 数据模型
  - 多维表格数据模型
---

# 飞书多维表格数据模型

> 飞书多维表格 (Bitable/Base) 的核心数据模型：以 App 为容器，包含数据表、字段、记录、视图、仪表盘和自动化流程，是一个简化版在线数据库。

## 定义

飞书多维表格的数据模型是一个轻量级在线数据库模型，区别于传统二维电子表格的行列结构，引入了字段类型、数据关联、多视图和自动化等数据库级抽象。

## 核心要点

1. **App (多维表格应用)**：顶层容器，由 `app_token` 标识。可独立存在或嵌入飞书文档/知识库/电子表格。
2. **数据表 (Table)**：数据容器，由 `table_id` 标识。一个 App 可包含多张数据表（如客户表、订单表、合同表）。
3. **记录 (Record)**：数据行，由 `record_id` 标识。一条记录就是一个业务对象实例。
4. **字段 (Field)**：数据列，由 `field_id` 标识。具有明确数据类型（文本/数字/日期/人员/关联/公式/AI 等 20+ 类型），字段上限 300 个。
5. **视图 (View)**：数据的展现方式，由 `view_id` 标识。支持表格/看板/甘特/日历/表单/画册 6 种视图，上限 200 个。
6. **仪表盘 (Block)**：统计与可视化，由 `block_id` 标识。数据表和仪表盘合计上限 100 个。
7. **自动化流程 (Workflow)**：触发条件 + 执行操作，由 `workflow_id` 标识。

## 相关概念

- [[wiki/concepts/agent-skills-system]] — 自动化流程与 Agent 能力对比

## 实体

- [[wiki/entities/feishu-bitable]] — 飞书多维表格实体页
- [[wiki/entities/jira]] — Jira 实体页（对比数据模型）

## 来源

- [[wiki/sources/feishu-bitable-introduction]] — 飞书多维表格系统介绍
- [[wiki/sources/feishu-bitable-vs-jira-comparison]] — 与 Jira 对比
