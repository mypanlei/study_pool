---
title: "Specification-Driven Development (SDD)"
tags:
  - concept
  - methodology
  - development
  - spec
created: 2026-06-13
updated: 2026-06-21
aliases:
  - SDD
  - 规格驱动开发
  - Spec-Driven Development
---

# Specification-Driven Development (SDD)

> 把需求、设计、任务、原则持久化为中间件，让 AI 每一轮都围绕同一套工件工作的开发方法论。SDD 是对 Vibe Coding 的工程化约束和可复现化改造。

## 定义

SDD 的核心思路不是继续堆 prompt，而是将需求、设计、任务、原则这些中间产物持久化，让 AI 每一轮都围绕同一套工件工作。和普通「聊天式 coding agent」相比，SDD 通常多出 4 个关键特征：

1. **持久化工件**: 至少保留 requirements/spec, design, tasks 核心文档
2. **阶段化流程**: 先定义 what，再定义 how，最后才进入 implementation
3. **可重复上下文**: 新会话或新 agent 能重新加载工件，而不是依赖聊天历史
4. **可审查与可追踪**: 更适合团队协作、评审、合规和 brownfield 演进

## 开源生态

### 第一层：显式 SDD 框架

| 方案 | 定位 | 适合谁 |
|------|------|--------|
| **GitHub Spec Kit** | 「事实标准模板」SDD 工具包 | 想建立统一规范的工作流 |
| **Fission AI OpenSpec** | 轻量迭代的 SDD 框架 | 不想被重流程拖慢的团队 |
| **LeanSpec** | 把 spec 当独立数据层管理 | 已有 issue 流程想加 AI 层 |
| **specs.md** | 可切换不同严格度的框架 | 快节奏和高追溯并存的团队 |
| **Shotgun** | 代码库感知的 spec planner | 大型 brownfield 仓库 |

### 第二层：相邻谱系

- **MetaGPT**: 多代理软件公司范式，spec-aware 但核心是多角色协作
- **gpt-engineer**: 前 SDD 时代祖先项目（已归档）
- **OpenHands**: 强在执行层和 agent runtime，不是规格层

## 三层落地架构

```
规格层 (Spec Kit / OpenSpec / LeanSpec / specs.md)
  → 规划层 (Shotgun / MetaGPT)
    → 执行层 (OpenHands / Cursor / Claude Code / Copilot / Codex)
```

## 四步落地流程

JavaGuide 实践推荐的四步法：

| 阶段 | 干什么 | 产出 | 关键动作 |
|------|--------|------|----------|
| **Specify** | 产品定义 | `requirements.md` | 明确功能、用户、痛点，定"做什么" |
| **Plan** | 技术规划 | `design.md` | 定技术栈、架构、契约，定"怎么做" |
| **Tasks** | 任务拆解 | `tasks.md` | 拆成原子任务，写验收标准 |
| **Implement** | AI 执行 | — | AI 按 Spec 干活，人验收 |

### 三色标签权限控制

- ✅ **Always**：AI 自行决定，如代码检查/测试/格式化
- ⚠️ **Ask First**：需确认，如改 API 路由/数据库索引
- 🚫 **Never**：绝对禁止，如直连生产库/提交密钥

Never 规则需要多层防线（Spec 声明+配置模板+Pre-commit hook+AI IDE 配置），不能只靠文档约束。

### Spec 管理策略

- 10 模块以内：分文件存储，按领域拆
- 10-30 模块：摘要索引，目录+关键词
- 30 模块以上：RAG 向量检索
- 不分规模都管用：单会话单任务

## 相关概念

- [[wiki/concepts/vibe-coding]]：SDD 可以理解为对 Vibe Coding 的工程化约束
- [[wiki/concepts/harness-engineering]]：SDD 不是单纯 prompt engineering，而是把内容工件提升为 runtime contract

## 来源

- [[wiki/sources/spec-driven-development-overview]]
- [[wiki/sources/spec-coding-javaguide]] — JavaGuide Spec Coding 深度解析：四步流程、三色标签、多 Agent 协作
