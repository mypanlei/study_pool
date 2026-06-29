---
title: "Claude Code 中实践 Harness Engineering — 实操指南"
tags:
  - synthesis
  - harness-engineering
  - claude-code
  - practice
  - guide
created: 2026-06-30
updated: 2026-06-30
aliases:
  - Claude Code Harness 实践
  - Claude Code 装具工程
  - Claude Code 工程化配置
---

# Claude Code 中实践 Harness Engineering — 实操指南

> **Agent = Model + Harness**。你用的模型是"大脑"，CLAUDE.md、MCP、Hooks、Permissions、Skills 这整套配置才是让大脑可靠运行的 Harness。本文按 Harness Engineering 六层架构，逐一映射到 Claude Code 的具体能力，并给出 P0/P1/P2 行动清单。

相关概念：[[wiki/concepts/harness-engineering]] · [[wiki/entities/claude-code]] · [[wiki/concepts/agent-skills-system]] · [[wiki/concepts/mcp-model-context-protocol]] · [[wiki/concepts/spec-driven-development]] · [[wiki/concepts/agents-md]]

---

## L1 信息边界层 — CLAUDE.md / AGENTS.md

**投入产出比最高的 P0 动作**。告诉 Claude Code 它是谁、在什么项目里、有什么规矩。

### CLAUDE.md（项目级 Harness 入口）

```markdown
# CLAUDE.md

## 技术栈
- Python 3.12, FastAPI, PostgreSQL 16, Redis
- 使用 SQLAlchemy 2.0 async + Alembic

## 架构规则
- 所有对外 API 必须经过 API Gateway，不可直连服务
- 数据库迁移必须新建文件，不可修改已有迁移
- 新功能必须附带单元测试 + 集成测试

## 常用命令
- `uv run pytest tests/` — 跑全部测试
- `uv run alembic upgrade head` — 迁移数据库
```

**三条关键原则**：

1. **能机械执行的不要写自然语言** — "跑 `ruff check`"比"代码风格要统一"有效 10 倍。"If it cannot be enforced mechanically, agents will deviate." — OpenAI
2. **同类错误出现几次后再抽象成规则**，不要一上来写几十条——正确废话太多会淹掉真正重要的规则
3. **测试命令写 exact 命令**，Claude Code 会照着跑而不是猜

**评判标准**：这行删掉后，Claude Code 会不会更容易犯错？如果会就保留，不会就是浪费上下文。

### AGENTS.md（跨工具开放标准）

AGENTS.md 的好处是**不绑 Claude Code**，换 Codex/Gemini/Cursor 也能用。适合团队级的角色定义。

```markdown
## 0. 角色定义
你是一名 senior backend engineer，严格遵循 TDD。

## 1. 工作流
1. 理解需求 → 2. 写测试 → 3. 实现 → 4. 验证 → 5. 提交

## 2. 边界
- ✅ Always: 测试、格式化、lint
- ⚠️ Ask: 改数据库索引、改 API 路由、改 CI 配置
- 🚫 Never: 改生产配置、提交密钥
```

详见 [[wiki/concepts/agents-md]]

---

## L2 工具系统层 — MCP / Skills

Claude Code 默认只有文件读写 + Shell 命令。通过 MCP Server 注入更多能力。

### MCP（垂直集成）

```bash
# 添加数据库查询 MCP
claude mcp add db-query -- npx @your-org/db-mcp

# 添加飞书文档 MCP
claude mcp add feishu -- uvx feishu-mcp
```

**推荐集成**：
- **数据库查询** → Claude Code 直接查 schema，不再靠猜
- **API 文档** → 接入内部 API 文档 MCP
- **代码搜索** → 对大型仓库特别有用

### Skills（可复用任务模板）

```markdown
---
name: add-api-endpoint
description: 新增 RESTful API 端点（路由 + 处理函数 + 测试 + 文档）
---

## 步骤
1. 在 `routes/` 下新建路由文件（遵循现有命名）
2. 在 `services/` 中实现业务逻辑
3. 在 `tests/` 中写 pytest 测试
4. 运行 `uv run pytest tests/` 确保通过
5. 更新 OpenAPI 文档
```

`claude skills link add-api-endpoint` 注入当前项目。

详见 [[wiki/concepts/agent-skills-system]] · [[wiki/sources/agent-skills-deep-dive-javaguide]]

---

## L3 执行编排层 — Hooks / Commands / Sub-agents

### Hooks（自动化门禁）

```json
// .claude/settings.json
{
  "hooks": {
    "PreCommit": "uv run ruff check --fix && uv run pytest tests/ -x --timeout=30",
    "PreRelease": "uv run pytest tests/ --cov=app --cov-fail-under=80"
  }
}
```

- `PreCommit` — **每次提交代码前**自动跑，失败则阻止提交
- `PreRelease` — 创建 PR/Release 前跑，适合端到端验证

### Commands（快捷入口）

```json
{
  "commands": {
    "test": "uv run pytest tests/ -v",
    "lint": "uv run ruff check .",
    "typecheck": "uv run pyright"
  }
}
```

Claude Code 会话中直接 `/test` 触发，节省 Claude 猜命令的上下文消耗。

### Sub-agents（专业化分工）

```
/agent create
```

创建专用 Agent，例如：
- **reviewer** — 只做代码审查，不给写权限
- **debugger** — 专注排查 bug
- **docs-writer** — 专门写文档

详见 [[wiki/sources/claude-code-custom-agent-guide]]

---

## L4 记忆与状态层 — Auto Memory / Context Resets

### Auto Memory

