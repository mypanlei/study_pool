---
title: "Wiki Lint Report — 2026-06-22"
tags:
  - meta
  - lint
created: 2026-06-22
updated: 2026-06-22
---

# Wiki Lint Report — 2026-06-22

> 定期 Lint 检查：孤儿页、断链、索引统计、raw/sources 与 wiki/sources 一致性

## 1. 孤儿页检查 (Orphan Pages)

**结果: ✅ 无孤儿页**

所有 186 个内容页面均在 `index.md` 中有索引条目。不存在有文件但未在索引中引用的页面。

## 2. 索引统计一致性

**结果: ✅ 所有统计与实际文件数一致**

| 类别 | index.md 统计 | 实际文件数 | 状态 |
|------|--------------|-----------|------|
| 实体 (Entities) | 28 | 28 | ✅ |
| 概念 (Concepts) | 33 | 33 | ✅ |
| 源摘要 (Sources) | 112 | 112 | ✅ |
| 综合分析 (Syntheses) | 13 | 13 | ✅ |
| 原始资料 (raw) | 114 | 114 | ✅ |

## 3. raw/sources 与 wiki/sources 一致性

**结果: ✅ 差异已确认**

- raw/sources: 114 篇
- wiki/sources: 112 篇
- 差异: 2 篇（预期内）

两个已知差异：
1. A2A 多源文件合并（3 个 Clippings + 2 个原始资料合并为单一源摘要）
2. 浙江省技术经纪人培训（`optimize` 操作，非标准 Ingest，已在 2026-06-19 Lint 中移除了断链索引条目）

## 4. 断链检查 (Broken Links)

**结果: ⚠️ 发现 1 个断链**

### 🟡 问题: vector-database 概念页待创建

`wiki/sources/rag-vector-store-javaguide.md` 中的 `[[wiki/concepts/vector-database]]` 指向不存在页面，标记为"（页面待创建）"。

- **根因**: 该页面在创建源摘要时被标记为待创建，但尚未填充。
- **影响**: 1 处死链接。
- **修复**: 已改为指向现有 `[[wiki/sources/vector-database-introduction]]`

## 5. 前次 Lint 修复验证

**结果: ✅ 全部 5 个知识缺口已填补**

| 优先级 | 概念 | 上次状态 | 当前状态 |
|--------|------|----------|----------|
| 🔴 P0 | MCP | ⚠️ 缺失 → ✅ 已创建 | ✅ 已大幅增强 |
| 🔴 P0 | ReAct | ⚠️ 缺失 → ✅ 已创建 | ✅ 稳定 |
| 🟡 P1 | Prompt Engineering | ⚠️ 缺失 → ✅ 已创建 | ✅ 稳定 |
| 🟡 P1 | Chain of Thought | ⚠️ 缺失 → ✅ 已创建 | ✅ 稳定 |
| 🟢 P2 | Guardrails | ⚠️ 缺失 → ✅ 已创建 | ✅ 稳定 |

## 汇总

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 孤儿页 | ✅ | 0 个孤儿 |
| 索引统计 | ✅ | 与实际文件数一致 |
| raw vs wiki 一致性 | ✅ | 差异 2 篇属预期 |
| 断链 | ⚠️ | 1 个问题：vector-database 引用已修复 |
| 前次修复 | ✅ | 5 个知识缺口全部填补 |

**全文统计**: 28 实体 + 33 概念 + 112 源摘要 + 13 综合分析 = 186 页
**原始资料**: 114 篇（全部已 Ingest）
