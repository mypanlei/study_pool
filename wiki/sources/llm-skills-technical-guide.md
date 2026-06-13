---
title: "LLM Skills 技术全景指南 — Tool Use、MCP 与 Agent Skills 架构"
tags:
  - source
  - skills
  - mcp
  - function-calling
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://modelcontextprotocol.io"
source_author: "自建知识库笔记"
source_date: 2026-02-28
---

# LLM Skills 技术全景指南

> LLM Skills（Tool Use / Function Calling）是构建 AI Agent 的基石。LLM 的角色是「智能调度员」，而非执行者。

## 核心论点

1. **调度员模式** — LLM 接收工具列表 + 问题 → 决定调用工具（JSON）→ 宿主应用实际执行 → 返回结果给 LLM → 生成最终回答。
2. **MCP 协议** — Anthropic 推出的工具标准化协议，分 Host（宿主）、Client（客户端）、Server（服务端）三层，解决如何访问私有数据和 API。
3. **Agent Skills（agentskills.io）** — 与 MCP 不同，关注「如何按特定标准和流程执行任务」，采用三级渐进披露机制：Metadata（始终加载）→ Instructions（按需加载）→ Scripts/Resources（运行时加载）。
4. **MCP vs Agent Skills** — MCP 关注「连接」；Agent Skills 关注「逻辑」。
5. **生产最佳实践** — 工具描述中写调用建议和错误处理示例、安全沙箱隔离执行、Token 优化（摘要后再喂给模型）、写操作幂等性。

## 受影响的 Wiki 页面

- [[wiki/concepts/agent-skills-system]] — 已更新
