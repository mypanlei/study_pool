---
title: "Obsidian 多设备同步方案综合分析"
tags:
  - synthesis
  - obsidian
  - sync
created: 2026-06-13
updated: 2026-06-13
---

# Obsidian 多设备同步方案综合分析

> 综合两篇深度文章，系统梳理 Obsidian 主流同步方案，含对比、选型建议和你当前使用的方案定位。

---

## 现有方案全景

### 一、官方生态

| 方案 | 费用 | 难度 | 实时性 | 加密 | 平台 |
|------|------|------|--------|------|------|
| **Obsidian Sync** | $4-10/月 | ⭐ | ✅ 自动 | ✅ 端到端 | 全平台 |
| **Obsidian Git** | 免费 | ⭐⭐⭐ | ❌ 手动 | ❌ | 全平台 |

### 二、云存储

| 方案 | 费用 | 难度 | 实时性 | 适合人群 |
|------|------|------|--------|----------|
| **iCloud** | 免费 | ⭐ | ✅ | 苹果全家桶 |
| **百度网盘同步空间** | ~178元/年 | ⭐⭐ | ✅ 有延迟 | 国内 Windows |
| **OneDrive** | 免费(5GB) | ⭐ | ✅ | Win/Mac |
| **坚果云插件** | 免费(5GB/1G月) | ⭐ | ✅ 有限制 | 国内轻度用户 |

### 三、技术方案

| 方案 | 费用 | 难度 | 实时性 | 加密 | 特点 |
|------|------|------|--------|------|------|
| **Syncthing** | 免费 | ⭐⭐⭐ | ✅ 实时 | ✅ P2P | iOS受限 |
| **Git (GitHub)** | 免费 | ⭐⭐⭐ | ❌ 手动 | ❌ | 版本历史 |
| **Remotely Save** | 免费 | ⭐ | ✅ | 取决于后端 | 多协议 |
| **Self-hosted LiveSync** | 免费 | ⭐⭐⭐⭐ | ✅ 即时 | ✅ | 需服务器 |
| **NAS (Synology/Nextcloud)** | 2000+硬件 | ⭐⭐⭐⭐ | ✅ 局域网 | ✅ | 完全自控 |

---

## 你当前的同步方案

你的 vault 位于 `C:\Users\mypan\OneDrive\workspace\study_pool`，这意味着你正在使用 **OneDrive** 作为底层的文件同步方案。

| 项目 | 内容 |
|------|------|
| **同步方式** | OneDrive（系统级同步） |
| **版本控制** | Git（已初始化，branch: main） |
| **Git 远程** | 有 origin（未推送） |
| **插件** | obsidian-git 已安装 |
| **附件** | OneDrive 同步 + Git 跟踪 |

### 当前方案的优势

- ✅ OneDrive 提供实时自动同步，不需要额外配置
- ✅ Git 提供版本历史（可配合 obsidian-git 插件自动化）
- ✅ 跨设备（Windows + 手机端 OneDrive 可用）
- ✅ `obsidian-excalidraw-plugin` 等绘图工具已就绪

### 潜在风险

- ⚠️ Git 尚未 push 到远程，当前只有本地历史
- ⚠️ OneDrive 同步冲突需要留意
- ⚠️ vault 含有 .git 目录，OneDrive 同步大 git 仓库可能有性能问题

---

## 选型建议

基于你的实际需求（已有 OneDrive + Git，偏好技术方案）：

1. **短期** — 维持 OneDrive + 本地 Git 的方案，配置 obsidian-git 插件做定时 commit
2. **中期** — 将 Git push 到 GitHub 私密仓库，实现跨设备版本控制和备份
3. **长期** — 若 vault 过大超出 OneDrive/ GitHub 限制，考虑 NAS + Syncthing

> **核心原则**：同步 ≠ 备份。无论哪种方案，定期将 Git push 到远程是最基本的保障。

---

## 来源

- [[wiki/sources/obsidian-sync-7-solutions]]
- [[wiki/sources/obsidian-sync-6-solutions]]

## 相关页面

- [[wiki/concepts/llm-wiki-pattern]]
- [[wiki/entities/claudian]]
