---
title: "RoPE 旋转位置编码"
tags:
  - concept
  - llm
  - positional-encoding
  - rope
  - long-context
created: 2026-06-13
updated: 2026-06-13
aliases:
  - RoPE
  - Rotary Positional Embedding
  - 旋转位置嵌入
---

# RoPE (Rotary Positional Embedding)

> 旋转位置嵌入，一种将位置信息通过旋转矩阵注入 Query 和 Key 的编码方式。点积仅取决于相对距离，是 Llama、Mistral 等主流 LLM 采用的位置编码方案。

## 定义

RoPE 通过旋转矩阵将位置信息注入 Q 和 K 向量，使得注意力得分仅依赖 Token 间的相对距离而非绝对位置。预训练时模型学习到 [0, L_train] 范围内的旋转角度语义，超出范围会导致注意力分布崩溃。

## 核心要点

1. **数学本质**：位置 m 的向量 q 旋转角度 m*theta。两个向量点积仅取决于相对距离 (m-n)。
2. **RoPE 插值**：扩展上下文的核心技术。本质是坐标系压缩（将每厘米缩为 0.5 厘米，使原尺子容纳 2 倍信息）。
3. **方法演进**：PI（线性插值，高频丢失）→ NTK-Aware（高频不缩放保留局部精度）→ YaRN（分段缩放+注意力温度修正，当前工业标准）→ DroPE（推理时逐渐减少位置嵌入权重，支持百万级）。

## 详细阐述

### 为什么需要插值
预训练长度 L_train 内模型见过所有旋转角度，超出时遇到从未见过的角度，注意力分布崩溃。插值将现有坐标系压缩而非外推。

### 参数选择
- <32k：不插值，保持原生精度
- 32k-128k：NTK/Dynamic-NTK
- 128k+：YaRN（最稳健的工程方案）
- 1M+：DroPE（前沿，需配合高效缓存）

## 相关概念

- [[wiki/concepts/transformer-architecture]] — 位置编码在 Transformer 中的角色
- [[wiki/concepts/kv-cache]] — 长上下文推理中的显存挑战
- [[wiki/concepts/fitting-mechanism]] — 插值后微调的精度补偿

## 来源

- [[wiki/sources/rope-interpolation-technical-detail]]
- [[wiki/sources/transformer-architecture-detail]]
- [[wiki/sources/kv-cache-technical-detail]]
