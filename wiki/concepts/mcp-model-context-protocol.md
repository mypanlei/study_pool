---
title: "MCP (Model Context Protocol)"
tags:
  - concept
  - mcp
  - protocol
  - anthropic
  - tool-use
  - agent
created: 2026-06-18
updated: 2026-06-19
aliases:
  - Model Context Protocol
  - MCP 协议
  - MCP Server
  - MCP Client
  - Model Context Protocol
---

# MCP (Model Context Protocol)

## 定义

MCP（Model Context Protocol）是 Anthropic 推出的开放协议，旨在为 AI 应用提供标准化的外部工具和数据接入方式。MCP 采用 **Host ↔ Client ↔ Server ↔ Data Source** 四层架构，本质是定义 AI 应用与外部资源之间的"接线规范"：**外部系统把能力封装成 MCP Server，支持 MCP 的 AI 应用连接上来之后，就能发现这些能力并调用。**

MCP 不是让模型变聪明，不是替代 Function Calling，也不是新一代 Agent 框架。它解决的核心问题是 **工具接入的重复适配问题**——让工具开发和 Agent 开发解耦。

## FC / MCP / Agent 三层关系

MCP、Function Calling、Agent 经常一起出现，但不在同一层：

| 层次 | 解决的问题 | 类比 |
|------|-----------|------|
| **Function Calling** | 模型怎么表达自己想调工具（输出结构化调用意图如 `{"name":"read_file","arguments":{...}}`） | 模型的"表达层" |
| **MCP** | 工具从哪里来、怎么被宿主发现、怎么真正连到后端服务 | 协议/连接层 |
| **Agent** | 任务怎么一步步做完（规划步骤、调用工具、读取结果、继续判断） | 规划/执行层 |

### 场景判断

| 场景 | 更关键的东西 | 原因 |
|------|-------------|------|
| 让模型判断要不要查天气 | Function Calling | 重点是模型把意图转成结构化参数 |
| 让 Claude Desktop 读取本地文件 | MCP | 重点是宿主和本地文件系统之间有标准接口 |
| 让 AI 自动排查线上故障 | Agent | 重点是多步决策、工具调用和结果反馈 |

> 三者经常一起用，只是各自负责的层级不同。Function Calling 是模型侧工具调用意图生成机制，MCP 是工具接入标准化协议，Agent 负责上层任务编排。

## 四层架构

```
Host (AI 应用：Claude Desktop / Cursor / VS Code)
  │
  ├── Client ── MCP Server A ── Data Source (本地文件系统)
  │
  └── Client ── MCP Server B ── Data Source (数据库 / GitHub API / 内部平台)
```

| 角色 | 描述 | 示例 |
|------|------|------|
| **Host** | 用户直接面对的 AI 应用 | Claude Desktop、Cursor、VS Code AI 插件、自定义 Agent |
| **Client** | Host 内部负责和 MCP Server 通信的层（一个 Server 对应一个 Client 会话） | 通常不需要自己写，由 SDK 或应用提供 |
| **Server** | 暴露具体能力的服务端（开发者最常接触的部分） | 文件系统 Server、GitHub Server、SQL 查询 Server |
| **Data Source** | Server 背后真实访问的数据和能力（不属于协议核心角色） | 本地文件、数据库、第三方 API、内部工单系统 |

**核心价值**：Host 不直接"裸连"所有工具。它先通过 Client 连到 Server，Server 再去碰真实数据源。这个分层让边界清楚很多——AI 应用只认 MCP，底层具体怎么查数据库、怎么调 API，由 Server 自己处理。**让工具开发和 Agent 开发解耦。**

## Server 侧能力

MCP Server 可以暴露三类能力：

### Resources（只读上下文）
供模型阅读理解，不执行写操作。例如：本地文件、日志片段、数据库 Schema、配置记录。

### Tools（可执行动作）
会主动执行逻辑或可能改变外部世界。例如：查询数据库、发送消息、创建工单、调用业务接口。

### Prompts（可复用提示词模板）
固定任务的提示词模板。例如："按团队规范做代码审查"、"生成故障复盘初稿"。

> 大多数 MCP Server 一开始只提供 Tools 就够了。Resources 和 Prompts 在有明确需求后再添加。

### 生活类比
> 用户说："我想吃凉拌黄瓜。"
> - **Resources**：冰箱里有什么、家里有没有黄瓜、调料放在哪里
> - **Tools**：切菜、拌料、开火、下单买菜
> - **Prompts**：家里固定的口味偏好（少放辣、必须放香菜）

## Client 侧能力

