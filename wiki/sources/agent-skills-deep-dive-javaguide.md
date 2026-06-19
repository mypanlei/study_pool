---
title: "Agent Skills 深度解析 — JavaGuide"
tags:
  - source
  - skills
  - javaguide
  - mcp
  - prompt
  - skill-md
  - routing
created: 2026-06-19
updated: 2026-06-19
source_url: "https://javaguide.cn/ai/agent/skills.html"
source_author: "JavaGuide (Guide)"
source_date: 2026-05-26
---

# Agent Skills 深度解析

> JavaGuide 出品的 Agent Skills 深度文章（~9000 字），系统阐述 Skill 与 Prompt/Function Calling/MCP 的边界与配合，SKILL.md 元数据和正文设计，延迟加载与渐进式披露三层模型，自由度的把控，工作流设计和路由策略，以及写 Skill 最容易踩的 8 个坑。

## 核心论点

1. **Skill 不是 Prompt/MCP/Function Calling 的替代品** — 它们分属不同层级：Prompt（用户意图）、Function Calling（工具调用格式）、MCP（连接协议）、Skills（任务经验封装）
2. **Skill = 上下文注入机制** — Agent 读一份文档，然后把里面的规则纳入后续推理，不像 Function Calling 那样是一段代码
3. **渐进式披露三层模型** — 广告层（元数据）→ 指令层（SKILL.md 正文）→ 资源层（scripts/references），只在需要时加载更深层
4. **Skill 路由在数量增多后变成检索问题** — 粗召回（向量相似度）→ 精排（多维度打分）→ 兜底（不选比选错安全）
5. **自由度需按任务风险控制** — 高风险操作（迁移/部署/删文件）收紧自由度，分析/评审类任务可放开

## 核心内容

### SKILL.md 标准结构

```
skill-name/
├── SKILL.md          # 元数据 + 正文（≤500 行）
├── scripts/          # 可执行脚本（不进上下文）
├── references/       # 参考资料（按需加载）
└── assets/           # 模板和静态文件（按需加载）
```

### 元数据关键字段

- **name**：小写字母+数字+连字符，≤64 字符，动名词形式
- **description**：写清楚"做什么 + 什么时候用"，含触发词

### 三大自由度级别

| 自由度 | 适合场景 | 写法 |
|--------|----------|------|
| 高 | 需要判断和取舍 | 给检查方向，不写死步骤 |
| 中 | 有固定模板但允许调整 | 给模板、参数和边界 |
| 低 | 操作脆弱，出错代价高 | 给精确命令，明确不能改 |

### 写 Skill 的 8 个常见坑

1. 把 Skill 当项目 README 写 — 不是写给人看的科普文
2. 想写得太全 — Skill 不怕小，怕边界不清楚
3. 给 Agent 太多选择 — 先给默认方案，再给兜底
4. 术语来回换 — 同一概念只用同一名称
5. 让 LLM 做确定性工作 — 格式转换/精确计算交给脚本
6. description 写得太虚 — 直接影响触发准确率
7. 没有验证点 — 复杂任务要有中间检查
8. 第三方 Skill 不审直接用 — SKILL.md 也是指令，可能夹带不安全操作

## 与现有知识的关系

- 与 [[wiki/sources/llm-skills-technical-guide]] 中 MCP vs Skills 的对比互补，本文深入 SKILL.md 设计细节
- 与 [[wiki/sources/skills-tutorial]] 菜鸟教程 Skills 内容一致但深入得多
- 与 [[wiki/concepts/agent-skills-system]] 高度相关，为其提供了丰富的实践素材

## 受影响的 Wiki 页面

- [[wiki/concepts/agent-skills-system]] — 已补充新来源引用
- [[wiki/concepts/mcp-model-context-protocol]] — 已补充 Skills vs MCP 对比来源
