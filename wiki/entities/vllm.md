---
title: "vLLM"
tags:
  - entity
  - inference
  - llm
  - serving
created: 2026-06-17
updated: 2026-06-19
aliases:
  - vLLM 推理引擎
---

# vLLM

> 高性能 LLM 推理引擎，核心创新是 PagedAttention 算法，解决了 KV Cache 显存碎片问题，大幅提升推理吞吐量。

## 关键信息

- **类型**: 开源 LLM 推理引擎
- **开发商**: UC Berkeley (SkyLab)
- **核心创新**: PagedAttention
- **Stars**: ~50k+（截至 2026-06）

## 核心特性

| 特性 | 说明 |
|------|------|
| **PagedAttention** | 类操作系统的分页显存管理，消除碎片 |
| **Continuous Batching** | 动态批处理，提升吞吐量 |
| **Prefix Caching** | 公共前缀缓存，加速 System Prompt |
| **Speculative Decoding** | 投机解码加速 |
| **多 GPU 推理** | Tensor/Pipeline 并行 |

## 生态定位

vLLM 常用于替代 KServe 的默认推理后端，作为高性能 LLM 推理层。

## 来源

- [[wiki/sources/mlops-open-source-platform-comparison]] — MLOps 平台对比，含 vLLM 推理后端定位
- [[wiki/sources/kv-cache-technical-detail]] — KV Cache 技术详解，PagedAttention 核心原理
- [[wiki/sources/large-model-parameters-and-performance]] — LLM 推理优化与性能分析
- [[wiki/concepts/kv-cache]] — KV Cache 概念与 PagedAttention
