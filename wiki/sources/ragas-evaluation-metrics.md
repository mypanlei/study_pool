---
title: "RAGAS 评估指标深度解析"
tags:
  - source
  - rag
  - ragas
  - llm-evaluation
  - ai-architecture
created: 2026-06-13
updated: 2026-06-13
source_author: "内部团队"
source_date: 2026-04-10
---

# RAGAS 评估指标深度解析：Faithfulness, Relevancy 与 Robustness

> RAG 系统评估主流框架 RAGAS 的深度解析。采用 LLM-as-a-Judge 思路，量化系统可靠性。

## 核心论点

1. **核心评估三元组**：
   - Faithfulness（忠实度）：Answer 拆分为 Claims，验证每个 Claim 能否从 Context 中找到依据。
   - Answer Relevancy（回答相关性）：根据 Answer 反向推测用户可能问的问题，计算与原始 Query 的相似度。
   - Context Precision（上下文精度）：评估排序靠前的检索结果是否真的比后面的更有用（信噪比）。
2. **鲁棒性（Robustness）**：生产环境中用户问题可能含陷阱或检索库含冲突信息，需测试 Negative Rejection（敢于说不知道）和 Noise Sensitivity（嘈杂资料中提取核心事实的能力）。
3. **评估流程**：准备测试集（Query+Context+Answer）→ 调用 LLM 裁判（GPT-4/Qwen-Max）→ 根据分数调整 Chunk Size/检索算法/Prompt。

## 与现有知识的关系

- 与 [[wiki/sources/rag-common-issues-and-optimization]] 构成 RAG 评估闭环
- 支撑 [[wiki/syntheses/rag-optimization-guide]]

## 受影响的 Wiki 页面

- [[wiki/concepts/rag-optimization]] — 已更新
- [[wiki/syntheses/rag-optimization-guide]] — 已更新
- [[wiki/concepts/rag-vs-wiki]] — 已更新
