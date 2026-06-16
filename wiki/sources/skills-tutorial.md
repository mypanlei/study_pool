---
title: "Skills 教程 — 菜鸟教程"
tags:
  - source
  - skills
  - agent
  - prompt
  - mcp
  - claude-code
  - cursor
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/skills-agent.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Skills 教程

> 系统介绍 Skills（技能）的概念、结构和实践。Skills 是以 Markdown 文件形式存在的可复用 AI 能力模块，通过按需加载和渐进式披露实现高效经验传递。涵盖 Skills 与传统 Prompt 的区别、SKILL.md 文件结构、Claude Code Skills 配置、以及推荐 Skills 资源列表。

## 核心内容

1. **Skills vs Prompt** — 普通 Prompt 每次重新描述且全量占用上下文，Skills 按需加载渐进式披露，一次编写处处复用。
2. **Skills 核心结构** — 文件夹 + SKILL.md（YAML frontmatter 元数据 + Markdown 指令），支持 scripts/references/assets 附属目录。
3. **Skills vs MCP** — Skills 用于知识复用（经验/最佳实践/工作流，无需后端），MCP 用于能力扩展（API/数据库/外部工具，需要编码配置）。
4. **Claude Code Skills** — 四级优先级（企业级>个人级~/.claude/skills>项目级.claude/skills>插件级），渐进式加载（发现→激活→执行）。
5. **推荐的 Skills 资源** — skills.sh、skillsmp.com、skillhub.tencent.com、agentskills.io 等市场平台，以及 find-skills/vercel-react-best-practices/frontend-design 等推荐技能。
6. **支持的客户端** — Claude Code、Cursor、Trae/OpenCode、VS Code 插件、国内平台（扣子等）。

## 关键概念

- Skills = "岗位培训大礼包"，告诉 AI 某类事情应该怎么做
- Skills 三种加载阶段：发现（只读名称和描述）→ 激活（匹配时加载完整指令）→ 执行
- Skills 极大节省 Token，只在需要时才把厚厚的 SOP 塞入上下文
