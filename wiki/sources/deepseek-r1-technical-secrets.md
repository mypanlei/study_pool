---
title: "DeepSeek-R1 技术成功秘诀分析"
tags:
  - source
  - deepseek
  - rl
  - grpo
  - moe
  - distillation
created: 2026-06-13
updated: 2026-06-13
aliases:
  - DeepSeek-R1 技术秘诀
---

# DeepSeek-R1 技术成功秘诀分析

> 本文深入分析了 DeepSeek-R1 成功的五大核心要素：GRPO 算法、多阶段训练流程、MLA+MoE 架构红利、知识蒸馏以及训练成本奇迹。

## 核心贡献

1. **GRPO (Group Relative Policy Optimization)**：去中心化价值模型，取消 PPO 中的 Critic 网络，通过计算一组输出的相对奖励来更新策略，显著降低分布式训练显存压力。
2. **四阶段训练流程**：冷启动 SFT (数千条高质量 CoT) → 推理导向 RL → 拒绝采样再微调 → 全场景 RL（平衡有用性、无害性与推理能力）。
3. **架构红利**：MLA 通过低秩投影减少 KV Cache，提升长文本推理吞吐量；671B MoE 每 Token 仅激活 37B，大幅降低推理成本。
4. **知识蒸馏**：将 671B 模型的推理策略蒸馏到小模型（如 Qwen-32B），达到接近 GPT-4o 水平，证明推理能力可压缩迁移。
5. **成本奇迹**：训练成本仅数百万美元（同行数亿美金），体现极致算力利用率。

## 关联页面

- [[wiki/entities/deepseek]] — DeepSeek AI 公司实体
- [[wiki/syntheses/deepseek-technical-analysis]] — DeepSeek 技术综合分析
- [[wiki/concepts/kv-cache]] — KV Cache 与 MLA 的关系

## 参考链接

- [DeepSeek-R1 Technical Report](https://github.com/deepseek-ai/DeepSeek-R1)
- [GRPO Algorithm Explained](https://arxiv.org/abs/2402.03300)
