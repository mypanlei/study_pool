---
title: "Obsidian + 浏览器扩展 + Claudian 知识工作流方案"
tags:
  - source
  - obsidian
  - web-clipper
  - claudian
  - claude-code
  - workflow
  - knowledge-base
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Obsidian Claudian 工作流
---

# Obsidian + 浏览器扩展 + Claudian 知识工作流方案

> 本文提出一个三层闭环知识工作流：浏览器扩展负责采集网页内容为结构化 Markdown，Obsidian 负责存储与组织，Claudian 负责 AI 理解与加工，形成从采集到沉淀的完整链路。

## 核心贡献

1. **三层闭环架构**：
   - 采集层：Obsidian Web Clipper 裁剪网页为结构化 Markdown（支持模板/变量/过滤器）。
   - 存储层：Obsidian Vault — 本地 Markdown、Wikilinks、双向链接、图谱、Git 管理。
   - 加工层：Claudian (Obsidian 插件) 嵌入 Claude Code/Codex 等 Agent 能力，直接读写 vault 文件。
2. **三个典型场景**：技术研究（阅读→采集→AI 提炼→综述）、内容生产（素材→AI 重组→人工审校）、个人第二大脑（信息→知识库→持续整理）。
3. **关键优势**：数据为本地 Markdown 不被平台锁死、AI 围绕完整 vault 工作而非片段上下文、采集与整理打通。
4. **主要限制**：Claudian 仅桌面端、依赖 CLI 环境、模板质量影响下游成本、隐私需关注 Provider 数据发送边界。
5. **推荐目录结构**：Inbox/Web-Clips → Topics/ → Maps/ → Templates/ → Assets/。

## 关联页面

- [[wiki/entities/claudian]] — Claudian 实体页
- [[wiki/entities/claude-code]] — Claude Code 作为后端引擎
- [[wiki/syntheses/obsidian-sync-comparison]] — Obsidian 同步方案综合分析（本工作流的同步基础）

## 参考链接

- [Claudian GitHub](https://github.com/YishenTu/claudian)
- [Obsidian Web Clipper](https://obsidian.md/clipper)
- [Claude Code 文档](https://code.claude.com/docs/en/overview)
