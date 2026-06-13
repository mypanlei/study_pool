---
title: "Git LFS"
tags:
  - concept
  - git
  - github
  - lfs
  - binary
  - version-control
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Git Large File Storage
  - Git LFS
---

# Git LFS (Git Large File Storage)

> Git 的大文件旁路存储机制，通过指针文件 + 独立对象存储解决 Git 对大二进制文件管理效率低和 GitHub 单文件大小限制的问题。

## 定义

Git LFS 是 Git 针对大体积二进制文件的一层旁路存储机制。核心思路是通过 Git filter 机制拦截大文件的提交和检出流程：Git 仓库中仅保留几十到几百字节的文本指针文件，真实文件内容存储在独立的 LFS 对象存储中。

## 核心要点

1. **工作机制**：
   - `git add` 时 clean filter 将真实文件替换为 pointer 文件，真实内容存入本地 LFS 对象区。
   - `git push` 时普通 Git 对象和 LFS 对象分别上传。
   - `checkout` 时 smudge filter 根据 pointer 下载并恢复真实文件。
2. **Pointer 文件格式**：包含 `version`（规范版本）、`oid`（SHA256 哈希）、`size`（原始文件大小）三字段。
3. **历史迁移**：从现在开始接管（不改历史，最稳妥）vs `git lfs migrate import` 改写历史（需 force-push）。
4. **GitHub 限制**：单文件 2-5 GB（按套餐）；免费额度 10 GiB 存储 + 10 GiB 月带宽；按整文件计存储（非 diff）。
5. **协作纪律**：所有协作者需装 Git LFS；`.gitattributes` 必须入库；历史中的大文件 blobs 不会自动消除。

## 相关概念

- [[wiki/concepts/data-versioning-and-management]] — 数据版本控制（DVC/lakeFS 等对比）

## 来源

- [[wiki/sources/git-lfs-guide]] — Git LFS 工作原理与配置指南
