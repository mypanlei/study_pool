---
title: "AI 应用系统设计：从 Prompt Demo 到生产级架构 — JavaGuide"
tags:
  - source
  - ai-system-design
  - javaguide
  - architecture
created: 2026-06-21
updated: 2026-06-21
source: "https://javaguide.cn/ai/system-design/ai-application-architecture.html"
author: "Guide (JavaGuide)"
---

# AI 应用系统设计：从 Prompt Demo 到生产级架构 — JavaGuide

> 深入拆解生产级 AI 应用系统设计，覆盖 Prompt 管理、模型网关、RAG、Memory、Tool、异步任务、可观测、评测、安全合规与 Java 后端落地方案。核心论点是：Prompt Demo 只证明"能回答"，生产级架构要证明"长期可控地回答"。

## Core Contributions

1. **Demo vs 生产六大维度差距**：稳定性（单模型→多模型路由/重试/Fallback）、权限（默认全查→检索前过滤）、成本（单次成功→Token 预算/模型分层/缓存归因）、可观测（记录问答→记录全链路）、评测（人工试→固定评测集/LLM-as-Judge/人工复核）、数据治理（原始入库→PII 脱敏/版本化/审计）。

2. **标准分层架构**：入口层（认证鉴权/请求标准化/限流/幂等/PII 脱敏）→ 业务编排层（选交互模式/组合上下文/决定工具权限）→ Prompt 与 Context 管理层（模板版本/变量注入/灰度/回滚）→ RAG、Memory、Tool 三类上下文的分离治理 → 模型网关 → 工具运行时 → 评测与观测。

3. **三类交互模式选型**：同步（短问答/分类/低延迟小任务）、流式（聊天/长答案/代码生成）、异步（报告生成/批量评测/长文档分析）。经验阈值：3 秒内稳定完成→同步；用户需要立刻看到输出→流式；长文档/多轮工具→异步。

4. **Prompt 版本化管理**：5 表建模（prompt_template/prompt_version/prompt_release/prompt_run/prompt_eval_result），支持变量注入/Schema 校验/灰度/回滚。强调 Prompt 变更要像代码变更一样可追踪，但发布频率可以比代码更高。

5. **RAG/Memory/Tool 三类上下文分离**：RAG=共享知识源（企业文档/制度），Memory=个性化背景（用户偏好/历史决策），Tool=真实业务系统（查询/创建/发送）。三者底层可能共用向量检索，但治理策略完全不同。高频盲区：不要把 Memory 当成个人版 RAG 随便塞。

6. **工具调用 6 道安全关**：工具注册→工具检索→参数校验→权限校验→二次确认→审计日志。核心心智模型：模型只能提出"想调用什么工具"，真正执行前必须经过系统校验。

7. **可观测与评测闭环**：Trace 至少记录 Prompt 版本、检索命中、工具调用、模型输出、Token、TTFT、延迟、成本。评测拆成链路指标（Context Recall/Precision/Faithfulness/Answer Relevancy/Tool Success Rate），形成"线上失败样本→进入数据集→回放→定位→灰度→对比→再发布"的闭环。

8. **Java 后端 11 模块拆分**：ai-api/ai-orchestrator/ai-prompt/ai-context/ai-gateway/ai-rag/ai-memory/ai-tool/ai-eval/ai-observability，含 10 张核心表设计和关键接口定义。

## Key Insights

- "Prompt Demo 只证明'能回答'，生产级架构要证明'长期可控地回答'"
- "RAG、Memory、Tool 要分开治理，共享知识、个性化记忆和真实业务动作不能混成一团"
- "模型只能提出'想调用什么工具'，真正执行前必须经过系统校验"
- "安全策略要靠代码强制执行，Prompt 只能辅助，不能替代权限、脱敏、审计和二次确认"
- "没有 Trace 和回放，优化基本靠猜"

## Related Pages

- [[wiki/concepts/prompt-engineering]] — Prompt Engineering 相关
- [[wiki/concepts/mcp-model-context-protocol]] — MCP 协议，工具接入标准化
- [[wiki/concepts/harness-engineering]] — Harness Engineering 六层架构
- [[wiki/concepts/rag-optimization]] — RAG 优化
- [[wiki/concepts/guardrails]] — Agent 安全护栏
- [[wiki/sources/structured-output-function-calling-javaguide]] — 同系列文章
- [[wiki/sources/llm-gateway-deep-dive-javaguide]] — LLM Gateway 详解
