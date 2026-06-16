---
title: "Marp — Markdown 演示生态系统"
tags:
  - concept
  - presentation
  - tool
  - markdown
created: 2026-06-17
updated: 2026-06-17
aliases:
  - Marp 演示
  - Marp 幻灯片
---

# Marp (Markdown Presentation Ecosystem)

> 用 Markdown 写幻灯片的开源工具。支持 `---` 分隔幻灯片、YAML frontmatter 设置主题、CSS 自定义样式、Mermaid 图表、LaTeX 公式。本知识库中的演示文稿均使用 Marp 格式。

## 核心语法

```markdown
---
marp: true
theme: uncover
---

# 第一页
内容...

---

# 第二页
```
用 `---` 分隔幻灯片，`<!-- -->` 添加指令（分页号、页头/页脚、主题等）。

## 在 Obsidian 中使用

- 安装 Obsidian 社区插件 `Marp`
- 文件 frontmatter 设置 `marp: true`
- 渲染后可通过 `Ctrl/Cmd + Shift + I` 打开预览

## 本知识库中的 Marp 演示

- [[wiki/syntheses/harness-engineering-presentation]]
- [[wiki/syntheses/flyte-vs-kubeflow-presentation]]

## 来源

- 知识库内 5 处引用
