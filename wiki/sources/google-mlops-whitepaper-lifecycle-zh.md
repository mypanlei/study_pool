---
title: "Google MLOps白皮书（上）— MLOps生命周期及核心能力（中文翻译）"
tags:
  - source
  - mlops
  - machine-learning
  - google-cloud
  - whitepaper
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://zhuanlan.zhihu.com/p/557745130"
source_author: "Google (中文翻译: dreaming)"
source_date: 2022-08-25
aliases:
  - Google MLOps White Paper ZH
  - MLOps 实践者指南
---

# Google MLOps白皮书（上）— MLOps生命周期及核心能力

> Google MLOps 白皮书（Practitioners Guide to MLOps）的中文翻译（第一部分）。系统定义了 MLOps 的七阶段生命周期、核心 ML 工程复杂度、以及 11 项技术能力。与 [[wiki/sources/mlops-google-cloud-cicd-ct-pipelines|Google Cloud CI/CD/CT 指南]] 互补：本白皮书定义"做什么"，CI/CD/CT 指南定义"做到什么程度"（成熟度模型）。

## 核心论点

1. **ML 工程的独特复杂性**：与传统软件不同，ML 系统需要准备和维护高质量数据、跟踪生产中模型性能退化、持续实验新算法和超参数、利用新数据持续再训练、避免训练-部署偏差、处理公平性和对抗性攻击。

2. **MLOps 七阶段生命周期**：ML 开发 → 训练操作 → 持续训练 → 模型部署 → 预测服务 → 持续监控 → 数据和模型管理（交叉功能）。

3. **端到端工作流**：ML 开发（实验）→ 训练流程（CI/CD）→ 持续训练（触发器驱动）→ 模型注册（审核/批准/发布）→ 模型部署（在线/批处理/流式）→ 持续监控（数据和概念漂移检测）。

4. **11 项核心技术能力**：
   - **实验**：notebook + Git 集成、实验跟踪、分析和可视化
   - **数据处理**：交互式+生产执行、数据连接器、批处理+流处理
   - **模型训练**：分布式训练、超参数调优、AutoML
   - **模型评估**：批量评分、切片评估、AI 可解释性
   - **模型部署**：在线+离线预测、复合预测例程、推理加速器
   - **在线实验**：金丝雀/影子部署、A/B 测试、MAB 测试
   - **模型监控**：延迟/资源监控、数据偏差检测、概念漂移
   - **ML 流程**：编排/自动化、触发器、本地+云端执行
   - **模型注册**：生命周期管理、审批/发布/回滚、模型卡
   - **数据集和特征库**：共享性/可发现性/版本控制、实时 + 批量
   - **ML 元数据和工件跟踪**：可追溯性和沿袭、参数配置、可视化

5. **三工程领域融合**：数据工程 → ML 工程 → 应用工程。ML 模型是应用系统的组件，需要与应用工程紧密集成。

## 受影响的 Wiki 页面

- [[wiki/concepts/mlops-lifecycle]] — 新增 Google MLOps 白皮书七阶段生命周期视角、11 项技术能力
- [[wiki/syntheses/mlops-ecosystem-overview]] — 可增加 Google MLOps 官方白皮书的生命周期定义
