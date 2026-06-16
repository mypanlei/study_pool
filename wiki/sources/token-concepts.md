---
title: "Token（词元） — 菜鸟教程"
tags:
  - source
  - token
  - llm
  - basics
  - context-window
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/token-intro.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Token（词元）

> 面向初学者的 Token 概念入门教程。Token（词元）是 AI 能理解的最小文本单位，介于字符和单词之间。涵盖 Token 切分原理（BPE 算法）、中文与英文的 Token 消耗差异、上下文窗口概念、Token 计费与生成速度的关系。

## 核心内容

1. **Token 本质** — AI 处理文本的最小单位，介于字母和单词之间的灵活中间单位，通过 BPE（字节对编码）算法切分。
2. **Token 切分示例** — 常见词一个 Token，复杂词被拆分（unbelievable→un+believ+able），标点空格都算 Token。
3. **中文 vs 英文** — 中文每字约消耗 2-3 个 Token，比英文消耗更多；1,000 Token ≈ 750 英文单词。
4. **上下文窗口** — GPT-3.5（4K）、GPT-4 Turbo（128K）、Claude 3.5（200K），超过即"遗忘"。
5. **Token 计费** — API 按输入+输出的 Token 总量收费；代码 Token 消耗比自然语言少。

## 关键概念

- Token = AI 世界的燃料，比单词更细，比字母更粗
- AI 逐 Token 生成回复，越长等待越久
- 理解 Token 是控制成本和优化 Prompt 的基础
