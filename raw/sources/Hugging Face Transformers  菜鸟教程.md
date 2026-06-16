---
title: "Hugging Face Transformers | 菜鸟教程"
source: "https://www.runoob.com/ai-agent/hugging-face-transformers.html"
author:
published:
created: 2026-06-17
description: "Hugging Face Transformers  Hugging Face Transformers 是目前最流行的开源 NLP / AI 库，提供数千个预训练模型，覆盖文本、图像、音频、多模态等几乎所有 AI 任务。 它的核心价值：把复杂的模型加载、推理、训练流程封装成几行代码。        Hugging Face 生态系统全景       Hub   40万+ 模型   10万+ 数据集       Transformers.."
tags:
  - "clippings"
---
## Hugging Face Transformers

Hugging Face Transformers 是目前最流行的开源 NLP / AI 库，提供数千个预训练模型，覆盖文本、图像、音频、多模态等几乎所有 AI 任务。

它的核心价值：把复杂的模型加载、推理、训练流程封装成几行代码。

<svg viewBox="0 0 720 280" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="280" fill="#f8f9fa" rx="12"></rect><text x="360" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">Hugging Face 生态系统全景</text> <ellipse cx="360" cy="148" rx="72" ry="50" fill="#f5a623" opacity="0.95"></ellipse><text x="360" y="142" text-anchor="middle" font-size="13" fill="#fff" font-weight="bold">Hub</text> <text x="360" y="158" text-anchor="middle" font-size="10" fill="#fff">40万+ 模型</text> <text x="360" y="172" text-anchor="middle" font-size="10" fill="#fff">10万+ 数据集</text> <rect x="30" y="50" width="135" height="60" rx="9" fill="#fff" stroke="#e74c3c" stroke-width="2"></rect><text x="97" y="74" text-anchor="middle" font-size="12" font-weight="bold" fill="#c0392b">Transformers</text> <text x="97" y="90" text-anchor="middle" font-size="9" fill="#555">预训练模型推理</text> <text x="97" y="103" text-anchor="middle" font-size="9" fill="#555">与微调框架</text> <line x1="165" y1="80" x2="292" y2="128" stroke="#e74c3c" stroke-width="1.5"></line><rect x="30" y="165" width="135" height="60" rx="9" fill="#fff" stroke="#3498db" stroke-width="2"></rect><text x="97" y="189" text-anchor="middle" font-size="12" font-weight="bold" fill="#2980b9">Datasets</text> <text x="97" y="205" text-anchor="middle" font-size="9" fill="#555">海量数据集</text> <text x="97" y="218" text-anchor="middle" font-size="9" fill="#555">高效加载处理</text> <line x1="165" y1="195" x2="292" y2="162" stroke="#3498db" stroke-width="1.5"></line><rect x="555" y="50" width="135" height="60" rx="9" fill="#fff" stroke="#2ecc71" stroke-width="2"></rect><text x="622" y="74" text-anchor="middle" font-size="12" font-weight="bold" fill="#27ae60">PEFT</text> <text x="622" y="90" text-anchor="middle" font-size="9" fill="#555">参数高效微调</text> <text x="622" y="103" text-anchor="middle" font-size="9" fill="#555">LoRA / QLoRA</text> <line x1="555" y1="80" x2="428" y2="128" stroke="#2ecc71" stroke-width="1.5"></line><rect x="555" y="165" width="135" height="60" rx="9" fill="#fff" stroke="#9b59b6" stroke-width="2"></rect><text x="622" y="189" text-anchor="middle" font-size="12" font-weight="bold" fill="#8e44ad">Accelerate</text> <text x="622" y="205" text-anchor="middle" font-size="9" fill="#555">多GPU/TPU训练</text> <text x="622" y="218" text-anchor="middle" font-size="9" fill="#555">分布式加速</text> <line x1="555" y1="195" x2="428" y2="162" stroke="#9b59b6" stroke-width="1.5"></line><rect x="290" y="38" width="140" height="45" rx="9" fill="#fff" stroke="#f39c12" stroke-width="2"></rect><text x="360" y="57" text-anchor="middle" font-size="12" font-weight="bold" fill="#e67e22">Tokenizers</text> <text x="360" y="73" text-anchor="middle" font-size="9" fill="#555">高性能分词器（Rust实现）</text> <line x1="360" y1="83" x2="360" y2="98" stroke="#f39c12" stroke-width="1.5"></line><rect x="290" y="222" width="140" height="45" rx="9" fill="#fff" stroke="#e67e22" stroke-width="2"></rect><text x="360" y="241" text-anchor="middle" font-size="12" font-weight="bold" fill="#d35400">Evaluate</text> <text x="360" y="257" text-anchor="middle" font-size="9" fill="#555">模型评估指标（BLEU/F1等）</text><line x1="360" y1="198" x2="360" y2="222" stroke="#e67e22" stroke-width="1.5"></line></svg>

### 支持的任务类型

<svg viewBox="0 0 720 210" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="210" fill="#f8f9fa" rx="12"></rect><text x="360" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a1a2e">Transformers 支持的任务分类</text> <rect x="15" y="40" width="210" height="155" rx="9" fill="#fff" stroke="#e74c3c" stroke-width="1.5"></rect><rect x="15" y="40" width="210" height="6" rx="9" fill="#e74c3c"></rect><text x="120" y="63" text-anchor="middle" font-size="12" font-weight="bold" fill="#c0392b">NLP 自然语言处理</text> <text x="28" y="82" font-size="9.5" fill="#555">文本分类（情感分析）</text> <text x="28" y="97" font-size="9.5" fill="#555">命名实体识别（NER）</text> <text x="28" y="112" font-size="9.5" fill="#555">问答系统（QA）</text> <text x="28" y="127" font-size="9.5" fill="#555">文本摘要生成</text> <text x="28" y="142" font-size="9.5" fill="#555">机器翻译</text> <text x="28" y="157" font-size="9.5" fill="#555">文本生成（对话）</text> <text x="28" y="172" font-size="9.5" fill="#555">填空/语言模型</text> <rect x="255" y="40" width="210" height="155" rx="9" fill="#fff" stroke="#3498db" stroke-width="1.5"></rect><rect x="255" y="40" width="210" height="6" rx="9" fill="#3498db"></rect><text x="360" y="63" text-anchor="middle" font-size="12" font-weight="bold" fill="#2980b9">CV 计算机视觉</text> <text x="268" y="82" font-size="9.5" fill="#555">图像分类</text> <text x="268" y="97" font-size="9.5" fill="#555">目标检测</text> <text x="268" y="112" font-size="9.5" fill="#555">图像分割</text> <text x="268" y="127" font-size="9.5" fill="#555">深度估计</text> <text x="268" y="142" font-size="9.5" fill="#555">图像生成</text> <text x="268" y="157" font-size="9.5" fill="#555">视频分类</text> <text x="268" y="172" font-size="9.5" fill="#555">关键点检测</text> <rect x="495" y="40" width="210" height="155" rx="9" fill="#fff" stroke="#9b59b6" stroke-width="1.5"></rect><rect x="495" y="40" width="210" height="6" rx="9" fill="#9b59b6"></rect><text x="600" y="63" text-anchor="middle" font-size="12" font-weight="bold" fill="#8e44ad">音频 &amp; 多模态</text> <text x="508" y="82" font-size="9.5" fill="#555">语音识别（ASR）</text> <text x="508" y="97" font-size="9.5" fill="#555">音频分类</text> <text x="508" y="112" font-size="9.5" fill="#555">文本转语音（TTS）</text> <text x="508" y="127" font-size="9.5" fill="#555">图文匹配（VQA）</text> <text x="508" y="142" font-size="9.5" fill="#555">图像描述生成</text> <text x="508" y="157" font-size="9.5" fill="#555">文档问答（DOC QA）</text> <text x="508" y="172" font-size="9.5" fill="#555">零样本分类</text></svg>

