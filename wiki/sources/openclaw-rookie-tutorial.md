---
title: "OpenClaw (Clawdbot) 教程 — 菜鸟教程"
tags:
  - source
  - openclaw
  - agent
  - clawdbot
  - tutorial
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/openclaw-clawdbot-tutorial.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# OpenClaw (Clawdbot) 教程

> OpenClaw 的安装配置与入门教程。OpenClaw（原名 Clawdbot/过渡名 Moltbot）是由 Peter Steinberger（PSPDFKit 创始人）开发的开源个人 AI 助手项目，将本地算力与大模型 Agent 自动化结合，实现任务规划、终端命令执行、文件操作、代码编写等工程级自动化能力。

## 核心内容

1. **项目背景** — Clawdbot → Moltbot → OpenClaw 的名称演变历程，因 Anthropic 商标顾虑更名。
2. **安装方式** — 一键脚本（curl/powershell）、npm/pnpm 全局安装、源码安装三种方式。
3. **配置流程** — 交互式向导（onboard）配置模型供应商、通道、网关端口、Skills 选择。
4. **核心功能** — 任务规划、终端命令执行、代码编写与自我修复、浏览器控制、邮件/日历操作、长期记忆。
5. **技能系统** — ClawHub 技能市场（500+ 社区技能）、Skills 安装与管理、插件管理。
6. **工作区结构** — AGENTS.md、USER.md、MEMORY.md、HEARTBEAT.md、SOUL.md、IDENTITY.md、BOOT.md。

## 关键概念

- OpenClaw 目标是让 AI 不只是给建议，而是直接完成完整工程任务
- 与 Claude Code 相比：Claude Code 强在代码质量，OpenClaw 强在完整工程流程自动化
- 支持国内外几乎所有大模型（Claude、Gemini、OpenAI、Ollama、Qwen 等）
