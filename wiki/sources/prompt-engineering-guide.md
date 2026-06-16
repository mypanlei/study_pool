---
title: "提示词工程（Prompt Engineering） — 菜鸟教程"
tags:
  - source
  - prompt-engineering
  - llm
  - tutorial
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/prompt-engineering.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# 提示词工程（Prompt Engineering）

> 全面的提示词工程教程，从基础到进阶涵盖清晰指令、角色设定、XML 标签、输出格式控制、思维链、少样本学习、防幻觉设计、提示词链和元提示等十大技巧。

## 核心内容

1. **三大消息角色** — System（幕后导演）、User（演员搭档）、Assistant（AI 演员）。
2. **Token 与上下文窗口** — Token 概念、Lost in the Middle 现象、关键信息放开头或结尾。
3. **十大技巧** — 清晰指令、角色设定、XML 标签分离数据与指令、输出格式控制（模板+预填充）、思维链（CoT）、少样本学习（Few-shot）、防幻觉（五策略）、提示词链（Prompt Chaining）、元提示（Meta-Prompting）、五段式架构。
4. **迭代优化工作流** — 写→测试→分析→修改→再测试的循环迭代。
5. **四要素框架速查表** — 角色 + 指令 + 背景 + 限制。

## 关键概念

- 提示词工程 = 降低模糊性，提升与 AI 的对齐度
- CoT 让 AI 先写草稿再给结论，准确率显著提升
- 元提示让 AI 帮你写或改进提示词
- 防幻觉最有效的策略：明确允许 AI 说"我不知道"
