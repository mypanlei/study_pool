---
title: Claude Code 自定义 Agent 配置指南
created_at: 2026-05-29
updated_at: 2026-05-29
tags: [Claude Code, Subagent, Agent, AI-Agent, Anthropic, 工具调用]
---

# Claude Code 自定义 Agent 配置指南

## 1. 核心结论

如果不使用 Cursor，而是使用 **Claude Code**，也可以创建自己的 Agent。Claude Code 中这类自定义 Agent 官方通常称为 **custom subagents**。

一句话理解：

```text
Claude Code 的自定义 Agent = 一个带 YAML frontmatter 的 Markdown 文件
```

它的作用是定义一个专门角色，让 Claude Code 在合适任务中自动或手动委派给它。

## 2. 创建方式

Claude Code 支持两种常见创建方式：

1. 使用 `/agents` 命令，通过交互界面创建。
2. 手动创建 Markdown 文件。

手动创建更适合版本管理和团队共享。

## 3. 文件位置

Claude Code 会扫描以下目录：

```text
项目级：.claude/agents/
用户级：~/.claude/agents/
```

区别：

| 类型 | 位置 | 作用范围 | 适合场景 |
|---|---|---|---|
| 项目级 Agent | `.claude/agents/` | 当前项目 | 项目专属审查、迁移、测试、架构规则 |
| 用户级 Agent | `~/.claude/agents/` | 所有项目 | 个人通用 reviewer、debugger、researcher |

如果同名 Agent 同时存在，项目级通常优先。

## 4. 最小示例

例如创建一个代码审查 Agent：

```text
.claude/agents/code-reviewer.md
```

内容：

```md
---
name: code-reviewer
description: Reviews code for quality, security, maintainability, and test coverage. Use after code changes.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer.

Your job is to review code changes independently.

When invoked:
1. Inspect the relevant changed files.
2. Focus on correctness, security, maintainability, and test coverage.
3. Identify concrete risks, not stylistic preferences.
4. Provide actionable suggestions.

Output format:
- Critical issues
- Warnings
- Suggestions
- Test gaps
- Overall assessment

Do not modify files unless explicitly asked.
```

## 5. 常用 frontmatter 字段

```yaml
---
name: code-reviewer
description: Reviews code for quality, security, maintainability, and test coverage. Use after code changes.
tools: Read, Grep, Glob, Bash
model: sonnet
---
```

常用字段：

| 字段 | 是否必需 | 作用 |
|---|---|---|
| `name` | 是 | Agent 的唯一名称，建议使用小写和短横线 |
| `description` | 是 | 说明什么时候应该调用这个 Agent，是自动路由的关键 |
| `tools` | 否 | 允许使用的工具列表；省略时通常继承主会话工具 |
| `disallowedTools` | 否 | 明确禁止某些工具 |
| `model` | 否 | 可指定 `sonnet`、`opus`、`haiku`、完整模型 ID 或 `inherit` |

`description` 非常重要。Claude Code 会根据它判断是否要把任务委派给这个 Agent。它应该写成触发条件，而不是泛泛的职位名称。

较弱写法：

```yaml
description: A helpful code reviewer.
```

较好写法：

```yaml
description: Reviews code for correctness, security, maintainability, and test coverage. Use after code changes.
```

## 6. 如何调用

### 6.1 自动调用

如果 `description` 写得清楚，Claude Code 可以根据任务自动选择合适的 subagent。

例如：

```text
请检查刚才的代码改动有没有安全和测试风险。
```

如果存在 `code-reviewer`，Claude Code 可能自动委派给它。

### 6.2 显式调用

也可以直接点名：

```text
Use the code-reviewer subagent to review these changes.
```

或中文：

```text
请使用 code-reviewer subagent 检查这次改动。
```

## 7. 工具权限设计

自定义 Agent 最好只给它完成任务所需的最小工具权限。

例如只读审查 Agent：

```yaml
tools: Read, Grep, Glob, Bash
```

如果不希望它运行命令，可以去掉 `Bash`：

```yaml
tools: Read, Grep, Glob
```

如果允许它编辑文件，再授予写入相关工具。原则是：

```text
审查类 Agent：默认只读
修复类 Agent：允许编辑和运行测试
研究类 Agent：允许搜索和读取
发布类 Agent：谨慎授予 Bash 和外部系统权限
```

## 8. 常见 Agent 模板

### 8.1 verifier

```md
---
name: verifier
description: Independently verifies whether completed work satisfies the request. Use after implementation.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a skeptical verifier.

Check whether the implementation satisfies the original request.

Focus on:
- Missing requirements
- Broken behavior
- Test coverage
- Risky assumptions
- Files that should have changed but did not

Do not modify files.
Return passed checks, failed checks, unverified areas, and remaining risks.
```

### 8.2 debugger

```md
---
name: debugger
description: Diagnoses difficult bugs using logs, stack traces, runtime evidence, and reproduction steps.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a systematic debugger.

Your job is to find root causes, not guess.

Workflow:
1. Restate the symptom.
2. List plausible hypotheses.
3. Gather evidence from code, logs, tests, and runtime behavior.
4. Eliminate unsupported hypotheses.
5. Identify the most likely root cause.
6. Recommend the smallest safe fix.

Do not make broad refactors.
```

### 8.3 security-auditor

```md
---
name: security-auditor
description: Reviews code for authentication, authorization, injection, secrets, data exposure, and unsafe defaults.
tools: Read, Grep, Glob
model: sonnet
---

You are a security auditor.

Focus on practical exploitable risks:
- Authentication bypass
- Authorization mistakes
- Injection vulnerabilities
- Secret leakage
- Unsafe deserialization
- Data exposure
- Insecure defaults

Return findings ordered by severity with evidence and remediation.
Do not modify files.
```

## 9. 与 Cursor 自定义 Agent 的关系

Claude Code 和 Cursor 的思路很接近：

| 维度 | Claude Code | Cursor |
|---|---|---|
| 自定义 Agent 名称 | custom subagents | custom subagents |
| 文件格式 | Markdown + YAML frontmatter | Markdown + YAML frontmatter |
| 项目级目录 | `.claude/agents/` | `.cursor/agents/` |
| 用户级目录 | `~/.claude/agents/` | `~/.cursor/agents/` |
| 触发方式 | 自动委派或显式指定 | 自动委派或显式指定 |
| 关键字段 | `name`、`description`、`tools`、`model` | `name`、`description`、`model`、`readonly` 等 |

核心差异主要是工具字段、权限字段和具体产品支持的配置项不同。

## 10. 最佳实践

1. **先从只读 Agent 开始**
   - 例如 reviewer、verifier、security-auditor。
   - 确认行为稳定后，再创建可写修复类 Agent。

2. **description 写触发条件**
   - 不要只写“代码审查专家”。
   - 要写“Use after code changes”这类触发语义。

3. **工具权限最小化**
   - 审查类 Agent 不要随便给写权限。
   - 发布类 Agent 不要默认给过宽的 Bash 和外部系统权限。

4. **输出格式固定**
   - 让 Agent 每次都用稳定结构输出。
   - 便于主 Agent 或用户快速消费。

5. **项目级 Agent 进入版本管理**
   - 团队共享 `.claude/agents/`。
   - 保证每个人使用同一套审查和开发规范。

## 11. 参考来源

- [Claude Code Docs: Create custom subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Docs: Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents)
- [[Cursor-Agent-vs-Skill-使用决策指南]]
- [[RAG-Skill-Agent-区别与联系]]

## Update History

- 2026-05-29: 初次创建，整理 Claude Code 中自定义 subagents 的位置、格式、字段、调用方式和模板。
