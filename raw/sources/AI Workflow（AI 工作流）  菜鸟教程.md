---
title: "AI Workflow（AI 工作流） | 菜鸟教程"
source: "https://www.runoob.com/ai-agent/ai-workflow.html"
author:
published:
created: 2026-06-17
description: "AI Workflow（AI 工作流）  AI Workflow（AI 工作流）是将多个 AI 模型调用、工具使用、数据处理步骤有序组合成一条自动化流水线的系统。 单独调用一次 LLM 能回答问题，但现实任务往往需要：查网页 → 提取信息 → 分析 → 写报告 → 发送邮件。AI Workflow 就是把这些步骤串起来，让 AI 自动完成完整任务，而不只是回答一句话。  一个直观的类比 想象一个装配流水线：   模式类比说明 单次 LL.."
tags:
  - "clippings"
---
## AI Workflow（AI 工作流）

AI Workflow（AI 工作流）是将多个 AI 模型调用、工具使用、数据处理步骤有序组合成一条自动化流水线的系统。

单独调用一次 LLM 能回答问题，但现实任务往往需要：查网页 → 提取信息 → 分析 → 写报告 → 发送邮件。AI Workflow 就是把这些步骤串起来，让 AI 自动完成完整任务，而不只是回答一句话。

### 一个直观的类比

想象一个装配流水线：

| 模式 | 类比 | 说明 |
| --- | --- | --- |
| 单次 LLM 调用 | 像一个工匠 | 给他一块铁，他还给你一把剑 |
| AI Workflow | 像整条流水线 | 原料进去，自动经过冶炼 → 锻造 → 淬火 → 打磨 → 包装，成品出来 |

每个步骤可以是 AI 模型、代码函数、外部 API，或者人工审核节点。

### 从问答到做事的进化

<svg viewBox="0 0 720 260" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="260" fill="#f8f9fa" rx="12"></rect><text x="360" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">AI 能力的三个层次</text> <rect x="30" y="48" width="195" height="185" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.5"></rect><rect x="30" y="48" width="195" height="8" rx="10" fill="#95a5a6"></rect><text x="127" y="72" text-anchor="middle" font-size="13" font-weight="bold" fill="#7f8c8d">第一层：单次问答</text> <text x="127" y="100" text-anchor="middle" font-size="12" font-weight="bold" fill="#95a5a6">Q &amp; A</text> <text x="127" y="132" text-anchor="middle" font-size="10" fill="#555">用户输入 → LLM → 输出</text> <text x="47" y="155" font-size="10" fill="#888">示例：</text> <text x="47" y="170" font-size="10" fill="#888">"帮我写一首诗"</text> <text x="47" y="190" font-size="10" fill="#e74c3c">局限：只能单步</text> <text x="47" y="205" font-size="10" fill="#e74c3c">无法完成复杂任务</text> <text x="241" y="148" font-size="22" fill="#bbb">→</text> <rect x="263" y="48" width="195" height="185" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.5"></rect><rect x="263" y="48" width="195" height="8" rx="10" fill="#3498db"></rect><text x="360" y="72" text-anchor="middle" font-size="13" font-weight="bold" fill="#2980b9">第二层：Chain 链式调用</text> <text x="360" y="100" text-anchor="middle" font-size="12" font-weight="bold" fill="#3498db">Chain</text> <text x="360" y="132" text-anchor="middle" font-size="10" fill="#555">步骤A → 步骤B → 步骤C</text> <text x="280" y="155" font-size="10" fill="#888">示例：</text> <text x="280" y="170" font-size="10" fill="#888">翻译 → 摘要 → 润色</text> <text x="280" y="190" font-size="10" fill="#e67e22">局限：流程固定</text> <text x="280" y="205" font-size="10" fill="#e67e22">无法动态决策</text> <text x="474" y="148" font-size="22" fill="#bbb">→</text> <rect x="496" y="48" width="195" height="185" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.5"></rect><rect x="496" y="48" width="195" height="8" rx="10" fill="#e74c3c"></rect><text x="593" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#c0392b">第三层：AI Workflow</text> <text x="593" y="84" text-anchor="middle" font-size="9" fill="#c0392b">含 Agent</text> <text x="593" y="108" text-anchor="middle" font-size="12" font-weight="bold" fill="#e74c3c">Agent</text> <text x="593" y="135" text-anchor="middle" font-size="10" fill="#555">感知 → 规划 → 工具调用</text> <text x="593" y="150" text-anchor="middle" font-size="10" fill="#555">→ 反思 → 循环迭代</text> <text x="513" y="172" font-size="10" fill="#888">示例：研究竞品并生成报告</text> <text x="513" y="192" font-size="10" fill="#2ecc71">动态决策，可完成开放性任务</text> <text x="360" y="248" text-anchor="middle" font-size="10" fill="#888">AI Workflow 是当前 AI 应用落地的主要范式，也是 AI Agent 的实现基础</text></svg>

---

## 为什么需要 AI Workflow

### 单次调用的局限

一次 LLM 调用能完成的事情非常有限：

- 上下文窗口有限：无法一次读完一本书
- 无法访问实时信息：训练数据有截止日期
- 无法执行操作：不能真正发邮件、写代码并运行
- 无法自我校验：生成错误后无法意识到并修正
- 复杂任务容易出错：一步做太多事情导致质量下降

### AI Workflow 解决的五大核心问题

<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="300" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">AI Workflow 解决的五大核心问题</text> <rect x="18" y="45" width="130" height="235" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="18" y="45" width="130" height="6" rx="10" fill="#e74c3c"></rect><text x="83" y="72" text-anchor="middle" font-size="13" font-weight="bold" fill="#c0392b">任务分解</text> <text x="30" y="95" font-size="9.5" fill="#555">将复杂任务拆解</text> <text x="30" y="109" font-size="9.5" fill="#555">为多个小步骤</text> <text x="30" y="123" font-size="9.5" fill="#555">每步专注一件事</text> <text x="30" y="148" font-size="9" fill="#aaa">写报告 → 调研+</text> <text x="30" y="161" font-size="9" fill="#aaa">大纲+撰写+审校</text> <text x="30" y="190" font-size="9" fill="#e74c3c">提升准确率</text> <text x="30" y="203" font-size="9" fill="#e74c3c">降低单步压力</text> <rect x="158" y="45" width="130" height="235" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="158" y="45" width="130" height="6" rx="10" fill="#f39c12"></rect><text x="223" y="72" text-anchor="middle" font-size="13" font-weight="bold" fill="#e67e22">工具集成</text> <text x="170" y="95" font-size="9.5" fill="#555">调用搜索、数据库</text> <text x="170" y="109" font-size="9.5" fill="#555">代码执行器、API</text> <text x="170" y="123" font-size="9.5" fill="#555">等外部能力</text> <text x="170" y="148" font-size="9" fill="#aaa">搜索引擎、计算器</text> <text x="170" y="161" font-size="9" fill="#aaa">数据库、邮件服务</text> <text x="170" y="190" font-size="9" fill="#e67e22">突破知识边界</text> <text x="170" y="203" font-size="9" fill="#e67e22">连接真实世界</text> <rect x="298" y="45" width="130" height="235" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="298" y="45" width="130" height="6" rx="10" fill="#2ecc71"></rect><text x="363" y="72" text-anchor="middle" font-size="13" font-weight="bold" fill="#27ae60">迭代反思</text> <text x="310" y="95" font-size="9.5" fill="#555">AI 可以检验自身</text> <text x="310" y="109" font-size="9.5" fill="#555">输出，发现问题后</text> <text x="310" y="123" font-size="9.5" fill="#555">重新尝试修正</text> <text x="310" y="148" font-size="9" fill="#aaa">生成代码 → 运行</text> <text x="310" y="161" font-size="9" fill="#aaa">→ 报错 → 修复</text> <text x="310" y="190" font-size="9" fill="#2ecc71">自动纠错</text> <text x="310" y="203" font-size="9" fill="#2ecc71">质量更有保障</text> <rect x="438" y="45" width="130" height="235" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="438" y="45" width="130" height="6" rx="10" fill="#3498db"></rect><text x="503" y="72" text-anchor="middle" font-size="13" font-weight="bold" fill="#2980b9">并行处理</text> <text x="450" y="95" font-size="9.5" fill="#555">多个子任务同时</text> <text x="450" y="109" font-size="9.5" fill="#555">执行，不必排队</text> <text x="450" y="123" font-size="9.5" fill="#555">等待前一步完成</text> <text x="450" y="148" font-size="9" fill="#aaa">同时分析财务</text> <text x="450" y="161" font-size="9" fill="#aaa">技术、市场三维度</text> <text x="450" y="190" font-size="9" fill="#3498db">大幅提升效率</text> <text x="450" y="203" font-size="9" fill="#3498db">节省运行时间</text> <rect x="578" y="45" width="130" height="235" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="578" y="45" width="130" height="6" rx="10" fill="#9b59b6"></rect><text x="643" y="72" text-anchor="middle" font-size="13" font-weight="bold" fill="#8e44ad">可观测性</text> <text x="590" y="95" font-size="9.5" fill="#555">每一步的输入输出</text> <text x="590" y="109" font-size="9.5" fill="#555">都可以被记录</text> <text x="590" y="123" font-size="9.5" fill="#555">监控和调试</text> <text x="590" y="148" font-size="9" fill="#aaa">日志、追踪</text> <text x="590" y="161" font-size="9" fill="#aaa">错误定位</text> <text x="590" y="190" font-size="9" fill="#9b59b6">生产级别可靠</text> <text x="590" y="203" font-size="9" fill="#9b59b6">便于排查问题</text></svg>

