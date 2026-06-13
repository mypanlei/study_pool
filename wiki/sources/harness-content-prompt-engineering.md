---
title: "Harness Engineering、Content Engineering 与 Prompt Engineering 的区别与联系"
tags:
  - source
  - harness
  - methodology
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://www.anthropic.com/engineering/building-effective-agents"
source_author: "自建知识库笔记"
source_date: 2026-06-04
---

# Harness Engineering、Content Engineering 与 Prompt Engineering 的区别与联系

> Prompt 决定表达方式，Content 决定知识底座，Harness 决定执行系统。三者是生产级 AI 系统的三层分工，不是前后淘汰关系。

## 核心论点

1. **Prompt Engineering** — 工程化设计「给模型下什么指令」，核心对象是模型输入中的指令层。典型工作：system prompt、few-shot、输出 schema。
2. **Content Engineering** — 工程化设计「给模型喂什么内容」，核心对象是知识和上下文资产。典型工作：文档切分、RAG 策略、知识库治理、长期记忆管理。
3. **Harness Engineering** — 工程化设计「模型在怎样的运行时里完成任务」，核心对象是执行运行时。典型工作：Agent 循环编排、工具接口、权限审批、评测审计。
4. **系统越复杂，关注点越外扩** — 单轮轻任务 Prompt 就够；知识密集型靠 Content；多步骤 Agent 系统 Harness 最重要。Prompt 不会消失，只是不再是唯一抓手。

## 分层关系

- Content Engineering → 可检索、可组合、可追溯的上下文
- Prompt Engineering → 指令、约束、示例、输出格式
- Harness Engineering → 模型、工具、记忆、护栏、校验装配成可执行闭环

## 受影响的 Wiki 页面

- [[wiki/concepts/harness-engineering]] — 已创建
- [[wiki/concepts/agent-skills-system]] — 已关联
