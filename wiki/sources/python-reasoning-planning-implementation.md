---
title: "Python 实现推理与规划 — 菜鸟教程"
tags:
  - source
  - python
  - reasoning
  - planning
  - react
  - cot
  - mcts
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/python-reasoning-planning.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Python 实现推理与规划

> Python 实现 AI Agent 核心推理与规划能力的教程，涵盖 ReAct 框架、Chain of Thought（思维链）、Tree of Thoughts（思维树）、MCTS（蒙特卡洛树搜索）、Reflexion（自我反思）、任务分解策略、Plan-and-Execute 模式。

## 核心内容

1. **ReAct 框架** — 推理→行动→观察循环，Agent 交替推理和行动形成闭环，模拟人类问题解决过程。
2. **思维链 (CoT)** — Zero-shot CoT（"让我们一步一步地思考"）和 Few-shot CoT（含推理过程的示例），可追溯性和准确性提升。
3. **思维树 (ToT)** — 在每个推理节点探索多条路径，形成树状结构，支持多路径探索和回溯评估。
4. **MCTS 规划** — 选择→扩展→模拟→反向传播四步循环，适合复杂决策和游戏 AI 规划。
5. **Reflexion 自我反思** — 执行→评审→反思→重试循环，让 Agent 从失败中学习和改进。
6. **任务分解策略** — 递归分解（逐层拆解到可执行）、平行分解（并行独立子任务）、层次分解（多层抽象）。
7. **Plan-and-Execute** — 先完整规划再按计划执行，与 ReAct（边推理边执行）形成互补。

## 关键概念

- ReAct 灵活但路径不稳定，Plan-and-Execute 稳定但缺乏动态调整能力
- CoT 线性推理 vs ToT 空间推理（多路径探索）
- Reflexion 引入"制作者-评审者"分离架构，评审器评估结果并生成反思
