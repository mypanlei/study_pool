---
title: Specification-Driven AI Development 开源方案综述
created_at: 2026-06-09
updated_at: 2026-06-09
tags: [AI-Agent, Spec-Driven-Development, SDD, Open-Source, AI-Native-Engineering]
---

# Specification-Driven AI Development 开源方案综述

## 1. 结论速览

有，而且到 2025-2026 年，已经出现了一批明确把自己定义为 **Spec-Driven Development, SDD** 的开源项目。

如果只看“明确自称 SDD、开源可用、已有一定生态和方法论沉淀”的方案，当前最值得重点关注的是下面五类：

| 方案 | 定位判断 | 适合谁 |
| --- | --- | --- |
| GitHub Spec Kit | 当前最像“事实标准模板”的 SDD 工具包 | 想建立统一规范、统一产物、统一 agent 工作流的团队 |
| Fission AI OpenSpec | 更轻、更强调迭代和 brownfield 的 SDD 框架 | 不想被重流程拖慢，但又不想回到纯聊天式开发的团队 |
| LeanSpec | 把 spec 当成独立后端和数据层来管理 | 已有 GitHub Issues、ADO、Jira、Markdown 流程，想加 AI 层而不想推翻原流程 |
| specs.md | 可切换不同严格度的 AI-native 开发框架 | 需要在“快速交付”和“全链路可追溯”之间切换的团队 |
| Shotgun | 代码库感知的 spec planner 和 staged PR orchestrator | 大型 brownfield 仓库、希望先理解代码再分阶段实施的团队 |

从生态成熟度看，**GitHub Spec Kit** 和 **OpenSpec** 是当前“显式 spec-driven AI development”里辨识度最高的两条主线。

### 1.1 横向对比表

如果你更关心“怎么选”，可以先看这张表：

| 方案 | 流程严格度 | Brownfield 友好度 | 对现有项目管理流程的兼容性 | 团队治理能力 | 上手门槛 | 最适合的场景 |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub Spec Kit | 高 | 中 | 中 | 高 | 中高 | 想建立统一模板、质量门和组织级 AI 开发规范 |
| OpenSpec | 中 | 高 | 中 | 中 | 低中 | 需要轻量迭代、又不想回到纯 prompt 开发 |
| LeanSpec | 中 | 中高 | 高 | 中高 | 中 | 已有 GitHub Issues、ADO、Markdown 流程，想叠加 AI 层 |
| specs.md | 可变 | 高 | 中 | 高 | 中高 | 既有快节奏项目，也有高追溯或 DDD 项目 |
| Shotgun | 中高 | 很高 | 中 | 中 | 中 | 大型旧仓库、复杂特性、迁移和 staged PR 规划 |

再进一步压缩成一句话：

- 要组织级标准化，选 Spec Kit。
- 要轻量 spec layer，选 OpenSpec。
- 要兼容现有 issue/work item 体系，选 LeanSpec。
- 要按项目复杂度切换严格度，选 specs.md。
- 要先读懂旧仓库再拆阶段交付，选 Shotgun。

## 2. 它到底解决什么问题

这类方案本质上是在解决一个很现实的问题：

> AI 编码助手在小改动上很好用，但一旦任务跨多个文件、涉及架构决策、上下文多轮漂移，就很容易偏离目标。

它们的共同思路不是继续堆 prompt，而是把需求、设计、任务、原则这些中间产物持久化，让 AI 每一轮都围绕同一套工件工作。

```mermaid
flowchart LR
  A[用户意图] --> B[澄清需求]
  B --> C[规格文档]
  C --> D[技术设计]
  D --> E[任务分解]
  E --> F[实现执行]
  F --> G[验证回归]
  G --> H[归档更新]
  H --> C
```

和普通“聊天式 coding agent”相比，SDD 方案通常会多出 4 个关键特征：