---

## Transformer 架构核心原理

在使用库之前，理解底层架构会让你知道为什么这样调参。

### 整体架构：Encoder-Decoder

![](https://www.runoob.com/wp-content/uploads/2026/05/runoob-cf08ae6f-a6fc-4a1b-8977-364df.png)

### 三大模型家族

<svg viewBox="0 0 720 175" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="175" fill="#f8f9fa" rx="12"></rect><text x="360" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a1a2e">三大模型家族：架构 x 适用场景 x 代表模型</text> <rect x="15" y="38" width="220" height="125" rx="9" fill="#fff" stroke="#e74c3c" stroke-width="1.8"></rect><rect x="15" y="38" width="220" height="6" rx="9" fill="#e74c3c"></rect><text x="125" y="60" text-anchor="middle" font-size="12" font-weight="bold" fill="#c0392b">仅 Encoder 模型</text> <text x="125" y="76" text-anchor="middle" font-size="10" fill="#555">双向注意力，理解全局上下文</text> <text x="28" y="96" font-size="9.5" fill="#555">适合：分类、NER、问答（理解类）</text> <text x="28" y="111" font-size="9.5" fill="#555">代表：BERT、RoBERTa、ALBERT</text> <text x="28" y="126" font-size="9.5" fill="#555">中文：BERT-wwm、MacBERT</text> <text x="28" y="141" font-size="9.5" fill="#555">特点：可同时看到全部输入</text> <rect x="28" y="148" width="193" height="10" rx="3" fill="#fdecea"></rect><text x="124" y="157" text-anchor="middle" font-size="8" fill="#c0392b">输入 -&gt; [CLS] 表示全局，[MASK] 做预训练</text> <rect x="250" y="38" width="220" height="125" rx="9" fill="#fff" stroke="#3498db" stroke-width="1.8"></rect><rect x="250" y="38" width="220" height="6" rx="9" fill="#3498db"></rect><text x="360" y="60" text-anchor="middle" font-size="12" font-weight="bold" fill="#2980b9">仅 Decoder 模型</text> <text x="360" y="76" text-anchor="middle" font-size="10" fill="#555">因果注意力（只看左侧），自回归生成</text> <text x="263" y="96" font-size="9.5" fill="#555">适合：文本生成、对话、代码生成</text> <text x="263" y="111" font-size="9.5" fill="#555">代表：GPT 系列、LLaMA、Qwen</text> <text x="263" y="126" font-size="9.5" fill="#555">中文：ChatGLM、Baichuan</text> <text x="263" y="141" font-size="9.5" fill="#555">特点：逐词预测下一个词</text> <rect x="263" y="148" width="193" height="10" rx="3" fill="#eaf4fb"></rect><text x="359" y="157" text-anchor="middle" font-size="8" fill="#2980b9">输入 -&gt; 预测下一词 -&gt; 拼接再预测 -&gt; 循环</text> <rect x="485" y="38" width="220" height="125" rx="9" fill="#fff" stroke="#2ecc71" stroke-width="1.8"></rect><rect x="485" y="38" width="220" height="6" rx="9" fill="#2ecc71"></rect><text x="595" y="60" text-anchor="middle" font-size="12" font-weight="bold" fill="#27ae60">Encoder-Decoder 模型</text> <text x="595" y="76" text-anchor="middle" font-size="10" fill="#555">序列到序列（Seq2Seq）任务</text> <text x="498" y="96" font-size="9.5" fill="#555">适合：翻译、摘要、问答生成</text> <text x="498" y="111" font-size="9.5" fill="#555">代表：T5、BART、mT5</text> <text x="498" y="126" font-size="9.5" fill="#555">中文：mT5、PEGASUS-Chinese</text> <text x="498" y="141" font-size="9.5" fill="#555">特点：编码输入，解码生成输出</text> <rect x="498" y="148" width="193" height="10" rx="3" fill="#eafaf1"></rect><text x="594" y="157" text-anchor="middle" font-size="8" fill="#27ae60">源序列 -&gt; Encoder -&gt; Decoder -&gt; 目标序列</text></svg>

---

## 安装与环境配置

### 安装

```
# 基础安装
pip install transformers

# 完整安装（包含训练依赖）
pip install transformers[torch]       # PyTorch 后端（推荐）
pip install transformers[tf-cpu]      # TensorFlow 后端
pip install transformers[flax]        # JAX/Flax 后端

# 常用配套库
pip install datasets          # HuggingFace 数据集库
pip install evaluate          # 模型评估指标
pip install accelerate        # 多GPU/混合精度训练
pip install peft              # 参数高效微调（LoRA等）
pip install tokenizers        # 高性能分词器
pip install sentencepiece     # 部分模型（T5/LLaMA）需要

# 验证安装
python -c "import transformers; print(transformers.__version__)"
```

### 环境变量配置

```
# 设置模型缓存目录（模型下载后缓存到此路径，默认 ~/.cache/huggingface）
export HF_HOME=/data/huggingface_cache

# 国内用户：使用镜像站加速下载（推荐 hf-mirror.com）
export HF_ENDPOINT=https://hf-mirror.com

# 离线模式（网络不可用时，只使用已缓存的模型）
export TRANSFORMERS_OFFLINE=1

# 禁用进度条（CI/CD 环境）
export DISABLE_TQDM=1
```

## 实例

\# 也可以在代码中设置  
import os  
os.environ\["HF\_ENDPOINT"\] = "https://hf-mirror.com"  
  
\# 查看当前缓存目录  
from transformers.utils import TRANSFORMERS\_CACHE  
print(TRANSFORMERS\_CACHE)

---

## Pipeline：五行代码跑 AI

Pipeline 是 Transformers 最高级别的抽象，把模型加载、预处理、推理、后处理全部封装好，三到五行代码即可完成推理。

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="200" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a1a2e">Pipeline 内部工作流程</text> <rect x="18" y="50" width="118" height="115" rx="9" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="1.5"></rect><text x="77" y="74" text-anchor="middle" font-size="12" fill="#2c3e50" font-weight="bold">原始输入</text> <text x="77" y="95" text-anchor="middle" font-size="9" fill="#888">文本 / 图像</text> <text x="77" y="110" text-anchor="middle" font-size="9" fill="#888">音频 / 等数据</text> <polygon points="140,107 156,100 156,114" fill="#bbb"></polygon><rect x="160" y="50" width="130" height="115" rx="9" fill="#fdecea" stroke="#e74c3c" stroke-width="1.5"></rect><text x="225" y="74" text-anchor="middle" font-size="12" fill="#c0392b" font-weight="bold">预处理</text> <text x="225" y="95" text-anchor="middle" font-size="9" fill="#888">Tokenizer 分词</text> <text x="225" y="110" text-anchor="middle" font-size="9" fill="#888">转为 token IDs</text> <text x="225" y="125" text-anchor="middle" font-size="9" fill="#888">Padding/Truncation</text> <polygon points="293,107 309,100 309,114" fill="#bbb"></polygon><rect x="312" y="50" width="130" height="115" rx="9" fill="#eaf4fb" stroke="#3498db" stroke-width="1.5"></rect><text x="377" y="74" text-anchor="middle" font-size="12" fill="#2980b9" font-weight="bold">模型推理</text> <text x="377" y="95" text-anchor="middle" font-size="9" fill="#888">前向传播</text> <text x="377" y="110" text-anchor="middle" font-size="9" fill="#888">输出 logits</text> <text x="377" y="125" text-anchor="middle" font-size="9" fill="#888">或隐藏层向量</text> <polygon points="444,107 460,100 460,114" fill="#bbb"></polygon><rect x="463" y="50" width="130" height="115" rx="9" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="528" y="74" text-anchor="middle" font-size="12" fill="#27ae60" font-weight="bold">后处理</text> <text x="528" y="95" text-anchor="middle" font-size="9" fill="#888">Softmax/Argmax</text> <text x="528" y="110" text-anchor="middle" font-size="9" fill="#888">解码 token-&gt;文字</text> <text x="528" y="125" text-anchor="middle" font-size="9" fill="#888">格式化输出</text> <polygon points="595,107 611,100 611,114" fill="#bbb"></polygon><rect x="614" y="50" width="90" height="115" rx="9" fill="#f5eafb" stroke="#9b59b6" stroke-width="1.5"></rect><text x="659" y="74" text-anchor="middle" font-size="12" fill="#8e44ad" font-weight="bold">结果</text> <text x="659" y="95" text-anchor="middle" font-size="9" fill="#888">标签/分数</text> <text x="659" y="110" text-anchor="middle" font-size="9" fill="#888">生成文本</text> <text x="360" y="185" text-anchor="middle" font-size="10" fill="#888">Pipeline 自动完成全部步骤，用户只需传入原始输入，拿到格式化结果</text></svg>

### Pipeline 快速示例大全

## 实例

from transformers import pipeline  
  
\# 1. 情感分析（文本分类）  
classifier = pipeline("sentiment-analysis")  
result = classifier("I love using Hugging Face Transformers!")  
\# -> \[{'label': 'POSITIVE', 'score': 0.9998}\]  
  
\# 2. 文本生成  
generator = pipeline("text-generation", model="gpt2")  
result = generator("Once upon a time in a land far away,",  
max\_new\_tokens=50, num\_return\_sequences=1, temperature=0.8)  
  
\# 3. 填空（掩码语言模型）  
unmasker = pipeline("fill-mask", model="bert-base-uncased")  
result = unmasker("The capital of France is \[MASK\].")  
\# -> \[{'token\_str': 'paris', 'score': 0.9823},...\]  
  
\# 4. 命名实体识别（NER）  
ner = pipeline("ner", aggregation\_strategy="simple")  
result = ner("My name is John and I work at Google in New York.")  
\# -> \[{'entity\_group': 'PER', 'word': 'John', 'score': 0.998},...\]  
  
\# 5. 抽取式问答  
qa = pipeline("question-answering")  
result = qa(question="Who invented Python?",  
context="Python was created by Guido van Rossum in 1991.")  
\# -> {'answer': 'Guido van Rossum', 'score': 0.9887}  
  
\# 6. 文本摘要  
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  
result = summarizer(article, max\_length=60, min\_length=20)  
  
\# 7. 机器翻译  
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")  
result = translator("Hello, how are you today?")  
\# -> \[{'translation\_text': '你好，你今天怎么样？'}\]  
  
\# 8. 零样本分类（不需要专门训练）  
zero\_shot = pipeline("zero-shot-classification")  
result = zero\_shot("I love playing football",  
candidate\_labels=\["sports", "politics", "technology"\])  
\# -> {'labels': \['sports',...\], 'scores': \[0.972,...\]}

### Pipeline 进阶配置

## 实例

import torch  
from transformers import pipeline  
  
\# 指定 GPU  
pipe = pipeline("text-generation", model="gpt2", device=0)  
  
\# 指定精度（省显存）  
pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-hf",  
torch\_dtype=torch.float16, device\_map="auto")  
  
