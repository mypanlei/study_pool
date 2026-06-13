---
title: "Claude Code"
tags:
  - entity
  - claude
  - ai
  - tool
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Claude Code CLI
---

# Claude Code

> Anthropic 推出的 AI 编程助手 CLI 工具，也是你当前通过 Claudian + 反代使用的后端引擎。

## 关键信息

- **类型**: AI 编程助手（CLI）
- **开发商**: Anthropic
- **核心能力**: 代码生成、文件操作、终端命令、Agent 模式
- **扩展机制**: Skills / Agents / Commands / Hooks

## 你当前的使用方式

- 通过 [[wiki/entities/claudian]] 在 Obsidian 侧边栏中使用
- 通过反代/中转连接到 DeepSeek API（`api.deepseek.com/anthropic`）
- 使用模型：`deepseek-v4-flash[1m]`（映射为 Haiku）
- Effort Level: max

## 配置位置

- **用户级配置**: `~/.claude/settings.json`
- **项目级配置**: `.claude/settings.json`（当前 vault 未设置）

## 与 Gemini CLI 对比

| 维度 | Claude Code | Gemini CLI |
|------|-------------|------------|
| 开发商 | Anthropic | Google |
| Skills 存储层级 | 项目级 `.claude/skills/` → 全局 `~/.claude/skills/` | 项目级 `.gemini/skills/` → 全局 `~/.gemini/skills/` → 插件级 |
| Skills 定义 | SKILL.md (YAML frontmatter + markdown) | SKILL.md (YAML frontmatter + markdown) |
| 激活机制 | 启动时扫描注入描述，会话中按需加载 | 启动时扫描注入 name/description，调用 `activate_skill` 工具全量加载 |
| 状态控制 | settings.json hooks 配置 | settings.json skills.enabled/disabled |
| 管理命令 | `claude skills list/link` | `gemini skills list/link` |

两者在 Skills 机制上高度相似，均采用"局部优先"的目录层级和 SKILL.md 规范。Gemini CLI 增加了一层插件级调度。

## 来源

- [[wiki/sources/claudian-setup-guide]]
- [[wiki/sources/claude-code-custom-agent-guide]]
- [[wiki/sources/gemini-cli-skills-guide]] — Gemini CLI Skills 对比参考资料
