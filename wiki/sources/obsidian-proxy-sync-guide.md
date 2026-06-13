---
title: "Obsidian 代理设置与非官方 Vault 同步方案"
tags:
  - source
  - obsidian
  - proxy
  - sync
  - vault
  - syncthing
  - webdav
  - git
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Obsidian 代理与同步方案
---

# Obsidian 代理设置与非官方 Vault 同步方案

> 全面梳理 Obsidian 代理配置的三种层次（系统代理、Electron 启动参数、插件/CLI 代理）以及八种非官方同步方案的对比选型。

## 核心贡献

1. **代理三层架构**：
   - 系统代理：影响 Obsidian 本体和 Chromium/Electron 网络栈请求。
   - Electron 启动参数：`--proxy-server`、`--proxy-bypass-list`、`--proxy-pac-url`，但 **不支持内嵌用户名密码认证**。
   - 插件/CLI 代理：Git、Claudian、Remotely Save 等组件需分别配置。
2. **八种非官方同步方案全景**：iCloud/OneDrive/Google Drive (云盘)、Syncthing (P2P)、Git (手动/插件)、Remotely Save (多协议)、WebDAV Sync、Self-hosted LiveSync。
3. **关键纪律**：同一 Vault 只跑一种主同步机制；慎重决定是否同步 `.obsidian` 目录；迁移前完整备份。
4. **设备组合建议**：Windows + Android + iPad 场景优先推荐 Remotely Save + WebDAV/R2；从零开始无后端时推荐 R2。

## 关联页面

- [[wiki/syntheses/obsidian-sync-comparison]] — Obsidian 同步方案综合分析（本文章已引用）
- [[wiki/entities/claudian]] — Claudian 插件需独立配置代理

## 参考链接

- [Obsidian 官方帮助：跨设备同步](https://help.obsidian.md/sync-notes)
- [Electron 命令行开关文档](https://www.electronjs.org/docs/latest/api/command-line-switches)