- 持久化工件：至少保留 `requirements/spec`, `design`, `tasks` 这一组核心文档。
- 阶段化流程：先定义 what，再定义 how，最后才进入 implementation。
- 可重复上下文：新会话或新 agent 能重新加载工件，而不是依赖聊天历史。
- 可审查与可追踪：更适合团队协作、评审、合规和 brownfield 演进。

## 3. 开源生态分层

### 3.1 第一层：显式 SDD 框架

#### 3.1.1 GitHub Spec Kit

- 仓库：<https://github.com/github/spec-kit>
- 开源协议：MIT
- 公开定位：open source toolkit for Spec-Driven Development
- 代表工作流：`/speckit.constitution` -> `/speckit.specify` -> `/speckit.plan` -> `/speckit.tasks` -> `/speckit.implement`
- 核心工件：项目原则、需求规格、技术计划、任务清单、实现结果
- 特点：支持 30+ AI coding agents，并提供 extension 和 preset 机制来扩展命令和改写模板

判断：

Spec Kit 最大的价值不是“能生成几个 markdown 文件”，而是它把 **spec、plan、tasks、checklist、analyze** 这些阶段做成了较完整的方法学，并且开始形成插件生态。它更像是“AI 时代的软件工程脚手架”。

适合：

- 想给团队建立统一 AI 开发流程的人
- 想让不同 agent 共用同一套开发契约的人
- 想把组织原则、合规要求、测试要求前置写入流程的人

代价：

- 相对偏重，文档和步骤更多
- 更适合愿意接受流程约束的团队，而不是极简个人流

#### 3.1.2 Fission AI OpenSpec

- 仓库：<https://github.com/Fission-AI/OpenSpec>
- 开源协议：MIT
- 公开定位：Spec-driven development for AI coding assistants
- 代表工作流：`/opsx:propose` -> `/opsx:apply` -> `/opsx:archive`
- 核心工件：`proposal.md`、`specs/`、`design.md`、`tasks.md`
- 特点：强调 fluid not rigid、iterative not waterfall、brownfield first

判断：

OpenSpec 是目前最典型的 **轻量化 SDD** 路线。它不是要把每个阶段都做成很重的 gate，而是保留 spec layer，让团队先对齐，再实施，再归档。和 Spec Kit 相比，它更强调“能随时回改工件、不要僵化瀑布”。

适合：

- 已有代码库上持续加功能的团队
- 不想把 SDD 弄成重 PM 流程的工程团队
- 希望把 spec 和 implementation 放在同一个仓库节奏里迭代的人

代价：

- 规范性不如 Spec Kit 那么强
- 如果团队需要统一企业模板、复杂治理和强制质量门，可能还要二次封装

#### 3.1.3 LeanSpec

- 仓库：<https://github.com/codervisor/leanspec>
- 开源协议：MIT
- 公开定位：tool-agnostic spec framework
- 关键能力：Markdown provider、MCP、CLI、Web UI、Board、Stats
- 核心思想：spec 后端可替换，既可以是本地 `specs/`，也可以映射到 GitHub Issues、ADO，未来再接 Jira、Linear

判断：

LeanSpec 和前两者最大的不同，在于它把 spec 看成一个独立的数据层，而不是只是一组 markdown 模板。也就是说，它更像“规格管理中间件”，而不是单纯的 agent prompt 包。

适合：

- 企业内部已经有 issue/work item 流程
- 想把 AI coding workflow 嵌入现有项目管理系统
- 希望有看板、统计和 MCP 接口来承接 agent 的团队

代价：

- 生态还在长，部分 provider 仍处于 planned 或 future 状态
- 如果你只想快速起一个简单 spec 流程，它可能反而偏“平台化”

#### 3.1.4 specs.md

- 仓库：<https://github.com/fabriqaai/specs.md>
- 开源协议：MIT
- 公开定位：AI-native development framework with pluggable flows
- 三种流程：Simple、FIRE、AI-DLC
- Simple：经典三件套 `requirements.md`、`design.md`、`tasks.md`
- FIRE：强调 adaptive execution、brownfield、monorepo、自动 walkthrough
- AI-DLC：强调 DDD、全链路 traceability 和 operations 阶段

