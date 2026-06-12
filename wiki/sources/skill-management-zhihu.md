---
title: "Skill 的管理方法 — 跨设备/跨工具/跨项目统一管理"
tags:
  - source
  - workflow
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://zhuanlan.zhihu.com/p/2025963062037868570"
source_author: "空格的键盘（知乎）"
source_date: 2026-04-10
---

# Skill 的管理方法

> 面对 130+ 个 Skill 在多个项目、多台电脑之间无法同步的痛点，作者提出「四个方法实现四层互通」的完整解决方案。

## 核心痛点

1. **跨文件夹/跨工具调不到** — Cursor 项目 A 有 Skill，项目 B 没有；改了 A 忘同步 B
2. **跨电脑用不了** — 公司、家里、出差三套残缺版本，手动拷贝总有遗漏
3. **分享出去很乱** — 130 个 Skill 混在一起，没有分类索引，分享要手动挑
4. **知识库同步不了** — Obsidian 仓库 100+ GB，GitHub 推不上去，换电脑就断

## 四层互通方案

### 第一层：跨文件夹互通 = 全局目录 + 软链接

> **核心原则：Single Source of Truth**

所有 Skill 只存一个地方：`~/.claude/skills/`，各项目通过 symlink 指向全局目录。

```bash
# 一行命令，所有项目都能调用全部 Skill
obsidian/.claude/skills → ~/.claude/skills (symlink)
```

改了某个 Skill？只改全局目录，所有项目同时生效。

### 第二层：跨电脑互通 = GitHub 私密仓库

全局目录解决了本地问题，但换台电脑还是得重新来。

```bash
~/.claude/skills/ → github.com/username/allSkills (private repo)
```

新电脑 git clone 一行命令，全部 Skill 恢复。

### 第三层：跨网络分享 = 分类 + GitHub 公开仓库

按领域拆分为多个公开仓库：

| 仓库 | 领域 | 数量 |
|------|------|------|
| write-skill | 写作 / 内容生产 | 21 |
| draw-skill | 画图 / 设计 / 视觉 | 13 |
| info-skill | 信息获取 / RSS / 爬虫 | 14 |
| protodesign | 产品 / PM / 原型 | 13 |

### 第四层：跨设备知识库同步 = NAS + rsync

针对 Obsidian 知识库太大无法用 GitHub 同步的问题，使用 NAS + rsync 定时同步。

## 元 Skill：skill-manage

用一个 Skill 管理所有 Skill：

1. 扫描全局目录，找出新增的 Skill
2. 按规则自动判断归属分类
3. 复制到对应的分类仓库
4. 全量同步到私密仓库
5. 对所有仓库执行 git commit + push
6. 可选：触发 NAS 同步

## 核心理念

> 上下文优先于提示词。Skill 的创建是封装上下文，Skill 的管理也是。
>
> - 全局目录 = 上下文的单一来源
> - 软链接 = 上下文的分发通道
> - GitHub = 上下文的持久化
> - NAS = 上下文的多端同步
> - skill-manage = 上下文的自动化维护

## 个人思考

- 这篇的思路与我之前生成的 [[wiki/syntheses/claude-skill-management]] 高度一致，但在跨电脑同步和分类分享方面给出了更落地的方案
- 区别在于：我之前推荐的方案是「每个项目独立 Skills 目录 + symlink 到集中仓库」；本文推荐的是「全局 `~/.claude/skills/` 做唯一来源 + 各项目 symlink 指向它」。前者更灵活，后者更简单。
- skill-manage 的思路很好：用元 Skill 来自动化管理流程，真正实现"用 AI 管理 AI 的能力"

## 受影响的 Wiki 页面

- [[wiki/syntheses/claude-skill-management]] — 已更新（补充全局目录策略和跨设备同步方案）
- [[wiki/concepts/llm-wiki-pattern]] — 验证了 LLM Wiki 模式中「好的答案归档回维基」的理念
