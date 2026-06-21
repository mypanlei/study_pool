---
title: "AI 编程必备 Skills 推荐：TDD、代码审查与网页自动化实战 — JavaGuide"
tags:
  - source
  - ai-skills
  - javaguide
  - claude-code
created: 2026-06-21
updated: 2026-06-21
source: "https://javaguide.cn/ai-coding/practices/programmer-essential-skills.html"
author: "Guide (JavaGuide)"
---

# AI 编程必备 Skills 推荐：TDD、代码审查与网页自动化实战 — JavaGuide

> 实战分享 6 个实用的 AI 编程 Skills 工具，覆盖 TDD 开发流程、代码审查、UI 设计、网页自动化与 Skill 开发场景。

## Core Contributions

1. **Superpowers** — 专为 Claude Code/Cursor 等设计的软件开发工作流框架，内置 9 个核心技能串联成完整工作流：brainstorming（苏格拉底式需求澄清）→ using-git-worktrees（隔离分支）→ writing-plans（拆解成 2-5 分钟小任务）→ executing-plans / subagent-driven-development → test-driven-development（红-绿-重构）→ code-review（双阶段审查）→ systematic-debugging → verification-before-completion。

2. **Everything Claude Code** — 开源配置集（GitHub 近 4w Star），把开发流程拆解成 Agents/Skills/Hooks/Rules/Commands 五大组件。实测让功能开发速度提升 65%，PR 平均问题数从 12 降到 3。核心价值：解决 AI "上下文腐化"问题——让 AI 在清晰的角色框架内工作，保持稳定输出。

3. **UI UX Pro Max** — 专业 UI/UX 设计 Skill，内置 67 种 UI 风格、161 个行业色板、57 种字体搭配、161 条推理规则。不是随便生成紫色渐变，而是根据产品类型和行业特性推理出合理的完整设计系统。

4. **sanyuan-skills** — 生产环境代码审查技能集合，核心是 Code Review Expert（SOLID/安全/性能/错误处理全方位审查），附带 Sigma（1 对 1 AI 导师）和 Skill Forge（元技能，创建高质量 Skill 的起点）。

5. **Web Access** — 让 Claude Code 能自主浏览网页并操作动态页面的 Skill。支持自动工具选择（WebSearch/WebFetch/curl/Jina/CDP 自由组合）、CDP 浏览器操作（直连日常 Chrome 携带登录态）、并行分治（多个子 Agent 共用一个 Proxy）、站点经验积累（按域名存储操作经验跨会话复用）。

6. **skill-creator** — Anthropic 官方元 Skill，提供意图捕获→起草 SKILL.md→测试验证→迭代优化→描述优化的完整 Skill 开发工作流，内置评估系统可对比"有 Skill vs 无 Skill"的输出差异。

## Key Insights

- "Superpowers 把 TDD + Code Review + Spec-Driven + Git Worktree + 子 Agent 协作等实践封装成 Skills，安装即用"
- "Everything Claude Code 解决 AI 聊太久会'失忆'的上下文腐化问题"
- "UI UX Pro Max 不是随便给你一套紫色渐变，而是推理出健康养生行业→柔和的 Soft UI→淡粉+鼠尾草绿+金色点缀"

## Related Pages

- [[wiki/concepts/agent-skills-system]] — Agent Skills 概念页
- [[wiki/entities/claude-code]] — Claude Code 实体
- [[wiki/sources/agent-skills-deep-dive-javaguide]] — Skills 深度解析
- [[wiki/sources/skills-tutorial]] — Skills 教程
- [[wiki/syntheses/claude-skill-management]] — Skill 管理指南
