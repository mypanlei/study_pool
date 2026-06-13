---
title: "DeepSeek-R1 全深度解析"
tags:
  - source
  - deepseek
  - rl
  - grpo
  - distillation
  - chain-of-thought
created: 2026-06-13
updated: 2026-06-13
aliases:
  - DeepSeek-R1 深度解析
---

# DeepSeek-R1 全深度解析：从 Zero 到 Distill

> 本文从 R1-Zero 与 R1 的体系架构对比出发，深入解析 GRPO 算法原理、四阶段训练流程以及蒸馏模型的行业影响。

## 核心贡献

1. **R1-Zero vs R1 路径对比**：
   - R1-Zero：纯 RL 路径，在 Base 模型上直接大规模强化学习，涌现"自我反思"能力（如自发纠正计算错误），但可读性差、语言一致性弱。
   - R1：复合路径，冷启动 SFT + 多阶段 RL，在保持顶尖逻辑能力的同时解决语言混乱问题。
2. **GRPO 群组相对策略优化**：生成一组候选答案 → 计算平均奖励 → 加强高于平均值的路径、削弱低于平均值的路径。无需独立的 Value 网络，显存开销极低。
3. **蒸馏模型影响力**：开源 R1-Distill-Qwen-7B/32B、R1-Distill-Llama-70B，实现"小模型也能拥有复杂推理能力"。

## 关联页面

- [[wiki/entities/deepseek]] — DeepSeek AI 公司实体
- [[wiki/syntheses/deepseek-technical-analysis]] — DeepSeek 技术综合分析

## 参考链接

- [DeepSeek-R1 官方仓库](https://github.com/deepseek-ai/DeepSeek-R1)
- [DeepSeek-R1 论文](https://arxiv.org/abs/2501.12948)
