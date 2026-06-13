---
title: "Pi、Claude Code、Codex 区别与选型指南 — 三种编码 Agent 的运行时与工作流差异"
tags:
  - source
  - pi
  - claude-code
  - codex
  - comparison
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "internal note"
source_author: "自建知识库笔记"
source_date: 2026-06-11
---

# Pi、Claude Code、Codex 区别与选型指南

> Pi 是 agent harness，Claude Code 是 coding agent 平台，Codex 是云端执行系统。三者的核心区别不在模型，而在运行位置、控制权和执行风格。

## 核心论点

1. **Pi** — 开源 coding agent harness/CLI，多 provider，本地控制优先，默认安全边界较弱需自己做 sandbox。更像「工程师自己的 agent 基建」。
2. **Claude Code** — Anthropic 的全功能 agentic coding 工具，跨终端/IDE/桌面/Web 统一工作流，instructions/memory/MCP/subagents 产品化能力强。更像「成熟的一体化编程代理工作台」。
3. **Codex** — OpenAI 的云端软件工程 agent，每个任务在独立云端 sandbox 执行，异步委派、并行处理、可审计交付。更像「远程 AI 工程师池」。
4. **常见误区** — 三者不是同一层级的模型对比。区别在于任务在本地还是云端跑、你要自己管多少安全和环境、你更需要实时结对还是异步委派。

## 受影响的 Wiki 页面

- [[wiki/entities/pi-agent]] — 已创建
- [[wiki/entities/claude-code]] — 已更新
- [[wiki/syntheses/ai-agent-ecosystem-comparison]] — 已更新
