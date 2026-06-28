---
title: "Spec-Driven Development 完全指南 — Augment Code"
tags:
  - source
  - spec-driven
  - methodology
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://www.augmentcode.com/guides/what-is-spec-driven-development"
source_author: "Molisha Shah (Augment Code)"
source_date: 2026-04-23
aliases:
  - SDD Complete Guide
  - Augment Code SDD Guide
---

# Spec-Driven Development 完全指南 — Augment Code

> Augment Code 发布的 Spec-Driven Development（SDD）深度指南。Molisha Shah 以实践者视角，系统阐述了 SDD 的定义、六大要素框架、三种落地模式、对抗性 Agent 模式、模型分层策略、棕地采纳路径和工具生态。对现有 [[wiki/concepts/spec-driven-development]] 概念页形成重要的实践层补充。

## 核心论点

1. **SDD 的本质转变**：规格从被动文档变为可执行契约（executable contracts），AI Agent 从中推导代码，CI 管线自动验证。传统规格是人类阅读的，SDD 规格是作为验证门（validation gates）执行的。

2. **Why Now（2025-2026 三大合力）**：
   - AI 生成代码的漏洞率 9.8%-42.1%（Yan et al., 2025），到 2026 年 2 月已有超过 11 万 AI 引入的问题存活在生产仓库中
   - EU AI Act 对高风险 AI 系统的合规要求从 2026 年 8 月 2 日起生效，最高罚款 €15M 或全球年营收的 3%
   - 分布式架构需要正式治理，Deloitte 报告仅 1/5 企业具备成熟的自主 AI Agent 治理模型

3. **六要素框架**：一个好的 Spec 必须回答六个问题——成果（Outcomes）、范围边界（Scope）、约束与假设（Constraints）、已做决策（Prior Decisions）、任务分解（Task Breakdown）、验证标准（Verification Criteria）。遗漏任何一项，Agent 都会用自己的假设填补。

4. **三种模式**：Spec-First（规格引导，AI 代码为主交付物）、Spec-Anchored（规格治理，含宪法约束和监督检查点，面向合规场景）、Spec-as-Source（规格即源码，ThoughtWorks 技术雷达列为 "Assess" 阶段）。

5. **对抗性 Agent 模式（Adversarial Agent Pattern）**：Coordinator 拆解规格 → Implementor 子 Agent 执行 → Verifier Agent 独立检查。Implementor 与 Verifier 目标对立：一个优化完成任务，另一个优化发现失败。这是 SDD 中最被低估的模式。

6. **模型分层**：写 Spec 用最贵模型（错误会向下游传播），Implement 用中档模型（Sonnet-class），Verify 用快速模型（准确性和低成本）。

7. **棕地采纳三阶段**：Phase 1 重构现有行为（AI 辅助逆向工程）→ Phase 2 只对变更区域写 Spec → Phase 3 增量式在 CI 中强制执行。

8. **何时跳过 Spec**：探索性工作、快速原型、小团队高变更环境、遗留系统需大量文档——Spec 的开销是真实成本。

## 核心贡献

- **六要素框架** — 这是对 SDD 概念层最重要的实践补充，此前现有概念页缺少产出物级别的可操作框架
- **SDD vs TDD/BDD/Vibe Coding 对比表** — 五个维度（Primary artifact / Scope / Validation mechanism / AI governance / Where truth lives）系统区分
- **工具对比矩阵** — 7 款工具（Spec Kit / SwaggerHub / Postman Spec Hub / Spectral / PactFlow / Specmatic / TypeSpec）在 Spec 格式 / CI/CD 执行 / AI Agent 兼容 / 适用场景四维度对比
- **Figma MCP + 对抗性 Agent 的完整实践案例** — 10 页产品网站，Coordinator 从 Figma MCP 拉取设计系统 → 按页分解 → 并行 Agent 在隔离 Worktree 执行 → Verifier 检查 → 设计师直接迭代
- **Intent Context Engine** — 企业级多仓库 SDD 的扩展方案（处理 400,000+ 文件的语义依赖图分析，SOC 2 Type II + ISO/IEC 42001 认证）

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — 需大幅扩展：添加六要素框架、三种模式、对抗性 Agent 模式、模型分层、棕地采纳、工具对比、实践案例
- [[wiki/concepts/vibe-coding]] — 可能的补充引用（SDD vs Vibe Coding 对比）
- [[wiki/concepts/harness-engineering]] — 对抗性 Agent 模式（Verifier Agent）与 Harness Engineering 的监督层相关
- [[wiki/entities/claude-code]] — 提及作为执行层工具
