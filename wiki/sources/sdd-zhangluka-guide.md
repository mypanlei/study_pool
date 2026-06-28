---
title: "SDD 落地实践指南 — zhangluka"
tags:
  - source
  - spec-driven
  - methodology
  - enterprise
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://github.com/zhangluka/SDD"
source_author: "zhangluka"
source_date: 2026-06
aliases:
  - SDD Enterprise Adoption Guide
  - zhangluka SDD
---

# SDD 落地实践指南 — zhangluka

> GitHub 仓库 `zhangluka/SDD` 发布的面向多团队 + 传统开发模式（BA Word 需求 + 设计评审 + 测试交付）的 SDD 落地实践指南。核心贡献在于给出了在企业组织上下文（非绿地、非 Agent-first 环境）中逐步引入 SDD 的具体路径。

## 核心论点

1. **SDD 定位**：不是 SDLC 中的某个孤立阶段，而是覆盖"从需求到运维全流程"的软件工程范式。核心起点在"需求分析收尾之后、编码开始之前"。

2. **六个生命周期阶段**：Specify（规格定义）→ Plan（方案规划）→ Tasks（任务拆解）→ Implement（实现与验证）→ Deliver（交付与集成）→ Iterate（迭代与运维）。

3. **七大设计理念**：
   - 规范 = 全流程唯一真相源
   - 契约先行（先定义做什么/不做什么、成功/失败标准、边界与异常）
   - 规范可执行、可验证、机器可读
   - 全角色协同共识（产品/BA/开发/测试/运维/安全共同参与规格评审）
   - 风险左移（在规格阶段解决歧义）
   - 规范是核心资产，代码是衍生物
   - 全生命周期闭环（任何修改先更新规范）

4. **企业落地四步法**：
   - 第 1 步：试点项目——选需求边界清晰的项目，在"BA Word + 需求澄清"后增加规格编写+评审环节
   - 第 2 步：规范与设计/代码绑定——设计评审增加"是否覆盖规格全部 AC"检查
   - 第 3 步：规范作为交付与结项依据——用户验收以规格的验收条件为清单
   - 第 4 步：逐步机器可读与自动化——稳定后再升级 YAML/JSON 结构

5. **工具选型建议**：优先采用 Spec-Kit（主用 Claude Code 时可选 Speck），需要强契约时可结合 OpenSpec 补充。

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — 新增企业落地六阶段模型、四步推进法、七大设计理念
