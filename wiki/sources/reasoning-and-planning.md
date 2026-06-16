---
title: "推理与规划（Reasoning & Planning） — 菜鸟教程"
tags:
  - source
  - reasoning
  - planning
  - react
  - cot
  - mcts
  - reflexion
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/reasoning-planning.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# 推理与规划（Reasoning & Planning）

> 系统介绍 AI Agent 推理与规划的五大框架：思维链（CoT）逐步推理、ReAct 推理+行动循环、Plan-and-Execute 规划先行执行、Tree of Thoughts（ToT）树状多路径探索与 MCTS 蒙特卡洛树搜索、Reflexion 自我反思与纠错，以及任务分解策略和工程化实践。

## 核心内容

1. **思维链（CoT）** — Zero-shot CoT（"Let's think step by step"）和 Few-shot CoT（含推理过程的示例），显著提升数学/逻辑推理准确度。
2. **ReAct 框架** — Thought（思考）→ Action（行动）→ Observation（观察）循环，动态适应环境，但上下文易随步骤累积爆炸。
3. **Plan-and-Execute** — Planner 先拆解子任务列表，Executor 逐个执行（上下文隔离），适合长线复杂任务但面临突发变化不够灵活。
4. **ToT & MCTS** — ToT 将推理建树，节点生成多个候选+评估器打分+搜索算法。MCTS 将 LLM 作为策略网络，通过选择→扩展→模拟→反向传播搜索最优路径。
5. **Reflexion** — 执行→失败→Reviewer 反思→情景记忆→重试闭环，赋予 Agent 自我纠错和持续进化能力。
6. **工程化策略** — 子任务模板化（SOP 状态机）、HITL（人工审批）、RLHF 引导规划。

## 关键概念

- 推理与规划是将 LLM 从"问答机"升级为"自主问题解决者"的核心引擎
- ReAct 灵活但上下文易爆炸，Plan-and-Execute 稳定但缺乏灵活性
- Reflexion 让 Agent 从"写反思"到"改行为"，实现自我进化
