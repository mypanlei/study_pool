---
title: "Claudian 安装教程：把 Claude Code 接进 Obsidian"
tags:
  - source
  - obsidian
  - claude
created: 2026-06-13
updated: 2026-06-13
source_url: "https://zhuanlan.zhihu.com/p/2027903175898744570"
source_author: "小墨同学爱写程序的小鱼（知乎）"
source_date: 2026-04-16
---

# Claudian 安装教程

> 在 Obsidian 侧边栏集成 Claude Code，实现不切屏的 AI 写作体验。三步走：装 Obsidian → BRAT 装 Claudian → 配置 CLI 路径。

## 核心论点

1. **Claudian 的价值** — 解决了 Claude Code（CLI）与 Obsidian 之间来回切换的痛苦，让 AI 模型与 Obsidian 融为一体
2. **安装流程** — Obsidian → BRAT 装 Claudian（beta 插件）→ 配置 Claude CLI 路径
3. **两条路由** — 订阅路径（直接填 CLI 路径）vs 反代/中转路径（追加 `ANTHROPIC_API_KEY` + `ANTHROPIC_BASE_URL`）
4. **常见坑** — CLI 路径不对 / nvm 多 Node 环境导致 Claudian 找不到 claude

## 关键细节

- Claudian 未进官方市场，需通过 **BRAT**（Obsidian beta 插件管理器）安装
- GitHub 地址：`https://github.com/YishenTu/claudian`
- 也支持 Codex 作为后端（beta，不够稳定）
- nvm/volta/fnm 多版本管理器用户容易遇到 `claude` 和 `node` 不在同目录的问题

## 个人思考

- 这篇文章描述的正是你现在正在使用的配置（Claudian + Claude Code），是你的工作流基础设施的一部分
- 「第三条路是 Codex，先不急」—— 这是 2026-04 的判断，现在 Codex 可能更成熟了
- 本质上 Claudian 是一个「AI 前端 UI」，把 LLM Agent 的能力嵌入到 Obsidian 的编辑体验中

## 受影响的 Wiki 页面

- [[wiki/entities/claudian]] — 已创建
- [[wiki/entities/claude-code]] — 已更新
