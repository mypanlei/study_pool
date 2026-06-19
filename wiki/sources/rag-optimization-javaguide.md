---
title: "万字详解 RAG 优化：从召回、重排到上下文工程的系统调优 — JavaGuide"
tags:
  - source
  - rag
  - optimization
  - rerank
  - javaguide
created: 2026-06-19
updated: 2026-06-19
source: "https://javaguide.cn/ai/rag/rag-optimization.html"
author: "Guide (JavaGuide)"
---

# 万字详解 RAG 优化：从召回、重排到上下文工程的系统调优 — JavaGuide

> A systematic treatment of RAG optimization as a full-chain engineering challenge, moving beyond the common mistake of treating embedding model selection as the primary lever. Covers the interplay of document parsing, chunk strategy, metadata design, hybrid search, query rewrite, reranking, context compression/engineering, prompt constraints, evaluation (RAGAS/DeepEval), and a practical incident investigation path for diagnosing RAG failures in production.

## Core Contributions

1. **Full-chain optimization framework**: Maps each pipeline stage (parsing, chunking, metadata, retrieval, reranking, context construction, generation, evaluation) to its typical failure modes and final quality impacts, establishing that RAG optimization must be systemic rather than point-wise.
2. **Data governance-first principle**: Argues convincingly that 60% of RAG failures stem from data issues (broken PDF tables, chunks splitting conditions from conclusions, empty candidate pools) rather than insufficient vector similarity — "data quality determines the upper bound."
3. **Multi-layered Top-K architecture**: Proposes three distinct K parameters — `recall_top_k` (30-100 for coarse retrieval), `rerank_top_n` (5-10 after reranking), and `context_top_n` (3-6 for final LLM context) — instead of a single Top-K parameter.
4. **Hybrid Search decision guide**: Provides a query-type matrix comparing vector vs. BM25 performance across query categories (semantic, exact-code, SKU, mixed, time-sensitive), with concrete guidance on when hybrid search is essential vs. when it adds marginal value.
5. **Query Rewrite taxonomy**: Catalogues six rewrite strategies (normalization, Multi-Query, Query Decomposition, Step-back, HyDE, Self-Query) with use cases and examples, plus the critical caution that original queries must be preserved alongside rewritten ones.
6. **Context engineering principles**: Details compression approaches (selective extraction, query-relevant summarization, structured extraction), evidence ordering strategies, and prompt boundary rules — emphasizing that more context is not better and that LLM attention is a limited resource.
7. **Production incident investigation path**: A 5-step diagnostic workflow: (1) classify failure samples, (2) check if correct evidence enters the candidate pool, (3) check if correct evidence enters context, (4) check if context is correct but answer is wrong, (5) establish regression testing.

## Key Insights

- "RAG 优化的目标是提高最终答案的可用性、可追溯性和稳定性，而不是让每个环节看起来高级" (The goal of RAG optimization is to improve answer usability, traceability, and stability — not to make each component look sophisticated.)
- "先向量检索，再做权限过滤" is dangerous — always pre-filter by metadata (tenant_id, ACL, document type) before vector search, not after.
- "我感觉好多了" is not a metric — every change must be evaluated against the same fixed test set with playback/comparison.
- Rerank cannot save you if the correct document is not in the candidate pool; check Context Recall before tuning reranker parameters.
- "RAG 的瓶颈通常不在某一个参数，而在证据从原始文档走到最终答案的整条路径上" (The RAG bottleneck is usually not in any single parameter, but in the entire path evidence travels from source documents to final answers.)

## Related Pages

- [[wiki/concepts/rag-optimization]] — RAG 全链路优化
- [[wiki/concepts/embedding]] — Embedding 嵌入与向量化
- [[wiki/concepts/rerank]] — Rerank 重排序
- [[wiki/concepts/rag-vs-wiki]] — RAG vs Wiki
- [[wiki/concepts/fine-tuning]] — 微调
- [[wiki/syntheses/rag-optimization-guide]] — RAG 优化指南
- [[wiki/sources/rag-basis-concepts-javaguide]] — RAG 基础概念（已梳理）
