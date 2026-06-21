---
title: "Spec Coding 规范驱动编程实战：从 Vibe Coding 到 AI 代码规范 — JavaGuide"
tags:
  - source
  - spec-coding
  - javaguide
  - vibe-coding
created: 2026-06-21
updated: 2026-06-21
source: "https://javaguide.cn/ai-coding/practices/spec-coding.html"
author: "Guide (JavaGuide)"
---

# Spec Coding 规范驱动编程实战：从 Vibe Coding 到 AI 代码规范 — JavaGuide

> 系统梳理 Spec Coding 规范驱动编程的核心思路与落地流程：Vibe Coding 与 Spec Coding 的适用场景边界、四步落地方法、AI IDE 规范文件配置、三色标签权限控制、Spec 分层管理和多代理协作避坑经验。

## Core Contributions

1. **Vibe Coding vs Spec Coding 适用边界**：Vibe Coding 适合 2 天就扔的脚本/一次性 Demo/内部小工具；3-5 天的中间地带写轻量 Spec；超过一周的代码必须写 Spec。判断标准：这段代码要活多久？

2. **四步落地流程**：Specify（`requirements.md`，产品定义"做什么"）→ Plan（`design.md`，技术规划"怎么做"）→ Tasks（`tasks.md`，原子任务+验收标准）→ Implement（AI 按 Spec 执行+人验收）。核心：先写清楚边界，再让 AI 执行，AI 乱猜的空间会小很多。

3. **三色标签权限控制**：✅ Always（AI 自行决定，如代码检查/测试/格式化）、⚠️ Ask First（需确认，如改 API 路由/数据库索引）、🚫 Never（绝对禁止，如直连生产库/提交密钥）。Never 规则需要多层防线（Spec 声明+配置模板+Pre-commit hook+AI IDE 配置）。

4. **Spec 分层管理策略**：10 模块以内→分文件存储（按 global/backend/frontend/shared 拆），10-30 模块→摘要索引（目录+关键词），30 模块以上→RAG 向量检索（text-embedding-3-small+Chroma/Pinecone/Milvus）。不分规模都管用的一条：单会话单任务。

5. **领域知识与自检清单**：业务规则、技术约束、历史债务、性能基线——AI 训练数据再多也不知道你项目特定的规则。完成自检清单：每完成任务，AI 必须逐项确认验收标准，不能只说"已完成"。

6. **多代理协作模式**：串行同分支（推荐起步，三个代理按顺序 commit，前缀区分角色）和链式继承（从上一代理分支 checkout）。翻车场景：死锁（确保依赖是 DAG）、无限循环（设最大轮次）、输出格式错误（加校验和重试）。

7. **主流 AI IDE 规范文件配置对比**：Cursor（`.cursor/rules/*.mdc`）、Claude Code（`CLAUDE.md`）、GitHub Copilot（`.github/copilot-instructions.md`）、Windsurf（`.windsurfrules`）、Aider（`CONVENTIONS.md`）。

8. **Spec 持续迭代原则**：渐进细化（先写高层大纲再一个模块一个模块补）、模块化组织（API/数据库/样式/错误码/权限各一个文件）、持续迭代（每次 CR 发现问题和 AI 反复踩坑就回去改 Spec）。

## Key Insights

- "Vibe Coding 不是不能用，关键是这段代码要活多久"
- "AI 写出来的屎山代码，谁来维护？"
- "AI 的行为是由你定义的，还是由它猜的？——这就是 Spec Coding 和 Vibe Coding 的根本区别"
- "Spec 定的是边界，不是逐行伪代码"
- "那个合并按钮，永远应该握在你自己手里"

## Related Pages

- [[wiki/concepts/spec-driven-development]] — SDD 概念页
- [[wiki/concepts/vibe-coding]] — Vibe Coding 概念
- [[wiki/entities/claude-code]] — Claude Code
- [[wiki/sources/vibe-coding-tips-javaguide]] — Vibe Coding 实用技巧
- [[wiki/sources/agent-skills-deep-dive-javaguide]] — Skills 深度解析
