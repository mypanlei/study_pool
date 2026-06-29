---
title: "Spec-Driven Development Knowledge Hub"
source: "https://intent-driven.dev/knowledge/openspec/"
author:
  - "[[Hari Krishnan]]"
published: 2025-11-20
created: 2026-06-29
description: "Learn OpenSpec for spec-driven development with tutorials, workflow diagrams, custom schemas, source-of-truth specs, and AI coding resources."
tags:
  - "clippings"
---
## 概述

OpenSpec 是一款基于规范的开发 (SDD) 工具，它强调维护 **一份统一的规范文档，** 作为系统设计和功能的权威参考。与将规范分散在多个文件中的传统方法不同，OpenSpec 将系统的当前状态整合到一个“动态”规范中，该规范会随着代码库的演进而不断更新。

这种真理来源方法解决了碎片化规范系统中的持续挑战，在这些系统中，整体系统意图难以全面掌握，功能交互直到实现后才能被发现，并且几乎不可能根据实时系统验证完整的规范。

## OpenSpec 的工作原理

OpenSpec 工作流程围绕三种关键工件类型展开：

### 变更规格（增量规格）

增量规范代表拟议的修改。这些临时文档会将章节标记为“新增”、“修改”或“删除”，清晰地传达变更内容。这使得人类和人工智能代理都能轻松理解拟议内容，而无需比较整个文档。

### 真实性来源规范

主规范代表系统的实际状态。所有增量变更最终都会在归档阶段合并到这份单一文档中，形成一份供利益相关者查阅的权威参考资料。这确保了所有人对系统功能的理解完全一致。

### 已存档规格

归档规范保留了早期增量规范的历史沿革，一旦它们被纳入权威规范，便能维护演进的审计追踪。这有助于明确责任，并使团队能够理解决策的制定方式和原因。

### 使用 Git 工作树进行并行开发

Git 工作树允许您同时检出多个分支到不同的目录中。结合 OpenCode 中的子代理，这实现了真正的并行功能开发：在主分支上提出更改，通过子代理将每个更改应用到隔离的工作树中，然后按顺序合并和归档。每个子代理在合并前都会运行验证，从而确保所有并行流的源代码规范保持一致。

### 建筑决策记录

自定义 OpenSpec 模式可以通过添加持久性工件来扩展工作流程。该 `spec-driven-with-adr` 模式引入了架构决策记录 (ADR)，它们与权威规范并存，独立于任何单一变更之外。规范记录了系统功能的当前状态；ADR 记录了其架构的当前状态——每个重要技术决策背后的背景、选项、选择和后果。即使变更被归档，这两个工件仍然保留，因此未来的提案可以利用设计阶段的先前推理，而无需重新发现。

## 视频教程

通过我们的视频教程学习 OpenSpec 工作流程和最佳实践。播放列表涵盖从入门到高级集成模式的所有内容。

