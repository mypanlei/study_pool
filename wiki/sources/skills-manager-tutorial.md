---
title: "Skills Manager — 跨 Agent 工具的统一 Skill 管理"
tags:
  - source
  - skills
  - workflow
  - tool
created: 2026-06-13
updated: 2026-06-13
source_url: "https://github.com/datawhalechina/ai-skills-for-everyone/blob/main/tutorial/06-manage-many-skills.md"
source_author: "Datawhale (ai-skills-for-everyone)"
source_date: 2026
---

# Skills Manager 教程：管理多个 Skill

> Datawhale 出品的 AI Skills 教程第 6 课，介绍开源工具 **Skills Manager** — 一个跨 Agent 工具的中央 Skill 管理器，解决"Skill 多了以后怎么整理"的问题。

## 核心论点

1. **Skills Manager**（[github.com/xingkongliang/skills-manager](https://github.com/xingkongliang/skills-manager)）是一个 Skill 管理器，不是 Skill 本身
2. **核心能力**：统一中央库、Global/Project Workspace、Presets（组合）、多工具同步、标签筛选、Git 备份
3. **适用时机**：5+ Skill、多 Agent 工具（Trae/Codex/Cursor/Claude Code）、不同任务组合
4. **安全建议**：首次用 Copy 模式（非 symlink），用假 Skill 做 smoke test

## 核心能力

| 能力 | 说明 |
|------|------|
| Unified library | 把不同来源的 Skill 收到中央库 |
| Global Workspace | 管理某 Agent 的全局 Skill 目录 |
| Project Workspace | 管理某项目的本地 Skill 目录 |
| Presets | 把一组 Skill 保存成组合，一次启用 |
| Multi-tool sync | 同一批 Skill 同步到多个 Agent |
| Tags & filters | 标签筛选 |
| Git backup | Git 备份，换电脑或回滚 |
| CLI | 命令行管理（需 Node.js + Rust） |

## 个人思考

- 这与之前 [[wiki/syntheses/claude-skill-management]] 中提到的「元 Skill」概念一致——用工具管理工具
- Skills Manager 用 GUI 做到了类似 `skill-manage` 元 Skill 的功能，但更偏向可视化操作
- 与全局目录 + symlink 方案对比：Skills Manager 更重但更可视化，全局目录更轻但更手动

## 受影响的 Wiki 页面

- [[wiki/syntheses/claude-skill-management]] — 已更新（新增 Skills Manager 策略）
