---
title: "MoE (Mixture of Experts) — 专家混合"
tags:
  - concept
  - architecture
  - llm
  - efficiency
created: 2026-06-17
updated: 2026-06-17
aliases:
  - 专家混合
  - Mixture of Experts
  - MoE 架构
---

# MoE（专家混合架构）

> 一种将模型拆分为多个「专家」子网络的架构，每个 Token 只激活部分专家。DeepSeek-V3/R1、Mixtral 等模型的核心架构技术。

## 核心思想

- 总参数量大（如 DeepSeek-V3 的 671B），但每个 Token 只激活一小部分（如 37B）
- 通过 Router（路由网络）决定每个 Token 分配给哪些专家
- 大幅降低训练和推理成本

## 关键概念

| 概念 | 说明 |
|------|------|
| **Expert** | 专门的子网络，负责处理特定类型的输入 |
| **Router** | 门控网络，决定 Token 路由到哪些专家 |
| **Top-k Routing** | 只激活得分最高的 k 个专家 |
| **Load Balancing** | 防止所有 Token 都涌向同一专家 |
| **Fine-grained MoE** | DeepSeek-V4 的细粒度专家拆分 |

## 优势与挑战

- ✅ 同等算力下获得更大模型容量
- ✅ 推理速度快于同等质量的密集模型
- ❌ 显存占用高（需加载所有专家参数）
- ❌ 路由负载均衡需要精细调优

## 来源

- [[wiki/sources/deepseek-r1-technical-secrets]]
- [[wiki/sources/deepseek-v4-technical-analysis]]