\# 批量处理（提升吞吐量）  
pipe = pipeline("sentiment-analysis", batch\_size=32)  
results = pipe(large\_text\_list) # 自动分批推理  
  
\# 大文本分块处理  
asr = pipeline("automatic-speech-recognition",  
model="openai/whisper-large-v2",  
chunk\_length\_s=30, stride\_length\_s=5)  
result = asr("long\_audio.wav", return\_timestamps=True)

---

## Tokenizer 深度解析

Tokenizer 是 NLP 的第一步：把原始文本转换成模型能理解的数字序列。

### Tokenization 完整流程

<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="320" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a1a2e">Tokenization 完整过程：文本 -&gt; 模型输入</text> <rect x="18" y="50" width="680" height="40" rx="7" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="1.5"></rect><text x="35" y="68" font-size="10" fill="#555" font-weight="bold">Step 1 原始文本：</text> <text x="160" y="68" font-size="11" fill="#1a1a2e" font-family="monospace">"Hello, I'm learning Transformers! It's great."</text> <line x1="360" y1="90" x2="360" y2="108" stroke="#bbb" stroke-width="1.5"></line><polygon points="355,108 360,118 365,108" fill="#bbb"></polygon><rect x="18" y="120" width="680" height="52" rx="7" fill="#fdecea" stroke="#e74c3c" stroke-width="1.5"></rect><text x="35" y="140" font-size="10" fill="#c0392b" font-weight="bold">Step 2 分词（Tokenize）：</text> <text x="35" y="158" font-size="10" fill="#1a1a2e" font-family="monospace">["Hello", ",", "I", "'m", "learning", "Transform", "##ers", "!",...]</text> <text x="35" y="168" font-size="9" fill="#888">WordPiece/BPE 子词分词：罕见词被拆分（Transformers -&gt; Transform + ##ers）</text> <line x1="360" y1="172" x2="360" y2="188" stroke="#bbb" stroke-width="1.5"></line><polygon points="355,188 360,198 365,188" fill="#bbb"></polygon><rect x="18" y="200" width="680" height="50" rx="7" fill="#fef9ec" stroke="#f39c12" stroke-width="1.5"></rect><text x="35" y="220" font-size="10" fill="#e67e22" font-weight="bold">Step 3 添加特殊标记：</text> <text x="35" y="238" font-size="10" fill="#1a1a2e" font-family="monospace">["[CLS]", "Hello", ",", "I", "'m", "learning", "Transform", "##ers",... "[SEP]"]</text> <text x="35" y="246" font-size="9" fill="#888">[CLS]分类标记 [SEP]分隔符 [PAD]填充；不同模型特殊标记不同</text> <line x1="360" y1="250" x2="360" y2="266" stroke="#bbb" stroke-width="1.5"></line><polygon points="355,266 360,276 365,266" fill="#bbb"></polygon><rect x="18" y="278" width="680" height="34" rx="7" fill="#eaf4fb" stroke="#3498db" stroke-width="1.5"></rect><text x="35" y="294" font-size="10" fill="#2980b9" font-weight="bold">Step 4 转换为 Token IDs：</text> <text x="195" y="294" font-size="10" fill="#1a1a2e" font-family="monospace">[101, 7592, 1010, 1045, 1005, 1049, 4083, 19081, 2121,... 102]</text> <text x="35" y="308" font-size="9" fill="#888">每个 token 映射到词表中的整数索引，送入模型 Embedding 层</text></svg>

### Tokenizer 核心用法

## 实例

from transformers import AutoTokenizer  
  
\# 加载 Tokenizer  
tokenizer = AutoTokenizer.from\_pretrained("bert-base-uncased")  
  
\# 一步完成编码  
encoding = tokenizer(  
"Hello, I'm learning Transformers!",  
return\_tensors="pt", # 返回 PyTorch tensor  
padding=True, # 填充到最长序列  
truncation=True, # 超出长度时截断  
max\_length=128, # 最大长度  
)  
  
print(encoding.keys())  
\# -> dict\_keys(\['input\_ids', 'token\_type\_ids', 'attention\_mask'\])  
  
