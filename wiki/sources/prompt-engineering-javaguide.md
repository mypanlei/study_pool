---
title: "Prompt Engineering 深度解析 — JavaGuide"
tags:
  - source
  - prompt-engineering
  - javaguide
  - llm
  - enterprise-security
created: 2026-06-19
updated: 2026-06-19
source_url: "https://javaguide.cn/ai/agent/prompt-engineering.html"
source_author: "JavaGuide (Guide)"
source_date: 2026-06-16
---

# Prompt Engineering 深度解析

> JavaGuide 出品的 Prompt Engineering 深度文章，涵盖四要素框架（Role/Task/Context/Format）、六大核心技巧（角色扮演/思维链/少样本学习/任务分解/结构化输出/XML 标签与预填充）、高级工程技巧及企业级安全实践。本文在 Prompt Engineering 的理论体系上与菜鸟教程一致，但在企业安全实践和实时数据注入方面有独特的补充。

## 核心论点

1. **Prompt 四要素框架** — 角色(Role) + 任务(Task) + 上下文(Context) + 格式(Format)，缺一不可
2. **企业级安全四道防线** — 输入验证与清洗、Prompt 注入检测、权限最小化（System Prompt 隔离）、输出过滤与审计
3. **Agent 场景中 Prompt 与 Context Engineering 的界限** — Prompt Engineering 偏提示词本身，Context Engineering 管理更宽的上下文（规则/记忆/工具描述/会话状态/Token 预算）

## 核心内容

### 四要素框架

| 要素 | 作用 | 常见表述 |
|------|------|----------|
| Role（角色） | 指定领域知识和语气 | "你是一位 10 年经验的 Java 架构师" |
| Task（任务） | 说明要完成什么动作 | "请评审以下代码的性能问题" |
| Context（上下文） | 补充任务相关背景 | "当前线上 QPS 2000，响应时间超 500ms" |
| Format（格式） | 规定输出格式 | "输出 JSON，包含 bottleneck、solution 两个字段" |

### 六大核心技巧

1. **角色扮演** — 分配专业角色激活特定知识域
2. **思维链 (CoT)** — 引导模型逐步推理，减少跳跃式错误
3. **少样本学习 (Few-shot)** — 提供输入输出示例规范输出
4. **任务分解** — 复杂任务拆成子步骤逐步完成
5. **结构化输出** — 使用 JSON Schema / XML Schema 约束格式
6. **XML 标签与预填充** — 数据与指令分离 + 提前填入示例引导格式

### 企业级安全实践

- 输入验证与清洗（长度/格式/特殊字符）
- Prompt 注入检测（语义分析 + 模式匹配）
- 权限最小化（System Prompt 与 User Prompt 隔离）
- 输出过滤与审计日志

## 与现有知识的关系

- 与 [[wiki/sources/prompt-engineering-guide]]（菜鸟教程）核心内容一致，但本文在企业安全实践方面有独特补充
- 与 [[wiki/concepts/prompt-engineering]] 概念页对应，为其企业安全部分提供了来源依据

## 受影响的 Wiki 页面

- [[wiki/concepts/prompt-engineering]] — 已补充新来源引用
