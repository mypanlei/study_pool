---
title: "Claudian"
tags:
  - entity
  - obsidian
  - plugin
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Claudian 插件
---

# Claudian

> Obsidian 社区插件，在侧边栏嵌入 Claude Code（或 Codex）对话界面，让 LLM Agent 与 Obsidian 编辑体验无缝融合。

## 关键信息

- **类型**: Obsidian 社区插件（beta）
- **开发者**: YishenTu
- **GitHub**: [github.com/YishenTu/claudian](https://github.com/YishenTu/claudian)
- **安装方式**: 通过 BRAT（Obsidian beta 插件管理器）安装
- **后端支持**: Claude Code（主力）、Codex（beta）
- **核心价值**: 不切屏、不开终端，在 Obsidian 侧边栏直接与 AI 对话

## 配置要点

1. 安装 BRAT → `Add beta plugin` → 粘贴 `https://github.com/YishenTu/claudian`
2. 设置中配置 Claude CLI 路径
3. 订阅路径：直接使用；反代路径：追加 `ANTHROPIC_API_KEY` + `ANTHROPIC_BASE_URL`

## 常见问题

- **CLI not found** — 路径不对或 nvm/volta 多 Node 环境导致 PATH 不一致
- **一直 loading** — CLI 路径对但 Claude Code 跑不起来
- **红色报错** — 多半是 CLI 路径问题

## 你当前的配置

- 你正在使用 Claudian（settingsProvider: "claude"）
- 配置了反代/中转（ANTHROPIC_BASE_URL → api.deepseek.com）
- 使用 Haiku 模型 + high effort

## 来源

- [[wiki/sources/claudian-setup-guide]]
