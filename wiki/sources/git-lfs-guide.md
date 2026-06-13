---
title: "Git LFS 工作原理与配置指南"
tags:
  - source
  - git
  - github
  - lfs
  - binary
  - tooling
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Git LFS 配置指南
---

# Git LFS 工作原理与配置指南

> 本文系统介绍 Git LFS 的核心机制（指针文件、clean/smudge filter）、配置步骤、历史迁移方案、GitHub 限制与计费规则以及协作治理注意事项。

## 核心贡献

1. **核心机制**：通过 Git filter 拦截流程 — `git add` 时 clean filter 将大文件替换为指针文件并存储到本地 LFS 对象区；`git push` 时 LFS 对象单独上传；`checkout` 时 smudge filter 恢复真实文件。
2. **指针文件格式**：包含 version、oid (SHA256 哈希)、size 三字段，Git 历史仅保存几十到几百字节文本指针。
3. **迁移策略**：从现在开始接管 (不改历史，最稳妥) vs `git lfs migrate import` 改写历史 (需 force-push，需协调协作者)。
4. **GitHub 限制与计费**：单文件上限 2-5 GB (按套餐)；免费额度 10 GiB 存储 + 10 GiB 月带宽；按整文件计存储 (非 diff)，fork 下载计原仓库带宽。
5. **协作纪律**：所有协作者需装 Git LFS；`.gitattributes` 必须入库；历史中的大文件 blobs 不会自动消除。

## 关联页面

- [[wiki/concepts/git-lfs]] — Git LFS 概念页

## 参考链接

- [GitHub LFS 官方文档](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)
- [GitHub LFS 计费](https://docs.github.com/en/billing/concepts/product-billing/git-lfs)
