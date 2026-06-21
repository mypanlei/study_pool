---
title: "CLAUDE.md 最佳实践：该写什么、不该写什么、项目变大后怎么拆 — JavaGuide"
tags:
  - source
  - claudemd
  - javaguide
  - claude-code
created: 2026-06-21
updated: 2026-06-21
source: "https://javaguide.cn/ai-coding/practices/claude-md-best-practices.html"
author: "Guide (JavaGuide)"
---

# CLAUDE.md 最佳实践：该写什么、不该写什么、项目变大后怎么拆 — JavaGuide

> 系统梳理 CLAUDE.md 的写法规范：该写什么不该写什么、单文件 vs 拆分策略、.claude/rules 和 Auto Memory 怎么配合、日常维护方法。结合 Claude Code 官方文档与实战经验。

## Core Contributions

1. **CLAUDE.md 核心定位**：写给 Claude 看的"项目工作卡"，不是 README。判断标准：这行删掉后，Claude 会不会更容易犯错？如果会就保留，不会就是浪费上下文。

2. **CLAUDE.md vs 其他规则文件**：CLAUDE.md（Claude Code 专属行为规范）vs AGENTS.md（跨工具开放标准，可被 CLAUDE.md 导入复用）vs .claude/rules/（局部规则，带 paths 的规则按需加载）vs SPEC.md（需求规格，当次任务约束）。

3. **五类值得写的内容**：技术栈和版本信息（框架版本差异是 AI 犯错源头）、常用命令（代码块里的命令 Claude 更倾向于照着跑）、架构决策和背后的理由（光写规则不够，写清楚"为什么"能让 Claude 举一反三）、团队约定和项目特有的坑、当前任务的关键信息（当作持久化任务手册）。

4. **三类不该写的内容**：代码风格规则（交给格式化工具）、语言/框架默认行为、大段参考文档（放链接就够了）。

5. **层级结构**：组织级→用户级（`~/.claude/CLAUDE.md`）→项目级（`./CLAUDE.md`）→本地级（`CLAUDE.local.md`）→子目录级。越靠近当前项目优先级越高。

6. **单文件到分层的演进路径**：起步（一份文件几行核心规则）→拆分（主文件做路由，规则分文件，用 `@path/to/file` 引用）→按工作区域加载（`.claude/rules/` 用 frontmatter 做路径匹配）。警告：`@` 导入巨型文件会烧掉大量上下文预算。

7. **维护方法**：添加规则要慢（同类错误出现几次后再收敛成规则），删规则要果断（删掉后 Claude 行为不变说明规则无效）。两个预警信号：Claude 为已有规则道歉→措辞问题；同规则反复违反→文件太长需压缩。

8. **CLAUDE.md vs Auto Memory**：CLAUDE.md=主动写给 Claude 的长期指令（团队规范），Auto Memory=Claude Code 自动记忆机制（个人调试经验）。影响团队协作的写 CLAUDE.md，个人调试发现交给 Auto Memory。

## Key Insights

- "CLAUDE.md 最怕的不是少写两条规则，而是正确废话太多，把真正重要的规则淹掉"
- "一条规则如果没法机械化验证，Agent 迟早会偏离"
- "能用工具强制执行的规则，不要写成自然语言。CLAUDE.md 是软约束，Linter/Hook/CI 才是硬约束"
- "写清楚'为什么'能让 Claude 举一反三"

## Related Pages

- [[wiki/entities/claude-code]] — Claude Code 实体
- [[wiki/concepts/agent-skills-system]] — Agent Skills，Rules 的进阶形式
- [[wiki/sources/agent-skills-deep-dive-javaguide]] — Skills 深度解析
- [[wiki/sources/harness-engineering-javaguide]] — Harness Engineering
- [[wiki/sources/spec-coding-javaguide]] — Spec Coding