---

## 核心组成要素

一个完整的 AI Workflow 由以下核心要素构成。

<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="380" fill="#f8f9fa" rx="12"></rect><text x="360" y="15" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">AI Workflow 核心架构组成</text> <ellipse cx="360" cy="195" rx="68" ry="48" fill="#1a1a2e"></ellipse><text x="360" y="188" text-anchor="middle" font-size="13" fill="#fff" font-weight="bold">AI</text> <text x="360" y="204" text-anchor="middle" font-size="13" fill="#fff" font-weight="bold">Workflow</text> <text x="360" y="218" text-anchor="middle" font-size="10" fill="#aaa">编排引擎</text> <line x1="295" y1="165" x2="175" y2="98" stroke="#e74c3c" stroke-width="2"></line><rect x="60" y="52" width="115" height="78" rx="9" fill="#fdecea" stroke="#e74c3c" stroke-width="1.5"></rect><text x="117" y="76" text-anchor="middle" font-size="12" font-weight="bold" fill="#c0392b">LLM/模型</text> <text x="72" y="93" font-size="9" fill="#777">GPT-4、Claude</text> <text x="72" y="105" font-size="9" fill="#777">Gemini、本地模型</text> <text x="72" y="117" font-size="9" fill="#777">Workflow 的大脑</text> <line x1="340" y1="148" x2="305" y2="60" stroke="#f39c12" stroke-width="2"></line><rect x="232" y="18" width="115" height="78" rx="9" fill="#fef5e7" stroke="#f39c12" stroke-width="1.5"></rect><text x="289" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#e67e22">工具/Tools</text> <text x="244" y="59" font-size="9" fill="#777">搜索、代码执行</text> <text x="244" y="71" font-size="9" fill="#777">数据库、外部 API</text> <text x="244" y="83" font-size="9" fill="#777">与外部交互</text> <line x1="419" y1="150" x2="455" y2="62" stroke="#2ecc71" stroke-width="2"></line><rect x="390" y="18" width="115" height="78" rx="9" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="447" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#27ae60">记忆/Memory</text> <text x="400" y="59" font-size="9" fill="#777">短期：对话历史</text> <text x="400" y="71" font-size="9" fill="#777">长期：向量数据库</text> <text x="400" y="83" font-size="9" fill="#777">跨会话持久化</text> <line x1="425" y1="195" x2="545" y2="160" stroke="#3498db" stroke-width="2"></line><rect x="547" y="112" width="115" height="78" rx="9" fill="#eaf4fb" stroke="#3498db" stroke-width="1.5"></rect><text x="604" y="136" text-anchor="middle" font-size="12" font-weight="bold" fill="#2980b9">状态/State</text> <text x="557" y="153" font-size="9" fill="#777">任务进度、中间</text> <text x="557" y="165" font-size="9" fill="#777">结果、上下文传递</text> <text x="557" y="177" font-size="9" fill="#777">如同接力棒</text> <line x1="415" y1="235" x2="530" y2="270" stroke="#9b59b6" stroke-width="2"></line><rect x="530" y="250" width="130" height="78" rx="9" fill="#f5eafb" stroke="#9b59b6" stroke-width="1.5"></rect><text x="595" y="274" text-anchor="middle" font-size="12" font-weight="bold" fill="#8e44ad">人工介入</text> <text x="540" y="291" font-size="9" fill="#777">审核、反馈</text> <text x="540" y="303" font-size="9" fill="#777">纠正、授权</text> <text x="540" y="315" font-size="9" fill="#777">高风险操作暂停</text> <line x1="305" y1="228" x2="195" y2="272" stroke="#e67e22" stroke-width="2"></line><rect x="60" y="252" width="130" height="78" rx="9" fill="#fef5e7" stroke="#e67e22" stroke-width="1.5"></rect><text x="125" y="276" text-anchor="middle" font-size="12" font-weight="bold" fill="#d35400">路由/条件</text> <text x="70" y="293" font-size="9" fill="#777">根据条件决定</text> <text x="70" y="305" font-size="9" fill="#777">走哪条执行路径</text> <text x="70" y="317" font-size="9" fill="#777">分支、循环、跳转</text> <line x1="293" y1="193" x2="175" y2="200" stroke="#2c3e50" stroke-width="2"></line><rect x="60" y="162" width="115" height="62" rx="9" fill="#ecf0f1" stroke="#2c3e50" stroke-width="1.5"></rect><text x="117" y="185" text-anchor="middle" font-size="11" font-weight="bold" fill="#2c3e50">输入/输出</text> <text x="70" y="200" font-size="9" fill="#777">文本、图像、文件</text> <text x="70" y="213" font-size="9" fill="#777">结构化数据</text> <text x="360" y="360" text-anchor="middle" font-size="10" fill="#888">各组件由编排引擎（LangChain / LlamaIndex / Dify 等）统一调度协作</text></svg>

### 各要素详解

LLM（大语言模型） - Workflow 的"大脑"，负责推理、生成、决策。常用：GPT-4o、Claude 3.5、Gemini 1.5、本地 Llama 3。

工具（Tools） - 让 AI 能与外部世界交互的接口，包括：搜索引擎（Tavily、Serper、Bing）、代码执行器（Python REPL、沙箱环境）、数据库查询（SQL、向量 DB）、外部 API（天气、股票、邮件、日历）、文件操作（读写、解析 PDF/Excel）。

记忆（Memory） - 短期记忆存储当前会话对话历史（存在 prompt 里），长期记忆通过向量数据库 + RAG 实现跨会话持久存储，工作记忆维护任务执行中的中间状态。

状态（State） - 任务在各步骤之间传递的信息载体，如同接力棒，每一步都能读取前步结果并写入新结果。

路由/条件（Router） - 根据前一步输出动态决定下一步走向，实现分支、循环、跳转等复杂流程控制。

人工介入（Human in the Loop） - 在关键节点暂停等待人工确认，适用于高风险操作（如删除数据、发送邮件、财务操作）。

---

## 六大常见 Workflow 模式

以下是 AI Workflow 中最常用的六种设计模式，从简单到复杂，适用于不同场景。

### 模式一：顺序链（Sequential Chain）

最基础的模式，步骤 A → B → C 线性执行，上一步输出是下一步输入。

<svg viewBox="0 0 680 140" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="680" height="140" fill="#f8f9fa" rx="12"></rect><text x="340" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">模式一：顺序链（Sequential Chain）</text> <rect x="18" y="45" width="90" height="60" rx="8" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="1.5"></rect><text x="63" y="72" text-anchor="middle" font-size="11" fill="#2c3e50" font-weight="bold">输入</text> <text x="63" y="88" text-anchor="middle" font-size="9" fill="#777">用户原始</text> <text x="63" y="100" text-anchor="middle" font-size="9" fill="#777">英文文章</text> <polygon points="110,75 125,68 125,82" fill="#bbb"></polygon><rect x="128" y="45" width="105" height="60" rx="8" fill="#fdecea" stroke="#e74c3c" stroke-width="1.5"></rect><text x="180" y="67" text-anchor="middle" font-size="10" font-weight="bold" fill="#c0392b">Step 1 翻译</text> <text x="180" y="81" text-anchor="middle" font-size="9" fill="#555">英文→中文</text> <text x="180" y="95" text-anchor="middle" font-size="9" fill="#555">GPT-4o</text> <polygon points="235,75 250,68 250,82" fill="#bbb"></polygon><rect x="253" y="45" width="105" height="60" rx="8" fill="#fef9ec" stroke="#f39c12" stroke-width="1.5"></rect><text x="305" y="67" text-anchor="middle" font-size="10" font-weight="bold" fill="#e67e22">Step 2 摘要</text> <text x="305" y="81" text-anchor="middle" font-size="9" fill="#555">提炼核心观点</text> <text x="305" y="95" text-anchor="middle" font-size="9" fill="#555">100字以内</text> <polygon points="360,75 375,68 375,82" fill="#bbb"></polygon><rect x="378" y="45" width="105" height="60" rx="8" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="430" y="67" text-anchor="middle" font-size="10" font-weight="bold" fill="#27ae60">Step 3 润色</text> <text x="430" y="81" text-anchor="middle" font-size="9" fill="#555">优化表达</text> <text x="430" y="95" text-anchor="middle" font-size="9" fill="#555">添加标题</text> <polygon points="485,75 500,68 500,82" fill="#bbb"></polygon><rect x="503" y="45" width="158" height="60" rx="8" fill="#eaf4fb" stroke="#3498db" stroke-width="1.5"></rect><text x="582" y="67" text-anchor="middle" font-size="11" fill="#2980b9" font-weight="bold">输出</text> <text x="582" y="81" text-anchor="middle" font-size="9" fill="#555">精炼中文摘要</text> <text x="582" y="95" text-anchor="middle" font-size="9" fill="#555">含标题与要点</text> <text x="340" y="128" text-anchor="middle" font-size="10" fill="#888">每步输出自动成为下一步的输入，线性流转，逻辑清晰</text></svg>

