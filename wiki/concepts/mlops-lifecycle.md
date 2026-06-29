---
title: "MLOps 生命周期"
tags:
  - concept
  - mlops
  - lifecycle
  - model-governance
  - machine-learning
created: 2026-06-13
updated: 2026-06-29
aliases:
  - ML 生命周期
  - MLOps 全链路
  - 机器学习生命周期管理
---

# MLOps 生命周期

> 将 DevOps、DataOps 和模型治理思想应用于 ML 系统的工程实践。核心是将业务目标、数据、实验、模型、部署、监控、治理和持续改进连接成可追踪、可复现、可审计、可自动化的闭环。

## 定义

MLOps 生命周期覆盖从业务问题定义到模型退役的全流程管理方法，包括数据准备、模型开发、模型部署、生产监控、持续训练和风险治理。

## 核心要点

1. **8 阶段生命周期**：业务目标识别 → ML 问题定义 → 数据处理 → 实验与模型开发 → 模型评估与门禁 → 模型注册 → 部署与发布 → 生产监控与再训练
2. **与 DevOps 差异**：MLOps = DevOps + DataOps + Model Governance，额外需要数据版本、模型漂移检测、实验管理、模型注册和审批。
3. **CI/CD/CT 自动化**：持续训练（CT）是 ML 特有的自动化维度，因为数据分布变化会导致模型自然退化。
4. **平台支撑**：MLflow（实验追踪/模型注册）+ Kubeflow（pipeline 编排）+ KServe（模型服务）+ Feast（特征管理）+ DataHub（元数据治理）。

## 学术根基

[[wiki/sources/hidden-technical-debt-ml-sculley-2015|Hidden Technical Debt in Machine Learning Systems]]（Sculley et al., Google, NeurIPS 2015）是 MLOps 领域引用最多的奠基性论文之一。该论文首次将"技术债务"框架系统性地应用于 ML 系统，揭示了传统代码维护问题之外的 ML 特有风险因素：

- **CACE 原则**（Changing Anything Changes Everything）—— ML 系统中任何输入变化都会影响所有其他部分
- **ML 系统反模式**——胶水代码、管道丛林、死亡实验代码路径、抽象债务
- **配置债务**——配置行数可远超代码行数
- **数据依赖债务**——不稳定依赖、未利用依赖、缺乏静态分析工具
- **反馈循环**——直接和隐藏反馈循环使系统行为难以预测

这些发现构成了 MLOps 生命周期中生产监控、数据管理、实验管理等环节的理论基础。

## 详细阐述

### 5 类核心能力
1. **项目和实验管理**：实验跟踪、指标记录、artifact 管理
2. **数据管理**：数据版本、特征工程、数据质量监控
3. **训练与编排**：pipeline 自动化、超参数搜索、分布式训练
4. **模型资产与部署**：模型注册、版本管理、灰度/蓝绿部署
5. **生产运维与治理**：监控、漂移检测、再训练、审计、风险治理

## MLOps 成熟度模型

Google Cloud Architecture Center 定义了 MLOps 三层成熟度模型（[[wiki/sources/mlops-google-cloud-cicd-ct-pipelines]]），从手动到完全自动化：

### Level 0：手动流程
数据科学家在 notebook 中进行交互式实验，ML 与运维脱节。特性：每步手动执行、ML 研究和工程分离、年发布次数极少、无 CI/CD、部署仅关注预测服务、缺乏性能监控。

### Level 1：ML Pipeline 自动化
目标是通过自动化 ML pipeline 实现持续训练（CT）。引入数据验证（schema 偏差/数值偏差检测）和模型验证（离线评估+在线金丝雀部署）。可选组件：特征存储（Feature Store）、元数据管理、pipeline 触发器（按需/定时/新数据/性能退化/概念漂移）。

### Level 2：CI/CD Pipeline 自动化
完整六阶段自动化：开发实验 → Pipeline CI（构建+单元测试+集成测试） → Pipeline CD（部署到目标环境） → 自动触发 → 模型 CD（部署预测服务） → 监控。CI 包含特征工程测试、模型收敛测试、NaN 检测、组件 artifact 测试。

### 关键差异
| 维度 | Level 0 | Level 1 | Level 2 |
|------|---------|---------|---------|
| 流程 | 手动 notebook | 自动化 ML pipeline | CI/CD + ML pipeline |
| 发布频率 | 年/几次 | 周/月 | 天/周 |
| CI | 无 | 代码测试 | 代码+数据+模型测试 |
| CD | 无 | 模型预测服务 | Pipeline + 模型 |
| CT | 无 | 是（触发器驱动） | 是（全自动） |

## 相关概念

- [[wiki/concepts/data-versioning-and-management]] — 数据层的版本与治理
- [[wiki/concepts/ai-platform-product-manager]] — 平台产品化组织角色

## 来源

- [[wiki/sources/ml-lifecycle-management-official-doc-summary]]
- [[wiki/sources/mlops-open-source-platform-comparison]]
- [[wiki/sources/internal-mlops-availability-requirements-user-stories-technical-plan]]
- [[wiki/sources/internal-mlops-availability-structured-analysis]]
- [[wiki/sources/ml-platform-availability-sla-commercial-assessment]]
- [[wiki/sources/hidden-technical-debt-ml-sculley-2015]] — ML 系统隐藏技术债务（Sculley et al., Google, NeurIPS 2015）
- [[wiki/sources/mlops-google-cloud-cicd-ct-pipelines]] — Google Cloud MLOps 三层成熟度模型
