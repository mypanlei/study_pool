---
title: "Claude Code 自定义 Agent 配置指南 — Subagent 的创建、字段与最佳实践"
tags:
  - source
  - claude
  - agent
  - workflow
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://code.claude.com/docs/en/sub-agents"
source_author: "Anthropic 官方文档"
source_date: 2026-05-29
---

# Claude Code 自定义 Agent 配置指南

> Claude Code 的自定义 Agent（Custom Subagent）本质是「一个带 YAML frontmatter 的 Markdown 文件」，通过角色定义实现任务委派。

## 核心论点

1. **创建方式** — 通过 `/agents` 命令交互创建或手动创建 Markdown 文件，后者更适合版本管理和团队共享。
2. **文件位置** — 项目级 `.claude/agents/`（当前项目生效）和用户级 `~/.claude/agents/`（所有项目共享），同名时项目级优先。
3. **关键 frontmatter 字段** — `name`（唯一名称）、`description`（触发条件，最关键）、`tools`（最小权限）、`model`（可指定模型）。
4. **调用方式** — 自动委派（根据 description 匹配）或显式指定（`/agent-name` 或自然语言）。
5. **工具权限最小化原则** — 审查类 Agent 默认只读，修复类允许编辑，发布类谨慎授予 Bash 权限。

## 常见 Agent 模板

- **verifier** — 独立验证实现是否满足需求
- **debugger** — 系统化诊断疑难 bug
- **security-auditor** — 安全风险审查

## 受影响的 Wiki 页面

- [[wiki/entities/claude-code]] — 已更新
- [[wiki/concepts/agent-skills-system]] — 已关联
