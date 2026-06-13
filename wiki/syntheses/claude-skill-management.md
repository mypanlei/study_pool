---
title: "Claude Code Skill Management — 多 Repo 技能管理指南"
tags:
  - synthesis
  - claude
  - workflow
created: 2026-06-13
updated: 2026-06-13
---

# Claude Code Skill Management

> 如何在多个 Repo 之间管理自有 Skills + 从 Marketplace 下载的第三方 Skills

---

## 一、Claude Code 扩展机制概览

Claude Code 支持四种扩展类型，按复杂度递增排列：

| 类型 | 位置 | 用途 | 示例 |
|------|------|------|------|
| **Skill** | `.claude/skills/<name>/SKILL.md` | 可复用的任务指令，LLM 自动匹配触发 | `llm-wiki`、`tailored-resume-generator` |
| **Agent** | `.claude/agents/<name>.md` | 带角色设定的持久化代理 | `llm-wiki.md` |
| **Command** | `.claude/commands/<name>.md` | 斜杠命令 `/name`，用户显式调用 | `/review`、`/simplify` |
| **Hook** | `.claude/hooks/` + `settings.json` | 自动触发的生命周期回调 | pre-message, post-tool-use |

> **Skill 是最灵活的扩展形式**：可被 LLM 自动检测匹配，也可通过 `/skill` 显式调用。本文聚焦 Skill 管理。

---

## 二、配置层级与加载优先级

Claude Code 配置按**作用域**分为三层，优先级从高到低：

```
1. Project-level    .claude/settings.local.json    ← 最高优先级（.gitignore 中）
2. Project-level    .claude/settings.json          ← 项目专属配置
3. User-level       ~/.claude/settings.json        ← 全局默认（所有项目共享）
```

### 关键原则

- **User-level (`~/.claude/`)** — 放所有项目都通用的内容：API keys、全局模型设置、插件市场
- **Project-level (`.claude/` in repo)** — 放本项目专属的内容：Skills、Agents、Commands
- **Skills 目录不继承**：Project `.claude/skills/` 只对当前项目生效；User-level 没有 skills 目录

---

## 三、自有 Skills 的三种管理策略

### 策略 A：内嵌式（最简单）

直接把 SKILL.md 放在项目 `.claude/skills/<name>/` 下。

```
your-project/
├── .claude/
│   └── skills/
│       └── my-skill/
│           └── SKILL.md
└── ...
```

✅ 简单直接  
❌ 无法跨项目复用  
❌ 不适合下载的第三方 skill（污染项目结构）

### 策略 B：Symlink 式（推荐 — 你当前在 resume 项目中使用的模式）

将 Skills 集中存储在项目内的一个独立目录（如 `.agents/skills/`），然后在 `.claude/skills/` 中创建符号链接。

```
your-project/
├── .agents/
│   └── skills/
│       └── my-skill/
│           └── SKILL.md
├── .claude/
│   └── skills/
│       └── my-skill -> ../.agents/skills/my-skill   ← symlink
└── ...
```

✅ Skills 与 Claude 配置逻辑分离，结构清晰  
✅ Git 跟踪技能文件（symlink 本身不提交，但指向的目录提交）  
✅ 方便将来抽离为独立仓库

### 策略 C：独立仓库式（最灵活 — 适合团队/跨项目共享）

创建专门的 Skills 仓库，各项目通过 symlink 引用。

```
~/workspace/
├── my-skills/                         ← 独立仓库
│   └── skills/
│       ├── code-review/
│       ├── commit-message/
│       └── db-helper/
├── project-a/
│   └── .claude/skills/code-review -> ../../my-skills/skills/code-review
└── project-b/
    └── .claude/skills/db-helper -> ../../my-skills/skills/db-helper
```

✅ 一处维护，多处生效  
✅ 配合 Git submodule 可实现版本化管理  
❌ 路径管理稍复杂

### 策略 D：全局目录式（来自知乎实践 — 最简洁）

> **核心原则：Single Source of Truth**

所有 Skill 只存一个地方：`~/.claude/skills/`（全局目录），各项目通过 symlink 指向它。

