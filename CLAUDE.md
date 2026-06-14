# LLM Wiki — 知识库架构

这是一个基于 **Karpathy LLM Wiki 模式** 构建的个人知识库。

## 三层架构

```
📂 raw/              ← 原始资料层（不可变，只读不写）
  ├── sources/         - 源文件（文章、论文、笔记、剪藏）
  └── assets/          - 图片等附件
📂 wiki/             ← 维基层（AI 全权写入和维护）
  ├── entities/        - 实体页（人物、组织、产品、项目）
  ├── concepts/        - 概念页（理论、方法、术语）
  ├── sources/         - 源摘要页（每篇源材料的总结）
  ├── syntheses/       - 综合分析页（跨源对比、专题综述）
  ├── templates/       - 页面模板
  ├── index.md         - 内容索引目录（自动更新）
  ├── log.md           - 操作日志（仅追加）
  └── tag-index.md     - Dataview 标签索引
📂 .claude/agents/   ← Schema 层（定义维基结构和工作流）
  └── llm-wiki.md      - LLM Wiki Agent 定义
📄 CLAUDE.md          ← 本文件（Schema 入口，知识库总览）
```

## 工作流

### 1. 采集
用 Obsidian Web Clipper 剪藏网页 → 自动落入 `Clippings/` → 手动或由 LLM 复制到 `raw/sources/`

### 2. Ingest
LLM 读取 `raw/sources/` 中的新文件 → 创建 `wiki/sources/` 摘要 → 更新相关实体/概念/综合分析页 → 更新 `index.md` 和 `log.md`

### 3. Query
用户提问 → LLM 读 `index.md` 定位页面 → 深入阅读 → 综合回答 → 有价值的答案归档为 wiki 页面

### 4. Lint
LLM 定期检查：矛盾主张、过时内容、孤儿页、知识缺口、交叉引用缺失

## 当前状态
- 原始资料: 55 篇（`raw/sources/`）
- Wiki 页面: 95+（entity 18 + concept 17 + source 53 + synthesis 7 + meta pages）
- 全部已 Ingest