print(encoding\["input\_ids"\]\[0\]\[:8\])  
\# -> tensor(\[101, 7592, 1010, 1045, 1005, 1049, 4083, 19081\])  
  
print(encoding\["attention\_mask"\]\[0\]\[:8\])  
\# -> tensor(\[1, 1, 1, 1, 1, 1, 1, 1\]) # 1=真实token, 0=填充  
  
\# 解码（ID -> 文本）  
decoded = tokenizer.decode(encoding\["input\_ids"\]\[0\], skip\_special\_tokens=True)  
print(decoded) # -> "hello, i'm learning transformers!"  
  
\# 批量编码（自动 padding 对齐）  
texts = \["Short.", "This is a much longer sentence for testing."\]  
batch = tokenizer(texts, padding=True, truncation=True, return\_tensors="pt")  
print(batch\["input\_ids"\].shape) # -> torch.Size(\[2, 10\])  
  
\# 词表信息  
print(f"词表大小: {tokenizer.vocab\_size}") # -> 30522  
print(f"\[CLS\] ID: {tokenizer.cls\_token\_id}") # -> 101  
print(f"\[SEP\] ID: {tokenizer.sep\_token\_id}") # -> 102  
print(f"最大长度: {tokenizer.model\_max\_length}") # -> 512

### 常见 Tokenizer 类型对比

<svg viewBox="0 0 720 185" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="185" fill="#f8f9fa" rx="12"></rect><text x="360" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">三种主流分词算法对比</text> <rect x="15" y="36" width="690" height="28" fill="#1a1a2e" rx="6"></rect><text x="105" y="55" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">算法</text> <text x="270" y="55" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">原理</text> <text x="460" y="55" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">示例分词</text> <text x="635" y="55" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">代表模型</text> <rect x="15" y="66" width="690" height="36" fill="#fff" rx="3"></rect><text x="105" y="85" text-anchor="middle" font-size="11" fill="#e74c3c" font-weight="bold">BPE</text> <text x="105" y="98" text-anchor="middle" font-size="9" fill="#888">Byte Pair Encoding</text> <text x="270" y="80" text-anchor="middle" font-size="9.5" fill="#555">统计高频字符对合并</text> <text x="270" y="94" text-anchor="middle" font-size="9.5" fill="#555">学习最优子词词表</text> <text x="460" y="80" text-anchor="middle" font-size="9" fill="#555" font-family="monospace">"transformers" -&gt;</text> <text x="460" y="95" text-anchor="middle" font-size="9" fill="#555" font-family="monospace">["transform", "ers"]</text> <text x="635" y="88" text-anchor="middle" font-size="9.5" fill="#e74c3c">GPT / RoBERTa</text> <rect x="15" y="104" width="690" height="36" fill="#fafafa" rx="3"></rect><text x="105" y="123" text-anchor="middle" font-size="11" fill="#3498db" font-weight="bold">WordPiece</text> <text x="270" y="118" text-anchor="middle" font-size="9.5" fill="#555">最大化语言模型概率</text> <text x="270" y="132" text-anchor="middle" font-size="9.5" fill="#555">## 前缀标记子词</text> <text x="460" y="118" text-anchor="middle" font-size="9" fill="#555" font-family="monospace">"transformers" -&gt;</text> <text x="460" y="133" text-anchor="middle" font-size="9" fill="#555" font-family="monospace">["transform", "##ers"]</text> <text x="635" y="126" text-anchor="middle" font-size="9.5" fill="#3498db">BERT / DistilBERT</text> <rect x="15" y="142" width="690" height="36" fill="#fff" rx="3"></rect><text x="105" y="158" text-anchor="middle" font-size="11" fill="#2ecc71" font-weight="bold">SentencePiece</text> <text x="105" y="170" text-anchor="middle" font-size="9" fill="#888">Unigram / BPE 变体</text> <text x="270" y="156" text-anchor="middle" font-size="9.5" fill="#555">语言无关，直接处理</text> <text x="270" y="170" text-anchor="middle" font-size="9.5" fill="#555">原始字节，开头标记词首</text> <text x="460" y="156" text-anchor="middle" font-size="9" fill="#555" font-family="monospace">"transformers" -&gt;</text> <text x="460" y="170" text-anchor="middle" font-size="9" fill="#555" font-family="monospace">["_transform", "ers"]</text> <text x="635" y="162" text-anchor="middle" font-size="9.5" fill="#2ecc71">T5 / LLaMA / Qwen</text></svg>

---

## 模型加载与推理

### AutoClass：自动选择正确的模型类

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="200" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">AutoClass 工作原理：自动匹配正确的模型架构</text> <rect x="18" y="50" width="180" height="55" rx="8" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="1.5"></rect><text x="108" y="72" text-anchor="middle" font-size="11" fill="#2c3e50" font-weight="bold">模型名称</text> <text x="108" y="90" text-anchor="middle" font-size="10" fill="#555" font-family="monospace">"bert-base-uncased"</text> <text x="108" y="104" text-anchor="middle" font-size="9" fill="#888">或本地路径</text> <polygon points="202,78 218,71 218,85" fill="#bbb"></polygon><rect x="222" y="42" width="200" height="70" rx="8" fill="#1a1a2e"></rect><text x="322" y="63" text-anchor="middle" font-size="11" fill="#f5a623" font-weight="bold">AutoClass</text> <text x="322" y="80" text-anchor="middle" font-size="9" fill="#aaa">读取 config.json</text> <text x="322" y="95" text-anchor="middle" font-size="9" fill="#aaa">匹配架构类型</text> <text x="322" y="108" text-anchor="middle" font-size="8" fill="#7f8c8d">AutoModel / AutoTokenizer /...</text> <polygon points="426,77 442,70 442,84" fill="#bbb"></polygon><rect x="446" y="42" width="260" height="70" rx="8" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="576" y="63" text-anchor="middle" font-size="11" fill="#27ae60" font-weight="bold">自动返回正确的类</text> <text x="576" y="80" text-anchor="middle" font-size="9" fill="#555">BertForSequenceClassification</text> <text x="576" y="94" text-anchor="middle" font-size="9" fill="#555">GPT2LMHeadModel</text> <text x="576" y="108" text-anchor="middle" font-size="9" fill="#555">T5ForConditionalGeneration...</text> <text x="360" y="138" text-anchor="middle" font-size="10" fill="#555" font-weight="bold">常用 AutoClass 速查：</text> <rect x="18" y="148" width="155" height="42" rx="6" fill="#fdecea" stroke="#e74c3c" stroke-width="1"></rect><text x="95" y="164" text-anchor="middle" font-size="9.5" fill="#c0392b" font-weight="bold">AutoTokenizer</text> <text x="95" y="180" text-anchor="middle" font-size="8.5" fill="#888">自动分词器</text> <rect x="183" y="148" width="165" height="42" rx="6" fill="#eaf4fb" stroke="#3498db" stroke-width="1"></rect><text x="265" y="164" text-anchor="middle" font-size="9.5" fill="#2980b9" font-weight="bold">AutoModel</text> <text x="265" y="180" text-anchor="middle" font-size="8.5" fill="#888">基础模型（输出隐藏层）</text> <rect x="358" y="148" width="200" height="42" rx="6" fill="#eafaf1" stroke="#2ecc71" stroke-width="1"></rect><text x="458" y="164" text-anchor="middle" font-size="9.5" fill="#27ae60" font-weight="bold">AutoModelForSeqClass</text> <text x="458" y="180" text-anchor="middle" font-size="8.5" fill="#888">文本分类任务</text> <rect x="568" y="148" width="135" height="42" rx="6" fill="#f5eafb" stroke="#9b59b6" stroke-width="1"></rect><text x="635" y="164" text-anchor="middle" font-size="9.5" fill="#8e44ad" font-weight="bold">AutoModelForCausalLM</text> <text x="635" y="180" text-anchor="middle" font-size="8.5" fill="#888">文本生成任务</text></svg>

