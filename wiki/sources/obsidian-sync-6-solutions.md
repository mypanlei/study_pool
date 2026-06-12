---
title: "Obsidian 多设备同步的六种方案：从官方同步到自建 NAS"
tags:
  - source
  - obsidian
  - sync
created: 2026-06-13
updated: 2026-06-13
source_url: "https://zhupite.com/tool/obsidian-knowledge-base-sync-solutions.html"
source_author: "zhupite"
source_date: 2026-06-07
---

# Obsidian 多设备同步的六种方案

> 系统梳理 6 种 Obsidian 同步方案：官方同步、iCloud、GitHub/Git、百度网盘、Syncthing、自建 NAS，含详细配置步骤和决策树。

## 核心论点

1. **六方案全覆盖** — 从$4/月的官方同步到免费开源的 Syncthing，从零配置的 iCloud 到需要硬件的 NAS
2. **决策树选型法** — 按预算 → 设备 → 技术能力逐层决策，帮用户找到最适合的方案
3. **Git 方案细节最丰富** — 包含完整配置步骤、`.gitignore` 推荐、Obsidian Git 插件自动化

## 关键方案速览

| 方案 | 年费 | 难度 | 实时同步 | 端到端加密 |
|------|------|------|----------|-----------|
| 官方同步 | $48-120 | ⭐ | ✅ | ✅ |
| iCloud | 免费 | ⭐ | ✅ | ❌ |
| GitHub | 免费 | ⭐⭐⭐ | ❌ | ❌ |
| 百度网盘 | ~178元 | ⭐⭐ | ✅（有延迟） | ❌ |
| Syncthing | 免费 | ⭐⭐⭐ | ✅ 实时 | ✅ |
| NAS | 2000+硬件 | ⭐⭐⭐⭐ | ✅ 局域网 | ✅ |

## 本文特有的内容

- **百度网盘同步空间** — 国内 Windows 用户的实用之选（其他文章未重点介绍）
- **NAS 子方案对比** — Synology Drive / Nextcloud / Seafile / WebDAV 四种 NAS 同步方式
- **详细决策树** — 从预算出发的可视化选择路径
- `.gitignore` 推荐配置 — 排除 Obsidian 工作区状态和临时文件

## 受影响的 Wiki 页面

- [[wiki/syntheses/obsidian-sync-comparison]] — 已更新