判断：

specs.md 的独特之处是把“严格度可调”做成了一等能力。很多团队的问题不是要不要规格，而是“规格要多重”。specs.md 通过多条 flow 让你能在原型、小团队、复杂领域、受监管场景之间切换。

适合：

- 同一组织内项目成熟度差异很大
- 既要支持 MVP，也要支持高追溯、高治理项目
- 对 DDD、运行阶段和过程留痕有要求的团队

代价：

- 概念层次比普通三文档流更复杂
- 新手第一次接触时，需要先选对 flow，不然容易觉得方法太多

#### 3.1.5 Shotgun

- 仓库：<https://github.com/shotgun-sh/shotgun>
- 开源协议：MIT
- 公开定位：write codebase-aware specs for AI coding agents so they do not derail
- 代表流程：Research -> Specify -> Plan -> Tasks -> Export
- 关键差异：先索引整个代码库，再做 spec，然后拆成 staged PRs

判断：

Shotgun 不完全像传统 SDD 框架，更像 **代码库感知的规格规划器**。它的强项是 brownfield：先读仓库结构、依赖和已有模式，再把一个大功能拆成可执行的阶段性 PR，降低 agent 一口气做大改动时的失控风险。

适合：

- 已经有复杂仓库，希望 AI 先理解再改的人
- 大特性、重构、迁移项目
- 希望把 spec 直接映射成分阶段交付计划的人

代价：

- 它更偏“研究和规划驱动”，不是最纯粹的规格模板框架
- 部分团队协作能力是付费特性，虽然核心仓库本身开源

### 3.2 第二层：相邻谱系，不完全等同于 SDD

#### MetaGPT

- 仓库：<https://github.com/FoundationAgents/MetaGPT>
- 开源协议：MIT
- 公开定位：one line requirement -> user stories / requirements / APIs / documents / code

判断：

MetaGPT 更像“多代理软件公司”范式。它和 SDD 的交集在于，会把需求拆成一系列中间工件，而不是直接从 prompt 跳到代码。但它的核心卖点是多角色协作和 SOP 编排，不是围绕“可持久化规格层”来建标准工具链。

所以它是 **spec-aware 的多代理开发框架**，但不是今天最典型的显式 SDD 工具。

#### gpt-engineer

- 仓库：<https://github.com/AntonOsika/gpt-engineer>
- 开源协议：MIT
- 状态：仓库已在 2026-04-22 归档，只读
- 公开定位：specify software in natural language, then let AI write and execute the code

判断：

gpt-engineer 是这一波“spec/prompt to code”工具的早期代表，历史意义很大，但它更像前 SDD 时代的祖先项目。它证明了“先写一个 prompt/spec，再让 AI 生成代码”这条路线可行，但今天如果你想要更成熟的规格治理、任务分解和团队协作，通常会优先看 Spec Kit、OpenSpec、LeanSpec、specs.md 这类更新的方案。

#### OpenHands

- 仓库：<https://github.com/OpenHands/OpenHands>
- 开源协议：核心多数 MIT，`enterprise/` 目录为 source-available
- 公开定位：AI-Driven Development

判断：

OpenHands 很强，但它的重点是 **执行层和 agent runtime**，不是规格层。它更适合和 SDD 框架配合使用，而不是单独被当成 SDD 方法本身。

一句话概括：

> OpenHands 更像“能干活的执行器”，Spec Kit / OpenSpec / LeanSpec / specs.md 更像“先把活定义清楚的规格层”。

## 4. 当前生态的真实判断

### 4.1 有开源方案，但还没有统一标准

现在的局面不是“没有方案”，而是“方案已经出现，但还没有像 OpenAPI 那样形成统一事实标准”。

目前大家正在竞争的，不是“要不要 spec”，而是下面这几个问题：

