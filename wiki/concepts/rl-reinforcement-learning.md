---
title: "RL (Reinforcement Learning) — 强化学习"
tags:
  - concept
  - rl
  - training
  - alignment
created: 2026-06-17
updated: 2026-06-17
aliases:
  - 强化学习
  - Reinforcement Learning
  - RLHF
---

# RL（强化学习）

> 强化学习是 LLM 后期训练的核心范式。模型通过在与环境交互中获得奖励信号来学习最优策略，是 DeepSeek-R1 中 GRPO、ChatGPT 中 RLHF 的基础。

## 在 LLM 中的作用

| 方法 | 全称 | 应用 |
|------|------|------|
| **RLHF** | Reinforcement Learning from Human Feedback | ChatGPT/Claude 的对齐训练 |
| **GRPO** | Group Relative Policy Optimization | DeepSeek-R1 核心算法 |
| **PPO** | Proximal Policy Optimization | RLHF 的常用算法 |
| **DPO** | Direct Preference Optimization | RLHF 的简化替代 |

## 核心概念

- **Agent**: 执行策略的模型
- **Environment**: Agent 交互的环境
- **Reward Model**: 评估输出质量的评分模型
- **Policy**: Agent 的行为策略
- **Value Function**: 状态或动作的预期回报估计

## 来源

- [[wiki/sources/deepseek-r1-technical-secrets]]
- [[wiki/sources/deepseek-r1-deep-analysis]]
- 知识库内 87 处引用
