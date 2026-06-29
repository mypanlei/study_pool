---
title: "MLOps: CI/CD/CT Pipelines — Google Cloud Architecture Center"
tags:
  - source
  - mlops
  - machine-learning
  - google-cloud
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning"
source_author: "Google Cloud Architecture Center (Jarek Kazmierczak, Khalid Salama, Valentin Huerta)"
source_date: 2026
aliases:
  - Google MLOps CI/CD CT Guide
  - GCP MLOps Pipeline Automation
---

# MLOps: CI/CD/CT Pipelines — Google Cloud Architecture Center

> Google Cloud 官方发布的 MLOps CI/CD/CT 指南，系统定义了三层 MLOps 成熟度模型（Level 0/1/2），详细阐述了 ML 系统中持续集成、持续交付和持续训练的实现方法。本文直接引用了 [[wiki/sources/hidden-technical-debt-ml-sculley-2015|Hidden Technical Debt in Machine Learning Systems]] 的 ML 系统组件图。

## 核心论点

1. **ML 系统的真实构成**：只有一小部分 ML 系统由 ML 代码构成，周围的基础设施（配置、自动化、数据收集、数据验证、测试、资源管理、模型分析、流程管理、服务基础设施、监控）广阔且复杂。引用 Sculley 2015 的 ML 技术债务框架。

2. **MLOps vs DevOps 五大差异**：团队技能（数据科学家可能非专业软件工程师）、开发（实验性本质+追踪/复现挑战）、测试（需数据验证+模型质量评估+模型验证）、部署（多步 pipeline 而非单个服务）、生产（模型因数据漂移而衰减）。

3. **ML 独特之处**：CI 需要测试数据和数据 schema 和模型；CD 是部署 ML 训练 pipeline（而非单个软件包）；**CT（持续训练）** 是 ML 系统独有的新维度。

4. **MLOps Level 0：手动流程** — 数据科学家的交互式 notebook 驱动流程，ML 与运维脱节，发布频率低（每年几次），无 CI/CD，部署仅关注预测服务，缺乏性能监控。

5. **MLOps Level 1：ML pipeline 自动化** — 目标是通过自动化 ML pipeline 实现 CT。引入数据验证（schema 偏差/数值偏差）和模型验证（离线+在线），可选特征存储（Feature Store）、元数据管理、pipeline 触发器（按需/定时/新数据可用/性能退化/概念漂移）。

6. **MLOps Level 2：CI/CD pipeline 自动化** — 完整六阶段：开发实验 → Pipeline CI（构建+测试） → Pipeline CD（部署到目标环境） → 自动触发 → 模型 CD → 监控。CI 包含特征工程单元测试、模型收敛测试、NaN 检测、组件 artifact 测试、集成测试。

## 受影响的 Wiki 页面

- [[wiki/concepts/mlops-lifecycle]] — 三层成熟度模型是对现有 MLOps 生命周期的重要补充
- [[wiki/syntheses/mlops-ecosystem-overview]] — 可增加 Google MLOps 成熟度模型视角