| 维度 | 说明 |
| --- | --- |
| 适用场景 | 文档处理流水线、内容生成、数据转换 |
| 优点 | 简单、可预测 |
| 缺点 | 僵硬，无法根据内容动态调整 |

### 模式二：条件路由（Conditional Routing）

根据某一步的输出内容，动态选择不同的后续路径。

<svg viewBox="0 0 680 220" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="680" height="220" fill="#f8f9fa" rx="12"></rect><text x="340" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">模式二：条件路由（Conditional Routing）</text> <rect x="18" y="80" width="110" height="55" rx="8" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="1.5"></rect><text x="73" y="100" text-anchor="middle" font-size="11" fill="#2c3e50" font-weight="bold">用户问题</text> <text x="73" y="115" text-anchor="middle" font-size="9" fill="#777">"怎么用 Python</text> <text x="73" y="127" text-anchor="middle" font-size="9" fill="#777">排序列表？"</text> <polygon points="130,107 145,100 145,114" fill="#bbb"></polygon><polygon points="230,80 295,107 230,135 165,107" fill="#f39c12" opacity="0.9"></polygon><text x="230" y="100" text-anchor="middle" font-size="10" fill="#fff" font-weight="bold">意图分类</text> <text x="230" y="114" text-anchor="middle" font-size="9" fill="#fff">Router</text> <line x1="295" y1="95" x2="350" y2="55" stroke="#3498db" stroke-width="1.5"></line><rect x="352" y="32" width="115" height="50" rx="8" fill="#eaf4fb" stroke="#3498db" stroke-width="1.5"></rect><text x="409" y="52" text-anchor="middle" font-size="10" font-weight="bold" fill="#2980b9">代码问题</text> <text x="409" y="68" text-anchor="middle" font-size="9" fill="#555">→ 代码生成 Agent</text> <polygon points="469,57 484,50 484,64" fill="#3498db"></polygon><rect x="486" y="32" width="160" height="50" rx="8" fill="#eaf4fb" stroke="#3498db" stroke-width="1"></rect><text x="566" y="52" text-anchor="middle" font-size="9" fill="#2980b9">运行代码验证</text> <text x="566" y="66" text-anchor="middle" font-size="9" fill="#2980b9">返回结果+解释</text> <line x1="295" y1="107" x2="350" y2="107" stroke="#2ecc71" stroke-width="1.5"></line><rect x="352" y="83" width="115" height="50" rx="8" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="409" y="103" text-anchor="middle" font-size="10" font-weight="bold" fill="#27ae60">知识问题</text> <text x="409" y="118" text-anchor="middle" font-size="9" fill="#555">→ RAG 知识库检索</text> <polygon points="469,107 484,100 484,114" fill="#2ecc71"></polygon><rect x="486" y="83" width="160" height="50" rx="8" fill="#eafaf1" stroke="#2ecc71" stroke-width="1"></rect><text x="566" y="103" text-anchor="middle" font-size="9" fill="#27ae60">召回相关文档</text> <text x="566" y="117" text-anchor="middle" font-size="9" fill="#27ae60">基于文档生成答案</text> <line x1="295" y1="120" x2="350" y2="160" stroke="#e74c3c" stroke-width="1.5"></line><rect x="352" y="136" width="115" height="50" rx="8" fill="#fdecea" stroke="#e74c3c" stroke-width="1.5"></rect><text x="409" y="156" text-anchor="middle" font-size="10" font-weight="bold" fill="#c0392b">实时问题</text> <text x="409" y="170" text-anchor="middle" font-size="9" fill="#555">→ 联网搜索</text> <polygon points="469,161 484,154 484,168" fill="#e74c3c"></polygon><rect x="486" y="136" width="160" height="50" rx="8" fill="#fdecea" stroke="#e74c3c" stroke-width="1"></rect><text x="566" y="156" text-anchor="middle" font-size="9" fill="#c0392b">搜索最新信息</text> <text x="566" y="170" text-anchor="middle" font-size="9" fill="#c0392b">整合成答案</text> <text x="340" y="205" text-anchor="middle" font-size="10" fill="#888">路由节点根据问题类型，将任务派发给最合适的处理分支</text></svg>

| 维度 | 说明 |
| --- | --- |
| 适用场景 | 智能客服、多功能助手、问题分类处理 |
| 优点 | 灵活，资源利用率高 |
| 缺点 | 路由逻辑需要精心设计，分类错误影响全流程 |

### 模式三：并行执行（Parallel Execution）

多个子任务同时运行，最后汇总结果。

