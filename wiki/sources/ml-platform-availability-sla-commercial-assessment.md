---
title: "ML Platform Availability SLA 商业评估"
tags:
  - source
  - mlops
  - sla
  - commercial-assessment
  - availability
  - ml-platform
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-06-02
---

# ML Platform Availability SLA 商业评估

> 评估 99.9% 平台可用性目标在商业 ML 平台市场中的位置。结论：99.9% 是主流水平；99.95% 属于更高档需限定条件；99.99% 在 ML-specific 平台中不常见。

## 核心论点

1. **市场对标**：Google Vertex AI、Azure ML、OpenAI Enterprise API 均为 99.9%；AWS SageMaker Online Inference 在多实例条件下为 99.95%；Azure Databricks 为 99.95%。
2. **三档商业定位**：
   - 标准 SKU：99.9%（与主流一致）
   - 高可用 SKU：99.95%（需多实例多可用区架构）
   - 极高可用：避免承诺 99.99% 作为通用 ML 平台 SLA
3. **商务合同注意事项**：必须定义统计周期、统计对象、计量方式、错误定义、排除项和补偿方式。
4. **99.95% 所需架构能力**：多实例推理端点、多可用区部署、控制面和数据面分离、自动故障转移、制品和元数据冗余、可观测性、error budget 机制。

## 关键数据

| Availability | 月度停机时间 | 商业含义 |
|---|---|---|
| 99.9% | 43.2 分钟 | 主流 ML/AI 平台公开 SLA |
| 99.95% | 21.6 分钟 | 高可用档位 |
| 99.99% | 4.32 分钟 | 底层基础设施级别 |

## 与现有知识的关系

- 与 [[wiki/sources/internal-mlops-availability-requirements-user-stories-technical-plan]] 构成商业-技术对照
- 补充 [[wiki/syntheses/mlops-ecosystem-overview]] 中的 SLA 维度

## 受影响的 Wiki 页面

- [[wiki/syntheses/mlops-ecosystem-overview]] — 已更新
