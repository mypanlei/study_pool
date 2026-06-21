---
title: "Vibe Coding 实用技巧总结：Git、Spec、上下文管理与多 Agent 协作 — JavaGuide"
tags:
  - source
  - vibe-coding
  - javaguide
  - ai-coding
created: 2026-06-21
updated: 2026-06-21
source: "https://javaguide.cn/ai-coding/practices/the-cool-tricks-for-vibe-coding.html"
author: "Guide (JavaGuide)"
---

# Vibe Coding 实用技巧总结：Git、Spec、上下文管理与多 Agent 协作 — JavaGuide

> 结合 Git、Spec、Skills、上下文管理、多模型分工、测试验证和代码 Review，整理 Vibe Coding 在真实项目里更可控的用法。不花哨但很管用的实战经验。

## Core Contributions

1. **Git 是 Vibe Coding 最重要的技巧**：开工前先 `git status --short` 确认工作区干净，开单独分支（`git switch -c feat/xxx`），改完后 `git diff --stat` 看影响面再 `git add -p` 分块提交。并行任务用 `git worktree` 隔离——一个 Agent 一个目录、一个分支、一个任务。

2. **开工前把范围写窄**：轻量 Spec 比返工便宜得多。小任务写目标+约束+验收，中等任务补接口格式+错误码+表结构。更管用的一招：给 AI 看项目里写得好的代码作为样板。

3. **善用规则文件**：Claude Code→CLAUDE.md，Codex→AGENTS.md，Cursor→Project Rules。每次 AI 犯重复错误就补进规则文件，不要只在聊天里训它。规则文件随仓库走，聊天记录会散。

4. **善用 Skill 沉淀套路**：规则文件管"一直要遵守什么"，Skill 管"遇到某类任务时应该怎么做"。TDD、Code Review、前端设计、网页调研这些每次流程都差不多的任务，适合沉淀成 Skill。

5. **贵模型别拿来搬砖**：第一步让 Claude Opus 出方案（只讨论方案不写代码），第二步把 Task 丢给 DeepSeek V4-Pro/GLM5.1 等低价模型编码，第三步让 Opus Review diff。多模型分工降低成本。

6. **别听 AI 说修好了，看证据**：看三样东西——测试、命令输出、diff。先让测试失败再让实现通过。没跑就写"未运行"并说明原因，最怕没跑但写"已验证"。

7. **上下文管理三原则**：别把仓库一股脑塞进去（只带 Spec/相关文件/报错日志/验收命令）；长任务及时用 `/compact` 压缩；关键进展落到 `NOTES.md` 或 handoff 文档里。一个会话只处理一个任务。

8. **多 Agent 先串行再并行**：Plan Agent→Code Agent→Test Agent→Review Agent 按顺序串行提交（`[plan]`→`[code]`→`[test]`→`[review]`）。流程跑顺后再考虑 worktree 并行。

9. **权限控制不能只靠 Prompt**：用 Claude Code 的 `/permissions` 配置 allow/ask/deny，加 Hooks（PreToolUse 拦截危险命令）和 Sandbox（执行环境隔离）。高风险操作不能只靠一条命令黑名单兜底。

## Key Insights

- "Git 不是写完代码之后再补的仪式，它应该站在 AI 动手之前"
- "贵模型别拿来搬砖。这就像请了一个资深架构师，结果天天让他改字段名"
- "上下文窗口大不等于效果好——窗口能装更多东西，但模型能不能稳定找到重点是另一回事"
- "AI 写代码越快，Git、测试、Review、Spec 这些老东西越不能丢"

## Related Pages

- [[wiki/concepts/vibe-coding]] — Vibe Coding 概念页
- [[wiki/concepts/spec-driven-development]] — SDD/Spec Coding
- [[wiki/concepts/agent-skills-system]] — Agent Skills
- [[wiki/entities/claude-code]] — Claude Code
- [[wiki/sources/spec-coding-javaguide]] — Spec Coding 深度解析
- [[wiki/sources/ai-skills-recommendations-javaguide]] — Skills 推荐
