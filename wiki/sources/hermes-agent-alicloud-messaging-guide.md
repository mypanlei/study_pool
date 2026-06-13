---
title: "Hermes Agent 阿里云消息入口实操 — 飞书与微信接入"
tags:
  - source
  - hermes
  - alicloud
  - deployment
  - active
created: 2026-06-13
updated: 2026-06-13
source_url: "https://hermes-agent.nousresearch.com/docs/user-guide/messaging"
source_author: "Nous Research / 自建笔记"
source_date: 2026-06-11
---

# Hermes Agent 阿里云消息入口实操：飞书与微信

> 在阿里云 ECS 上把 Hermes Agent 接到飞书（WebSocket 推荐）和微信（iLink Bot API，仅限私聊）两种消息入口的完整实操指南。

## 核心论点

1. **飞书推荐 WebSocket 模式** — ECS 只需出网能力，不需要域名和公网 webhook，安全组只开 22 端口即可。私聊高可用，群聊默认仅 `@bot` 响应。
2. **微信仅适合私聊入口** — 走 iLink Bot API 的 long-poll 模式，群聊可靠性低，普通微信群事件常常根本不会送达。需要区分 Weixin（个人微信）和 WeCom（企业微信）。
3. **最小部署顺序** — 先跑通 CLI → 第一个入口接飞书 WebSocket → 稳定后再补微信私聊入口。不要在第一阶段承诺微信群聊能力。
4. **飞书可能踩的坑** — 应用没发布、群聊不 @ 不回、没做 allowlist、Webhook 没配 token/encrypt key。

## 建议的落地顺序

1. 按阿里云部署指南跑通 CLI 和 provider
2. 第一个消息入口接飞书 WebSocket
3. 用飞书完成 `/set-home` 作为主入口
4. gateway 稳定后补微信私聊入口（仅个人触达）

## 受影响的 Wiki 页面

- [[wiki/entities/hermes-agent]] — 已更新
- [[wiki/sources/hermes-agent-alicloud-deployment-guide]] — 关联文章
