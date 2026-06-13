---
title: "Hermes Agent 阿里云部署指南 — ECS + Docker + systemd 全流程"
tags:
  - source
  - hermes
  - alicloud
  - deployment
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://hermes-agent.nousresearch.com/docs/getting-started/installation"
source_author: "Nous Research / 自建笔记"
source_date: 2026-06-11
---

# Hermes Agent 阿里云部署指南

> 面向「把 Hermes Agent 长期部署在阿里云上」的场景：ECS Ubuntu + Hermes Agent + Docker backend + systemd 常驻网关服务。

## 核心论点

1. **推荐路线** — ECS Ubuntu 22.04/24.04 → SSH 登录 → 安装 Hermes → 先跑通 CLI 对话 → 切 Docker backend → 配 messaging gateway → systemd 常驻。
2. **Docker backend 是生产推荐** — 提供 cap-drop、no-new-privileges、PID limit、tmpfs 限制等隔离边界，危险命令审批不再是主要边界，容器本身才是边界。
3. **Provider 选择** — 中国地域 ECS 最自然组合是 DashScope/Qwen；也可用 Nous Portal 一键配置。
4. **单机版 vs 分离版** — 单机版（一台 ECS 就够）最推荐；分离版（网关机 + 执行机）适合更严格的安全边界。
5. **安全规范** — 不要以 root 运行、配 `GATEWAY_ALLOWED_USERS` 或 DM pairing、用 Docker backend、密钥放 `~/.hermes/.env` 并收紧权限。

## 最小上线顺序

1. 创建 ECS，开放 22 端口
2. 安装 Hermes，跑通 CLI 对话
3. 配置 provider
4. 安装 Docker，切到 `terminal.backend: docker`
5. 跑通一个消息平台的 gateway
6. 改为 systemd 常驻运行

## 受影响的 Wiki 页面

- [[wiki/entities/hermes-agent]] — 已更新
- [[wiki/sources/hermes-agent-alicloud-messaging-guide]] — 关联文章
