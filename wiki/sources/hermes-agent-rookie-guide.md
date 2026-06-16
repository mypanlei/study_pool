---
title: "Hermes Agent 教程 — 菜鸟教程"
tags:
  - source
  - hermes-agent
  - agent-framework
  - nous-research
  - installation
  - gateway
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/hermes-agent.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Hermes Agent 教程

> Runoob 出品的 Hermes Agent 完整上手教程，涵盖快速安装、手动安装、模型提供商配置、消息网关设置（Telegram/Discord/Slack 等 15+ 平台）、以及日常使用命令。Hermes Agent 是 Nous Research 开源的自主 AI Agent 框架，核心理念是"让 AI 成为长期在线的数字员工"。

## 核心内容

1. **Hermes Agent 概述** — Nous Research 开源自主 AI Agent，原生内置学习闭环，支持记忆管理、技能生成与优化、跨会话召回。一句话定义："The agent that grows with you."
2. **模型提供商** — 支持 Nous Portal、OpenAI Codex、Anthropic Claude、OpenRouter（200+ 模型）、DeepSeek、Hugging Face、自定义端点（VLLM/SGLang/Ollama）。`hermes model` 一键切换，无厂商锁定。
3. **一键安装** — `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`，自动处理 uv/Python 3.11/Node.js/ripgrep/ffmpeg 依赖。Windows 需 WSL2。
4. **手动安装** — 分 8 步：git clone → 安装 uv → 创建 venv → pip install → 配置目录 → API 密钥 → PATH 链接 → 验证。支持扩展安装（messaging/cron/voice/mcp/honcho）。
5. **消息网关** — 单一网关接入 15+ 平台（Telegram/Discord/Slack/WhatsApp/Signal/Email/钉钉/飞书/企业微信/Home Assistant 等），支持前台/后台/Docker 运行。
6. **架构分层** — 10 层架构：接入层、输入层、调度器（Agent Orchestrator）、能力层、记忆层、知识层、模型层、工具层、外部服务层、基础设施层。

## 关键概念

- Hermes Agent 原生内置学习闭环，可从执行经验中沉淀技能并自主优化
- 消息网关支持单一入口对接多平台，`hermes gateway` 统一管理
- 定时自动化（Cron）+ 并行子 Agent + 多环境运行（本地/Docker/SSH/Modal）
