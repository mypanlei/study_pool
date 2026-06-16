---
title: "Hugging Face Transformers — 菜鸟教程"
tags:
  - source
  - huggingface
  - transformers
  - nlp
  - llm
  - fine-tuning
  - rookie-tutorial
created: 2026-06-17
updated: 2026-06-17
source_url: "https://www.runoob.com/ai-agent/hugging-face-transformers.html"
source_author: "菜鸟教程 (Runoob)"
source_date: 2026-06-17
---

# Hugging Face Transformers

> 系统的 Hugging Face Transformers 库教程，覆盖 Pipeline 快速推理、Tokenizer 详解、AutoClass 模型加载、十大 NLP/CV/音频任务实战、微调完整流程（Trainer API）、LoRA 参数高效微调、推理加速技术栈、以及常见问题排查。

## 核心内容

1. **生态系统全景** — Hub（40万+模型）、Transformers（推理/微调）、Datasets、PEFT（LoRA/QLoRA）、Accelerate（分布式）、Tokenizers、Evaluate。
2. **三大模型家族** — 仅 Encoder（BERT-理解类）、仅 Decoder（GPT-生成类）、Encoder-Decoder（T5-翻译/摘要类）。
3. **Pipeline 快速推理** — 五行代码完成情感分析、文本生成、NER、问答、摘要、翻译等任务。
4. **Tokenizer 深度解析** — BPE/WordPiece/SentencePiece 三种算法对比，完整编码流程（文本→分词→特殊标记→Token IDs）。
5. **微调完整流程** — 数据加载→Tokenize→模型加载→TrainingArguments→Trainer→评估→保存，含 LoRA（训练不到 1% 参数，显存降低 60-70%）。
6. **推理加速技术栈** — Level 1 零成本优化（fp16/batch）、Level 2 量化（4-bit/8-bit）、Level 3 编译优化（FlashAttention-2/torch.compile）、Level 4 专用引擎（vLLM/TGI）。

## 关键概念

- Transformers 核心价值：把复杂的模型加载、推理、训练流程封装成几行代码
- AutoClass 自动根据 config.json 匹配正确的模型架构
- LoRA 将 ΔW 分解为两个低秩矩阵（r<<d），大幅降低训练成本
