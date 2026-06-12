---
title: "skill 的管理方法"
source: "https://zhuanlan.zhihu.com/p/2025963062037868570"
author:
  - "[[空格的键盘AI产品和开发丨公号：空格的键盘]]"
published:
created: 2026-06-13
description: "最近，每次换家里电脑，打开 Cursor，准备干活。 敲一句\"帮我写个选题\"，AI 回了一段毫无灵魂的通用输出。愣了两秒才反应过来：这台电脑上没有我的 Skill。 我有 130 多个 Skill，，选题的、写作的、画图…"
tags:
  - "clippings"
---
15 人赞同了该文章

最近，每次换家里电脑，打开 [Cursor](https://zhida.zhihu.com/search?content_id=272868020&content_type=Article&match_order=1&q=Cursor&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODE0NTg0ODMsInEiOiJDdXJzb3IiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzI4NjgwMjAsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.QBIr7Us5P568YtxwY9NFKmGYg9H7S7Ak5egX7z6y7VI&zhida_source=entity) ，准备干活。  
敲一句"帮我写个选题"，AI 回了一段毫无灵魂的通用输出。愣了两秒才反应过来：这台电脑上没有我的 Skill。  
我有 130 多个 Skill，，选题的、写作的、画图的、做 PRD 的、爬 RSS 的，全在公司电脑的文件夹里躺着。换了工具、换了电脑就没法用了  
还有一个场景是，给别人分享 Skill 时，写作的、画图的、飞书的、产品的混成一锅粥。自己都看不懂，更不用想分享给其他人了。  
最大的问题 是我的 [Obsidian](https://zhida.zhihu.com/search?content_id=272868020&content_type=Article&match_order=1&q=Obsidian&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODE0NTg0ODMsInEiOiJPYnNpZGlhbiIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3Mjg2ODAyMCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.mYPKwLoEX7-znk9QdBYPNM4pYpegDQggv7vZ84ME-t0&zhida_source=entity) 知识库已经 100 多 GB 了。 [GitHub](https://zhida.zhihu.com/search?content_id=272868020&content_type=Article&match_order=1&q=GitHub&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODE0NTg0ODMsInEiOiJHaXRIdWIiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzI4NjgwMjAsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.URmAdHxcJ8yW6Zj8uxFnnc4kHAqzBCga9uNgEUu4u9g&zhida_source=entity) 推不上去，换台电脑知识库就断了。  
总结一下这四个问题就是：  
**1 跨文件夹/工具调不到：** Cursor 打开项目 A，里面的 Skill 跑得飞起。切到项目 B，同样的 Skill 不存在。 [Codex](https://zhida.zhihu.com/search?content_id=272868020&content_type=Article&match_order=1&q=Codex&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODE0NTg0ODMsInEiOiJDb2RleCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3Mjg2ODAyMCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.7_7b_uD5uP7SR7Yn13_dCs_0ieQb4QZI2ZapWkccmFo&zhida_source=entity) 那边又是另一套。改了 A 里的 Skill 忘了同步 B，两边版本不一致，输出质量忽高忽低，排查半天才发现是 Skill 版本的问题。  
**2 跨电脑用不了：** 公司电脑一套 Skill，家里电脑一套。出差用笔记本，又是一套残缺版。每次换设备都要手动拷贝，拷完发现漏了几个，或者拷的是旧版本。  
**3 分享出去很乱：** 有人问我要"写作类的 Skill"，我打开文件夹一看：ai-writing-assistant、blog-post-writer、content-digest、topic-agent、x-post，分散在 130 个目录里，没有分类，没有索引。每次分享都要手动挑，挑完还要解释每个是干嘛的。  
**4 知识库同步不了：** Obsidian 仓库越来越大，几百篇文章、几千条素材、大量图片。GitHub 有文件大小限制， [NAS](https://zhida.zhihu.com/search?content_id=272868020&content_type=Article&match_order=1&q=NAS&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODE0NTg0ODMsInEiOiJOQVMiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzI4NjgwMjAsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.f1N66OLV_aUd8ld4tPusfX6pPsxkbOp7Mde4Yc5kcr8&zhida_source=entity) 同步要手动操作。换台电脑，知识库就断了，AI 读不到历史上下文，等于失忆。  
这四个问题折腾了我两个月，最后摸索出一套方案。不复杂，就四句话。  
**01 四个方法，四层互通**  
**第一：跨文件夹互通 = 全局目录 + 软链接**  
所有 Skill 只存一个地方：~/.claude/skills/。  
这是全局唯一来源，Single Source of Truth。不管打开哪个项目，不管用 Cursor 还是 Codex 还是 OpenClaw，都从这一个目录读取 Skill。  
怎么让每个项目都能调用？软链接。  
obsidian/.claude/skills → ~/.claude/skills (symlink)复制  
一行命令搞定。打开 Obsidian 项目，自动能调用全部 130 个 Skill。打开另一个项目，加一条 symlink，也能调用。改了某个 Skill？只需要改全局目录，所有项目同时生效。  
不再有"项目 A 有但项目 B 没有"的问题，不再有版本不一致的问题。  
对于这个操作也很简单，让你的 claudecode、cursor 来执行：  
**根据.claude/skills 创建软链接到 【目标文件夹位置】**  
  
**第二：跨电脑互通 = [GitHub 私密仓库](https://zhida.zhihu.com/search?content_id=272868020&content_type=Article&match_order=1&q=GitHub+%E7%A7%81%E5%AF%86%E4%BB%93%E5%BA%93&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODE0NTg0ODMsInEiOiJHaXRIdWIg56eB5a-G5LuT5bqTIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjcyODY4MDIwLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.3DzRX3N5Buq3Xp_4DXu_NoVZZB1JiIczk0G3qn-ufc0&zhida_source=entity)**  
全局目录解决了本地问题，但换台电脑还是得重新来。  
解法很直接：把 ~/.claude/skills/ 全量推到一个 GitHub 私密仓库。  
~/.claude/skills/ → [github.com/zephyrwang6/](https://link.zhihu.com/?target=http%3A//github.com/zephyrwang6/allSkills) (private)复制  
新电脑到手，git clone 一行命令，130 个 Skill 全部恢复。Private 仓库，只有自己能看到，不怕泄露。  
这里建议大家使用 github 的 CLI，可以实现本地命令行登录和增删改查 github 仓库。  
下载完成后，直接用 https 认证登录，然后就可以指挥 AI 来新增仓库，和本地文件同步。  
丝滑流畅。  
**第三：跨网络分享 = 分类 + GitHub 公开仓库**  
全量仓库是给自己备份的，分享给别人不能甩 130 个过去。  
我把 Skill 按领域拆成了四个公开仓库：

| 仓库 | 领域 | 数量 |
| --- | --- | --- |
| write-skill | 写作 / 内容生产 | 21 个 |
| draw-skill | 画图 / 设计 / 视觉 | 13 个 |
| info-skill | 信息获取 / RSS / 爬虫 | 14 个 |
| protodesign | 产品 / PM / 原型 | 13 个 |

要分享写作类的 Skill，给他 write-skill 的链接就行。要画图的？draw-skill。干干净净，不用翻。  
分类的规则也很简单：按 Skill 名称和功能描述自动判断归属。写作相关的关键词（article、topic、content、blog）归写作类，画图相关的（image、cover、infographic、illustration）归画图类，以此类推。  
**第四：跨设备知识库同步 = NAS + rsync**  
GitHub 解决了 Skill 的同步，但知识库太大，推不上去。  
我的方案是用 NAS 做中转。写了一个 rsync 脚本，每天下午 6 点自动把本地 Obsidian 仓库同步到 NAS：  
本地 obsidian/ → 极空间 NFS /obsidian/ (每天 18:00 自动)复制  
脚本会自动检测 NAS 是否在线，离线就跳过，不会卡死。排除了.git/、.trash/、node\_modules/ 这些不需要同步的目录。  
家里的电脑、公司的电脑，都能通过 NAS 访问同一份知识库。AI 读取的上下文永远是最新的。  
**02 用一个 Skill 管理所有 Skill**  
方案有了，但每次手动执行这些操作还是麻烦。扫描新增的 Skill、判断归类、复制到分类仓库、全量同步、推送 GitHub...步骤不少。  
所以我做了一个" Skill"：skill-manage。  
说"整理 Skill"，AI 就知道该干什么：  
1 扫描全局目录，找出最近新增的 Skill  
2 按分类规则自动判断归属（写作/画图/信息获取/PM）  
3 复制到对应的分类仓库  
4 全量同步到 allSkills 私密仓库  
5 依次对所有仓库执行 git commit + push  
6 可选：触发一次 NAS 同步  
一句话触发，全流程自动化。  
不只是用 AI 干活，而是用 AI 管理 AI 的能力。Skill 管理 Skill，系统自我维护。  
**03 我的 Skill 库，全部公开**  
既然做了分类，公开出来就更容易让大家使用了。这是我目前在用的四个分类仓库：  
**1 写作类：write-skill**  
地址： [github.com/zephyrwang6/](https://link.zhihu.com/?target=http%3A//github.com/zephyrwang6/write-skill)  
21 个 Skill，覆盖内容创作全流程：

- ai-writing-assistant — 6 种写作方法引导，从对话式创作到素材整合
- topic-agent — 选题系统，从热点采集到选题审核全自动
- blog-post-writer — 零散想法转公众号文章
- x-post — 长文改写成即刻/X 动态
- content-digest — 长内容（播客、视频、文章）提炼成短内容
- doc-coauthoring — 结构化协作写作，从大纲到终稿

**2 画图类：draw-skill**  
地址： [github.com/zephyrwang6/](https://link.zhihu.com/?target=http%3A//github.com/zephyrwang6/draw-skill)  
13 个 Skill，解决"AI 配图"这件事：

- baoyu-image-gen — 多 API 统一调用（OpenAI / Google / DashScope）
- baoyu-cover-image — 文章封面图生成，5 维度组合（类型×色板×渲染×文字×情绪）
- baoyu-infographic — 信息图生成，20 种布局 × 17 种风格
- article-batch-illustration — 分析文章结构，批量生成段落配图
- logo-batch-generator — 品牌 Logo 批量生成
- storyboard-generator — 故事分镜脚本 + 配图

**3 信息获取类：info-skill**  
地址： [github.com/zephyrwang6/](https://link.zhihu.com/?target=http%3A//github.com/zephyrwang6/info-skill)  
14 个 Skill，把散落各处的信息收回来：

- rss-aggregator — RSS 聚合，定时获取关注源的最新内容
- youtube-feed — YouTube 博主更新监控
- youtube-transcript-cn — 提取 YouTube 视频字幕转中文文字稿
- web-scraper — 网页内容抓取转 Markdown
- baoyu-danger-x-to-markdown — X/Twitter 推文保存为 Markdown
- podcast-workflow — 播客处理一站式：字幕提取 → 摘要 → 存档

**4 产品经理类：protodesign**  
地址： [github.com/zephyrwang6/](https://link.zhihu.com/?target=http%3A//github.com/zephyrwang6/protodesign)  
13 个 Skill，产品经理的工具箱：

- pm-prd-writer — 模糊需求转 PRD
- pm-analytics — 数据分析 + 可视化报告
- pm-experiment-designer — A/B 实验方案设计
- pm-competitor-deconstructor — 竞品四维拆解（策略/功能/体验/增长）
- pm-roadmap-planner — 版本路线图规划
- pm-image2proto — 截图复刻成 HTML 原型

这些仓库都是 public 的，直接 clone 就能用。  
**04 最后**  
刚开始搭 AI 生产力系统的时候，核心理念是"上下文优先于提示词"。Skill 的创建是在封装上下文，Skill 的管理其实也是。  
全局目录是上下文的单一来源。软链接是上下文的分发通道。GitHub 是上下文的持久化。NAS 是上下文的多端同步。skill-manage 是上下文的自动化维护。  
绕了一圈，管理 Skill 这件事本身，就是一次上下文工程的实践。  
130 个 Skill 说到底是我个人场景下打磨出来的，未必适合所有人。但如果能让一些正在搭建自己 AI 系统的人少走几步弯路，省下几个晚上的折腾时间，那就值了。

编辑于 2026-04-10 15:47・广东