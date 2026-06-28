---
title: "Spec-driven development with AI — GitHub Spec Kit 官方博客"
tags:
  - source
  - spec-driven
  - active
created: 2026-06-29
updated: 2026-06-29
source_url: "https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/"
source_author: "Den Delimarsky (GitHub)"
source_date: 2025-09-03
aliases:
  - GitHub Spec Kit Announcement
---

# Spec-driven development with AI — GitHub Spec Kit 官方博客

> GitHub 官方宣布 Spec Kit 开源工具包的博客文章。Den Delimarsky 阐述了 Spec Kit 的设计理念：将 spec 视为活的、可执行的工作，随项目演化。Spec Kit 支持 GitHub Copilot、Claude Code、Gemini CLI 等多种编码代理。

## 核心论点

1. **问题本质**：编码代理的问题不在于编码能力，而在于我们的方法——把编码代理当搜索引擎用，而它们更像是"字面意义上的结对程序员"。

2. **Spec Kit 四阶段**：
   - **Specify**：描述"构建什么、为什么"，AI 生成详细规范（用户旅程、体验、成功标准）
   - **Plan**：提供技术栈、架构和约束，AI 生成技术计划（可请求多方案对比）
   - **Tasks**：AI 将规范和计划拆分为可独立实现和测试的小块
   - **Implement**：AI 逐个（或并行）处理任务，开发者的角色是验证而非滚动千行代码

3. **核心洞察**：每个阶段都有明确的检查点，不通过不可进入下一阶段。开发者的角色不仅是引导（steer），更是验证（verify）——AI 生成工件，你确保它们正确。

4. **最佳场景**：
   - 绿地项目（zero-to-one）：前期少量工作确保 AI 构建你真正想要的
   - 存量功能扩展（N-to-N+1）：最强大的场景——通过 Spec 明确与现有系统的交互方式
   - 遗留系统现代化：捕获业务逻辑到现代 Spec，让 AI 重建底层系统

5. **未来方向**：从"代码是真相源"到"意图是真相源"。Spec 变成可执行的真相信，决定构建什么。

## 受影响的 Wiki 页面

- [[wiki/concepts/spec-driven-development]] — 新增 Spec Kit 设计理念详解