![](https://www.youtube.com/watch?v=B7VPMKW5tnk)

## 工作流程图

理解 OpenSpec 工作流程和集成模式的可视化指南。### OpenSpec 工作流程图

完整的“提议→应用→归档”工作流程展示了增量规范如何演变为最终的真实规范。

[在 GitHub 上查看](https://github.com/Fission-AI/OpenSpec/discussions/294)

[![[raw/assets/06b5eec4a824fa33cf71661d526e42f5_MD5.jpg]]](https://intent-driven.dev/blog/2026/01/11/linear-mcp-openspec-sdd-workflow/)

### 线性 MCP + OpenSpec 工作流程

集成工作流程展示了 Linear MCP 如何通过提议、应用和归档阶段保持待办事项同步。

[阅读指南](https://intent-driven.dev/blog/2026/01/11/linear-mcp-openspec-sdd-workflow/)

[![[raw/assets/f30b60cb540c9159075178ff750400e8_MD5.jpg]]](https://intent-driven.dev/blog/2026/04/01/openspec-git-worktrees-opencode/)

### Git 工作树 + OpenSpec 工作流

Git 工作树如何实现 OpenSpec 的并行更改，使每个更改都与主分支隔离在各自的工作树中。

[阅读指南](https://intent-driven.dev/blog/2026/04/01/openspec-git-worktrees-opencode/)

[![[raw/assets/ed48f9f889b82f8e89b8a6fbc4ac5b4c_MD5.jpg]]](https://intent-driven.dev/blog/2026/04/29/spec-driven-development-with-adr/)

### 基于规范的ADR模式

自定义模式如何 `spec-driven-with-adr` 将架构决策记录作为持久工件与真理源规范一起保存。

[阅读指南](https://intent-driven.dev/blog/2026/04/29/spec-driven-development-with-adr/)

## 博客文章

深入介绍 OpenSpec 概念、工作流程和集成模式的文章。

- [使用 OpenSpec 和 OpenCode 进行规范驱动开发](https://intent-driven.dev/blog/2026/05/10/spec-driven-development-openspec-opencode/)
	2026年5月10日 — 逐步介绍意图驱动模板，该模板将 OpenSpec 设置、openspec-git-discipline 技能、grill-me 提案、C4 图表、ADR 和意图驱动的自定义模式连接成一个单一的规范驱动开发工作流程。
- [使用 OpenSpec 进行规范驱动开发的架构决策记录](https://intent-driven.dev/blog/2026/04/29/spec-driven-development-with-adr/)
	2026年4月29日 — 自定义 OpenSpec 模式，将架构决策记录与规范一起保存，以便架构推理能够保留到未来的变更提案中，而不是在变更归档时丢失。
- [OpenSpec、Git 工作树和 OpenCode](https://intent-driven.dev/blog/2026/04/01/openspec-git-worktrees-opencode/)
	2026年4月1日 — 在 OpenCode 中使用 Git WorkTrees 和 SubAgents 与 OpenSpec 并行构建功能的工作流程：在主分支上提出建议，在隔离的工作树中应用，合并，然后归档。
- [棕地项目的规范驱动型开发](https://intent-driven.dev/blog/2026/03/10/spec-driven-development-brownfield/)
	2026年3月10日 — 使用自定义 OpenSpec 配置文件和探索工作流程，逐步将 SDD 应用于棕地项目，并使用 Repomix 进行上下文管理。
- [OpenSpec 自定义模式](https://intent-driven.dev/blog/2026/02/12/openspec-custom-schemas/)
	2026年2月12日 — OpenSpec 中的自定义模式允许您根据自身领域定制基于规范的工作流程。涵盖了极简模式和事件驱动模式的示例。
- [OpenSpec 1.0 版本](https://intent-driven.dev/blog/2026/01/26/openspec-1-0-release/)
	2026年1月26日 — OpenSpec 1.0 版本更新，包含演示视频和工作流程亮点。
- [线性 MCP + OpenSpec：一种规范驱动的开发工作流程](https://intent-driven.dev/blog/2026/01/11/linear-mcp-openspec-sdd-workflow/)
	2026年1月11日 — 本文将实际演示如何使用 Linear MCP 和 OpenSpec 来保持待办事项列表同步。内容涵盖角色、交接以及如何将业务用例（做什么）与技术实现（怎么做）分开。
- [基于 OpenSpec 的规范驱动开发：真实规范的来源](https://intent-driven.dev/blog/2025/11/09/spec-driven-development-openspec-source-truth/)
	2025年11月9日 — 全面解释 OpenSpec 工作流程和权威规范概念的指南。理解 OpenSpec 的基础文章。

## 主要优势

- **基于规范的对齐：** OpenSpec 通过维护统一的规范，支持在任何阶段根据当前权威规范进行验证。这与碎片化的方法形成鲜明对比，后者通常停留在“规范优先”的阶段，规范指导初始设计，但随着实现的偏离，其可靠性逐渐降低。
- **更快的迭代周期：** 简化的工作流程支持更好的流程状态和更快的实施周期，尤其是在与 AI 编码代理合作时。
- **棕地支持：** 对棕地和遗留项目提供自然支持——您可以捕获现有的系统状态，而无需完全重写。
- **特征交互检测：** 当所有特征都包含在一个规范中时，理解特征之间的非预期交互就变得更容易了。
- **持续验证：** 通过真实性模型确保规范与实施保持同步。

## 何时使用 OpenSpec

OpenSpec 非常适合采用增量式、规范驱动开发模式的团队，这些团队需要确保规范与实现保持同步。它尤其适用于：

- 项目需要规范和代码之间持续验证。
- 棕地或遗留系统现代化改造工作
- 重视快速迭代和频繁规范更新的团队
- 理解功能之间非预期交互至关重要的系统
- 涉及人工智能编码代理的开发工作流程

该工具假定用户能够适应人工智能辅助开发，并通过小而有针对性的修改来维持严谨的变更实践。

## 资源

- [OpenSpec GitHub 仓库](https://github.com/Fission-AI/OpenSpec)
	官方 OpenSpec 代码库，包含文档、示例和 CLI 工具。
- [OpenSpec GitHub 讨论](https://github.com/Fission-AI/OpenSpec/discussions/294)
	社区就 OpenSpec 工作流程和最佳实践进行讨论和反馈。