---
title: "Gemini CLI Skills 配置指南"
tags:
  - source
  - gemini
  - cli
  - skill
  - tooling
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Gemini CLI Skills 配置
---

# Gemini CLI Skills 配置指南

> 本文介绍 Gemini CLI 的 Skills 扩展机制，涵盖存储层级、定义规范 (SKILL.md)、运行机制 (发现/激活/状态控制) 和管理命令。

## 核心贡献

1. **存储层级**：项目级 (`.gemini/skills/`) → 全局级 (`~/.gemini/skills/`) → 插件级，遵循"局部优先"原则。
2. **SKILL.md 规范**：每个 Skill 为独立目录，包含带有 YAML Frontmatter (name, description) 的 SKILL.md。
3. **运行机制**：启动时扫描并注入 name/description → 用户需求匹配时调用 `activate_skill` 工具全量加载 → `settings.json` 中 skills.enabled/disabled 控制。
4. **管理命令**：`gemini skills list`、`gemini skills link <dir_path>`、`/skills` 对话模式查看。

## 关联页面

- [[wiki/entities/google-adk]] — Google ADK/Agent 平台（含 Gemini CLI Skills 对比）
- [[wiki/entities/claude-code]] — Claude Code Skills 机制对比

## 参考链接

- Gemini CLI 官方文档
