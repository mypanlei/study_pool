---
title: "Prompt Engineering (提示词工程)"
tags:
  - concept
  - prompt-engineering
  - llm
  - agent
  - technique
created: 2026-06-18
updated: 2026-06-18
aliases:
  - 提示词工程
  - Prompt Engineering
  - Prompt 设计
  - 提示工程
---

# Prompt Engineering (提示词工程)

## 定义

Prompt Engineering（提示词工程）是一门设计和优化输入提示（Prompt）的技术学科，旨在引导 LLM 产生期望的输出。其核心目标是**降低模糊性，提升与 AI 的对齐度**——通过精心设计的指令、格式和上下文，让模型准确理解用户意图并以可靠方式回应。

在 Agent 语境中，Prompt Engineering 是构建 Agent System Prompt 的基础技术，决定了 Agent 的行为边界、决策逻辑和工具使用方式。

## 核心要点

- **三大消息角色**：System（幕后导演，设定全局行为）、User（演员搭档，用户输入）、Assistant（AI 演员，模型回复）
- **降低模糊性**：给 LLM 提供具体、明确、可执行的指令，而非模糊的请求
- **迭代优化**：写→测试→分析→修改→再测试的循环迭代是 Prompt Engineering 的核心工作流
- **性能杠杆**：好的 Prompt 可以显著提升模型表现，是最低成本的效果优化手段
- **四要素框架**：角色 + 指令 + 背景 + 限制

## 详细阐述

### 三大消息角色

| 角色 | 类比 | 作用 |
|------|------|------|
| **System** | 幕后导演 | 设定全局行为规范、角色、约束条件 |
| **User** | 演员搭档 | 用户输入和提问 |
| **Assistant** | AI 演员 | 模型生成的回复 |

### 十大技术

1. **清晰指令** — 使用具体动词（"列出"、"比较"、"解释"），避免模糊表述
2. **角色设定** — 分配专家角色（"你是一名资深数据分析师"）
3. **XML 标签分离** — 用 `<instruction>`、`<data>` 等标签区分指令与数据
4. **输出格式控制** — 使用模板 + 预填充，强制结构化输出（JSON、Markdown 等）
5. **思维链 (CoT)** — 引导模型逐步推理，先写草稿再给结论
6. **少样本学习 (Few-shot)** — 提供 1-3 个输入输出示例作为参考
7. **防幻觉策略** — 明确允许说"不知道"、标注知识截止日期、要求引用来源
8. **提示词链 (Prompt Chaining)** — 将复杂任务拆分为多个连续 Prompt 步骤
9. **元提示 (Meta-Prompting)** — 让 AI 帮你写或改进提示词
10. **五段式架构** — Persona（角色）+ Context（背景）+ Task（任务）+ Format（格式）+ Tone（语气）

### Agent System Prompt 设计

在 Agent 场景中，Prompt Engineering 直接体现为 System Prompt 的设计，需要额外考虑：

- **工具描述** — 清晰描述每个工具的用途、参数、成功/失败场景
- **约束条件** — 安全边界、权限范围、错误处理策略
- **行为规范** — 何时调用工具、何时直接回答、何时请求澄清
- **上下文管理** — 历史压缩、关键信息保留、Budget 控制

### 与相关概念的关系

- **Harness Engineering** 中的 Context Management 是 Prompt Engineering 在 Agent 场景的系统化延伸
- **CoT** 是 Prompt Engineering 中最有效的单一技术之一
- **Agent Skills** 本质上是将 Prompt Engineering 的最佳实践封装为可复用指令

## 相关概念

- [[wiki/concepts/cot-chain-of-thought]] — CoT 是 Prompt Engineering 的核心技术之一
- [[wiki/concepts/harness-engineering]] — Harness 工程中的 Context Management 是 Prompt Engineering 的工程化延伸
- [[wiki/concepts/react-reasoning-acting]] — ReAct System Prompt 设计依赖 Prompt Engineering
- [[wiki/concepts/agent-skills-system]] — Agent Skills 封装了 Prompt Engineering 的最佳实践

## 来源

- [[wiki/sources/prompt-engineering-guide]] — 菜鸟教程 Prompt Engineering 十大技术详解
- [[wiki/sources/harness-content-prompt-engineering]] — Harness/Content/Prompt Engineering 三层分工体系
- [[wiki/sources/ai-agent-glossary]] — Agent 术语定义
- [[wiki/sources/harness-engineering-deep-dive]] — Harness 工程中的 Context 设计