- 规格应该只是 markdown，还是要变成独立数据层。
- 流程应该强约束，还是轻量可回改。
- brownfield 应该优先，还是 greenfield 更容易。
- spec 应该服务单 agent，还是多 agent、MCP、工作项系统。
- 产物应该停留在文档，还是能继续生成 issue、PR、看板和验证步骤。

### 4.2 行业正在收敛到一套共同骨架

虽然实现不同，但这些项目已经表现出明显共识：

1. 需求、设计、任务必须持久化，不能只留在聊天上下文里。
2. AI 需要分阶段工作，不应该直接一跳生成大块代码。
3. brownfield 是主战场，框架必须理解现有仓库，而不是只服务 0 到 1。
4. 文档本身要变成 agent 可消费的上下文资产，而不是写给人看完就丢。
5. 最终最好能连到 issue、PR、board、validation，而不只是停留在 markdown。

## 5. 如果你要选，我的建议

### 5.1 个人和小团队

- 首选 OpenSpec：轻、快、迭代自然。
- 如果你想跟着一个更完整的方法学走，选 Spec Kit。

### 5.2 中大型工程团队

- 如果你要统一组织规范、质量门、模板和 agent 接入，优先 Spec Kit。
- 如果你已经有 GitHub Issues、ADO 等流程，不想推翻重来，优先 LeanSpec。

### 5.3 Brownfield 和复杂仓库改造

- 如果核心痛点是“AI 经常改偏、改炸、看不懂旧仓库”，优先 Shotgun。
- 如果你还要保留明确 spec artifacts，再叠加 OpenSpec 或 Spec Kit 的工件层。

### 5.4 合规、DDD、强追溯项目

- 优先看 specs.md 的 AI-DLC 路线。
- 如果你需要企业化的自定义模板，也可以把 Spec Kit 做成组织内 preset。

## 6. 一个务实判断框架

你可以把这些方案理解成三层：

| 层级 | 代表项目 | 作用 |
| --- | --- | --- |
| 规格层 | Spec Kit, OpenSpec, LeanSpec, specs.md | 把需求、设计、任务和治理规则沉淀成持久化工件 |
| 规划层 | Shotgun, MetaGPT | 做研究、拆解、编排，把复杂工作变成可执行阶段 |
| 执行层 | OpenHands, Cursor, Claude Code, Copilot, Codex 等 | 真的去改代码、跑命令、验证结果 |

所以更现实的落地方式通常不是“只选一个”，而是：

> 用规格层定义边界，用规划层拆任务，用执行层完成实现。

## 7. 这和已有知识点的关系

- [[AI-Agent-架构与框架全景指南]]：讲的是 agent 架构和开发框架全景。
- [[Harness-Content-Prompt-Engineering-区别与联系]]：有助于理解为什么 SDD 不是单纯 prompt engineering，而是把内容工件提升为 runtime contract。
- [[Vibe-Coding-实战指南]]：SDD 可以理解为对 vibe coding 的工程化约束和可复现化改造。

## 8. 参考来源

- GitHub Spec Kit: <https://github.com/github/spec-kit>
- GitHub Spec Kit 方法文档: <https://github.com/github/spec-kit/blob/main/spec-driven.md>
- Fission AI OpenSpec: <https://github.com/Fission-AI/OpenSpec>
- Shotgun: <https://github.com/shotgun-sh/shotgun>
- LeanSpec: <https://github.com/codervisor/leanspec>
- specs.md: <https://github.com/fabriqaai/specs.md>
- MetaGPT: <https://github.com/FoundationAgents/MetaGPT>
- gpt-engineer: <https://github.com/AntonOsika/gpt-engineer>
- OpenHands: <https://github.com/OpenHands/OpenHands>

## Update History

- 2026-06-09: 初次创建，整理 specification-driven AI development 的开源方案生态、项目定位和选型建议。
- 2026-06-09: 补充横向对比矩阵，增强不同团队场景下的快速选型能力。