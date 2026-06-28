---
title: "Using spec-driven development with Claude Code — Heeki Park"
tags:
  - source
  - spec-driven
  - claude
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://heeki.medium.com/using-spec-driven-development-with-claude-code-4a1ebe5d9f29"
source_author: "Heeki Park"
source_date: 2026-03-01
aliases:
  - SDD with Claude Code Practical Guide
---

# Using spec-driven development with Claude Code — Heeki Park

> Heeki Park（AWS 解决方案架构师）分享的 SDD + Claude Code 实践经验。核心论点：花更多时间在规划阶段、结构化的需求文档 + 分阶段构建 + 持续更新规范 = 更好的 AI 输出。

## 核心论点

1. **规划为王**：花大量时间在规划阶段，提前定义和记录需求，能带来更好的输出和更少的挫败体验。SDD 是对 Vibe Coding 的刹车。

2. **三层 SDD 实践**（引用 Birgitta Böckeler）：
   - **Spec-First**：先写好规范再用 AI 开发（最常用）
   - **Spec-Anchored**：任务完成后持续维护规范（"规范永不落灰"）
   - **Spec-as-Source**：人只编辑规范，从不碰代码（最极致）
   - 常见陷阱：Spec-Once（规范启动项目后被遗忘）——需要持续回访规范才能接近 Spec-Anchored

3. **Claude Code 实战技巧**：
   - 200k 上下文窗口对多数项目足够，压缩过程约 3-12 分钟
   - Opus 比 Sonnet 更快耗尽订阅计划配额（Sonnet 可连续使用数小时无限制）
   - 要求 Claude Code 主动提问澄清，并用可选项简化响应（减少来回沟通成本）
   - 信任度随时间增长，但慎用 `--dangerously-skip-permissions`
   - 使用 `tmux` 运行多个并行 Claude Code 会话
   - 基于 Bedrock 运行时效果良好（支持 1m token 上下文，需 beta header）

4. **分阶段构建**：将项目拆分为多个 Stack/Phase，每阶段可独立测试。AWS 示例：Interceptor（Lambda）→ MCP Server on AgentCore Runtime → Gateway 资源配置 → Interceptor 集成。

5. **教训**：
   - 前置规划时间对实现效率和输出质量有复利效应
   - 小、易测试的块逐步构建
   - 尽早构建安全层（OAuth AuthorizerType 不可原地修改，需整栈替换）
   - 定期回访和更新文档——每次修正设计时同步更新规范

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — 新增三层 SDD 实践视角、Spec-Once 概念、Claude Code 实战经验
