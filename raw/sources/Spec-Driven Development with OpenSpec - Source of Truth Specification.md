---
title: "Spec-Driven Development with OpenSpec - Source of Truth Specification"
source: "https://intent-driven.dev/blog/2025/11/09/spec-driven-development-openspec-source-truth/"
author:
  - "Hari Krishnan"
published: 2025-11-09
created: 2026-06-29
description: "Learn how OpenSpec keeps a source-of-truth specification for spec-driven development, helping AI coding agents stay aligned with project intent."
tags:
  - source
  - spec-driven
  - openspec
  - comparison
---
[点击此处查看完整图表 →](https://intent-driven.dev/assets/blog/openspec-source-truth/workflow-diagram.jpg)

---

我在之前的文章中提到过，我一直在尝试使用几种规范驱动开发（SDD）工具，既是为了评估它们，也是为了在自己的工作中应用它们。其中，OpenSpec 逐渐成为我最喜欢的 SDD 工具之一。它引入了一个很有意思的理念：使用单一的顶层“权威规范”。在本文中，我将探讨 OpenSpec 的工作流程、“权威规范”的优势以及一些其他方面的观察。

## OpenSpec - 变更工作流程

![](https://www.youtube.com/watch?v=B7VPMKW5tnk)

[点击此处查看完整图表 →](https://intent-driven.dev/assets/blog/openspec-source-truth/workflow-diagram.jpg)

我刚开始使用 GitHub Spec-Kit 时，Roslyn Zolandor 绘制的功能工作流程图对我帮助极大。受其启发，我为 OpenSpec 创建了一个工作流程图，一方面是为了加深自己对 OpenSpec 的理解，另一方面也是为了向其他可能正在探索 OpenSpec 的人阐明其模型。如果您发现上述图表有任何不足或改进之处，欢迎指正。

上图重点展示了变更过程中生成的文件，以及OpenSpec README文件中已记录的基本工作流程。以下是一些关键方面。

**变更规范（增量规范）** ——这些是我们提出变更时生成的规范文件。它们遵循将章节标记为“已添加”、“已修改”或“已删除”的约定。

**“权威规范”** ——这是代表系统当前状态的动态规范。所有增量变更最终都会合并到这份单一文档中（作为归档步骤的一部分），该文档将作为最终参考。

**已存档规范** \- 顾名思义，这些规范保留了早期增量规范的历史记录，一旦它们被合并到“真理之源”规范中。

## 为什么“真理之源”规范如此重要？

为了理解它的重要性，回顾一下我在此背景下使用 Spec-Kit 和 Kiro 等工具时遇到的一些困难会有所帮助。

如果没有顶级规范，功能级别的规范通常会分散在“specs”目录下的各个子文件夹中。这种分散性会导致以下问题：

1. **理解分散** ——系统的总体意图分散在多个文件中，难以保持连贯的理解。
2. **规范演变** ——在规范演变过程中似乎出现了一些问题和困惑，这些问题和困惑已经在相关的讨论中得到了充分的讨论。
3. **意外交互** \- 由于没有统一的验证视图，每个新增功能都有可能无意中影响现有行为。

根据我的经验，Spec-Kit 在每次修改都保持小而集中时效果最佳（这通常也是个好主意），这也有助于控制上下文长度，正如我在之前的文章中详述的那样。通过这些小而集中的修改，我逐渐将 specs 文件夹视为一个账本，其中只添加条目而不更新。这意味着即使我们修改或删除功能，实际上也只是追加新的 specs。

如果我们需要应用程序的总体规范，可以尝试按顺序应用所有更改来构建总体规范。然而，我们得到的只是一个衍生视图，而非原始视图。很难说这种累积规范是否会随着时间的推移而保持有效或与实际系统保持一致。

这自然引出了一个问题：从这种设置中，我们可以在概念上期望获得何种程度的验证？

## 一致性层次——规范与实现

我发现 Birgitta Boeckeler 的文章《理解规范驱动开发：Kiro、spec-kit 和 Tessl》（推荐阅读）在这方面非常有帮助。她概述了规范与实现之间三种一致性类别。

**规格优先**

**规格锚定**

**规格即来源**

即使从概念上讲，当我们依赖碎片化的规范（例如 Spec-Kit 或 Kiro）时，最终也会面临一致性问题。随着功能被弃用或演进，相关的规范会部分失效。随着时间的推移，这使得我们无法针对当前系统状态验证所有规范并期望获得一致的结果。因此，这种碎片化的规范方法本质上使我们仍然处于“规范优先”的范畴，规范在初始探索和功能定义方面很有用，但从长远来看，它们可能无法与实现保持一致。

相比之下，OpenSpec 通过维护一个持续代表实时系统的顶级规范，能够成为一个规范锚定工具，随时可以根据统一的、真实来源的规范进行验证。

为了保持本文的重点，我将不讨论“规范即资源”这一概念。

## 关于 OpenSpec 的其他观察

**快速迭代** ——我倾向于小幅、渐进式的修改，在这种模式下，OpenSpec 的整体提案周期明显更快。使用 Spec-Kit 时，规划阶段通常耗时更长（这未必是坏事，因为它似乎能进行更深入的分析），但 OpenSpec 的响应速度有助于保持稳定的迭代节奏。

**心流状态** ——因为我能够快速迭代，所以我的上下文切换频率较低，并且能够更长时间地保持专注。

**1-N / 现有项目** \- OpenSpec 的定位是更适合现有项目，目前看来确实如此。无论是通过更新“project.md”文件，还是通过自然演进规范源，它都能捕捉现有系统的当前状态，并支持重构和增量变更。我还没有在大型复杂代码库上进行测试，因此无法将其与 Spec-Kit 和 Kiro 进行真正的比较，但就目前而言，OpenSpec 的工作流程在扩展现有项目时感觉自然流畅，不会造成干扰。

## 概要

在不断发展的规范驱动开发生态系统中，OpenSpec 是一款特别引人注目的工具。我建议您试用一下。

话虽如此，我仍然是 GitHub Spec-Kit 和 OpenSpec 的活跃贡献者，并且经常使用 Kiro。根据我的经验，挫败感往往并非源于工具本身，而是源于预期不符。

我非常希望得到反馈、问题或您在使用 OpenSpec 和其他软件开发工具方面的经验分享。

---

同时发布在 [blog.harikrishnan.io](https://blog.harikrishnan.io/2025-11-09/spec-driven-development-openspec-source-truth) 和 [LinkedIn](https://www.linkedin.com/pulse/spec-driven-development-openspec-source-truth-hari-krishnan--obrfc) 上。