---
title: "大模型结构化输出：从 JSON 契约到 Function Calling 落地 — JavaGuide"
tags:
  - source
  - llm
  - structured-output
  - function-calling
  - mcp
  - javaguide
created: 2026-06-19
updated: 2026-06-19
source: "https://javaguide.cn/ai/llm-basis/structured-output-function-calling.html"
author: "Guide (JavaGuide)"
---

# 大模型结构化输出：从 JSON 契约到 Function Calling 落地 — JavaGuide

> 从"请返回 JSON"在生产环境为什么不可靠的五个典型翻车场景出发，系统拆解结构化输出的工程体系。文章清晰界定了 JSON Mode、JSON Schema、Structured Outputs 三个层次的工作边界（语法 vs 契约 vs 生成约束），深入讲解 Function Calling 的完整调用链路（模型只生成调用意图，执行在校验和业务侧），并梳理了 Function Calling、MCP Tool、HTTP API、Agent Skill 的层次关系。最后给出了 Java 后端工具调用的完整代码示例，以及 Schema 设计、失败重试、降级策略和安全治理的工程清单。

## Core Contributions

1. **"请返回 JSON"不可靠的五类翻车场景**：格式漂移（模型加了解释文本）、字段缺失（模型认为某字段不重要就省略）、类型错误（JSON 合法但业务类型不合法）、额外解释文本（模型天然喜欢解释，降低可解析性）、边界条件崩溃（用户输入模糊/矛盾时模型顺着用户走）。

2. **JSON Mode / JSON Schema / Structured Outputs 三层约束模型**：JSON Mode 管语法（输出合法 JSON），JSON Schema 管契约（定义字段/类型/枚举/必填），Structured Outputs 把契约前移到模型生成阶段。关键结论：无论模型侧约束多强，服务端校验都不能省。

3. **Function Calling 调用链路的完整拆解**：7 步工程链路（服务端注册工具定义 -> 用户发起请求 -> 模型选择工具 -> 业务侧校验参数 -> 业务侧执行工具 -> 工具结果回填模型 -> 模型生成最终回答）。核心认知纠正：模型不执行函数，只生成调用意图。

4. **Function Calling / MCP / HTTP API / Agent Skill 的层次关系**：Function Calling 是模型侧工具调用意图生成机制，MCP 是工具接入标准化协议，HTTP API 是业务系统确定性接口，Agent Skill 是上层任务执行说明书。四者不是并列关系，而是不同层的组件。

5. **结构化输出工程落地七要素**：Schema 设计（字段原子化，一个字段只表达一件事）、字段说明要写"何时用"和"何时不用"、枚举优先于自由文本、必填字段谨慎但不要偷懒、版本兼容（Schema 也要有版本号）、校验失败重试（让模型修正具体错误而非全文重跑）、降级策略（可以降级但不能让模型编造业务事实）。

6. **工具调用安全的六层防御体系**：参数校验（结构/业务/权限三层）、风险分层控制、敏感操作二次确认（prepare/confirm 两步）、幂等设计（idempotencyKey + 唯一约束）、全链路审计日志、超时短路（失败后不让模型基于空结果编回答）。

7. **Java 后端工具调用的完整代码示例**：使用 Jackson + JSON Schema Validator 实现工具调用分发器，展示按工具名分发 -> JSON Schema 校验 -> 权限校验 -> 执行工具 -> 全链路审计的标准模式，并给出了 `ToolCall` / `ToolResult` / `QueryOrderArgs` 等 Record 设计。

## Key Insights

- "问题不在于模型'不听话'，而在于我们把**自然语言承诺**错当成了**工程契约**。"
- "结构化输出的本质，是把大模型从'生成给人看的文本'收敛成'生成给程序消费的数据契约'。"
- "Function Calling 不执行函数。模型只生成调用意图，执行、校验、权限和审计都在业务侧。"
- "可读性不是第一目标，可解析性才是第一目标。"
- "字段越原子，后端越容易校验、统计、路由和灰度。"
- "可以降级，但不能让模型编造业务事实。"
- "如果一个工具不能安全重试，它就不应该被 Agent 随意调用。"

## Related Pages

- [[wiki/concepts/mcp-model-context-protocol]] — MCP 协议
- [[wiki/concepts/agent-skills-system]] — Agent Skills
- [[wiki/concepts/prompt-engineering]] — Prompt Engineering
- [[wiki/concepts/harness-engineering]] — Harness Engineering 三层架构
- [[wiki/syntheses/llm-technical-foundations]] — LLM 技术基础
- [[wiki/syntheses/ai-agent-ecosystem-comparison]] — AI Agent 生态