## 实例

import torch  
from transformers import AutoTokenizer, AutoModelForSequenceClassification  
  
model\_name = "bert-base-uncased"  
tokenizer = AutoTokenizer.from\_pretrained(model\_name)  
model = AutoModelForSequenceClassification.from\_pretrained(  
model\_name, num\_labels=2, torch\_dtype=torch.float16, device\_map="auto"  
)  
  
\# 手动推理完整流程  
text = "Transformers is an amazing library!"  
  
\# 1. 编码  
inputs = tokenizer(text, return\_tensors="pt", truncation=True, max\_length=512)  
inputs = {k: v.to(model.device) for k, v in inputs.items()}  
  
\# 2. 前向传播  
with torch.no\_grad():  
outputs = model(\*\*inputs)  
  
\# 3. 解析输出  
logits = outputs.logits # shape: \[1, 2\]  
probs = torch.softmax(logits, dim=-1)  
pred = torch.argmax(probs, dim=-1).item()  
  
id2label = model.config.id2label # {0: 'LABEL\_0', 1: 'LABEL\_1'}  
print(f"预测类别: {id2label\[pred\]}, 置信度: {probs\[0\]\[pred\]:.4f}")

### 提取句子向量

## 实例

from transformers import AutoModel, AutoTokenizer  
import torch  
  
model = AutoModel.from\_pretrained("bert-base-uncased")  
tokenizer = AutoTokenizer.from\_pretrained("bert-base-uncased")  
  
def get\_sentence\_embedding(text: str) -> torch.Tensor:  
inputs = tokenizer(text, return\_tensors="pt", max\_length=512, truncation=True)  
with torch.no\_grad():  
outputs = model(\*\*inputs)  
\# 对所有 token 做均值池化（Mean Pooling）  
token\_embeddings = outputs.last\_hidden\_state # \[1, seq\_len, 768\]  
attention\_mask = inputs\["attention\_mask"\].unsqueeze(-1)  
mean\_embedding = (token\_embeddings \* attention\_mask).sum(1) / attention\_mask.sum(1)  
return mean\_embedding # \[1, 768\]  
  
vec = get\_sentence\_embedding("Hello world")  
print(vec.shape) # -> torch.Size(\[1, 768\])

---

## 十大常见任务实战

### 文本分类（情感分析）

## 实例

from transformers import AutoTokenizer, AutoModelForSequenceClassification  
import torch  
  
model\_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"  
tokenizer = AutoTokenizer.from\_pretrained(model\_name)  
model = AutoModelForSequenceClassification.from\_pretrained(model\_name)  
  
def predict\_sentiment(texts):  
inputs = tokenizer(texts, return\_tensors="pt", padding=True,  
truncation=True, max\_length=512)  
with torch.no\_grad():  
logits = model(\*\*inputs).logits  
probs = torch.softmax(logits, dim=-1)  
results = \[\]  
for i, t in enumerate(texts):  
pid = probs\[i\].argmax().item()  
results.append({"text": t, "label": model.config.id2label\[pid\],  
"score": round(probs\[i\]\[pid\].item(), 4)})  
return results  
  
print(predict\_sentiment(\["I love this!", "This is terrible."\]))  
\# -> \[{'text': 'I love this!', 'label': 'positive', 'score': 0.9756},...\]

### 文本生成（对话 / 续写）

## 实例

from transformers import AutoTokenizer, AutoModelForCausalLM  
import torch  
  
model\_name = "Qwen/Qwen2-1.5B-Instruct" # 阿里通义千问（支持中文）  
tokenizer = AutoTokenizer.from\_pretrained(model\_name)  
model = AutoModelForCausalLM.from\_pretrained(  
model\_name, torch\_dtype=torch.float16, device\_map="auto"  
)  
  
messages = \[  
{"role": "system", "content": "你是一个有用的 AI 助手。"},  
{"role": "user", "content": "请用三句话解释什么是 Transformer？"},  
\]  
text = tokenizer.apply\_chat\_template(messages, tokenize=False,  
add\_generation\_prompt=True)  
inputs = tokenizer(text, return\_tensors="pt").to(model.device)  
  
with torch.no\_grad():  
output\_ids = model.generate(  
\*\*inputs, max\_new\_tokens=300, temperature=0.7, top\_p=0.9,  
do\_sample=True, repetition\_penalty=1.1,  
pad\_token\_id=tokenizer.eos\_token\_id,  
)  
  
new\_tokens = output\_ids\[0\]\[inputs\["input\_ids"\].shape\[1\]:\]  
response = tokenizer.decode(new\_tokens, skip\_special\_tokens=True)  
print(response)

### 命名实体识别（NER）

## 实例

from transformers import pipeline  
  
ner = pipeline("ner", model="dslim/bert-base-NER", aggregation\_strategy="simple")  
result = ner("Elon Musk founded SpaceX in 2002 and Tesla Motors in 2003.")  
for entity in result:  
print(f"{entity\['word'\]:<20} -> {entity\['entity\_group'\]} ({entity\['score'\]:.3f})")  
  
\# 中文 NER  
ner\_cn = pipeline("ner", model="hfl/chinese-bert-wwm-ext-ner-msra",  
aggregation\_strategy="simple")  
result = ner\_cn("小明在北京大学读书，后来去了阿里巴巴工作。")

### 机器翻译

## 实例

from transformers import pipeline  
  
\# 英译中  
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")  
result = translator("Artificial intelligence is transforming the world.")  
print(result\[0\]\["translation\_text"\]) # -> 人工智能正在改变世界。  
  
\# 中译英  
translator\_zh = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")  
result = translator\_zh("人工智能正在改变世界。")  
print(result\[0\]\["translation\_text"\])

### 文本摘要

## 实例

from transformers import pipeline  
  
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  
result = summarizer(long\_text, max\_length=80, min\_length=30,  
do\_sample=False, no\_repeat\_ngram\_size=3)  
print(result\[0\]\["summary\_text"\])

---

## 微调（Fine-tuning）

微调是将预训练模型适配到你的特定任务和数据上，是 Transformers 最重要的应用场景。

### 微调流程全景

