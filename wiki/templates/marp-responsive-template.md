---
marp: true
---

<!--
Marp 演示文稿模板 — 使用说明

1. 复制此文件作为新演示文稿的起点
2. 在 <style> 块中调整字号（所有值必须加 !important）
3. 每页只放一个核心点，大表格/Mermaid 图单独一页
4. 导出: VS Code 中 Ctrl+Shift+P → Marp: Export Slide Deck
-->

<style>
/*
 * Marp CSS 规则
 *
 * 注意：Marp 内置主题样式优先级高，所有 CSS 必须加 !important
 * vw/clamp() 在 Marp 中不可靠，统一用固定 px
 */
section { font-size: 20px !important; padding: 40px !important; line-height: 1.5 !important; }
h1 { font-size: 36px !important; margin: 0 0 12px 0 !important; }
h2 { font-size: 28px !important; margin: 0 0 10px 0 !important; }
h3 { font-size: 22px !important; margin: 0 0 8px 0 !important; }
p { font-size: 18px !important; margin: 4px 0 !important; }
li { font-size: 17px !important; margin: 2px 0 !important; }
blockquote { font-size: 18px !important; margin: 6px 0 !important; padding: 6px 16px !important; }
table { font-size: 14px !important; width: 100% !important; }
table th, table td { padding: 3px 8px !important; }
code { font-size: 13px !important; }
pre { font-size: 13px !important; margin: 6px 0 !important; }
.mermaid { font-size: 14px !important; }
section.lead { justify-content: center !important; align-items: center !important; text-align: center !important; }
section.lead h1 { font-size: 42px !important; }
section.lead h2 { font-size: 30px !important; }
ul, ol { margin: 4px 0 !important; padding-left: 24px !important; }
</style>
