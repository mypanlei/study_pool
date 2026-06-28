---
title: "Specification-Driven Development (SDD)"
tags:
  - concept
  - methodology
  - development
  - spec
created: 2026-06-13
updated: 2026-06-29
aliases:
  - SDD
  - 规格驱动开发
  - Spec-Driven Development
  - Spec Driven Development
---

# Specification-Driven Development (SDD)

> 把需求、设计、任务、原则持久化为可执行契约（executable contracts），让 AI Agent 从中推导代码，CI 管线自动验证——而非仅作为人类阅读的被动文档。SDD 是对 Vibe Coding 的工程化约束和可复现化改造。

## 定义

SDD 的核心思路不是继续堆 prompt，而是将需求、设计、任务、原则这些中间产物持久化，让 AI 每一轮都围绕同一套工件工作。和普通「聊天式 coding agent」相比，SDD 通常多出 4 个关键特征：

1. **持久化工件**: 至少保留 requirements/spec, design, tasks 核心文档
2. **阶段化流程**: 先定义 what，再定义 how，最后才进入 implementation
3. **可重复上下文**: 新会话或新 agent 能重新加载工件，而不是依赖聊天历史
4. **可审查与可追踪**: 更适合团队协作、评审、合规和 brownfield 演进

## Why SDD Matters Now

2025-2026 三大合力使 SDD 成为 AI 生成代码落生产的必要前提：

- **AI 代码漏洞率高企**：LLM 生成代码的漏洞率在 9.8%-42.1% 之间（Yan et al., 2025）。SonarQube 分析五个 LLM 生成的 Java 代码发现，Llama 3.2 90B 超过 70% 的检测漏洞为 BLOCKER 级别。到 2026 年 2 月，已有超过 11 万 AI 引入的问题存活在生产仓库中（arXiv, 2026）。单元测试验证个体函数，无法捕获架构违规、API 契约漂移或跨服务安全反模式——SDD 规格在系统级运行。
- **合规要求将规格视为证据**：EU AI Act 对高风险 AI 系统的合规义务从 2026 年 8 月 2 日起生效，不合规最高罚款 €15M 或全球年营收的 3%。
- **分布式架构需要正式治理**：Deloitte State of AI 2026 报告仅 1/5 企业具备成熟的自主 AI Agent 治理模型。

## 六要素框架（Six-Element Framework）

一个好的 Spec 必须回答六个问题。遗漏任何一项，Agent 都会用自己的假设填补：

1. **成果（Outcomes）** — 不是"构建一个认证流"，而是"用户可以用邮箱+密码注册、收到验证邮件、无错误登录。会话跨页面刷新保持。"
2. **范围边界（Scope）** — In-scope 和 explicitly out-of-scope 同等重要。"OAuth 不属于此任务范围"对 Agent 来说不是显而易见的。
3. **约束与假设（Constraints）** — 技术栈决策、第三方 API 限制、性能要求。结合 [[wiki/concepts/agent-skills-system|AGENTS.md]] 文件可以给 Agent 持久的项目上下文。
4. **已做决策（Prior Decisions）** — 如果已选定数据库 schema 或加密库，明确写出。不知道决策已做出的 Agent 会自己做决定。
5. **任务分解（Task Breakdown）** — 一次性要求太多是 AI 最大的失败模式之一。拆分为离散子任务，让多个 Agent 可以独立验证、并行执行。
6. **验证标准（Verification Criteria）** — 不是"能工作就行"，而是什么测试通过、哪些边界情况被处理。对抗性 Agent 模式中，这是 Verifier 的检查依据。

## SDD vs TDD / BDD / Vibe Coding

| 维度 | TDD | BDD | Vibe Coding | SDD |
|------|-----|-----|-------------|-----|
| 主要产物 | 单元测试 | Given-When-Then 场景 | 自然语言提示 | 可执行规格（Executable Specifications） |
| 范围 | 个体函数正确性 | 跨功能行为 | 全应用生成 | 系统级架构契约 |
| 验证机制 | 自动化测试套件 | 人工参考文档 | 人工评审（如果有） | Build 失败于规格偏离 |
| AI 治理 | 无内置 | 无内置 | 无内置 | 宪法约束和检查点 |
| 真理所在 | 测试套件 | 工作坊产物 | Prompt 历史 | 版本化的规格文档 |