<svg viewBox="0 0 720 310" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="310" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a1a2e">Transformers 微调完整流程</text> <rect x="18" y="48" width="128" height="240" rx="9" fill="#fff" stroke="#e74c3c" stroke-width="1.5"></rect><rect x="18" y="48" width="128" height="5" rx="9" fill="#e74c3c"></rect><text x="82" y="68" text-anchor="middle" font-size="12" fill="#c0392b" font-weight="bold">准备数据</text> <text x="28" y="92" font-size="9" fill="#555">数据集加载</text> <text x="28" y="108" font-size="9" fill="#555">HF datasets</text> <text x="28" y="124" font-size="9" fill="#555">or 自定义 CSV</text> <text x="28" y="148" font-size="9" fill="#555">Tokenize 编码</text> <text x="28" y="164" font-size="9" fill="#555">Padding 对齐</text> <text x="28" y="180" font-size="9" fill="#555">DataLoader</text> <text x="28" y="210" font-size="9" fill="#e74c3c">关键：数据质量</text> <text x="28" y="224" font-size="9" fill="#e74c3c">&gt; 数据数量</text> <polygon points="150,168 165,161 165,175" fill="#bbb"></polygon><rect x="169" y="48" width="128" height="240" rx="9" fill="#fff" stroke="#f39c12" stroke-width="1.5"></rect><rect x="169" y="48" width="128" height="5" rx="9" fill="#f39c12"></rect><text x="233" y="68" text-anchor="middle" font-size="12" fill="#e67e22" font-weight="bold">加载模型</text> <text x="179" y="92" font-size="9" fill="#555">AutoModelForTask</text> <text x="179" y="108" font-size="9" fill="#555">指定 num_labels</text> <text x="179" y="124" font-size="9" fill="#555">冻结底层参数</text> <text x="179" y="148" font-size="9" fill="#555">（可选）</text> <text x="179" y="164" font-size="9" fill="#555">只微调顶层</text> <text x="179" y="210" font-size="9" fill="#e67e22">技巧：小数据集</text> <text x="179" y="224" font-size="9" fill="#e67e22">先冻结底层</text> <polygon points="301,168 316,161 316,175" fill="#bbb"></polygon><rect x="320" y="48" width="128" height="240" rx="9" fill="#fff" stroke="#2ecc71" stroke-width="1.5"></rect><rect x="320" y="48" width="128" height="5" rx="9" fill="#2ecc71"></rect><text x="384" y="68" text-anchor="middle" font-size="12" fill="#27ae60" font-weight="bold">训练配置</text> <text x="330" y="92" font-size="9" fill="#555">TrainingArguments</text> <text x="330" y="108" font-size="9" fill="#555">学习率：2e-5</text> <text x="330" y="124" font-size="9" fill="#555">Batch：32</text> <text x="330" y="140" font-size="9" fill="#555">Epochs：3~5</text> <text x="330" y="156" font-size="9" fill="#555">Warmup 步数</text> <text x="330" y="172" font-size="9" fill="#555">权重衰减</text> <text x="330" y="210" font-size="9" fill="#27ae60">技巧：学习率</text> <text x="330" y="224" font-size="9" fill="#27ae60">最重要</text> <polygon points="452,168 467,161 467,175" fill="#bbb"></polygon><rect x="471" y="48" width="128" height="240" rx="9" fill="#fff" stroke="#3498db" stroke-width="1.5"></rect><rect x="471" y="48" width="128" height="5" rx="9" fill="#3498db"></rect><text x="535" y="68" text-anchor="middle" font-size="12" fill="#2980b9" font-weight="bold">训练 &amp; 评估</text> <text x="481" y="92" font-size="9" fill="#555">Trainer.train()</text> <text x="481" y="108" font-size="9" fill="#555">监控 loss 曲线</text> <text x="481" y="124" font-size="9" fill="#555">验证集评估</text> <text x="481" y="140" font-size="9" fill="#555">Early stopping</text> <text x="481" y="156" font-size="9" fill="#555">保存最优 ckpt</text> <text x="481" y="210" font-size="9" fill="#2980b9">注意：过拟合</text> <text x="481" y="224" font-size="9" fill="#2980b9">对比基线</text> <polygon points="603,168 618,161 618,175" fill="#bbb"></polygon><rect x="622" y="48" width="80" height="240" rx="9" fill="#fff" stroke="#9b59b6" stroke-width="1.5"></rect><rect x="622" y="48" width="80" height="5" rx="9" fill="#9b59b6"></rect><text x="662" y="68" text-anchor="middle" font-size="12" fill="#8e44ad" font-weight="bold">保存</text> <text x="632" y="92" font-size="9" fill="#555">save_model()</text> <text x="632" y="108" font-size="9" fill="#555">save_pretrained</text> <text x="632" y="124" font-size="9" fill="#555">推送 Hub</text> <text x="632" y="148" font-size="9" fill="#888">生产部署</text> <text x="632" y="164" font-size="9" fill="#888">量化推理</text> <text x="632" y="180" font-size="9" fill="#888">ONNX 导出</text> <text x="360" y="305" text-anchor="middle" font-size="10" fill="#888">使用 HuggingFace Trainer 可以大幅简化训练流程，自动处理梯度累积、混合精度、分布式训练等</text></svg>

### 完整微调示例：文本分类

## 实例

from datasets import load\_dataset  
from transformers import (  
AutoTokenizer, AutoModelForSequenceClassification,  
TrainingArguments, Trainer, DataCollatorWithPadding,  
EarlyStoppingCallback,  
)  
import evaluate, numpy as np  
  
\# 1. 加载数据集  
dataset = load\_dataset("imdb") # HF Hub 公开数据集  
  
\# 2. Tokenizer + 预处理  
MODEL\_NAME = "bert-base-uncased"  
tokenizer = AutoTokenizer.from\_pretrained(MODEL\_NAME)  
  
def tokenize\_fn(examples):  
return tokenizer(examples\["text"\], truncation=True, max\_length=512)  
  
tokenized\_ds = dataset.map(tokenize\_fn, batched=True,  
remove\_columns=\["text"\])  
tokenized\_ds = tokenized\_ds.rename\_column("label", "labels")  
tokenized\_ds.set\_format("torch")  
data\_collator = DataCollatorWithPadding(tokenizer=tokenizer)  
  
\# 3. 加载模型  
model = AutoModelForSequenceClassification.from\_pretrained(  
MODEL\_NAME, num\_labels=2,  
id2label={0: "NEGATIVE", 1: "POSITIVE"},  
label2id={"NEGATIVE": 0, "POSITIVE": 1},  
)  
  
\# 4. 评估指标  
accuracy = evaluate.load("accuracy")  
f1 = evaluate.load("f1")  
def compute\_metrics(eval\_pred):  
logits, labels = eval\_pred  
preds = np.argmax(logits, axis=-1)  
return {"accuracy": accuracy.compute(predictions=preds, references=labels)\["accuracy"\],  
"f1": f1.compute(predictions=preds, references=labels, average="binary")\["f1"\]}  
  
\# 5. 训练参数  
training\_args = TrainingArguments(  
output\_dir="./results", num\_train\_epochs=3,  
per\_device\_train\_batch\_size=16, per\_device\_eval\_batch\_size=32,  
gradient\_accumulation\_steps=2, learning\_rate=2e-5,  
weight\_decay=0.01, warmup\_ratio=0.1,  
evaluation\_strategy="steps", eval\_steps=500,  
save\_strategy="steps", save\_steps=500,  
load\_best\_model\_at\_end=True, metric\_for\_best\_model="f1",  
fp16=True, logging\_steps=100, seed=42,  
)  
  
\# 6. 创建 Trainer 并训练  
trainer = Trainer(  
model=model, args=training\_args,  
train\_dataset=tokenized\_ds\["train"\],  
eval\_dataset=tokenized\_ds\["test"\],  
tokenizer=tokenizer, data\_collator=data\_collator,  
compute\_metrics=compute\_metrics,  
callbacks=\[EarlyStoppingCallback(early\_stopping\_patience=3)\],  
)  
trainer.train()  
  
\# 7. 评估并保存  
eval\_result = trainer.evaluate()  
print(f"准确率: {eval\_result\['eval\_accuracy'\]:.4f}")  
print(f"F1: {eval\_result\['eval\_f1'\]:.4f}")  
  
trainer.save\_model("./my-sentiment-model")  
tokenizer.save\_pretrained("./my-sentiment-model")

### LoRA 参数高效微调（推荐）