| 能力 | 描述 |
|------|------|
| **Roots** | Host 通过 Client 告诉 Server 的工作范围边界（如"只允许访问当前项目目录"） |
| **Sampling** | Server 请求 Host 侧的 LLM 做辅助生成（如读取日志后让模型做摘要） |
| **Elicitation** | Server 在执行过程中向用户补充询问信息（参数不完整、选项有歧义、执行前需要确认） |

> 这些能力不要硬凑。Roots/Sampling/Elicitation 要看对应 Client 是否支持，也要看业务场景是否真的用得上。

## 通信：JSON-RPC 2.0

MCP 底层使用 JSON-RPC 2.0，而非 REST。

- **REST** 偏资源操作（`/users/1`、`/orders/100`）
- **JSON-RPC** 偏方法调用（`tools/call`、`resources/read`）
- AI 工具调用天然是"我要执行某个动作"，JSON-RPC 更贴切

工具调用请求示例：
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "read_file",
    "arguments": { "path": "/path/to/file.txt" }
  },
  "id": 1
}
```

成功响应：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [{ "type": "text", "text": "文件内容..." }]
  }
}
```

失败响应：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": { "code": -32602, "message": "Invalid params" }
}
```

> ⚠️ 成功响应里不要同时写 `result` 和 `error: null`。JSON-RPC 2.0 里两者互斥。

**JSON-RPC 的优点**：轻量、纯文本、容易打日志，不强制绑定某种传输方式。

**局限**：不像 gRPC 有强 IDL 和编译期类型约束。MCP 用 JSON Schema 描述工具参数，但这是运行时校验和模型提示层面的约束，Server 侧仍需做严格参数校验。

## 传输方式

### stdio（本地开发）
Host 将 MCP Server 当成本地子进程启动，通过 stdin/stdout 通信。Claude Desktop 多数本地 Server 使用此方式。

**优点**：简单，几乎没有网络部署成本。
**缺点**：Server 跑在本机，权限边界要自己管好。

**重要提醒**：⚠️ 不要往 stdout 打调试日志。stdout 是 JSON-RPC 消息通道，随手 `print()` 会污染消息流导致 Server 断连。日志请写到 stderr 或文件。

### Streamable HTTP（远程部署）
MCP 早期用 HTTP+SSE，2025-03-26 升级为 Streamable HTTP，通信收敛到统一端点。

**优点**：认证、负载均衡、网关接入更接近普通 HTTP 服务。

### 选型建议

- 本地工具、本地文件、个人使用 → **stdio**
- 团队服务、远程 API、多用户访问 → **Streamable HTTP**
- 涉及写操作和敏感数据 → 不管哪种传输都要额外做鉴权和审计

## 一次 MCP 调用的完整流程

1. 用户提问后，模型判断缺少外部信息，生成工具调用意图（Function Calling）
2. Host 将调用交给 MCP Client
3. Client 发送 `initialize` 请求（含协议版本和能力列表）→ Server 返回支持版本和能力 → Client 发 `initialized` 通知
4. Client 通过 JSON-RPC 请求 MCP Server 执行工具
5. Server 查询真实 Data Source（文件/数据库/API）
6. 结果一路返回给模型
7. 模型组织成最终回答给用户

> 初始化握手阶段很关键。很多"Server 配好了但工具没出现"的问题，排查时都应先看初始化阶段有没有失败。

## 生产落地六大问题

1. **类型和 Schema 要管住** — JSON Schema 不等于强类型。字段单位、时间格式、枚举值、默认值、分页参数都需要明确标注。Server 侧做强校验，错误信息要能让模型看懂。

2. **可观测性要补上** — 一次回答可能调用多个 Server 和工具。需要 Trace ID、结构化日志、调用链记录。否则线上出错了只能人肉拼调用链。

3. **权限不能只靠用户同意** — 文件能读哪些目录，SQL 能查哪些表，API 能不能写生产数据。写操作默认保守，做二次确认、审计和回滚预案。

4. **工具描述也要审核** — 恶意或粗糙的 Server 可能在 description/Prompt 模板里夹带提示词注入。企业需要审核 Server 来源和工具描述。

5. **成本要能归因** — Token 成本、API 成本、云资源成本要能按用户、业务线、工具、会话追踪。否则账单来了只知道总数变高。

6. **版本管理不能靠口头约定** — 工具接口一改，Agent 就可能出错。字段改名、枚举值变化、返回结构调整都影响模型判断。工具级版本管理、灰度、兼容性测试都需要。

## MCP Server 开发最佳实践

### 工具设计原则
- 工具要拆小（`get_user_by_id` 而非 `execute_sql(id, table)`）
- 名字用**动词+名词**（`list_active_orders`、`read_file`）
- description 写清楚三件事：什么时候用、需要哪些参数、什么时候**不要**用
- 在 description 里明确**禁用场景**（"如果用户问的是网络或内存问题，不要调用此工具"）

### 大文件处理
1. 先返回元数据（文件名、大小、更新时间、摘要）
2. 分块读取（单块控制 100KB 以内）
3. 设置硬限制（超过 10MB 只返回说明和可选读取方式）

### 安全红线
- 文件读取：防路径遍历（`../` 逃逸）
- SQL 查询：参数化，不让模型拼字符串
- 数据脱敏：手机号、邮箱、Token、密钥、内部链接
- 写操作限权：删除/修改/发送/调用生产接口 → 人工确认
- 资源滥用限速：Server 侧做限速、超时、熔断和配额

## 最小示例

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool()
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    return f"{city} 今天晴天，温度 25°C"

@mcp.resource("weather://forecast")
def weather_forecast() -> str:
    """返回未来一周天气预报"""
    return "未来七天天气预报..."

if __name__ == "__main__":
    mcp.run()
```

