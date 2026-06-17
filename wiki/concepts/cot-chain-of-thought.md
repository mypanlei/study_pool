---
title: "Chain of Thought (CoT / 思维链)"
tags:
  - concept
  - cot
  - reasoning
  - prompting
  - technique
created: 2026-06-18
updated: 2026-06-18
aliases:
  - 思维链
  - Chain of Thought
  - CoT
  - 思维链推理
  - 逐步推理
---

# Chain of Thought (CoT / 思维链)

## 定义

Chain of Thought（思维链，简称 CoT）是一种引导 LLM 进行**逐步推理**的提示技术。通过在 Prompt 中加入"让我们一步一步思考"或提供推理步骤示例，让模型在给出最终答案之前先生成中间推理步骤。CoT 能显著提升 LLM 在数学、逻辑、常识推理等需要多步推导的任务上的准确率。

CoT 与 ReAct 的区别在于：**CoT 只在"头脑中"推理**（纯文本空间），而 **ReAct 在推理中穿插工具调用**（与外部世界交互）。

## 核心要点

- **逐步推理**：引导模型先写草稿再给结论，而非直接跳到答案
- **Zero-shot CoT**：简单添加"Let's think step by step"即可触发（Kojima et al., 2022）
- **Few-shot CoT**：提供带推理步骤的示例，模型模仿示例的推理格式
- **自洽性 (Self-Consistency)**：多次采样取多数答案，可进一步提升准确率
- **与 ReAct 的关系**：ReAct = CoT + Tool Use，CoT 是"思考"部分，ReAct 是"思考 + 行动"循环

## 详细阐述

### 背景

标准 prompting 下，LLM 倾向于直接从问题跳到答案（"跳跃式推理"），这在简单任务中效率高，但在复杂推理任务中容易出错。CoT 通过显式输出中间推理步骤，让模型的"思考过程"可追踪、可验证。

### CoT 方法对比

| 方法 | 描述 | 适用场景 |
|------|------|----------|
| **Zero-shot CoT** | Prompt 尾部加 "Let's think step by step" | 简单推理，无需示例 |
| **Few-shot CoT** | 提供含推理链的示例 | 复杂推理，需匹配输出格式 |
| **自洽性 CoT** | 多次推理 + 多数投票 | 高精度要求的场景 |
| **结构化 CoT** | 用 XML/JSON 标记推理步骤 | 需要结构化输出的场景 |

### CoT vs 其他推理方法

| 维度 | CoT | ReAct | Plan & Execute | ToT |
|------|-----|-------|----------------|-----|
| 是否调用工具 | ❌ | ✅ | ✅ | ❌ |
| 推理路径 | 单条链 | 交互式循环 | 预规划→执行 | 多路径树状 |
| 自我修正 | 有限的 | 通过观察反馈 | 通过重新规划 | 通过路径剪枝 |
| 上下文消耗 | 低 | 高（容易膨胀） | 中 | 高 |

### 典型应用

- **数学问题**：逐步计算，减少计算错误
- **逻辑推理**：显式列出前提和推论，避免跳跃
- **代码生成**：先描述算法思路，再生成代码
- **Agent 规划**：在 ReAct 循环中，CoT 为 Thought 步骤提供推理基础
- **DeepSeek-R1**：通过 GRPO 训练让模型自主学习 CoT 推理，产生可见的"思考"过程

## 相关概念

- [[wiki/concepts/react-reasoning-acting]] — ReAct 在 CoT 基础上增加工具调用，CoT 是 ReAct 的"思考"组件
- [[wiki/concepts/prompt-engineering]] — CoT 是 Prompt Engineering 中最有效的单一技术之一
- [[wiki/concepts/rl-reinforcement-learning]] — DeepSeek-R1 用 GRPO 训练模型学习 CoT 推理

## 来源

- [[wiki/sources/reasoning-and-planning]] — 菜鸟教程推理框架对比，含 CoT/ReAct/ToT/MCTS
- [[wiki/sources/prompt-engineering-guide]] — 菜鸟教程 Prompt Engineering 十大技术，CoT 是核心
- [[wiki/sources/python-reasoning-planning-implementation]] — CoT Python 实现代码
- [[wiki/sources/deepseek-r1-technical-secrets]] — DeepSeek-R1 中的 CoT 推理训练