<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="220" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a1a2e">LoRA 原理：只训练低秩矩阵，冻结原始权重</text> <rect x="30" y="48" width="290" height="150" rx="9" fill="#fff" stroke="#e74c3c" stroke-width="1.8"></rect><rect x="30" y="48" width="290" height="6" rx="9" fill="#e74c3c"></rect><text x="175" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#c0392b">全量微调（Full Fine-tuning）</text> <rect x="50" y="82" width="250" height="50" rx="6" fill="#fdecea" stroke="#e74c3c" stroke-width="1"></rect><text x="175" y="107" text-anchor="middle" font-size="11" fill="#c0392b">W + ΔW</text> <text x="175" y="123" text-anchor="middle" font-size="9" fill="#888">更新全部权重矩阵</text> <text x="50" y="155" font-size="9" fill="#555">参数量：全部（如 7B 参数全训）</text> <text x="50" y="169" font-size="9" fill="#555">显存需求：极高（需 4x 模型大小）</text> <text x="50" y="183" font-size="9" fill="#e74c3c">成本：昂贵，需要大量 GPU</text> <rect x="400" y="48" width="290" height="150" rx="9" fill="#fff" stroke="#2ecc71" stroke-width="1.8"></rect><rect x="400" y="48" width="290" height="6" rx="9" fill="#2ecc71"></rect><text x="545" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#27ae60">LoRA 微调</text> <rect x="420" y="82" width="115" height="50" rx="6" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="1"></rect><text x="477" y="104" text-anchor="middle" font-size="11" fill="#7f8c8d">W（冻结）</text> <text x="477" y="120" text-anchor="middle" font-size="9" fill="#aaa">不参与训练</text> <text x="545" y="108" text-anchor="middle" font-size="14" fill="#555">+</text> <rect x="558" y="82" width="115" height="50" rx="6" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="615" y="101" text-anchor="middle" font-size="11" fill="#27ae60" font-weight="bold">B x A</text> <text x="615" y="115" text-anchor="middle" font-size="8" fill="#888">r &lt;&lt; d（低秩矩阵）</text> <text x="615" y="128" text-anchor="middle" font-size="8" fill="#2ecc71">只训练这里</text> <text x="420" y="155" font-size="9" fill="#555">参数量：原来的 0.1%～1%</text> <text x="420" y="169" font-size="9" fill="#555">显存需求：低（只存低秩矩阵梯度）</text> <text x="420" y="183" font-size="9" fill="#2ecc71">成本：单卡 24GB 可微调 7B</text> <text x="360" y="210" text-anchor="middle" font-size="10" fill="#888">LoRA 将 ΔW 分解为两个低秩矩阵，r 远小于 d（通常 r=8~64），大幅降低训练成本</text></svg>

## 实例

from peft import LoraConfig, get\_peft\_model, TaskType  
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments  
import torch  
  
model\_name = "meta-llama/Llama-2-7b-hf"  
model = AutoModelForCausalLM.from\_pretrained(  
model\_name, torch\_dtype=torch.float16, device\_map="auto",  
load\_in\_4bit=True, # 4-bit 量化加载（QLoRA），进一步省显存  
)  
  
\# 配置 LoRA  
lora\_config = LoraConfig(  
task\_type=TaskType.CAUSAL\_LM, r=16, lora\_alpha=32,  
lora\_dropout=0.05,  
target\_modules=\["q\_proj", "v\_proj", "k\_proj", "o\_proj"\],  
)  
  
model = get\_peft\_model(model, lora\_config)  
model.print\_trainable\_parameters()  
\# -> trainable: 4,194,304 || all: 6,742,609,920 || 0.0622%

> LoRA 优势：只训练不到 1% 的参数，显存降低 60-70%，速度快 2-3 倍，权重文件仅几 MB，可为同一基础模型保存多个 LoRA 适配器用于不同任务。

---

## 模型保存、加载与发布

## 实例

\# 本地保存  
model.save\_pretrained("./my-model")  
tokenizer.save\_pretrained("./my-model")  
  
\# 本地加载  
model = AutoModelForSequenceClassification.from\_pretrained("./my-model")  
tokenizer = AutoTokenizer.from\_pretrained("./my-model")  
  
\# 发布到 HuggingFace Hub  
from huggingface\_hub import login  
login(token="your\_hf\_token") # huggingface.co/settings/tokens  
model.push\_to\_hub("your-username/my-sentiment-model")  
tokenizer.push\_to\_hub("your-username/my-sentiment-model")  
  
\# 通过 Trainer 直接发布  
training\_args = TrainingArguments(  
output\_dir="your-username/my-model",  
push\_to\_hub=True, hub\_strategy="every\_save",  
)

---

## 性能优化技巧

### 推理加速全景

<svg viewBox="0 0 720 260" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="260" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a1a2e">推理加速技术栈：从简单到深度优化</text> <rect x="18" y="45" width="680" height="45" rx="8" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="30" y="63" font-size="11" fill="#27ae60" font-weight="bold">Level 1 - 零成本优化</text> <text x="30" y="81" font-size="9.5" fill="#555">torch.no_grad() 推理 | fp16/bf16 半精度 | batch 推理 | device_map="auto" 自动分配设备</text> <text x="550" y="72" font-size="9.5" fill="#27ae60">加速：1.5~2x</text> <rect x="18" y="100" width="680" height="45" rx="8" fill="#eaf4fb" stroke="#3498db" stroke-width="1.5"></rect><text x="30" y="118" font-size="11" fill="#2980b9" font-weight="bold">Level 2 - 量化（模型压缩）</text> <text x="30" y="136" font-size="9.5" fill="#555">bitsandbytes 4-bit/8-bit 量化 | GPTQ（后训练量化）| AWQ（激活感知量化）</text> <text x="550" y="127" font-size="9.5" fill="#3498db">加速：2~4x，显存减半</text> <rect x="18" y="155" width="680" height="45" rx="8" fill="#fef9ec" stroke="#f39c12" stroke-width="1.5"></rect><text x="30" y="173" font-size="11" fill="#e67e22" font-weight="bold">Level 3 - 编译与运行时优化</text> <text x="30" y="191" font-size="9.5" fill="#555">torch.compile()（PyTorch 2.0）| FlashAttention-2 | xFormers | Optimum（TensorRT/ONNX）</text> <text x="550" y="182" font-size="9.5" fill="#f39c12">加速：3~10x</text> <rect x="18" y="210" width="680" height="40" rx="8" fill="#fdecea" stroke="#e74c3c" stroke-width="1.5"></rect><text x="30" y="228" font-size="11" fill="#c0392b" font-weight="bold">Level 4 - 专用推理引擎</text> <text x="30" y="244" font-size="9.5" fill="#555">vLLM（LLM 高吞吐推理）| TGI | TensorRT-LLM | llama.cpp（CPU）</text> <text x="550" y="236" font-size="9.5" fill="#e74c3c">生产级，最高性能</text></svg>

## 实例

\# 4-bit 量化加载（13B 模型只需约 7GB 显存）  
from transformers import BitsAndBytesConfig, AutoModelForCausalLM  
import torch  
  
quant\_config = BitsAndBytesConfig(  
load\_in\_4bit=True, bnb\_4bit\_compute\_dtype=torch.float16,  
bnb\_4bit\_use\_double\_quant=True, bnb\_4bit\_quant\_type="nf4",  
)  
model = AutoModelForCausalLM.from\_pretrained(  
"meta-llama/Llama-2-13b-hf",  
quantization\_config=quant\_config, device\_map="auto",  
)  
  
\# FlashAttention-2 加速（需 pip install flash-attn）  
model = AutoModelForCausalLM.from\_pretrained(  
"mistralai/Mistral-7B-v0.1",  
attn\_implementation="flash\_attention\_2",  
torch\_dtype=torch.bfloat16, device\_map="auto",  
)  
  
\# torch.compile (PyTorch 2.0+)  
model = torch.compile(model, mode="reduce-overhead")

---

## 常见问题排查

