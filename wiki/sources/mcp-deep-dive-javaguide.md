---
title: "MCP（Model Context Protocol）深度解析：协议、架构与生产落地 — JavaGuide"
tags:
  - source
  - mcp
  - function-calling
  - agent
  - javaguide
created: 2026-06-19
updated: 2026-06-19
source: "https://javaguide.cn/ai/agent/mcp.html"
author: "Guide (JavaGuide)"
---

# MCP（Model Context Protocol）深度解析：协议、架构与生产落地 — JavaGuide

> 从"工具接入的重复适配问题"切入，系统讲解 MCP 的核心概念、四层分层架构、JSON-RPC 2.0 通信机制及生产级 MCP Server 开发实践。文章重点区别于"介绍 MCP 是什么"的教程，重点阐述了 MCP、Function Calling、Agent 三者的分层关系，MCP 的 Resources/Tools/Prompts 三种能力模型，以及企业落地前必须解决的 Schema 管理、权限安全、可观测性、成本归因等工程问题。最后给出了使用 FastMCP 的最小示例和本地调试方法。

## Core Contributions

1. **FC/MCP/Agent 三层关系**：Function Calling 解决"模型怎么表达自己想调工具"（输出结构化调用意图），MCP 解决"工具从哪里来、怎么被宿主发现、怎么连到后端服务"（协议层），Agent 解决"任务怎么一步步做完"（规划层）。三者不是并列关系，而是不同层级的组件。场景判断表：简单意图判断用 FC，宿主资源连接用 MCP，多步决策用 Agent。

2. **MCP 四层架构详解**：Host（AI 应用本身，用户直接面对）→ Client（Host 内负责通信的层，一个 Server 对应一个 Client）→ Server（暴露具体能力的服务端，开发者最常接触）→ Data Source（Server 背后的真实数据来源，不属于协议核心角色但必不可少）。分层意义：AI 应用只认 MCP，底层怎么查数据库、调 API 由 Server 自己处理。

3. **Server 侧三类能力**：Resources（只读上下文，供模型阅读理解）、Tools（可执行动作，能主动执行逻辑或改变外部世界）、Prompts（可复用提示词模板）。用生活例子（做凉拌黄瓜）生动解释了三类能力的区别。明确建议：大多数 Server 一开始只提供 Tools 就够了。

4. **Client 侧三类能力**：Roots（Host 告诉 Server 的工作范围边界）、Sampling（Server 请求 Host 侧 LLM 做辅助生成）、Elicitation（Server 向用户补充询问信息的能力）。提醒"不要硬凑"，要看 Client 是否支持。

5. **JSON-RPC 2.0 通信机制**：选择 JSON-RPC 而非 REST 的原因（AI 工具调用天然是"执行方法"而非操作资源）。给出 tools/call 请求与响应的完整 JSON 示例，强调成功响应不要同时写 result 和 error。指出 JSON-RPC 的局限（不像 gRPC 有强 IDL 和编译期类型约束）。

6. **传输方式对比**：stdio（本地开发，Host 将 Server 当子进程启动，通过 stdin/stdout 通信，简单但权限边界需自管）vs Streamable HTTP（远程部署，统一端点，认证/负载均衡/网关更接近普通 HTTP 服务）。关键提醒：stdio 模式不要往 stdout 打调试日志，否则污染消息流。

7. **生产落地六大问题**：(1) 类型和 Schema 要管住（JSON Schema 不等于强类型，字段单位/时间格式/枚举要写清楚），(2) 可观测性要补上（Trace ID、结构化日志、调用链），(3) 权限不能只靠用户同意（文件/数据库/API 要有边界，写操作要二次确认），(4) 工具描述本身也要审核（防提示词注入），(5) 成本要能归因（Token/API/云资源按业务线拆分），(6) 版本管理不能靠口头约定（工具级版本、灰度、兼容性测试）。

8. **企业落地检查清单**：五大维度（Schema 和版本、权限和安全、可观测性、成本归因、依赖治理）共 25+ 条检查项。

9. **MCP Server 开发最佳实践**：工具要拆小（`get_user_by_id` 而非 `execute_sql`），名字用动词+名词，description 写清楚"什么时候用、需要哪些参数、什么时候不要用"。大文件处理三层次（元数据→分块读取→硬限制）。安全问题（路径遍历/SQL 注入/数据脱敏/资源滥用）。

10. **最小示例与调试**：使用 FastMCP（Python SDK）的 weather-server 完整代码，Claude Desktop 配置方法，MCP Inspector 本地调试命令。强调生产环境用 uv run 显式声明依赖而非全局 python。

## Key Insights

- "MCP 先解决工具接入这块的重复适配问题" — 不是让模型变聪明，也不是替代 Function Calling
- "让工具开发和 Agent 开发解耦" — 工具团队负责能力封成 Server，Agent 团队负责任务组织和用户交互
- "MCP Server 不是能跑就行。你要把能力描述成模型看得懂、选得准、用得安全的形式"
- "工具名不清楚、参数描述模糊、返回结构不稳定，都会让 Agent 做出奇怪选择"
- "Demo 阶段这样挺好。问题是一到生产，麻烦就会出来" — 生产落地六大问题
- "AI 应用再新，鉴权、审计、日志、版本、限流这些基本功也绕不过去"
- "MCP 做的事就是把'各自适配'变成'统一接口'"

## Related Pages

- [[wiki/concepts/mcp-model-context-protocol]] — MCP 协议概念页（本来源将显著增强该页面）
- [[wiki/concepts/a2a-agent-to-agent-protocol]] — A2A 协议，MCP 的互补协议
- [[wiki/concepts/agent-skills-system]] — Agent Skills（指令层）与 MCP（连接层）对比
- [[wiki/concepts/react-reasoning-acting]] — ReAct 模式，Agent 核心推理循环
- [[wiki/sources/structured-output-function-calling-javaguide]] — 同系列文章，结构化输出与 Function Calling
- [[wiki/sources/agent-core-concepts-javaguide]] — JavaGuide Agent 核心概念全景
- [[wiki/sources/harness-engineering-javaguide]] — JavaGuide Harness Engineering