Claude Code 自动在 `~/.claude/memory/` 记录调试经验。你需要做的是：

- 当 Claude Code **反复犯同一类错误**时，显式告诉它"记住这个"
- 它会写入 Auto Memory，下次新对话自动加载

### Context Resets（关键技巧）

**现象**：回复变慢、开始犹豫、提前收工 → 上下文窗口快满了（Dex Horthy 发现 168K 上下文用到约 40% 时质量显著下降）。

**解决方案**：

```
1. 在当前对话要求 Claude Code 生成结构化交接文档
2. 新建对话
3. 在 CLAUDE.md / 首条 prompt 中加载交接文档
```

**交接文档模板**：

```markdown
## 当前状态
- 已完成：xxx
- 当前阶段：xxx
- 待做事项：xxx
- 关键决策：xxx（附理由）
- 未解决的问题：xxx
```

新对话的上下文窗口从头开始，不重复历史。详见 [[wiki/sources/harness-engineering-javaguide]] 的 "40% 阈值"章节。

---

## L5 评估与观测层 — 独立验证

### 机械约束优先

文档约束是软约束，Claude Code 总有一天会偏离。你需要**多层防线**：

| 层级 | 机制 | 强制力 |
|------|------|--------|
| L1 | CLAUDE.md 自然语言规则 | 软 |
| L2 | PreCommit Hook 自动脚本 | 中 |
| L3 | CI Pipeline 硬失败 | 硬 |
| L4 | 代码审查（人工/Sub-agent） | 硬 |

**自定义 Linter**：写 CLI 工具检查架构违规（如"禁止直连数据库"、"import 必须走 `@core/` 别名"），在 PreCommit 和 CI 中运行。

### 观测指标

- Token 消耗（`~/.claude/logs/`）
- Hook 通过率
- **Claude Code 生成代码被人工修改的比例** — 最有价值的间接质量指标

---

## L6 约束校验与恢复层 — 权限与容错

### 权限模型

| 模式 | 命令 | 适用场景 |
|------|------|----------|
| 只读 | `claude --allow-read` | Code Review |
| 写允许 | `claude --allow-write` | 纯编码，不需要执行 |
| 完全 | 默认 | 日常开发，每个高危命令弹确认 |

### 容错

Hooks 可加 fallback 机制：

```json
{
  "hooks": {
    "PreCommit": "uv run pytest tests/ -x || (echo 'auto-fix...' && uv run pytest tests/ --last-failed -x)"
  }
}
```

---

## 成熟度模型

参考 JavaGuide 提出的 Level 0-4：

| Level | 状态 | 特征 |
|-------|------|------|
| **L0** | 裸奔 | 无 CLAUDE.md，无 Hooks，全靠手写 prompt |
| **L1** | 基础约束 | 有 CLAUDE.md + PreCommit Hook |
| **L2** | 工具化 | + MCP 集成 + Skills + Commands |
| **L3** | 可观测 | + Context Resets + 自定义 Linter + 指标收集 |
| **L4** | 自适应 | + Sub-agent 分工 + 自动清理 + 成熟度自评 |

---

## P0 / P1 / P2 行动清单

| 优先级 | 做什么 | Claude Code 对应 | 预估投入 |
|--------|--------|-----------------|----------|
| **P0** | 写 CLAUDE.md | 项目根目录创建，5-15 条核心规则 | 30 min |
| | 写 AGENTS.md | 设定角色 / 边界 / Always / Ask / Never | 15 min |
| | 配置 PreCommit Hook | `settings.json` 加 lint + test | 10 min |
| | 建 3-5 个核心 Skills | 最频繁的任务模板化 | 1-2 h |
| **P1** | 分层上下文管理 | CLAUDE.md + `.claude/rules/` 按路径拆分 | 1 h |
| | MCP 工具集成 | 数据库 / API doc / 搜索 | 2-4 h |
| | PreRelease Hook | 端到端验证 + 覆盖率门禁 | 30 min |
| | Sub-agents 分工 | /agent create 创建 reviewer / debugger | 30 min |
| **P2** | Context Resets 流程 | 交接文档模板标准化 | 30 min |
| | 自定义 Linter | 架构违规检查 CLI 工具 | 4-8 h |
| | 可观测仪表盘 | Token / Hook 通过率 / 人工修改率 | 4-8 h |

> **一条终局原则**：每一层 Harness 都在编码一个"模型自己搞不定"的假设。模型在变强，这些假设需要定期重新测试——删掉某一层后 Claude Code 行为没变，说明那层已经不需要了。

---

## 相关来源

- [[wiki/concepts/harness-engineering]] — Harness Engineering 三层架构 + JavaGuide 六层架构
- [[wiki/entities/claude-code]] — Claude Code 实体与配置位置
- [[wiki/sources/harness-engineering-javaguide]] — JavaGuide 一文搞懂 Harness Engineering（P0/P1/P2、40% 阈值、五个团队案例）
- [[wiki/sources/claude-md-best-practices-javaguide]] — CLAUDE.md 最佳实践（五类该写/三类不该写/层级结构/维护方法）
- [[wiki/sources/claude-code-custom-agent-guide]] — Claude Code Subagent 创建指南
- [[wiki/sources/spec-coding-javaguide]] — Spec Coding 三色标签权限控制
- [[wiki/concepts/agents-md]] — AGENTS.md 规范（六大工程要素、三层边界模型）
- [[wiki/concepts/agent-skills-system]] — Agent Skills 系统
- [[wiki/concepts/mcp-model-context-protocol]] — MCP 协议
