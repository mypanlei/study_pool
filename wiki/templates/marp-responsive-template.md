---
marp: true
---

<!--
此模板使用 viewport 相对单位（vw/vh/clamp）实现自适应缩放。
窗口变大 → 字号自动变大；窗口变小 → 字号自动缩小。
复制此文件作为新演示文稿的起点。
-->

<style>
/*
 * Marp 自适应 CSS 规则 — 直接复制到任何 Marp 文件中使用
 *
 * 核心原理：vw（视口宽度）/ vh（视口高度）单位
 * - 窗口越大字越大，窗口越小字越小，始终铺满屏幕
 * - clamp(MIN, PREFERRED, MAX) 确保不超出边界
 * - 在 Obsidian 侧边栏预览和全屏演示时自动适配
 */
section {
  font-size: clamp(12px, 1.6vw, 24px);
  height: 100svh; min-height: 100svh;
  padding: 5vh 5vw;
  display: flex; flex-direction: column;
  justify-content: flex-start;
  overflow: auto; line-height: 1.4;
}
h1 { font-size: clamp(22px, 3vw, 44px); margin: 0 0 0.4em 0; }
h2 { font-size: clamp(18px, 2.2vw, 32px); margin: 0 0 0.3em 0; }
h3 { font-size: clamp(15px, 1.8vw, 26px); margin: 0 0 0.2em 0; }
p { font-size: clamp(11px, 1.4vw, 20px); margin: 0.15em 0; }
li { font-size: clamp(11px, 1.3vw, 19px); margin: 0.1em 0; }
blockquote { font-size: clamp(11px, 1.4vw, 20px); margin: 0.2em 0; padding: 0.2em 1em; }
table { font-size: clamp(9px, 1.1vw, 16px); width: 100%; }
table th, table td { padding: 0.15em 0.5em; }
code { font-size: clamp(8px, 1vw, 14px); }
pre { font-size: clamp(8px, 1vw, 14px); margin: 0.2em 0; line-height: 1.3; }
.mermaid { font-size: clamp(9px, 1.2vw, 16px); }
section.lead { justify-content: center; align-items: center; text-align: center; }
section.lead h1 { font-size: clamp(28px, 4vw, 56px); }
section.lead h2 { font-size: clamp(20px, 2.6vw, 36px); }
ul, ol { margin: 0.15em 0; padding-left: 1.5em; }
</style>