SDD 不是在替换 TDD/BDD——而是在架构层之上叠加规格治理。TDD 保留给实现验证，BDD 场景可以嵌入 SDD 作为可执行验证门。

## 三种落地模式

| 模式 | 规格角色 | 代码角色 | 适用场景 |
|------|----------|----------|----------|
| **Spec-First** | 引导和约束 AI 输出 | 主要交付物 | 团队开始采用 SDD |
| **Spec-Anchored** | 通过检查点和宪法约束治理 | 可验证交付物 | 企业团队需要审计线索 |
| **Spec-as-Source** | 字面意义的源码 | 生成的产物 | API 优先领域，工具链成熟 |

**Spec-First**：规格先于代码，约束 AI Agent 生成。代码仍是主要交付物。大多数团队从此模式起步。

**Spec-Anchored**：添加治理层、宪法约束（constitutional constraints）和监督检查点。当监管合规需要审计线索、多团队跨服务协调、AI 生成代码需要人工审批时使用。arXiv 2026 年 2 月的《Constitutional SDD》论文将其形式化，嵌入了含 CWE 漏洞映射的安全约束。

**Spec-as-Source**：规格字面意义上成为源码。ThoughtWorks 技术雷达（Vol.33, 2025）将其列为 "Assess" 阶段，并警告"过度前期规格和 big-bang 发布"的反模式。

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

## 对抗性 Agent 模式（Adversarial Agent Pattern）

SDD 中最被低估的模式：分配一个独立的 Agent 来检查工作，而非信任实现 Agent 的自我验证。

**结构**：Coordinator 拆解 Spec 并委派任务给 Implementor 子 Agent → 每个 Implementor 从自己的子 Spec 工作 → Verifier Agent 在标记完成前对照 Spec 检查输出。

**关键设计**：Implementor 和 Verifier 目标对立。一个优化完成任务，另一个优化发现失败。这种对立迫使 Spec 必须包含显式的验证标准——这反过来提升了 Spec 本身的质量。

**如何运作**：
- Sub-agent 实时更新 Spec 进度 → Coordinator 始终掌握当前状态
- 多个 Implementor 可同时运行（如各自在独立 git worktree 中工作）
- Verifier 在合并前捕获冲突

**实践案例**：一个 10 页产品网站，Figma MCP 连到 Coordinator 读取设计系统 → Coord 按页分解（每页含接收标准/组件需求/布局约束） → 并行 Agent 在隔离 Worktree 执行 → Verifier 检查 → 项目约 45 分钟达 95% 完成度。剩余 5% 由设计师（无 Git 经验）直接通过 Intent 平台迭代。

## 模型分层（Model Tiering）

Coordinator/Implementor/Verifier 模式允许为不同角色分配不同模型：

- **写 Spec** — 用最贵/最强的模型。Spec 中的错误会向下游传播，在这里省钱是最大的浪费。
- **实现** — 中档模型（Sonnet-class, GPT-5.1-Codex），适度思考。Spec 扎实后不需要最贵的模型来执行。
- **验证** — 快速模型，注重准确性和低成本，不需要深度推理。

分配搞反（便宜模型写 Spec，贵模型实现）会在修正循环中消耗比分层节省更多的成本。

## 棕地采纳（Brownfield SDD）

对现有代码库应用 SDD 与绿地开发有本质不同，分三阶段：

**Phase 1：重构现有行为** — AI 辅助逆向工程。从可见工件（UI 元素、二进制、数据血缘）开始，增量丰富，保持可追溯性。

**Phase 2：只对变更区域写 Spec** — 不要试图 retroactively 为整个系统写 Spec。"Spec 在靠近变更区域时最细粒度。"每个 bug 修复或功能添加都成为对触及代码添加规格的机会。

**Phase 3：增量式 CI 执行** — 防止 drift 积累比定期调和已分歧的规格更务实。

如 InfoQ 所指出："SDD 不消除复杂性，只是重新定位它。"规格继承源码的所有属性：技术债务、跨团队耦合、架构引力。

## 何时跳过 Spec

Spec 开销是真实成本，不是每个任务都需要：

| 写 Spec 时 | 跳过 Spec 时 |
|-----------|-------------|
| 工作跨多个 Agent 会话 | 工作是探索性或实验性的 |
| 涉及多个服务或仓库 | 单次 Prompt 能产出可用的输出 |
| 错误解释的纠正成本高 | 输出可在 5 分钟内审完 |
| 需要合规或审计线索 | 原型是一次性的 |
| 需要真实注意力的评审（组件逻辑、端到端流） | 变更是机械性或低风险的 |

