---
title: "GitHub CLI (gh) 代理配置指南"
tags:
  - source
  - github
  - cli
  - proxy
  - network
created: 2026-06-13
updated: 2026-06-13
aliases:
  - GitHub CLI 代理配置
---

# GitHub CLI (gh) 代理配置指南

> 本文明确 GitHub CLI (gh) 本身没有 `gh config set proxy` 的直接命令，需要通过系统环境变量或 Git 配置实现代理功能，并涵盖 SSH 协议代理和验证方法。

## 核心贡献

1. **推荐方式：环境变量** — `gh` 自动识别 `HTTPS_PROXY`/`HTTP_PROXY`/`NO_PROXY` 标准环境变量，适用于 Linux/macOS/Windows。
2. **Git 配置层**：`gh repo clone` 等操作调用底层 `git` 命令，需单独配置 Git 代理 (`git config --global http.proxy`)。
3. **SSH 协议代理**：`~/.ssh/config` 中通过 `ProxyCommand nc -X 5 -x` 配置 SOCKS5 代理。
4. **SOCKS5 支持**：格式为 `socks5://127.0.0.1:7890`；代理认证使用 `http://username:password@host:port`。

## 关联页面

- [[wiki/entities/claude-code]] — 关联到 CLI 代理配置环境

## 参考链接

- [GitHub CLI Manual](https://cli.github.com/manual/gh_config)
- [GitHub CLI Environment Variables](https://cli.github.com/manual/gh_help_environment)
