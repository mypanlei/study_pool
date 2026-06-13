---
title: "标签索引 (Dataview)"
tags:
  - meta
  - dataview
created: 2026-06-13
updated: 2026-06-13
aliases:
  - Tags Index
  - 标签导航
---

# 标签索引

> 本页使用 Dataview 动态查询自动生成。需要先安装 Dataview 社区插件。
>
> **安装**: 设置 → 社区插件 → 搜索 "Dataview" → 安装并启用

---

## 全部页面概览

按类型分类，包含所有 Wiki 内容页（排除模板）：

```dataview
TABLE length(file.tags) as "标签数", file.folder as "位置"
FROM "wiki"
WHERE file.name != "index.md" AND file.name != "log.md" AND !contains(file.path, "templates/")
SORT file.folder ASC, file.name ASC
```

---

## 按标签分组浏览

### `#agent` — AI Agent 相关

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #agent AND "wiki"
WHERE file.name != "index.md" AND file.name != "log.md"
SORT file.folder ASC
```

### `#ai` — AI 通用

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #ai AND "wiki"
WHERE file.name != "index.md" AND file.name != "log.md"
SORT file.folder ASC
```

### `#claude` — Claude / Claude Code

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #claude AND "wiki"
SORT file.folder ASC
```

### `#obsidian` — Obsidian 相关

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #obsidian AND "wiki"
SORT file.folder ASC
```

### `#hermes` — Hermes Agent

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #hermes AND "wiki"
SORT file.folder ASC
```

### `#comparison` — 对比分析

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #comparison AND "wiki"
SORT file.folder ASC
```

### `#methodology` — 方法论

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #methodology AND "wiki"
SORT file.folder ASC
```

### `#gemini` + `#kubeflow` — 企业 AI 平台

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM (#gemini OR #kubeflow OR #mlops) AND "wiki"
SORT file.folder ASC
```

### `#openclaw` + `#pi` — Personal AI Agent

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM (#openclaw OR #pi) AND "wiki"
SORT file.folder ASC
```

### `#sync` — 同步方案

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #sync AND "wiki"
SORT file.folder ASC
```

### `#harness` — Harness Engineering

```dataview
TABLE file.folder as "类型", file.etags as "标签"
FROM #harness AND "wiki"
SORT file.folder ASC
```

---

## 标签云

所有标签及其出现频率：

```dataview
TABLE rows.file.link as "页面"
FROM "wiki"
WHERE !contains(file.path, "templates/") AND file.name != "index.md" AND file.name != "log.md"
FLATTEN file.tags as tag
GROUP BY tag
SORT rows.length DESC
```

---

## 最近更新的页面

```dataview
TABLE file.folder as "位置", file.mtime as "最后更新"
FROM "wiki"
WHERE file.name != "index.md" AND file.name != "log.md" AND !contains(file.path, "templates/")
SORT file.mtime DESC
LIMIT 15
```