<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="320" fill="#f8f9fa" rx="12"></rect><text x="360" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a1a2e">常见报错与解决方案速查</text> <rect x="15" y="36" width="690" height="28" fill="#1a1a2e" rx="6"></rect><text x="255" y="55" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">错误信息</text> <text x="555" y="55" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">原因与解决方案</text> <rect x="15" y="66" width="690" height="42" fill="#fff" rx="3"></rect><text x="25" y="82" font-size="9" fill="#e74c3c" font-family="monospace">CUDA out of memory</text> <text x="25" y="98" font-size="8.5" fill="#888">显存不足</text> <text x="270" y="82" font-size="9.5" fill="#555">减小 batch_size；加 gradient_accumulation_steps；用 fp16/4-bit；用更小模型</text> <rect x="15" y="110" width="690" height="42" fill="#fafafa" rx="3"></rect><text x="25" y="126" font-size="9" fill="#e74c3c" font-family="monospace">OSError: model not found</text> <text x="25" y="142" font-size="8.5" fill="#888">模型名称错误或网络问题</text> <text x="270" y="126" font-size="9.5" fill="#555">检查拼写；设置 HF_ENDPOINT 镜像；已下载则用本地路径</text> <rect x="15" y="154" width="690" height="42" fill="#fff" rx="3"></rect><text x="25" y="170" font-size="9" fill="#e74c3c" font-family="monospace">ValueError: num_labels mismatch</text> <text x="270" y="170" font-size="9.5" fill="#555">加载模型时显式指定 num_labels=你的类别数</text> <rect x="15" y="198" width="690" height="42" fill="#fafafa" rx="3"></rect><text x="25" y="214" font-size="9" fill="#e74c3c" font-family="monospace">tensors on different devices</text> <text x="270" y="214" font-size="9.5" fill="#555">inputs = {k: v.to(model.device) for k, v in inputs.items()}</text> <rect x="15" y="242" width="690" height="35" fill="#fff" rx="3"></rect><text x="25" y="258" font-size="9" fill="#e74c3c" font-family="monospace">loss = NaN / loss 不下降</text> <text x="270" y="258" font-size="9.5" fill="#555">检查学习率（太大会 NaN）；检查 labels 值域（0~N-1）；加 gradient_clipping</text> <rect x="15" y="279" width="690" height="35" fill="#fafafa" rx="3"></rect><text x="25" y="295" font-size="9" fill="#e74c3c" font-family="monospace">slow tokenizer / 速度慢</text> <text x="270" y="295" font-size="9.5" fill="#555">pip install tokenizers 安装 Rust 快速版本；使用 use_fast=True（默认）</text></svg>

---

## 总结与学习路径

<svg viewBox="0 0 720 250" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="250" fill="#1a1a2e" rx="12"></rect><text x="360" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#fff">Transformers 学习路径与核心知识点</text> <rect x="15" y="48" width="160" height="165" rx="10" fill="#e74c3c" opacity="0.9"></rect><text x="95" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">第一阶段</text> <text x="95" y="86" text-anchor="middle" font-size="10" fill="#fcc">入门（1周）</text> <text x="25" y="108" font-size="9" fill="#fff">pip install 配置环境</text> <text x="25" y="124" font-size="9" fill="#fff">Pipeline 跑通 5 个任务</text> <text x="25" y="140" font-size="9" fill="#fff">理解 Tokenizer 流程</text> <text x="25" y="156" font-size="9" fill="#fff">AutoModel 手动推理</text> <text x="25" y="172" font-size="9" fill="#fff">理解 Encoder/Decoder</text> <text x="25" y="188" font-size="9" fill="#fff">读懂模型输出结构</text> <polygon points="178,130 193,123 193,137" fill="#aaa"></polygon><rect x="197" y="48" width="160" height="165" rx="10" fill="#f39c12" opacity="0.9"></rect><text x="277" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">第二阶段</text> <text x="277" y="86" text-anchor="middle" font-size="10" fill="#fde">进阶（2周）</text> <text x="207" y="108" font-size="9" fill="#fff">加载 Hub 上的模型</text> <text x="207" y="124" font-size="9" fill="#fff">文本分类微调实战</text> <text x="207" y="140" font-size="9" fill="#fff">Trainer API 熟练使用</text> <text x="207" y="156" font-size="9" fill="#fff">自定义数据集处理</text> <text x="207" y="172" font-size="9" fill="#fff">compute_metrics 评估</text> <text x="207" y="188" font-size="9" fill="#fff">保存发布到 Hub</text> <polygon points="360,130 375,123 375,137" fill="#aaa"></polygon><rect x="379" y="48" width="160" height="165" rx="10" fill="#2ecc71" opacity="0.9"></rect><text x="459" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">第三阶段</text> <text x="459" y="86" text-anchor="middle" font-size="10" fill="#d5f5e3">高级（3周）</text> <text x="389" y="108" font-size="9" fill="#fff">LoRA / PEFT 微调</text> <text x="389" y="124" font-size="9" fill="#fff">量化（4-bit/8-bit）</text> <text x="389" y="140" font-size="9" fill="#fff">多模态模型使用</text> <text x="389" y="156" font-size="9" fill="#fff">自定义训练循环</text> <text x="389" y="172" font-size="9" fill="#fff">Accelerate 多 GPU</text> <text x="389" y="188" font-size="9" fill="#fff">FlashAttention 加速</text> <polygon points="542,130 557,123 557,137" fill="#aaa"></polygon><rect x="561" y="48" width="145" height="165" rx="10" fill="#3498db" opacity="0.9"></rect><text x="633" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">第四阶段</text> <text x="633" y="86" text-anchor="middle" font-size="10" fill="#d6eaf8">专家（持续）</text> <text x="571" y="108" font-size="9" fill="#fff">自定义模型架构</text> <text x="571" y="124" font-size="9" fill="#fff">预训练从头开始</text> <text x="571" y="140" font-size="9" fill="#fff">vLLM 生产部署</text> <text x="571" y="156" font-size="9" fill="#fff">RLHF/DPO 对齐</text> <text x="571" y="172" font-size="9" fill="#fff">贡献开源模型</text> <text x="571" y="188" font-size="9" fill="#fff">研究前沿论文</text> <text x="360" y="230" text-anchor="middle" font-size="10" fill="#aaa">每个阶段都应动手实践：找一个真实数据集，跑通训练-&gt;评估-&gt;发布的完整流程</text></svg>

### 关键 API 速查

## 实例

\# 1. 加载分词器  
tokenizer = AutoTokenizer.from\_pretrained("model\_name")  
  
\# 2. 编码文本  
inputs = tokenizer(text, return\_tensors="pt", truncation=True, max\_length=512)  
  
\# 3. 加载模型  
model = AutoModelForSequenceClassification.from\_pretrained("model\_name", num\_labels=N)  
  
\# 4. 推理  
with torch.no\_grad():  
outputs = model(\*\*inputs)  
  
\# 5. Pipeline  
pipe = pipeline("task\_name", model="model\_name")  
  
\# 6. 训练配置  
args = TrainingArguments(output\_dir="./out", num\_train\_epochs=3, learning\_rate=2e-5)  
  
\# 7. 训练  
trainer = Trainer(model=model, args=args, train\_dataset=ds, compute\_metrics=fn)  
  
\# 8. 保存  
model.save\_pretrained("./my-model")  
tokenizer.save\_pretrained("./my-model")  
  
\# 9. 数据集  
dataset = load\_dataset("dataset\_name")  
dataset = dataset.map(tokenize\_fn, batched=True)  
  
\# 10. LoRA  
config = LoraConfig(r=16, lora\_alpha=32, target\_modules=\["q\_proj","v\_proj"\])  
model = get\_peft\_model(model, config)

---