```
~/.claude/skills/          ← 全局唯一来源（所有 Skill 实际存放在这里）
├── write-skill/
├── draw-skill/
├── code-review/
└── ...

~/workspace/
├── project-a/.claude/skills/ → ~/.claude/skills  (symlink 到全局)
├── project-b/.claude/skills/ → ~/.claude/skills  (symlink 到全局)
└── ...
```

✅ **Single Source of Truth** — 改了某个 Skill，所有项目同时生效  
✅ 跨工具（Cursor / Codex / Claude Code / OpenClaw）共享同一套  
✅ 配合 GitHub 私密仓库可实现跨电脑同步  
❌ `~/.claude/skills/` 默认不存在（需手动创建）  
❌ 所有项目共享全部 Skill（无法按项目精细化筛选）

> **同台电脑上的所有工具、所有项目读取同一份 Skill，再也不存在「项目 A 有但 B 没有」的问题。**

### 策略对比总结

| 维度 | 内嵌式 (A) | Symlink (B) | 独立仓库 (C) | 全局目录 (D) |
|------|-----------|-------------|-------------|-------------|
| 跨项目共享 | ❌ | ✅ 手动 | ✅ 自动 | ✅ 自动 |
| 版本管理 | 项目自带 | 项目 + 仓库 | 独立仓库 | 全局 + GitHub |
| 精细化控制 | ✅ 完全 | ✅ 按项目选 | ✅ 按项目选 | ❌ 全部共享 |
| 设置复杂度 | 最低 | 低 | 中 | 低 |
| 跨设备同步 | ❌ | ❌ | ✅ Git | ✅ GitHub |
| 适用场景 | 一次性项目 | 中型项目 | 团队/多项目 | 个人全栈 |

### 策略 E：Skills Manager 工具式（适合多 Agent / 多工具用户）

