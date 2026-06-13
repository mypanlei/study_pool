---
title: "内部 MLOps 平台 Availability 提升结构化分析"
tags:
  - source
  - mlops
  - availability
  - sla
  - sre
  - structured-analysis
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-06-02
---

# 内部 MLOps 平台 Availability 提升结构化分析

> 本文是 [[Internal-MLOps-Availability-Requirements-User-Stories-Technical-Plan]] 的重新编排版，按评审和汇报逻辑组织为 Background & Motivation → Current Status → Industrial Mature Practice Study → 总体思路 → 需求分解 → User Story 定义 → 执行计划 → Glossary。

## 核心论点

1. **当前状态诊断**：平台存在但还不能证明端到端 99.9% 是否真实可靠，缺少用户旅程级 SLI、状态层单点、上游依赖 OLA 不明确、变更与升级治理缺失。
2. **成熟实践映射**：引入 Google SRE SLI/SLO/Error Budget、OpenSLO、Prometheus Blackbox Exporter、Prometheus Operator、Sloth、Pyrra、Grafana、Alertmanager、ITIL change management 等成熟实践。
3. **三 availability 口径**：Gross user-facing、Net SLA、Platform-owned controllable。
4. **Error budget 分摊模型**：MLOps owned 50%（21.6 分钟）、Upstream critical 30%（13 分钟）、Planned maintenance 10%（4.3 分钟）、Unknown 10%（4.3 分钟）。

## 关键框架

- **执行资产**：Incident 基线记录字段、SLO-as-code 模板、Kubernetes 加固目录、HA 改造清单、Runbook 与 RCA 模板
- **SLA readiness 文档**：包含 Service Scope、Availability Target、Exclusions、Maintenance Window、Upstream Dependency OLA 等

## 与现有知识的关系

- 与 [[wiki/sources/internal-mlops-availability-requirements-user-stories-technical-plan]] 同源，编排结构不同
- 与 [[wiki/sources/mlops-open-source-platform-comparison]] 互补（平台能力 vs 可靠性工程）

## 受影响的 Wiki 页面

- [[wiki/concepts/mlops-lifecycle]] — 已更新
- [[wiki/syntheses/mlops-ecosystem-overview]] — 已更新
