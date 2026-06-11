---
title: "Claudian 安装教程：把 Claude Code 接进 Obsidian，从 0 到侧边栏对话"
source: "https://zhuanlan.zhihu.com/p/2027903175898744570"
author:
  - "[[小墨同学爱写程序的小鱼]]"
published:
created: 2026-06-11
description: "在很多人看来使用CLI还是有一定难度的，或者在编辑文案内容的时候很不方便，需要来回切换文章和CLI命令行，我这篇要做的事很直接：Obsidian 左边多一个机器人图标，点开之后在侧边栏发一句话，Claude 直接把内容写…"
tags:
  - "clippings"
---
8 人赞同了该文章

在很多人看来使用CLI还是有一定难度的，或者在编辑文案内容的时候很不方便，需要来回切换文章和CLI命令行，我这篇要做的事很直接： [Obsidian](https://zhida.zhihu.com/search?content_id=273182441&content_type=Article&match_order=1&q=Obsidian&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODEzMTkyMDgsInEiOiJPYnNpZGlhbiIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3MzE4MjQ0MSwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.2QWHP_zvlGfgOSFwKWCfbZQL4JC79yTe0_N-JhxzZ6Q&zhida_source=entity) 左边多一个机器人图标，点开之后在侧边栏发一句话，Claude 直接把内容写进笔记。不切屏，不开终端让AI模型和Obsidian融为一体。

我自己也是Obsidian 高强度的使用者。但是在文学创作的时候Claude code和Obsidian来回切换让我痛苦不堪，最后我找到了这个 `Claudian` 可以完美的解决我的问题，这里我也把我自己的踩坑和安装总结成了这篇文章。

---

## Obsidian的安装

第一步：下载Obsidian

![](https://picx.zhimg.com/v2-f523df1f493b47f0f753481b31f07889_1440w.jpg)

> 下载地址： [obsidian.md/download](https://link.zhihu.com/?target=https%3A//obsidian.md/download)

第二步：创建仓库

![](https://pica.zhimg.com/v2-8b1bd0ddf826c39e66a05fcb18f325ae_1440w.jpg)

## 第二步：用 BRAT 装 Claudian，把 CLI 路径填进去

因为Claudian 还没进官方插件市场，所以我们需要通过 BRAT 装。BRAT 是 Obsidian 社区专门装 beta 插件的工具，非常的安全和高效。

第一步：先开 Obsidian 第三方插件：设置 → 第三方插件 → 关掉安全模式

![](https://pic3.zhimg.com/v2-9c9d68630c7eb979e4e2f1cd2c54e2fc_1440w.jpg)

第二步：搜索BRAT插件（启用插件）

![](https://picx.zhimg.com/v2-5422d4932cbe9c6a36a9453d2f3b9c3f_1440w.jpg)

然后用 BRAT 拉 Claudian：左侧列表进 BRAT → `Add beta plugin` → 粘这个地址：

```
https://github.com/YishenTu/claudian
```
![](https://pic2.zhimg.com/v2-68081681d720e3b07aee47e8817a7a0d_1440w.jpg)

等它装完。回设置页，左侧多出 `Claudian` ，点进去：

1. 语言切中文
2. 找到 `Claude CLI 路径` ，粘上第一步复制的完整路径
3. 粘完 Claudian 会自动探测一次，没报错就往下走
![](https://pica.zhimg.com/v2-5e7da65382b7fd783b7a6925cbb3b272_1440w.jpg)

这一步之后，分成两条路：订阅路径和反代。

**订阅路径** ：不用再改。第一次发消息时 Claude Code 可能弹一个登录链接，跟着走，跟claude code都是一样的使用方式，如果你一个登入授权过就不需要管了。

**反代/中转路径** ：在 Claudian 设置里找到"自定义环境变量"这一块（字样以你装的版本为准），追加两条：

```
ANTHROPIC_API_KEY=你中转站的 key
ANTHROPIC_BASE_URL=你中转站的地址
```

`ANTHROPIC_BASE_URL` 是接口根路径，不是登录页地址，别粘错。中转站控制台的"API 接入"那栏一般能找到。

如果是使用nvm安装的node环境的需要注意CLI命令的路径，默认使用的是用户的命令行窗口，但是如果你有多个node环境可以会导致出现错误。

![](https://pic1.zhimg.com/v2-2e39eb862d359d4546e708664ecff126_1440w.jpg)

> 延伸阅读：对"反代/中转到底怎么配"没概念的，先看： [Claude Code 在大陆怎么稳定用：我用 cc-switch 接 MiniMax 跑通了一套替代方案](https://link.zhihu.com/?target=https%3A//www.legacyvps.com/archives/claude-code-minimax-cc-switch-guide)

---

## 第三步：测试使用Claudian

关掉设置页，看 Obsidian 左边功能区那一竖排图标——应该多出一个机器人。

没看到的话：

- 第三方插件列表里确认 `Claudian` 开关是开的
- BRAT 里看 Claudian 还在不在列表，不在就重新 `Add beta plugin`

点机器人图标，右边弹侧边栏。输入框里发一句最轻的：

```
你是谁
```

几秒内应该开始流式输出回复。看到回复就算跑通。

跑不通的三种画面：

- **一直 loading** ：CLI 路径对，但 Claude Code 跑不起来
- **红色报错** ：多半是 `Claude CLI not found`
- **什么都没动** ：Claudian 没启用，或者你点的不是机器人图标
![](https://pic2.zhimg.com/v2-fe1465fa17db090115b92bcb6a1ffdbd_1440w.jpg)

## 两个最容易卡的报错

现象：侧边栏一发消息就弹红字 `Claude CLI not found` 。

定位：

1. 终端重新敲 `which claude` 。返回空就是 CLI 没装上，回第一步
2. 返回路径就完整复制——小心别带多余空格或换行
3. Claudian 设置 → 高级 → `Claude CLI 路径` ，粘进去覆盖
4. 关设置页，再发一次"你是谁"

### npm CLI 和 Node.js 不在同一目录

现象：路径填得一字不差还是找不到 `claude` 。用 nvm、volta、fnm 的人最容易踩， `claude` 和 node 可能不在同一个目录，Claudian 启动子进程时 PATH 里只有其中一个。

先对比：

```
dirname $(which claude)
dirname $(which node)
```

两条一样就不是这个问题。不一样就是。

两种解法：

**A. Claudian 设置里把 Node 目录也加进 PATH**

高级 → 环境变量 → 找到 `PATH` ，把 `dirname $(which node)` 的目录用冒号追加进去，原内容不动。重启 Obsidian。

**B. 装 Claude Code 原生二进制，绕开版本管理器**

去 Anthropic 官方下载对应系统的原生二进制，装完 `which claude` 会指向系统级目录（比如 `/usr/local/bin/claude` ），和 Node 无关。Claudian 里重填新路径。

---

## Codex 部署

Claudian 其实也同时支持 Codex 作为后端，但官方仓库写着还是 beta状态，跨平台还在验证阶段不稳定。我自己测试过能跑没问题，但是还是有优化的空间。

但是大体的思路都是一样的：装好 Codex CLI，Claudian 里把 provider 切成 Codex，CLI 路径换成 Codex 的可执行文件。报错排查套路基本一致。等 Claudian 把 beta 摘掉我再回来补一篇专门讲 Codex 的。

---

## 写在最后

三条路，我的排序很明确：

- **能开订阅就开订阅** 。Claudian 填个 CLI 路径就完事，不用碰 Base URL，稳定性也是三条里最好的。能花钱解决的事别折腾
- **开不了就走反代** 。配置本身十分钟能搞定，但出问题的时候你得能分清是 Claudian 挂了还是中转站挂了，这个判断力比配置本身重要
- **Codex 先不急** 。beta 阶段能跑但不够稳，等 GA 再说

到这里，Claudian 装完、侧边栏能对话，安装这件事就算结束了。但装上只是把路打通——斜杠命令怎么用、@提及笔记怎么喂上下文、计划模式怎么拆任务，这些才决定它到底是个聊天框还是你的写作搭档。下一篇再讲。

编辑于 2026-04-16 00:18・广东