![](https://www.runoob.com/wp-content/uploads/2026/05/ai-workflow-runoob.png)

| 维度 | 说明 |
| --- | --- |
| 适用场景 | 多维度分析、批量处理、独立子任务 |
| 优点 | 速度大幅提升 |
| 缺点 | 需要处理并发控制和结果合并逻辑 |

### 模式四：ReAct 循环（Reason + Act）

AI 先推理决定做什么，再行动调用工具，根据结果继续推理，循环直到任务完成。这是 AI Agent 的核心模式。

<svg viewBox="0 0 680 280" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="680" height="280" fill="#f8f9fa" rx="12"></rect><text x="340" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">模式四：ReAct 循环（Reason → Act → Observe → Repeat）</text> <rect x="20" y="50" width="130" height="55" rx="8" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="1.5"></rect><text x="85" y="72" text-anchor="middle" font-size="10" font-weight="bold" fill="#2c3e50">任务</text> <text x="85" y="87" text-anchor="middle" font-size="9" fill="#777">查询北京今天</text> <text x="85" y="100" text-anchor="middle" font-size="9" fill="#777">天气并推荐穿搭</text> <polygon points="152,77 167,70 167,84" fill="#bbb"></polygon><rect x="170" y="45" width="130" height="65" rx="8" fill="#fdecea" stroke="#e74c3c" stroke-width="1.5"></rect><text x="235" y="65" text-anchor="middle" font-size="11" font-weight="bold" fill="#c0392b">Thought 思考</text> <text x="235" y="80" text-anchor="middle" font-size="9" fill="#555">我需要先获取</text> <text x="235" y="93" text-anchor="middle" font-size="9" fill="#555">北京实时天气</text> <text x="235" y="106" text-anchor="middle" font-size="9" fill="#555">应调用天气 API</text> <polygon points="302,77 317,70 317,84" fill="#bbb"></polygon><rect x="320" y="45" width="130" height="65" rx="8" fill="#fef9ec" stroke="#f39c12" stroke-width="1.5"></rect><text x="385" y="65" text-anchor="middle" font-size="11" font-weight="bold" fill="#e67e22">Action 行动</text> <text x="385" y="80" text-anchor="middle" font-size="9" fill="#555">调用天气工具</text> <text x="385" y="93" text-anchor="middle" font-size="9" fill="#555">get_weather(</text> <text x="385" y="106" text-anchor="middle" font-size="9" fill="#555">city="北京")</text> <polygon points="452,77 467,70 467,84" fill="#bbb"></polygon><rect x="470" y="45" width="185" height="65" rx="8" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="562" y="65" text-anchor="middle" font-size="11" font-weight="bold" fill="#27ae60">Observation 观察</text> <text x="562" y="80" text-anchor="middle" font-size="9" fill="#555">返回：晴天，气温</text> <text x="562" y="93" text-anchor="middle" font-size="9" fill="#555">18°C，微风</text> <text x="562" y="106" text-anchor="middle" font-size="9" fill="#555">（工具执行结果）</text> <path d="M562,112 Q562,160 385,175 Q210,190 235,112" fill="none" stroke="#9b59b6" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrowLoop)"></path><defs><marker id="arrowLoop" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#9b59b6"></path></marker></defs><text x="395" y="178" text-anchor="middle" font-size="9" fill="#9b59b6">循环继续推理</text> <rect x="170" y="205" width="130" height="55" rx="8" fill="#fdecea" stroke="#e74c3c" stroke-width="1" stroke-dasharray="4,2"></rect><text x="235" y="222" text-anchor="middle" font-size="10" fill="#c0392b">Thought (第2轮)</text> <text x="235" y="236" text-anchor="middle" font-size="9" fill="#555">天气已知，现在可以</text> <text x="235" y="249" text-anchor="middle" font-size="9" fill="#555">直接给出穿搭建议</text> <polygon points="302,232 317,225 317,239" fill="#bbb"></polygon><rect x="320" y="198" width="320" height="65" rx="8" fill="#eaf4fb" stroke="#3498db" stroke-width="1.5"></rect><text x="480" y="219" text-anchor="middle" font-size="11" font-weight="bold" fill="#2980b9">Final Answer 最终答案</text> <text x="480" y="234" text-anchor="middle" font-size="9" fill="#555">北京今天晴，18°C，建议穿轻薄外套</text> <text x="480" y="248" text-anchor="middle" font-size="9" fill="#555">长裤+运动鞋，可带一件薄外套备用。</text> <text x="480" y="260" text-anchor="middle" font-size="9" fill="#2980b9">（任务完成，退出循环）</text> <text x="340" y="275" text-anchor="middle" font-size="10" fill="#888">每轮"思考→行动→观察"不断积累信息，直到 LLM 认为已可作出最终回答</text></svg>

| 维度 | 说明 |
| --- | --- |
| 适用场景 | AI Agent、复杂任务执行、开放式问题求解 |
| 优点 | 动态灵活，可处理未知情况 |
| 缺点 | 循环次数不可控，需要设定最大步数防止死循环 |

### 模式五：Plan & Execute（规划后执行）

先让 LLM 制定完整计划，再按计划逐步执行。与 ReAct 的区别是"先想清楚，再行动"。

<svg viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="680" height="160" fill="#f8f9fa" rx="12"></rect><text x="340" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">模式五：Plan &amp; Execute（先规划再执行）</text> <rect x="18" y="50" width="110" height="60" rx="8" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="1.5"></rect><text x="73" y="74" text-anchor="middle" font-size="10" font-weight="bold" fill="#2c3e50">任务目标</text> <text x="73" y="89" text-anchor="middle" font-size="9" fill="#777">调研竞品并写</text> <text x="73" y="102" text-anchor="middle" font-size="9" fill="#777">出分析报告</text> <polygon points="130,80 145,73 145,87" fill="#bbb"></polygon><rect x="148" y="40" width="145" height="80" rx="8" fill="#f5eafb" stroke="#9b59b6" stroke-width="1.8"></rect><text x="220" y="62" text-anchor="middle" font-size="11" font-weight="bold" fill="#8e44ad">Planner 规划</text> <text x="220" y="77" text-anchor="middle" font-size="9" fill="#555">1 搜集竞品信息</text> <text x="220" y="90" text-anchor="middle" font-size="9" fill="#555">2 提取关键特征</text> <text x="220" y="103" text-anchor="middle" font-size="9" fill="#555">3 对比分析</text> <text x="220" y="116" text-anchor="middle" font-size="9" fill="#555">4 撰写报告</text> <polygon points="295,80 310,73 310,87" fill="#bbb"></polygon><rect x="313" y="44" width="85" height="55" rx="7" fill="#fdecea" stroke="#e74c3c" stroke-width="1.2"></rect><text x="355" y="64" text-anchor="middle" font-size="10" font-weight="bold" fill="#c0392b">执行1</text> <text x="355" y="79" text-anchor="middle" font-size="9" fill="#555">搜索引擎</text> <text x="355" y="92" text-anchor="middle" font-size="9" fill="#555">调用 x3</text> <polygon points="400,71 413,64 413,78" fill="#bbb"></polygon><rect x="415" y="44" width="85" height="55" rx="7" fill="#fef9ec" stroke="#f39c12" stroke-width="1.2"></rect><text x="457" y="64" text-anchor="middle" font-size="10" font-weight="bold" fill="#e67e22">执行2+3</text> <text x="457" y="79" text-anchor="middle" font-size="9" fill="#555">LLM 提取</text> <text x="457" y="92" text-anchor="middle" font-size="9" fill="#555">对比分析</text> <polygon points="502,71 515,64 515,78" fill="#bbb"></polygon><rect x="517" y="44" width="145" height="55" rx="7" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.2"></rect><text x="589" y="64" text-anchor="middle" font-size="10" font-weight="bold" fill="#27ae60">执行4 → 输出</text> <text x="589" y="79" text-anchor="middle" font-size="9" fill="#555">生成 Markdown</text> <text x="589" y="92" text-anchor="middle" font-size="9" fill="#555">竞品分析报告</text> <text x="340" y="138" text-anchor="middle" font-size="10" fill="#888">Planner 只用一次 LLM 调用制定全局计划，后续各步骤严格按计划执行</text></svg>

### 模式六：多智能体协作（Multi-Agent）

多个专职 Agent 分工合作，每个 Agent 有自己的角色和工具集。

<svg viewBox="0 0 700 340" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="700" height="340" fill="#f8f9fa" rx="12"></rect><text x="350" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">模式六：多智能体协作（Multi-Agent）</text> <rect x="245" y="42" width="210" height="60" rx="10" fill="#1a1a2e"></rect><text x="350" y="66" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">协调者 Agent</text> <text x="350" y="82" text-anchor="middle" font-size="9" fill="#aaa">接收用户任务，分配给专职 Agent，汇总结果</text> <line x1="280" y1="102" x2="120" y2="148" stroke="#e74c3c" stroke-width="1.5"></line><line x1="325" y1="102" x2="265" y2="150" stroke="#f39c12" stroke-width="1.5"></line><line x1="375" y1="102" x2="435" y2="150" stroke="#2ecc71" stroke-width="1.5"></line><line x1="420" y1="102" x2="578" y2="148" stroke="#3498db" stroke-width="1.5"></line><rect x="28" y="150" width="185" height="100" rx="9" fill="#fdecea" stroke="#e74c3c" stroke-width="1.5"></rect><text x="120" y="172" text-anchor="middle" font-size="11" font-weight="bold" fill="#c0392b">研究员 Agent</text> <text x="43" y="190" font-size="9" fill="#555">工具：搜索引擎、网页抓取</text> <text x="43" y="204" font-size="9" fill="#555">职责：收集资料、整理事实</text> <text x="43" y="218" font-size="9" fill="#555">输出：结构化的信息摘要</text> <text x="43" y="238" font-size="9" fill="#e74c3c">↑ 向协调者汇报</text> <rect x="228" y="152" width="140" height="98" rx="9" fill="#fef9ec" stroke="#f39c12" stroke-width="1.5"></rect><text x="298" y="172" text-anchor="middle" font-size="11" font-weight="bold" fill="#e67e22">分析师 Agent</text> <text x="240" y="190" font-size="9" fill="#555">工具：计算器、Python</text> <text x="240" y="204" font-size="9" fill="#555">职责：数据分析、图表生成</text> <text x="240" y="218" font-size="9" fill="#555">输出：分析结论</text> <text x="240" y="238" font-size="9" fill="#e67e22">↑ 向协调者汇报</text> <rect x="382" y="152" width="140" height="98" rx="9" fill="#eafaf1" stroke="#2ecc71" stroke-width="1.5"></rect><text x="452" y="172" text-anchor="middle" font-size="11" font-weight="bold" fill="#27ae60">写作者 Agent</text> <text x="394" y="190" font-size="9" fill="#555">工具：文档模板</text> <text x="394" y="204" font-size="9" fill="#555">职责：撰写、润色报告</text> <text x="394" y="218" font-size="9" fill="#555">输出：最终文档</text> <text x="394" y="238" font-size="9" fill="#27ae60">↑ 向协调者汇报</text> <rect x="536" y="150" width="150" height="100" rx="9" fill="#eaf4fb" stroke="#3498db" stroke-width="1.5"></rect><text x="611" y="172" text-anchor="middle" font-size="11" font-weight="bold" fill="#2980b9">审核者 Agent</text> <text x="548" y="190" font-size="9" fill="#555">工具：事实核查工具</text> <text x="548" y="204" font-size="9" fill="#555">职责：检验准确性</text> <text x="548" y="218" font-size="9" fill="#555">输出：审核意见</text> <text x="548" y="238" font-size="9" fill="#3498db">↑ 向协调者汇报</text> <rect x="230" y="268" width="240" height="34" rx="8" fill="#f5eafb" stroke="#9b59b6" stroke-width="1.5"></rect><text x="350" y="289" text-anchor="middle" font-size="11" fill="#8e44ad" font-weight="bold">最终成果 → 用户</text> <line x1="350" y1="102" x2="350" y2="268" stroke="#9b59b6" stroke-width="1.5" stroke-dasharray="5,3"></line><text x="350" y="318" text-anchor="middle" font-size="10" fill="#888">各 Agent 专精一项技能，协调者统筹全局，分工合作效率远超单一 Agent</text></svg>

| 维度 | 说明 |
| --- | --- |
| 适用场景 | 复杂软件开发、科研辅助、企业自动化 |
| 优点 | 专职专用，质量更高，易于扩展 |
| 缺点 | 系统复杂度高，Agent 间通信需要精心设计 |

---

## 主流框架与工具对比

以下是当前最主流的 AI Workflow 框架全景对比，帮助你根据自身情况做出选择。

<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="420" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">AI Workflow 主流框架全景对比</text> <rect x="15" y="38" width="690" height="30" fill="#1a1a2e" rx="6"></rect><text x="88" y="58" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">框架</text> <text x="188" y="58" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">定位</text> <text x="305" y="58" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">核心特点</text> <text x="468" y="58" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">适合人群</text> <text x="612" y="58" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">学习曲线</text> <text x="683" y="58" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">开源</text> <rect x="15" y="70" width="690" height="52" fill="#fff" rx="3"></rect><rect x="15" y="70" width="6" height="52" fill="#e74c3c" rx="3"></rect><text x="88" y="88" text-anchor="middle" font-size="12" fill="#e74c3c" font-weight="bold">LangChain</text> <text x="88" y="105" text-anchor="middle" font-size="9" fill="#888">Python/JS</text> <text x="188" y="93" text-anchor="middle" font-size="10" fill="#444">代码优先框架</text> <text x="188" y="108" text-anchor="middle" font-size="9" fill="#888">最完整生态</text> <text x="305" y="86" text-anchor="middle" font-size="9.5" fill="#444">Chain、Agent、RAG 全覆盖</text> <text x="305" y="100" text-anchor="middle" font-size="9.5" fill="#444">工具集成数量最多（200+）</text> <text x="305" y="114" text-anchor="middle" font-size="9.5" fill="#444">LangSmith 可观测平台</text> <text x="468" y="93" text-anchor="middle" font-size="9.5" fill="#444">有 Python 基础的开发者</text> <text x="468" y="108" text-anchor="middle" font-size="9.5" fill="#444">需要大量自定义集成</text> <text x="612" y="96" text-anchor="middle" font-size="10" fill="#f39c12" font-weight="bold">中等</text> <text x="683" y="96" text-anchor="middle" font-size="13" fill="#2ecc71">√</text> <rect x="15" y="124" width="690" height="52" fill="#fafafa" rx="3"></rect><rect x="15" y="124" width="6" height="52" fill="#e67e22" rx="3"></rect><text x="88" y="142" text-anchor="middle" font-size="12" fill="#e67e22" font-weight="bold">LangGraph</text> <text x="88" y="159" text-anchor="middle" font-size="9" fill="#888">LangChain 出品</text> <text x="188" y="147" text-anchor="middle" font-size="10" fill="#444">图状 Agent 框架</text> <text x="188" y="162" text-anchor="middle" font-size="9" fill="#888">有状态工作流</text> <text x="305" y="140" text-anchor="middle" font-size="9.5" fill="#444">用"图"定义复杂工作流</text> <text x="305" y="154" text-anchor="middle" font-size="9.5" fill="#444">内置状态管理、断点续传</text> <text x="305" y="168" text-anchor="middle" font-size="9.5" fill="#444">支持 Human-in-the-Loop</text> <text x="468" y="147" text-anchor="middle" font-size="9.5" fill="#444">需要复杂流程控制的场景</text> <text x="468" y="162" text-anchor="middle" font-size="9.5" fill="#444">生产级 Agent 应用</text> <text x="612" y="150" text-anchor="middle" font-size="10" fill="#e74c3c" font-weight="bold">较难</text> <text x="683" y="150" text-anchor="middle" font-size="13" fill="#2ecc71">√</text> <rect x="15" y="178" width="690" height="52" fill="#fff" rx="3"></rect><rect x="15" y="178" width="6" height="52" fill="#9b59b6" rx="3"></rect><text x="88" y="196" text-anchor="middle" font-size="12" fill="#9b59b6" font-weight="bold">LlamaIndex</text> <text x="88" y="213" text-anchor="middle" font-size="9" fill="#888">Python</text> <text x="188" y="201" text-anchor="middle" font-size="10" fill="#444">RAG 专精框架</text> <text x="188" y="216" text-anchor="middle" font-size="9" fill="#888">数据处理最强</text> <text x="305" y="194" text-anchor="middle" font-size="9.5" fill="#444">数据摄入、索引、检索最优</text> <text x="305" y="208" text-anchor="middle" font-size="9.5" fill="#444">支持 80+ 数据源连接器</text> <text x="305" y="222" text-anchor="middle" font-size="9.5" fill="#444">高级 RAG 策略内置</text> <text x="468" y="201" text-anchor="middle" font-size="9.5" fill="#444">知识库、文档问答场景</text> <text x="468" y="216" text-anchor="middle" font-size="9.5" fill="#444">需要接入大量非结构化数据</text> <text x="612" y="204" text-anchor="middle" font-size="10" fill="#f39c12" font-weight="bold">中等</text> <text x="683" y="204" text-anchor="middle" font-size="13" fill="#2ecc71">√</text> <rect x="15" y="232" width="690" height="52" fill="#fafafa" rx="3"></rect><rect x="15" y="232" width="6" height="52" fill="#3498db" rx="3"></rect><text x="88" y="250" text-anchor="middle" font-size="12" fill="#3498db" font-weight="bold">Dify</text> <text x="88" y="267" text-anchor="middle" font-size="9" fill="#888">开源 LLMOps</text> <text x="188" y="255" text-anchor="middle" font-size="10" fill="#444">可视化低代码</text> <text x="188" y="270" text-anchor="middle" font-size="9" fill="#888">全栈 AI 平台</text> <text x="305" y="248" text-anchor="middle" font-size="9.5" fill="#444">拖拽构建 Workflow，无需写代码</text> <text x="305" y="262" text-anchor="middle" font-size="9.5" fill="#444">内置应用管理、API 发布</text> <text x="305" y="276" text-anchor="middle" font-size="9.5" fill="#444">支持自托管和云端</text> <text x="468" y="255" text-anchor="middle" font-size="9.5" fill="#444">非技术背景用户</text> <text x="468" y="270" text-anchor="middle" font-size="9.5" fill="#444">快速原型到生产部署</text> <text x="612" y="258" text-anchor="middle" font-size="10" fill="#2ecc71" font-weight="bold">最低</text> <text x="683" y="258" text-anchor="middle" font-size="13" fill="#2ecc71">√</text> <rect x="15" y="286" width="690" height="52" fill="#fff" rx="3"></rect><rect x="15" y="286" width="6" height="52" fill="#27ae60" rx="3"></rect><text x="88" y="304" text-anchor="middle" font-size="12" fill="#27ae60" font-weight="bold">n8n</text> <text x="88" y="321" text-anchor="middle" font-size="9" fill="#888">自动化平台</text> <text x="188" y="309" text-anchor="middle" font-size="10" fill="#444">通用工作流自动化</text> <text x="188" y="324" text-anchor="middle" font-size="9" fill="#888">含 AI 节点</text> <text x="305" y="302" text-anchor="middle" font-size="9.5" fill="#444">400+ 服务集成，可视化编排</text> <text x="305" y="316" text-anchor="middle" font-size="9.5" fill="#444">AI 节点 + 传统自动化混合</text> <text x="305" y="330" text-anchor="middle" font-size="9.5" fill="#444">可自托管，数据不出境</text> <text x="468" y="309" text-anchor="middle" font-size="9.5" fill="#444">需要连接各类 SaaS 系统</text> <text x="468" y="324" text-anchor="middle" font-size="9.5" fill="#444">业务流程自动化场景</text> <text x="612" y="312" text-anchor="middle" font-size="10" fill="#2ecc71" font-weight="bold">较低</text> <text x="683" y="312" text-anchor="middle" font-size="13" fill="#2ecc71">√</text> <rect x="15" y="340" width="690" height="52" fill="#fafafa" rx="3"></rect><rect x="15" y="340" width="6" height="52" fill="#2c3e50" rx="3"></rect><text x="88" y="358" text-anchor="middle" font-size="12" fill="#2c3e50" font-weight="bold">CrewAI</text> <text x="88" y="375" text-anchor="middle" font-size="9" fill="#888">Python</text> <text x="188" y="363" text-anchor="middle" font-size="10" fill="#444">多 Agent 协作</text> <text x="188" y="378" text-anchor="middle" font-size="9" fill="#888">角色扮演框架</text> <text x="305" y="356" text-anchor="middle" font-size="9.5" fill="#444">以"角色"和"任务"定义 Agent</text> <text x="305" y="370" text-anchor="middle" font-size="9.5" fill="#444">内置委托、监督机制</text> <text x="305" y="384" text-anchor="middle" font-size="9.5" fill="#444">API 极简，上手快</text> <text x="468" y="363" text-anchor="middle" font-size="9.5" fill="#444">多 Agent 协作场景</text> <text x="468" y="378" text-anchor="middle" font-size="9.5" fill="#444">有 Python 基础的入门者</text> <text x="612" y="366" text-anchor="middle" font-size="10" fill="#2ecc71" font-weight="bold">较低</text> <text x="683" y="366" text-anchor="middle" font-size="13" fill="#2ecc71">√</text> <text x="360" y="408" text-anchor="middle" font-size="10" fill="#888">新手推荐：有代码基础 → LangChain / CrewAI；非技术背景 → Dify / n8n</text></svg>

### 框架选型决策树

根据你的具体情况，按照以下决策树选择合适的框架：

```
你的情况是什么？
│
├─── 没有编程基础，想用可视化工具搭建
│    ├─── 主要是 AI 应用（问答、生成）→ Dify（首选）
│    └─── 需要连接 Slack/邮件等 SaaS 系统 → n8n
│
├─── 有 Python 基础，代码优先
│    ├─── 做知识库 / RAG 系统 → LlamaIndex
│    ├─── 做多 Agent 协作，想快速上手 → CrewAI
│    ├─── 需要复杂有状态流程控制 → LangGraph
│    └─── 通用场景，想要最大生态 → LangChain
│
└─── 已有明确场景，生产级要求
     ├─── 高并发、精细控制 → LangGraph + LangSmith
     └─── 企业部署、私有化 → Dify 自托管
```

---

## 快速上手：Python 代码示例

以下示例从最简单的顺序链到复杂的多 Agent 协作，逐步演示 AI Workflow 的实现方式。

### LangChain 顺序链

最基础的 Workflow 模式，用管道操作符 | 串联多个 LLM 调用步骤。

安装依赖包：

```
pip install langchain langchain-openai
```

## 实例

from langchain\_openai import ChatOpenAI  
from langchain\_core.prompts import ChatPromptTemplate  
from langchain\_core.output\_parsers import StrOutputParser  
  
llm = ChatOpenAI(model="gpt-4o-mini", api\_key="your-api-key")  
  
\# ─── 定义三个步骤 ────────────────────────────────────────────  
\# 步骤 1：将文章翻译成中文  
translate\_prompt = ChatPromptTemplate.from\_template(  
"将下面的英文文章翻译成中文，保持原意：\\n\\n{article}"  
)  
  
\# 步骤 2：提取摘要  
summarize\_prompt = ChatPromptTemplate.from\_template(  
"请将以下文章提炼成 3 个要点，每点一句话：\\n\\n{translated}"  
)  
  
\# 步骤 3：生成标题  
title\_prompt = ChatPromptTemplate.from\_template(  
"根据以下摘要，生成一个吸引人的中文标题（15字以内）：\\n\\n{summary}"  
)  
  
parser = StrOutputParser()  
  
\# ─── 用 | 操作符链接成流水线 ─────────────────────────────────  
chain = (  
{"translated": translate\_prompt | llm | parser}  
| {"summary": summarize\_prompt | llm | parser,  
"translated": lambda x: x\["translated"\]}  
| title\_prompt | llm | parser  
)  
  
\# ─── 运行 ────────────────────────────────────────────────────  
article = """  
Artificial intelligence is transforming how we work and live.  
From automating repetitive tasks to assisting in creative work,  
AI tools are becoming indispensable in modern workflows...  
"""  
  
result = chain.invoke({"article": article})  
print(result)

```
AI 正在重塑现代工作流：从自动化到创意辅助
```

### 工具调用 Agent（ReAct 模式）

ReAct 是 AI Agent 的核心模式，让 AI 在思考和行动之间循环，直到完成任务。

## 实例

from langchain\_openai import ChatOpenAI  
from langchain.agents import AgentExecutor, create\_react\_agent  
from langchain\_core.tools import tool  
from langchain import hub  
import requests, datetime  
  
\# ─── 定义工具 ────────────────────────────────────────────────  
@tool  
def get\_weather(city: str) -> str:  
"""获取指定城市的当前天气信息"""  
\# 实际项目中替换为真实天气 API  
mock\_data = {  
"北京": "晴天，气温 22°C，微风",  
"上海": "多云，气温 26°C，湿度 75%",  
"广州": "小雨，气温 30°C，建议带伞",  
}  
return mock\_data.get(city, f"暂无 {city} 的天气数据")  
  
@tool  
def search\_web(query: str) -> str:  
"""在网络上搜索信息，返回相关内容摘要"""  
\# 实际项目中接入 Tavily / Serper API  
return f"搜索 '{query}' 的结果：这是一个模拟的搜索结果..."  
  
@tool  
def calculate(expression: str) -> str:  
"""计算数学表达式，例如 '2 + 3 \* 4'"""  
try:  
result = eval(expression, {"\_\_builtins\_\_": {}}, {})  
return str(result)  
except Exception as e:  
return f"计算错误：{e}"  
  
@tool  
def get\_date() -> str:  
"""获取今天的日期"""  
return datetime.date.today().strftime("%Y年%m月%d日")  
  
\# ─── 创建 Agent ───────────────────────────────────────────────  
tools = \[get\_weather, search\_web, calculate, get\_date\]  
llm = ChatOpenAI(model="gpt-4o", temperature=0)  
  
\# 使用 LangChain Hub 的标准 ReAct prompt  
prompt = hub.pull("hwchase17/react")  
  
agent = create\_react\_agent(llm, tools, prompt)  
agent\_executor = AgentExecutor(  
agent=agent,  
tools=tools,  
verbose=True, # 打印每步思考过程，方便调试  
max\_iterations=8, # 防止无限循环  
handle\_parsing\_errors=True  
)  
  
\# ─── 运行 ────────────────────────────────────────────────────  
result = agent\_executor.invoke({  
"input": "今天是几号？北京天气怎么样？如果出门步行 5km 消耗约 300 卡路里，"  
"跑步同样距离消耗大约是步行的 1.6 倍，请计算跑步消耗的卡路里。"  
})  
  
print(result\["output"\])  
\# Agent 会自动决策：先调用 get\_date → get\_weather("北京") → calculate("300\*1.6")  
\# 最后综合所有信息给出完整回答

### LangGraph 有状态 Workflow

LangGraph 用图的方式定义复杂流程，每个节点是一个函数，边定义跳转逻辑。

## 实例

from langgraph.graph import StateGraph, END  
from langchain\_openai import ChatOpenAI  
from typing import TypedDict, Annotated  
import operator  
  
\# ─── 定义状态结构（在节点间传递的数据）────────────────────────  
class ResearchState(TypedDict):  
topic: str # 研究主题  
research\_notes: str # 研究笔记  
draft: str # 草稿  
review\_feedback: str # 审阅意见  
final\_report: str # 最终报告  
revision\_count: Annotated\[int, operator.add\] # 修改次数（累加）  
  
llm = ChatOpenAI(model="gpt-4o")  
  
\# ─── 定义节点函数 ─────────────────────────────────────────────  
def research\_node(state: ResearchState) -> dict:  
"""节点1：调研阶段"""  
response = llm.invoke(  
f"请对以下主题进行简要调研，列出 5 个关键要点：{state\['topic'\]}"  
)  
return {"research\_notes": response.content}  
  
def write\_node(state: ResearchState) -> dict:  
"""节点2：撰写草稿"""  
prompt = f"""  
主题：{state\['topic'\]}  
调研笔记：{state\['research\_notes'\]}  
{'上次审阅意见：' + state.get('review\_feedback', '') if state.get('review\_feedback') else ''}  
  
请根据以上内容撰写一篇 300 字的分析报告草稿。  
"""  
response = llm.invoke(prompt)  
return {"draft": response.content, "revision\_count": 1}  
  
def review\_node(state: ResearchState) -> dict:  
"""节点3：审阅草稿"""  
response = llm.invoke(  
f"审阅以下报告，如果质量达标回复 'APPROVED'，否则给出具体修改意见：\\n\\n{state\['draft'\]}"  
)  
return {"review\_feedback": response.content}  
  
def finalize\_node(state: ResearchState) -> dict:  
"""节点4：最终定稿"""  
return {"final\_report": state\["draft"\]}  
  
\# ─── 路由函数：决定审阅后走哪条路 ─────────────────────────────  
def should\_revise(state: ResearchState) -> str:  
if "APPROVED" in state\["review\_feedback"\]:  
return "finalize" # → 最终定稿  
elif state\["revision\_count"\] >= 3:  
return "finalize" # → 超过3次修改，强制结束  
else:  
return "revise" # → 返回写作节点修改  
  
\# ─── 构建工作流图 ─────────────────────────────────────────────  
workflow = StateGraph(ResearchState)  
  
\# 添加节点  
workflow.add\_node("research", research\_node)  
workflow.add\_node("write", write\_node)  
workflow.add\_node("review", review\_node)  
workflow.add\_node("finalize", finalize\_node)  
  
\# 设置入口  
workflow.set\_entry\_point("research")  
  
\# 添加边（定义流转逻辑）  
workflow.add\_edge("research", "write") # 调研 → 写作  
workflow.add\_edge("write", "review") # 写作 → 审阅  
  
\# 条件边：审阅后根据结果选择路径  
workflow.add\_conditional\_edges(  
"review",  
should\_revise,  
{  
"revise": "write", # 需要修改 → 回到写作  
"finalize": "finalize" # 通过审核 → 最终定稿  
}  
)  
  
workflow.add\_edge("finalize", END)  
  
\# 编译并运行  
app = workflow.compile()  
  
result = app.invoke({"topic": "生成式 AI 对软件开发行业的影响", "revision\_count": 0})  
print(result\["final\_report"\])

### CrewAI 多 Agent 协作

CrewAI 通过定义角色和任务，让多个 Agent 像团队一样协作。

## 实例

from crewai import Agent, Task, Crew, Process  
from langchain\_openai import ChatOpenAI  
  
llm = ChatOpenAI(model="gpt-4o")  
  
\# ─── 定义 Agent（角色） ────────────────────────────────────────  
researcher = Agent(  
role="市场研究员",  
goal="收集并整理关于目标主题的全面、准确的市场信息",  
backstory="你是一位经验丰富的市场分析师，擅长从海量信息中提炼关键洞察",  
llm=llm,  
verbose=True  
)  
  
analyst = Agent(  
role="数据分析师",  
goal="基于研究员提供的信息，进行深度分析并得出有价值的结论",  
backstory="你擅长用数据说话，能发现隐藏在信息背后的趋势和机会",  
llm=llm,  
verbose=True  
)  
  
writer = Agent(  
role="报告撰写专家",  
goal="将分析结论撰写成清晰、专业、有说服力的报告",  
backstory="你有丰富的商业写作经验，能让复杂的分析变得易于理解",  
llm=llm,  
verbose=True  
)  
  
\# ─── 定义 Task（任务） ────────────────────────────────────────  
research\_task = Task(  
description="调研中国新能源汽车市场的现状，包括主要品牌、市场份额、增长趋势",  
expected\_output="一份包含 5 个关键数据点的市场调研报告，含数字和具体事实",  
agent=researcher  
)  
  
analysis\_task = Task(  
description="基于调研报告，分析未来 3 年的机会与风险，给出投资评级建议",  
expected\_output="SWOT 分析表格 + 投资评级（强烈推荐/推荐/中性/谨慎）+ 理由",  
agent=analyst,  
context=\[research\_task\] # 依赖调研任务的输出  
)  
  
writing\_task = Task(  
description="将调研和分析整合成一份 500 字的专业投资简报，格式清晰",  
expected\_output="包含执行摘要、市场现状、机会风险、投资建议四个部分的简报",  
agent=writer,  
context=\[research\_task, analysis\_task\]  
)  
  
\# ─── 组建团队并执行 ───────────────────────────────────────────  
crew = Crew(  
agents=\[researcher, analyst, writer\],  
tasks=\[research\_task, analysis\_task, writing\_task\],  
process=Process.sequential, # 顺序执行（也可改为 hierarchical）  
verbose=True  
)  
  
result = crew.kickoff()  
print(result)

### Human-in-the-Loop（人工审核节点）

LangGraph 支持在关键步骤暂停，等待人工确认后再继续执行。

## 实例

from langgraph.graph import StateGraph, END  
from langgraph.checkpoint.memory import MemorySaver  
from typing import TypedDict  
  
class EmailState(TypedDict):  
recipient: str  
content: str  
approved: bool  
  
def draft\_email(state: EmailState) -> dict:  
"""起草邮件"""  
content = f"尊敬的 {state\['recipient'\]}，\\n\\n这是 AI 起草的邮件内容...\\n\\n此致"  
return {"content": content}  
  
def send\_email(state: EmailState) -> dict:  
"""发送邮件（高风险操作，需要人工审核后才执行）"""  
print(f"邮件已发送给 {state\['recipient'\]}")  
return {}  
  
\# 路由：根据人工审核结果决定是否发送  
def check\_approval(state: EmailState) -> str:  
return "send" if state.get("approved") else END  
  
workflow = StateGraph(EmailState)  
workflow.add\_node("draft", draft\_email)  
workflow.add\_node("send", send\_email)  
workflow.set\_entry\_point("draft")  
  
\# draft 完成后暂停，等待人工审核（interrupt\_after）  
workflow.add\_conditional\_edges("draft", check\_approval, {"send": "send", END: END})  
workflow.add\_edge("send", END)  
  
\# 使用 MemorySaver 支持中断和恢复  
memory = MemorySaver()  
app = workflow.compile(  
checkpointer=memory,  
interrupt\_after=\["draft"\] # 在 draft 节点后暂停  
)  
  
config = {"configurable": {"thread\_id": "email-001"}}  
  
\# 第一次运行：执行到 draft 后暂停  
state = app.invoke({"recipient": "客户A", "approved": False}, config)  
print("草稿已生成，等待审核：")  
print(state\["content"\])  
  
\# 人工审核后，更新状态并继续执行  
user\_input = input("\\n是否批准发送？(y/n): ")  
if user\_input.lower() == "y":  
app.update\_state(config, {"approved": True})  
app.invoke(None, config) # 从断点继续  
print("邮件已发送")  
else:  
print("已取消发送")

### Prompt 工程：Workflow 中的关键技巧

在 AI Workflow 中，Prompt 的质量直接影响每个节点的输出质量。

## 实例

\# 模糊的角色定义  
\# system\_prompt = "你是一个 AI 助手，帮我分析这份文档"  
  
\# 清晰的角色定义（推荐）  
system\_prompt = """  
你是一位专业的财务分析师，专注于识别财务报告中的风险信号。  
你的任务：从以下报告中提取所有涉及负债、现金流和盈利能力的关键数据点。  
输出格式：JSON，包含 risk\_level（high/medium/low）和 key\_findings（列表）。  
注意：只输出 JSON，不要添加任何说明文字。  
"""

## 实例

\# 传递非结构化文本  
\# state\["previous\_output"\] = "分析结果：这个公司看起来不错，有一些风险..."  
  
\# 传递结构化数据（推荐）  
state\["analysis\_result"\] = {  
"risk\_level": "medium",  
"key\_findings": \["负债率 45%，行业均值 38%", "现金流为正，Q3 环比下降 12%"\],  
"recommendation": "谨慎持有"  
}

## 实例

\# 在 prompt 中强制要求 JSON 输出  
prompt = """  
请分析以下文本的情感倾向。  
严格按照如下 JSON 格式输出，不要添加任何其他内容：  
{  
"sentiment": "positive" | "negative" | "neutral",  
"confidence": 0.0-1.0,  
"reason": "简短说明"  
}  
  
文本：{text}  
"""

### 错误处理与重试

## 实例

from tenacity import retry, stop\_after\_attempt, wait\_exponential  
import logging  
  
@retry(  
stop=stop\_after\_attempt(3), # 最多重试 3 次  
wait=wait\_exponential(multiplier=1, min=2, max=10) # 指数退避等待  
)  
def call\_llm\_with\_retry(prompt: str) -> str:  
try:  
response = llm.invoke(prompt)  
return response.content  
except Exception as e:  
logging.error(f"LLM 调用失败：{e}")  
raise  
  
def safe\_parse\_json(text: str) -> dict:  
"""安全解析 LLM 输出的 JSON"""  
import json, re  
\# 提取 JSON 部分（LLM 有时会加多余的说明文字）  
json\_match = re.search(r'\\{.\*\\}', text, re.DOTALL)  
if json\_match:  
try:  
return json.loads(json\_match.group())  
except json.JSONDecodeError:  
pass  
return {"error": "解析失败", "raw": text}

### 成本控制

## 实例

\# ─── 根据任务重要性选择模型 ────────────────────────────────  
def get\_llm(task\_type: str):  
if task\_type == "classification": # 分类任务，轻量模型足够  
return ChatOpenAI(model="gpt-4o-mini")  
elif task\_type == "generation": # 生成任务，用中等模型  
return ChatOpenAI(model="gpt-4o-mini")  
elif task\_type == "reasoning": # 复杂推理，用强模型  
return ChatOpenAI(model="gpt-4o")  
  
\# ─── 缓存重复请求 ──────────────────────────────────────────  
from langchain.globals import set\_llm\_cache  
from langchain\_community.cache import InMemoryCache  
set\_llm\_cache(InMemoryCache()) # 相同输入直接返回缓存，不重复计费  
  
\# ─── 文本分块避免超长 ──────────────────────────────────────  
from langchain.text\_splitter import RecursiveCharacterTextSplitter  
  
splitter = RecursiveCharacterTextSplitter(  
chunk\_size=2000, # 每块 2000 字符  
chunk\_overlap=200 # 重叠 200 字符保证上下文连贯  
)  
chunks = splitter.split\_text(long\_document)

---

## 典型应用场景

AI Workflow 已经在多个领域广泛落地，以下是六个最具代表性的场景。

<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="360" fill="#f8f9fa" rx="12"></rect><text x="360" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">AI Workflow 典型应用场景</text> <rect x="18" y="45" width="215" height="135" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="18" y="45" width="215" height="5" rx="10" fill="#e74c3c"></rect><text x="125" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#c0392b">AI 编程助手</text> <text x="35" y="88" font-size="9.5" fill="#555">用户描述需求 → 理解需求 →</text> <text x="35" y="102" font-size="9.5" fill="#555">生成代码 → 自动运行 →</text> <text x="35" y="116" font-size="9.5" fill="#555">发现报错 → 自动修复 →</text> <text x="35" y="130" font-size="9.5" fill="#555">生成文档和测试用例</text> <text x="35" y="150" font-size="9" fill="#e74c3c">代表：GitHub Copilot Workspace</text> <text x="35" y="164" font-size="9" fill="#e74c3c">Claude Code、Cursor</text> <rect x="248" y="45" width="215" height="135" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="248" y="45" width="215" height="5" rx="10" fill="#f39c12"></rect><text x="355" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#e67e22">自动化研究报告</text> <text x="265" y="88" font-size="9.5" fill="#555">接收研究主题 → 分解子问题</text> <text x="265" y="102" font-size="9.5" fill="#555">→ 并行搜集资料 → 提取</text> <text x="265" y="116" font-size="9.5" fill="#555">关键信息 → 综合分析 →</text> <text x="265" y="130" font-size="9.5" fill="#555">生成带引用的完整报告</text> <text x="265" y="150" font-size="9" fill="#e67e22">代表：Perplexity Deep Research</text> <text x="265" y="164" font-size="9" fill="#e67e22">OpenAI Deep Research</text> <rect x="478" y="45" width="225" height="135" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="478" y="45" width="225" height="5" rx="10" fill="#2ecc71"></rect><text x="590" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#27ae60">智能客服系统</text> <text x="495" y="88" font-size="9.5" fill="#555">识别用户意图 → 查询订单</text> <text x="495" y="102" font-size="9.5" fill="#555">数据库 → 检索政策文档</text> <text x="495" y="116" font-size="9.5" fill="#555">→ 生成个性化回复 →</text> <text x="495" y="130" font-size="9.5" fill="#555">复杂问题转人工处理</text> <text x="495" y="150" font-size="9" fill="#27ae60">代表：各大电商平台 AI 客服</text> <text x="495" y="164" font-size="9" fill="#27ae60">银行智能客服</text> <rect x="18" y="195" width="215" height="145" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="18" y="195" width="215" height="5" rx="10" fill="#3498db"></rect><text x="125" y="218" text-anchor="middle" font-size="12" font-weight="bold" fill="#2980b9">数据分析自动化</text> <text x="35" y="238" font-size="9.5" fill="#555">上传 Excel/CSV → 理解</text> <text x="35" y="252" font-size="9.5" fill="#555">数据结构 → 自动选择</text> <text x="35" y="266" font-size="9.5" fill="#555">分析方法 → 执行 Python</text> <text x="35" y="280" font-size="9.5" fill="#555">→ 生成图表+自然语言解读</text> <text x="35" y="302" font-size="9" fill="#3498db">代表：ChatGPT Advanced</text> <text x="35" y="316" font-size="9" fill="#3498db">Data Analysis</text> <rect x="248" y="195" width="215" height="145" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="248" y="195" width="215" height="5" rx="10" fill="#9b59b6"></rect><text x="355" y="218" text-anchor="middle" font-size="12" font-weight="bold" fill="#8e44ad">内容营销流水线</text> <text x="265" y="238" font-size="9.5" fill="#555">输入主题和受众 → 调研</text> <text x="265" y="252" font-size="9.5" fill="#555">热点 → 生成大纲 → 撰写</text> <text x="265" y="266" font-size="9.5" fill="#555">全文 → 优化 SEO → 生成</text> <text x="265" y="280" font-size="9.5" fill="#555">配图描述 → 多平台适配</text> <text x="265" y="302" font-size="9" fill="#9b59b6">代表：各类 AI 写作</text> <text x="265" y="316" font-size="9" fill="#9b59b6">和营销自动化工具</text> <rect x="478" y="195" width="225" height="145" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="1.2"></rect><rect x="478" y="195" width="225" height="5" rx="10" fill="#e67e22"></rect><text x="590" y="218" text-anchor="middle" font-size="12" font-weight="bold" fill="#d35400">医疗辅助诊断</text> <text x="495" y="238" font-size="9.5" fill="#555">患者描述症状 → 结构化</text> <text x="495" y="252" font-size="9.5" fill="#555">病史 → 检索医学文献 →</text> <text x="495" y="266" font-size="9.5" fill="#555">分析影像报告 → 生成</text> <text x="495" y="280" font-size="9.5" fill="#555">参考建议 → 医生确认</text> <text x="495" y="302" font-size="9" fill="#e67e22">注：高风险场景必须保留</text> <text x="495" y="316" font-size="9" fill="#e67e22">Human-in-the-Loop</text></svg>

---

## 最佳实践与常见陷阱

### 常见陷阱与解决方案

以下是初学者在使用 AI Workflow 时最容易遇到的问题。

| 陷阱 | 现象 | 解决方案 |
| --- | --- | --- |
| 幻觉级联 | 前一步 AI 输出错误，被当成事实传给下一步，错误被放大 | 关键节点增加验证步骤；数值类信息用工具获取 |
| 无限循环 | ReAct Agent 反复调用工具，不知道何时停止 | 设置 max\_iterations；给 LLM 明确的终止条件 |
| 上下文爆炸 | 随着步骤增加，传入 LLM 的文本越来越长，超出窗口 | 每步只传必要字段；用摘要压缩历史信息 |
| 工具滥用 | Agent 明明可以直接回答，却反复调用工具 | 优化工具描述；给 LLM 明确说明何时不需要工具 |
| JSON 解析失败 | LLM 输出格式不稳定，程序崩溃 | 加 safe\_parse\_json；用 LangChain OutputParser |
| 费用超支 | 未估算 token 用量，月底账单超预期 | 先用 gpt-4o-mini 测试；用 LangSmith 监控用量 |
| 并发冲突 | 多个 Agent 同时写同一个状态导致数据错乱 | 用 LangGraph 内置状态管理；避免共享可变状态 |

---

## 总结与学习路径

### 核心知识点回顾

<svg viewBox="0 0 720 210" xmlns="http://www.w3.org/2000/svg" font-family="'Segoe UI', Arial, sans-serif" style="max-width:100%;height:auto;"><rect width="720" height="210" fill="#1a1a2e" rx="12"></rect><text x="360" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#fff">AI Workflow 核心知识点</text> <rect x="15" y="48" width="108" height="145" rx="9" fill="#e74c3c" opacity="0.85"></rect><text x="69" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">核心要素</text> <text x="69" y="90" text-anchor="middle" font-size="9" fill="#fcc">LLM、工具</text> <text x="69" y="104" text-anchor="middle" font-size="9" fill="#fcc">记忆、状态</text> <text x="69" y="118" text-anchor="middle" font-size="9" fill="#fcc">路由、人工</text> <text x="69" y="132" text-anchor="middle" font-size="9" fill="#fcc">介入六大件</text> <text x="69" y="152" text-anchor="middle" font-size="8" fill="#f99">构成完整系统</text> <rect x="133" y="48" width="108" height="145" rx="9" fill="#f39c12" opacity="0.85"></rect><text x="187" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">六大模式</text> <text x="187" y="90" text-anchor="middle" font-size="9" fill="#fde">顺序链</text> <text x="187" y="104" text-anchor="middle" font-size="9" fill="#fde">条件路由</text> <text x="187" y="118" text-anchor="middle" font-size="9" fill="#fde">并行执行</text> <text x="187" y="132" text-anchor="middle" font-size="9" fill="#fde">ReAct 循环</text> <text x="187" y="146" text-anchor="middle" font-size="9" fill="#fde">Plan&amp;Execute</text> <text x="187" y="160" text-anchor="middle" font-size="9" fill="#fde">多 Agent</text> <rect x="251" y="48" width="108" height="145" rx="9" fill="#2ecc71" opacity="0.85"></rect><text x="305" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">主流框架</text> <text x="305" y="90" text-anchor="middle" font-size="9" fill="#d5f5e3">LangChain</text> <text x="305" y="104" text-anchor="middle" font-size="9" fill="#d5f5e3">LangGraph</text> <text x="305" y="118" text-anchor="middle" font-size="9" fill="#d5f5e3">LlamaIndex</text> <text x="305" y="132" text-anchor="middle" font-size="9" fill="#d5f5e3">CrewAI</text> <text x="305" y="146" text-anchor="middle" font-size="9" fill="#d5f5e3">Dify / n8n</text> <text x="305" y="160" text-anchor="middle" font-size="9" fill="#d5f5e3">按需选型</text> <rect x="369" y="48" width="108" height="145" rx="9" fill="#3498db" opacity="0.85"></rect><text x="423" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">关键代码</text> <text x="423" y="90" text-anchor="middle" font-size="9" fill="#d6eaf8">Chain 链式调用</text> <text x="423" y="104" text-anchor="middle" font-size="9" fill="#d6eaf8">tool 工具定义</text> <text x="423" y="118" text-anchor="middle" font-size="9" fill="#d6eaf8">StateGraph 状态图</text> <text x="423" y="132" text-anchor="middle" font-size="9" fill="#d6eaf8">Agent + Executor</text> <text x="423" y="146" text-anchor="middle" font-size="9" fill="#d6eaf8">Human-in-Loop</text> <text x="423" y="160" text-anchor="middle" font-size="9" fill="#d6eaf8">interrupt_after</text> <rect x="487" y="48" width="108" height="145" rx="9" fill="#9b59b6" opacity="0.85"></rect><text x="541" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">关键陷阱</text> <text x="541" y="90" text-anchor="middle" font-size="9" fill="#e8daef">幻觉级联</text> <text x="541" y="104" text-anchor="middle" font-size="9" fill="#e8daef">无限循环</text> <text x="541" y="118" text-anchor="middle" font-size="9" fill="#e8daef">上下文爆炸</text> <text x="541" y="132" text-anchor="middle" font-size="9" fill="#e8daef">JSON 解析失败</text> <text x="541" y="146" text-anchor="middle" font-size="9" fill="#e8daef">费用超支</text> <text x="541" y="160" text-anchor="middle" font-size="9" fill="#e8daef">预防优于治疗</text> <rect x="605" y="48" width="100" height="145" rx="9" fill="#27ae60" opacity="0.85"></rect><text x="655" y="70" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">应用场景</text> <text x="655" y="90" text-anchor="middle" font-size="9" fill="#d5f5e3">AI 编程助手</text> <text x="655" y="104" text-anchor="middle" font-size="9" fill="#d5f5e3">研究报告</text> <text x="655" y="118" text-anchor="middle" font-size="9" fill="#d5f5e3">智能客服</text> <text x="655" y="132" text-anchor="middle" font-size="9" fill="#d5f5e3">数据分析</text> <text x="655" y="146" text-anchor="middle" font-size="9" fill="#d5f5e3">内容生产</text> <text x="655" y="160" text-anchor="middle" font-size="9" fill="#d5f5e3">医疗辅助</text></svg>

### 推荐学习路径

第一阶段：理解基础（1 周）

1. 理解 LLM API 调用，能用 OpenAI SDK 发起请求
2. 跑通本文 LangChain 顺序链示例
3. 理解 Prompt Engineering 基本原则

第二阶段：工具与 Agent（2 周）

1. 学会用 @tool 装饰器定义工具
2. 跑通 ReAct Agent 示例，观察 verbose 日志理解循环逻辑
3. 用 Dify 或 n8n 搭建一个可视化 Workflow 原型

第三阶段：复杂 Workflow（3 周）

1. 学习 LangGraph 状态图，实现带条件分支的工作流
2. 用 CrewAI 实现一个双 Agent 协作任务
3. 接入真实工具（Tavily 搜索、Python REPL）
4. 用 LangSmith 观测并调试你的 Workflow

第四阶段：生产就绪（持续）

1. 实现错误重试、结构化输出解析
2. 成本监控与优化（模型分级使用）
3. 部署到生产，设置监控告警

---