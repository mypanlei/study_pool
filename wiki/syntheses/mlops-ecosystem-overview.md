---
title: "MLOps 生态全景"
tags:
  - synthesis
  - mlops
  - availability
  - platform-comparison
  - data-versioning
  - sla
created: 2026-06-13
updated: 2026-06-13
aliases:
  - MLOps 全景
---

# MLOps 生态全景

> 综合 7 篇 MLOps 主题文章的跨源综合分析，涵盖平台可用性工程、生命周期管理、开源平台对比、数据版本控制与数据管理、SLA 商业评估。

## 背景

本次综合覆盖 7 篇 MLOps 领域的深度文章：2 篇内部平台可用性分析（Requirements + Structured Analysis）、1 篇 ML 生命周期管理官方文档总结、1 篇数据版本控制方案对比、1 篇 MLOps 开源平台对比、1 篇 SLA 商业评估、1 篇数据管理平台 PRD。这些文章从不同维度描绘了 MLOps 平台的完整图景。

## 各方观点

### 维度 A：平台可用性工程
来源：[[wiki/sources/internal-mlops-availability-requirements-user-stories-technical-plan]], [[wiki/sources/internal-mlops-availability-structured-analysis]]

强调面向 ML developer 真实体验的可用性定义，提出 99.9% SLO 需分解为用户旅程 SLI、error budget 分摊和上游依赖治理。核心输出是 7 个 Epic（29 个 User Stories）和 90 天分阶段执行路线图。

### 维度 B：生命周期管理
来源：[[wiki/sources/ml-lifecycle-management-official-doc-summary]]

从 AWS/Google/Azure/MLflow/Kubeflow/NIST 官方资料出发，定义 ML 生命周期 8 阶段模型，强调 MLOps = DevOps + DataOps + Model Governance，以及 CI/CD/CT 三线自动化。

### 维度 C：平台选型
来源：[[wiki/sources/mlops-open-source-platform-comparison]], [[wiki/sources/mlops-data-versioning-open-source-comparison]]

不存在单一最优平台。MLflow+DVC 为最通用基础组合；Kubeflow 为最完整 K8s 原生平台；Data Versioning（DVC/lakeFS/Nessie）和 Data Management（DataHub/OpenMetadata）是不同问题域。

### 维度 D：SLA 商业评估与产品化
来源：[[wiki/sources/ml-platform-availability-sla-commercial-assessment]], [[wiki/sources/internal-mlops-data-versioning-prd]]

99.9% 为主流 ML 平台水平，99.95% 需架构支撑。PRD 层面建议先解决训练可复现、数据可发现、影响可见和责任清晰 4 类问题。

## 对比分析

| 维度 | 可用性工程视角 | 生命周期视角 | 平台选型视角 | 商业视角 |
|------|--------------|------------|------------|---------|
| 核心关注 | SLO/SLI/Error Budget | 流程闭环 | 工具组合 | 合同/市场定位 |
| 度量方式 | 43.2 分钟/月 | 阶段完成度 | 生命周期覆盖度 | % 可用性 |
| 主要工具 | Prometheus/Grafana/Alertmanager | MLflow/Kubeflow | DVC/lakeFS/DataHub | - |
| 组织层级 | SRE/Platform | ML/Lifecycle | Architecture | Business/Product |

## 综合结论

一个成熟的 MLOps 平台需要同时满足 **4 个维度**的要求：

1. **可用性可靠**：有明确的 SLO/SLI、error budget、依赖治理和分阶段执行路径
2. **生命周期完整**：覆盖从业务定义到模型退役的全链路，支持 CI/CD/CT 自动化
3. **工具组合合理**：根据团队规模和数据形态选择合适的组合（而非追求单一"最佳平台"）
4. **商业可持续**：SLA 口径与市场一致，产品化路径清晰

## 开放问题

- 如何平衡 99.9% availability 投入与平台新功能开发速度？
- 数据版本控制（lakeFS/Nessie）和元数据治理（DataHub/OpenMetadata）的演进优先级如何确定？
- 内部平台 vs 公有云 ML 平台的长期成本与能力差异评估

## 来源

- [[wiki/sources/internal-mlops-availability-requirements-user-stories-technical-plan]]
- [[wiki/sources/internal-mlops-availability-structured-analysis]]
- [[wiki/sources/ml-lifecycle-management-official-doc-summary]]
- [[wiki/sources/mlops-open-source-platform-comparison]]
- [[wiki/sources/mlops-data-versioning-open-source-comparison]]
- [[wiki/sources/ml-platform-availability-sla-commercial-assessment]]
- [[wiki/sources/internal-mlops-data-versioning-prd]]