Claude Desktop 配置：
```json
{
  "mcpServers": {
    "weather-server": {
      "command": "uv",
      "args": ["run", "--with", "mcp", "/path/to/weather_server.py"]
    }
  }
}
```

本地调试用 MCP Inspector：
```bash
# Python Server
npx @modelcontextprotocol/inspector uv run --with mcp /path/to/weather_server.py
```

## MCP vs 相关概念

### MCP vs A2A

| 维度 | MCP | A2A |
|------|-----|-----|
| 解决问题 | Agent ↔ Tool 连接（垂直集成） | Agent ↔ Agent 通信（水平互联） |
| 类比 | USB（设备连接） | HTTP（Web 通信） |
| Agent 模型 | Agent 主动调用外部工具 | Agent 之间以黑盒方式协作 |
| 发起方 | Host 应用决定调用 | Client Agent 发起任务请求 |

### MCP vs Agent Skills

| 维度 | MCP | Agent Skills |
|------|-----|--------------|
| 关注点 | **连接** — 如何访问数据和 API | **逻辑** — 如何按流程执行任务 |
| 本质 | 协议层（传输） | 指令层（知识） |
| 是否需要后端 | 需要编码配置和 Server 运行 | 不需要后端，纯文本指令 |
| 复用方式 | HTTP/stdio 连接 | 文件复制 + 加载 |

### MCP vs Function Calling

| 维度 | MCP | Function Calling |
|------|-----|-----------------|
| 关注点 | 工具发现、连接和执行 | 模型输出结构化调用意图 |
| 归属 | 协议层（MCP Client ↔ Server） | 模型层（LLM 输出层） |
| 是否模型相关 | 与模型无关 | 强依赖模型能力 |

## 相关概念

- [[wiki/concepts/a2a-agent-to-agent-protocol]] — A2A（Agent 间通信）与 MCP 互补
- [[wiki/concepts/agent-skills-system]] — Agent Skills（指令层）与 MCP（连接层）对比
- [[wiki/concepts/harness-engineering]] — Harness 工程中工具的集成和管理
- [[wiki/concepts/react-reasoning-acting]] — ReAct 模式，Agent 与工具交互的核心循环
- [[wiki/concepts/prompt-engineering]] — Prompt Engineering，与 MCP Prompts 的关系
- [[wiki/concepts/guardrails]] — Agent 安全护栏，MCP Server 安全设计相关
- [[wiki/entities/anthropic]] — Anthropic 公司，MCP 协议的提出者

## 来源

- [[wiki/sources/mcp-deep-dive-javaguide]] — JavaGuide MCP 深度解析（主要来源，本文核心内容基于此文）
- [[wiki/sources/llm-skills-technical-guide]] — LLM Skills 技术全景指南，含 MCP 协议详解
- [[wiki/sources/ai-agent-tools-integration]] — 菜鸟教程 Agent 工具集成，含 MCP 实现
- [[wiki/sources/skills-tutorial]] — Skills 教程，MCP vs Skills 对比
- [[wiki/sources/multi-agent-system]] — A2A vs MCP 对比框架
- [[wiki/sources/ai-agent-glossary]] — Agent 术语词典含 MCP 定义
- [[wiki/sources/agent-core-concepts-javaguide]] — JavaGuide Agent 核心概念，含 MCP 与 Function Calling 详解
- [[wiki/sources/agent-skills-deep-dive-javaguide]] — JavaGuide Skills 深度解析，含 Skills vs MCP 对比
- [[wiki/sources/structured-output-function-calling-javaguide]] — 同系列文章，Function Calling 七步流水线
