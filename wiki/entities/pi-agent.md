---
title: "Pi"
tags:
  - entity
  - agent
  - ai
  - coding
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Pi Agent
  - Pi coding agent
---

# Pi

> 开源、多 provider、偏本地控制的 coding agent harness。强调开放控制权，但默认安全边界较弱需自己配置。

## 关键信息

- **类型**: 开源 coding agent harness / CLI
- **开发商**: earendil-works（社区开源）
- **核心定位**: self extensible coding agent，统一多模型访问层 + agent runtime + CLI + TUI
- **默认运行位置**: 本地
- **模型策略**: 多 provider，不绑定单一家模型厂商

## 核心特色

| 特性 | 描述 |
|------|------|
| 多 provider | 支持多种模型提供商切换 |
| 本地 CLI | 终端原生工作方式 |
| 可扩展 runtime | 可自定义容器化和隔离方式 |
| 开源 | 完全开源，可自建 |
| 默认安全边界 | 较弱，需自己做 sandbox/containerization |

## 选型判断

- 适合：想要开源可控、多 provider 灵活切换、自己掌控 agent runtime
- 不适合：需要即开即用的安全边界和产品化体验

## 来源

- [[wiki/sources/pi-claude-codex-comparison]]
- [[wiki/sources/pi-claude-codex-english-presentation]]
- [[wiki/sources/openclaw-hermes-pi-codex-copilot-comparison]]
