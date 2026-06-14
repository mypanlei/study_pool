---
title: "Stop Prompting Claude. Use Karpathy's Method Instead."
tags:
  - source
  - karpathy
  - methodology
  - workflow
created: 2026-06-15
updated: 2026-06-15
source_url: "https://www.youtube.com/watch?v=7zZy1QTvokM"
source_author: "Austin Marchese"
source_date: 2026-06-10
---

# Karpathy Method 实操指南：Spec → Verifier → Environment

> Austin Marchese 对 Karpathy AI 方法的实操化拆解：三层架构（Spec × Verifier × Environment），配合具体的 Claude Code 操作提示词。

## 核心论点

### Layer 1: The Spec
- 不要只用 Plan Mode，而要跟 Agent 协作设计**详细规格说明书**
- 三原则：① Interview 模式挖掘真实目标 ② 敏捷式拆解（小范围 + 清晰检查点）③ 精确 + 用脑思考
- Karpathy 原话：*"I don't even like the plan mode. You have to work with your agent to design a spec that is very detailed."*

### Layer 2: The Verifier
- LLM 是"幽灵"不是"动物"——它没有内在动机，你不能靠喊叫或情绪驱动它
- **验证杠杆**是唯一有效的杠杆
- 三步验证：① 预制评估标准 ② 用第二模型做评审（如 Claude Code + Codex 插件）③ 拉取外部信号验证

### Layer 3: The Environment
- CLAUDE.md 是工作坊的"墙壁蓝图"——每次注入自动生效
- LLM Wiki 知识库——"your data is your moat"
- Skills 技能集——反复使用的任务沉淀为 Skill
- 规则护栏：Always Do / Ask First / Never Do 三层

## 个人思考

- 这篇文章本质上是对 [[wiki/concepts/llm-wiki-pattern]] 的实操版解读，从理论到"三层方法论"做了教学化包装
- spec + verifier + environment 的三层与 LLM Wiki 的 raw + wiki + schema 三层有异曲同工之妙
- CLAUDE.md + LLM Wiki + Skills 的组合正是这个知识库正在实践的路径

## 受影响的 Wiki 页面

- [[wiki/concepts/llm-wiki-pattern]] — 已更新
- [[wiki/syntheses/claude-skill-management]] — 已更新
