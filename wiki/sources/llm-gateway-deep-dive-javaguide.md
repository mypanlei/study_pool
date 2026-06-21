---
title: "大模型网关详解：多模型路由、Fallback、限流与成本控制 — JavaGuide"
tags:
  - source
  - llm-gateway
  - javaguide
  - system-design
created: 2026-06-21
updated: 2026-06-21
source: "https://javaguide.cn/ai/system-design/llm-gateway.html"
author: "Guide (JavaGuide)"
---

# 大模型网关详解：多模型路由、Fallback、限流与成本控制 — JavaGuide

> 介绍 LLM Gateway 的边界与核心能力：模型路由、Fallback、限流配额、Token 预算、成本统计、观测审计、缓存策略、Java 后端落地方案和主流方案选型。核心论点：先解决工程治理，再追求智能路由。

## Core Contributions

1. **LLM Gateway 定义与定位**：API 网关能力+模型调用控制面。不替代既有 API 网关，但把模型路由、预算、审计和适配逻辑收口。与 LLM Router 的区别：Router 管模型选择，Gateway 管整次模型调用全生命周期。

2. **LLM Gateway vs RAG/Agent/MCP**：Gateway 靠近"模型调用治理"，RAG/Agent/MCP 靠近"应用能力组织"。一个复杂 Agent 可以在多个步骤里调用 Gateway，Gateway 对每个步骤分别记录 scene/route_reason/Token/成本。

3. **多模型路由完整策略体系**：固定规则路由（起步首选）→ 成本优先/级联路由（先小模型后升级）→ 语义/分类路由（embedding 相似度）→ 学习型路由（数据驱动）→ 个性化路由（用户偏好）→ Agentic 路由（多步动态切模型）。演进路线：先让系统可控→再让系统省钱→最后让系统变聪明。

4. **Fallback 机制**：区分错误类型（网络瞬断/5xx/429/上下文超限/参数错误/安全拒答/结构化解析失败），不同错误不同处理。幂等键+LLMResponse 缓存是 LLM 高消费场景的兜底护栏。

5. **Token 预算是 LLM 特有的限流维度**：预估（estimate）→ 预留（reserve）→ 真实用量（usage）→ 对账（reconcile）四步走。用户/租户/模型/供应商/Token 五维限流。

6. **成本归因字段模型**：request_id/attempt_id/tenant_id/user_id/scene/prompt_version/provider/model_tier/model/input_tokens/output_tokens/cached_tokens/cost/price_version/latency_ms/ttft_ms/fallback_used/error_code。

7. **观测与审计**：Trace 至少包含 tenant_id/user_id/scene/prompt_version/model_tier/route_reason/input_tokens/output_tokens/cost/ttft_ms/latency_ms/fallback_used。审计边界：不要无脑长期保存完整 Prompt 和回答，元数据长期保留，Prompt 采样存储，PII 入口脱敏。

8. **缓存策略全景**：精确缓存→OpenAI/Anthropic/Gemini 供应商缓存→语义缓存（谨慎）→结果片段缓存。Prompt cache 稳定内容放前面、动态内容放后面是关键原则。

9. **主流方案选型**：自研轻量网关（可控贴合业务）、LiteLLM（多供应商灵活接入，注意供应链安全）、Cloudflare AI Gateway（托管边缘入口，适合已在 Cloudflare 的团队）、Kong AI Gateway（企业 API 治理集成）、Inworld Router（实时路由和实验能力）、LLMRouter（研究与算法工具箱）。

10. **Java 后端完整实现**：LLMRequest/LLMResponse/ProviderClient/LLMGateway 接口定义，RouteConfig（YAML 配置的基于 scene 的路由）、RuleBasedModelRouter、TokenBudget/LLMRateLimiter（四步预算扣减）、成本追踪和 Trace 设计。

## Key Insights

- "LLM Gateway 解决的不是钱，而是后续换模型、控延迟、查问题时的混乱"
- "不要把所有请求都走最强模型：意图分类、标题生成、JSON 修复也走旗舰模型，单次看不贵，流量上来后很吓人"
- "没有 trace，不上分类器；没有评测集，不上学习型 Router；没有成本上限，不上 Agentic 路由"
- "先解决工程治理，再追求智能路由"
- "路由规则不能写完就不管。它要像 Prompt 一样有版本，像代码一样做回归测试"

## Related Pages

- [[wiki/concepts/harness-engineering]] — Harness Engineering
- [[wiki/concepts/mcp-model-context-protocol]] — MCP 协议
- [[wiki/concepts/guardrails]] — Agent 安全护栏
- [[wiki/sources/ai-system-design-javaguide]] — AI 应用系统设计
- [[wiki/sources/structured-output-function-calling-javaguide]] — 结构化输出与 Function Calling
- [[wiki/sources/llm-operation-mechanism-javaguide]] — LLM 运行机制