触发判断：如果 Agent 以不同于你意图的方式解释需求会让你恼怒，就写 Spec。如果能在快速跟进 Prompt 中修好输出，就跳过。

## 开源生态

### 第一层：显式 SDD 框架

| 方案 | 定位 | 适合谁 |
|------|------|--------|
| **GitHub Spec Kit** | 「事实标准模板」SDD 工具包（88k stars, 129 releases, 支持 28 个 AI Agent 平台） | 想建立统一规范的工作流 |
| **Fission AI OpenSpec** | 轻量迭代的 SDD 框架 | 不想被重流程拖慢的团队 |
| **LeanSpec** | 把 spec 当独立数据层管理 | 已有 issue 流程想加 AI 层 |
| **specs.md** | 可切换不同严格度的框架 | 快节奏和高追溯并存的团队 |
| **Shotgun** | 代码库感知的 spec planner | 大型 brownfield 仓库 |

### 第二层：相邻谱系

- **MetaGPT**: 多代理软件公司范式，spec-aware 但核心是多角色协作
- **gpt-engineer**: 前 SDD 时代祖先项目（已归档）
- **OpenHands**: 强在执行层和 agent runtime，不是规格层

### SDD 工具对比

| 工具 | Spec 格式 | CI/CD 执行 | AI Agent 兼容 | 最佳场景 |
|------|-----------|-----------|---------------|----------|
| GitHub Spec Kit | Markdown/结构化 | 通过 Agent 工作流 | 28 平台 | SDD 工作流采用 |
| SwaggerHub / API Hub | OpenAPI, AsyncAPI | CLI + Git 集成 | MCP Server | API 优先团队生命周期管理 |
| Postman Spec Hub | OpenAPI, 多协议 | GitHub sync, CI runner | MCP servers; Claude 插件 | 全 API 生命周期 + 治理 |
| Spectral | OpenAPI, AsyncAPI, JSON Schema | CLI 退出码 | 间接 | API 风格检查与标准执行 |
| PactFlow | Pact + OpenAPI | can-i-deploy 门 | 部分 | 跨服务契约测试 |
| Specmatic | OpenAPI（可执行） | 是 | Agent-ready | 可执行 API 契约执行 |
| TypeSpec | TypeSpec → OpenAPI | 通过下游工具链 | 是（生成 OpenAPI） | Azure/微软生态 |

**企业级扩展**：Intent's Context Engine 通过处理 400,000+ 文件的语义依赖图分析，解决"工具通常将 Spec 与代码保持在单仓库中"的限制（InfoQ, 2026），实现多仓库协调。Intent 持有 SOC 2 Type II 和 ISO/IEC 42001 认证，是首个获得 ISO/IEC 42001 的 AI 编码助手。

## 三层落地架构

```
规格层 (Spec Kit / OpenSpec / LeanSpec / specs.md)
  → 规划层 (Shotgun / MetaGPT)
    → 执行层 (OpenHands / Cursor / Claude Code / Copilot / Codex)
```

## 相关概念

- [[wiki/concepts/vibe-coding]]：SDD 可以理解为对 Vibe Coding 的工程化约束
- [[wiki/concepts/harness-engineering]]：SDD 不是单纯 prompt engineering，而是把内容工件提升为 runtime contract。对抗性 Agent 的 Verifier 角色与 Harness 的监督层直接对应
- [[wiki/concepts/agent-skills-system]]：AGENTS.md 文件作为 Spec 的持久项目上下文
- [[wiki/concepts/guardrails]]：Spec-Anchored 模式中的宪法约束（constitutional constraints）是 Guardrails 的一种实现

## 来源

- [[wiki/sources/spec-driven-development-overview]] — SDD 开源生态全景（自建笔记，2026-06-13）
- [[wiki/sources/spec-coding-javaguide]] — JavaGuide Spec Coding 深度解析：四步流程、三色标签、多 Agent 协作
- [[wiki/sources/spec-driven-development-complete-guide]] — Augment Code SDD 完全指南：六要素框架、对抗性 Agent 模式、模型分层、棕地采纳（Molisha Shah, 2026-04-23）