使用开源工具 [Skills Manager](https://github.com/xingkongliang/skills-manager) 进行可视化集中管理：

```
Skills Manager Central Library
├── Preset: Writing
│   ├── ai-writing-assistant
│   ├── blog-post-writer
│   └── content-digest
├── Preset: Frontend
│   └── ...
├── Preset: Research
│   └── ...
└── Sync → Claude Code / Codex / Cursor / Trae
```

✅ **Multi-tool sync** — 一次配置同步到多个 Agent 工具  
✅ **Presets** — 按任务组合保存，按需启用  
✅ **GUI + CLI** — 图形界面和命令行双模式  
✅ **Git backup** — 内置备份能力  
✅ **Tags & filters** — 标签筛选和搜索  
❌ 额外引入一个工具，增加学习成本  
❌ 不适合 Skill 少于 5 个的初学者

> **适用判断**：当你同时使用 2+ Agent 工具、拥有 5+ Skill 时，Skills Manager 比手动管理更高效。

---

## 五、跨设备同步方案

Skill 管理不只是「本地多项目共享」，还有「多台电脑同步」的问题。

### 方案 1：GitHub 私密仓库（推荐）

```
~/.claude/skills/ → github.com/yourname/all-skills (private repo)
```

新电脑只需 `git clone`，全部 Skill 恢复。

### 方案 2：分类仓库 + 公开分享

将 Skill 按领域拆分为多个公开仓库，方便分享：

| 仓库 | 领域 | 数量参考 |
|------|------|----------|
| write-skill | 写作 / 内容生产 | ~20 |
| draw-skill | 画图 / 设计 / 视觉 | ~13 |
| info-skill | 信息获取 / RSS / 爬虫 | ~14 |
| protodesign | 产品 / PM / 原型 | ~13 |

分类规则：按 Skill 名称和功能描述自动判断归属（写作类关键词如 article/topic/content/blog，画图类如 image/cover/illustration 等）。

### 方案 3：NAS + rsync（适合超大知识库）

当 Obsidian 知识库超过 GitHub 限制（100MB+ 或大量图片）时，使用 NAS + rsync 做定时同步。

---

## 六、元 Skill：用 Skill 管理 Skill

> 不只是用 AI 干活，而是用 AI 管理 AI 的能力。

创建一个 **skill-manage** Skill 来自动化整个管理流程：

1. 扫描 `~/.claude/skills/`，找出新增的 Skill
2. 按规则自动判断归属分类（写作/画图/信息/产品）
3. 复制到对应的分类公开仓库
4. 全量同步到私密备份仓库
5. 对所有仓库执行 `git commit + push`
6. 可选：触发 NAS 同步

**一句话触发，全流程自动化。**

## 四、Marketplace 第三方 Skills 的管理

Claude Code 官方插件市场安装在 `~/.claude/plugins/`，通过 npm 包管理。

### 你已经安装的官方 Marketplace

路径：`~/.claude/plugins/marketplaces/claude-plugins-official/`

这是通过 `npx @anthropic-ai/claude-code install-plugin` 拉取的官方市场。

### 已下载的第三方插件

| 插件 | Skills | 用途 |
|------|--------|------|
| `discord` | `access`, `configure` | Discord 集成 |
| `imessage` | `access`, `configure` | iMessage 集成 |
| `telegram` | `access`, `configure` | Telegram 集成 |
| `asana` | — | Asana 项目管理 |
| `context7` | — | 上下文管理 |
| `fakechat` | — | 模拟聊天 |
| `firebase` | — | Firebase 集成 |
| `github` | — | GitHub 集成 |
| `gitlab` | — | GitLab 集成 |
| `greptile` | — | 代码搜索 |
| `laravel-boost` | — | Laravel 增强 |
| `linear` | — | Linear 集成 |
| `playwright` | — | 浏览器自动化 |
| `serena` | — |  Serena 集成 |
| `terraform` | — | Terraform 集成 |

### 已安装的官方内置插件

| 插件 | Skills | 用途 |
|------|--------|------|
| `agent-sdk-dev` | `agent-sdk-verifier-py`, `agent-sdk-verifier-ts` | Agent SDK 开发 |
| `claude-code-setup` | `claude-automation-recommender` | 自动化推荐 |
| `claude-md-management` | `claude-md-improver` | CLAUDE.md 优化 |
| `code-review` | — | 代码审查 |
| `code-simplifier` | — | 代码简化 |
| `code-modernization` | — | 代码现代化 |
| `commit-commands` | — | 提交命令 |
| `cwc-makers` | `cardputer-buddy`, `m5-onboard` | CWC 开发 |
| `explanatory-output-style` | — | 解释型输出风格 |
| `feature-dev` | — | 特性开发 |
| `frontend-design` | `frontend-design` | 前端设计 |
| `hookify` | `writing-rules` | Hook 管理 |
| `learning-output-style` | — | 教学型输出风格 |
| `math-olympiad` | `math-olympiad` | 数学竞赛 |
| `mcp-server-dev` | `build-mcp-app`, `build-mcp-server`, `build-mcpb` | MCP 服务器开发 |
| `playground` | `playground` | 测试环境 |
| `plugin-dev` | `agent-development`, `command-development`, `hook-development`, `mcp-integration`, `plugin-settings`, `plugin-structure`, `skill-development` | 插件开发 |
| `pr-review-toolkit` | — | PR 审查工具包 |
| `ralph-loop` | — | 循环执行 |
| `security-guidance` | — | 安全指南 |
| `session-report` | `session-report` | 会话报告 |
| `skill-creator` | `skill-creator` | Skill 创建向导 |
| `LSP 插件` | — | 各语言的 LSP 支持（clangd, csharp, gopls, jdtls, kotlin, lua, php, pyright, ruby, rust-analyzer, swift, typescript 等） |

---

## 七、你的当前技能清单

### 你自建的 Skills

| Skill/Agent | 所在项目 | 类型 | 说明 |
|-------------|----------|------|------|
| `llm-wiki` | `study_pool` | Agent | LLM Wiki 知识库维护者 |
| `tailored-resume-generator` | `resume` | Skill | 简历定制优化 |

### 你拥有的 Repos（按是否启用 Claude Code 分类）

**已启用（有 `.claude` 配置）：**
- `study_pool` — 当前 vault，有 Agent: `llm-wiki`
- `resume` — 有 Skill: `tailored-resume-generator`（使用 symlink 策略）

**未启用（不含 `.claude` 配置）：**
- `ai_knowledge` — AI 知识库
- `my_knowledge` — 个人知识库
- `bdd` — BDD 相关
- `mleco` / `mleco1` — ML 相关
- `openclaw-overview` — OpenClaw 概览
- `wind-seeker` — 寻风项目

---

## 八、推荐的管理方案

基于你当前的实际情况，我推荐**分层管理策略**：

```
~/.claude/
├── settings.json                     ← 全局配置（API keys、模型等）
└── plugins/marketplaces/             ← 官方插件市场（npm 管理）

~/workspace/
├── study_pool/                       ← 主知识库 vault
│   └── .claude/
│       ├── agents/llm-wiki.md        ← Agent 配置
│       └── skills/                   ← （可选的 vault 专属 skills）
│
├── resume/
│   └── .claude/
│       └── skills/tailored-resume-generator → symlink to .agents/
│
├── my-skills/                        ← 【建议新建】集中式自有 Skills 仓库
│   ├── skills/
│   │   ├── llm-wiki-skill/           ← 通用版 LLM Wiki skill
│   │   ├── code-reviewer/
│   │   └── ...
│   └── .git
│
└── each-project/
    └── .claude/skills/<name> → ../../my-skills/skills/<name>
```

### 具体建议

1. **新建 `my-skills` 仓库** — 集中存储你所有自建 Skills，各项目通过 symlink 引用
2. **Marketplace 插件保持全局安装** — 它们已经安装在 `~/.claude/plugins/`，无需移到项目内
3. **每个项目的 `.claude/skills/` 只放 symlink** — 指向 `my-skills/` 或 `.agents/skills/`
4. **`.gitignore` 中排除 `.claude/settings.local.json`** — 保持密钥安全

### symlink 快速配置

```bash
# 在目标项目中启用一个 skill
cd ~/workspace/target-project
mkdir -p .claude/skills
ln -s ../../my-skills/skills/my-skill .claude/skills/my-skill
```

### Windows (PowerShell) symlink

```powershell
# 以管理员或启用开发者模式运行
New-Item -ItemType Junction -Path ".claude/skills/my-skill" -Target "../../my-skills/skills/my-skill"
```

---

## 九、Skill 与 Agent 的选择建议

| 场景 | 推荐类型 | 原因 |
|------|----------|------|
| 可复用的任务指令 | **Skill** | LLM 自动匹配，多项目共享方便 |
| 长期运行的维护角色 | **Agent** | 持久化上下文，有角色设定 |
| 用户显式触发的操作 | **Command** | `/command` 调用，精准触发 |
| 知识库维护 | **Agent** (如 `llm-wiki`) | 需要持续上下文和角色一致性 |
| 代码审查 | **Command** (`/review`) | 显式调用，不需要自动触发 |
| 代码简化/重构 | **Skill** | LLM 在合适时机自动建议 |

---

## 十、快速入门 Cheatsheet

```bash
# 1️⃣ 查看当前项目已注册的 skills
ls .claude/skills/

# 2️⃣ 查看全局插件市场
ls ~/.claude/plugins/marketplaces/claude-plugins-official/plugins/

# 3️⃣ 从市场安装插件
npx @anthropic-ai/claude-code install-plugin <plugin-name>

# 4️⃣ 创建新 skill
mkdir -p .claude/skills/my-skill
# 编辑 .claude/skills/my-skill/SKILL.md

# 5️⃣ 创建新 command
# 编辑 .claude/commands/my-command.md

# 6️⃣ 创建新 agent
# 编辑 .claude/agents/my-agent.md

# 7️⃣ 跨项目引用（symlink）
ln -s ../../central-skills-repo/skills/my-skill .claude/skills/my-skill
```

## 来源

- [[wiki/sources/llm-wiki-pattern]]
- [[wiki/sources/skill-management-zhihu]]
- [[wiki/entities/andrej-karpathy]]

## 相关页面

- [[wiki/concepts/llm-wiki-pattern]]
- [[wiki/concepts/rag-vs-wiki]]
